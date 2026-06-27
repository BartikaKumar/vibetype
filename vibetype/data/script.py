# import csv
# import sqlite3

# conn_data=sqlite3.connect('vibetype_data.db')

# cursor=conn_data.cursor()

# with open("random.csv", newline="", encoding="utf-8") as f:
#     reader = csv.DictReader(f)

#     rows = [
#         (r["word"],)
#         for r in reader
#     ]

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS random(
#     id INTEGER PRIMARY KEY,
#     word TEXT
# )
# """)

# cursor.executemany("""
# INSERT INTO random(word)
# VALUES (?)
# """, rows)

# with open("anime.csv", newline="", encoding="utf-8") as f:
#     reader1 = csv.DictReader(f)

#     rows1 = [
#         (r["sentence"],r["details"])
#         for r in reader1
#     ]

# with open("dsa.csv", newline="", encoding="utf-8") as f:
#     reader2 = csv.DictReader(f)

#     rows2 = [
#         (r["sentence"],"")
#         for r in reader2
#     ]

# with open("pokemon.csv", newline="", encoding="utf-8") as f:
#     reader3 = csv.DictReader(f)

#     rows3 = [
#         (r["sentence"],"")
#         for r in reader3
#     ]

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS anime(
#     id INTEGER PRIMARY KEY,
#     sentence TEXT,
#     details TEXT
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS dsa(
#     id INTEGER PRIMARY KEY,
#     sentence TEXT,
#     details TEXT
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS pokemon(
#     id INTEGER PRIMARY KEY,
#     sentence TEXT,
#     details TEXT
# )
# """)


# # # print(rows)

# cursor.executemany("""
# INSERT INTO dsa(sentence,details)
# VALUES (?,?)
# """, rows2)

# cursor.executemany("""
# INSERT INTO pokemon(sentence,details)
# VALUES (?,?)
# """, rows3)

# cursor.executemany("""
# INSERT INTO anime(sentence,details)
# VALUES (?,?)
# """, rows1)

# # cursor.execute("""
# #     ALTER TABLE pokemon
# #     ADD COLUMN details TEXT;
# # """)

# # cursor.execute("""
# #     ALTER TABLE dsa
# #     ADD COLUMN details TEXT;
# # """)



# conn_data.commit()