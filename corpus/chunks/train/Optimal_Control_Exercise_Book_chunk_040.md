# Solution:

Let’s consider the simplified notation $y ( x ) = y$ and $y ^ { \prime } ( x ) = y ^ { \prime }$ for convenience. The first step is to calculate the Lagrangian of the function, which is given by:

$$L (x, y, y ^ {\prime}) = \left(y ^ {\prime}\right) ^ {2} + 2 y e ^ {x} \tag {76}$$

Then, we calculate the derivatives of the Lagrangian as:

$$L _ {y} = \frac {\partial}{\partial y} L (x, y, y ^ {\prime}) = 2 e ^ {x} \tag {77}L _ {y ^ {\prime}} = \frac {\partial}{\partial y ^ {\prime}} L (x, y, y ^ {\prime}) = 2 y ^ {\prime} \tag {78}$$

The Euler-Lagrange equation becomes:

$$2 e ^ {x} = \frac {d}{d x} 2 y ^ {\prime} \tag {79}$$

Which yields:

$$e ^ {x} = \frac {d}{d x} y ^ {\prime} \tag {80}e ^ {x} = y ^ {\prime \prime} \tag {81}\int e ^ {x} d x = \int y ^ {\prime \prime} d x \tag {82}\int \left(e ^ {x} + c _ {0}\right) d x = \int y ^ {\prime} d x \tag {83}e ^ {x} + c _ {0} x + c _ {1} = y \tag {84}$$

Applying the boundary conditions $\mathrm { y } ( 0 ) = 0$ and $\mathrm { y } ( 1 ) = 1$ yields:

$$1 + c _ {1} = 0 \tag {85}e + c _ {0} - 1 = 0 \tag {86}$$

by which we obtain $c _ { 0 } = 1 - e$ and $c _ { 1 } = - 1$ . So, the extremal for the problem is:

$$y (x) = e ^ {x} + (1 - e) x - 1 \tag {88}$$


