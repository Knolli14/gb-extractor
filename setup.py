from setuptools import find_packages, setup

with open("requirements.txt") as f:
    content = f.readlines()

requirements =  [x.strip() for x in content if "git+" not in x]

setup(
    name="gbextractor",
    version="0.1",
    description="Extract Manuals from specific Wegbpage",
    author="knolli",
    install_requirements=requirements,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
