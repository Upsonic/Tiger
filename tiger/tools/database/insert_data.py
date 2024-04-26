import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def insert_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def main():
    database = r"pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # insert project
        project = ('Cool App with SQLite & Python', '2020-01-01', '2020-12-31');
        project_id = insert_project(conn, project)
        print(f"Project created with id: {project_id}")

if __name__ == '__main__':
    main()
