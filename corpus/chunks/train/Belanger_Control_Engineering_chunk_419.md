# (Active Suspension)

In the active suspension of Example 2.2 (Chapter 2), let the roadway deviation be represented by the equation $\dot{y}_R = w(t)$ .

(a) Write a new set of state equations, with the state variables $\ell_1 = x_1 - x_2$ , $\ell_2 = x_1 - y_R$ , $v_1$ , and $v_2$ .   
(b) Design a state feedback law that will ensure $\ell_1 = \ell_{1d}$ in the steady state, with closed-loop eigenvalues at $-3 \pm j3$ , $-25 \pm j25$ , and $-5$ .   
(c) Simulate the response, from equilibrium, for $w(t) = 0.1u_0(t)$ and $\ell_{1d} = 0.1$ .

Solution The new state equations, with an integrator appended, are

$$\dot {\ell} _ {1} = v _ {1} - v _ {2}\dot {\ell} _ {2} = v _ {1} - w\dot {v} _ {1} = - 1 0 \ell_ {1} - 2 \left(v _ {1} - v _ {2}\right) + 0. 0 0 3 3 4 u\dot {v} _ {2} = 6 0 \ell_ {1} + 1 2 \left(v _ {1} - v _ {2}\right) - 6 6 0 \left(- \ell_ {1} + \ell_ {2}\right) - 0. 0 2 u\dot {x} = \ell_ {1} - \ell_ {1 d}.$$

In matrix form,

$$
\frac {d}{d t} \left[ \begin{array}{c} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \\ x \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 0 & 1 & - 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ - 1 0 & 0 & - 2 & 2 & 0 \\ 7 2 0 & - 6 6 0 & 1 2 & - 1 2 & 0 \\ 1 & 0 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \\ x \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ . 0 0 3 3 4 \\ -. 0 2 \\ 0 \end{array} \right] u + \left[ \begin{array}{c} 0 \\ - 1 \\ 0 \\ 0 \\ 0 \end{array} \right] w - \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{array} \right] \ell_ {1 d}.
$$

The new state variables have an advantage over the previous ones in that the absolute heights $x_{1}$ and $x_{2}$ are no longer needed—a definite plus if the vehicle is to travel over mountainous terrain, for example. That is made possible by the fact that $y_{d}$ is described by pure integration.

By pole placement (MATLAB place), we obtain the gain

$$\mathbf {k} ^ {T} = \left[ 5. 1 4 9 3 e 4 - 2. 5 2 2 3 e 4 \quad 6. 2 2 8 0 e 3 - 1. 3 0 9 9 e 3 \quad 5. 1 0 3 4 e 4 \right]$$

It is not difficult to show that, at equilibrium, $\ell_1 = \ell_2 = \ell_{1d}$ , $v_1 = v_2 = 0$ , and $u = 3000\ell_{1d}$ ; the state variable $x$ may have any value at all.

The control law is

$$u = - k _ {1} \ell_ {1} - k _ {2} \ell_ {2} - k _ {3} v _ {1} - k _ {4} v _ {2} - k _ {5} x.$$

At equilibrium, we must have

$$3 0 0 0 \ell_ {1 d} = - k _ {1} \ell_ {1 d} - k _ {2} \ell_ {1 d} - k _ {5} x ^ {*}$$

or

$$x ^ {*} = - 0. 5 7 3 5 \ell_ {1 d}.$$
