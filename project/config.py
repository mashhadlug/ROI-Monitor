#coding: utf-8
import os

class DefaultConfig(object):
    DEBUG = True
    DEPLOYMENT = False

    ACCEPT_LANGUAGES = ['fa', 'en']
    
    BABEL_DEFAULT_LOCALE = 'fa'
    BABEL_DEFAULT_TIMEZONE = 'Asia/tehran'

    CSRF_ENABLED = True
    SECRET_KEY = '\x05m\xa8\x8b\r\xd94\xc7\x81\x99\xdb\x06<-cwT\x0fk'\
        '\x88\xb9\xb6\x18\xceV\x89\xb8&*\x06\xe8\xde'

    SITE_NAME = u'انجمن برنامه نویسان پایتون ایران'
    logger_name = 'pug'
    # Blueprint haye nasb shode dar app bayad be in list ezafe beshan
    INSTALLED_BLUEPRINTS = (
        'site',
        'sensors',
        'rest',
    )

class DeploymentConfig(DefaultConfig):
    DEBUG = False
    TESTING = False
    DEPLOYMENT = True


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    CACHE_TYPE = 'null'
    #PROPAGATE_EXCEPTIONS = True
