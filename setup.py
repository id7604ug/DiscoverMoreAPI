from setuptools import setup

setup(name='DiscoverMoreAPI',
    version='0.1.dev',
    description='api "requesting" api\'s from different sources' ,
    author='Momo Johnson, Anthony Flowers, Jeremy Baisley',
    packages=['DiscoverMoreAPI'],
    install_requires=['Beautifulsoup4', 'requests', 'tweepy', 'google-api-python-client', 'TwitterSearch'])