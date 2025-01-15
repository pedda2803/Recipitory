from database.database_handler import *
import tkinter

DB = 'source/recipes.db'

def main():
    database_handler.create_table()
    tkinter._test()
    
if __name__ == "__main__":
    database_handler = DatabaseHandler(DB)
    main()