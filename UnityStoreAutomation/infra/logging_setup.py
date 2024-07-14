import logging


class LoggingSetup:
    """
    A class to manage logging configuration for the project.
    """
    logging.basicConfig(
        filename="../unity_store_logfile.log",
        level=logging.INFO,
        format='%(asctime)s : %(levelname)s : %(message)s',
        force=True
    )
    # Suppress logging from 'undetected_chromedriver' to avoid clutter
    logging.getLogger('undetected_chromedriver').setLevel(logging.WARNING)


# Create an instance of LoggingSetup to configure logging when this module is imported
logger_setup = LoggingSetup()
