from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in said_custom/__init__.py
from said_custom import __version__ as version

setup(
	name="said_custom",
	version=version,
	description="SAID Innovations custom code",
	author="Geoffrey Karani",
	author_email="geoffrey.kamundi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
