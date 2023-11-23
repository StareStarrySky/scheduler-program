import logging


class BusLogger:
    def __init__(self, log_name: str = __name__):
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        self.log = logging.getLogger(log_name)
        self.log.setLevel(logging.INFO)
        self.log.addHandler(handler)

