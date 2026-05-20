# Converting Transfer Functions to State Space and Back

Python control has functions to easily convert back and forth between transfer functions and state space system descriptions. For example, suppose we have the transfer function:

$$\frac {s + 2}{s ^ {2} + 2 0 s + 9 6}$$

we can easily use python's tf2ss(sys) function to convert this to a state space representation as in Listing 8.5:

Python.control returns a linear system object which contains all four matrices $A , B , C , D .$ . In the computation above, the matrices $A \dots D$ are not necessarily the same as those you would derive using the system EOMs. However they describe an equivalent dynamical system. It turns out there are many SS representations for each transfer function or dynamical system. A full treatment of this issue requires a course in modern control theory, but a few interesting observations are worth noting.

The eigenvalues of the system matrix A, are the same as the poles of the transfer function. In the example above,

$$\frac {s + 2}{s ^ {2} + 2 0 s + 9 6} = \frac {s + 2}{(s + 8) (s + 1 2)}$$

has poles $s = \{ - 8 , - 1 2 \}$ . The function to compute eigenvalues in python is np.linalg.ei $\mathtt { g } ( )$ . Using it on the matrix A computed above gives $[ - 8 , - 1 2 ]$ as expected from the poles.

```python
import numpy as np
import control as ctl
import matplotlib.pyplot as plt

s = ctl.TransferFunction.s
tf1 = (s+2)/(s**2+20*s+96)
ssys = ctl.tf2ss(tf1)

print(ssys)
