$$
\begin{array}{l} A - B K = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{c} - 1 \\ 1 \end{array} \right] [ k _ {1} \quad k _ {2} ] \\ = \left[ \begin{array}{c c} 0 & 1 \\ 0 & 0 \end{array} \right] - \left[ \begin{array}{c c} - k _ {1} & - k _ {2} \\ k _ {1} & k _ {2} \end{array} \right] \\ = \left[ \begin{array}{c c} k _ {1} & 1 + k _ {2} \\ - k _ {1} & - k _ {2} \end{array} \right]. \\ \end{array}
$$

The characteristic equation is

$$\det (s I - A + B K) = 0$$

or

$$
\det \left[ \begin{array}{c c} s - k _ {1} & - 1 - k _ {2} \\ k _ {1} & s + k _ {2} \end{array} \right] = 0
s ^ {2} + \left(k _ {2} - k _ {1}\right) s + k _ {1} = 0.
$$

The closed-loop eigenvalues are

$$s _ {1}, s _ {2} = \frac {k _ {1} - k _ {2} \pm \sqrt {k _ {1} ^ {2} - 2 k _ {1} k _ {2} + k _ {2} ^ {2} - 4 k _ {1}}}{2}.$$

Clearly, they change with $k_{1}$ and $k_{2}$ .

By contrast, the zeros are unchanged by state feedback.

Theorem 7.1

Let z be a transmission zero of the system $\dot{x} = Ax + Bu$ , $y = Cx + Du$ , and let the closed-loop system be defined by the state feedback law $u = -Kx + u_{ex}$ . Then z is also a transmission zero of the closed-loop matrix transfer function relating y to $u_{ex}$ .

Proof: From Chapter 3, $z$ satisfies

$$
\operatorname{rank} \left[ \begin{array}{c c} - z I + A & B \\ C & D \end{array} \right] <   n + r.
$$

Since the above matrix is not of full rank, there exists a vector $[ \begin{array}{c} \mathbf{v}_1 \\ \mathbf{v}_2 \end{array} ]$ such that

$$
\left[ \begin{array}{c c} - z I + A & B \\ C & D \end{array} \right] \left[ \begin{array}{l} \mathbf {v} _ {1} \\ \mathbf {v} _ {2} \end{array} \right] = 0. \tag {7.10}
$$

With state feedback, the system equations are

$$\dot {\mathbf {x}} = A \mathbf {x} - B K \mathbf {x} + B \mathbf {u} _ {e x}y = C \mathbf {x} - D K \mathbf {x} + D \mathbf {u} _ {e x}.$$

A closed-loop zero $\zeta$ satisfies

$$
\operatorname{rank} \left[ \begin{array}{c c} - \zeta I + A - B K & B \\ C - D K & D \end{array} \right] <   n + r. \tag {7.11}
$$

We claim that this holds with $\zeta = z$ . To see this, form
