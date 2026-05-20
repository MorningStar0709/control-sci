# Exercise 1.26: Existence, uniqueness and stability with the cross term

Consider the linear quadratic problem with system

$$x ^ {+} = A x + B u \tag {1.59}$$

and infinite horizon cost function

$$V (x (0), \mathbf {u}) = (1 / 2) \sum_ {k = 0} ^ {\infty} x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k)$$

The existence, uniqueness and stability conditions for this problem are: (A, B) stabilizable, $Q \geq 0 , ( A , Q )$ detectable, and $R > 0$ . Consider the modified objective function with the cross term

$$V = (1 / 2) \sum_ {k = 0} ^ {\infty} x (k) ^ {\prime} Q x (k) + u (k) ^ {\prime} R u (k) + 2 x (k) ^ {\prime} M u (k) \tag {1.60}$$

(a) Consider reparameterizing the input as

$$\nu (k) = u (k) + T x (k) \tag {1.61}$$

Choose T such that the cost function in x and v does not have a cross term, and express the existence, uniqueness and stability conditions for the transformed system. Goodwin and Sin (1984, p.251) discuss this procedure in the state estimation problem with nonzero covariance between state and output measurement noises.

(b) Translate and simplify these to obtain the existence, uniqueness and stability conditions for the original system with cross term.
