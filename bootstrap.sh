#!/bin/sh

if ! [ -f configuration.yaml ]; then
	echo "Have you forgotten to copy and edit configuration.yaml?"
	exit 2
fi

if ! which ansible-playbook > /dev/null; then
	echo "Attempting to install ansible-core"
	sudo apt update
	sudo apt install -qqy ansible
fi

# people who know Ansible might be questioning some of the practices
# here such as why not use ansible.cfg right here, or templates in
# templates/ directory; the intention is to hide as much of the
# stuff users require to know as possible.

export ANSIBLE_CONFIG=files/ansible/ansible.cfg

ansible-playbook owntracks-setup.yml "$@"
