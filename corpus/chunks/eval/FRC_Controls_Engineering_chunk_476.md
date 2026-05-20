$$\mathcal {A} = \mathbf {A} - \mathbf {B R} ^ {- 1} \mathbf {N} ^ {\mathsf {T}}\mathcal {Q} = \mathbf {Q} - \mathbf {N R} ^ {- 1} \mathbf {N} ^ {\mathrm{T}}$$

If there is no cross-correlation between error and control effort, N is a zero matrix and the cost functional simplifies to

$$J = \sum_ {k = 0} ^ {\infty} (\mathbf {x} _ {k} ^ {\mathsf {T}} \mathbf {Q x} _ {k} + \mathbf {u} _ {k} ^ {\mathsf {T}} \mathbf {R u} _ {k})$$

The feedback control law which minimizes this J subject to $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { k }$ is

$$\mathbf {u} _ {k} = - \mathbf {K x} _ {k}$$

where K is given by

$$\mathbf {K} = \left(\mathbf {R} + \mathbf {B} ^ {\mathsf {T}} \mathbf {P B}\right) ^ {- 1} \mathbf {B} ^ {\mathsf {T}} \mathbf {P A}$$

and P is found by solving the discrete time algebraic Riccati equation defined as

$$\mathbf {A} ^ {\top} \mathbf {P A} - \mathbf {P} - \mathbf {A} ^ {\top} \mathbf {P B} (\mathbf {R} + \mathbf {B} ^ {\top} \mathbf {P B}) ^ {- 1} \mathbf {B} ^ {\top} \mathbf {P A} + \mathbf {Q} = 0$$

Snippets B.1 and B.2 compute the infinite horizon, discrete time LQR.

```cpp
#include <Eigen/Cholesky>
#include <Eigen/Core>

#include "dare.hpp"

template <int States, int Inputs>
Eigen::Matrix<double, Inputs, States> lqr(
    const Eigen::Matrix<double, States, States>& A,
    const Eigen::Matrix<double, States, Inputs>& B,
    const Eigen::Matrix<double, States, States>& Q,
    const Eigen::Matrix<double, Inputs, Inputs>& R,
    const Eigen::Matrix<double, States, Inputs>& N) {
    using StateMatrix = Eigen::Matrix<double, States, States];

auto R_llt = R_llt();
    StateMatrix A_2 = A - B * R_llt.solve(N.transpose());
    StateMatrix Q_2 = Q - N * R_llt.solve(N.transpose());

StateMatrix P = DARE<States, Inputs>(A_2, B, Q_2, R);

return (B.transpose() * P * B + R)
    .llt()
    .solve(B.transpose() * P * A + N.transpose());
} 
```

Snippet B.1. Infinite horizon, discrete time LQR solver in C++ (see subsection 5.11.2 for DARE solver)

```txt
""Function for computing the infinite horizon LQR."""
import numpy as np 
```

```python
import scipy as sp

def lqr(A, B, Q, R, N):
    """
    Solves for the optimal discrete linear-quadratic regulator (LQR).

Parameter ``A``:
    numpy.array(states x states), system matrix.

Parameter ``B``:
    numpy.array(states x inputs), input matrix.

Parameter ``Q``:
    numpy.array(states x states), state cost matrix.

Parameter ``R``:
    numpy.array(inputs x inputs), control effort cost matrix.
