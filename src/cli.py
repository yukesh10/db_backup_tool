import argparse
from db_backup import backup_mysql, backup_postgresql, backup_mongodb, backup_sqlite, backup_mssql, backup_invalid_dbms


database_directory = {
    "mysql": backup_mysql,
    "postgresql": backup_postgresql,
    "mongodb": backup_mongodb,
    "sqlite": backup_sqlite,
    "mssql": backup_mssql
}

def backup_database(args):
    return database_directory.get(args.dbms, backup_invalid_dbms)(args.host, args.port, args.user, args.password, args.database, args.output)

def main():
    parser = argparse.ArgumentParser(description="Database Backup Utility")
    parser.add_argument("--dbms", type=str, required=True, help="Database Management System (acceptable value: MySQL, PostgreSQL, MongoDB, SQLite)")
    parser.add_argument("--host", type=str, required=False, help="Database Host")
    parser.add_argument("--port", type=int, required=False, help="Databse Port")
    parser.add_argument("--user", type=str, required=True, help="Database Username")
    parser.add_argument("--password", type=str, required=True, help="Database Password")
    parser.add_argument('--database', type=str, required=True, help='Database Name')
    parser.add_argument("--output", type=str, required=True, help="Output Directory for Database Backup")
    # parser.add_argument("--schedule", type=str, required=False, help="Backup Schedule (acceptable value: hourly, daily, weekly)")
    args = parser.parse_args()

    backup_database(args)

if __name__ == "__main__":
    main()