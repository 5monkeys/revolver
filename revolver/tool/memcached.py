# -*- coding: utf-8 -*- 

from revolver import command
from revolver import package

def install():
    package.install('memcached')

def ensure():
    if command.exists('memcached'):
        return

    install()
    
