#!/usr/bin/env bash
# -*- coding: utf-8 -*-

export DEBIAN_FRONTEND=noninteractive

aptitude update
aptitude dist-upgrade -y
aptitude install build-essential -y
aptitude install linux-headers-amd64 -y
ln -sf /vagrant /home/vagrant/

if [[ -z "$(which ansible)" ]]; then
    echo "Installing Ansible..."
    aptitude install -y python3 python3-dev python3-pip ansible
fi

cd /home/vagrant/vagrant/ansible
ansible-playbook vagrant.yml
