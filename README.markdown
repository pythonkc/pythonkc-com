# `pythonkc.com` website

[![Join the chat at https://gitter.im/pythonkc/pythonkc.com](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pythonkc/pythonkc.com?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Files for the `pythonkc.com` website.

## Development Quickstart Option 1 (vagrant)

We're going to use Vagrant and Virtualbox to run pythonkc.com inside a Debian
VM. We're using the [shell provisioner][shell] to install Ansible inside our VM and
then using Ansible to manage the environment from there. (Note: we're *not*
using the [ansible provisioner][ansible].)

First you need to install [Vagrant][vagrant] and [VirtualBox][virtualbox] and clone [our
repository][] from github.

Now copy `pythonkc_site/.env.example` to `pythonkc_site/.env` and add
your own [meetup api key][meetup] and a unique [django secret key][django] (`.env` will
be ignored by git)

Then you have to install some vagrant plugins and build your vagrant box:

```
vagrant plugin install vagrant-vbguest
vagrant plugin install vagrant-hostmanager
vagrant plugin install vagrant-hostsupdater
vagrant up
```

`vagrant up` will run `provision.sh` which runs ansible on the VM.

We've done this so you don't have to install ansible on your local machine.

If you'd prefer you can always ssh in and run/re-run the provisioner manually
(the output is a little nicer this way):

```
vagrant ssh
cd ~/vagrant/ansible
ansible-playbook vagrant.yml
```

To run the Django development server:

```
vagrant ssh
django-admin runserver 192.168.100.101:8000
```

Now go to `http://192.168.100.101:8000` in your browser. You can edit the files
on your local machine and the server should reload automatically.

For now, this is a Python 2 project. If you want to start using Python 3
and help us fix our problems, set Ansible's `python_version` variable to 3
and it will build the virtualenv using Python 3:

```
ansible-playbook vagrant.yml -e python_version=3
```


## Development Quickstart Option 2 (virtualenv)

```
mkvirtualenv pythonkc
git clone git@github.com:pythonkc/pythonkc-com.git
cd pythonkc.com/pythonkc_site
pip install -r requirements/project.txt
python manage.py runserver
```

Profit! $$$

## More Detailed Instructions

See: docs/local_development



[ansible]: http://docs.vagrantup.com/v2/provisioning/ansible.html
[django]: http://www.miniwebtool.com/django-secret-key-generator/
[meetup]: https://secure.meetup.com/meetup_api/key/
[shell]: http://docs.vagrantup.com/v2/provisioning/shell.html
[vagrant]: https://www.vagrantup.com/downloads.html
[virtualbox]: https://www.virtualbox.org
