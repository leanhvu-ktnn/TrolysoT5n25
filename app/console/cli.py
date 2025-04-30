#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from components.agents.base_agent import BaseAgent
from config.logging import LogConfig
import logging

# Khởi tạo logger
logger = LogConfig.get_logger(__name__)

# Khởi tạo rich console
console = Console()

def main():
    """Hàm chính để chạy vòng lặp chat"""
    try:
        # Khởi tạo BaseAgent
        agent = BaseAgent()
        
        console.print(Panel.fit(
            Text("Chào mừng đến với Trợ lý số!", style="bold green"),
            title="Trợ lý số",
            border_style="blue"
        ))
        console.print("Gõ 'EXIT' để thoát hoặc 'CLEAR' để xóa lịch sử chat\n")
        
        while True:
            # Nhận input từ người dùng
            user_input = Prompt.ask("Bạn")
            
            # Kiểm tra điều kiện thoát
            if user_input.upper() == "EXIT":
                console.print("\n[bold red]Tạm biệt![/bold red]")
                break
                
            # Kiểm tra điều kiện xóa lịch sử
            if user_input.upper() == "CLEAR":
                agent.clear_history()
                console.print("\n[bold yellow]Đã xóa lịch sử chat[/bold yellow]")
                continue
                
            try:
                # Xử lý input và lấy response
                with console.status("[bold green]Đang xử lý...[/bold green]"):
                    response = agent.process_input(user_input)
                    console.print(f"\n[bold blue]Trợ lý:[/bold blue] {response}\n")
                    
            except Exception as e:
                logger.error(f"Lỗi khi xử lý input: {str(e)}")
                console.print(f"\n[bold red]Lỗi:[/bold red] {str(e)}\n")
                
    except Exception as e:
        logger.error(f"Lỗi trong chương trình chính: {str(e)}")
        console.print(f"\n[bold red]Lỗi nghiêm trọng:[/bold red] {str(e)}\n")
        
@click.group()
def cli():
    """CLI cho Trợ lý số"""
    pass

@cli.command()
def chat():
    """Bắt đầu phiên chat với Trợ lý số"""
    main()

if __name__ == "__main__":
    cli() 