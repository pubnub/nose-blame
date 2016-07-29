from setuptools import setup, find_packages

setup(
    name='nose-blame',
    version='1.0.0',
    author='Ben Parham',
    author_email = 'ben@pubnub.com',
    url = 'https://github.com/pubnub/nose-blame',
    description = 'Nose blame plugin',
    long_description = 'Nose plugin that allows adding owners to tests and outputs blame report on test failure',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['nose'],
    entry_points = {
        'nose.plugins.0.10': ['blame = nose_blame:BlamePlugin']
    }
)
