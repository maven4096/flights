import csv, sqlite3
def initialize_table(table_name: str):
    conn = sqlite3.connect('./data/flights.db')
    cursor = conn.cursor()
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (airport_name TEXT, city TEXT, IATA CHAR(3), ICAO CHAR(4));")
def pull_table(table_name :str):
    table = []
    with sqlite3.connect("./data/flights.db") as con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        for row in cur.fetchall():
            table.append(row)
    return table
def populate_table_from_csv(table_name :str, csv_name :str):
    initialize_table(table_name)
    with open(f'./data/{csv_name}.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        reader = list(reader)
    with sqlite3.connect('./data/flights.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO airports VALUES (?, ?, ?, ?)", reader)
        con.commit()
if __name__ == '__main__':
    populate_table_from_csv("airports", "airports")