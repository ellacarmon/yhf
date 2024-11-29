from setuptools import setup, find_packages

setup(
    name="yhf-wrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
    ],
    author="Ella Carmon",
    author_email="ellacarmon@gmail.com",
    description="A YH Finance API wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ellacarmon/yhf-wrapper",  # if you have a repository
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6"
)