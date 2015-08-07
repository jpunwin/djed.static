import logging
import os
from collections import namedtuple

from zope.interface import Interface
from bowerstatic import (
    Bower,
    Error,
    InjectorTween,
    PublisherTween,
)
from pyramid.interfaces import IApplicationCreated
from pyramid.path import AssetResolver
from pyramid.exceptions import ConfigurationError


log = logging.getLogger('djed.static')


StaticPackageContainer = namedtuple('StaticPackageContainer', 'name path')
StaticPackage = namedtuple('StaticPackage', 'name path version container')


class IBower(Interface):
    """ Bower interface
    """


class IBowerComponents(Interface):
    """ Bower components interface
    """


class IBowerComponent(Interface):
    """ Bower component interface for local components
    """


def bower_factory_from_settings(settings):
    prefix = settings.get('djed.static.prefix', 'djed.static.')

    bower = Bower()

    bower.initialized = False
    bower.publisher_signature = settings.get(
        prefix + 'publisher_signature', 'bowerstatic')
    bower.components_path = settings.get(
        prefix + 'components_path', None)
    bower.components_name = settings.get(
        prefix + 'components_name', 'components')

    return bower


def get_bower(request):
    registry = getattr(request, 'registry', None)
    if registry is None:
        registry = request
    return registry.getUtility(IBower)


def bowerstatic_tween_factory(handler, registry):
    bower = get_bower(registry)

    def bowerstatic_tween(request):
        injector_handler = InjectorTween(bower, handler)
        publisher_handler = PublisherTween(bower, injector_handler)

        return publisher_handler(request)

    return bowerstatic_tween


def add_bower_components(config, path):
    """
    """
    registry = config.registry
    resolver = AssetResolver()
    directory = resolver.resolve(path).abspath()

    if not os.path.isdir(directory):
        raise ConfigurationError(
            "Directory '{0}' does not exist".format(directory)
        )

    bower = get_bower(registry)

    name = bower.components_name

    discr = ('djed:static', name)

    def register():
        container = StaticPackageContainer(name, directory)
        registry.registerUtility(container, IBowerComponents, name=name)

    config.action(discr, register)


def add_bower_component(config, name, path, version=None):
    """
    """
    registry = config.registry
    resolver = AssetResolver()
    directory = resolver.resolve(path).abspath()

    if not os.path.isfile(os.path.join(directory, 'bower.json')):
        raise ConfigurationError(
            "Directory '{0}' does not contain 'bower.json' file"
            .format(directory)
        )

    bower = get_bower(registry)
    container = bower.components_name

    discr = ('djed:static', name, container)

    def register():
        package = StaticPackage(name, directory, version, container)
        registry.registerUtility(package, IBowerComponent, name=name)

    config.action(discr, register)


def include(request, path_or_resource):
    """
    """
    registry = request.registry
    bower = get_bower(registry)

    name = bower.components_name

    components = bower._component_collections.get(name)

    if components is None:
        raise Error("Bower components '{0}' not found.".format(name))

    include = components.includer(request.environ)
    include(path_or_resource)


def init_static(event):
    registry = event.app.registry
    bower = get_bower(registry)

    if not bower.initialized:
        log.info("Initialize static resources...")

        for _, container in registry.getUtilitiesFor(IBowerComponents):
            bower.components(container.name, container.path)

            log.info("Add static resource collection '{0}': {1}".format(*container))

        for _, package in registry.getUtilitiesFor(IBowerComponent):
            container = bower._component_collections.get(package.container)

            if container is None:
                raise Error("Bower components '{0}' not found."
                            .format(package.container))

            component = container.load_component(
                package.path, 'bower.json', package.version, package.version is None)

            container.add(component)

            log.info("Add local static package '{0}': {1}".format(*package))

        bower.initialized = True


def includeme(config):
    bower = bower_factory_from_settings(config.registry.settings)
    config.registry.registerUtility(bower, IBower)

    config.add_tween('djed.static.bowerstatic_tween_factory')
    config.add_subscriber(init_static, IApplicationCreated)

    config.add_directive('add_bower_components', add_bower_components)
    config.add_directive('add_bower_component', add_bower_component)

    config.add_request_method(include, 'include')
    config.add_request_method(get_bower, 'get_bower')

    if bower.components_path is not None:
        config.add_bower_components(bower.components_path)
