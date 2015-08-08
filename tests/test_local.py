from djed.testing import BaseTestCase


class TestLocalComponents(BaseTestCase):

    _includes = ('djed.static',)

    def test_add(self):

        self.config.add_bower_components('tests:static/dir1')
        self.config.add_bower_component('myapp', 'tests:static/local/myapp')
        self.config.make_wsgi_app()

        bower = self.request.get_bower()

        collection = bower._component_collections['components']

        self.assertIn('myapp', collection._components)

    def test_add_non_existent(self):
        from pyramid.exceptions import ConfigurationError

        self.assertRaises(ConfigurationError, self.config.add_bower_component,
                          'myapp', 'tests:static/local/not_exists')

        self.assertRaises(ConfigurationError, self.config.add_bower_component,
                          'myapp', 'tests:static/local/empty')

    def test_add_local_component_before_container(self):
        self.config.add_bower_component('myapp', 'tests:static/local/myapp')
        self.config.commit()

        self.config.add_bower_components('tests:static/dir1')
        self.config.make_wsgi_app()

        bower = self.request.get_bower()

        collection = bower._component_collections['components']

        self.assertIn('myapp', collection._components)
        

    def test_add_error(self):
        from pyramid.exceptions import ConfigurationError

        self.config.add_bower_component('myapp', 'tests:static/local/myapp')
        
        self.assertRaises(ConfigurationError, self.config.make_wsgi_app)
