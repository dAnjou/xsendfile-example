# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.synced_folder ".", "/home/vagrant/xsendfile_example"
  config.vm.synced_folder "/home/max/Bilder/Wallpaper", "/home/vagrant/media"
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
  config.vm.provision "shell", path: "./root_provision.sh"
  config.vm.provision "shell", path: "./user_provision.sh",
    privileged: false
  config.vm.provision "shell", inline: "service apache2 restart"
end
