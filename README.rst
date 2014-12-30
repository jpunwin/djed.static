.. image:: https://travis-ci.org/djedproject/djed.static.png?branch=master
   :target: https://travis-ci.org/djedproject/djed.static

.. _Bower: http://bower.io

.. _Bower configuration: http://bower.io/docs/creating-packages/

.. _BowerStatic: https://github.com/faassen/bowerstatic

.. _Pyramid: https://github.com/pylons/pyramid


*djed.static* provides Integration of BowerStatic_ into Pyramid_, so that you
can serve static resources (JavaScript, CSS) which you install and manage
through the Bower_ package manager.


Include *djed.static* in your Pyramid application and initialize it with the
path to your folder that contains the Bower components:

.. code-block:: python

    config.include('djed.static')
    config.init_bower_components('myapp:static/bower_components')


If required, you can add local Bower packages:

.. code-block:: python

    config.add_bower_component('myapp:static', version='0.1')

The defined folder has to contain a `bower.json` file
(see `Bower configuration`_).


To include a Bower package and its dependencies on your page:

.. code-block:: python

    request.include('bootstrap')

This works both in templates and views. 
