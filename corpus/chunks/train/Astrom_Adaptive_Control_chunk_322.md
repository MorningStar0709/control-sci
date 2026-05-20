# EXAMPLE 5.11 Static nonlinear systems

Consider a static nonlinear system characterized by the function $f: R \to R$ . We have

$$\langle y \mid u \rangle = \int_ {0} ^ {\infty} f (u (t)) u (t) d t$$

The right-hand side is thus nonnegative if

$$x f (x) \geq 0 \tag {5.44}$$

which is the condition for passivity. This condition means that the graph of the curve $f$ is entirely in the first and the third quadrants. The system is input strictly passive if

$$x f (x) \geq \delta | x | ^ {2}$$

It is output strictly passive if

$$x f (x) \geq \delta f ^ {2} (x)$$

A static system with $f(x) = x + x^{3}$ is thus input strictly passive, and a static system with $f(x) = x/(1 + |x|)$ is output strictly passive. □
