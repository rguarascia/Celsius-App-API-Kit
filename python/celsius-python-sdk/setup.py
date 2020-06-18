''' Setup script for Celsius-Python-SDK '''

from setuptools import setup
import os

README = open('README.md')

ver = os.path.join('pyCelsius', 'version.py')
with open(ver) as verCEL:
    code = compile(verCEL.read(), ver, 'exec')
    exec(code)
    
#Package setup
setup(
    name="celsius-python-sdk",
    version=__version__,
    description="Celsius API SDK for Python",
    long_description=README.read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rguarascia/Celsius-App-API-Kit/tree/master/python/celsius-python-sdk",
    author="Raag Naidu",
    author_email="raag.naidu@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pyCelsius"],
    include_package_data=True,
    install_requires=["requests"],
)
