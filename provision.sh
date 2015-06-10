#!/usr/bin/env bash
# -*- coding: utf-8 -*-

export DEBIAN_FRONTEND=noninteractive

aptitude update
aptitude dist-upgrade -y
aptitude install -y python3 python3-dev python3-pip ansible
ln -sf /vagrant /home/vagrant/
# TODO: Run Ansible playbooks
