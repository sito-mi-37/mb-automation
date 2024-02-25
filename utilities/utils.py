import inspect
import logging
import softest


class Utils(softest.TestCase):

    def custom_logger(logLevel=logging.DEBUG):
        # set_class/method name from where its called
        logger_name = inspect.stack()[1][3]
        # create logger
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        # create console handler or file handler and set the log level
        fh = logging.FileHandler("automation.log")
        # create formatter - How you want your logs to be formatted
        formatter = logging.Formatter("%(levelname)s|%(filename)s:%(lineno)d|%(asctime)s|%(message)s")
        # add formatter to console or file handler
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        return logger