from database.database_handler import *

DB = 'source/recipes.db'

def main():
    database_handler.create_table()
    
if __name__ == "__main__":
    database_handler = DatabaseHandler(DB)
    main()