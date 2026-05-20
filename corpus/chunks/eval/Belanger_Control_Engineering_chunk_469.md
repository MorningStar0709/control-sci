# M 7.65

Chemical reactor A model for a chemical reactor was derived in Problem 2.9 (Chapter 2) and linearized in Problem 2.15. Problem 3.48 (Chapter 3) showed that the equations for $\Delta \dot{c}_A$ and $\Delta \dot{T}$ constitute a minimal realization. A pole-placement controller was designed in Problem 7.13, but control against unmeasured constant disturbances must be added.

a. Append the equation $\Delta\dot{Q}^{*}=0$ to the two linear state equations, as in Equations 7.96 and 7.97.   
b. With $\Delta T$ as measured output, design a reduced-order observer for the variables $\Delta c_A$ and $\Delta Q^*$ . The error-system eigenvalues are to be $-0.8 \pm j0.8$ .   
c. Express the observer in a form that does not require the evaluation of derivatives. Write the state description of the controller with $\Delta Q = \Delta \widehat{Q}^{*} - K[\frac{\Delta T}{\Delta \hat{c}_{A}}]$ , where $K$ is the gain from Problem 7.13.   
d. Calculate the controller transfer function $\Delta Q / \Delta T_{d}$ .   
e. Apply this linear control to the nonlinear model of Problem 2.9 (Chapter 2), and compute the responses to steps in $\Delta T_{d}$ of $10^{\circ}\mathrm{K}$ , $20^{\circ}\mathrm{K}$ , and $40^{\circ}\mathrm{K}$ .
