import json

from setuptools import setup

setup(
    name="basic-tools",
    version=json.load(open("basic_tools/version.json"))["version"],
    description="basic-tools is a library that contains a cluster of different useful tools",
    author="André Graça",
    author_email="andre.p.g@sapo.pt",
    platforms="Python",
    packages=["basic_tools"],
    install_requires=[
        "tqdm",
        "varname",
    ],
)
