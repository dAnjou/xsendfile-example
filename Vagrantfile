# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.provider "virtualbox" do |vb|
        vb.customize ["modifyvm", :id, "--memory", "1024"]
    end

    config.vm.define "ansible", autostart: false do |ansible_machine|
        ansible_machine.vm.network "forwarded_port", guest: 80, host: 8081
        ansible_machine.vm.provision "ansible" do |ansible|
            ansible.playbook = "./provisioning/ansible/playbook.yml"
        end
    end

    config.vm.define "default", autostart: false do |default_machine|
        default_machine.vm.network "forwarded_port", guest: 80, host: 8080
        default_machine.vm.provision "shell",
            inline: "apt-get update && \
            apt-get install -y \
            apache2 libapache2-mod-wsgi libapache2-mod-xsendfile python-pip \
            python-virtualenv &&
            a2enmod wsgi && \
            a2enmod xsendfile && \
            a2dissite 000-default"
        default_machine.vm.provision "file",
            source: "./provisioning/default/xsendfile_example.vhost",
            destination: "/home/vagrant/xsendfile_example.vhost"
        default_machine.vm.provision "shell",
            inline: "cp /home/vagrant/xsendfile_example.vhost \
            /etc/apache2/sites-available/xsendfile_example.conf && \
            a2ensite xsendfile_example && \
            service apache2 restart"
        default_machine.vm.provision "shell",
            inline: "virtualenv /home/vagrant/venv",
            privileged: false
    end

end
