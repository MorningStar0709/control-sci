# 7.9.3 Runge-Kutta fourth-order method

The most common method we’ll cover is Runge-Kutta fourth-order (RK4). It’s simple and accurate for most systems we’ll see in FRC. We’ll demonstrate how to translate its Butcher tableau into equations that integrate $\dot { \mathbf { x } } = f ( t , \mathbf { x } )$ from 0 to $h$ .

$$
\mathbf {k} _ {1} = f (t + 0 h, \mathbf {x} _ {k})\mathbf {k} _ {2} = f \left(t + \frac {1}{2} h, \mathbf {x} _ {k} + h \left(\frac {1}{2} \mathbf {k} _ {1}\right)\right)\mathbf {k} _ {3} = f (t + \frac {1}{2} h, \mathbf {x} _ {k} + h (0 \mathbf {k} _ {1} + \frac {1}{2} \mathbf {k} _ {2}))\mathbf {k} _ {4} = f (t + 1 h, \mathbf {x} _ {k} + h (0 \mathbf {k} _ {1} + 0 \mathbf {k} _ {2} + 1 \mathbf {k} _ {3}))\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h (\frac {1}{6} \mathbf {k} _ {1} + \frac {1}{3} \mathbf {k} _ {2} + \frac {1}{3} \mathbf {k} _ {3} + \frac {1}{6} \mathbf {k} _ {4})
\begin{array}{c c c c c} 0 & & & \\ \frac {1}{2} & \frac {1}{2} & & \\ \frac {1}{2} & 0 & \frac {1}{2} & & \\ 1 & 0 & 0 & 1 & \\ \hline & \frac {1}{6} & \frac {1}{3} & \frac {1}{3} & \frac {1}{6} \end{array}
$$

Remove zeroed out terms.

$$\mathbf {k} _ {1} = f (t, \mathbf {x} _ {k})\mathbf {k} _ {2} = f (t + \frac {1}{2} h, \mathbf {x} _ {k} + h \frac {1}{2} \mathbf {k} _ {1})\mathbf {k} _ {3} = f (t + \frac {1}{2} h, \mathbf {x} _ {k} + h \frac {1}{2} \mathbf {k} _ {2})\mathbf {k} _ {4} = f (t + h, \mathbf {x} _ {k} + h \mathbf {k} _ {3})\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h \left(\frac {1}{6} \mathbf {k} _ {1} + \frac {1}{3} \mathbf {k} _ {2} + \frac {1}{3} \mathbf {k} _ {3} + \frac {1}{6} \mathbf {k} _ {4}\right)$$

$\frac { 1 } { 6 }$ is usually factored out of the last equation to reduce the number of floating point operations.

$$\mathbf {x} _ {k + 1} = \mathbf {x} _ {k} + h \frac {1}{6} (\mathbf {k} _ {1} + 2 \mathbf {k} _ {2} + 2 \mathbf {k} _ {3} + \mathbf {k} _ {4})$$

In FRC, our differential equations are of the form $\dot { \mathbf { x } } = f ( \mathbf { x } , \mathbf { u } )$ where u is held constant between timesteps. Since it’s time-invariant, we can ignore the time argument of the integration method. This gives theorem 7.9.2.

Theorem 7.9.2 — Runge-Kutta fourth-order integration. Given the differential equation $\dot { \mathbf { x } } = f ( \mathbf { x } _ { k } , \mathbf { u } _ { k } )$ , this method solves for $\mathbf { x } _ { k + 1 }$ at h seconds in the future. u is assumed to be held constant between timesteps.
