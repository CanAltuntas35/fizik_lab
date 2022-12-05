
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

f1a = 1/8.500

#x ve y eksenindeki veriler
y = np.array([0.38, 0.34, 0.31, 0.28])
#y = np.array([0.1176, 0.05714, 0.04082])
x = np.array([1/900, 1/1000, 1/1100, 1/1200])


colors = np.array(["royalblue","royalblue","royalblue","royalblue","royalblue","royalblue","royalblue","royalblue","royalblue"])

markers = ["o","o","o","o","o","o","o","o","o"]

#x ve y için hata sınırları
y_error = 0.001
x_error = 0

#her bir noktaya hem farklı renk hem de farklı marker
for xi,yi, m, c in zip(x,y,markers, colors):
    plt.scatter(xi, yi, c=c, marker=m, s=55)

#en iyi doğruyu bulma polyfit buluyor
a, b = np.polyfit(x, y, 1)

#en iyi doğruyu çizdirme
plt.plot(x, a*x+b, color='darkslategray', linestyle='-', linewidth=1.7,)

#plt.errorbar(x, y, yerr=y_error, xerr=x_error, fmt='.',c='black', elinewidth = 1.0, capsize=1, capthick= 1, barsabove= False)

#fonskiyonu grafiğe bastırma
plt.text(0.000825, 0.345, 'y = ' +  '{:.2f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b),c = 'black', size=13)
#eğimi grafiğe bastırma
plt.text(0.000825, 0.345, 'eğim =  {:.2f}'.format(a) + " m / s ",c = 'black', size=13)


plt.title("Grafik - 5 | Lambda λ (m) - 1/f (s)  Grafiği")

plt.xlabel("1/f (s)",c = 'black')

plt.ylabel("Lambda λ (m)",c = 'black')

plt.tight_layout()

plt.grid(True)

plt.tight_layout()

#plt.legend([""])
print(plt.style.available)

plt.show()
