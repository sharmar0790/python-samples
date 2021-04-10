import matplotlib.pyplot as plt


plt.plot([1,2,3,4],label="a")
plt.plot([2,4,6,8],label="b")
plt.plot([1,2,3,4],label="c")
plt.legend()
plt.grid(True)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Learning Python - Matplotlib")
plt.show()