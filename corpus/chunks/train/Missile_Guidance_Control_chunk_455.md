where ${ \bf x } ( t )$ is the n-dimensional state vector that represents components of position, velocity, and any other modeling parameters, while u(t) is the r-dimensional plant control input vector. $A ( t )$ and $B ( t )$ are $n \times n$ and $n \times r$ matrices, respectively. The optimal linear regulator problem for a linear dynamic system entails the determination of the optimal control u(t ), $t \in [ t _ { 0 } , T ]$ , that minimizes the quadratic performance index [2]

$$J \left(\mathbf {x} _ {0}, t _ {0}, T, \mathbf {u} (t)\right) = \frac {1}{2} \left[ \mathbf {x} ^ {T} (T) S \mathbf {x} (T) \right] + \frac {1}{2} \int_ {t _ {0}} ^ {T} \left[ \mathbf {x} ^ {T} (t) Q (t) \mathbf {x} (t) + \mathbf {u} ^ {T} (t) R (t) \mathbf {u} (t) \right] d t, \tag {5.53}$$

where the superscript T denotes vector or matrix transpose, S and $Q ( t )$ are real symmetric positive semidefinite (i.e., nonzero) $n \times n$ matrices, $R ( t )$ is a real symmetric positive definite $r \times r$ matrix, and T is the terminal time, which may be either fixed a priori or unspecified $( T > t _ { 0 } )$ . The weighting matrices $R ( t )$ and $Q ( t )$ are selected by the control system designer to place bounds on the trajectory and control, respectively, while S and the terminal penalty cost $\mathbf { x } ^ { T } ( T ) S \mathbf { x } ( T )$ are included in order to ensure that x(t) stays close to zero near the terminal time. The term $\mathbf { x } ^ { T } ( t ) Q ( t ) \mathbf { x } ( t )$ is chosen to penalize deviations of the regulated state x(t) from the desired equilibrium condition $\mathbf { x } ( t ) = 0$ , while the term ${ \mathbf { u } } ^ { T } ( t ) R ( t ) { \mathbf { u } } ( t )$ discourages the use of excessively large control effort. For example, if in (5.53) $R ( t ) = 0$ , we do not penalize the system for its control-energy expenditure. The optimal control in this case will try to bring the state to zero as fast as possible. With the aid of the minimum (or maximum) principle, the optimal control function that minimizes (5.53) is given by [8]

$$\mathbf {u} (t) = - R ^ {- 1} B ^ {T} S \mathbf {x} (t), \tag {5.54}$$

where S satisfies the time-varying matrix Riccati equation

$$\frac {d S}{d t} = - S A - A ^ {T} S + S B R ^ {- 1} S - Q. \tag {5.55}$$

A possible control law for the linear quadratic regulator problem may be expressed as follows:

$$\mathbf {u} (t) = \mathbf {u} _ {n} (t) - R ^ {- 1} (t) B ^ {T} (t) S (t) [ \mathbf {x} (t) - \mathbf {x} _ {n} (t) ], \tag {5.56}$$

where
