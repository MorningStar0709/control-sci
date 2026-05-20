# Exercise 6.8: A refinement to the warm start

Consider the following refinement to the warm start in the suboptimal MPC strategy. First add the requirement that the initialization strategy satisfies the following bound

$$\mathbf {h} (x) \leq \bar {d} | x | \quad x \in \mathcal {X} _ {N}$$

in which $\bar { d } > 0$ . Notice that all initializations considered in the chapter satisfy this requirement.

Then, at time k and state x, in addition to the shifted input sequence from time k − 1, u, evaluate the initialization sequence applied to the current state, u = h(x). Select whichever of these two input sequence has lower cost as the warm start for time k. Notice also that this refinement makes the constraint

$$| \mathbf {u} | \leq d | x | \quad x \in r \mathcal {B}$$

redundant, and it can be removed from the MPC optimization.

Prove that this refined suboptimal strategy is exponentially stabilizing on the set $x _ { N }$ . Notice that with this refinement, we do not have to assume that $x _ { N }$ is bounded or that U is bounded.
