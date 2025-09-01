from setuptools import setup

version = '0.0.0+develop'

setup(
    name='lakasirclient',
    version=version,
    author='Apriliansyah Idris',
    author_email='apriliansyahidris@gmail.com',
    description="Unofficial Python Client for Lakasir",
    install_requires=[
        'requests==2.32.5',
    ],
    license='MIT license'
)
