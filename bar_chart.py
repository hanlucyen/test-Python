import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
n=np.array([0,1,2,3,4,5])
x=np.linspace(0,5,10)
xx=np.linspace(-0.75,1.,100)
axl=plt.subplot2grid((2,4),(0,2))
axl.bar(n,n**2, align="center",width=0.5,alpha=0.5)
axl.set_title("bar chart")
