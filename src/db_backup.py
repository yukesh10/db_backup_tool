import subprocess

def backup_mysql(host, port, user, password, database, output):
    command = [
        "mysqldump",
        f"--host={host}",
        f"--port={port}",
        f"--user={user}",
        f"--password={password}",
        database,
        f"--result-file={output}/{database}.sql"
    ]
    subprocess.run(command)

def backup_postgresql(host, port, user, password, database, output):
    # TODO
    print("Backing up PostgreSQL")

def backup_mongodb(host, port, user, password, database, output):
    # TODO
    print("Backing up MongoDB")

def backup_sqlite(host, port, user, password, database, output):
    # TODO
    print("Backing up SQLite")

def backup_mssql(host, port, user, password, database, output):
    # TODO
    print("Backing up MSSQL")

def backup_invalid_dbms(host, port, user, password, database, output):
    print("Invalid Database Management System")