from djed.testing import BaseTestCase


class TestLocalComponents(BaseTestCase):

    _includes = ('djed.static',)

    def test_add(self):

        self.config.add_bower_components('tests:bower_components')
        self.config.add_bower_component('myapp', 'tests:local_component')
        self.config.make_wsgi_app()

        bower = self.request.get_bower()

        collection = bower._component_collections['components']

        self.assertIn('myapp', collection._components)

    def test_add_non_existent(self):
        from pyramid.exceptions import ConfigurationError

        self.assertRaises(ConfigurationError, self.config.add_bower_component,
                          'myapp', 'tests:not_exists')

        self.assertRaises(ConfigurationError, self.config.add_bower_component,
                          'myapp', 'tests:empty_dir')

    def test_add_local_component_before_container(self):
        self.config.add_bower_component('myapp', 'tests:local_component')
        self.config.commit()

        self.config.add_bower_components('tests:bower_components')
        self.config.make_wsgi_app()

        bower = self.request.get_bower()

        collection = bower._component_collections['components']

        self.assertIn('myapp', collection._components)
        

    def test_add_error(self):
        from pyramid.exceptions import ConfigurationError

        self.config.add_bower_component('myapp', 'tests:local_component')
        
        self.assertRaises(ConfigurationError, self.config.make_wsgi_app)
