from setuptools import setup, find_packages

setup(
    name="auto-factory",
    version="0.1.0",
    description="A custom DjangoModelFactory with automatic data generation for model fields",
    author="Ryan Jackson",
    author_email="ryanauj@umich.edu",
    url="https://github.com/ryanauj/auto_factory",
    packages=find_packages(),
    install_requires=[
        "Django>=3.0",
        "factory_boy>=3.0",
        "Faker>=8.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)
