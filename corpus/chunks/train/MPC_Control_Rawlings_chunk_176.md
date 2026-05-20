# Exercise 1.51: Alive on arrival

The following two optimization problems are helpful in understanding the arrival cost decomposition in state estimation.

(a) Let $V ( x , y , z )$ be a positive, strictly convex function consisting of the sum of two functions, one of which depends on both x and y, and the other of which depends on y and z

$$V (x, y, z) = g (x, y) + h (y, z) \qquad V: \mathbb {R} ^ {m} \times \mathbb {R} ^ {n} \times \mathbb {R} ^ {p} \to \mathbb {R} _ {\geq 0}$$

Consider the optimization problem

$$P 1: \min _ {x, y, z} V (x, y, z)$$

The arrival cost decomposes this three-variable optimization problem into two, smaller dimensional optimization problems. Define the “arrival cost” $\tilde { g }$ for this problem as the solution to the following single-variable optimization problem

$$\tilde {g} (y) = \min _ {x} g (x, y)$$

and define optimization problem P2 as follows

$$P 2: \min _ {y, z} \tilde {g} (y) + h (y, z)$$

Let $( x ^ { \prime } , y ^ { \prime } , z ^ { \prime } )$ denote the solution to P1 and $( x ^ { 0 } , y ^ { 0 } , z ^ { 0 } )$ denote the solution to $P 2 .$ , in which

$$x ^ {0} = \arg \min _ {x} g (x, y ^ {0})$$

Prove that the two solutions are equal

$$(x ^ {\prime}, y ^ {\prime}, z ^ {\prime}) = (x ^ {0}, y ^ {0}, z ^ {0})$$

(b) Repeat the previous part for the following optimization problems

$$V (x, y, z) = g (x) + h (y, z)$$

Here the y variables do not appear in g but restrict the x variables through a linear constraint. The two optimization problems are:

$$P 1: \min _ {x, y, z} V (x, y, z) \quad \text { subject to } E x = yP 2: \min _ {y, z} \tilde {g} (y) + h (y, z)$$

in which

$$\tilde {g} (y) = \min _ {x} g (x) \quad \text { subject to } E x = y$$
