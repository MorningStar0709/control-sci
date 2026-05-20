$$J = \int_ {0} ^ {\infty} \left(\mathbf {x} ^ {\prime} \mathbf {Q x} + u ^ {\prime} R u\right) d t$$

where

$$
\mathbf {Q} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right], \quad R = [ 1 ]
$$

Assume that the following control u is used.

$$u = - \mathbf {K x}$$

Determine the optimal feedback gain matrix K.

The optimal feedback gain matrix K can be obtained by solving the following Riccati equation for a positive-definite matrix P:

$$\mathbf {A} ^ {\prime} \mathbf {P} + \mathbf {P A} - \mathbf {P B R} ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {P} + \mathbf {Q} = \mathbf {0}$$

The result is

$$
\mathbf {P} = \left[ \begin{array}{c c} 2 & 1 \\ 1 & 1 \end{array} \right]
$$

Substituting this P matrix into the following equation gives the optimal K matrix:

$$
\mathbf {K} = R ^ {- 1} \mathbf {B} ^ {\prime} \mathbf {P}
= [ 1 ] \left[ \begin{array}{l l} 0 & 1 \end{array} \right] \left[ \begin{array}{l l} 2 & 1 \\ 1 & 1 \end{array} \right] = \left[ \begin{array}{l l} 1 & 1 \end{array} \right]
$$

Thus, the optimal control signal is given by

$$u = - \mathbf {K x} = - x _ {1} - x _ {2}$$

MATLAB 10–19 also yields the solution to this problem.
