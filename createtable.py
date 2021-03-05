import psycopg2

DATABASE_URL = "postgres://xgcdthkexgrmxk:94093c3e42997d172ec998ffd9be108f9c9f3d569c854711045b1793dba5c3fd@ec2-54-87-34-201.compute-1.amazonaws.com:5432/d2mptevqotb4f1"
con = None

sql = "CREATE TABLE access (id INT PRIMARY_KEY, plate_no VARCHAR(255));"

try:
    # create a new database connection by calling the connect() function
    con = psycopg2.connect(DATABASE_URL, sslmode="require")

    #  create a new cursor
    cur = con.cursor()
    
    # execute an SQL statement to create log table
    cur.execute(sql)
    print("Table created successfully")
    
    # close the communication with the HerokuPostgres
    cur.close()

except Exception as error:
    print("Error")
    print('Cause: {}'.format(error))

finally:
    # close the communication with the database server by calling the close()
    if con is not None:
        con.commit()
        con.close()
        print('Database connection closed.')
