#!/usr/bin/env bash
# -*- coding: utf-8 -*-

export DEBIAN_FRONTEND=noninteractive

aptitude update
aptitude purge -y chef chef-zero puppet puppet-common
aptitude dist-upgrade -y
ln -sf /vagrant /home/vagrant/
mkdir -p /var/www
ln -sf /vagrant/pythonkc_site /var/www/pythonkc_site

if [[ -z "$(which ansible)" ]]; then
    echo "Installing pip and Ansible..."
    aptitude install -y python-dev python-pip
    pip2 install ansible
fi

cd /home/vagrant/vagrant/ansible
sudo -H -u vagrant ansible-playbook vagrant.yml
