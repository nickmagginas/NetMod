from NetMod.Support.Log import Log
from NetMod.Architecture.Link import Link,Node
from NetMod.Data.IPV4Packet import IPV4Packet
from NetMod.Simulation.Simulator import Simulation
from time import sleep

def define(log):
	ControlZ = Node('ControlZ', parentNetwork = 'HasanSuxCox')
	ControlC = Node('ControlC', parentNetwork = 'HasanSuxCox')
	Ajax = Link('Ajax', ControlZ , ControlC , log = log, load = 0, capacity = 130000, delay = 10)
	packet = IPV4Packet('ToTrasmit',source = ControlZ, destination = ControlC, IHL = 10, length = 65000)
	Ajax.sendPacket(packet)
	sleep(2)
	log('Ajax Load: ' + str(Ajax.load))
	Ajax.sendPacket(packet)
	log('Ajax Load: ' + str(Ajax.load))
	sleep(3)
	Ajax.sendPacket(packet)
	#Ajax.toggleFailure()
	Ajax.sendPacket(packet)
	Ajax.sendPacket(packet)
	Ajax.toggleFailure()
	Ajax.sendPacket(packet)

def main():
	simulation = Simulation('Sim')
	simulation.run(define)
	

if __name__ == '__main__':
	main()