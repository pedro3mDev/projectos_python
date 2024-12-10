import psycopg2

def cria_connecao():
    return psycopg2.connect( 
                database = "ucan.aulaJdbc", 
                host = "localhost", 
                user = "postgres", 
                password = "0000", 
                port = "5432" 
            )

