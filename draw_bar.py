import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

x_data = ["v-{}".format(i) for i in range(1, 4)]
y_data = [85.76, 92.08, 99.17]


plt.rcParams["font.sans-serif"] = ['Times New Roman']
plt.rcParams["axes.unicode_minus"] = False

# maybe a better looking math fonts 😊
plt.rcParams['mathtext.fontset'] = 'stix'

# Hey, Jessie~ You can adjust the figure size here. 👇
# (6.4，4，8) here makes the figure's width 6.4 inches, and its height 4.8 inches. (with an aspect ratio of 4/3)
# Change it to whatever value fits your paper.
plt.rcParams["figure.figsize"] = (6.4, 4.8)


for i in range(len(x_data)):
    plt.bar(x_data[i],
            y_data[i],
            0.5,
            color='white',  # 😁 To be honest, I don't think `pink` is a good choice, but anyway follow your heart~
            edgecolor='black')

for i in range(len(y_data)):
    plt.text(i,
             y_data[i]-10,  # put value mark down a bit from the bars
             "%s" % y_data[i]+"%",
             verticalalignment='center',
             horizontalalignment='center',
             fontsize=15,
             fontweight='bold')


plt.xticks(fontsize=15, fontweight='bold')
plt.yticks(fontsize=15, fontweight='bold')

plt.gca().yaxis.set_major_formatter(PercentFormatter())


plt.title("Record Linkage Comparison Patterns & $O(n^{1.35})$", fontsize=15, fontweight='bold')
plt.xlabel("Version Number", fontsize=15, fontweight='bold')
plt.ylabel("Accuracy", fontsize=15, fontweight='bold')


# This line helps remove the figure margin 👇
plt.tight_layout(pad=0.05)

plt.show()

# Good Luck~ ❤️


