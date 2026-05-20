# 3.1 Introduction

Similarly, an uncertain system may be described by the difference equation

$$x ^ {+} = f (x, u, w) \tag {3.2}$$

in which the variable w that represents the uncertainty takes values in a specified set W. We use $\phi ( k ; x , i , { \mathbf { u } } , { \mathbf { w } } )$ to denote the solution of (3.2) when the initial state at time i is x and the control and disturbance sequences are, respectively, $\textbf { u } = { \{ u ( 0 ) , u ( 1 ) , \dots \} }$ and $\textbf { w } =$ $\{ w ( 0 ) , w ( 1 ) , \ldots \}$ . The uncertain system may alternatively be described by a difference inclusion of the form

$$x ^ {+} \in F (x, u)$$

in which $F ( \cdot )$ is a set-valued map. We use the notation $F : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \sim$ $\mathbb { R } ^ { n }$ or1 $F : \mathbb { R } ^ { n } \times \mathbb { R } ^ { m } \to 2 ^ { \mathbb { R } ^ { n } }$ to denote a function that maps points in $\mathbb { R } ^ { n } \times \mathbb { R } ^ { m }$ into subsets of $\mathbb { R } ^ { n }$ . If the uncertain system is described by (3.2), then

$$F (x, u) = f (x, u, \mathbb {W}) := \{f (x, u, w) \mid w \in \mathbb {W} \}$$

If x is the current state, and u the current control, the successor state $x ^ { + }$ lies anywhere in the set $F ( x , u )$ . If a control policy $\pmb { \mu } : = \ \{ \mu _ { 0 } ( \cdot )$ , $\mu _ { 1 } ( \cdot ) , \ldots \}$ is employed, the state evolves according to

$$x ^ {+} \in F (x, \mu_ {k} (x)) \tag {3.3}$$

in which x is the current state, k the current time, and $x ^ { + }$ the successor state at time $k + 1$ . The system described by (3.3) does not have a single solution for a given initial state; it has a solution for each possible realization w of the disturbance sequence. We use $S ( x , i )$ to denote the set of solutions of (3.3) if the initial state is x at time i. If $\phi ( \cdot ) \in S ( x , i )$ then

$$\phi (t) = \phi (t; x, i, \pmb {\mu}, \mathbf {w})$$

for some admissible disturbance sequence w where $\phi ( t ; x , i , \pmb { \mu } , \mathbf { w } )$ denotes the solution at time t of

$$x ^ {+} = f (x, \mu_ {k} (x), w)$$

when the initial state is x at time i and the disturbance sequence is w. The policy µ is defined, as before, to be the sequence $\{ \mu _ { 0 } ( \cdot ) , \mu _ { 1 } ( \cdot ) , \ldots ,$ $\mu _ { N - 1 } ( \cdot ) \big \}$ of control laws. The tube $\mathbf { X } = \{ X _ { 0 } , X _ { 1 } , \ldots \}$ , discussed in Section 3.4, generated when policy $\pmb { \mu }$ is employed, satisfies

$$X _ {k + 1} = \mathbf {F} (X _ {k}, \mu_ {k} (\cdot)) := \{f (x, \mu_ {k} (x), w) \mid x \in X _ {k}, w \in \mathbb {W} \}$$

in which F maps sets into sets.
