
from pylab import *
from numpy import loadtxt

bands = loadtxt('pw.dat')

plot(bands[:,0], bands[:,1], 'ro', ms=5)

xlim((0,26))
xticks([0,10,15,26],['$\Gamma$','M','K','$\Gamma$'])
axvline(10)
axvline(15)
ylabel('Energy (eV)')

show()
