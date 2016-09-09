xsendfile-example
=================

Django application that shows how to [serve files with Apache and X-SENDFILE](https://speakerdeck.com/danjou/protecting-static-files-in-your-web-app)
by using [django-sendfile](https://github.com/johnsensible/django-sendfile).

![sequence diagram showing a request/response cycle with X-SENDFILE](diagram.png)

---

This project also serves as a playground for other technologies.

## Usage

This is a pretty normal Django application, nothing too fancy. So you could just
grab the `xsendfile_example` folder and run with it. But to make it a bit easier
I provide 3 options to run this application.

### Docker

Install [Docker](https://www.docker.com/).

*Docker lets you provision container images including your application which you
can then deploy and run.*

Build the image:

    docker build --tag xsendfile-example .

Run the container:

    docker run --rm -p 8082:80 -v /path/to/your/data:/data xsendfile-example

Browse to http://localhost:8082/

### Vagrant + Fabric

Install [Vagrant](http://www.vagrantup.com/), [VirtualBox](https://www.virtualbox.org/)
and [Fabric](http://www.fabfile.org/)+[fabtools](http://fabtools.readthedocs.io).

*Vagrant helps with provisioning VMs especially for development, in this case
VirtualBox VMs. Fabric is a command-line tool for application deployment via
SSH.*

Boot and provision the VM:

    vagrant up default

Deploy the application

    fab vagrant:default deploy

Browse to http://localhost:8080/

### Vagrant + Fabric + Ansible

This option works pretty much the same as the one before except that it uses
[Ansible](https://www.ansible.com/), so you have to install that too.

*Ansible is a configuration management tool that lets you automate server
installations not only for development but also for production.*

Boot and provision the VM:

    vagrant up ansible

Deploy the application

    fab vagrant:ansible deploy

Browse to http://localhost:8081/

## Notes

If you want to run the project using Django's development server you have to set
another backend in `xsendfile_example/settings.py`:

    SENDFILE_BACKEND = 'sendfile.backends.development'
