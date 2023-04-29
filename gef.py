from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib .ticker import LinearLocator,FormatStrFormatter

def f(x,y):
    return x**2 + y**2 +1
y=arange(-5,5,.25)
x=arange(-5,5,.25)
X,Y =meshgrid(x,y)
Z=f(X,Y)



fig=figure(1)
ax=fig.gca(projection='3d')
surf=ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=cm.RdBu,linewidth=0,antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink = 0.7, aspect=5)
show()