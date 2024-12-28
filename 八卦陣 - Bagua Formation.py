import matplotlib.pyplot as plt
import numpy as np

def draw_bagua():
    # Circle for outer boundary
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    plt.plot(x, y, color='black', linewidth=2)

    # Inner trigrams
    for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        x_start, y_start = 0.8 * np.cos(angle), 0.8 * np.sin(angle)
        x_end, y_end = np.cos(angle), np.sin(angle)
        plt.plot([x_start, x_end], [y_start, y_end], color='blue', linewidth=1.5)

    # Central Yin-Yang symbol
    yin_theta = np.linspace(0, np.pi, 100)
    yang_theta = np.linspace(np.pi, 2 * np.pi, 100)

    # Yin
    plt.fill_between(np.cos(yin_theta), np.sin(yin_theta), color='black')
    plt.fill_between(np.cos(yang_theta), np.sin(yang_theta), color='white')

    # Add dots to Yin and Yang
    plt.scatter(0, 0.25, color='white', s=50)
    plt.scatter(0, -0.25, color='black', s=50)

    # Adjust display
    plt.axis('equal')
    plt.axis('off')
    plt.title("八卦陣 - Bagua Formation", fontsize=14)
    plt.show()

if __name__ == "__main__":
    draw_bagua()
