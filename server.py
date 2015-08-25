import socket, os
import sys

tcpPort = 13000	#port number
imageLength = 512	#image length each time we read
passTime = 2	#time to pass the image

if __name__ == "__main__":
	#connection set
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serverSocket.bind(("", tcpPort))
	serverSocket.listen(1)
	print "wait for client..."
	commuSocket, address = serverSocket.accept()
	print "Connect to: ", address, "\n"

	#transfer the image and check if the name is wrong
	imageIsCorrect = True
	try:
		imageName = 'lab.jpg'
		imagePtr = open(imageName, 'r')
		print "open the file ", imageName
	except IOError, e:
		print "the image name wrong..."
		imageIsCorrect = False

	#transfer the file
	#pass 10 times
	for i in range (1, passTime):
		print "start to transfer..."
		while imageIsCorrect:
			imageReadBinary = imagePtr.read(imageLength)
			print "read..."
			if not imageReadBinary:
				break
			commuSocket.send(imageReadBinary)
		print "image send successful!"

	#close the ptr
	imagePtr.close()
	commuSocket.close()
	serverSocket.close()

