# implementation notes

- `bootstrap.sh` is a simple shell script which installs Ansible and launches our main playbook.
- people who know Ansible might be questioning some of the practices here such as why not use and `ansible.cfg` right in the main directory, or why are templates not in a `templates` directory. The main idea is to hide as much of the internals from users as possible. We do this in order to make things look simple.
- the configuration ([configuration.yaml.example](configuration.yaml.example)) is, again, supposed to be as simple as possible, and we chose this syntax to make it a) easy to integrate in Ansible, and b) hopefully easy to edit for users who'll be using this.
- wherever possible we have chosen what we believe are sensible defaults.
- we explicitly opted to support only new'ish Debian-type systems at this point. If we find people want support for other operating systems we'll gladly a) accept patches or b) contribute.
- there are most definitely too many passwords lying around in clear text:
   - a password may be specified per/user in `configuration.yaml`
   - if it isn't, a random 20-character password is generated into `/usr/local/owntracks/userdata/*.pass`, different for each user
   - passwords are, again in clear, written to `*.otrc` for device configuration
   - a password for a _local reader_ `_lr` is stored there and in the first friend's `~/.config/mosquitto_[ps]ub`
   - solutions? many probably, but most too unpractical?
-
