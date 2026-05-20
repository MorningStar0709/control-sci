# 3.2.4 Input-to-State Stability

When an uncertain system is nominally asymptotically stable, it is sometimes possible to establish input-to-state stability (ISS) as shown in Section B.6 in Appendix B. We consider the uncertain system described by

$$x ^ {+} = f (x, u, w) \tag {3.7}$$

in which w is a bounded additive disturbance. The constraints that are required to be satisfied are

$$x (i) \in \mathbb {X} \qquad u (i) \in \mathbb {U}$$

for all $i \in \mathbb { I } _ { \geq 0 } : = \{ 0 , 1 , 2 , . . . \}$ , the set of nonnegative integers. The disturbance w may take any value in the set W. As before, u denotes the control sequence $\{ u ( 0 ) , u ( 1 ) , \ldots \}$ and w the disturbance sequence $\{ w ( 0 ) , w ( 1 ) , . . . \} ; \phi ( i ; x , { \bf u } , { \bf w } )$ denotes the solution of (3.7) at time i if the initial state is x, and the control and disturbance sequences are, respectively, u and w.

The nominal system is described by

$$x ^ {+} = \bar {f} (x, u) := f (x, u, 0) \tag {3.8}$$

and $\bar { \phi } ( i ; x , { \bf { u } } )$ denotes the solution of the nominal system (3.8) at time i if the initial state is x and the control sequence is u. The nominal control problem, defined subsequently, includes, for reasons discussed in Chapter 2, a terminal constraint

$$x (N) \in \mathbb {X} _ {f}$$

The nominal optimal control problem is

$$\mathbb {P} _ {N} (x): \quad V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x) \right\}\mathbf {u} ^ {0} (x) = \arg \min _ {\mathbf {u}} \left\{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x) \right\}$$

in which $\mathbf { u } ^ { 0 } ( x ) \ = \ \{ u _ { 0 } ^ { 0 } ( x ) , u _ { 1 } ^ { 0 } ( x ) , \ldots , u _ { N - 1 } ^ { 0 } ( x ) \}$ } and the nominal cost $V _ { N } ( \cdot )$ is defined by

$$V _ {N} (x, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N)) \tag {3.9}$$

In (3.9) and (3.10), $x ( i ) : = \bar { \phi } ( i ; x , { \bf u } )$ for all $i \in \mathbb { I } _ { 0 : N - 1 } = \{ 0 , 1 , 2 , \dots , N -$ 1}; the set of admissible control sequences $\mathcal { U } _ { N } ( x )$ is defined by

$$\mathcal {U} _ {N} (x) := \{\mathbf {u} \mid u (i) \in \mathbb {U}, \quad x (i) \in \mathbb {X} \forall i \in \mathbb {I} _ {0: N - 1}, \quad x (N) \in \mathbb {X} _ {f} \} \tag {3.10}$$
