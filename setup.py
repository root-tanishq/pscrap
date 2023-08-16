from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pscrap',
    version='1.0.0',
    long_description=readme(),
    long_description_content_type="text/markdown",
    description='multi processed parameter scrapper',
    url='https://github.com/root-tanishq/pscrap',
    author='Tanishq Rathore',
    license='MIT',
    packages=['pscrap'],
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'pscrap = pscrap.__main__:main'
        ]
    },
)
