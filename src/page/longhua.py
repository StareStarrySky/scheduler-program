import os

from requests_html import HTMLSession

from bus_log.bus_logger import BusLogger


class Longhua:
    def __init__(self):
        self.logger = BusLogger(__name__).log
        self.res = None

    def req(self):
        session = HTMLSession()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://yuyue.shdc.org.cn/forwardDocInfo.action'
        }
        params = (
            'platformHosId=6'
            '&platformDeptId=3160'
            '&platformDoctorId=6198'
            '&docInfo.hisDoctId=2462'
            '&platformhosno=42502634500'
            '&nextNumInfo=0'
        )
        self.res = session.post(
            'https://yuyue.shdc.org.cn/ajaxSearchOrderNumInfoForComment.action',
            headers=headers,
            params=params
        )

    def reptile(self):
        huiszhou = self.res.html.find('.huiszhou')
        zhou = self.res.html.find('.zhou')
        self.logger.info(str(len(zhou)) + '-' + str(len(huiszhou)))
        for z in zhou:
            if z.text == '星期日':
                key_id = z.element.getparent().attrib.get('id')[3:]
                self.logger.info(key_id)
                os.system('msg * ' + key_id)

    def analysis(self):
        self.req()
        if self.res.status_code == 200 and self.res.text.find('星期日'):
            self.reptile()
        else:
            print('req failed')
