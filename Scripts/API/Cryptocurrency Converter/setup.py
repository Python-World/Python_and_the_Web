from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cryptozor.py",
    version="1.0.8",
    author="Abhinav Anand",
    author_email="abhinavanandpnbe@gmail.com",
    description="A Python Cryptocurrency converter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests",
    ],
    py_modules=["cryptozor"],
)
