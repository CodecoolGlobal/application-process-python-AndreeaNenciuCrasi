import database_common


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_full_names(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_mentor_nicknames(cursor):
    cursor.execute("""
                    SELECT nick_name FROM mentors;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_applicant_name(cursor, first_name):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                    FROM applicants WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_applicant_name_by_email(cursor, string):
    cursor.execute("""
                    SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                    FROM applicants WHERE email LIKE %string;
                   """,
                   {'email': string})
    names = cursor.fetchall()
    return names
