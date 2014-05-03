xsendfile-example
=================

Django project that shows how to serve files with Apache and X-SENDFILE by using [django-sendfile](https://github.com/johnsensible/django-sendfile).

## Usage

Install [Vagrant](http://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) (Vagrant is a tool to quickly spin up and bootstrap (aka provision) VMs).

Clone this repository and edit the `Vagrantfile`:

    config.vm.synced_folder "/PATH/TO/MEDIA/DIRECTORY/ON/HOST/MACHINE", "/home/vagrant/media"

Run `vagrant up`. The first time it will take a while because it will download a VirtualBox image. If everything ran through you should be to access the site at http://localhost:8080/.

If you want to run the project using Django's development server you have to set another backend in `settings.py`:

    SENDFILE_BACKEND = 'sendfile.backends.development'
