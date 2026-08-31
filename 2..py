import numpy as np

steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

#i.
total = np.sum(steps)
print(total)
print("\n")
#ii.

mean = np.mean(steps)
print(mean)
print("\n")

#iii.
max = np.max(steps)
print(max)
min = np.min(steps)
print(min)
print("\n")


#iv.
day_steps = np.sum(steps, axis=0)
print(day_steps)
print("\n")

#v.
user_steps = np.sum(steps, axis=1)
print(user_steps)
print("\n")


#vi.
position = np.where(steps == np.max(steps))

print(position)
print("\n")