# 3.4.1 The Matrix Transfer Function

The zero-state response is best studied by means of the Laplace transform. The system is represented by

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}\mathbf {y} = C \mathbf {x} + D \mathbf {u}. \tag {3.16}$$

Taking transforms of the state equation [and remembering that $\mathbf{x}(0) = 0$ ],

$$s \mathbf {x} (s) = A \mathbf {x} (s) + B \mathbf {u} (s)\mathbf {x} (s) = (s I - A) ^ {- 1} B \mathbf {u} (s). \tag {3.17}$$

Use of the output equation yields

$$\mathbf {y} (s) = [ C (s I - A) ^ {- 1} B + D ] \mathbf {u} (s). \tag {3.18}$$

The matrix

$$H (s) = C (s I - A) ^ {- 1} B + D \tag {3.19}$$

has $m$ rows (the number of outputs) and $r$ columns (the number of inputs). It is the matrix transfer function. For a single-input, single-output (SISO) system, $m = r = 1$ and $H(s)$ is just a scalar valued function.

A time-domain expression is obtained by writing Equation 3.18 as

$$\mathbf {y} (s) = C \mathcal {L} [ e ^ {A t} ] B \mathbf {u} (s) + D \mathbf {u} (s).$$

By the real convolution theorem, a product of transforms goes into the time domain as a convolution integral, so that

$$\mathbf {y} (t) = \int_ {0} ^ {t} C e ^ {A (t - \tau)} B \mathbf {u} (\tau) d \tau + D \mathbf {u} (t). \tag {3.20}$$
