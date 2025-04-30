#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List, Dict, Optional, Any
import httpx
from config import GROQ_API_KEY, MODEL_CONFIG, API_CONFIG
from config.logging import LogConfig
import logging
import asyncio
import os
import json

class BaseAgent:
    """
    Lớp cơ sở cho tất cả các agent trong hệ thống
    """
    
    def __init__(
        self,
        model_name: Optional[str] = None,
        logger: Optional[logging.Logger] = None
    ):
        """
        Khởi tạo BaseAgent
        
        Args:
            model_name: Tên model (mặc định lấy từ config)
            logger: Logger instance
        """
        # Khởi tạo logger nếu chưa có
        if logger is None:
            logger = LogConfig.get_logger(__name__)
            
        # Lấy API key từ config
        self.api_key = GROQ_API_KEY
        if not self.api_key:
            raise ValueError("GROQ_API_KEY không được tìm thấy trong config")
            
        # Lấy cấu hình model từ config
        if model_name is None:
            model_name = MODEL_CONFIG["model"]
            
        # Lưu logger instance và model name
        self.logger = logger
        self.model = model_name
        self.message_history = []
        
    async def _make_request(self, messages: List[Dict[str, str]]) -> str:
        """
        Gửi request đến GROQ API
        
        Args:
            messages: Danh sách các message
            
        Returns:
            Response từ model
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{API_CONFIG['base_url']}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": messages,
                    "temperature": MODEL_CONFIG["temperature"],
                    "max_tokens": MODEL_CONFIG["max_tokens"]
                }
            )
            
            if response.status_code != 200:
                raise Exception(f"Lỗi khi gọi GROQ API: {response.text}")
                
            result = response.json()
            return result["choices"][0]["message"]["content"]
        
    def process_input(self, user_input: str) -> str:
        """
        Xử lý input từ người dùng và trả về response
        
        Args:
            user_input: Input từ người dùng
            
        Returns:
            Response từ agent
        """
        try:
            # Tạo message từ input
            messages = [
                {"role": "system", "content": "Bạn là một trợ lý AI thông minh và hữu ích."},
                {"role": "user", "content": user_input}
            ]
            
            # Thêm lịch sử chat nếu có
            if self.message_history:
                messages = self.message_history + messages
                
            # Chạy agent và lấy kết quả
            response = asyncio.run(self._make_request(messages))
            
            # Lưu lịch sử chat
            self.message_history.extend([
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": response}
            ])
            
            # Trả về nội dung response
            return response
            
        except Exception as e:
            error_msg = f"Lỗi khi xử lý input: {str(e)}"
            self.logger.error(error_msg)
            return error_msg
            
    def get_history(self) -> List[Dict]:
        """
        Lấy lịch sử chat
        
        Returns:
            Danh sách các message trong lịch sử
        """
        return self.message_history
        
    def clear_history(self) -> None:
        """Xóa lịch sử chat"""
        self.message_history.clear()
        
    def get_status(self) -> Dict:
        """
        Lấy trạng thái của agent
        
        Returns:
            Dict chứa thông tin trạng thái
        """
        return {
            "model": self.model,
            "history_length": len(self.message_history)
        } 