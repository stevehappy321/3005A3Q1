import psycopg2

conn = psycopg2.connect(
    database="3005A3",
    host="localhost",
    user="postgres",
    password="1",
    port="5432")
conn.autocommit = True

#add new student to table
#inputs: first name, last name, email, enrollment date (yyyy-mm-dd)
def addStudent(first_name, last_name, email, enrollment_date):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Students (first_name, last_name, email, enrollment_date) "
        f"VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')"
        )

#change student email
#inputs: student id, new email address
def updateStudentEmail(student_id, new_email):
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Students "
        f"SET email = '{new_email}' "
        f"WHERE student_id = {student_id}"
        )

#delete student from table
#inputs: student id
def deleteStudent(student_id):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Students "
        f"WHERE student_id = {student_id}"
        )

#print all students as array
def getAllStudents():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students")
    entries = cursor.fetchall();
    print(entries);
