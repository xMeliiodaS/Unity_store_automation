import logging


class LoggingSetup:
    """
    A class to manage logging configuration for the project.
    """
    logging.basicConfig(
        filename="../unity_store_logfile.log",
        level=logging.INFO,
        format='%(asctime)s : %(levelname)s : %(message)s',
        force=False
    )
    # Suppress logging from 'undetected_chromedriver' to avoid clutter
    logging.getLogger('undetected_chromedriver').setLevel(logging.WARNING)
