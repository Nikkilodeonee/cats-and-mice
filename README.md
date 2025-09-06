Project Description:

In a large square garden lives a group of cats and plenty of mice. From morning, the cats chase the mice, creating worn paths in the grass. Sometimes a cat and a mouse may meet in the same spot. How does such a situation end? It depends (possible scenarios are described below). In the evening, the paths trampled by the animals are visible on the grass.

At the start of the simulation, cats and mice are placed in the garden. The list of initial positions (i.e., the locations of cat boxes and mouse holes) for all cats and mice is loaded from files, which are described further down. Based on these, objects representing the animals are created.

During the day, both cats and mice move around the garden, each in their own way:

Mice are small, so they take small steps. At any moment, they can change their position (x, y) by at most 1 (or not at all) in each direction. The exception is when escaping, then a mouse gains superpowers and teleports to its shelter, regardless of distance.

Average Cats and Lazy Cats move in a random direction, changing their position by at most 10, both in the x and y directions.

Kittens move randomly, changing each coordinate by at most 5, but never stray more than 100 units from their home. If the new position would place a kitten more than 100 units away from home, it returns to its previous position instead.

Note: Every animal remembers all of its positions.

If a mouse is found within a distance less than 4 from a cat, a meeting occurs. The encounter between a cat and a mouse can proceed differently:

Average Cats, the most numerous, simply always tap the mouse with their paw; the mouse teleports to its home, and the cat is satisfied.

Kittens are very young and practically always afraid of mice; when they meet, they immediately teleport back to their box. The mouse continues to walk freely in the garden. However, if by chance a kitten meets a mouse near its box (within a radius of 50), they become brave and can scare the rodent enough that this time the rodent immediately teleports to its shelter.

Lazy Cats are relatively harmless. When they meet a mouse, even in their home, they often completely ignore it, and after the meeting, both go their own way as if nothing happened. Sometimes, however, a cat taps a mouse with its paw, the mouse flees (teleports) to its shelter, and the cat is happy it chased away the rodent. Whether the cat is interested in the mouse depends on chance, but it also depends on the number of mice already chased away. The more there are, the more the cat wants. The probability of interest is 
 1/(1+e^(- 0.1n)
 , where 
n
n is the number of mice chased away so far.

The whole day lasts several hundred iterations, and the entire simulation is one day. After the simulation ends, we want to see all the paths trampled in the grass by the cats and mice.

Data files: Using any program (or manually), create text files where each line contains two numbers separated by a space — the initial 
x
x and 
y
y positions of one animal. Data for each type of animal should be in a separate file (3 types of cats + mice → total 4 files). The positions should be non-negative integers, and no animal should be placed outside the garden. Several animals of each type should be created.

After the simulation finishes, we want to see the paths trodden by all the animals. Since each animal remembers all its positions, it is enough to draw a plot showing consecutive connected points. This can be done using Matplotlib and the plot command.

Example plot:

Installation
To run this simulation, Python 3 and Matplotlib are required.

Install Python 3
Download and install Python 3 from python.org if it is not installed yet.

Install Matplotlib
Use pip to install the required package:
<img width="595" height="457" alt="image" src="https://github.com/user-attachments/assets/d349c783-2702-4902-98e6-0ff80bdb45d6" />
