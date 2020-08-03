from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["regex>=2020.6.7", "requests>=2"]

setup(
    name="cronjobfilter",
    version="0.0.3",
    author="Priyesh Naik",
    author_email="blackbeastfilo@live.com",
    description="A package will help to filter list of cronjobs which are coming under from date and to date.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Solution4Problem/cronjobfilter/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
