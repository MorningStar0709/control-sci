$$V _ {N} ^ {0} (x) \leq \alpha (| x |) \forall x \in \mathcal {X} _ {N}$$

Summarizing, we have:

If these assumptions on $V _ { f } ( \cdot ) , \mathbb { X } _ { f }$ , and $\ell ( \cdot )$ hold, and Assumptions 2.2 and 2.3 are satisfied, then Assumptions 2.12, 2.13, and 2.16(a) are satisfied. If, in addition, the controllability Assumption 2.23 is satisfied, then it follows from Theorem 2.24(b) that the origin is asymptotically stable with a region of attraction $x _ { N }$ for $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ .

Case 2. $V _ { f } ( x ) = ( 1 / 2 ) | x | _ { P } ^ { 2 } , \mathbb { X } _ { f } = \{ x \mid V _ { f } ( x ) \leq a \}$ . In this case we obtain a terminal cost function $V _ { f } ( \cdot )$ and a terminal constraint set $\mathbb { X } _ { f }$ by linearization of the nonlinear system $x ^ { + } ~ = ~ f ( x , u )$ at the origin. Hence, for the purpose of this case we assume $f ( \cdot )$ and $\ell ( \cdot )$ are twice continuously differentiable. Suppose then the linearized system is

$$x ^ {+} = A x + B u$$

where $A : = f _ { x } ( 0 , 0 )$ and $B : = f _ { u } ( 0 , 0 )$ . We assume that $( A , B )$ is stabilizable and we choose any controller $u = K x$ such that the origin is globally exponentially stable for the system $x ^ { + } = A _ { K } x , A _ { K } : = A + B K$ , i.e., such that $A _ { K }$ is stable. Suppose also that the stage cost $\ell ( \cdot )$ is defined by $\ell ( x , u ) : = ( 1 / 2 ) ( | x | _ { O } ^ { 2 } + | u | _ { R } ^ { 2 } )$ where Q and R are positive definite; hence $\ell ( x , K x ) = ( 1 / 2 ) \dot { x } ^ { \prime } Q ^ { * } x$ where $Q ^ { * } : = ( Q + K ^ { \prime } R K )$ . Let P be defined by the Lyapunov equation

$$A _ {K} ^ {\prime} P A _ {K} + 2 Q ^ {*} = P$$

The reason for the factor 2 will become apparent soon. Since $Q ^ { * }$ is positive definite and $A _ { K }$ is stable, P is positive definite. Let the terminal cost function $V _ { f } ( \cdot )$ be defined by

$$V _ {f} (x) := (1 / 2) x ^ {\prime} P x$$

Clearly $V _ { f } ( \cdot )$ is a global CLF for the linear system $x ^ { + } = A x + B u$ . Indeed, it follows from its definition that $V _ { f } ( \cdot )$ satisfies

$$V _ {f} (A _ {K} x) + x ^ {\prime} Q ^ {*} x - V _ {f} (x) = 0 \quad \forall x \in \mathbb {R} ^ {n} \tag {2.33}$$

Consider now the nonlinear system $x ^ { + } = f ( x , u )$ with linear control $u = K x$ . The controlled system satisfies

$$x ^ {+} = f (x, K x)$$

We wish to show that $V _ { f } ( \cdot )$ is a local CLF for $x ^ { + } = f ( x , u )$ in some neighborhood of the origin; specifically, we wish to show there exists an $a \in ( 0 , \infty )$ such that

$$V _ {f} (f (x, K x)) + (1 / 2) x ^ {\prime} Q ^ {*} x - V _ {f} (x) \leq 0 \quad \forall x \in W (a) \tag {2.34}$$
