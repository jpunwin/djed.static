from djed.testing import BaseTestCase


class TestComponents(BaseTestCase):

    _includes = ('djed.static',)

    def test_add(self):

        self.config.add_bower_components('tests:bower_components')
        self.config.make_wsgi_app()

        bower = self.request.get_bower()

        self.assertIn('components', bower._component_collections)
        self.assertEqual(len(bower._component_collections), 1)

        components = bower._component_collections.get('components')
        self.assertTrue(components.path.endswith('/tests/bower_components'))

    def test_add_override(self):

        self.config.add_bower_components('tests:bower_components')
        self.config.commit()
        self.config.add_bower_components('tests:components')
        self.config.make_wsgi_app()

        bower = self.request.get_bower()
        components = bower._component_collections.get('components')

        self.assertTrue(components.path.endswith('/tests/components'))

    def test_add_non_existent_dir(self):
        from pyramid.exceptions import ConfigurationError

        self.assertRaises(ConfigurationError, self.config.add_bower_components,
                          'tests:not_exists')

    def test_add_conflict_error(self):
        from pyramid.exceptions import ConfigurationConflictError

        self.config.autocommit = False

        self.config.add_bower_components('tests:bower_components')
        self.config.add_bower_components('tests:bower_components')

        self.assertRaises(ConfigurationConflictError, self.config.commit)
