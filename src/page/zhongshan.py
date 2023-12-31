import os

from requests_html import HTMLSession

from bus_log.bus_logger import BusLogger
from page import shdc
from util.encrypt import Encrypt


class Zhongshan:
    def __init__(self):
        self.logger = BusLogger(__name__).log
        self.domain = shdc.domain
        self.base_url = shdc.base_url
        self.encrypt = Encrypt(shdc.public_key)
        self.res = None

    def req(self):
        header_r = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'yuyue.shdc.org.cn',
            'Referer': 'https://yuyue.shdc.org.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/110.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"'
        }
        header_p = {
            'Client': '30FAD44254F142A999933EE2981F6F15',
            'Version': '2.6',
            'Access-Token': '',
            'Signature': self.encrypt.generate_unique_encrypt()
        }
        headers = {**header_r, **header_p}

        # sequence:
        # "hosDeptCode=7205&topHosDeptCode=03&registerType=2&doctName=高血压门诊&platformHosNo=42500506900&hosOrgCode=42500506900"
        data = {
            'hosDeptCode': '7205',
            'topHosDeptCode': '03',
            'registerType': '2',
            'doctName': '高血压门诊',
            # 'platformHosNo': '42500506900', # code: 484
            'hosOrgCode': '42500506900'
        }
        param = ''
        for k in data:
            v = data[k]
            param += '&' + k + '=' + v
        session = HTMLSession()

        # {"code":200,"data":{"diseaseSchedules":[]}}
        # {"code": 500, "msg": "就诊类型不能为空"}
        # {"code":500,"msg":"就诊类型错误"}
        # {"code":484,"msg":"请勿重放攻击","errorMsg":"请勿重放攻击"}
        self.res = session.get(
            self.domain + self.base_url + '?' + self.encrypt.encrypt_long(param[1:]),
            headers=headers
        )

    def reptile(self, disease_schedules):
        num = 0
        for disease_schedule in disease_schedules:
            if int(disease_schedule['reserveOrderNum']) > 0 and disease_schedule['weekDays'] == '星期五':
                num += 1

        self.logger.info(str(len(disease_schedules)) + '-' + str(num))

        for disease_schedule in disease_schedules:
            if int(disease_schedule['reserveOrderNum']) > 0 and disease_schedule['weekDays'] == '星期五':
                self.logger.info(disease_schedule['scheduleDate'])
                os.system('msg * ' + disease_schedule['scheduleDate'])

    def analysis(self):
        self.req()
        if self.res.status_code == 200 and 'json' in self.res.headers['Content-Type']:
            data = self.res.json()
            if data['code'] == 200 and 'diseaseVo' in data['data'].keys() and len(data['data']['diseaseSchedules']) > 0:
                self.reptile(data['data']['diseaseSchedules'])
        else:
            self.logger.error('请求失败')
