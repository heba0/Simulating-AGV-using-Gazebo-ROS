"""
Setup script
How to upload new release
1. change version in setup.py
2. setup twine, see:https://blog.amedama.jp/entry/2017/12/31/175036
3. create zip file: python setup.py sdist
4. upload twine upload --repository pypi dist/hogehoeg
"""
import os

from setuptools import setup, find_packages

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# read README
try:
    import pypandoc
    readme = pypandoc.convert_file(PROJECT_PATH + '/README.md', 'rst')
except(IOError, ImportError):
    readme = open(PROJECT_PATH + '/README.md').read()

setup(
    name="pyroombaadapter",
    version="0.1.1",
    url="https://github.com/AtsushiSakai/PyRoombaAdapter",
    author="Atsushi Sakai",
    author_email="asakaig@gmail.com",
    maintainer='Atsushi Sakai',
    maintainer_email='asakaig@gmail.com',
    description="A Python library for Roomba Open Interface",
    long_description=readme,
    python_requires='>3.6.0',
    license="MIT",
    keywords="python roomba",
    packages=find_packages(),
    install_requires=['pyserial'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    test_suite='tests'
)
