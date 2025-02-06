from setuptools import setup, find_packages

setup(
    name="code_generator",
    version="0.2.0",
    description="A tool to generate and analyze Python code using Groq API.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "groq",
        "ast",  # Part of Python standard library
    ],
    entry_points={
        "console_scripts": [
            "code-generator=code_generator.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    keywords="code generation, code analysis, groq, ast",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/code_generator/issues",
        "Source": "https://github.com/yourusername/code_generator",
    },
    long_description="""
    Code Generator and Analyzer
    ==========================
    
    A Python package that provides two main functionalities:
    
    1. Code Generation: Generate Python code from natural language suggestions using the Groq API
    2. Code Analysis: Analyze Python code files for metrics, complexity, and best practices
    
    Features:
    - Generate Python code from text descriptions
    - Analyze code structure and complexity
    - Generate detailed markdown reports
    - Command-line interface for both generation and analysis
    """,
    long_description_content_type="text/markdown",
)
