import matplotlib.pyplot as plt


hfont = { 'fontname': 'Rockwell'}

# gold
medals = [117, 118]
gender = ["Male", "Female"]
colors = ["#CD5A01", "#E68E4A"]

plt.subplot(1, 3, 1)
plt.pie(medals, labels=gender, colors=colors)
plt.title("Gold", pad=10, **hfont)

# silver
medals = [92, 69]
gender = ["Male", "Female"]
colors = ["#CD5A01", "#E68E4A"]

plt.subplot(1, 3, 2)
plt.pie(medals, labels=gender, colors=colors)
plt.title("Silver", pad=10, **hfont)

# bronze
medals = [19, 35]
gender = ["Male", "Female"]
colors = ["#CD5A01", "#E68E4A"]

plt.subplot(1, 3, 3)
plt.pie(medals, labels=gender, colors=colors)
plt.title("Bronze", pad=10, **hfont)


plt.suptitle("Medals Won by Canada from 1990s", **hfont)

plt.show()