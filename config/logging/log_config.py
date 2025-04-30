from .. import LOG_CONFIG
import logging

class LogConfig:
    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Lấy logger với cấu hình từ LOG_CONFIG
        
        Args:
            name: Tên logger
            
        Returns:
            Logger instance
        """
        logger = logging.getLogger(name)
        logger.setLevel(LOG_CONFIG["level"])
        
        formatter = logging.Formatter(LOG_CONFIG["format"])
        
        file_handler = logging.FileHandler(LOG_CONFIG["filename"])
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        return logger 