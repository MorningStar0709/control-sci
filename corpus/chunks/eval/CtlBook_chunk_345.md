#
z1 = -6+2j
z2 = cc(z1)
K=1
rp = -50
Controller = (K*np.abs(rp)*(s-z1)*(s-z2)) / (s*(s-rp))  # regularized PID controller
