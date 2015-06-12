# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

# Allow host platform checks
# http://stackoverflow.com/questions/26811089/vagrant-how-to-have-host-platform-specific-provisioning-steps
module OS
  def OS.windows?
    (/cygwin|mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM) != nil
  end

  def OS.mac?
    (/darwin/ =~ RUBY_PLATFORM) != nil
  end

  def OS.unix?
    !OS.windows?
  end

  def OS.linux?
    OS.unix? and not OS.mac?
  end
end

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant-hostmanager plugin is required
  unless Vagrant.has_plugin?("vagrant-hostmanager")
    raise 'vagrant-hostmanager is not installed. run: vagrant plugin install vagrant-hostmanager'
  end

  # vagrant-hostsupdater plugin is required
  unless Vagrant.has_plugin?("vagrant-hostsupdater")
    raise 'vagrant-hostsupdater is not installed. run: vagrant plugin install vagrant-hostsupdater'
  end

  # vagrant-vbguest plugin is required
  unless Vagrant.has_plugin?("vagrant-vbguest")
    raise'vagrant-vbguest is not installed. run: vagrant plugin install vagrant-vbguest'
  end

  config.vm.define "pykcdotdev" do |pykcdotdev|
    pykcdotdev.vm.box = "debian/jessie64"
    pykcdotdev.vm.hostname = "pythonkc.dev"
    pykcdotdev.vm.network "private_network", ip: "192.168.100.101"
    if OS.unix?
      pykcdotdev.vm.synced_folder "./",  "/vagrant/", type: "nfs"
    elsif OS.windows?
      pykcdotdev.vm.synced_folder "./", "/vagrant/" # , type: "smb"
    else
      raise 'Unknown host operating system. Cannot continue.'
    end

    pykcdotdev.vm.provider "virtualbox" do |vb|
      vb.name = "pykcdotdev"
      vb.memory = 512
      vb.cpus = 2
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", "80"]
    end
    pykcdotdev.vm.provision :shell, :path => "provision.sh"
  end
end
