# Solution:

Let’s consider the simplified notation $y ( x ) = y$ and $y ^ { \prime } ( x ) = y ^ { \prime }$ for convenience.

The first step is to calculate the Lagrangian of the function, which is given by:

$$L (x, y, y ^ {\prime}) = y ^ {2} y ^ {\prime 2} \tag {69}$$

The derivatives of the Lagrangian are given by

$$L _ {y} = 2 y y ^ {\prime 2} \tag {70}L _ {y} ^ {\prime} = 2 y ^ {2} y ^ {\prime} \tag {71}$$

The Euler-Lagrange equation yields the following differential equation:

$$y y ^ {\prime 2} = \frac {d}{d x} y ^ {2} y ^ {\prime} \tag {72}$$

whose solutions are of the form $y ( x ) = c _ { 2 } { \sqrt { c _ { 1 } + 2 x } }$ . Given the boundary conditions, we can get:

$$
\left\{ \begin{array}{l} y (0) = 0 \\ y (1) = 1 \end{array} \Longrightarrow \left\{ \begin{array}{l} c _ {2} \sqrt {c _ {1}} = 0 \\ c _ {2} \sqrt {c _ {1} + 2} = 1 \end{array} \Longrightarrow \left\{ \begin{array}{l} c _ {1} = 0 \\ c _ {2} = \frac {1}{\sqrt {2}} \end{array} \right. \right. \right. \tag {73}
$$

therefore, an extremal for the problem will be:

$$y (x) = 2 \sqrt {x} \tag {74}$$

![](image/faff9d9b1249774e2928365f25302d63a704071637f8df20a75b44e8735623ea.jpg)
