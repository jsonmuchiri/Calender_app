from setuptools import setup


setup(
    name='Calendar',
    version='1.0',
    py_modules=['calender_app'],
    install_requires=[
        'click'
    ],
    entry_points='''
        [console_scripts]
        Calender=calender_app:cli
    ''',
)