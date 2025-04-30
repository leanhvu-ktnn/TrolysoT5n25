from .. import (
    TVPL_DB_PATH, MEM_DB_PATH, CHAT_DB_PATH,
    DB_CONFIG
)

class DatabaseConfig:
    @staticmethod
    def get_tvpl_db_path() -> str:
        return TVPL_DB_PATH
    
    @staticmethod
    def get_mem_db_path() -> str:
        return MEM_DB_PATH
    
    @staticmethod
    def get_chat_db_path() -> str:
        return CHAT_DB_PATH
    
    @staticmethod
    def get_db_config() -> dict:
        return DB_CONFIG 