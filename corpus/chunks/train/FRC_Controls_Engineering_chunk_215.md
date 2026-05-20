# 7.9.2 Forward Euler method

The simplest explicit Runge-Kutta integration method is forward Euler integration. Avoid it because it suffers from numerical stability issues. We’ll demonstrate how to translate its Butcher tableau into equations that integrate $\dot { \mathbf { x } } = f ( t , \mathbf { x } )$ from 0 to h.

$$
\begin{array}{l} \mathbf {k} _ {1} = f (t + 0 h, \mathbf {x} _ {k}) \\ \mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h (1 \mathbf {k} _ {1}) \\ \begin{array}{c c} 0 & \\ \hline & 1 \end{array} \\ \end{array}
$$

Remove zeroed out terms.

$$\mathbf {k} _ {1} = f (t, \mathbf {x} _ {k})\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h \mathbf {k} _ {1}$$

Simplify.

$$\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h f (t, \mathbf {x} _ {k})$$

In FRC, our differential equations are of the form $\dot { \mathbf { x } } = f ( \mathbf { x } , \mathbf { u } )$ where u is held constant between timesteps. Since it’s time-invariant, we can ignore the time argument of the integration method. This gives theorem 7.9.1.

Theorem 7.9.1 — Forward Euler integration. Given the differential equation $\dot { \mathbf { x } } = f ( \mathbf { x } _ { k } , \mathbf { u } _ { k } )$ , this method solves for $\mathbf { x } _ { k + 1 }$ at $h$ seconds in the future. u is assumed to be held constant between timesteps.

$$
\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h f (\mathbf {x} _ {k}, \mathbf {u} _ {k})
\begin{array}{c c} 0 & \\ \hline & 1 \end{array}
$$
