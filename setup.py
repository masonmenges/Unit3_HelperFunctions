from setuptools import setup

setup(
    name='lambdata_masonm',  # Required
    version='0.0.6',  # Required
    author='masonm',  # Optional
    author_email='mason.menges2@gmail.com',  # Optional
    keywords='dspt11_lambda',  # Optional
    packages=['hfmodule'],  # Required
    python_requires='>=3.6, <4',
    install_requires=['pandas', 'random2'],  # Optional
)