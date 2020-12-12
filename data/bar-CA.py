import matplotlib.pyplot as plt

hfont = { 'fontname': 'Rockwell'}

sports = ["Biathlon", "Bobsleigh", "Curling", "Ice Hockey", "Skating", "Skiing"]

medals = [3, 18, 50, 218, 129, 32]


plt.bar(sports, medals, color = "#CD5A01")


plt.ylabel("Total Amount of Medals", **hfont)
plt.xlabel("Sports Category of Winter Olympis", **hfont)
plt.title("Medals Won by Canada from 1990s", pad=20, **hfont)

plt.show()