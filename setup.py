#try:
#    from setuptools import setup
#except ImportError:
#    from distutils.core import setup

from setuptools import setup, find_packages

setup(
    name='agilEarning',
    version='0.0.1dev',
    description='lottery analysis',
    author='Chia-Chi Chang',
    author_email='c3h3.tw@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        "pandas"
    ],
)
