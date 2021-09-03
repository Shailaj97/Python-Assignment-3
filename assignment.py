import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="new",
        user="postgres",
        password="apple_ball",
        port=5432
    )

    cursor = connection.cursor()

    # create_query = '''
    #      CREATE TABLE IF NOT EXISTS Doctor (
    #         id INT PRIMARY KEY,
    #         name VARCHAR(100) NOT NULL,
    #         specialization INT,
    #         phone_number CHAR(12)
    #     )

    #     CREATE TABLE IF NOT EXISTS Patient (
    #         id INT PRIMARY KEY,
    #         name VARCHAR(100) NOT NULL,
    #         date_of_birth DATE,
    #         gender VARCHAR(10)
    #     )

    #     CREATE TABLE IF NOT EXISTS Appointment (
    #         id INT PRIMARY KEY,
    #         doctor_id INT,
    #         patient_id INT,
    #         fee INT,
    #         daignosis VARCHAR(50)
    #     )

    #     CREATE TABLE IF NOT EXISTS Doctor_Specialization (
    #         id INT PRIMARY KEY,
    #         specialization_type VARCHAR(20)
    #     )

    #     '''

    # cursor.execute(create_query)
    # connection.commit()

    # insert_query = '''
    #     INSERT INTO Doctor Values(1 ,'Lionel Smart', 1 ,2811232323 )
    #     INSERT INTO Doctor Values(2 ,'Michelle Sanders', 2 ,1899912310 )
    #     INSERT INTO Doctor Values(3 ,'Pretti Patel', 3 ,7980123982 )
    #     INSERT INTO Doctor Values(4 ,'Sadiq Khan', 1 ,7983129813 )
    #     INSERT INTO Doctor Values(5 ,'Chaz Smith', 2 ,2039820398 )

    #  '''
    # cursor.execute(insert_query)
    # connection.commit()

    # insert_query = '''
    #     INSERT INTO Patiend VALUES(%(id)s,%(name)s,%(date_of_birth)s,%(gender)s)

    # '''
    # data = [
    #     {
    #         'id' : 1,
    #         'name' :'Jane Henderson' ,
    #         'date_of_birth' : 1989-9-19,
    #         'gender' : 'Female'
    #     },
    #     {
    #         'id' : 2,
    #         'name' : 'Alice Sprigg' ,
    #         'date_of_birth' : 1991-11-12,
    #         'gender' :'Female'
    #     },
    #     {
    #         'id' : 3,
    #         'name' :'Dave Carr' ,
    #         'date_of_birth' : 1995-3-28,
    #         'gender' :'Male'
    #     },
    #     {
    #         'id' : 4,
    #         'name' :'Morris Beckman' ,
    #         'date_of_birth' : 2001-7-7,
    #         'gender' : 'Male'
    #     },
    # ]

    # cursor.execute(insert_query,data)
    # connection.commit()

    # insert_query = '''
    #     INSERT INTO Doctor_Specialization VALUES(%(id)s,%(specialization_type)s)

    # '''
    # data = [
    #     {
    #         'id' : 1,
    #         'name' :'Anaesthesiologist'

    #     },
    #     {
    #         'id' : 2,
    #         'name' :'Surgeon'

    #     },
    #     {
    #         'id' : 3,
    #         'name' :'Psychiatrist'

    #     },
    # cursor.executemany(insert_query,data)
    # print(cursor.rowcount)
    # connection.commit()
    #  insert_query = '''
    #     INSERT INTO Appointment VALUES(%(id)s,%(doctor_id)s,%(patient_id)s,%(fee)s,%(diagnosis)s)

    # '''
    # data = [
    #     {
    #         'id' : 1,
    #         'doctor_id' : 1 ,
    #         'patient_id' :2 ,
    #         'fee' : 1000,
    #         'diagnosis': ' '

    #     },
    #     {
    #         'id' : 2,
    #         'doctor_id' : 1 ,
    #         'patient_id' : 4 ,
    #         'fee' : 1000,
    #         'diagnosis':  'Headache'

    #     },
    #     {
    #         'id' : 3,
    #         'doctor_id' : 4,
    #         'patient_id' : 3,
    #         'fee' : 2000,
    #         'diagnosis':' '

    #     },
    #     {
    #         'id' : 4,
    #         'doctor_id' : 2,
    #         'patient_id' : 1,
    #         'fee' : 1500,
    #         'diagnosis': 'Back_Pain'

    #     },
    # cursor.executemany(insert_query,data)
    # print(cursor.rowcount)
    # connection.commit()

except Exception as e:
    print("Error occured", e)

finally:
    cursor.close()
    connection.close()

    # select query ='''
    #     SELECT * FROM Patients
    #     WHERE date_of_birth > 1990
    # '''
    # cursor.execute(select_query)
    # print(cursor.fetchmany())
    # print(cursor.fetchone())

    # select query ='''
    #     SELECT *
    #     WHERE specialization =2
    # '''
    # cursor.execute(select_query)
    # paint(cursor.fetchmany())
    # print(cursor.fetchone())

