Multiple Component Directories
===============================

BowerStatic provides the possibility to create more than one
``bower_components`` directory. Each directory is an "isolated universe" of
components. Components in a ``bower_components`` directory can depend on each
other only – they cannot depend on components in another directory.

To add multiple ``bower_components`` directories, you need to give them
names:

.. code-block:: python

    config.add_bower_components('myapp:static/this_components', name='this')
    config.add_bower_components('myapp:static/that_components', name='that')

You can use components from this directories as follows:

.. code-block:: python

    request.include('jquery', 'this')
    request.include('bootstrap', 'that')

.. note:: At the moment it is not possible to create multiple local
          ``bower_components`` directories


