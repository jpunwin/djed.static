.. _getting-started:

Getting Started
===============

Install the package into your python environment:

.. code-block:: sh

    $ /path/to/pyvenv/bin/pip install djed.static

Include it in your Pyramid application:

.. code-block:: python

    config.include('djed.static')

Set-up the path to the ``bower_components`` directory in your ``.ini`` file:

.. code-block:: ini

    [app:main]
    # ... other settings ...
    djed.static.components_path = myapp:static/bower_components

Or use the following statement to add the ``bower_components`` directory:

.. code-block:: python

    config.add_bower_components('myapp:static/bower_components')

Now, you can use all installed bower packages. To include the desired
components, call the following function in a HTML template or
somewhere else in your code:

.. code-block:: python

    request.include('bootstrap')

This adds the following tags to the end of the HTML ``<head>`` section:

.. code-block:: html

  <script type="text/javascript" src="/bowerstatic/components/jquery/2.1.4/dist/jquery.js"></script>
  <script type="text/javascript" src="/bowerstatic/components/bootstrap/3.3.5/dist/js/bootstrap.js"></script>
  <link rel="stylesheet" type="text/css" href="/bowerstatic/components/bootstrap/3.3.5/dist/css/bootstrap.css">
    
As you can see, all required dependencies are automatically resolved and also
included in your HTML document.
