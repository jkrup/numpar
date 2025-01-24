from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="numpar",
    version="0.1.1",
    packages=find_packages(),
    description="A package for parsing number strings in various formats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Just",
    author_email="justin@bokuga.com",
    python_requires=">=3.6",
    install_requires=[],
    test_suite="tests",
    url="https://github.com/jkrup/numpar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)