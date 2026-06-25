import csv
import sqlite3

conn_data=sqlite3.connect('vibetype_data.db')

cursor=conn_data.cursor()

with open("dsa.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    rows = [
        (r["sentence"],)
        for r in reader
    ]

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS dsa(
#     id INTEGER PRIMARY KEY,
#     sentence TEXT
# )
# """)

# print(rows)

cursor.executemany("""
INSERT INTO dsa(sentence)
VALUES (?)
""", rows)

# cursor.execute("""
#     ALTER TABLE pokemon
#     DROP COLUMN fact;
# """)

# cursor.execute("""DROP TABLE dsa;""")

conn_data.commit()