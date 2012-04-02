from setuptools import setup
from setuptools import find_packages

version = '1.0'

requires = [
    'setuptools',
    'SQLAlchemy',
    'zope.sqlalchemy',
    ]

tests_require = []

setup(name='easy_sqlalchemy',
      version=version,
      description='SQLAlchemy wrapper',
      long_description=open('README.rst'),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='http://lxneng.com/',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          'docs': ['sphinx'],
          'tests': tests_require,
          },
      test_suite='easy_sqlalchemy')
