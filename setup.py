from setuptools import setup, find_packages

__author__ = 'drews'

setup(
    name='traffic-simulation',
    packages=find_packages(),
    version='1.0',
    description='Testing the theory that breaking suddenly in traffic can cause gridlock.',
    author='Drew J. Sonne',
    author_email='drew.sonne@gmail.com',
    url='http://github.com/drewsonne/TrafficSimulation',
    install_requires=['vispy'],
    entry_points={
        'console_scripts': [
            'traffic-simulation-breaking=trafficsimulation:main'
        ]
    }
)
