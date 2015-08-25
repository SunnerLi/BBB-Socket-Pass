import socket, os
import sys

tcpPort = 13000	#port number
imageLength = 512	#image length each time we read
passTime = 100	#time to pass the image

if __name__ == "__main__":
	#connection set
	print "wait for connection"
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#test if connection is ready
	try:
		clientSocket.connect(("192.168.1.90", tcpPort))
		print "connect success!"
	except socket.error, e:
		print "connect fail..."

	#transfer the image and check if the name is wrong
	imageIsCorrect = True
	try:
		imageName = 'ball.jpg'
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
			clientSocket.send(imageReadBinary)
		print "image send successful!"

	#close the Ptr
	#imagePtr.close()
	clientSocket.close()
		
