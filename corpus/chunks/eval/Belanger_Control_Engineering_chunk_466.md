a. For the Maglev model of Problem 2.20 (Chapter 2), design a reduced-order observer with the gap lengths $\Delta S_{L1}$ , $\Delta S_{L2}$ , $\Delta_{G1}$ , and $\Delta S_{G2}$ as measurements. Place the poles of the second-order error system at $-300 \pm j300$ .   
b. Obtain, by simulation, the time and observed state variables for zero inputs and (i) $\Delta z(0)=1$ , (ii) $\Delta\theta(0)=1$ , (iii) $\Delta y(0)=1$ , and all other state variables being zero.

![](image/ee8d3f4bb95deb1afcbbbe0db618e9785450172cb9543aa629bf4494b04c5003.jpg)

7.56 Maglev Sensors do fail, and failure is often detectable. Suppose $\Delta S_{L1}$ becomes unavailable. We wish to reconfigure the observer to handle this contingency.

a. For the Maglev model, design a reduced-order observer using the gap lengths $\Delta S_{L2}$ , $\Delta S_{G1}$ , and $\Delta S_{G2}$ as measurements. Place the poles of the error system at $-300 \pm j300$ and $-300$ .   
b. Simulate for the conditions of Problem 7.55, and compare.   
c. In the event of a failure, how would you initialize the third-order observer to ensure smooth transfer from the second-order observer?

7.57 In Problem 7.6, a pole-placement state feedback was designed for the system of Problem 7.1. A second-order observer for this plant was designed in Problem 7.37.

a. Write the state description of the controller that results from generating a state estimate and using this in the control law.   
b. Compute the transfer function u/y of the control law.

7.58 Repeat Problem 7.57 for the plant of Problem 7.2, the state feedback law of Problem 7.7, and the observer of Problem 7.38.

7.59 The plant of Problem 7.1 is to be regulated to a nonzero reference value, with zero steady-state error. This requires a steady-state control component, $u^{*}$ . We wish to design a controller that uses an estimate of $u^{*}$ and an estimate of the incremental state $\Delta x$ .

a. Design a third-order observer for $u^*$ and $\Delta x$ .   
b. Using the state feedback gain $\mathbf{k}^T$ of Problem 7.6, design a controller where $u = \widehat{u}^{*} + \mathbf{k}^{T}\widehat{\mathbf{x}}$ .   
c. Calculate the transfer function $u / e$ , where $e = y_{d} - y = -\Delta y$ . Verify that this transfer function contains an integrator.

![](image/24d6da2980d6e3c14003462e2c8b069918ff04755953310703f22dc20d181d64.jpg)
