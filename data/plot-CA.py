import matplotlib.pyplot as plt

hfont = { 'fontname': 'Rockwell'}

years = ["1992", "1994", "1998", "2002", "2006", "2010", "2014"]

gold = [5, 3, 14, 53, 29, 68, 63]
silver = [29, 32, 28, 7, 28, 15, 22]
bronze = [3, 5, 7, 15, 11, 8, 5]


plt.plot(years, bronze)
plt.plot(years, silver)
plt.plot(years, gold)

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(years, bronze, label="bronze", color = "#9E6A5D", marker="o", ms=7)
ax.plot(years, silver, label="silver", color = "#9B9B9B", marker="o", ms=7)
ax.plot(years, gold, label="gold", color = "#DEA300", marker="o", ms=7)

plt.ylabel("Amount of Three Medals", **hfont)
plt.xlabel("Year of Winter Olympis", **hfont)
plt.title("Medals Won by Canada from 1990s", pad=20, **hfont)

ax.legend()
plt.show()