from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='apprepo.site',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['apprepo'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'plone.app.referenceablebehavior',
          'plone.app.relationfield',
          'plone.app.theming',
          'Products.ContentWellPortlets',
          'diazotheme.bootstrap',
          'collective.packagekit',
          'plone.contentratings',
          'collective.miscbehaviors'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
