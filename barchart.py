import matplotlib.pyplot as plt
# plt.bar([1,3,5],[20,44,88])
d={'a':25,'b':35,'c':54}
for i, key in enumerate(d):
    plt.bar(i+2,d[key])
    plt.xticks([1,2,3],d.keys())
plt.show()