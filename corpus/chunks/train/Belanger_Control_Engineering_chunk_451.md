7.12 Heat exchanger The heat exchanger model of Problem 2.8 (Chapter 2), linearized as in Problem 2.14, has open-loop poles at -0.1914, -0.5252 ± j0.1278, -1.2872, and -0.9531 ± j0.1278. [See Problem 3.18 (Chapter 3) for the transfer function.] The poles have sufficient damping, but we wish to speed up the response, i.e., move some poles farther into the LHP. The system input is $\Delta F_{H}$ , the change in hot liquid flow from its steady-state value.

a. Obtain the state feedback gain matrix to place the closed-loop poles at -0.70, $-0.5252 \pm j0.5252$ , -1.2872, and $-0.9531 \pm j0.1278$ .   
b. Using the linearized model of Problem 2.14, design a control law, based on the gain of part (a), for regulation of $\Delta T_{c3}$ to a set point $\Delta T_d$ .   
c. Calculate the transfer function $\Delta T_{c3} / \Delta T_d$ , and compute the unit-step response.

![](image/cc1959694505a45d6cdc36c90c6bb71cee3a026c2bedb9b8e35d553f0eed14fc.jpg)

7.13 Chemical reactor The chemical reactor model of Problem 2.9 (Chapter 2) was linearized in Problem 2.15. It was shown in Problem 3.48 (Chapter 3) that the differential equations for $\Delta c_A$ and $\Delta T$ constitute a minimal realization for the input $\Delta Q$ and the output $\Delta T$ .

a. Use this minimal realization to design a state feedback control law to regulate $\Delta T$ to a set point $\Delta T_{d}$ , with closed-loop poles $-0.5 \pm j0.5$ .   
b. The closed-loop control system of part (a) is described by a new set of state equations, with $\Delta T_{d}$ as the input. Write this new set, starting from the fourth-order model of Problem 2.15. Identify the controllable and uncontrollable modes.   
c. Apply this linear control law to the nonlinear model of Problem 2.9, and compute the responses to steps in $\Delta T_{d}$ of $10^{\circ}\mathrm{K}$ , $20^{\circ}\mathrm{K}$ , and $40^{\circ}\mathrm{K}$ . Comment on the performance of the linear controller for this highly nonlinear system.

![](image/4fcb3a237bd805ce505d3462d3c1e1cda82f484de7eb0bade15e199fd13bb862.jpg)

7.14 High-wire artist The high-wire artist model of Problem 2.12 was linearized in Problem 2.18.
