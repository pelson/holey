from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='holey',

    version='2018.11',

    description='Geometry predicates written in python, optimised with numba',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.io/pelson/holey',

    author='Phil Elson',

    author_email='pelson.pub@gmail.com',

    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: GIS',

        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='geometry polygon shapely triangulation rasterization',

    packages=find_packages(exclude=['examples']),
    install_requires=[
            'numba',
            'numpy'],

    extras_require={
        'test': ['coverage', 'pytest'],
    },
    project_urls={
        'Source': 'https://github.com/pelson/holey/',
    },
)
