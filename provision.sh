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
    echo "Installing Ansible..."
    aptitude install -y python3 python3-dev python3-pip ansible
fi

cd /home/vagrant/vagrant/ansible
ansible-playbook vagrant.yml
