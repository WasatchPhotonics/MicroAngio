import os

from setuptools import setup, find_packages

README=""
CHANGES=""

requires = [
    "pytest",
    "pytest-cov",
    "pytest-qt",
    "pytest-capturelog",
    "pyside",
    ]

setup(name="microangio",
      version="0.0",
      description="Minimal PySide testable application",
      long_description=README + "\n\n" + CHANGES,
      classifiers=[],
      author="Nathan Harrington",
      author_email="nharrington@wasatchphotonics.com",
      url="",
      keywords="",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite="microangio",
      install_requires=requires,
      )
