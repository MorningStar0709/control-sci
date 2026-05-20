$$
\begin{array}{l} \begin{array}{l} x \left(t _ {k + 1}\right) = \Phi \left(t _ {k + 1}, t _ {k}\right) x \left(t _ {k}\right) + \Gamma \left(t _ {k + 1}, t _ {k}\right) u \left(t _ {k}\right) \\ v (t) = C v (t) + D v (t). \end{array} \tag {2.3} \\ y (t _ {k}) = C x (t _ {k}) + D u (t _ {k}) \\ \end{array}
$$

where

$$
\begin{array}{l} \Phi (t _ {k + 1}, t _ {k}) = e ^ {\Lambda (t _ {k + 1} - t _ {k})} \\ \Gamma (t _ {k + 1}, t _ {k}) = \int_ {0} ^ {t _ {k + 1} - t _ {k}} e ^ {A s} d s B \\ \end{array}
$$

The relationship between the sampled signals thus can be expressed by the linear difference equation, (2.3). Notice that Equation (2.3) does not involve any approximations. It gives the exact values of the state variables and the output at the sampling instants because the control signal is constant between the sampling instants. The model in (2.3) is therefore called a zero-order-hold sampling of the system in (2.1). The system in (2.3) can also be called the zero-order-hold equivalent of (2.1).

In most cases D = 0. One reason for this is because in computer-controlled systems, the output y is first measured and the control signal $u(t_{k})$ is then generated as a function of $y(t_{k})$ . In practice it often happens that there is a significant delay between the A-D and D-A conversions. However, it is easy to make the necessary modifications. The state vector at times between sampling points is given by (2.2). This makes it possible to investigate the intersample behavior of the system. Notice that the responses between the sampling points are parts of step responses, with initial conditions, for the system. This implies that the system is running in open loop between the sampling points.

For periodic sampling with period h, we have $t_{k} = k \cdot h$ and the model of (2.3) simplifies to the time-invariant system

$$
\begin{array}{l} x (k h + h) = \Phi x (k h) + \Gamma u (k h) \\ \text {（2.4）} \end{array}
y (k h) = C x (k h) + D u (k h)
$$

where

$$
\begin{array}{l} \Phi = e ^ {A h} \\ \Gamma = \int_ {0} ^ {h} e ^ {A s} d s B \tag {2.5} \\ \end{array}
$$

It follows from (2.5) that

$$\frac {d \Phi (t)}{d t} = A \Phi (t) = \Phi (t) A\frac {d \Gamma (t)}{d t} = \Phi (t) B$$

The matrices $\Phi$ and $\Gamma$ therefore satisfy the equation

$$
\frac {d}{d t} \left( \begin{array}{c c} \Phi (t) & \Gamma (t) \\ 0 & I \end{array} \right) = \left( \begin{array}{c c} \Phi (t) & \Gamma (t) \\ 0 & I \end{array} \right) \left( \begin{array}{c c} A & B \\ 0 & 0 \end{array} \right)
$$

where I is a unit matrix of the same dimension as the number of inputs. The matrices $\Phi(h)$ and $\Gamma(h)$ for the sampling period h therefore can be obtained from the block matrix

$$
\left( \begin{array}{c c} \Phi (h) & \Gamma (h) \\ 0 & I \end{array} \right) = \exp \left(\left( \begin{array}{c c} A & B \\ 0 & 0 \end{array} \right) h\right) \tag {2.6}
$$
