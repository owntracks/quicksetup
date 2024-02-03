# quicksetup

Work in progress 

## features

- Let's Encrypt certificate enrollment and renewal (cron)
- MQTT broker (Mosquitto) and HTTP server (Apache) secured with SSL/TLS
- configured OwnTracks [Recorder](https://github.com/owntracks/recorder)
- [Frontend](https://github.com/owntracks/frontend)
- automatic configuration of friends, each of which can see eachother via MQTT in the apps and on Frontend, etc.
- users can download pre-configured [.otrc remote configuration files](https://owntracks.org/booklet/features/remoteconfig/) for ease of configuration of the apps
- users are created with random passwords
- these same users inserted into `mosquitto.pw`, `mosquitto.acl`, and `htpasswd`
- optional but recommended [OpenCageData](https://opencagedata.com/) for reverse geo. (Sign up for [a free account](https://opencagedata.com/users/sign_up) you use with OwnTracks.) Location data is cached by the Recorder and stored alongside location publishes, served from the API
- should be able to support a dozen or more friends on a 512MB VPS
- `mosquitto_pub`/`mosquitto_sub` pre-configured to use local broker with files in `$HOME/.config/`
- ufw firewall with open TCP ports at 22, 80, 443, 8883
- jq and jo
- bootstrapping of installation
- Recorder Views (without requiring basic auth)

## installation

1. Get a copy of all files in this repository:
   1. either install git and clone the repository:
      ```console
      apt install -y git
      git clone https://github.com/owntracks/quicksetup
      cd quicksetup
      ```
   2. or download a copy of the files and extract them:
      ```console
      curl -LO https://github.com/owntracks/quicksetup/archive/master.tar.gz
      tar xf master.tar.gz
      cd quicksetup-main
      ```

2. Make a copy of the [configuration file](configuration.yaml.example) used for setup and edit its content.
   ```console
   cp configuration.yaml.example configuration.yaml
   nano configuration.yaml
   ```

3. Launch the installer which will install packages and configure services.
   ```console
   $ ./bootstrap.sh
   ```

If you later decide you wish to add a friend to `configuration.yaml`, just run the installer again: `./bootstrap.sh`.

