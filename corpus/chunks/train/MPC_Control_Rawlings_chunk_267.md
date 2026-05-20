# 2.5.3.2 Nonlinear Systems

The system to be controlled is

$$x ^ {+} = f (x, u)$$

in which $f ( \cdot )$ is assumed to be twice continuously differentiable. The system is subject to state and control constraints

$$x \in \mathbb {X} \quad u \in \mathbb {U}$$

in which X is closed and U is compact; each set contains the origin in its interior. The cost function is defined by

$$V _ {N} (x, \mathbf {u}) = \sum_ {i = 0} ^ {N - 1} \ell (x (i), u (i)) + V _ {f} (x (N))$$

in which, for each $i , x ( i ) : = \phi ( i ; x , \mathbf { u } )$ , the solution of $x ^ { + } = f ( x , u )$ at time i if the initial state is x at time 0 and the control is u. The stage cost $\ell ( \cdot )$ is defined by

$$\ell (x, u) := (1 / 2) \left(\left| x \right| _ {Q} ^ {2} + \left| u \right| _ {R} ^ {2}\right)$$

in which Q and R are positive definite. The optimal control problem $\mathbb { P } _ { N } ( x )$ is defined by

$$\mathbb {P} _ {N} (x): \quad V _ {N} ^ {0} (x) = \min _ {\mathbf {u}} \{V _ {N} (x, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x) \}$$

in which $\mathcal { U } _ { N } ( x )$ is defined by (2.6) and includes the terminal constraint $x ( N ) \ = \ \phi ( N ; x , \mathbf { u } ) \in \ \mathbb { X } _ { f }$ (in addition to the state and control constraints). Our first task is to choose the ingredients $V _ { f } ( \cdot )$ and $\mathbb { X } _ { f }$ of the optimal control problem to ensure asymptotic stability of the origin for the controlled system. We proceed as in Section 2.5.1.3, i.e., we linearize the system at the origin to obtain the linear model

$$x ^ {+} = A x + B u$$

in which $A = f _ { x } ( 0 , 0 )$ and $B = f _ { u } ( 0 , 0 )$ and assume, as before, that $( A , B )$ is stabilizable. We choose any controller $u = K x$ such that $A _ { K }$ is stable. Choose $Q ^ { * } : = ( Q + K ^ { \prime } R K )$ and let P be defined by the Lyapunov equation

$$A _ {K} ^ {\prime} P A _ {K} + 2 Q ^ {*} = P$$

The terminal cost function $V _ { f } ( \cdot )$ is again chosen to be

$$V _ {f} (x) := (1 / 2) x ^ {\prime} P x$$

and $\mathbb { X } _ { f }$ is chosen to be a sublevel set $W ( a ) : = \mathrm { l e v } _ { a } V _ { f } : = \{ x \mid V _ { f } ( x ) \leq a \}$ for some suitably chosen constant a. As shown in Section 2.5.1.3, under the assumptions made previously, there exists an $\alpha > 0$ such that

$$V _ {f} (f (x, K x)) + \ell (x, K x) - V _ {f} (x) \leq 0 \forall x \in \mathbb {X} _ {f} := W (a)$$

in which $x ^ { + } = f ( x , K x )$ describes the nonlinear system if the linear controller $u \ = \ K x$ is employed. To take into account the state and control constraints, we reduce a if necessary to satisfy, in addition,
