# Example 4.8 Full-order observer for the double integrator

Consider a double-integrator plant. The matrix $\Phi - KC$ is given by

$$
\Phi_ {o} = \Phi - K C = \left( \begin{array}{l l} 1 & h \\ 0 & 1 \end{array} \right) - \left( \begin{array}{l} k _ {1} \\ k _ {2} \end{array} \right) \left( \begin{array}{l l} 1 & 0 \end{array} \right) = \left( \begin{array}{l l} 1 - k _ {1} & h \\ - k _ {2} & 1 \end{array} \right)
$$

Thus the characteristic equation is given by

$$z ^ {2} - (2 - k _ {1}) z + 1 - k _ {1} + k _ {2} h = 0$$

Let the desired characteristic equation be

$$z ^ {2} + p _ {1} z + p _ {2} = 0$$

The following equations are obtained:

$$2 - k _ {1} = - p _ {1}1 - k _ {1} + k _ {2} h = p _ {2}$$

These linear equations give

$$k _ {1} = 2 + p _ {1}k _ {2} = \left(1 + p _ {1} + p _ {2}\right) / h$$

The deadbeat observer is obtained by setting $p_{1}=p_{2}=0$ . This gives

$$k _ {1} = 2k _ {2} = 1 / h$$

and the observer becomes

$$\hat {x} _ {1} (k + 1) = \hat {x} _ {1} (k) + h \hat {x} _ {2} (k) + 2 \left(y (k) - \hat {x} _ {1} (k)\right)\hat {x} _ {2} (k + 1) = \hat {x} _ {2} (k) + \frac {1}{h} (y (k) - \hat {x} _ {1} (k))$$

Straightforward calculations give

$$\hat {x} _ {1} (k + 1) = 2 y (k) - y (k - 1)\hat {x} _ {2} (k + 1) = \frac {y (k) - y (k - 1)}{h}$$
