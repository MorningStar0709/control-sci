Unreachable setpoints, strong duality, and dissipativity. Unreachable setpoints are discussed in Section 2.9.3. It is known that the optimal MPC value function in this case is not decreasing and is therefore not a Lyapunov function for the closedloop system. A recent paper by Diehl, Amrit, and Rawlings (2011) has shown that a modified MPC cost function, termed rotated cost, is a Lyapunov function for the unreachable setpoint case and other more general cost functions required for optimizing process economics. A strong duality condition is shown to be a sufficient condition for asymptotic stability of economic MPC with nonlinear models.

This result is further generalized in the recent paper Angeli, Amrit, and Rawlings (2011). Here a dissipation inequality is shown to be sufficient for asymptotic stability of economic MPC with nonlinear models. This paper also shows that MPC is better than optimal periodic control for systems that are not optimally operated at steady state.

Unbounded input constraint sets. Assumption 2.3 includes the restriction that the input constraint set U is compact (bounded and closed). This basic assumption is used to ensure existence of the solution to the optimal control problem throughout Chapter 2. If one is interested in an MPC theory that handles an unbounded input constraint set U, then one can proceed as follows. First modify Assumption 2.3 by removing the boundedness assumption on U.

Assumption 5 (Properties of constraint sets – unbounded case). The sets $\mathbb { X } , \ \mathbb { X } _ { f }$ , and U are closed, $\mathbb { X } _ { f } \subseteq \mathbb { X } ;$ each set contains the origin.

Then, to ensure existence of the solution to the optimal control problem, consider the cost assumption on page 154 in the section on nonpositive definite stage costs, slightly restated here.

Assumption 6 (Stage cost lower bound). Consider the following two lower bounds for the stage cost.

(a)

$$\ell (y, u) \geq \alpha_ {1} (\mid (y, u) \mid) \quad \text { for all } y \in \mathbb {R} ^ {p}, u \in \mathbb {R} ^ {m}V _ {f} (x) \leq \alpha_ {2} (| x |) \quad \text { for all } x \in \mathbb {X} _ {f}$$

in which $\alpha _ { 1 } ( \cdot )$ is a $\mathcal { K } _ { \infty }$ function.

(b)

$$\ell (y, u) \geq c _ {1} | (y, u) | ^ {a} \quad \text { for all } y \in \mathbb {R} ^ {p}, u \in \mathbb {R} ^ {m}V _ {f} (x) \leq c _ {2} | x | ^ {a} \quad \text { for all } x \in \mathbb {X} _ {f}$$

in which $c _ { 1 } , c _ { 2 } , a > 0$
