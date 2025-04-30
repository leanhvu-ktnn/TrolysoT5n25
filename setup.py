from setuptools import setup, find_packages

setup(
    name="trolyso",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pydantic>=1.8.0",
        "python-dotenv>=0.19.0",
        "openai>=1.0.0",
        "groq>=0.4.0",
        "streamlit>=1.0.0",
        "pytest>=6.2.5",
        "black>=21.7b0",
        "isort>=5.9.3",
        "flake8>=3.9.2",
        "mypy>=0.910",
        "python-multipart>=0.0.5",
        "httpx>=0.23.0",
        "pyyaml>=5.4.1",
        "loguru>=0.5.3",
        "rich>=14.0.0",
        "pydantic-ai==0.1.8",
        "pydantic-ai-slim==0.1.8"
    ],
    entry_points={
        "console_scripts": [
            "trolyso=app.console.cli:cli"
        ]
    }
) 