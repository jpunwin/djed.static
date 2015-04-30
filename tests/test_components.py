from base import BaseTestCase


class TestComponents(BaseTestCase):

    def test_add(self):

        self.config.add_bower_components(
            self.make_asset_spec('bower_components'))

        bower = self.request.get_bower()

        self.assertIn('components', bower._component_collections)
        self.assertEqual(len(bower._component_collections), 1)

    def test_add_conflict_error(self):
        from djed.static import Error

        self.config.add_bower_components(
            self.make_asset_spec('bower_components'))

        self.assertRaises(Error, self.config.add_bower_components,
                          'components')

    def test_add_custom(self):

        self.config.add_bower_components(
            self.make_asset_spec('bower_components'), name='custom')

        bower = self.request.get_bower()

        self.assertIn('custom', bower._component_collections)
        self.assertEqual(len(bower._component_collections), 1)

    def test_add_custom_conflict_error(self):
        from djed.static import Error

        self.config.add_bower_components(
            self.make_asset_spec('bower_components'), name='custom')

        self.assertRaises(Error, self.config.add_bower_components,
                          self.make_asset_spec('components'), name='custom')

    def test_add_multiple(self):

        self.config.add_bower_components(
            self.make_asset_spec('bower_components'))
        self.config.add_bower_components(
            self.make_asset_spec('components'), name='custom')

        bower = self.request.get_bower()

        self.assertIn('components', bower._component_collections)
        self.assertIn('custom', bower._component_collections)
        self.assertEqual(len(bower._component_collections), 2)
