import random
import math
import matplotlib.pyplot as plt

# ----------------------------
# Base classes
# ----------------------------

class Animal:
    def __init__(self, x, y, garden_size):
        self.x = x
        self.y = y
        self.garden_size = garden_size
        self.path = [(x, y)]

    def record_position(self):
        self.path.append((self.x, self.y))

    def limit_coordinates(self):
        self.x = max(0, min(self.x, self.garden_size - 1))
        self.y = max(0, min(self.y, self.garden_size - 1))


# ----------------------------
# Mice
# ----------------------------

class Mouse(Animal):
    def __init__(self, x, y, garden_size):
        super().__init__(x, y, garden_size)
        self.home = (x, y)  # remember shelter

    def move(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.limit_coordinates()
        self.record_position()

    def teleport_home(self):
        self.x, self.y = self.home
        self.record_position()


# ----------------------------
# Cats
# ----------------------------

class Cat(Animal):
    def move(self):
        self.x += random.randint(-10, 10)
        self.y += random.randint(-10, 10)
        self.limit_coordinates()
        self.record_position()


class AverageCat(Cat):
    def encounter(self, mouse):
        if math.hypot(self.x - mouse.x, self.y - mouse.y) < 4:
            mouse.teleport_home()


class LazyCat(Cat):
    def __init__(self, x, y, garden_size):
        super().__init__(x, y, garden_size)
        self.chased_mice = 0

    def encounter(self, mouse):
        if math.hypot(self.x - mouse.x, self.y - mouse.y) < 4:
            probability = 1 / (1 + math.exp(-0.1 * self.chased_mice))
            if random.random() < probability:
                mouse.teleport_home()
                self.chased_mice += 1


class Kitten(Animal):
    def __init__(self, x, y, garden_size):
        super().__init__(x, y, garden_size)
        self.home = (x, y)

    def move(self):
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        new_x = self.x + dx
        new_y = self.y + dy
        # Stay within 100 of home
        if math.hypot(new_x - self.home[0], new_y - self.home[1]) <= 100:
            self.x, self.y = new_x, new_y
        self.limit_coordinates()
        self.record_position()

    def encounter(self, mouse):
        if math.hypot(self.x - mouse.x, self.y - mouse.y) < 4:
            dist_home = math.hypot(self.x - self.home[0], self.y - self.home[1])
            if dist_home <= 50:
                mouse.teleport_home()  # brave near home
            else:
                self.x, self.y = self.home  # kitten flees home
                self.record_position()


# ----------------------------
# Simulation
# ----------------------------

def load_positions(filename, garden_size):
    animals = []
    with open(filename) as f:
        for line in f:
            if line.strip():
                x, y = map(int, line.split())
                animals.append((x, y))
    return animals


def run_simulation(garden_size=500, iterations=500):
    # Load positions
    mice = [Mouse(x, y, garden_size) for x, y in load_positions("mice.txt", garden_size)]
    avg_cats = [AverageCat(x, y, garden_size) for x, y in load_positions("average_cats.txt", garden_size)]
    lazy_cats = [LazyCat(x, y, garden_size) for x, y in load_positions("lazy_cats.txt", garden_size)]
    kittens = [Kitten(x, y, garden_size) for x, y in load_positions("kittens.txt", garden_size)]

    all_cats = avg_cats + lazy_cats + kittens

    for _ in range(iterations):
        # Move mice
        for mouse in mice:
            mouse.move()

        # Move cats
        for cat in all_cats:
            cat.move()

        # Check encounters
        for cat in all_cats:
            for mouse in mice:
                if isinstance(cat, AverageCat):
                    cat.encounter(mouse)
                elif isinstance(cat, LazyCat):
                    cat.encounter(mouse)
                elif isinstance(cat, Kitten):
                    cat.encounter(mouse)

    # Plot paths
    for mouse in mice:
        xs, ys = zip(*mouse.path)
        plt.plot(xs, ys, color="gray", linewidth=0.8, label="Mouse" if mouse == mice[0] else "")

    for cat in avg_cats:
        xs, ys = zip(*cat.path)
        plt.plot(xs, ys, color="red", linewidth=1, label="Average Cat" if cat == avg_cats[0] else "")

    for cat in lazy_cats:
        xs, ys = zip(*cat.path)
        plt.plot(xs, ys, color="green", linewidth=1, label="Lazy Cat" if cat == lazy_cats[0] else "")

    for cat in kittens:
        xs, ys = zip(*cat.path)
        plt.plot(xs, ys, color="blue", linewidth=1, label="Kitten" if cat == kittens[0] else "")

    plt.title("Paths of Cats and Mice")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    run_simulation()
