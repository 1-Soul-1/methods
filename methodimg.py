import numpy as np
import matplotlib.pyplot as plt
from skimage import data, transform, io
from skimage.util import img_as_float

img = io.imread('./Tigers.png')

# Уменьшаем картинку для дальнейшего увеличения и видимости разницы
img_small = transform.resize(img,(50,50))

img_nearest = transform.resize(img_small,(200,200), order = 0) # ближайший сосед
img_linear = transform.resize(img_small,(200,200), order = 1) # линейная
img_cubic = transform.resize(img_small,(200,200), order = 2) # кубический сплайн
img_quintic = transform.resize(img_small,(200,200), order = 3) # сплайн 5-го порядка

# Визуализация
fig,axes = plt.subplots(2,3,figsize = (12,8))

axes[0,0].imshow(img,cmap = 'gray')
axes[0,0].set_title("Оригинал 512х512")
axes[0,0].axis('off')

axes[0,1].imshow(img_small,cmap = 'gray')
axes[0,1].set_title("Уменьшенное 50х50")
axes[0,1].axis('off')

axes[0,2].imshow(img_nearest,cmap = 'gray')
axes[0,2].set_title("Ближайший соcед(order = 0)")
axes[0,2].axis('off')

axes[1,0].imshow(img_linear,cmap = 'gray')
axes[1,0].set_title("Линейная(order = 1)")
axes[1,0].axis('off')

axes[1,1].imshow(img_cubic,cmap = 'gray')
axes[1,1].set_title("Кубическая")
axes[1,1].axis('off')

axes[1,2].imshow(img_quintic,cmap = 'gray')
axes[1,2].set_title("Сплайн 5-го порядка")
axes[1,2].axis('off')

plt.tight_layout()
plt.show()