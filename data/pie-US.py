import matplotlib.pyplot as plt


hfont = { 'fontname': 'Rockwell'}

# gold
medals = [31, 47]
gender = ["Male", "Female"]
colors = ["#62529B", "#9D90C9"]

plt.subplot(1, 3, 1)
plt.pie(medals, labels=gender, colors=colors)
plt.title("Gold", pad=10, **hfont)

# silver
medals = [94, 90]
gender = ["Male", "Female"]
colors = ["#62529B", "#9D90C9"]

plt.subplot(1, 3, 2)
plt.pie(medals, labels=gender, colors=colors)
plt.title("Silver", pad=10, **hfont)

# bronze
medals = [54, 53]
gender = ["Male", "Female"]
colors = ["#62529B", "#9D90C9"]

plt.subplot(1, 3, 3)
plt.pie(medals, labels=gender, colors=colors)
plt.title("Bronze", pad=10, **hfont)


plt.suptitle("Medals Won by the United States from 1990s", **hfont)

plt.show()