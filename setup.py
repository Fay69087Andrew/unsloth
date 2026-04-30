# Setup configuration for unsloth - optimized LLM fine-tuning library
import re
from setuptools import setup, find_packages


def get_version():
    """Read version from __init__.py to avoid importing the package."""
    with open("unsloth/__init__.py", "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r'^__version__\s*=\s*["\']([^"\']+)["\']', content, re.MULTILINE)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string in unsloth/__init__.py")


def get_long_description():
    """Read the long description from README.md."""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Unsloth: 2x faster, 60% less memory LLM fine-tuning"


setup(
    name="unsloth",
    version="2024.12.0",
    author="Unsloth AI",
    author_email="info@unsloth.ai",
    description="2x faster, 60% less memory LLM fine-tuning",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/unslothai/unsloth",
    project_urls={
        "Bug Tracker": "https://github.com/unslothai/unsloth/issues",
        "Documentation": "https://docs.unsloth.ai",
        "Source Code": "https://github.com/unslothai/unsloth",
    },
    packages=find_packages(exclude=["tests*", "docs*", "examples*"]),
    python_requires=">=3.9",
    install_requires=[
        "torch>=2.1.0",
        "transformers>=4.38.0",
        "datasets>=2.16.0",
        "sentencepiece>=0.1.99",
        "tqdm>=4.66.1",
        "psutil",
        "wheel>=0.42.0",
        "packaging>=23.1",
        "tyro>=0.7.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            # mypy is handy for catching type errors during local development
            "mypy>=1.0.0",
        ],
        "training": [
            "trl>=0.7.9",
            "peft>=0.7.0",
            "accelerate>=0.26.0",
            "bitsandbytes>=0.42.0",
            "xformers>=0.0.23",
        ],
        "triton": [
            "triton>=2.1.0",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "llm",
        "fine-tuning",
        "lora",
        "qlora",
        "transformers",
        "pytorch",
        "machine learning",
        "deep learning",
    ],
    include_package_data=True,
    zip_safe=False,
)
