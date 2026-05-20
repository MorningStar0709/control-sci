# C.1.1 Optimal Control Problem

The discrete time system we consider is described by

$$x ^ {+} = f (x, u) \tag {C.1}$$

where $f ( \cdot )$ is continuous. The system is subject to the mixed statecontrol constraint

$$(x, u) \in \mathbb {Z}$$

where $\mathbb { Z }$ is a closed subset of $\mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ and $\mathcal { P } _ { u } ( \mathbb { Z } )$ is compact where $\mathcal { P } _ { u }$ is the projection operator $( x , u ) \mapsto u$ . Often $\mathbb { Z } = \mathbb { X } \times \mathbb { U }$ in which case the constraint $( x , u ) \in \mathbb { Z }$ becomes $x \in \mathbb { X }$ and $u \in \mathbb { U }$ and $\mathcal { P } _ { u } ( \mathbb { Z } ) = \mathbb { U }$ so that U is compact. In addition there is a constraint on the terminal state $x ( N )$ :

$$x (N) \in \mathbb {X} _ {f}$$

where $\mathbb { X } _ { f }$ is closed. In this section we find it easier to express the value function and the optimal control in terms of the current state and current time i rather than using time-to-go k. Hence we replace time-to-go k by time i where $k = N - i$ , replace $V _ { k } ^ { 0 } ( x )$ (the optimal cost at state x when the time-to-go is k) by $V ^ { 0 } ( x , i )$ (the optimal cost at state x, time i) and replace $X _ { k }$ by $X ( i )$ where $X ( i )$ is the domain of $V ^ { 0 } ( \cdot , i ) )$ .

The cost associated with an initial state x at time 0 and a control sequence $\mathbf { u } : = \{ u ( 0 ) , u ( 1 ) , \ldots , u ( N - 1 ) \}$ is

$$V (x, 0, \mathbf {u}) = V _ {f} (x (N)) + \sum_ {i = 1} ^ {N - 1} \ell (x (i), u (i)) \tag {C.2}$$

where $\ell ( \cdot )$ and $V _ { f } ( \cdot )$ are continuous and, for each $i , x ( i ) = \phi ( i ; ( x , 0 ) , \mathbf { u } )$ is the solution at time i of (C.1) if the initial state is x at time 0 and the control sequence is u. The optimal control problem $\mathbb { P } ( x , 0 )$ is defined by

$$V ^ {0} (x, 0) = \min _ {\mathbf {u}} V (x, 0, \mathbf {u}) \tag {C.3}$$

subject to the constraints $( \boldsymbol { x } ( i ) , \boldsymbol { u } ( i ) ) \ \in \ \mathbb { Z } , \ i \ = \ 0 , 1 , \dots , N - 1$ and $x ( N ) \in \mathbb { X } _ { f }$ . Equation (C.3) may be rewritten in the form

$$V ^ {0} (x, 0) = \min _ {\mathbf {u}} \{V (x, 0, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} (x, 0) \} \tag {C.4}$$

where u := {u(0), u(1), . . . , u(N − 1)},

$$\mathcal {U} (x, 0) := \left\{\mathbf {u} \in \mathbb {R} ^ {N m} \mid (x (i), u (i)) \in \mathbb {Z}, i = 0, 1, \dots , N - 1; x (N) \in \mathbb {X} _ {f} \right\}$$
