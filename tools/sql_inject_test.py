import MySQLdb
# username = "18888920713"
# passwd = "pbkdf2_sha256$260000$loCE8IEIq7yNJI4PjquwTF$xSngyV2F2tIP4A1gQ2x9yL4W8AL5OOi9mc5dWb9SKQ4="
username = "' OR 1=1 #"
passwd = "pbkdf2_sha256$260000$loCE8IEIq7yNJI4PjquwTF$xSngyV2F2tIP4A1gQ2x9yL4W8AL5OOi9mc5dWb9SKQ4="
conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="mxonline")
cursor = conn.cursor()
sql = f"select * from users_userprofile where username='{username}' and password='{passwd}'"
print(sql)
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)