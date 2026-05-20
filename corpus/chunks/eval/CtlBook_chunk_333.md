# Specs: T_s < 1.33 %OS <= 1% (34deg, zeta = 0.83)
sigTS = -4/1.33
angOS = 34.0*np.pi/180.0 #rad
plt.plot([sigTS,sigTS],[-yl,yl],color='g') # vert line for Ts
rad = 8
ostargIM = rad*np.sin(angOS)
ostargRE = rad*np.cos(angOS)
plt.plot([0, -ostargRE,0,-ostargRE],[0, ostargIM ,0, -ostargIM],color='purple')
} % end of query (frmlry 
```
