# mkpasswords.py, JPM, take list of users, add random
# password if a dict has no 'password' element in it.

from ansible.errors import AnsibleFilterError
import secrets
import os

# make a note of first seen users and their passwords; more than one
# configuration entry for the same user will re-use its first password
seen_users = {}

def mkpasswords(users, directory):
    newusers = []

    # print(directory)

    ## users.append(dict(tid="rr", username="_rr"))

    for u in users:
        low_u = u["username"].lower()
        if not "password" in u:
            # if file exists, read its content (a.k.a password lookup)
            p = os.path.join(directory, u["username"] + ".pass")
            if os.path.exists(p):
                with open(p, "r") as f:
                    u["password"] = f.read().rstrip()
            else:
                u["password"] = secrets.token_urlsafe(16)
        if low_u in seen_users:
            u["password"] = seen_users[low_u]

        seen_users[low_u] = u["password"]

        if "secret" in u:
            ''' if the encryptionKey secret begins with a slash, it's
                a file which contains the secret '''
            if u["secret"].startswith("/"):
                file = u["secret"]
                if os.path.exists(file):
                    with open(file, "r") as f:
                        u["secret"] = f.read().rstrip()
                else:
                    raise AnsibleFilterError("mkpasswords: cannot open file {0} for user {1}".format(file, u["username"]))


        newusers.append(u)

    return newusers

class FilterModule(object):
    def filters(self):
        return {
            'mkpasswords': mkpasswords,
        }
