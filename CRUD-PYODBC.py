import pyodbc

dados_conexao = ("Driver={SQLite3 ODBC Driver}; Server=localhost; Database=manipulacao.db;")

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()


#garantir que a conexão foi finalizada

while True:

    #TELA INICIAL

    print('\n====== CRUD (Registro = IDADE / NOME) ======\n')
    reposta= int(input('1 - ADICIONAR REGISTRO NO BANCO DE DADOS \n2 - EXIBIR BANCO DE DADOS\n3 - ATUALIZAR REGISTRO NO BANCO DE DADOS\n4 - DELETAR REGISTRO NO BANCO DE DADOS\n5 - SAIR DO SISTEMA\n.... '))
    
 
    
    #LOGICA DO CRUD
    
    # CREAT
    
    if reposta == 5:
        conexao.close()
        print('Saiu do sistema.')
        break
    
    
    if reposta == 1:
        print('\nDigite abaixo as informações necessárias para criar um registro:\n')
        nome = input('\nDigite o nome a ser inserido: ')
        idade = int(input('\nDigite a idade a ser inserida: '))
        
        
        cursor.execute(f"""
        INSERT INTO registro (Nome, Idade)
        VALUES ('{nome}', {idade})
        """)

        cursor.commit()
        
        print('\n Adicionado com sucesso!\n')
        
    elif reposta == 2:
        cursor.execute("""
        SELECT * FROM registro
        """)

        valores = cursor.fetchall()
        
        print(f'\n{valores}\n')
        
    elif reposta == 3:
        print('\nDigite abaixo as informações necessárias para ATUALIZAR um registro:\n')
        nome_up = input('\nDigite o nome do registro que sera alterado: ')
        nome_up_act = input('\nDigite o novo nome desse registro: ')
        idade_up_act = int(input('\nDigite a nova idade desse registro: '))
        
        cursor.execute(f"""
        UPDATE registro SET Nome='{nome_up_act}', Idade={idade_up_act} WHERE Nome = '{nome_up}'
        """)

        cursor.commit()
        
        print('\n Atualizado com sucesso!\n')
        
    elif reposta == 4:
        print('\nDigite abaixo as informações necessárias para DELETAR um registro:\n')
        nome_del = input('\nDigite o nome do registro que sera DELETADO: ')
    
        cursor.execute(f"""
        DELETE FROM registro WHERE Nome = '{nome_del}'
        """)

        cursor.commit()
        
        print('\n Deletado com sucesso!\n')



    
    
    
    



