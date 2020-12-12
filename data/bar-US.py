import matplotlib.pyplot as plt

hfont = { 'fontname': 'Rockwell'}

sports = ["Luge", "Bobsleigh", "Curling", "Ice Hockey", "Skating", "Skiing"]

medals = [5, 15, 5, 20, 42, 20]


plt.bar(sports, medals, color = "#62529B")


plt.ylabel("Total Amount of Medals", **hfont)
plt.xlabel("Sports Category of Winter Olympis", **hfont)
plt.title("Medals Won by the United States from 1990s", pad=20, **hfont)

plt.show()