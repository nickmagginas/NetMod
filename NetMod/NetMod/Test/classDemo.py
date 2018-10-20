'''
	+++++++++++++++++++++++++++++++++++++++++
	|			Hello Folks,                |
	|	Welcome to your Library Code Demo	|
	|			Your Host is:               |			
	|			  Vaginator                 |
	|                                       |
	|	----   Nikolaos Manginas   ----		|
	|	----          UCL          ----		|
	|	----      16 Oct. 2018     ----		|
	|	---- Neural Packet Routing ----		|
	+++++++++++++++++++++++++++++++++++++++++
'''
''' First Order of Business is to install the Library'''
''' In Neural-Package-Routing/NetMod pip install . '''
''' Friends, Use frontslash in Linux and double backslash in Windows. 
	I am currently in the realms of a Windows 
	operating system and thus I use \\ '''

from NetMod.Architecture import Network, Node, Link
from NetMod.Support.Log import Log

''' U have now imported the classes in what is probably the 
	Best choise in your Life. Yee-Haw   '''

def main():

	# Use can initialize a Node

	ControlZ = Node('ControlZ')

	# and print this node
	log = Log('Log')
	log.begin()
	log(ControlZ)

	# nodes can also hava parent networks

	ControlZ.parentNetwork = 'HasanSuxCox'
	print(ControlZ)

	# or you can pass it in initialization

	ControlZ = Node('ControlZ', parentNetwork = 'HasanSuxCox')
	print(ControlZ)
	
	ControlC = Node('ControlC', parentNetwork = 'HasanSuxCox')

	# You can define a link between to Nodes. 
	# -----! Attention Whores !----- #
	# Please 5 arguments or it will complain#
	# Name the two Nodes it links load and capacity #

	LinkInPark = Link('ControlZ/ControlC', ControlZ, ControlC, load = 0, capacity = 10)

	# You can also print Links

	print(LinkInPark)

	# You can also say the link is under use to print more

	LinkInPark.underUse = True

	# or

	LinkInPark = Link('ControlZ/ControlC', ControlZ, ControlC, underUse = True ,load = 0, capacity = 10)

	print(LinkInPark)

	# if there is a failure you can report it by

	LinkInPark.failed = True

	# or if you know it to hava failed from initilization then pass it there 

	LinkInPark = Link('ControlZ/ControlC', ControlZ, ControlC, failed = True, underUse = True ,load = 0, capacity = 10)

	# Shows when you print the object

	print(LinkInPark)

	# Now you can use these to make networks or define new ones
	# Lets call this for a change HasanSuxCos
	# Casue he Does
	# xD

	HasanSuxCos = Network('HasanSuxCox')

	# You can add Nodes by 

	HasanSuxCos.nodes = [ControlZ, ControlC]
	
	# Even for one node put it in list
	# Call construct links for links to automatically be made

	HasanSuxCos.constructNetwork()

 	# Every time You add a node call construct network to link it to all other nodes

	print(HasanSuxCos)

	# You can also pass many things in initialization

	ControlX = Node('ControlX', parentNetwork = 'HasanSuxCos')

	# U guessed it People HasanSuxCox

	HasanSuxCox = Network('HasanSuxCox',nodes = [ControlX,ControlZ,ControlC], empty = False)

	# If u initialize with nodes it makes links by itself

	print(HasanSuxCox)

	# U can also clearly pass empty to indicate empty networks

	# This has been all for today
	# As always Peace !!!

	#  ---------- Balllsss Dude ------------- #

if __name__ == '__main__': 
	main()
