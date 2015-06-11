# PYTHONKC.COM WEBSITE

Files for the PythonKC.com website.

## Development Quickstart Option 1 (vagrant)

```
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

## Development Quickstart Option 2 (virtualenv)

```
mkvirtualenv pythonkc
git clone git@github.com:pythonkc/pythonkc.com.git
cd pythonkc.com/pythonkc_site
pip install -r requirements/project.txt
python manage.py runserver
```

Profit! $$$

## More Detailed Instructions

See: docs/local_development
