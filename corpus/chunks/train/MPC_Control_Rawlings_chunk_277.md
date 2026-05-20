in which, with $x ( N ) : = \phi ( N ; x , { \bf u } )$ ,

$$V _ {N} ^ {e} (x, \mathbf {u}) := J _ {N} (x, \mathbf {u}) + V _ {f} ^ {e} (x (N))$$

and $J _ { N } ( \cdot )$ and $\hat { \mathcal { U } } _ { N } ( x )$ are defined in Section 2.6.1. Let $\mathbf { u } ^ { e } ( x )$ denote the solution of $\mathbb { P } _ { N } ^ { e } ( x )$ and $\mathbf { x } ^ { e } ( x )$ the associated state trajectory where

$$\mathbf {u} ^ {e} (x) = \{u ^ {e} (0; x), u ^ {e} (1; x), \dots , u ^ {e} (N - 1; x) \}\mathbf {x} ^ {e} (x) = \{x ^ {e} (0; x), x ^ {e} (1; x), \ldots , x ^ {e} (N; x) \}$$

The implicit MPC control law is $\kappa _ { N } ^ { e } ( \cdot )$ defined by

$$\kappa_ {N} ^ {e} (x) := u ^ {e} (0; x)$$

We now define a restricted set $\mathcal { X } _ { N } ^ { e }$ of initial states by

$$\mathcal {X} _ {N} ^ {e} := \{x \mid x ^ {e} (N; x) \in \mathbb {X} _ {f} \}$$

Hence, the terminal state of any optimal state trajectory with initial state $x \in \mathcal { X } _ { N } ^ { e }$ lies in $\mathbb { X } _ { f }$ . It follows, by the usual arguments, that for all $x \in \mathcal { X } _ { N } ^ { e }$

$$\hat {V} _ {N} ^ {e} (x ^ {+}) \leq \hat {V} _ {N} ^ {e} (x) - \ell (x, \kappa_ {N} ^ {e} (x))$$

where $x ^ { + } : = f ( x , \kappa _ { N } ^ { e } ( x ) ) = x ^ { e } ( 1 ; x )$ . If $\mathcal { X } _ { N } ^ { e }$ is positive invariant for $x ^ { + } = f ( x , \kappa _ { N } ^ { e } ( x ) )$ , the origin is asymptotically stable for the system $x ^ { + } : = f ( x , \kappa _ { N } ^ { e } ( x ) )$ ) with a region of attraction $\mathcal { X } _ { N } ^ { e }$ . Note, however, that $x \in \mathcal { X } _ { N } ^ { e }$ does not necessarily imply that $x ^ { + } = f ( x , \kappa _ { N } ^ { e } ( x ) ) \in \mathcal { X } _ { N } ^ { e }$ . Hu and Linnemann (2002) show that $x \in \mathcal { X } _ { N } ^ { e }$ implies

$$V _ {f} ^ {e} (x ^ {e} (N; x ^ {+})) \leq V _ {f} ^ {e} (x ^ {e} (N - 1; x ^ {+})) - \ell (x ^ {e} (N - 1; x ^ {+}), u ^ {e} (N - 1; x ^ {+}))$$
