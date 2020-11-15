import rpyc
from constRPYC import * #-

class Client:
	conn_directory = rpyc.connect(DIR_SERVER, DIR_PORT)

	(addr,port) = conn_directory.root.exposed.lookup("DBList")

	print(addr, port)

	conn=rpyc.connect(addr,port)

	conn.root.exposed_append(2)
	conn.root.exposed_append(4)
	print(conn.root.exposed_value())
	print(conn.root.exposed_removename())