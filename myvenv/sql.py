from mysql.connector import connect

connection = sqlite3.connect("course.db")
cursor = connection.cursor()

insert_statement = "INSERT INTO data_learner(first, last, dob, occupation)
    VALUES ("Precious", "Akpan", "1914", "Developer");"
cursor.execute()

learner = cursor.fetchone()
