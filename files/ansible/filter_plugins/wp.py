from ansible.errors import AnsibleFilterError
from string import Template
import os
import yaml

# wp, (C)2024 by Jan-Piet Mens <jp@mens.de>
# Ansible Jinja filter to test if a file waypoints/username.json, username.yaml, or
# username.otrw can be read. If so, the array of waypoints from either
# is read and merged into the list of waypoints contained in
# `data'.


def test_object(data, path):

    for waypoint in data:
        for key in [ "_type", "desc", "tst", "rad", "lat", "lon" ]:
            if key not in waypoint:
                raise AnsibleFilterError("Key [%s] is missing in %s" % (key, path))

def load_file(username, filetype):

    data = []
    path = os.path.join("waypoints", "%s.%s" % (username, filetype))
    if os.path.exists(path):
        with open(path, "r") as f:
            try:
                data = yaml.safe_load(f)
                if filetype == "otrw":
                    if type(data) == dict and "waypoints" not in data and data.get("_type", "unknown") != "waypoints":
                        raise AnsibleFilterError("Not an OTRW file in %s" % path)
                    else:
                        data = data["waypoints"]
                test_object(data, path)

            except:
                raise AnsibleFilterError("Cannot load %s from %s" % (filetype, path))

    return data

def wp(waypoints, username):

    additional_wp = []

    for filetype in [ "json", "otrw", "yaml" ]:
        wps = load_file(username, filetype)
        if wps is not None:
            additional_wp = additional_wp + wps

    return waypoints + additional_wp


class FilterModule(object):
    def filters(self):
        return {
            'wp': wp,
        }
