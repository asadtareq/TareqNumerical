from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="TareqNumerical",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "sympy",
    ],
    author="Md Asaduzzaman",
    description="A complete numerical analysis tool for roots, ODEs and interpolation",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
