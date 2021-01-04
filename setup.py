from setuptools import setup, find_packages
from os import path
from io import open

from feishu_sdk import __version__, __description__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="feishu_py_sdk",
    version=__version__,
    description=__description__, 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilpan/feishu-sdk",
    author="ilpan",
    author_email="pna.dev@outlook.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="feishu sdk client server",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    python_requires=">=3.6",
    install_requires=[
        "aiohttp==3.7.3",
        "async-timeout==3.0.1; python_full_version >= '3.5.3'",
        "attrs==20.3.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "chardet==3.0.4",
        "idna==2.10; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "multidict==5.1.0; python_version >= '3.6'",
        "typing-extensions==3.7.4.3",
        "yarl==1.6.3; python_version >= '3.6'",
    ],
    extras_require={"dev": []},
    dependency_links=[],
)
