# System Identification

The least-squares method can be used to identify parameters in dynamic systems. Let the system be described by (13.1) with $C(q) = q^{n}$ . Further, assume that A and B are of order n and n - 1, respectively. Assume that a sequence of inputs $\{u(1), u(2), \ldots, u(N)\}$ has been applied to the system and that the corresponding sequence of outputs $\{y(1), y(2), \ldots, y(N)\}$ has been observed. The unknown parameters are then

$$
\theta = \left( \begin{array}{c c c c c c} a _ {1} & \dots & a _ {n} & b _ {1} & \dots & b _ {n} \end{array} \right) ^ {T} \tag {13.6}
$$

Further, we introduce

$$
\varphi^ {T} (k + 1) = \left( \begin{array}{c c c c c c} - y (k) & \dots & - y (k - n + 1) & u (k) & \dots & u (k - n + 1) \end{array} \right) \tag {13.7}
$$

and

$$
\Phi = \left( \begin{array}{c} \varphi^ {T} (n + 1) \\ \vdots \\ \varphi^ {T} (N) \end{array} \right)
$$

The least-squares estimate is then given by (13.5) if $\Phi^{T}\Phi$ is nonsingular. For instance, this is the case if the input signal is, loosely speaking, sufficiently rich.
