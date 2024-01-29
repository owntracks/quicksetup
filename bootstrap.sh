#!/bin/sh

if ! which -s ansible; then
	echo "Attempting to install ansible-core"
	sudo apt update
	sudo apt install -y ansible-core
fi

# people who know Ansible might be questioning some of the practices
# here such as why not use ansible.cfg right here, or templates in
# templates/ directory; the intention is to hide as much of the
# stuff users require to know as possible.

export ANSIBLE_CONFIG=files/ansible/ansible.cfg

ansible-playbook files/owntracks-setup.yml
