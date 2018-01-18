import os
from setuptools import find_packages, setup

setup(
	name='d08-ex00',
	version='0.1',
	packages=find_packages(),
	include_package_data=True,
	author='Mickael Sorin',
	author_email='msorin@student.42.fr',
	classifiers=[
		'Environment :: Web Environment',
		'Framworks :: Django',
		'Framworks :: Django :: 1.9',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
	]
)
