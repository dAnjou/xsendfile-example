# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
  config.vm.define "default", autostart: false do |default|
    default.vm.provision "shell", path: "./provisioning/default/root_provision.sh"
    default.vm.provision "shell", path: "./provisioning/default/user_provision.sh",
      privileged: false
  end
  config.vm.define "ansible", autostart: false do |ansible|
    ansible.vm.provision "ansible" do |ansible_provisioner|
      ansible_provisioner.playbook = "./provisioning/ansible/playbook.yml"
    end
  end
end
