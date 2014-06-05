#coding: utf-8
import os

class DefaultConfig(object):
    DEBUG = True
    DEPLOYMENT = False

    ACCEPT_LANGUAGES = ['fa', 'en']

    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'Asia/tehran'

    SITE_NAME = u'انجمن برنامه نویسان پایتون ایران'
    logger_name = 'pug'
    # Blueprint haye nasb shode dar app bayad be in list ezafe beshan
    INSTALLED_BLUEPRINTS = (
        'site',
        'sensors',
    )

class DeploymentConfig(DefaultConfig):
    DEBUG = False
    TESTING = False
    DEPLOYMENT = True


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    CACHE_TYPE = 'null'
    #PROPAGATE_EXCEPTIONS = True
