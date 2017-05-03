try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    reqs = f.read().splitlines()
    
setup(
    name='ethjsonrpc',
    version='0.3.1',
    description='Ethereum JSON-RPC client',
    long_description=open('README.rst').read(),
    author='ConsenSys',
    author_email='info@consensys.net',
    url='https://github.com/ConsenSys/ethjsonrpc',
    packages=['ethjsonrpc'],
    license='Unlicense',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires=reqs,
)