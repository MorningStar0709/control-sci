In particular, $u ^ { 0 } ( i ; ( x , i ) ) \ : = \ : u ^ { 0 } ( 0 ; ( x , 0 ) )$ , i.e., the control $u ^ { 0 } ( i ; ( x , i ) )$ applied to the plant is equal to $u ^ { 0 } ( 0 ; ( x , 0 ) )$ , the first element in the sequence $\mathbf { u } ^ { 0 } ( x , 0 )$ . Hence we may as well merely consider problem $\mathbb { P } _ { N } ( x , 0 )$ which, since the initial time is irrelevant, we call $\mathbb { P } _ { N } ( x )$ . Similarly, for simplicity in notation, we replace $\mathbf { u } ^ { 0 } ( x , 0 )$ and $\mathbf { x } ^ { 0 } ( x , 0 )$ by, respectively, $\mathbf { u } ^ { 0 } ( x )$ and $\mathbf { x } ^ { 0 } ( x )$ .

The optimal control problem $\mathbb { P } _ { N } ( x )$ may then be expressed as minimization of

$$\sum_ {k = 0} ^ {N - 1} \ell (x (k), u (k)) + V _ {f} (x (N))$$

with respect to the decision variables (x, u) subject to the constraints that the state and control sequences x and u satisfy the difference equation (2.1), the initial condition $x ( 0 ) ~ = ~ x$ , and the state and control constraints (2.2). Here u denotes the control sequence $\{ u ( 0 ) , u ( 1 ) , \ldots ,$ $u ( N - 1 ) \}$ and x the state sequence $\{ x ( 0 ) , x ( 1 ) , \ldots , x ( N ) \}$ . Retaining the state sequence in the set of decision variables is discussed in Chapter 6. For the purpose of analysis, however, it is preferable to constrain the state sequence x a priori to be a solution of $x ^ { + } = f ( x , u )$ enabling us to express the problem in the equivalent form of minimizing, with respect to the decision variable u, a cost that is purely a function of the initial state x and the control sequence u. This formulation is possible since the state sequence x may be expressed, via the difference equation $x ^ { + } = f ( x , u )$ , as a function of (x, u). The cost becomes $V _ { N } ( x , { \bf u } )$ defined by

$$V _ {N} (x, \mathbf {u}) := \sum_ {k = 0} ^ {N - 1} \ell (x (k), u (k)) + V _ {f} (x (N)) \tag {2.4}$$

where, now, $x ( k ) : = \phi ( k ; x , { \bf u } )$ for all $k \in \mathbb { I } _ { 0 : N }$ . Similarly the constraints (2.2), together with an additional terminal constraint

$$x (N) \in \mathbb {X} _ {f}$$

where $\mathbb { X } _ { f } \subseteq \mathbb { X }$ , impose an implicit constraint on the control sequence of the form

$$\mathbf {u} \in \mathcal {U} _ {N} (x) \tag {2.5}$$

in which the control constraint set $\mathcal { U } _ { N } ( x )$ is the set of control sequences $\mathbf { u } : = \{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ satisfying the state and control constraints. It is therefore defined by

$$\mathcal {U} _ {N} (x) := \{\mathbf {u} \mid (x, \mathbf {u}) \in \mathbb {Z} _ {N} \} \tag {2.6}$$
