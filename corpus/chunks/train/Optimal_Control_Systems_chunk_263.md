# 5.2 Discrete-Time Optimal Control Systems

We develop the Minimum Principle for discrete-time control systems analogous to that for continuous-time control systems addressed in previous Chapters 2, 3, and 4. Instead of repeating all the topics of the continuous-time systems for the discrete-time systems, we focus on linear quadratic optimal control problem. We essentially approach the problem using the Lagrangian and Hamiltonian (or Pontryagin) functions.

Consider a linear, time-varying, discrete-time control system described by

$$\mathbf {x} (k + 1) = \mathbf {A} (k) \mathbf {x} (k) + \mathbf {B} (k) \mathbf {u} (k) \tag {5.2.1}$$

where, $k = k_{0}$ , $k_{1}, \ldots, k_{f} - 1$ , $\mathbf{x}(k)$ is nth order state vector, $\mathbf{u}(k)$ is rth order control vector, and $\mathbf{A}(k)$ and $\mathbf{B}(k)$ are matrices of nxn and nxr dimensions, respectively. Note that we used A and B for the state space representation for discrete-time case as well as for the continuous-time case as shown in the previous chapters. One can alternatively use, say G and E for the discrete-time case so that the case of discretization of a continuous-time system with A and B will result in G and E in the discrete-time representation. However, the present notation should not cause any confusion once we redefine the matrices in the discrete-time case. We are given the initial condition as

$$\mathbf {x} (k = k _ {0}) = \mathbf {x} (k _ {0}). \tag {5.2.2}$$

We will discuss later the final state condition and the resulting relations. We are also given a general performance index (PI) with terminal cost as

$$
\begin{array}{l} J = J (\mathbf {x} (k _ {0}), \mathbf {u} (k _ {0}), k _ {0}) \\ = \frac {1}{2} \mathbf {x} ^ {\prime} \left(k _ {f}\right) \mathbf {F} \left(k _ {f}\right) \mathbf {x} \left(k _ {f}\right) \\ + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \mathbf {x} ^ {\prime} (k) \mathbf {Q} (k) \mathbf {x} (k) + \mathbf {u} ^ {\prime} (k) \mathbf {R} (k) \mathbf {u} (k) \right] \tag {5.2.3} \\ \end{array}
$$

where, $\mathbf{F}(k_f)$ and $\mathbf{Q}(k)$ are each $nxn$ order symmetric, positive semi-definite matrices, and $\mathbf{R}(k)$ is $rxr$ symmetric, positive definite matrix.

The methodology for linear quadratic optimal control problem is carried out under the following steps.
