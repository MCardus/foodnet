# Ubuntu provisioning

# Upgrade system
sudo apt-get update && sudo apt-get -y upgrade


# Install essential packages
sudo apt-get install -y build-essential python git libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev

# Install python pip
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
rm -fr get-pip.py

# Ansible installation
sudo pip install ansible
