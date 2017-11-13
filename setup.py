from setuptools import setup

setup(
    name='blog',
    packages=['application'],
    include_package_data=True,
    install_requires=[
        'flask',
        'Flask-SQLAlchemy',
    ],
)