from masonite.listeners import BaseExceptionListener
from .Logger import Logger

class LoggerExceptionListener(BaseExceptionListener):

    listens = ['*']

    def __init__(self, logger: Logger):
        self.logger = logger

    def handle(self, exception, file, line):
        self.logger.error("{} in {} on line {} \n".format(
            exception.__class__.__name__, 
            file,
            line,
        ), exc_info=True)
