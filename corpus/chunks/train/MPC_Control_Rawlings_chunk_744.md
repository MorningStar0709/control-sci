# Exercise 6.22: Norm constraints as linear inequalities

Consider the quadratic program (QP) in decision variable u with parameter x

$$\min _ {u} (1 / 2) u ^ {\prime} H u + x ^ {\prime} D u\text { s.t. } E u \leq F x$$

in which $u \in \mathbb { R } ^ { m } , x \in \mathbb { R } ^ { n }$ , and $H > 0$ . The parameter x appears linearly (affinely) in the cost function and constraints. Assume that we wish to add a norm constraint of the following form

$$\left| u \right| _ {\alpha} \leq c \left| x \right| _ {\alpha} \quad \alpha = 2, \infty$$

(a) If we use the infinity norm, show that this problem can be posed as an equivalent QP with additional decision variables, and the cost function and constraints remain linear (affine) in parameter x. How many decision variables and constraints are added to the problem?

(b) If we use the two norm, show that this problem can be approximated by a QP whose solution does satisfy the constraints, but the solution may be suboptimal compared to the original problem.
