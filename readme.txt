o projeto possui 4 arquivos, sendo eles:
====================================================================================================================================
directory.py
Servidor de diretorio:
	implementa a classe Directory que usa a tabela registry;

	implementa um servidor rpc e possui 4 metodos, usando o metodo de servidor thread
	
	def exposed_register: recebe 3 parametros, nome do servidor, numero de ip e numero de porta;
	verifica se o nome nao existe,caso nao as 3 sao armazenados na tabela registry, usando o nome como chave, e faz uma tupla com 	o numero de ip e porta, caso contrario retorna que ja possui o registro;
	na linha print(self.registry) imprimi oque foi salvo e o retorno, informa que a registraçao esta ok;

	def exposed_reregister: complemento do exposed_register, refaz o registro do servidor;

	def exposed_lookup:metodo de decoberta de servidor, onde e passado somente o nome do servidor,e  caso o servidor ja tenha sido 	registrado, o servidor de diretorio retorna a entrada do registro associado ao nome, retornando a tupla de ip e porta, caso 		contrario informa que o servidor nao esta registrado;

	def exposed_removeregister: se o nome estiver registrado, ele remove da lista, caso nao ele informa que nao esta registrado


====================================================================================================================================
server.py
Servidor da aplicaçao:

	Class DBList: e a base de dados

	possui dois metodos, e usa o metodo forking server;

	append: faz um append de um valor da lista do DBList;
	
	value: obtem o valor da lista;

	na var conn ele conecta ao diretorio do servidor e em
	my_addr: obtem o endereço de ip da maquina que esta rodando

	e registra ele mesmo no diretorio do servidor
====================================================================================================================================
constRPYC.py

	arquivo de controle do diretorio do servidor, e porta
	====================================================================================================================================
cliente.py
	conn =  ele conecta ao diretorio do servidor
	em (addr,port) = conn_directory.root.exposed.lookup("DBList"): ele faz um loockup ja recebido o end de ip e porta,

	 em print(addr, port):ele  imprimi  o endereço de ip e porta
	
	conn=rpyc.connect(addr,port): conecta o servidor com os ip e porta que recebeu
	
	e depois faz a chamada do apend e a quantidade de elementos do apend
	
	e imprimi o resultado em :	
		conn.root.exposed_append(2)
		conn.root.exposed_append(4)
		print(conn.root.exposed_value())

	em print(conn.root.exposed_removename()): retorna a informaçao da funçao que retira o servidor do registro;

	





























