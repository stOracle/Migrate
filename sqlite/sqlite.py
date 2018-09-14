import sqlite3
DATABASE = 'st.db'
con = sqlite3.connect(DATABASE)
dbcur = con.cursor()
dbcur.execute("INSERT INTO HR VALUES (3, 'bobbett', 40, 'seattle', 120)")
con.commit()
dbcur.close()