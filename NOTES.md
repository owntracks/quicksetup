# implementation notes

- `bootstrap.sh` is a simple shell script which installs Ansible and launches our main playbook.
   - create a dedicated user `ansible`
   - install ansible-core plus needed collections into a virtualenv at /usr/local/owntracks/ansible
- people who know Ansible might be questioning some of the practices here such as why not use and `ansible.cfg` right in the main directory, or why are templates not in a `templates` directory. The main idea is to hide as much of the internals from users as possible. We do this in order to make things look simple, maybe even simpler than they are.
- the configuration ([configuration.yaml.example](configuration.yaml.example)) is, again, supposed to be as simple as possible, and we chose this syntax to make it a) easy to integrate in Ansible, and b) hopefully easy to edit for users who'll be using this.
- wherever possible we have chosen what we believe are sensible defaults.
- we explicitly opted to support only new'ish Debian-type systems at this point. If we find people want support for other operating systems we'll gladly a) accept patches or b) contribute.
- there are most definitely too many passwords lying around in clear text:
   - a password may be specified per/user in `configuration.yaml`
   - if it isn't, a random 20-character password is generated into `/usr/local/owntracks/userdata/*.pass`, different for each user
   - passwords are, again in clear, written to `*.otrc` for device configuration
   - a password for a _local reader_ `_lr` is stored there and in the first friend's `~/.config/mosquitto_[ps]ub`
   - solutions? many probably, but most too unpractical?
   - passwords are hashed for _nginx_ and are managed idempotently
     ```console
     $ head -1 /usr/local/owntracks/userdata/htpasswd
     jane:$apr1$JoJGeeu.$E02WF5lv97aX6vqzwboCo1
     ```
   - passwords are hashed for _Mosquitto_ and are resalted at each `./bootstrap.sh`
     ```console
     $ head -1 /etc/mosquitto/mosquitto.pw
     jane:$7$101$JCER9MacrEgNIBgK$EY+qYeAoeer3Fp4KOFPSy+tu2+JjTpQHCjZzFJqnhOCH2EPyvmy8e50HLyIDKodqKO2Eln6i4/wbIW8/V/LG+g==
     ```
- we use _lego_ for ACME enrollment b/c we've had very good experience with it (admittedly mostly with `dns-01` challenge). _cron_ is configured to run the enroller which _stops_ _nginx_ during the short window it takes to renew a certificate.
