from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',

]

setup(
    author='Mahfuz Salehin Moaz',
    author_email='almuaz1998@gmail.com',
    name='FireNext',
    version='1.0.1',
    description='This is an offline database library',
    long_description=open('README.md').read() + '\n\n' + open("CHANGELOG.txt").read(),
    url='https://github.com/almoaz/PyFireNext',
    license='MIT',
    classifiers='classifiers',
    keywords='firenext',
    packages=find_packages(),

)
