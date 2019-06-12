from setuptools import setup, find_packages

setup(name='DataStructures',
      version='0.1',
      description='Data structure implementation in python',
      long_description='A repository of famous data structures and algorithms implemented in python for educational purpose.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='data structures algorithms python',
      url='https://github.com/ali92hm/data-structure-implementation',
      author='Ali Hajimirza',
      author_email='ali@alihm.net',
      license='MIT',
      packages=find_packages(),
      install_requires=[],
      include_package_data=True,
      zip_safe=False)
