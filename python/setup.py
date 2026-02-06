#!/usr/bin/env python
"""Setup script for OHAP Python SDK"""

from setuptools import setup, find_packages

with open("python/README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ohap-sdk",
    version="0.1.0",
    author="OHAP Community",
    author_email="contact@ohap.org",
    description="Official Python SDK for the Open Human Agent Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/Open-Human-Agent-Protocol",
    project_urls={
        "Documentation": "https://ohap.org/docs/python",
        "Source": "https://github.com/your-org/Open-Human-Agent-Protocol",
        "Tracker": "https://github.com/your-org/Open-Human-Agent-Protocol/issues",
    },
    packages=find_packages("python"),
    package_dir={"": "python"},
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0",
            "mypy>=1.0",
            "black>=23.0",
            "isort>=5.12",
            "flake8>=6.0",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords="ohap human-ai-collaboration protocol sdk fusion-workflow",
    license="MIT",
)
