
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

#x ve y eksenindeki veriler
x = np.array([40, 50, 60, 70, 80])
y = np.array([0.582169, 0.697225, 0.850084, 0.925444, 1.062961])

colors = np.array(["red","green","blue","brown","orange"])

markers = ["d","o","v","D","s"]

#x ve y için hata sınırları
y_error = 0
x_error = 0.01

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=100)

#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='blue', linestyle='-', linewidth=2,)

plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 0.2, capsize=2, capthick= 1, barsabove= False)

#fonskiyonu grafiğe bastırma
plt.text(45, 1.01, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=13)
#eğimi grafiğe bastırma
plt.text(45, 1.01, 'eğim =  {:.3f}'.format(a) + " s²/g", size=13)


plt.title("Kesim 2 -  T² / Kütle Grafiği")

plt.xlabel("Kütle - m (g)")

plt.ylabel("Periyot T² - (s²)")

plt.tight_layout()

plt.grid(True)

plt.tight_layout()

plt.legend(["40g","50g","60g","70g","80g"])
print(plt.style.available)

plt.show()
