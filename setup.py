from setuptools import setup

setup(
    name='terminaltrail',
    version='0.1.0',
    author='Ar-Ray-code',
    author_email='ray255ar@gmail.com',
    description='A package for TerminalTrail.',
    packages=['terminaltrail'],
    url='https://github.com/Ar-Ray-code/TerminalTrail',
    requires=['openai'],
    entry_points={
        'console_scripts': [
            'TerminalTrail=terminaltrail.terminaltrail:main'
        ]
    }
)
