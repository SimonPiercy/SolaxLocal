from setuptools import setup, find_packages

setup(
    name='solaxlocal',
    version='1.0.2',
    packages=find_packages(),
    install_requires=[
        'pydantic>=2.0b2',
        'requests>=2.0.0',
    ],
)
