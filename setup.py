from setuptools import setup, find_packages

setup(
    name='mite-simulator',
    version='0.1.0',
    description='Flight simulator powered performance testing',
    author='Jordan Brennan',
    author_email='jb098@hotmail.com',
    packages=find_packages(),
    install_requires=["mite", "pygame"]
)