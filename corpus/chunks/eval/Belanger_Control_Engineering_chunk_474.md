# 7.70 Maglev The nominal value of one of $u_{G1}$ and $u_{G2}$ is arbitrary (the other is nominally equal to the first, but may not be exactly so if the magnets are slightly different). We wish to use the design technique of Chapter 6, Section 6.8.

a. Append the three equations $\Delta \dot{u}_{L1} = \Delta \dot{u}_{L2} = \Delta \dot{u}_{G2} = 0$ to the original set of state equations, and design a reduced-order observer of order 5. Place the poles of the error system at $-300, -300 \pm j300$ , and $-250 \pm j250$ .   
b. Proceed to design the controller as in Section 7.8, using the state feedback law of Problem 7.28.   
c. Simulate for the conditions of Problem 7.69(a).   
d. Compute the matrix transfer function of the controller, with the gap lengths as inputs and the input variables as outputs. Verify the presence of poles at s = 0.
