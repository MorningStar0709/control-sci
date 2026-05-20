# Solution:

Let’s consider the simplified notation $y ( x ) = y$ and $y ^ { \prime } ( x ) = y ^ { \prime }$ for convenience.

Thus, we can consider the first-order necessary condition for integral constrained optimality:

$$\left(L _ {y} - \frac {d}{d x} L _ {y ^ {\prime}}\right) + \lambda \left(M _ {y} - \frac {d}{d x} M _ {y ^ {\prime}}\right) = 0, \quad \forall x \in [ a, b ] \tag {128}$$

where $\begin{array} { r } { L = \frac { 1 } { 2 } y ^ { \prime 2 } } \end{array}$ and $M = y$ . Substituting, we obtain:

$$\frac {d}{d x} y ^ {\prime} + \lambda \cdot 1 = 0 \tag {129}y ^ {\prime \prime} = - \lambda \tag {130}$$

Integrating twice, we get: (131)

$$y ^ {\prime} = - \lambda x + c _ {1} \tag {132}y = \frac {- \lambda x ^ {2}}{2} + c _ {1} x + c _ {2} \tag {133}$$

(134)

The optimal curve $y ^ { * } ( x )$ is:

$$y ^ {*} (x) = \frac {- \lambda x ^ {2}}{2} + c _ {1} x + c _ {2} \tag {135}$$

Now, we can find the value of λ given the integral constraint. So:

$$\int_ {0} ^ {1} \frac {- \lambda x ^ {2}}{2} + c _ {1} x + c _ {2} d x = \frac {1}{6} \tag {136}\left. \frac {- \lambda x ^ {3}}{6} + \frac {c _ {1} x ^ {2}}{2} + c _ {2} x \right| _ {0} ^ {1} = \frac {1}{6} \tag {137}\frac {- \lambda}{6} + \frac {c _ {1}}{2} + c _ {2} = \frac {1}{6} \tag {138}\lambda = 3 c _ {1} + 6 c _ {2} - 1 \tag {139}$$

So the optimal solution is:

$$y ^ {(} x) = - \frac {3 c _ {1} + 6 c _ {2} - 1}{2} x ^ {2} + c _ {1} x + c _ {2} \tag {140}$$

Given the boundary conditions, we could also easily calculate the values of $c _ { 1 }$ and $c _ { 2 }$ . 
