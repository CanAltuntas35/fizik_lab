import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

#x ve y eksenindeki veriler
x = np.array([40, 60, 80, 100, 120])
y = np.array([1.1, 1.7, 2.3, 2.9, 3.6])

colors = np.array(["red","green","blue","brown","orange"])

markers = ["d","o","v","D","s"]

#x ve y için hata sınırları
y_error = 0.1
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
plt.text(50, 3.35, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=13)
#eğimi grafiğe bastırma
plt.text(50, 3.3, 'eğim =  {:.3f}'.format(a) + "cm/g", size=13)


plt.title("Kesim 1 - 2.Yay Sabiti")

plt.xlabel("Kütle - m (g)")

plt.ylabel("Yay uzama miktarı - (cm)")

plt.tight_layout()

plt.grid(True)

plt.tight_layout()

plt.legend(["40g","60g","80g","100g","120g"])
print(plt.style.available)

plt.show()
