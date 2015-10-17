# -*- coding: utf-8 -*-

import codecs
from setuptools import setup, find_packages


install_requires = open("requirements.txt").readlines()
test_requires = []
for line in open("requirements-test.txt").readlines():
    if line.strip() and not line.startswith("-r"):
        test_requires.append(line.strip())

long_description = codecs.open('README.rst', "r", "utf-8").read()


setup(
    name='badtouch',
    version="0.1",
    description='A friendly python library for the Bose SoundTouch (R) API',
    long_description=long_description,
    author="Christian Assing",
    author_email="chris@ca-net.org",
    url="http://github.com/chassing/badtouch/",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
    license="BSD",
    platforms='any',
    keywords='nidhogg',
    classifiers=[
        # Picked from
        #    http://pypi.python.org/pypi?:action=list_classifiers
        # "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        # "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    test_suite='tests',
)
