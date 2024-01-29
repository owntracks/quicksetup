# Swiped from https://stackoverflow.com/questions/69036942/
#
# Custom filters for use with ansible
def mosquitto_passwd(passwd):
    from hashlib import pbkdf2_hmac
    from base64 import b64encode
    import secrets

    # See https://github.com/eclipse/mosquitto/blob/master/src/password_mosq.h
    iterations = 101

    salt = secrets.token_bytes(12)
    dk = pbkdf2_hmac('sha512',
                     bytes(passwd, 'utf-8'),
                     salt,
                     iterations
                     )
    return (
            "$7$" + str(iterations) + "$" +
            b64encode(salt).decode() + "$" +
            b64encode(dk).decode()
            )

class FilterModule(object):
    def filters(self):
        return {
            'mosquitto_passwd': mosquitto_passwd,
        }
