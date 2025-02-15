import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'pyzotero',
    'toml',
]

tests_require = [
    'WebTest',
    'pytest',
    'pytest-cov',
]

setup(
    name='zobib',
    version='0.1.0',
    description='mtmdl',
    long_description=README,
    classifiers=[
        'Programming Language :: Python',
    ],
    author='',
    author_email='',
    url='',
    keywords='zotero bibtex biblatex',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'zobib = zobib.scripts.zobib_main:main',
        ],
    },
)
