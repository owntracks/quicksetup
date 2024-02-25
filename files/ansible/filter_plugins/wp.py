from ansible.errors import AnsibleFilterError
from string import Template
import os
import json

# wp, (C)2024 by Jan-Piet Mens <jp@mens.de>
# Ansible Jinja filter to test if a file waypoints/username.json or
# waypoints/username.otrw can be read. If so, the array of waypoints from either
# is read and merged into the list of waypoints contained in
# `data'.

def wp(data, username):

    new_waypoints = []

    path = os.path.join("waypoints", "%s.json" % username)
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                new_waypoints = json.loads(f.read())
            except:
                raise AnsibleFilterError("Cannot parse JSON from %s" % path)

    path = os.path.join("waypoints", "%s.otrw" % username)
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                d = json.loads(f.read())
                if "waypoints" not in d and d.get("_type", "unknown") != "waypoints":
                    raise AnsibleFilterError("Not an OTRW file in %s" % path)
                new_waypoints = d["waypoints"]
            except:
                raise AnsibleFilterError("Cannot parse OTRW from %s" % path)

    return data + new_waypoints


class FilterModule(object):
    def filters(self):
        return {
            'wp': wp,
        }
