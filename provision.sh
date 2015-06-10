#!/usr/bin/env bash
# -*- coding: utf-8 -*-

export DEBIAN_FRONTEND=noninteractive

ln -sf /vagrant /home/vagrant/

if [[ -z "$(which ansible)" ]]; then
    echo "Installing ansible"
    aptitude update
    aptitude install -y python3 python3-dev python3-pip ansible
fi

cd /home/vagrant/vagrant/ansible
ansible-playbook vagrant.yml
