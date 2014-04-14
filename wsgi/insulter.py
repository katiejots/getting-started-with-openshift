import psycopg2
import os

#get a connection to use in the DB calls. Only need a cursor because these connections are read only
def get_cursor():
    #open a connection
    conn = psycopg2.connect(database=os.environ['OPENSHIFT_APP_NAME'], user=os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'], 
                password=os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'], host=os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'], 
                port=os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'] )
    #get a cursor from the connection
    cursor = conn.cursor()  
    return cursor   

#Clean up when done with the cursor and connection  
def close_cursor(cursor):
    conn = cursor.connection
    cursor.close()
    conn.close()

#Expects to be passed a psycopg2 cursor
#Using the solution found on this Stack Overflow page 
#http://stackoverflow.com/questions/5297396/quick-random-row-selection-in-postgres
def get_word(cursor, table):
    sql = "select string from " + table + " offset random()* (select count(*) from " +  table + ") limit 1;"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result[0]

def insult():
    return "Thou " + generate_insult() + "!"

def named_insult(name):
    return name + ", thou " + generate_insult() + "!"

def generate_insult():
    local_cursor = get_cursor()
    final_insult = get_word(local_cursor, "short_adjective") + " " + get_word(local_cursor, "long_adjective") + " " + get_word(local_cursor, "noun")
    close_cursor(local_cursor)
    return final_insult
