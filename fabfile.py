from __future__ import with_statement
from fabric.api import cd
from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import settings

env.hosts = ['nsquareu@nsquare.us']


def deploy():
    code_dir = '~/www/missionchinesefood'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:20twoes/mcf-static.git %s" % code_dir)
    with cd(code_dir):
        run('git pull')

