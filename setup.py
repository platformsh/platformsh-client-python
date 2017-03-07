"""
Platform python client.
"""
from setuptools import setup

version = '0.0.1'

install_requires = [
    'requests'
]

setup(
    name='pshclient',
    version=version,
    url='https://github.com/platformsh/platformsh-client-python',
    license='MIT',
    author='Platform.sh, Raphael Deem',
    author_email='raphael@platform.sh',
    description=(
        'Platformsh Python API endpoints'),
    packages=['pshclient'],
    platforms='any',
    install_requires=install_requires,
)
