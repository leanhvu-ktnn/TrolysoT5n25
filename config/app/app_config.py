from .. import STREAMLIT_CONFIG, API_CONFIG, MODEL_CONFIG

class AppConfig:
    @staticmethod
    def get_streamlit_config() -> dict:
        return STREAMLIT_CONFIG
    
    @staticmethod
    def get_api_config() -> dict:
        return API_CONFIG
    
    @staticmethod
    def get_model_config() -> dict:
        return MODEL_CONFIG 