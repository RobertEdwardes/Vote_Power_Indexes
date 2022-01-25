import pathlib
from distutils.core import setup
HERE = pathlib.Path(__file__).parent
README = (HERE/"README.md")

setup(
    name="voter-power-index",
    version="0.1.0",
    description="Tool to help show voter index for vote dilution analyst",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Robert Edwardes",
    author_email="robbie@fairlines.org",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["vpidx"],
    install_requires=['pandas'],
)