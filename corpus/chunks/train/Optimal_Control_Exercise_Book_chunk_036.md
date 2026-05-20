# Solution:

Let’s take as an example of variational problem the shortest path in the plane connecting two different points A and B. By intuition, we know that the solution of this problem will be a straight line connecting the two points; however, we can prove it by considering the problem as a variational problem.

Let’s consider the following Cartesian coordinates: $A = ( x _ { 0 } , y _ { 0 } )$ and $B = ( x _ { 1 } , y _ { 1 } )$ with $x _ { 0 } < x _ { 1 }$ , and the function $y ( x ) \in \mathcal { C } ^ { 2 }$ is the function describing the coordinate y with respect to x. Moreover, $x _ { 0 } \leq x \leq x _ { 1 }$ . Therefore, we want to minimize the following cost functional:

$$L = \int_ {A} ^ {B} d s = \int_ {x _ {o}} ^ {x _ {1}} \sqrt {d x ^ {2} + d y ^ {2}} \tag {65}$$

Considering $d y = y ^ { \prime } ( x ) d x$ yields to:

$$\min _ {y: \left[ x _ {0}, x _ {1} \right]\rightarrow \left[ y _ {0}, y _ {1} \right]} \int_ {x _ {0}} ^ {x _ {1}} \sqrt {1 + y ^ {\prime} (x) ^ {2}} d x \tag {66}$$

subject to

$$y (x _ {0}) = y _ {0}, \quad y (x _ {1}) = y _ {1} \tag {67}$$

![](image/3f582ee7cb376c12b6bbbc94c6344d40e081a44fe77196be38d42f4081d1eea0.jpg)
