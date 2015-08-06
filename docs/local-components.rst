.. _local-components:

Local Components
================

If you develop your own front-end-code (so called "local components"), you
can also publish them with BowerStatic.

First of all you have to create a ``bower_components`` directory as described
in :ref:`getting-started` and then you can add one or more local components:

.. code-block:: python

    config.add_bower_component('myapp', 'myapp:static/my_component', version='1.0.0')

.. note::
   You can retrieve the version of your Pyramid application like this:

   .. code-block:: python

      import pkg_resources
      version = pkg_resources.get_distribution('myapp').version

Your local components can depend on all available packages in the
``bower_components`` directory and can be included on your HTML page like any
other component:

.. code-block:: python

    request.include('my_component')

This includes your front-end-code in the HTML page and all dependencies that
are defined in the ``bower.json`` file.
