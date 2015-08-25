import socket, os
import sys

hostName = '192.168.7.2'
tcpPort = 13000	#port number
imageLength = 512	#image length each time we read
passTime = 1000	#time to pass the image

if __name__ == "__main__":
	#connection set
	print "wait for connection"
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#test if connection is ready
	try:
		clientSocket.connect((hostName, tcpPort))
		print "connect success!"
	except socket.error, e:
		print "connect fail..."

	#recv the image and store it
	#create the image
	imageName = 'R.jpg'
	imagePtr = open(imageName, 'w')
	
	#looping recv the binary image
	#recv 10 times
	for i in range (1, passTime):
		while True:
			#print "recv...",
			imageBinary = clientSocket.recv(imageLength)
	
			#check if reaching end
			if not imageBinary:
				break

			#write the image
			imagePtr.write(imageBinary)
		print "done write", i

	#close the Ptr
	#imagePtr.close()
	clientSocket.close()
		
