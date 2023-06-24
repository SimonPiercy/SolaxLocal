from setuptools import setup, find_packages

setup(
    name='solaxlocal',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0b2',
        'pydantic>=2.0a4',
    ],
)
