# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant-hostmanager plugin is required
  unless Vagrant.has_plugin?("vagrant-hostmanager")
    raise 'vagrant-hostmanager is not installed. run: vagrant plugin install vagrant-hostmanager'
  end

  # vagrant-vbguest plugin is required
  unless Vagrant.has_plugin?("vagrant-vbguest")
    raise 'vagrant-vbguest is not installed. run: vagrant plugin install vagrant-vbguest'
  end

  config.vm.define "pykcdotdev" do |pykcdotdev|
    pykcdotdev.vm.box = "box-cutter/debian81"
    pykcdotdev.vm.hostname = "pythonkc.dev"
    pykcdotdev.vm.network "private_network", ip: "192.168.100.101"
    pykcdotdev.vm.synced_folder "./",  "/vagrant/"
    pykcdotdev.vm.synced_folder "./pythonkc_site", "/var/www/pythonkc_site"
    # TODO: Create a synced folder location for Ansible playbooks

    pykcdotdev.vm.provider "virtualbox" do |vb|
      vb.name = "pykcdotdev"
      vb.memory = 512
      vb.cpus = 2
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", "80"]
    end
    pykcdotdev.vm.provision :shell, :path => "provision.sh"
  end
end
