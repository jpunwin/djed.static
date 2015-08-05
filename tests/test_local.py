from pyramid.exceptions import ConfigurationError

from djed.testing import BaseTestCase


class TestLocalComponents(BaseTestCase):

    _includes = ('djed.static',)

    def test_add(self):

        self.config.add_bower_components('tests:bower_components')
        self.config.add_bower_component('myapp', 'tests:local_component')

        bower = self.request.get_bower()

        collection = bower._component_collections['components']

        self.assertIn('myapp', collection._components)

    def test_add_non_existent(self):
        self.assertRaises(ConfigurationError, self.config.add_bower_component,
                          'myapp', 'tests:not_exists')

        self.assertRaises(ConfigurationError, self.config.add_bower_component,
                          'myapp', 'tests:empty_dir')

    def test_add_error(self):
        from djed.static import Error

        self.assertRaises(Error, self.config.add_bower_component,
                          'myapp', 'tests:local_component')
