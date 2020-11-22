#pi-shutdown
===========
Shutdown/reboot(/power on) Raspberry Pi with a push button

## Pinout :
Connect pushbutton to GPIO pin 40 gpio 21 and ground 

Connect led        to GPIO pin 37 gpio 26 and ground

check image  

## Install 

```
cd /home/pi
sudo git clone https://github.com/Djang0Pepper/pi-shutdown.git
sudo pip install RPi.GPIO
sudo python pishutdown.py
```

test led blink then short press for reboot and long press to stop


## Autostart script :

If you’re using systemd then create a file called pishutdown.service in */etc/systemd/system/*

(replace #path /home/pi/pishutdown with appropriate your path):

```
sudo cp /home/pi/pi-shutdown/pishutdown.service  /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pishutdown.service
sudo systemctl restart pishutdown.service
sudo systemctl status pishutdown.service
```


## USAGE

When button is pressed for less than 3 seconds, Pi reboot. 

If pressed for more than 3 seconds it will shutdown.


## Service file
```
[Service]
ExecStart=/usr/bin/python3 /home/pi/pi-shutdown/pishutdown.py
WorkingDirectory= /home/pi/pi-shutdown/
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=pishutdown
User=root
Group=root

[Install]
WantedBy=multi-user.target
```


## Added by fred:
led toggle 5 secondes during normal running

led will keep high during reboot

led will be low if shutdown
