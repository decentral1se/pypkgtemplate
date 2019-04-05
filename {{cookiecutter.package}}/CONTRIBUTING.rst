*************
Get Involved
*************

We use `tox`_ as the development interface.

.. _tox: http://tox.readthedocs.io/

Run tests
---------

.. code-block:: bash

    tox -e test

Lint source
-----------

.. code-block:: bash

    tox -e lint

Format source
-------------

.. code-block:: bash

    tox -e format

Type check source
-----------------

.. code-block:: bash

    tox -e type

Development install
-------------------

.. code-block:: bash

    $ pip install -e .'[test,lint,format,type,docs,pkg]'

Add a new dependency
--------------------

You add to the `install_requires`_ entry in the `setup.cfg`_.

.. _install_requires: https://setuptools.readthedocs.io/en/latest/setuptools.html#options
.. _setup.cfg: ./setup.cfg

Release Process
---------------

.. code-block:: bash

    $ git tag x.x.x
    $ git push --tags

Test release
============

.. code-block:: bash

    $ tox -e metadata-release
    $ tox -e test-release

Validate that you can install the package:

.. code-block:: bash

    $ pip install -i https://test.pypi.org/simple/ {{cookiecutter.package}}
    $ pip show {{cookiecutter.package}}

Production release
==================

.. code-block:: bash

    $ tox -e metadata-release
    $ tox -e prod-release

Validate that you can install the package:

.. code-block:: bash

    $ pip install {{cookiecutter.package}}
    $ pip show {{cookiecutter.package}}
