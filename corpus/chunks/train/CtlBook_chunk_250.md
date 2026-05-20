# Example 8.2

4x4 State space example in python.

The python code in Listing 8.4 sets up the state equations for Example 4.1.

In lines 5 to 14 we dene our helper functions to make it easier to set up ocial row and column vectors in numpy.

In lines 17 to 21 we enter mechanical parameters for our car suspension.

With reference to the derived state space equation, in lines 24-31 we set up the matrix elements, and in lines 48-66 we dene the A, B, C, D of the state space equations

$$\dot {x} = A x + B uy = C x + D u$$

Recall that x1 is not a 'state' but rather an input so our state vector is:

$$\boldsymbol {x} = [ \boldsymbol {x} _ {2}, \dot {\boldsymbol {x}} _ {2}, \boldsymbol {x} _ {3}, \dot {\boldsymbol {x}} _ {3} ] ^ {T}$$

Line 6 (2nd page of listing) creates a control.StateSpace class instance from our four matrices.

In lines 12 we compute the step response of our system. Here we should be aware that python.control determines the number of inputs and outputs from the dimensions of B and C. If B > 1 or C > 1, there is more than one transfer function based on the permutations of inputs and outputs. For our system here, B has one column (line 33) so there is just one input and C is 4x4 meaning 4 outputs.

In lines 17-18 we plot 4 step responses based on the 4x4 C matrix (line 60 prev. page) which generates an output vector containing the step responses.

```python
import numpy as np
import control as ctl
import matplotlib.pyplot as plt
