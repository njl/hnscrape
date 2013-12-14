from distutils.core import setup
setup(name='hnscrape',
      version='0.1',
      py_modules=['hnscrape'],
      install_requires = [
          'lxml',
          'requests',
          'cssselect',
          ]
      )
