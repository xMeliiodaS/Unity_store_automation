import logging


class LoggingSetup:
    """
    A class to manage logging configuration for the project.
    """
    logging.basicConfig(
        filename="../solar_logfile.log",
        level=logging.INFO,
        format='%(asctime)s : %(levelname)s : %(message)s',
        force=True
    )
    # Suppress logging from 'undetected_chromedriver' to avoid clutter
    logging.getLogger('undetected_chromedriver').setLevel(logging.WARNING)
