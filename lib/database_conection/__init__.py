import mysql.connector


def coletaEmails():
    conexao = mysql.connector.connect(database='taqadress',
                                  host='localhost',
                                  password='',
                                  user='root')

    if conexao.is_connected():
        cursor = conexao.cursor()
    else:
        print('ERRO CRÍTICO! Falha na conexão com o banco de dados.')
    
    cursor.execute('SELECT email FROM tb_emails;')
    r = cursor.fetchone()
    emails = list()
    while r is not None:
        emails += r
        r = cursor.fetchone()
    cursor.close()
    conexao.close()
    return emails
