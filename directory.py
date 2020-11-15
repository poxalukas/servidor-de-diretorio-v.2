import rpyc
from constRPYC import * #-
from rpyc.utils.server import ThreadedServer

class Directory(rpyc.Service):
	registry={}

	def exposed_register(Self, server_name, ip_adress,port_number):
		if server_name in self.registry.keys():
			return "Nome ja resgistrado"
		else:
			self.registry[server_name] = (ip_adress, port_number)
			print(self.registry)
			return "Registration OK"

	def exposed_reregister(Self, server_name, ip_adress,port_number):
			self.registry[server_name] = (ip_adress, port_number)
			print(self.registry)
			return "Re-registration OK"

	def exposed_removeregister(Self, server_name, ip_adress,port_number):
		if server_name in self.registry.keys():
			self.registry[server_name].remove()
			return "Registro retirado"
		else:
			return "Registro nao existe"

	def exposed_lookup(Self, server_name):
		if server_name in self.registry.keys():
			print(self.registry)
			return self.registry[server_name]
		else:
			return "Lookup doesnt exist"

if __name__ == "__main__":
	server = ThreadedServer(Directory,port = DIR_PORT)

server.start()