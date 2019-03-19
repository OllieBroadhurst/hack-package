from setuptools import setup, find_packages

setup(
    name='hackpackage',
    version='1.0',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA Hackathon recursion and sorting package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/OllieBroadhurst/hackpackage/',
    author='Oliver Broadhurst',
    author_email='olliebroadhurst@gmail.com'
)
