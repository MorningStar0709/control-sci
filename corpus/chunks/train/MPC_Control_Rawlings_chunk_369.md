# 3.3.2 Preliminary Results

As in conventional MPC, the value function and implicit control law may, in principle, be obtained by DP. But DP is, in most cases, impossible to use because of its large computational demands. There are, of course, important exceptions such as $H _ { 2 }$ and $H _ { \infty }$ optimal control for unconstrained linear systems with quadratic cost functions. DP also can be used for low dimensional constrained optimal control problems when the system is linear, the constraints are affine, and the cost is affine or quadratic. Even when DP is computationally prohibitive, however, it remains a useful tool because of the insight it provides. Because of the cost definition, min-max DP is required. For each $i \in \{ 0 , 1 , \ldots , N \}$ , let $V _ { i } ^ { 0 } ( \cdot )$ and $\kappa _ { i } ( \cdot )$ denote, respectively, the partial value function and the optimal solution to the optimal control problem $\mathbb { P } _ { i }$ defined by (3.19) with i replacing N. The DP recursion equations for computing these functions are

$$V _ {i} ^ {0} (x) = \min _ {u \in \mathbb {U}} \max _ {w \in \mathbb {W}} \{\ell (x, u, w) + V _ {i - 1} ^ {0} (f (x, u, w)) \mid f (x, u, \mathbb {W}) \subseteq \mathcal {X} _ {i - 1} \}\kappa_ {i} (x) = (\arg \min _ {u \in \mathbb {U}}) \max _ {w \in \mathbb {W}} \{\ell (x, u, w) + V _ {i - 1} ^ {0} (f (x, u)) \mid f (x, u, \mathbb {W}) \subseteq \mathcal {X} _ {i - 1} \}\mathcal {X} _ {i} = \{x \in \mathbb {X} \mid \exists u \in \mathbb {U} \text { such that } f (x, u, \mathbb {W}) \subseteq \mathcal {X} _ {i - 1} \}$$

with boundary conditions

$$V _ {0} ^ {0} (x) = V _ {f} (x) \qquad \mathcal {X} _ {0} = \mathbb {X} _ {f}$$

In these equations, the subscript i denotes the time to go. For each i, $x _ { i }$ is the domain of $V _ { i } ^ { 0 } ( \cdot )$ (and $\kappa _ { i } ( \cdot ) )$ and is therefore the set of states x for which a solution to problem $\mathbb { P } _ { i } ( x )$ exists. Thus $x _ { i }$ is the set of states that can be robustly steered by state feedback, i.e., by a policy $\pmb { \mu } \in \mathcal { M } ( x )$ , to $\mathbb { X } _ { f }$ in i steps or less satisfying all constraints for all disturbance sequences. It follows from these definitions that

$$V _ {i} ^ {0} (x) = \max _ {w \in \mathbb {W}} \{\ell (x, \kappa_ {i} (x), w) + V _ {i - 1} ^ {0} (f (x, \kappa_ {i} (x), w)) \} \tag {3.20}$$

as discussed in Exercise 3.1.
