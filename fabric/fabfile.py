
from __future__ import with_statement

import os
import sys
from getpass import getuser

from fabric.api import cd
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import settings


################
# Config setup #
################

conf = {}
if sys.argv[0].split(os.sep)[-1] == "fab":
    # Ensure we import settings from the current dir
    try:
        conf = __import__("settings", globals(), locals(), [], 0).FABRIC
        try:
            conf["HOSTS"][0]
        except (KeyError, ValueError):
            raise ImportError
    except (ImportError, AttributeError):
        print "Aborting, no hosts defined."
        exit()

env.user = conf.get("SSH_USER", getuser())
env.hosts = conf.get("HOSTS", [])


##############
# Deployment #
##############

def deploy():
    code_dir = '~/www/missionchinesefood'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:20twoes/mcf-static.git %s" % code_dir)
    with cd(code_dir):
        run('git pull')

