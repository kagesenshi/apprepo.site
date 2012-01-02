Introduction
============

This package contains a basic buildout for AppRepo, and customizations done 
on it.

Deploying this package will create an almost exact buildout of the apprepo.org,
where you can use for development, or for deploying your own apprepo server.

Deploying
=========

Requirements
-------------

These are the stuff you need to deploy this. Note that Plone 4.1.2 requires
Python 2.6. If you need a Python2.6 RPM, you may grab it here:

http://izhar.fedorapeople.org/compat-python26/

Specific requirements:

 * python-devel (2.6)
 * gcc/g++
 * libjpeg-devel
 * zlib-devel
 * freetype-devel
 * git
 * subversion

Building
-----------

You may deploy this easily using these commands::

  git clone git@github.com:kagesenshi/apprepo.site.git 
  # if you didnt have a github account, use 
  # git://github.com/kagesenshi/apprepo.site.git instead
  cd apprepo.site
  python2.6 bootstrap.py
  ./bin/buildout -vvv

The buildout tool will pull all the dependencies from python PyPi 
and deploy them inside a self-contained environment in the directory

Starting
---------

Once buildout is successful, you may start the zope server using::

  ./bin/instance fg

You may then access the site at http://localhost:8080. Default admin login
is admin:admin

Initial setup
--------------

Once you have the server running, add a Plone site, include the AppRepo
Customization addon in the installation

After its done, you will have a Plone site, find the "Add new" dropdown, 
and you may add Application there.

The sidebar items in apprepo.org are portlets, you might want to assign the
PackageKit Web Portlet in your left sidebar at 
http://localhost:8080/$site/@@manage-portlets . It will appear in the context
of an application, displaying the icon and install button.




