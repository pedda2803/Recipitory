import sqlite3

class DatabaseHandler():
    
    def __init__(self, database_path) -> None:
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def create_table(self):
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL CHECK (category IN ('Vorspeise', 'Hauptgericht', 'Dessert')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_cooked TIMESTAMP,
            favorite BOOLEAN,
            diet_type TEXT NOT NULL CHECK (diet_type IN ('omnivor', 'vegetarisch', 'vegan')),
            times_cooked INTEGER,
            special_feature TEXT CHECK (special_feature IN ('Glutenfrei', 'Laktosefrei', 'Low Carb'))
        );
        ''')

    if __name__ == "__main__":
        create_table()  