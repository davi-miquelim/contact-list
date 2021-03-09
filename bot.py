import sqlite3 as sql

#DATABASE connection
conexion  = sql.connect('contatos.db')

#Create cursor
cursor = conexion.cursor()

option = int(input('''O que deseja fazer?
1 - Inserir novo contato
2 - Ver todos os contatos 
3 - procurar contato
 '''))
if option == 1:
    nome = input('Insira o nome:')
    negocio = input('Insira o negocio:')
    numero = input('Insira o numero: ')
    cursor.execute(f"""
        INSERT INTO contatos ('nome','negocio','numero') VALUES ('{nome}','{negocio}','{numero}')
    """)
    if nome and negocio and numero:
        conexion.commit()
        conexion.close()
    else:
        print('Por favor preencha todos os campos corretamente')
elif option == 2:
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    for contato in contatos:
        print(contato)

elif option == 3:
    nome = input('Insira o contato pelo qual esta buscando ')
    cursor.execute(f"SELECT * FROM contatos WHERE nome = '{nome}'")
    contatos = cursor.fetchall()
    for contato in contatos:
        print(contato) 
else:
    print('Por favor insira um valor valido. Feche o script e tente novamente')