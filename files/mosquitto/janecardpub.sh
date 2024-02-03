#/bin/sh

# Publish a CARD for Jane Q. 
# this is here simply as a mechanism for automating
# documentation; recall the mosquitto clients are
# autoconfigured at $HOME/.config/mosquitto_[pb]ub

image="files/mosquitto/assets/logo-owntracks-grayscale-192x192.jpg"

jo \
	_type=card \
	name="Jane Q." \
	face=%${image} |
	mosquitto_pub -r -t owntracks/jane/nokia/info -l

