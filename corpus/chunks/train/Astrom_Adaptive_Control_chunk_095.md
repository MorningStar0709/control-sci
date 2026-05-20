# Transfer Function Models

The least-squares method can be used to identify parameters in dynamical systems. Let the system be described by the model

$$A (q) y (t) = B (q) u (t) \tag {2.34}$$

where $q$ is the forward shift operator and $A(q)$ and $B(q)$ are the polynomials

$$A (q) = q ^ {n} + a _ {1} q ^ {n - 1} + \dots + a _ {n}B (q) = b _ {1} q ^ {m - 1} + b _ {2} q ^ {m - 2} + \dots + b _ {m}$$

Equation (2.34) can be written as the difference equation

$$y (t) + a _ {1} y (t - 1) + \dots + a _ {n} y (t - n) = b _ {1} u (t + m - n - 1) + \dots + b _ {m} u (t - n)$$

Assume that the sequence of inputs $\{u(1), u(2), \ldots, u(t)\}$ has been applied to the system and the corresponding sequence of outputs $\{y(1), y(2), \ldots, y(t)\}$ has been observed. Introduce the parameter vector

$$
\theta^ {T} = \left( \begin{array}{c c c c c c} a _ {1} & \dots & a _ {n} & b _ {1} & \dots & b _ {m} \end{array} \right) \tag {2.35}
$$

and the regression vector

$$
\varphi^ {T} (t - 1) = \left( \begin{array}{c c c c c} - y (t - 1) & \dots & - y (t - n) & u (t + m - n - 1) & \dots & u (t - n) \end{array} \right)
$$

Notice that the output signal appears delayed in the regression vector. The model is therefore called an autoregressive model. The way in which the elements are ordered in the matrix $\theta$ is, of course, arbitrary, provided that $\varphi(t-1)$ is also similarly reordered. Later, in dealing with adaptive control, it will be natural to reorder the terms. The convention that the time index of the $\varphi$ vector will refer to the time when all elements in the vector are available will also be adopted. The model can formally be written as the regression model

$$y (t) = \varphi^ {T} (t - 1) \theta$$

Parameter estimates can be obtained by applying the least-squares method (Theorem 2.1). The matrix $\Phi$ is given by

$$
\Phi = \left( \begin{array}{c} \varphi^ {T} (n) \\ \vdots \\ \varphi^ {T} (t - 1) \end{array} \right)
$$

If we use the statistical interpretation of the least-squares estimate given by Theorem 2.2, it follows that the method described will work well when the disturbances can be described as white noise added to the right-hand side of Eq. (2.34). This leads to the least-squares model

$$A (q) y (t) = B (q) u (t) + e (t + n)$$

(Compare with Eq. (2.12).) The method is therefore called an equation error method. A slight variation of the method is better if the disturbances are described instead as white noise added to the system output, that is, when the model is

$$y (t) = \frac {B (q)}{A (q)} u (t) + e (t)$$
