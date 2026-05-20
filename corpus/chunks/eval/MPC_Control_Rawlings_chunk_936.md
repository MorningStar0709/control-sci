We would like to be sure that the controlled system is “stable”, i.e., that small perturbations of the initial state do not cause large variations in the subsequent behavior of the system, and that the state converges to a desired state or, if this is impossible due to disturbances, to a desired set of states. These objectives are made precise in Lyapunov stability theory; in this theory, the system $x ^ { + } = f ( x )$ is assumed given and conditions ensuring the stability, or asymptotic stability of a specified state or set are sought; the terms stability and asymptotic stability are defined below. If convergence to a specified state, $x ^ { * }$ say, is sought, it is desirable for this state to be an equilibrium point:

Definition B.1 (Equilibrium point). A point $x ^ { * }$ is an equilibrium point of $x ^ { + } = f ( x )$ if $x ( 0 ) = x ^ { * }$ implies $x ( k ) = \phi ( k ; x ^ { * } ) = x ^ { * }$ for all $k \geq 0$ . Hence $x ^ { * }$ is an equilibrium point if it satisfies

$$x ^ {*} = f (x ^ {*})$$

An equilibrium point $x ^ { * }$ is isolated if there are no other equilibrium points in a sufficiently small neighborhood of $x ^ { * }$ . A linear system $x ^ { + } = A x + b$ has a single equilibrium point $x ^ { * } = ( I - A ) ^ { - 1 } b { \mathrm { ~ i f ~ } } I - A$ is invertible; if not, the linear system has a continuum $\{ x \mid ( I - A x ) = b \}$ of equilibrium points. A nonlinear system, unlike a linear system, may have several isolated equilibrium points.

In other situations, for example when studying the stability properties of an oscillator, convergence to a specified closed set $\mathcal { A } \subset \mathbb { R } ^ { n }$ is sought. In the case of a linear oscillator with state dimension 2, this set is an ellipse. If convergence to a set A is sought, it is desirable for the set A to be positive invariant:

Definition B.2 (Positive invariant set). A set A is positive invariant for the system $x ^ { + } = f ( x ) { \mathrm { ~ i f ~ } } x \in { \mathcal { A } }$ implies $f ( x ) \in { \mathcal { A } }$ .
