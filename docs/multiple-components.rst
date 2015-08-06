.. _multiple-components:

Multiple Component Directories
===============================

BowerStatic provides the possibility to create more than one
``bower_components`` directory. Each directory is an "isolated universe" of
components. Components in a ``bower_components`` directory can depend on each
other only – they cannot depend on components in another directory.

To use multiple ``bower_components`` directories, you need to give them
names:

.. code-block:: python

    config.add_bower_components('myapp:static/more_components', name='more')

You can use components from this directories as follows:

.. code-block:: python

    request.include('jquery', 'more')

To use this ``bower_components`` directory for local components:

.. code-block:: python

    config.add_bower_component('myapp:static/my_component', verions='1.0.0',
                               name='more')

After that, you can include your local components on the HTML page:

.. code-block:: python

    request.include('my_component', 'more')


