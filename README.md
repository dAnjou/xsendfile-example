xsendfile-example
=================

Django project that shows how to serve files with Apache and X-SENDFILE by using [django-sendfile](https://github.com/johnsensible/django-sendfile).

## Usage

Install [Vagrant](http://www.vagrantup.com/), [VirtualBox](https://www.virtualbox.org/) and [Fabric](http://www.fabfile.org/).

*Vagrant is a tool to quickly spin up and bootstrap (aka provision) VMs, in this case VirtualBox VMs. Fabric is a command-line tool for application deployment via SSH.*

Clone this repository.

Run `vagrant up`. The first time it will take a while because it will download a VirtualBox image. If everything ran through you should be to access the site at http://localhost:8080/.

Run `fab --set=vagrant_home="." deploy`. `vagrant_home` is the location where the `Vagrantfile` lies. This is needed to get the SSH config for the vagrant VM to be able to login.

## Notes

If you want to run the project using Django's development server you have to set another backend in `settings.py`:

    SENDFILE_BACKEND = 'sendfile.backends.development'
