from server.server import Server

server = Server(__name__)

app = server.session

if __name__ == '__main__':
	server.run(host='0.0.0.0', 
		   	port='5000')
