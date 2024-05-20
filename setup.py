from setuptools import setup, find_packages

setup(
    name="dpc-python",
    version="0.1.0",
    description="A library for handling DPC data",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Mitsuhiro Setoguchi",
    author_email="setomits@gmail.com",
    url="https://github.com/setomits/dpc-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    test_suite='tests',
)
