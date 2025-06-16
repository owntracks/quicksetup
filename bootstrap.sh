#!/bin/bash

if [ $(id -u) -ne 0 ]; then
	echo "Please run $0 as root or using sudo!"
	exit 2
fi

cd "$(dirname $0)" || { echo "Can't cd to boostrap" >&2; exit 2; }

if ! [ -f configuration.yaml ]; then
	echo "Have you forgotten to copy and edit configuration.yaml?"
	exit 2
fi

printf "This program will overwrite existing files! Hit ENTER to continue: "
read ans

ADIR=/usr/local/owntracks/ansible

if ! [ -x $ADIR/bin/ansible-playbook ]; then
	echo "Attempting to install ansible and prerequisites for bootstrapping"
	sudo apt update
	sudo NEEDRESTART_MODE=a apt -qq install -y python3-pip python3-venv

	# create a dedicated user for Ansible (without login capabilities)
	#
	# ansible:x:998:998:Ansible:/usr/local/owntracks/ansible:/bin/false
	#
	useradd --home-dir $ADIR \
		--create-home \
		--comment Ansible \
		--system \
		--shell /bin/false \
		ansible

	# install ansible core into a python venv
	sudo -u ansible python3 -mvenv $ADIR
	sudo -u ansible $ADIR/bin/pip install ansible-core

	sudo -u ansible $ADIR/bin/ansible-galaxy collection install \
		community.general \
		community.crypto

fi

# people who know Ansible might be questioning some of the practices
# here such as why not use ansible.cfg right here, or templates in
# templates/ directory; the intention is to hide as much of the
# stuff users require to know as possible.

export ANSIBLE_CONFIG=files/ansible/ansible.cfg

/usr/local/owntracks/ansible/bin/ansible-playbook owntracks-setup.yml "$@"
