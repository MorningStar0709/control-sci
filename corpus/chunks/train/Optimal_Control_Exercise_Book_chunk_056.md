# Solution:

We can consider this problem as a fixed-time, free-endpoint problem subject to the Euler Lagrange Equations. The first step is to calculate the Hamiltonian. First, let’s calculate the Lagrangian as:

$$L (t, x (t), u (t)) = \frac {1}{2} \left(x (t) ^ {2} + P u (t) ^ {2}\right) \tag {196}$$

The Hamiltonian will be calculated as:

$$H (t, x (t), u (t), p (t)) = \langle p (t), f ((t), x (t), u (t)) \rangle - L (t, x (t), u (t)) = \dots \tag {197}\dots = p (t) u (t) - \frac {1}{2} x (t) ^ {2} - \frac {P}{2} u (t) ^ {2} \tag {198}$$

Now, we have to calculate the adjoint vector $p ( t )$ which satisfies the following differential equation:

$$\dot {p} (t) = - H _ {x} (t, x (t), u (t), p (t)) = x (t) \tag {199}\text { with } p (1) = - K _ {x} \left(1, x ^ {*} (1)\right) = 0 (\text { since there is no terminal cost }) \tag {200}$$

Therefore, ${ \dot { p } } ( t ) = x ( t )$ ,with the final state condition $p ( 1 ) = 0$ . Now, we have the first order condition on the Hamiltonian of:

$$H _ {u} (t, x (t), u (t), p (t)) = p (t) - P u (t) = 0 \tag {201}$$

from which we obtain $\begin{array} { r } { u ( t ) = \frac { p ( t ) } { P } } \end{array}$ p . We can summarize the influence on the state as

$$\dot {x} (t) = p (t) = P u (t) \tag {202}$$

We have the two-point boundary value problem (TPBVP) stated as follows:

$$
\left\{ \begin{array}{l l} \dot {x} (t) = p (t), & t _ {0} = 0, \quad x (0) = 1 \\ \dot {p} (t) = x (t), & t _ {f} = 1, \quad p (1) = 0 \end{array} \right. \tag {203}
$$

We can observe that ${ \ddot { x } } ( t ) = { \dot { p } } ( t ) = x ( t ) \Longrightarrow { \ddot { x } } ( t ) = x ( t )$ . We solve this second order differential equation whose solution is:

$$
\left\{ \begin{array}{l} x (t) = c _ {1} e ^ {t} + c _ {2} e ^ {- t} \\ p (t) = \dot {x} (t) = c _ {1} e ^ {t} - c _ {2} e ^ {- t} \end{array} \right. \tag {204}
$$

Now, we can obtain the values of $c _ { 1 }$ and $c _ { 2 }$ from the boundary conditions:

$$
\left\{ \begin{array}{l} x (0) = 1 \Longrightarrow x (0) = c _ {1} + c _ {2} = 1 \\ p (1) = 0 \Longrightarrow p (1) = c _ {1} e - c _ {2} e ^ {- 1} \Longrightarrow c _ {2} = c _ {1} e ^ {2} \end{array} \right. \tag {205}
$$

from which we obtain

$$
\left\{ \begin{array}{l l} & c _ {1} = \frac {1}{1 + e ^ {2}} \\ & c _ {2} = \frac {e ^ {2}}{1 + e ^ {2}} \end{array} \right. \tag {206}
$$

The optimal solution then becomes:
