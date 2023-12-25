from setuptools import setup, find_packages

setup(name='eigenfaces',
      packages=find_packages(where='src'),
      package_dir={'': '.'},
      version='0.0.1',
      install_requires=[], )