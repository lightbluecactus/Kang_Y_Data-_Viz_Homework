import matplotlib.pyplot as plt

hfont = { 'fontname': 'Rockwell'}

sports = ["Luge", "Bobsleigh", "Curling", "Ice Hockey", "Skating", "Skiing"]

medals = [9, 33, 5, 148, 98, 76]


plt.bar(sports, medals, color = "#62529B")


plt.ylabel("Total Amount of Medals", **hfont)
plt.xlabel("Sports Category of Winter Olympis", **hfont)
plt.title("Medals Won by the United States from 1990s", pad=20, **hfont)

plt.show()