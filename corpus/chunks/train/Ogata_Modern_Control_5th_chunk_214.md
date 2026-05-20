Taking Laplace transforms of the state-space equations, we obtain

$$s \mathbf {X} (s) - \mathbf {x} (0) = \mathbf {A X} (s) + \mathbf {B U} (s) \tag {5-37}\mathbf {Y} (s) = \mathbf {C X} (s) + \mathbf {D U} (s) \tag {5-38}$$

In deriving the transfer matrix, we assume that $\mathbf { x } ( 0 ) = \mathbf { 0 } { \mathrm { . } }$ Then, from Equation (5–37), we get.

$$\mathbf {X} (s) = (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B U} (s) \tag {5-39}$$

Substituting Equation (5–39) into Equation (5–38), we obtain

$$\mathbf {Y} (s) = \left[ \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D} \right] \mathbf {U} (s)$$

Thus the transfer matrix G(s) is given by

$$\mathbf {G} (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D}$$

The transfer matrix G(s) for the given system becomes

$$
\begin{array}{l} \mathbf {G} (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} \\ = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c c} s + 1 & 1 \\ - 6. 5 & s \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] \\ = \frac {1}{s ^ {2} + s + 6 . 5} \left[ \begin{array}{c c} s & - 1 \\ 6. 5 & s + 1 \end{array} \right] \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] \\ = \frac {1}{s ^ {2} + s + 6 . 5} \left[ \begin{array}{c c} s - 1 & s \\ s + 7. 5 & 6. 5 \end{array} \right] \\ \end{array}
$$

Hence

$$
\left[ \begin{array}{c} Y _ {1} (s) \\ Y _ {2} (s) \end{array} \right] = \left[ \begin{array}{c c} \frac {s - 1}{s ^ {2} + s + 6 . 5} & \frac {s}{s ^ {2} + s + 6 . 5} \\ \frac {s + 7 . 5}{s ^ {2} + s + 6 . 5} & \frac {6 . 5}{s ^ {2} + s + 6 . 5} \end{array} \right] \left[ \begin{array}{c} U _ {1} (s) \\ U _ {2} (s) \end{array} \right]
$$

Since this system involves two inputs and two outputs, four transfer functions may be defined, depending on which signals are considered as input and output. Note that, when considering the signal $u _ { 1 }$ as the input, we assume that signal $u _ { 2 }$ is zero, and vice versa. The four transfer functions are

$$\frac {Y _ {1} (s)}{U _ {1} (s)} = \frac {s - 1}{s ^ {2} + s + 6 . 5}, \quad \frac {Y _ {1} (s)}{U _ {2} (s)} = \frac {s}{s ^ {2} + s + 6 . 5}\frac {Y _ {2} (s)}{U _ {1} (s)} = \frac {s + 7 . 5}{s ^ {2} + s + 6 . 5}, \quad \frac {Y _ {2} (s)}{U _ {2} (s)} = \frac {6 . 5}{s ^ {2} + s + 6 . 5}$$

Assume that $u _ { 1 }$ and $u _ { 2 }$ are unit-step functions. The four individual step-response curves can then be plotted by use of the command

$$\operatorname{step} (A, B, C, D)$$
