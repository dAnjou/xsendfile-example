from tempfile import NamedTemporaryFile
from fabric.api import *

PACKAGE_NAME = 'xsendfile-example.tar'
RED_DOT = """iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAA
ABGdBTUEAALGPC/xhBQAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9Y
GARc5KB0XV+IAAAAddEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIFRoZSBHSU1
Q72QlbgAAAF1JREFUGNO9zL0NglAAxPEfdLTs4BZM4DIO4C7OwQg2JoQ9LE1
exdlYvBBeZ7jqch9//q1uH4TLzw4d6+ErXMMcXuHWxId3KOETnnXXV6MJpcq
2MLaI97CER3N0vr4MkhoXe0rZigAAAABJRU5ErkJggg=="""


# use SSH configuration of the vagrant VM
env.use_ssh_config = True
with lcd(env.vagrant_home):
    ssh_config = local('vagrant ssh-config', capture=True)
with NamedTemporaryFile(delete=False) as f:
    f.write(ssh_config)
env.ssh_config_path = f.name
env.hosts = ['default']


def deploy():
    # create package from code
    commit = local('git stash create', capture=True)
    local('git archive %s > %s' % (commit, PACKAGE_NAME))
    # copy package to VM
    put(PACKAGE_NAME, '~')
    with cd('~'):
        # install package
        run('mkdir xsendfile_example', quiet=True)
        with cd('xsendfile_example'):
            run('tar -xf ~/%s' % PACKAGE_NAME)
        # create sample media file
        run('mkdir media', quiet=True)
        with cd('media'):
            run('echo "%s" | base64 -d > red_dot.png' % RED_DOT)
    # setup VirtualHost
    put('xsendfile_example.vhost',
        '/etc/apache2/sites-available/xsendfile_example', use_sudo=True)
    sudo('a2dissite 000-default')
    sudo('a2ensite xsendfile_example')
    sudo('service apache2 restart')
