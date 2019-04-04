*************
pypkgtemplate
*************

A python package cookiecutter which focuses on providing modern tooling boilerplate
------------------------------------------------------------------------------------

.. image:: https://git.coop/decentral1se/pypkgtemplate/badges/master/pipeline.svg
   :target: https://git.coop/decentral1se/pypkgtemplate/commits/master
   :alt: Pipeline status

.. image:: https://img.shields.io/badge/license-GPL-brightgreen.svg
   :target: LICENSE
   :alt: Repository license
   
.. image:: https://img.shields.io/badge/support-me-lightgreen.svg
   :target: https://lukewm.info/support/
   :alt: Support badge

Support
-------

This package is created and maintained by `decentral1se`_.

Please consider supporting their work by donating.

    https://lukewm.info/support

.. _decentral1se: https://lukewm.info/

.. _documentation:

Documentation
-------------

Why another template?
=====================

A lot of cookiecutter template designers try to include **all** the things from
the start and then due to maintenance burdens, the package fall behind with the
moving ecosystem. For example, one of the most commonly used packages,
`cookiecutter-pypackage`_ has, at present moment, not been updated for a year
and has 23 open change requests. 

This template is about moving with the ecosystem to provide a modern and
up-to-date cookiecutter template for creating Python packages. In order to keep
pace, I focus on tooling rather than code customisation. Your Python package
code can be different each time but the tools should be standardised and
reliable.

.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

Design Principles
=================

* Use standardised tooling for packaging (setuptools, pip).
* Use standardised tooling for testing (tox, pytest)
* Use best-in-class tools for quality assurance (flake8, isort, mypy, black)
* Make no assumptions about the Python package code (different every time)

Assumptions
===========

* Use the GPL3-or-later for licensing
* Use Gitlab CI for continuous integration
* Use Gitlab CI for code coverage report

These are based on my current preferences but I am open to accepting
contributions to customise this behaviour. I know a lot of people use different
platforms out there in the wild.

Usage
=====

Install `cookiecutter`_ and then invoke the following spell:

.. code-block:: bash

    cookiecutter https://git.coop/decentral1se/pypkgtemplate.git

.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/

Variables
=========

.. code-block:: json

    {
        "package": "",
        "author": "",
        "author_email": "",
        "author_site": "",
        "git_hosting_url": "",
        "package_description": "",
        "support": ""
    }
