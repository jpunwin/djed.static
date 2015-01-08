Getting Started
===============

Installation
------------
Install the package into your python environment::

    pip install djed.static

Usage
-----

Include djed.static in your Pyramid application::

    config.include('djed.static')

Initialize a ``bower_components`` directory::

    config.init_bower_components('myapp:static/bower_components')

Include required Bower packages on your page. You can do this in templates or
somewhere else in your code::

    request.include('bootstrap')
