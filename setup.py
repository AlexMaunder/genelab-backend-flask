from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'psycopg2',
]

setup(
    name='genelab',
    version='0.0',
    description='A Genetic Repository built with Flask',
    author='Lex Maunder',
    author_email='',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
