from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=Path(__file__).resolve().parents[1]
u=np.linspace(0,1,1060);e=u**3*(u*(u*6-15)+10)
t=u*(106/30);theta=np.deg2rad(450)*e;radius=.8+(14-.8)*(1-(1-u)**3)
p=np.array([np.sin(theta)*radius,1.7+3.3*e,np.cos(theta)*radius]).T
v=np.gradient(p,t,axis=0);a=np.gradient(v,t,axis=0)
fig,axes=plt.subplots(3,1,figsize=(10,8))
for ax,values,title in zip(axes,[p,v,a],['position','velocity','acceleration']):
 for i,label in enumerate('xyz'):ax.plot(t,values[:,i],label=label)
 ax.set_ylabel(title);ax.legend(loc='upper left')
axes[-1].set_xlabel('S34 local seconds');fig.tight_layout();fig.savefig(r/'assets/helix-camera-qa.png',dpi=120)
assert np.isfinite(a).all()
print('450 degree orbit, radius 0.8 to 14, finite position/velocity/acceleration. Plot requires visual review.')
