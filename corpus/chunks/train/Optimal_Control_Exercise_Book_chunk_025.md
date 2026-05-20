# Solution:

Let’s consider the following function:

$$f (x _ {1}, x _ {2}) = 4 2 (x _ {1} + x _ {2}) \tag {39}$$

given the following

$$h _ {1} (x _ {1}, x _ {2}) = (x _ {1} - 1) ^ {2} + x _ {2} ^ {2} = 1 \tag {40}h _ {2} \left(x _ {1}, x _ {2}\right) = \left(x _ {2} - 2\right) ^ {2} + x _ {2} ^ {2} = 4 \tag {41}$$

The problem only has one feasible point $( x _ { 1 } , x _ { 2 } ) = ( 0 , 0 )$ . The function f is then minimized at this feasible point, thus leading to $x ^ { * } = ( x _ { 1 } ^ { * } , x _ { 2 } ^ { * } ) = ( 0 , 0 )$ . We have:

$$
\nabla f (x ^ {*}) = \left[ \begin{array}{c} 4 2 \\ 4 2 \end{array} \right], \nabla h _ {1} (x ^ {*}) = \left[ \begin{array}{c} - 2 \\ 0 \end{array} \right], \nabla h _ {2} (x ^ {*}) = \left[ \begin{array}{c} - 4 \\ 0 \end{array} \right] \tag {43}
$$

We notice that:

$$\nabla h _ {2} (x ^ {*}) = 2 \nabla h _ {1} (x ^ {*}) \tag {44}$$

which implies they are linearly dependent. Therefore the point $x ^ { * } = ( x _ { 1 } ^ { * } , x _ { 2 } ^ { * } ) = ( 0 , 0 )$ is by definition not a regular point.

The first-order necessary condition for constrained optimality is true if there exist real numbers $\lambda _ { 1 } ^ { * } , \lambda _ { 2 } ^ { * }$ such that:

$$\nabla f (x ^ {*}) + \lambda_ {1} ^ {*} \nabla h _ {1} (x ^ {*}) + \lambda_ {2} ^ {*} \nabla h _ {2} (x ^ {*}) = 0 \tag {45}$$

which leads to

$$
\left[ \begin{array}{l} 4 2 \\ 4 2 \end{array} \right] + \lambda_ {1} ^ {*} \left[ \begin{array}{c} - 2 \\ 0 \end{array} \right] + \lambda_ {2} ^ {*} \left[ \begin{array}{c} - 4 \\ 0 \end{array} \right] = 0 \tag {46}
$$

However, there exist no such $\lambda _ { 1 } ^ { * } , \lambda _ { 2 } ^ { * }$ that can cancel out the second element of $\nabla f ( x ^ { * } )$ ; this is due to the linearly dependent $\nabla h _ { 1 } ( x ^ { * } )$ and $\nabla h _ { 2 } ( x ^ { * } )$ . Therefore, we have shown the necessary condition is false.

![](image/7b6f224323f3ebde3c0162088d7f02a0d4b666adcba6d68ebb95ad3ef5180851.jpg)
