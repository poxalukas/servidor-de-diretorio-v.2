import rpyc
import socket
from constRPYC import * #-
from rpyc.utils.server import ForkingServer

class DBList(rpyc.Service):
	value = []

	def exposed_append(self,data):
		self.value = self.value + [data]
		print("Valor Appended: ",data)
		return self.value

	def exposed_value(self):
		return self.value

	def exposed_removename(self):
		return (conn.root.exposed_removeregister("DBList",my_addr, 12345))

 	if __name__ == "__main__":
		server = ForkingServer(DIR_SERVER, DIR_PORT)

	conn=rpyc.connect(DIR_SERVER, DIR_PORT)

	my_addr = socket.gethostbyname(socket.gethostname())
	if ("conn.root.exposed_register("DBList",my_addr, 12345)" == "Registration OK"):
		print(conn.root.exposed_register("DBList",my_addr, 12345))
	else:
		print(conn.root.exposed_reregister("DBList",my_addr, 12345))
	server.start()

	