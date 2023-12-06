import os

from bus_log.bus_logger import BusLogger


class TenMinutesBreak:
    def __init__(self):
        self.logger = BusLogger(__name__).log

    def take_a_drink(self):
        os.system('msg * "take a drink~"')
        self.logger.info('take a drink~')
