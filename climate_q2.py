import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('climate.csv')


years = data['Year']
co2 = data['CO2']
temp = data['Temperature']


fig, (ax1, ax2) = plt.subplots(2, 1)


ax1.plot(years, co2, 'b--')
ax1.set_title("Climate Data")
ax1.set_ylabel("[CO2]")
ax1.set_xlabel("Year (decade)")


ax2.plot(years, temp, 'r*-')
ax2.set_ylabel("Temp (C)")
ax2.set_xlabel("Year (decade)")

plt.tight_layout()
plt.savefig("co2_temp_2.png")
plt.show()
