#!/usr/bin/env python3

from osc_interface import osc_device

o = osc_device()
o.sendrecv("/xinfo")
o.changeChannelName(1, "Nathan Bellew Triangle")
o.changeChannelName(2, "Jackson Hill Theremin")
o.changeChannelName(3, "Neil Peart Drums")
o.changeChannelName(4, "Geddy Lee Bass")
o.changeChannelName(5, "Geddy Lee Vocals")
o.changeChannelName(6, "Alex Lifeson Guitar")
for i in range(1, 7):
	print(o.getChannelName(i))


 
