from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("entry_points.ini", "r") as fh:
    entry_points = fh.read()

setup(
    name="bf20_mill",
    version="0.0.1",
    author="James Walker",
    author_email="james.walker.nz@me.com",
    description="bf20_mill - A QtPyVCP based Virtual Control Panel for LinuxCNC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joco-nz/bf20_mill",
    download_url="https://github.com/joco-nz/bf20_mill/tarball/master",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    install_requires=[
       'qtpyvcp',
    ],
)
