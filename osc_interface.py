#!/usr/bin/env python3

from socket import socket, AF_INET, SOCK_DGRAM

class osc_device:
	def __init__(self, ip_addr = "192.168.1.1", port = 10024):
		self.ip_addr = ip_addr
		self.port = port
		self.soc = socket(AF_INET, SOCK_DGRAM)

	def sendCommand(self, command):
		self.soc.sendto(bytes(command, 'ascii'), (self.ip_addr, self.port))

	def recvCommand(self):
		return self.soc.recvfrom(8192)

	def sendrecv(self, command):
		self.soc.sendto(bytes(command, 'ascii'), (self.ip_addr, self.port))
		return self.soc.recvfrom(8192)


	def changeChannelName(self, channel, name):
		chan = str(channel)
		if(len(chan) == 1):
			chan += "0"
			chan = chan[::-1]

		command = "/ch/" + chan + "/config/name\0\0,s\0\0"
		sn = len(name)
		name += (4 - sn%4) * "\0"

		self.sendCommand(command + name)	

	def getChannelName(self, channel):
		chan = str(channel)
		if(len(chan) == 1):
			chan += "0"
			chan = chan[::-1]

		command = "/ch/" + chan + "/config/name\0\0,"
		return self.sendrecv(command)
