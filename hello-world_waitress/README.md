# hello-world_waitress

This sample application launch a hello-world web application using flask/waitress.
It listen to on port 5000/tcp.

It is a quick reference for how to integrate an application with systemd, using the python *sdnotify* module.
The main goal is to use systemd's watchdog capabilities to make a python application more available and resilient.

Together with the systemd unit file *myapp.service*, it enables to run *myapp.py* python script (here a web app) as a linux service.
