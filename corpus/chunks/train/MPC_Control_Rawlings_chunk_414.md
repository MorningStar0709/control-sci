$$\bar {\mathbb {P}} _ {N} (z): \quad \bar {V} _ {N} ^ {0} (z) = \min _ {\mathbf {v}} \{\bar {V} _ {N} (z, \mathbf {v}) \mid \mathbf {v} \in \mathcal {V} _ {N} (z) \}$$

A solution exists if z is feasible for $\bar { \mathbb P } _ { N } ( z )$ because $\bar { V } _ { N } ( \cdot )$ is continuous and $\gamma _ { N } ( z )$ is compact. Let $\mathcal { Z } _ { N } : = \{ z \mid \mathcal { V } _ { N } ( z ) \neq \emptyset \}$ denote the domain of $\bar { V } _ { N } ^ { 0 } ( z )$ , the set of feasible states for $\bar { \mathbb { P } } _ { N } ( z )$ . By virtue of our assumptions, the set $\mathcal { Z } _ { N }$ is bounded. The solution of $\bar { \mathbb P } _ { N } ( z )$ is the minimizing control sequence

$$\mathbf {v} ^ {0} (z) = \{\nu^ {0} (0; z), \nu^ {0} (1; z), \dots , \nu^ {0} (N - 1; z) \}$$

which we assume is unique, and the associated optimal state sequence is

$$\mathbf {z} ^ {0} (z) = \{z, z ^ {0} (1; z), \dots , z ^ {0} (N; z) \}$$

The first element $\nu ^ { 0 } ( 0 ; z )$ of $\mathbf { v } ^ { 0 } ( z )$ is the control that is applied in MPC. The implicit MPC control law is, therefore, $\bar { \kappa } _ { N } ( \cdot )$ defined by

$$\bar {\kappa} _ {N} (z) := \nu^ {0} (0; z)$$

The nominal system under MPC satisfies

$$z ^ {+} = f (z, \bar {\kappa} _ {N} (z))$$

The central path that defines the ancillary control problem defined in the next subsection consists of the state trajectory

$$\mathbf {z} ^ {*} (z) := \{z ^ {*} (0; z), z ^ {*} (1; z), \dots \}$$

and the control trajectory

$$\mathbf {v} ^ {*} (z) := \{\nu^ {*} (0; z), \nu^ {*} (1; z), \dots \}$$

in which z is the initial state of the nominal system. These trajectories are the solutions of the controlled nominal system described by

$$z ^ {+} = f (z, \bar {\kappa} _ {N} (z))$$

so that for all i

$$z ^ {*} (i; z) = \bar {\phi} (i; z, \bar {\kappa} _ {N}) \quad \nu^ {*} (i; z) = \bar {\kappa} _ {N} \left(z ^ {*} (i; z)\right) \tag {3.48}$$

If the terminal cost function $V _ { f } ( \cdot )$ and terminal constraint set $\mathbb { Z } _ { f }$ are chosen to satisfy the usual stability assumptions, which we assume to be the case, and $\mathcal { Z } _ { N }$ is bounded, there exist $c _ { 1 } > 0$ and $\bar { c } _ { 2 } > c _ { 1 }$ such that

$$\bar {V} _ {N} ^ {0} (z) \geq c _ {1} | z | ^ {2}\bar {V} _ {N} ^ {0} (z) \leq \bar {c} _ {2} | z | ^ {2}\Delta \bar {V} _ {N} ^ {0} (z) \leq - c _ {1} | z | ^ {2}$$

for all $z \in \mathcal { Z } _ { N }$ in which

$$\Delta \bar {V} _ {N} ^ {0} (z) := \bar {V} _ {N} ^ {0} (f (z, \bar {\kappa} _ {N} (z))) - \bar {V} _ {N} ^ {0} (z)$$

It follows that the origin is exponentially stable with a region of attraction ${ \mathcal { Z } } _ { N }$ for the system $z ^ { + } = f ( z , \bar { \kappa } _ { N } ( z ) )$ . The state of the controlled nominal system converges to the origin exponentially fast.
