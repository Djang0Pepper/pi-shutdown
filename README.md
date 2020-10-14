pi-shutdown
===========

Shutdown/reboot(/power on) Raspberry Pi with pushbutton

## Usage:
Connect pushbutton to GPIO pin 40 gpio 21 and ground then
Connect led        to GPIO pin 37 gpio 26 and ground then run:
```
sudo python pishutdown.py
```

When button is pressed for less than 3 seconds, Pi reboots. If pressed for more than 3 seconds it shuts down.
While shut down, if button is connected to GPIO pin 5, then pressing the button powers on Pi.

## Autostart the script:
If you’re using systemd then create a file called pishutdown.service in /etc/systemd/system/
(replace #path\_to\_pishutdown with appropriate path):

[Service]
ExecStart=/usr/bin/python3 ~/Python/pi-shutdown/pishutdown.py
WorkingDirectory= ~/Python/pi-shutdown/
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=pishutdown
User=root
Group=root

[Install]
WantedBy=multi-user.target

## Enable service:
sudo systemctl enable pishutdown.service
Run service (will be automatically started on next reboot):
sudo systemctl start pishutdown.service
