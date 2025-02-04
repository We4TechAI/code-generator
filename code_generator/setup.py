# setup.py

from setuptools import setup, find_packages

setup(
    name="code_generator",
    version="0.1.0",
    description="A package to generate code based on suggestions using the Groq API.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # This will find the inner package(s)
    install_requires=[
        "groq",  # Make sure this dependency is available, or adjust accordingly.
    ],
    entry_points={
        "console_scripts": [
            "code-generator=code_generator.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
