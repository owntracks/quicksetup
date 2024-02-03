# mkpasswords.py, JPM, take list of users, add random
# password if a dict has no 'password' element in it.

import secrets
import os

def mkpasswords(users, directory):
    newusers = []

    # print(directory)

    ## users.append(dict(tid="rr", username="_rr"))

    for u in users:
        u["username"] = u["username"].lower()
        u["devicename"] = u["devicename"].lower()
        if not "password" in u:
            # if file exists, read its content (a.k.a password lookup)
            p = os.path.join(directory, u["username"] + ".pass")
            if os.path.exists(p):
                with open(p, "r") as f:
                    u["password"] = f.read().rstrip()
            else:
                u["password"] = secrets.token_urlsafe(16)

        newusers.append(u)

    return newusers

class FilterModule(object):
    def filters(self):
        return {
            'mkpasswords': mkpasswords,
        }
