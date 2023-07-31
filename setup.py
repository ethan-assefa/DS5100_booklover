# This file is the setup for the package on BookLover
## Ethan Assefa

from setuptools import setup, find_packages
# The setup file for my booklover package
setup(
    name='BookLove',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Ethan Assefa',
    author_email='eda8ek@virginia.com',
    description='A package that wraps up the BookLover class and the test suite for it. (This is work for M09 of the DS5100 course at UVA SDS)',
    packages=find_packages(),    
    install_requires=['unittest', 'pandas >= 1.5.3'],
)