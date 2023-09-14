import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

years = []
co2 = []
temp = []

try:
    cursor.execute('SELECT * FROM ClimateData')
    rows = cursor.fetchall()
    for row in rows:
        years.append(row[0])
        co2.append(row[1])
        temp.append(row[2])
except sqlite3.Error as e:
    print("SQLite error:", e)
finally:
    conn.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")

plt.savefig("co2_temp_1.png")
plt.show()
