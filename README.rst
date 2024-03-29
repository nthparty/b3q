===
b3q
===

Boto3 utility library that supports parameter-driven and predicate-driven retrieval of collections of AWS resources.

|pypi| |readthedocs| |actions| |coveralls|

.. |pypi| image:: https://badge.fury.io/py/b3q.svg
   :target: https://badge.fury.io/py/b3q
   :alt: PyPI version and link.

.. |readthedocs| image:: https://readthedocs.org/projects/b3q/badge/?version=latest
   :target: https://b3q.readthedocs.io/en/latest/?badge=latest
   :alt: Read the Docs documentation status.

.. |actions| image:: https://github.com/nthparty/b3q/workflows/lint-test-cover-docs/badge.svg
   :target: https://github.com/nthparty/b3q/actions/workflows/lint-test-cover-docs.yml
   :alt: GitHub Actions status.

.. |coveralls| image:: https://coveralls.io/repos/github/nthparty/b3q/badge.svg?branch=main
   :target: https://coveralls.io/github/nthparty/b3q?branch=main
   :alt: Coveralls test coverage summary.

Purpose
-------
This library makes it possible to use `Boto3 <https://boto3.readthedocs.io>`__ to retrieve a collection of AWS resources (selected according to supplied parameters, constraints, and/or predicates) within an AWS service.

Installation and Usage
----------------------
This library is available as a `package on PyPI <https://pypi.org/project/b3q>`__::

    python -m pip install b3q

The library can be imported in the usual ways::

    import b3q
    from b3q import *

Examples
^^^^^^^^
The library make it possible to concisely retrieve all instances of an AWS resource (potentially spanning multiple pages of results). The library requires the use of the `Boto3 <https://boto3.readthedocs.io>`__ library to create a client object that can be used to retrieve information about AWS resources. In the example below, an AWS API Gateway client is created::

    >>> import boto3
    >>> client = boto3.client('apigateway')

In the example below, all custom domain name entries are retrieved::

    >>> import b3q
    >>> ns = b3q.get(client.get_domain_names)

The example below illustrates the retrieval of an API with the name ``'example_api'``::

    >>> apis = b3q.get(client.get_rest_apis, constraints={'name': 'example_api'})
    >>> api = apis[0] # Assumes there is one result.

The steps below retrieve all API deployments associated with the specific API retrieved above::

    >>> ds = b3q.get(client.get_deployments, arguments={'restApiId': api['id']})

Development
-----------
All installation and development dependencies are fully specified in ``pyproject.toml``. The ``project.optional-dependencies`` object is used to `specify optional requirements <https://peps.python.org/pep-0621>`__ for various development tasks. This makes it possible to specify additional options (such as ``docs``, ``lint``, and so on) when performing installation using `pip <https://pypi.org/project/pip>`__::

    python -m pip install .[docs,lint]

Documentation
^^^^^^^^^^^^^
The documentation can be generated automatically from the source files using `Sphinx <https://www.sphinx-doc.org>`__::

    python -m pip install .[docs]
    cd docs
    sphinx-apidoc -f -E --templatedir=_templates -o _source .. && make html

Testing and Conventions
^^^^^^^^^^^^^^^^^^^^^^^
All unit tests are executed and their coverage is measured when using `pytest <https://docs.pytest.org>`__ (see the ``pyproject.toml`` file for configuration details)::

    python -m pip install .[test]
    python -m pytest

Alternatively, all unit tests are included in the module itself and can be executed using `doctest <https://docs.python.org/3/library/doctest.html>`__::

    python src/b3q/b3q.py -v

Style conventions are enforced using `Pylint <https://pylint.pycqa.org>`__::

    python -m pip install .[lint]
    python -m pylint src/b3q

Contributions
^^^^^^^^^^^^^
In order to contribute to the source code, open an issue or submit a pull request on the `GitHub page <https://github.com/nthparty/b3q>`__ for this library.

Versioning
^^^^^^^^^^
The version number format for this library and the changes to the library associated with version number increments conform with `Semantic Versioning 2.0.0 <https://semver.org/#semantic-versioning-200>`__.

Publishing
^^^^^^^^^^
This library can be published as a `package on PyPI <https://pypi.org/project/b3q>`__ by a package maintainer. First, install the dependencies required for packaging and publishing::

    python -m pip install .[publish]

Ensure that the correct version number appears in ``pyproject.toml``, and that any links in this README document to the Read the Docs documentation of this package (or its dependencies) have appropriate version numbers. Also ensure that the Read the Docs project for this library has an `automation rule <https://docs.readthedocs.io/en/stable/automation-rules.html>`__ that activates and sets as the default all tagged versions. Create and push a tag for this version (replacing ``?.?.?`` with the version number)::

    git tag ?.?.?
    git push origin ?.?.?

Remove any old build/distribution files. Then, package the source into a distribution archive::

    rm -rf build dist src/*.egg-info
    python -m build --sdist --wheel .

Finally, upload the package distribution archive to `PyPI <https://pypi.org>`__::

    python -m twine upload dist/*
