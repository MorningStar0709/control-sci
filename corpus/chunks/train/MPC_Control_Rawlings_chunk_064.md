# 1.2.4 Discrete Time Models

Discrete time models are often convenient if the system of interest is sampled at discrete times. If the sampling rate is chosen appropriately, the behavior between the samples can be safely ignored and the model describes exclusively the behavior at the sample times. The finite dimensional, linear, time-invariant, discrete time model is

$$x (k + 1) = A x (k) + B u (k)y (k) = C x (k) + D u (k) \tag {1.3}x (0) = x _ {0}$$

in which $k \in \mathbb { I } _ { \geq 0 }$ is a nonnegative integer denoting the sample number, which is connected to time by $t = k \Delta$ in which $\Delta$ is the sample time. We use I to denote the set of integers and $ { \mathbb { I } } _ { \geq 0 }$ to denote the set of nonnegative integers. The linear discrete time model is a linear difference equation.

It is sometimes convenient to write the time index with a subscript

$$x _ {k + 1} = A x _ {k} + B u _ {k}y _ {k} = C x _ {k} + D u _ {k}x _ {0} \text { given }$$

but we avoid this notation in this text. To reduce the notational complexity we usually express (1.3) as

$$x ^ {+} = A x + B uy = C x + D ux (0) = x _ {0}$$

in which the superscript + means the state at the next sample time. The linear discrete time model is convenient for presenting the ideas and concepts of MPC in the simplest possible mathematical setting. Because the model is linear, analytical solutions are readily derived. The solution to (1.3) is

$$x (k) = A ^ {k} x _ {0} + \sum_ {j = 0} ^ {k - 1} A ^ {k - j - 1} B u (j) \tag {1.4}$$

Notice that a convolution sum corresponds to the convolution integral of (1.2) and powers of A correspond to the matrix exponential. Because (1.4) involves only multiplication and addition, it is convenient to program for computation.

The discrete time analog of the continuous time input-output model is obtained by defining the Z-transform of the signals

$$\overline {{{y}}} (z) := \sum_ {k = 0} ^ {\infty} z ^ {k} y (k)$$

The discrete transfer function matrix G(z) then represents the discrete input-output model

$$\overline {{{y}}} (z) = G (z) \overline {{{u}}} (z)$$

and $G ( z ) \in \mathbb { C } ^ { p \times m }$ is the transfer function matrix. Notice the state does not appear in this input-output description. We make only passing reference to transfer function models in this text.
