import logging

class log_class:
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\test.log",  # Log file path
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
            level=logging.INFO  # Log level
        )
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger