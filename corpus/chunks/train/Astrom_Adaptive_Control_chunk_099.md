# EXAMPLE 2.3 Nonlinear system

Consider the model

$$y (t) + a y (t - 1) = b _ {1} u (t - 1) + b _ {2} \sin (u (t - 1))$$

By introducing

$$
\theta = \left( \begin{array}{c c c} a & b _ {1} & b _ {2} \end{array} \right) ^ {T}
$$

and

$$
\varphi^ {T} (t) = \left( \begin{array}{l l l} - y (t) & u (t) & \sin (u (t - 1)) \end{array} \right)
$$

the model can be written as

$$y (t) = \varphi^ {T} (t - 1) \theta$$

The model is linear in the parameters, and the least-squares method can be used to estimate $\theta$ .
