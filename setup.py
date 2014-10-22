from distutils.core import setup

setup(
    name='phoShuff',
    version='0.0.1',
    author='Michael Imelfort',
    author_email='mike@mikeimelfort.com',
    packages=['phoshuff'],
    scripts=['bin/phoshuff'],
    url='http://pypi.python.org/pypi/phoShuff/',
    license='GPLv3',
    description='phoShuff',
    long_description=open('README.md').read(),
    install_requires=[],
)

