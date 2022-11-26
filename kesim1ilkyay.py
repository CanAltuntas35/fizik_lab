import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

#define data
x = np.array([20, 30, 40, 50, 60])
y = np.array([6.6, 9.9, 13.2, 16.5, 19.8])

colors = np.array(["red","green","blue","brown","orange"])

markers = ["d","o","v","D","s"]

y_error = 0.1
x_error = 0.01

#find line of best fit
a, b = np.polyfit(x, y, 1)

#add points to plot
for xp,yp, m, p in zip(x,y,markers, colors):
    plt.scatter(xp, yp, c=p, marker=m, s=100)

#add line of best fit to plot
plt.plot(x, a*x+b, color='blue', linestyle='-', linewidth=2)


plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 0.2, capsize=2, capthick= 1, barsabove= False)

#add fitted regression equation to plot
plt.text(25, 19, 'y = ' +  '{:.2f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=13)
plt.text(25, 19, 'eğim =  {:.2f}'.format(a) + "cm/g", size=13)

plt.title("Kesim 1 - 1.Yay Sabiti")

plt.xlabel("Kütle - m (g)")
plt.ylabel("Yay uzama miktarı - (cm)")

plt.tight_layout()

plt.grid(True)

plt.tight_layout()

plt.legend(["20g","30g","40g","50g","60g"])


plt.show()
