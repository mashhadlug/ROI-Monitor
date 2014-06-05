#from python
import os
import sys
import logging
import logging.handlers

#from flask
from flask import Flask, request, jsonify, redirect, url_for, flash, g, session
from flask.ext.babel import Babel
from flask.ext.babel import gettext as _

#from project
from project.config import DefaultConfig as base_config

__all__ = ['create_app', 'create_simple_app']

DEFAULT_APP_NAME = 'project'


def create_app(config=None, app_name=DEFAULT_APP_NAME):
    """
    Tabe asli hast ke app ro misaze va configesh mikone.
    be in tabe tanzimate barname tahte name config ersal mishe va on tabzimat dar dakhele object
    app zakhire va negahdari mishe

    @param config: class ya objecte haviye tanzimate kolliye app mibashad.
    @param app_name: name asliye narm afzar
    """

    #TODO: static_folder va template_folder bayad dar method joda set beshe
    app = Flask(app_name, static_folder='media/statics', template_folder='media/templates')

    configure_app(app, config)
    configure_blueprints(app)
    configure_errorhandlers(app)
    configure_template(app)
    return app


def configure_app(app, config):
    """
    tanzimate kolli app ke mamolan dar yek file zakhore mishavat tavasote in tabe
    megdar dehi va load mishavad
    """

    # config default ro dakhele app load mikone
    app.config.from_object(base_config())
    #sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    if config is not None:
        # agar config degari be create_app ersal shode bashe dar in bakhsh load mishe
        # agar tanzimate in bakhsh gablan va dakhele defalt config tanzim shode bashe dobare nevisi mishe
        app.config.from_object(config)

    # dar sorati ke environment variable baraye tanzimat set shode bashe ham load mishe
    app.config.from_envvar('project_CONFIG', silent=True)


def configure_blueprints(app):
    """
    Tanzimate marbot be blueprint ha va load kardan ya nasbe onha ro inja anjam midim
    """

    app.config.setdefault('INSTALLED_BLUEPRINTS', [])
    blueprints = app.config['INSTALLED_BLUEPRINTS']
    for blueprint_name in blueprints:
        bp = __import__('project.apps.%s' % blueprint_name, fromlist=['views'])

        try:
            mod = __import__('project.%s'%blueprint_name, fromlist=['urls'])
        except ImportError:
            pass
        else:
            mod.urls.add_url_rules(bp.views.mod)
        try:
            app.register_blueprint(bp.views.mod)
        except:
            # report has no views
            pass


def configure_errorhandlers(app):
    """
    tavasote in method baraye error haye asli va mamol khatahaye monaseb bargasht dade mishavad
    """

    if app.testing:
        return

    @app.errorhandler(404)
    def page_not_found(error):
        # import_cart_to_list(error)
        return ('Sorry, page not found'), 404

    @app.errorhandler(403)
    def forbidden(error):
        # import_cart_to_list(error)
        return ('Sorry, not allowed'), 403

    @app.errorhandler(500)
    def server_error(error):
        # import_cart_to_list(error)
        return ('Sorry, an error has occurred'), 500

    @app.errorhandler(401)
    def unauthorized(error):
        # import_cart_to_list(error)
        return ("Login required") , 401


def configure_before_handlers(app):
    pass


def configure_template (app):
  """ Function doc """
  base_dir = os.path.dirname(os.path.abspath(__file__))
  app.template_folder = base_dir + '/templates'
  app.static_folder = base_dir + '/static'
  print app.template_folder, app.static_folder
