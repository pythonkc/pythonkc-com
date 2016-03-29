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
    raise 'vagrant-vbguest is not installed. run: vagrant plugin install vagrant-vbguest'
  end

  config.vm.define "pykcdevel" do |pykcdevel|
    pykcdevel.vm.box = "debian/jessie64"
    pykcdevel.vm.hostname = "pythonkc.devel"
    pykcdevel.vm.network "private_network", type: "dhcp"
    if OS.unix?
      pykcdevel.vm.synced_folder "./", "/vagrant/", type: "nfs"
    elsif OS.windows?
      pykcdevel.vm.synced_folder "./", "/vagrant/", type: "smb"
    else
      raise 'Unknown host operating system. Cannot continue.'
    end

    pykcdevel.vm.provider "virtualbox" do |vb|
      vb.name = "pykcdevel"
      vb.memory = 512
      vb.cpus = 2
      vb.customize ["modifyvm", :id, "--cpuexecutioncap", "80"]
    end
    pykcdevel.vm.provision :shell, :path => "provision.sh"
  end
end
