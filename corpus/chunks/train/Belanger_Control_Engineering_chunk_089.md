To study the motion resulting from the excitation of the mode $\pm j\sqrt{50}$ , consider Equation 3.14, with $\alpha = Ve^{j\phi}$ and with V real and positive. Then,

$$
\mathbf {x} (0) = 2 R e \left\{V e ^ {j \phi} \left[ \begin{array}{c} 1 \\ j \sqrt {5 0} \\ 0 \\ 0 \end{array} \right] \right\} = 2 R e \left\{V (\cos \phi + j \sin \phi) \left[ \begin{array}{c} 1 \\ j \sqrt {5 0} \\ 0 \\ 0 \end{array} \right] \right\}

= 2 V \cos \phi \left[ \begin{array}{l} 1 \\ 0 \\ 0 \\ 0 \end{array} \right] - 2 V \sin \phi \left[ \begin{array}{c} 0 \\ \sqrt {5 0} \\ 0 \\ 0 \end{array} \right] = \left[ \begin{array}{c} 2 V \cos \phi \\ - 2 \sqrt {5 0} V \sin \phi \\ 0 \\ 0 \end{array} \right]
$$

This vector describes an initial state with nonzero vertical position and/or velocity, but zero angular position and velocity. By appropriate choices of V and $\phi$ , the vertical position and velocity can be selected arbitrarily; i.e., $\mathbf{x}(0)$ may be any linear combination of the real and imaginary parts of the eigenvector.

From Equation 3.15, the subsequent motion is

$$
\begin{array}{l} \mathbf {x} (t) = 2 R e \left[ V e ^ {j \phi} e ^ {j \sqrt {5 0} t} \mathbf {v} _ {1} \right] \\ = 2 V \cos (\sqrt {5 0} t + \phi) \left[ \begin{array}{l} 1 \\ 0 \\ 0 \\ 0 \end{array} \right] - 2 V \sin (\sqrt {5 0} t + \phi) \left[ \begin{array}{c} 0 \\ \sqrt {5 0} \\ 0 \\ 0 \end{array} \right] \\ = \left[ \begin{array}{c} 2 V \cos (\sqrt {5 0} t + \phi) \\ - 2 V \sqrt {5 0} \sin (\sqrt {5 0} t + \phi) \\ 0 \\ 0 \end{array} \right] \\ \end{array}
$$

The physical interpretation is this: given an initial state with vertical motion only, the subsequent motion is also purely vertical, and is sinusoidal with a frequency of $\sqrt{50}$ rad/s. Mechanical engineers call this the heave mode.

The modes with frequencies $\pm j\sqrt{150}$ rad/s are analyzed in the same manner. The result is sinusoidal motion at $\sqrt{150}$ rad/s in the last two coordinates, $\theta$ and $\omega$ , with no motion of the center of gravity, provided that the initial state has only angular displacement and velocity. That mode is called the pitch mode.

This example has a simple structure, which we did not exploit. The state equations are seen to be composed of two independent sets of two equations:

$$
\left[ \begin{array}{c} y \\ \dot {v} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 5 0 & 0 \end{array} \right] \left[ \begin{array}{c} y \\ v \end{array} \right]
$$

and
