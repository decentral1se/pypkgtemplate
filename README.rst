*************
pypkgtemplate
*************

.. image:: https://img.shields.io/badge/license-GPL-brightgreen.svg
   :target: LICENSE
   :alt: Repository license

.. image:: https://img.shields.io/badge/support-maintainers-brightgreen.svg
   :target: https://decentral1.se
   :alt: Support badge

A Python package cookiecutter with modern tooling
-------------------------------------------------

Why another template?
=====================

A lot of cookiecutter template designers try to include **all** the things from
the start and then due to maintenance burdens, the package fall behind with the
moving ecosystem. For example, one of the most commonly used packages,
`cookiecutter-pypackage`_ has, at present moment, not been updated for a year
and has 23 open change requests. 

This template is about moving with the ecosystem to provide a modern and
up-to-date cookiecutter template for creating Python packages. In order to keep
up to speed, I focus on tooling configuration rather than code customisation.
Your Python package code can be different each time but the tools should be
standardised and reliable.

.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

Design Principles
=================

* Make no assumptions about the Python package code (different every time)
* Use standardised tooling for packaging and dependencies (setuptools, twine).
* Use best-in-class tooling for testing (tox, pytest, coverage)
* Use best-in-class tooling for documentation (sphinx, towncrier, reStructuredText, readthedocs)
* Use best-in-class tools for quality assurance (flake8, isort, mypy, black)
* Use community and maintenance aids (CoC templates, issue templates)
* Provide common CI configurations (Travis CI)
* Use GPL version 3+ for the license.

Usage
=====

Install `cookiecutter`_ and then invoke the following spell:

.. code-block:: bash

    cookiecutter https://hack.decentral1.se/decentral1se/pypkgtemplate.git

Then you manually need to create your `readthedocs`_ project.

Refer to `CONTRIBUTING.rst`_ for the developer interface.

.. _CONTRIBUTING.rst: ./{{cookiecutter.package}}/CONTRIBUTING.rst
.. _readthedocs: https://readthedocs.org/accounts/login/
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/latest/

Variables
=========

.. code-block:: json

    {
        "package": "",
        "organisation": "",
        "author": "",
        "author_email": "",
        "author_site": "",
        "git_hosting_url": "",
        "package_description": "",
        "support": ""
    }

* **package**: The package name.
* **organisation**: The organisation name (for code of conduct).
* **author**: The package creator.
* **author_email**: The package creator's email.
* **author_site**: The package creator's website.
* **git_hosting_url**: The git hosting URL of the package.
* **package_description**: The package short description.
* **support**: The package creator's support/donation URL.
