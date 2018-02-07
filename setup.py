from setuptools import setup

setup(name='WrappedTFP',
      version='0.1',
      description='wrapped Tensorflow Projector',
      url='http://github.com/cedias/WrappedTFP',
      author='cedias',
      author_email='me@mymail.com',
      license='MIT',
      packages=['wrappedtfp'],
      data_files=[('tpf')],
      zip_safe=False)