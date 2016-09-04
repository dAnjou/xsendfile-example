from tempfile import NamedTemporaryFile
from os.path import join, abspath
from fabric.api import *
from fabric.colors import red
from fabtools import python
from fabtools.vagrant import vagrant

USAGE=red("""Usage:
    fab -H <host> deploy       - Deploy on <host>
    fab vagrant:default deploy - Deploy on a Vagrant VM
    fab vagrant:ansible deploy - Deploy on an Ansible provisioned Vagrant VM
""")
PACKAGE_NAME = 'xsendfile-example.tar'
RED_DOT = """iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAA
ABGdBTUEAALGPC/xhBQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9Y
GARc5KB0XV+IAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1
Q72QlbgAAAF1JREFUGNO9zL0NglAAxPEfdLTs4BZM4DIO4C7OwQg2JoQ9LE1
exdlYvBBeZ7jqch9//q1uH4TLzw4d6+ErXMMcXuHWxId3KOETnnXXV6MJpcq
2MLaI97CER3N0vr4MkhoXe0rZigAAAABJRU5ErkJggg=="""


@task
def deploy():
    """
    deploy xsendfile_example application
    """
    if not env.hosts:
        abort(USAGE)
    # create package from code
    commit = local('git stash create', capture=True)
    if not commit:
        commit = 'HEAD'
    local('git archive %s > %s' % (commit, PACKAGE_NAME))
    # copy package to VM
    put(PACKAGE_NAME, '~')
    with cd('~'):
        # install package
        run('mkdir xsendfile_example', quiet=True)
        with cd('xsendfile_example'):
            run('tar -xf ~/%s' % PACKAGE_NAME)
            # install application dependencies
            with python.virtualenv('/home/vagrant/venv'):
                python.install_requirements('requirements.txt')
        # create sample media file
        run('mkdir media', quiet=True)
        with cd('media'):
            run('echo "%s" | base64 -d > red_dot.png' % RED_DOT)
    sudo('service apache2 restart')
