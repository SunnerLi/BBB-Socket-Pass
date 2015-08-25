import socket, os
import sys

tcpPort = 13000	#port number
imageLength = 512	#image length each time we read
passTime = 100	#time to pass the image

if __name__ == "__main__":
	#connection set
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serverSocket.bind(("", tcpPort))
	serverSocket.listen(1)
	print "wait for client..."
	commuSocket, address = serverSocket.accept()
	print "Connect to: ", address, "\n"

	#recv the image and store it
	#create the image
	imageName = 'R.jpg'
	imagePtr = open(imageName, 'w')
	
	#looping recv the binary image
	#recv 10 times
	for i in range (1, passTime):
		while True:
			#print "recv...",
			imageBinary = commuSocket.recv(imageLength)
	
			#check if reaching end
			if not imageBinary:
				break

			#write the image
			imagePtr.write(imageBinary)
		print "done write", i

	#close the ptr
	imagePtr.close()
	commuSocket.close()
	serverSocket.close()

