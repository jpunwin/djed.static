.. _local-components:

Local Components
================

If you develop your own front-end-code (so called "local components"), you
can also publish them with BowerStatic.

You can add one or more local components in this way:

.. code-block:: python

    config.add_bower_component('myapp:static/myapp')

To use a local components in an application, a ``bower_components`` directory
has to been defined somewhere in the application configuration
(see :ref:`getting-started`).

Local components can be included on your HTML page like any other component:

.. code-block:: python

    request.include('myapp')

This includes your front-end-code in the HTML page and all dependencies that
are defined in the ``bower.json`` file.
