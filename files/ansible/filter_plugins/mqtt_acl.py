from ansible.errors import AnsibleFilterError
from string import Template
import os

# mqtt_acl, (C)2024 by Jan-Piet Mens <jp@mens.de>
# This Ansible Jinja filter tests if a fragment file for the specified username
# exists; if so it is read in, otherwise a default ACL for the particular user
# is emitted.

def mqtt_acl(username):

    default_acl = """
user $U
topic readwrite owntracks/$U/#
topic read owntracks/+/+
topic read owntracks/+/+/event
topic read owntracks/+/+/info
"""

    path = os.path.join("acl", "%s.acl" % username)
    if os.path.exists(path):
        with open(path, "r") as f:
            fragment = f.read()
            return fragment

    return Template(default_acl).safe_substitute(U=username)

class FilterModule(object):
    def filters(self):
        return {
            'mqtt_acl': mqtt_acl,
        }
