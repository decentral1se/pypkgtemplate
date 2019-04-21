*************
Get Involved
*************

We use `tox`_ as the development interface. This means that as a
contributor you do not have to manage a virtual environment or
dependencies. You can safely run ``pip install --user tox`` as a
standard `user package install`_ and then use the following
commands below to perform day-to-day development tasks.

.. note::

    It is recommended to use Python3.7 when doing development as
    some tooling requires this version.  Please see `pyenv`_ as a
    convenient tool to install multiple Python versions without
    interfering with your system level Python installation.

    .. _pyenv: https://github.com/pyenv/pyenv

.. _tox: http://tox.readthedocs.io/
.. _user package install: https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site

Run tests
---------

Use ``tox -l | grep test`` to choose a unit test environment that
uses a Python interpreter that you have available on your system.
Then you can run, for example:

.. code-block:: bash

    tox -e py36-test

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

Release Process
---------------

Test release
============

Add a change entry and re-generate the changelog:

.. code-block:: bash

    $ towncrier

See `test.pypi.org/{{cookiecutter.package}}`_ for latest version number.

Pick a new version and expose it in your terminal:

.. code-block:: bash

    $ export SETUPTOOLS_SCM_PRETEND_VERSION=X.X.X

If you have a development install locally, you can verify:

.. code-block:: bash

    $ {{cookiecutter.package}}--version

Then run the release process:

.. code-block:: bash

    $ tox -e metadata-release
    $ tox -e test-release

Validate that you can install the package:

.. code-block:: bash

    $ pip install \
      --index-url https://test.pypi.org/simple \
      --extra-index-url https://pypi.org/simple \
      {{cookiecutter.package}}
    $ pip show {{cookiecutter.package}}

.. _test.pypi.org/{{cookiecutter.package}}: https://test.pypi.org/project/{{cookiecutter.package}}/

Production release
==================

Add a change entry and re-generate the changelog:

.. code-block:: bash

    $ towncrier

Make a new release tag:

.. code-block:: bash

    $ git tag x.x.x
    $ git push --tags

If you have a development install locally, you can verify:

.. code-block:: bash

    $ {{cookiecutter.package}} --version

Then run the release process:

.. code-block:: bash

    $ tox -e metadata-release
    $ tox -e prod-release

Validate that you can install the package:

.. code-block:: bash

    $ pip install {{cookiecutter.package}}
    $ pip show {{cookiecutter.package}}
