import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
import numpy as np


def simulate_fire(forest):  # Metoda ustalająca zasady modelu płonącego lasu
    new_forest = np.zeros((x_size, y_size))
    for x in range(1, x_size - 1):
        for y in range(1, y_size - 1):
            if forest[x, y] == EMPTY and np.random.random() <= p:
                new_forest[x, y] = TREE
            if forest[x, y] == TREE:
                new_forest[x, y] = TREE
                for xx, yy in neighbourhood:
                    if forest[x + xx, y + yy] == FIRE:
                        new_forest[x, y] = FIRE
                        break
                else:
                    if np.random.random() <= f:
                        new_forest[x, y] = FIRE
    return new_forest


def animate(a):  # Metoda generująca animacje
    image.set_data(animate.forest)
    animate.forest = simulate_fire(animate.forest)


neighbourhood = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))  # sąsiedztwo punktu o wslółrzędnych x, y
EMPTY = 0
TREE = 1
FIRE = 2
colors_list = [(0.4, 0.2, 0), 'limegreen', 'orange']  # kolory pikseli lasu odpowiednio: brązowy, zielony, pomarańczowy
color_map = colors.ListedColormap(colors_list)
borders = [0, 1, 2, 3]
map_normalized = colors.BoundaryNorm(borders, color_map.N)


forest_density = 0.5  # Gęstość lasu
p = 0.01  # Prawdopodobieństwo wyrośnięcia nowego drzewa
f = 0.0001  # Prawdopodobieństwo uderzenia pioruna
x_size = 100  # Wielkość mapy
y_size = 100


my_forest = np.zeros((x_size, y_size))
# Losowanie liczby zmiennoprzecinkowej w zakresie od 0 do 1 a następnie sprawdzenie, czy wygenerowana liczba jest mniejsza niż gęstość lasu
my_forest[1:x_size - 1, 1:y_size - 1] = np.random.random(size=(x_size - 2, y_size - 2)) < forest_density
fig = plt.figure(figsize=(7, 5))   # Wielkość okna animacji
ax = fig.add_subplot(111)
ax.set_axis_off()
image = ax.imshow(my_forest, cmap=color_map, norm=map_normalized)


animate.forest = my_forest
interval = 80
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)
plt.show()
