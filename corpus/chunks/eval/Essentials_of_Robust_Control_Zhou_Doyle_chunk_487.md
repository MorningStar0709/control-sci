Let $\rho _ { R } ( M )$ be the real spectral radius $( { \mathrm { i . e . } }$ , the largest magnitude of the real eigenvalues of M ). For example, if $\mathrm { ~ a ~ 4 ~ } \times \mathrm { ~ 4 ~ }$ matrix M has eigenvalues $1 \pm j 3 , - 2 , 1$ , then $\rho ( M ) = | 1 + j 3 | = \sqrt { 1 0 }$ and $\rho _ { R } ( { \cal M } ) = | - 2 | = 2$ . It is easy to see that

$$\mu_ {\boldsymbol {\Delta}} (M) = \max _ {\boldsymbol {\Delta} \in \mathbf {B} \boldsymbol {\Delta}} \rho_ {R} (M \boldsymbol {\Delta})$$

where $\mathbf { B } \pmb { \Delta } : = \{ \pmb { \Delta } : ~ \Delta \in \pmb { \Delta } , ~ \overline { { \sigma } } ( \Delta ) \leq 1 \}$ . Note that $\operatorname* { m a x } _ { \Delta \in \mathbf { B } } \rho _ { R } ( M \Delta ) = \operatorname* { m a x } _ { \Delta \in \mathbf { B } \Delta } \rho ( M \Delta )$ if $s _ { r } = 0$ . [This should not be confused with the fact that, for a given matrix $\Delta \in \mathbf { B } \Delta$ and $M , \rho _ { R } ( M \Delta )$ may not be equal to $\rho ( M \Delta )$ . For example, $M = 2 e ^ { j { \frac { \pi } { 4 } } }$ and $\Delta = 1$ ; then $\rho ( M \Delta ) = 2$ but $\rho _ { R } ( M \Delta ) = 0$ since M has no real eigenvalues. However, one can choose another $\Delta _ { 1 } = e ^ { - j \frac { \pi } { 4 } }$ such that $\rho _ { R } ( { \cal M } \Delta _ { 1 } ) = 2 = \rho ( { \cal M } \Delta ) . ]$ ]

Define

$$
\mathcal {Q} = \{\Delta \in \boldsymbol {\Delta}: \phi_ {i} \in [ - 1, 1 ], | \delta_ {i} | = 1, \Delta_ {i} \Delta_ {i} ^ {*} = I _ {m _ {i}} \}
\mathcal {D} = \left\{ \begin{array}{c} \operatorname{diag} \left[ \tilde {D} _ {1}, \ldots , \tilde {D} _ {s _ {r}}, D _ {1}, \ldots , D _ {s _ {c}}, d _ {1} I _ {m _ {1}}, \ldots , d _ {F - 1} I _ {m _ {F - 1}}, I _ {m _ {F}} \right]: \\ \tilde {D} _ {i} \in \mathbb {C} ^ {k _ {i} \times k _ {i}}, \tilde {D} _ {i} = \tilde {D} _ {i} ^ {*} > 0, D _ {i} \in \mathbb {C} ^ {r _ {i} \times r _ {i}}, D _ {i} = D _ {i} ^ {*} > 0, d _ {j} \in \mathbb {R}, d _ {j} > 0 \end{array} \right\}.
\mathcal {G} = \left\{\operatorname{diag} \left[ G _ {1}, \dots , G _ {s _ {r}}, 0, \dots , 0 \right]: G _ {i} = G _ {i} ^ {*} \in \mathbb {C} ^ {k _ {i} \times k _ {i}} \right\}.
$$

It was shown in Young [1993] that

$$\mu_ {\Delta} (M) = \max _ {Q \in \mathcal {Q}} \rho_ {R} (Q M).$$

Note that the above maximization is not necessarily achieved on the vertices for the real parameters; hence one must search over the entire interval for each real parameter. Again this maximization problem can have many local maximums and a power algorithm has been developed in Young [1993] to compute a lower bound.
