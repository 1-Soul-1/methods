# Рассчёт сплайнов
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, UnivariateSpline, PchipInterpolator

# Простой кубический сплайн
x = np.array([0,1,2,3,4,5])
y = np.array([2,8,4,5,1,0])
t = np.linspace(0,5,100)

cs = CubicSpline(x,y)

# plt.plot(t,cs(t))
# plt.plot(x,y,'ro')
# plt.show()


# Сглаживающий сплайн
x = np.array([0,1,2,3,4,5])
y = np.array([2,8,4,5,1,0])
t = np.linspace(0,5,100)

spline = UnivariateSpline(x,y,s = 0.5) # s = 0 проходит черех точки

# plt.plot(t,spline(t))
# plt.plot(x,y,'ro')
# plt.show()


# Сплайн Эрмита
# x = np.array([0,1,2,3,4,5,5,7,3,2,6,7,8,9,3,2,4,5,8,1,1,0,1,8,5,6,3,6,4,0])
# y = np.array([2,8,4,5,1,0,1,0,0,0,1,3,0,5,4,3,2,7,4,1,5,7,1,1,2,6,4,4,6,3])
# t = np.linspace(0,30,100)

x_list = []
y_list = []

for i in range(50):
    print(i)

    x_list.append(i)
    y_list.append(random.randint(1,50))

x = np.array(x_list)
y = np.array(y_list)
t = np.linspace(0,50,1000)

phip = PchipInterpolator(x,y)

plt.plot(t,phip(t),'b-', label='Сплайн Эрмита')
plt.plot(x,y,'ro', label = 'Оригинальные данные')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Сплайн Эрмита')
plt.grid(True, alpha = 0.3)
plt.show()