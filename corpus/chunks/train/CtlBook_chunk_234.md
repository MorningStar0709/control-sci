# Solution:

Referring to Listing 8.2:

In lines 10-22 we dene the EOM terms and set up A and B matrices.

We have this unusual output in which the output is a linear combination of the states which we implement with the C matrix. Note that for this single output case, C could be 2x2 or a 2x1 column vector equivalently:

$$
C = \left[ \begin{array}{c} 2 \\ 0. 7 \end{array} \right]
$$

Finally, there is no contribution of input directly to the output, so

$$
D = \left[ \begin{array}{c c} 0, & 0 \\ 0, & 0 \end{array} \right]
$$

We will do the step response two ways to illustrate one-output or two-output modes:

First performing step response (Line 37) we get a python control TimeResponse object (stepResponseData) which gives us the time and amplitude vector for our special combined output (based on our A,B,C,D values) x(t), x(t) (this output is not shown here).

To illustrate outputting both states, we redo C,D, to plot both x(t), x˙ (t) (line 49) which plots both as below.

![](image/93cebd03a95de3154c414fdb007bcade09fdee135f4580e7c609b5d637eb8935.jpg)

<details>
<summary>line</summary>

| Time [s] | Position X | Velocity X-dot |
| --- | --- | --- |
| 0 | 0.028 | 0.005 |
| 5 | 0.009 | -0.003 |
| 10 | 0.022 | 0.003 |
| 15 | 0.013 | -0.001 |
| 20 | 0.019 | 0.001 |
| 25 | 0.015 | -0.001 |
| 30 | 0.017 | 0.000 |
| 35 | 0.016 | -0.001 |
| 40 | 0.016 | 0.000 |
| 45 | 0.016 | -0.001 |
| 50 | 0.016 | 0.000 |
| 55 | 0.016 | -0.001 |
| 60 | 0.016 | 0.000 |
| 65 | 0.016 | -0.001 |
| 70 | 0.016 | 0.000 |
| 75 | 0.016 | -0.001 |
| 80 | 0.016 | 0.000 |
| 85 | 0.016 | -0.001 |
| 90 | 0.016 | 0.000 |
| 95 | 0.016 | -0.001 |
| 100 | 0.016 | 0.000 |
</details>

```python
import numpy as np
import control as ctl
import matplotlib.pyplot as plt

def RowVector(x):  # vectors in numpy have to be 2-dimensional(!)
    x = np.matrix([x])
    return np.atleast_2d(x)
def ColVector(x):
    return RowVector(x).T
