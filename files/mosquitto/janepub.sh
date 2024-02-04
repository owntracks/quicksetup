#/bin/sh

# this is here simply as a mechanism for automating
# documentation; recall the mosquitto clients are
# autoconfigured at $HOME/.config/mosquitto_[pb]ub

# paris
lat=48.85833 
lon=3.29513

jo _type=location \
      SSID=mywifi \
      batt=$(perl -e 'print int(rand(99) + 1)') \
      lat=$lat \
      lon=$lon \
      tid=j1 \
      tst=$(date +%s) |
   mosquitto_pub -r -t owntracks/jane/nokia -l

