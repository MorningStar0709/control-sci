in which, for each $i , x ( i ) : = \bar { \phi } ( i ; x , { \bf u } )$ is the solution of (3.49) at time i if the initial state is x and the control input sequence is u; $z ^ { * } ( i ; z )$ and $\nu ^ { * } ( i ; z )$ are defined in (3.48). For the purpose of analysis it is convenient to suppose that the entire infinite sequences ${ \bf z } ^ { \ast } \left( z \right)$ and $\mathbf { v } ^ { * } ( z )$ have been precalculated. In practice, apart from initialization, generation of the sequences used in (3.51) require only one solution of $\mathbb { P } _ { N }$ at each iteration. It is not necessary for the cost function $\ell ( \cdot )$ in (3.51) to be the same function as in (3.47) that defines the cost for the nominal controller. Indeed, as we show subsequently, it is not even necessary for the ancillary controller to have the same sample time as the nominal controller. The ancillary control problem is the minimization of $V _ { N } ( x , z , { \bf u } )$ with respect to u subject to merely one state constraint, the terminal equality constraint $x ( N ) = z ^ { * } ( N ; z )$ . The tube-based controller implicitly satisfies the state and input constraints. The terminal constraint is chosen for simplicity to ensure stability. Hence, the ancillary control problem $\mathbb { P } _ { N } ( x , z )$ is defined by

$$V _ {N} ^ {0} (x, z) = \min _ {\mathbf {u}} \left\{V _ {N} (x, z, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x, z) \right\}\mathcal {U} _ {N} (x, z) := \{\mathbf {u} \in \mathbb {U} ^ {N} \mid \bar {\phi} (N; x, \mathbf {u}) = z ^ {*} (N; z) \}$$

in which $\mathcal { U } _ { N } ( x , z )$ is the constraint set. For each $( x , z )$ , the set $\mathcal { U } _ { N } ( x , z )$ is compact. There is no terminal cost and the terminal constraint set is the single state $z ^ { * } ( N ; z ) = \bar { \phi } ( N ; z , \bar { \kappa } _ { N } ( \cdot ) )$ 号

$$\mathbb {X} _ {f} (z) = \{z ^ {*} (N; z) \}$$

For each $z \in \mathcal { Z } _ { N }$ , the domain of the value function $V _ { N } ^ { 0 } ( \cdot , z )$ and of the minimizer is the set $X _ { N } ( z )$ defined by

$$X _ {N} (z) := \{x \in \mathbb {X} \mid \mathcal {U} _ {N} (x, z) \neq \emptyset \}$$

For each $z \in { \mathcal { Z } } _ { N }$ , the set $X _ { N } ( z )$ is bounded. For future reference, let the set $\mathcal { M } _ { N } \subset \mathbb { R } ^ { n } \times \mathbb { R } ^ { n }$ be defined by

$$\mathcal {M} _ {N} := \{(x, z) \mid z \in \mathcal {Z} _ {N}, x \in X _ {N} (z) \}$$
