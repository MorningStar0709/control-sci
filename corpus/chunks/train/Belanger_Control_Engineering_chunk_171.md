$$
\left[ \begin{array}{c} \Delta \ell \\ \Delta C _ {S} \end{array} \right] = T ^ {- 1} \left[ \begin{array}{c} \Delta \ell \\ \Delta V _ {A} \end{array} \right].
$$

Use the symbolic form of the linearized equations, rather than the form with numerical values for the coefficients.

b. Show that the transformation matrix $T$ diagonalizes the equations. (This is one case where the transformed variables have physical meaning.)

c. Use the transformed equations to interpret the results of Problem 3.32.

3.48 Chemical reactor For the linearized system of Problem 2.15 (Chapter 2), show that the differential equations for $\Delta c_A$ and $\Delta T$ , taken together, are a minimal realization of the transfer function $\Delta T / \Delta Q$ .

3.49 Show that the controllable canonical form is controllable.

3.50 Show that the observable canonical form is observable.

3.51 Give the controllable and observable canonical forms for a system with transfer function $H(s) = (s + 1) / (s^3 + s^2 + s + 1)$ .

3.52 Repeat Problem 3.51 for $H(s) = (2s + 3) / (s^3 - 2s^2 + s + 2)$ .

3.53 Servo with flexible shaft Give the controllable and observable canonical forms for the transfer function $\theta_{2}/v$ of Problem 3.14.

3.54 Heat exchanger Give the controllable and observable canonical forms for the transfer function $\Delta T_{c3}/\Delta F_{H}$ of Problem 3.18.

3.55 The system of Figure 3.22 consists of two cascaded subsystems, $S_{1}$ and $S_{2}$ , with transfer functions $H_{1}(s)$ and $H_{2}(s)$ , respectively. With

$$H _ {1} (s) = \frac {1}{(s - 1) (s + 1)}, \quad H _ {2} (s) = \frac {2 (s - 1)}{s ^ {2} + s + 1}$$

a. Give realizations in controllable canonical form for $S_{1}$ and $S_{2}$ .

b. If x1 and x2 are the state vectors for $S_{1}$ and $S_{2}$ , respectively, give a realization for the composite system $S_{1}$ using $x = \begin{bmatrix} x1 \\ x2 \end{bmatrix}$ as the state vector.

c. Is the realization of $S$ derived in part (b) minimal? If not, find the uncontrollable and/or unobservable mode(s).

![](image/729ae3ce1a826da4b5039848d3885c5c9610430bdc90cef2506a0958943335c4.jpg)  
Figure 3.22 Series interconnection of two subsystems

3.56 Repeat Problem 3.55, but with $H_{2}(s)$ as the transfer function for $S_{1}$ and $H_{1}(s)$ as the transfer function for $S_{2}$ .

3.57 Is the composite system S of Problem 3.55 internally stable? Is it input-output stable? Explain.
