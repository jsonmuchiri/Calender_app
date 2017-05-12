#the calender app

from setuptools import setup

setup(
    name='alpham1',
    version='1.0',
    py_modules=['calender'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mycal=mycal:cli
    ''',
)