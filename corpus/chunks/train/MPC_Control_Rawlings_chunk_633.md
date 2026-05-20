# 5.6.4 Tube-Based Output MPC

We apply the methodology of Chapter 3, Section 3.6 to the control of the uncertain system $\hat { x } ^ { + } = f ( \hat { x } , u ) + \delta , \delta \in \Delta$ , making allowance for the fact that $x ( i )$ lies in $\{ \hat { x } ( i ) \} \oplus \mathbb { \Sigma } _ { x }$ for all i. This method of control permits, in principle, larger disturbances.

We assume, therefore, that we have an implicit, stabilizing, control law $\nu = \bar { \kappa } _ { N } ( z )$ for the nominal system $z ^ { + } = f ( z , \nu )$ . This control law is chosen to satisfy the tightened constraints

$$z \in \mathbb {Z} \quad v \in \mathbb {V}$$

We discuss the choice of Z and V later. The control law is obtained by solving the nominal control problem $\bar { \mathbb { P } } _ { N } ( z )$ whose solution also yields the “central” state and control trajectories $\{ \mathbf { z } ^ { * } ( i ; z ) \}$ and $\{ \mathbf { u } ^ { * } ( i ; z ) \}$ ; these trajectories are the solutions of

$$z ^ {+} = f (z, \bar {\kappa} _ {N} (z)), \quad \nu = \bar {\kappa} _ {N} (z)$$

with initial state $z ( 0 ) = z$

The second ingredient of the tube-based controller is the ancillary controller that attempts to steer the trajectories of the uncertain system $\hat { x } ^ { + } = f ( \hat { x } , u ) + \delta$ toward the central path defined above. This determines u by solving the ancillary problem $\mathbb { P } _ { N } ( \hat { x } , z )$ defined by

$$\bar {V} _ {N} ^ {0} (\hat {x}, z) = \min _ {\mathbf {u}} \{V _ {N} (\hat {x}, z, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (\hat {x}, z) \}$$

in which the cost function $\bar { V } _ { N } ^ { 0 } ( \cdot )$ is defined, as in Chapter 3, by

$$V _ {N} (\hat {x}, z, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (\hat {x} (i) - z ^ {*} (i; z), u (i) - v ^ {*} (i; z))$$

where $\hat { x } ( i ) : = \bar { \phi } ( i ; \hat { x } , { \bf u } )$ , the solution at time i of the nominal system $z ^ { + } = f ( z , u )$ with initial state $\hat { x }$ and control sequence u; $z ^ { \ast } ( i ; z ) : =$ $\bar { \phi } ( i ; z , \bar { \kappa } _ { N } ( \cdot ) )$ , the solution at time i of the controlled nominal system $z ^ { + } = f ( z , \bar { \kappa } _ { N } ( z ) )$ MPC with initial state z, and $\nu ^ { * } ( i ; z ) = \bar { \kappa } _ { N } ( z ^ { * } ( i ; z ) )$ . The constraint set $\mathcal { U } _ { N } ( \hat { x } , z )$ is defined by

$$\mathcal {U} _ {N} (\hat {x}, z) := \{\mathbf {u} \in \mathbb {R} ^ {N m} \mid \bar {\phi} (N; \hat {x}, \mathbf {u}) = z ^ {*} (N; z) \}$$
