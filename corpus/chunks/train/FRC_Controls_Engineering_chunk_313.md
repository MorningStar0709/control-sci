# 9.6.5 Steady-state Kalman gain

One may have noticed that the error covariance matrix can be updated independently of the rest of the model. The error covariance matrix tends toward a steady-state value, and this matrix can be obtained via the discrete algebraic Riccati equation. This can then be used to compute a steady-state Kalman gain.

General matrix inverses like $\mathbf { S } ^ { - 1 }$ are expensive. We want to put $\mathbf { K } = \mathbf { P } \mathbf { C } ^ { \mathsf { T } } \mathbf { S } ^ { - 1 }$ into Ax = b form so we can solve it more efficiently.

$$
\begin{array}{l} \mathbf {K} = \mathbf {P C} ^ {\top} \mathbf {S} ^ {- 1} \\ \mathbf {K S} = \mathbf {P C} ^ {\top} \\ (\mathbf {K S}) ^ {\mathsf {T}} = (\mathbf {P C} ^ {\mathsf {T}}) ^ {\mathsf {T}} \\ \mathbf {S} ^ {\mathsf {T}} \mathbf {K} ^ {\mathsf {T}} = \mathbf {C P} ^ {\mathsf {T}} \\ \end{array}
$$

The solution of Ax = b can be found via $\mathbf { x } = \mathrm { s o l v e } ( \mathbf { A } , \mathbf { b } )$ .

$$
\begin{array}{l} \mathbf {K} ^ {\mathsf {T}} = \operatorname{solve} (\mathbf {S} ^ {\mathsf {T}}, \mathbf {C P} ^ {\mathsf {T}}) \\ \mathbf {K} = \operatorname{solve} (\mathbf {S} ^ {\mathsf {T}}, \mathbf {C P} ^ {\mathsf {T}}) ^ {\mathsf {T}} \\ \end{array}
$$

Drop the transposes on symmetric matrices S and P.

$$\mathbf {K} = \operatorname{solve} (\mathbf {S}, \mathbf {C P}) ^ {\mathsf {T}}$$

Snippet 9.1 computes the steady-state Kalman gain matrix.

```python
"""Function for computing the steady-state Kalman gain matrix."""
import numpy as np
import scipy as sp

def kalmd(A, C, Q, R):
    """
    Solves for the discrete steady-state Kalman gain.

    Parameter ``A``:
    numpy.array(states x states), system matrix.

    Parameter ``C``:
    numpy.array(outputs x states), output matrix.

    Parameter ``Q``:
    numpy.array(states x states), process noise covariance matrix.

    Parameter ``R``:
    numpy.array(outputs x outputs), measurement noise covariance matrix.

    Returns: 
```

```python
numpy.array(outputs x states), Kalman gain matrix.
"""
P = sp.linalg.solve_discrete_are(a=A.T, b=C.T, q=Q, r=R)
return np.linalg.solve(C @ P @ C.T + R, C @ P).T 
```

Snippet 9.1. Steady-state Kalman gain matrix calculation in Python
