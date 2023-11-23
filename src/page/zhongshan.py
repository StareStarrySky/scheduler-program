import os

from requests_html import HTMLSession

from bus_log.bus_logger import BusLogger


class Zhongshan:
    def __init__(self):
        self.logger = BusLogger(__name__).log
        self.res = None

    def req(self):
        session = HTMLSession()
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://yuyue.shdc.org.cn/searchOrderNumInfoAction.action'
        }
        params = ('platformHosId=49'
                  '&platformDeptId=UUjjFFyyZZnnRRZZTTjjBB00TTjjRRSSYYTTQQxxNNDDFFkkRR00JJvvQQTT0099'
                  '&deptdesc=OOTTccxxbb11ppDDdd33hhSSddnnBB33VV11BBVVSSEEZZMMTTUUVVDDUUTT0099'
                  '&docInfo.hisDoctId=NNjjddBBTTFFhhUURRHHhhaaVVnnVVwwOOUU11iiccFFIIrreellFFCCddzz0099'
                  '&visitLevelCode=YYiittyyWWXXNNCCUUjjgg33LL00xxrreeTTllJJZZEEFFLLeeDDNNJJddzz0099'
                  '&platformhosno=aallRRCCNNDDJJKKTT33llBBccHHBBSSeeFFQQ33TTTTAA55eeCCttOOUUTT0099'
                  '&nextNumInfo=0'
                  '&key=aaHHddVVYYXXVV44aaXXZZIIRR33ZZ44ddHHAArraaFFAAzzYYllRRkkUUkkoowwZZmm55IIQQXXpphhZZGGFFXXUUDDFF'
                  'WWYYllFFvvccFFZZRRaaUUhhzzTTUUFFaaMMFFhhNNTTkkJJHHTTkk99DDWWVVllSSNNGGNNVVSSHHVVwwccWWJJrrZZ00EE33cc'
                  'zzhhwwaaDDNNXXSSllJJEENNGGllSSQQnnYY11OOCC9955NNHHBBEEZZFFddkkbb33ZZzzRRWWZZmmaaWW99uuSSEEhhjjUU00NN'
                  '44RRzzBBrrQQkkddZZTTVVFFrrZZ33hh66aakk11yyUUnnZZ22eeEE99VVQQUUZZaaZZDDRR22dd0099XXddFFBBJJWWllNNllcc'
                  'EEFFssOODDUU33RRGGllttKKyy99nnWWnnYYvvaa11oorrcc11ZZNNNN22II00PPQQ===='
                  '&parentDeptID=ddkkVVmmVVEEllOOZZ11BBBBZZUUNNOOZZ2299XXbbllMM55ZZTTZZNNZZzz0099')
        self.res = session.post(
            'https://yuyue.shdc.org.cn/ajaxSearchOrderNumInfoZB.action',
            headers=headers,
            params=params
        )

    def reptile(self):
        huiszhou = self.res.html.find('.huiszhou')
        zhou = self.res.html.find('.zhou')
        self.logger.info(str(len(zhou)) + '-' + str(len(huiszhou)))
        for z in zhou:
            if z.text == '星期五':
                key_id = z.element.getparent().attrib.get('id')[3:]
                self.logger.info(key_id)
                os.system('msg * ' + key_id)

    def analysis(self):
        self.req()
        if self.res.status_code == 200 and self.res.text.find('星期五'):
            self.reptile()
        else:
            print('req failed')
