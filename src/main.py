from apscheduler.schedulers.blocking import BlockingScheduler

from page.longhua import Longhua
from page.zhongshan import Zhongshan

if __name__ == '__main__':
    longhua = Longhua()
    zhongshan = Zhongshan()

    scheduler = BlockingScheduler()
    scheduler.add_job(longhua.analysis, 'interval', minutes=1, jitter=30)
    scheduler.add_job(zhongshan.analysis, 'interval', minutes=1, jitter=30)
    # scheduler.add_job(longhua.analysis, 'interval', seconds=3)
    scheduler.start()
