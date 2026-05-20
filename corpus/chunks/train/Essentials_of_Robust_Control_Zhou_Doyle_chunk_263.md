# 10.2.2 Bounds

In this section we will concentrate on the bounds

$$\max _ {U \in \mathcal {U}} \rho (U M) \leq \mu_ {\boldsymbol {\Delta}} (M) \leq \inf _ {D \in \mathcal {D}} \overline {{\sigma}} (D M D ^ {- 1}).$$

The lower bound is always an equality (Doyle [1982]).

Theorem 10.3 $\operatorname* { m a x } _ { U \in \mathcal { U } } \rho ( M U ) = \mu _ { \pmb { \Delta } } ( M )$

Unfortunately, the quantity $\rho \left( U M \right)$ can have multiple local maxima that are not global. Thus local search cannot be guaranteed to obtain $\mu ,$ but can only yield a lower bound. For computation purposes one can derive a slightly different formulation of the lower bound as a power algorithm that is reminiscent of power algorithms for eigenvalues and singular values (Packard and Doyle [1988a, 1988b]). While there are open questions about convergence, the algorithm usually works quite well and has proven to be an effective method to compute $\mu .$ .

The upper-bound can be reformulated as a convex optimization problem, so the global minimum can, in principle, be found. Unfortunately, the upper-bound is not always equal to $\mu .$ . For block structures $\pmb { \Delta }$ satisfying $2 S + F \le 3$ , the upper-bound is always equal to $\mu _ { \Delta } ( M )$ , and for block structures with $2 S + F > 3$ , there exist matrices for which $\mu$ is less than the infimum. This can be summarized in the following diagram, which shows for which cases the upper-bound is guaranteed to be equal to $\mu .$ See Packard and Doyle [1993] for details.

Theorem 10.4 $\mu _ { \Delta } ( M ) = \operatorname * { i n f } _ { D \in \mathcal { D } } \overline { { \sigma } } ( D M D ^ { - 1 } ) \ i f \ 2 S + F \leq 3$

<table><tr><td> $F=$  $S=$ </td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>0</td><td></td><td>yes</td><td>yes</td><td>yes</td><td>no</td></tr><tr><td>1</td><td>yes</td><td>yes</td><td>no</td><td>no</td><td>no</td></tr><tr><td>2</td><td>no</td><td>no</td><td>no</td><td>no</td><td>no</td></tr></table>

Several of the boxes have connections with standard results.

$$\bullet S = 0, F = 1: \mu_ {\Delta} (M) = \overline {{\sigma}} (M).$$

• $S = 1 , F = 0 : \mu _ { \Delta } ( M ) = \rho ( M ) = \operatorname* { i n f } _ { { D } \in { D } } \overline { { \sigma } } \left( D M { D } ^ { - 1 } \right)$ DED . This is a standard result in linear algebra. In fact, without a loss in generality, the matrix M can be assumed in Jordan canonical form. Now let
