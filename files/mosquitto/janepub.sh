#/bin/sh

# this is here simply as a mechanism for automating
# documentation; recall the mosquitto clients are
# autoconfigured at $HOME/.config/mosquitto_[pb]ub

tics=$(date +%s)

# paris
lat=48.85833 
lon=3.29513

jo _type=location \
      SSID=mywifi \
      alt=154 \
      batt=53 \
      conn=w \
      lat=48.856826 \
      lon=2.292713 \
      tid=j1 \
      tst=${tics} \
      vel=0 |
   mosquitto_pub -r -t owntracks/jane/nokia -l

