import os
from setuptools import setup

try:
    README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except Exception as e:
    README = "Readme unavailable"

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

requires = [
    'django',
    'psycopg2',
    'boto',
    'PIL',
    'oauth2',
    'passlib'
    ]
setup(
    name='photos',
    version='0.1',
    packages=['photos'],
    include_package_data=True,
    license='BSD License',  # example license
    description="""
    A Django app for processing sports photos in conjunction with the USA today photos
    API.
    """,
    long_description=README,
    url='https://github.com/adamsar',
    author='Andrew Adams',
    author_email='adamsar@gmail.com',
    install_requires=requires,
    tests_requires=requires,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Sports afficionados',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        
        # replace these appropriately if you are using Python 3
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
