from setuptools import setup
from setuptools import find_packages

requires = [
    'SQLAlchemy==1.3.10',
    'zope.sqlalchemy==1.2',
    'IPy==1.0',
    ]

tests_require = []

setup(name='easy_sqlalchemy',
      version='0.2.1',
      description='SQLAlchemy wrapper',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='https://github.com/lxneng/easy_sqlalchemy',
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
