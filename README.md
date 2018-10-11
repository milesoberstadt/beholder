# beholder

### A network watchdog that makes sure your services are up!

In this age of cheap IoT devices and incredibly cheap WiFi enabled hardware, there's been a 
"move fast and break stuff" motto that has been great for makers and hardware hackers, but kind of terrible
for uptime. I decided to write this after my bike got stolen from my garage one night after the Pi Zero 
that was supposed to automatically close the door behind me crashed. I couldn't find a decent tool that let 
me easily notify me if stuff crashed, so I wrote my own.

### Docker Setup (recommended)

0. Install Docker on your machine
1. Clone this repositiory on a server on your network. Could be a Pi, could be something else

`git clone https://github.com/milesoberstadt/beholder.git`

2. Setup the Docker container 

```
cd beholder
docker build -t beholder .
```

3. Test run the container

`docker run -it --rm --name beholder beholder`


### Setup without Docker (good luck with that)

TODO: Write this
