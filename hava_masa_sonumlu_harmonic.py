
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-poster')

#x ve y eksenindeki veriler
x = np.array([1.9, 1.8, 1.7, 1.5, 1.4, 1.1, 0.7, 0.3, 0])
y = np.array([0, 0.7, 1.35, 1.95, 2.6, 3.2, 3.85, 4.5, 5.15])

colors = np.array(["#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2","#5351f2"])

markers = ["o","o","o","o","o","o","o","o","o"]

#x ve y için hata sınırları
y_error = 0.00001
x_error = 0

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=150)

#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='black', linestyle='-', linewidth=2,)

plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 0.2, capsize=2, capthick= 1, barsabove= False)

#fonskiyonu grafiğe bastırma
plt.text(0.020, 2.55, 'y = ' +  '{:.3f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b), size=17)
#eğimi grafiğe bastırma
plt.text(0.020, 2.50, 'eğim =  {:.3f}'.format(a) + " ", size=17)


plt.title("ln(A) - t (s) Grafiği")

plt.xlabel("t (s)")

plt.ylabel("ln(A)")

plt.tight_layout()

plt.grid(True)

plt.tight_layout()

plt.legend(["ln(A)"])
print(plt.style.available)

plt.show()
