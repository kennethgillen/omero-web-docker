#!/usr/bin/env python
# 1. Run .omero files from /opt/omero/web/config/
# 2. Set omero config properties from CONFIG_ envvars
#    Variable names should replace "." with "_" and "_" with "__"
#    E.g. CONFIG_omero_web_public_enabled=false

import os
from subprocess import call
from re import sub


CONFIG_OMERO = '/opt/omero/web/config/omero-web-config-update.sh'
OMERO = '/opt/omero/web/OMERO.web/bin/omero'

if os.access(CONFIG_OMERO, os.X_OK):
    rc = call([CONFIG_OMERO])
    assert rc == 0

for (k, v) in os.environ.iteritems():
    if k.startswith('CONFIG_'):
        prop = k[7:]
        prop = sub('([^_])_([^_])', r'\1.\2', prop)
        prop = sub('__', '_', prop)
        value = v
        rc = call([OMERO, 'config', 'set', '--', prop, value])
        assert rc == 0
