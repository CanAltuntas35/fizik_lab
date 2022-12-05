
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

f1a = 1/8.500

#x ve y eksenindeki veriler
y = np.array([(17.9)*(17.9), (24.9)*(24.9), (33.4)*(33.4)])
#y = np.array([0.1176, 0.05714, 0.04082])
x = np.array([0.5, 1.0, 1.5])


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
plt.text(0.47, 700, 'y = ' +  '{:.2f}'.format(a) + 'x' + ' + {:.2f}\n'.format(b),c = 'black', size=13)
#eğimi grafiğe bastırma
plt.text(0.47, 700, 'eğim =  {:.2f}'.format(a) + " m / kg ",c = 'black', size=13)


plt.title("Grafik - 4 | V² (m²/s²) - F (N)  Grafiği")

plt.xlabel("F (N)",c = 'black')

plt.ylabel("V² (m²/s²)",c = 'black')

plt.tight_layout()

plt.grid(True)

plt.tight_layout()

#plt.legend([""])
print(plt.style.available)

plt.show()
