9.10 Obtain the recursive algorithm (i.e., the difference equation) corresponding to the following pulse transfer functions:

a. $H(z) = (z + 1) / (z^2 + z + 1)$ .   
b. $H(z) = [1/z^{3}(z - .7)]$ .

9.11 Obtain the pulse transfer function of the discrete-time system in state form, with $A = \left[ \begin{array}{ll}0.3 & 0\\ -0.5 & 0.5 \end{array} \right]$ , $\mathbf{b} = \left[ \begin{array}{ll}0\\ 1 \end{array} \right]$ , $\mathbf{c} = [1\quad 0]$ , and $D = 0$ .   
9.12 Repeat Problem 9.11 with $A = \left[ \begin{array}{cc}0 & 2 \\ -2 & 2 \end{array} \right]$ , $\mathbf{b} = \left[ \begin{array}{c}1\\ -1 \end{array} \right]$ , $\mathbf{c} = [1\quad 0]$ , and $D = 0$ .   
9.13 Rewrite the system

$$\mathbf {x} (k + 1) = A \mathbf {x} (k) + B \mathbf {u} (k - n)$$

in standard-state form, by introducing new state variables corresponding to different delayed input values. Show that the resulting A-matrix has at least n eigenvalues at the origin.

9.14 Calculate $A^k$ , $A = [\begin{array}{cc}0 & 1 \\ .5 & .5\end{array}]$ .   
9.15 Calculate $A^k, A = \left[\begin{array}{cc} - .5 & 0 \\ 0 & .7 \end{array}\right]$ .

9.16 Between sampling instants $k$ and $k + 1$ , a zero-order hold maintains the input $u$ of a sampled-data system at a constant value $\widehat{u}(k)$ . Thus, $\dot{u} = 0$ , $kT_s \leq t < (k + 1)T_s$ . Append this to the continuous-time system state equations, and show how $\mathcal{A}$ and $\mathcal{B}$ in Equation 9.31 can be computed with software that computes $e^{At}$ .

9.17 For the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 1 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 1 \\ - 1 \end{array} \right] u
y = [ 1 \quad 0 ] \mathbf {x}.
$$

a. Compute the sampled-data state representation with x as the state vector, as a function of the sampling period $T_{s}$ .   
b. Verify that the eigenvalues of the discrete-time system are $e^{s_i T_s}$ , where $s_i$ are the eigenvalues of the continuous-time system.   
c. Compute the pulse transfer function.

9.18 Repeat Problem 9.17 for

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 1 & 0 \\ - 1. 5 & . 7 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c}. 5 \\ 1 \end{array} \right] u.
y = [ 1 \quad 1 ] \mathbf {x}.
$$
