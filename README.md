# FindMyIN100
A ultra low current 1.5v battery tag for Apple's Find My network

This work based on https://github.com/seemoo-lab/openhaystack/ and https://github.com/biemster/FindMy.

It does not (currently) deal with the evaluation of the tracking data, but rather focuses on the hardware.
The goal was to create a tracker/tag that requires as little power as possible and is as small as possible.

The size of previous tracker/tag was primarily determined by the battery.

nRF52 button style:

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image3.jpg" width="200" height="400"/>

ST17H66 keyfob style: 

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image1.jpg">

ESP32:

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image4.jpg">

Even the 'cut' ST17H66 will be dominated by the size of the battery:

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image2.jpg">


# Key generation
The python script fingen.py creates a set of all necessary data.
An example can be seen here:

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image5.jpg">

The created key file (*.keys) is compatible with: https://github.com/biemster/FindMy/blob/main/request_reports.py


# Power consumption
An important aspect of long-term trackers is power consumption.

The popular ST17H66 is given as an example:

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image6.jpg">

The power consumption of the FindMyIN100 with a 1.5v battery is even lower:

<img src="https://github.com/Cyl0nius/FindMyIN100/blob/main/Image7.jpg">


# Programming the FindMyIN100



