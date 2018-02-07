from setuptools import setup, find_packages

setup(name='WrappedTFP',
      version='0.1',
      description='wrapped Tensorflow Projector',
      url='http://github.com/cedias/WrappedTFP',
      author='cedias',
      author_email='me@mymail.com',
      license='MIT',
      packages=find_packages('.'),  
      package_dir={'':'.'}, 
      include_package_data=True,
      package_data={
        'wrappedtfp': ['tpf/*','tpf/oss_data/*'],
      })
