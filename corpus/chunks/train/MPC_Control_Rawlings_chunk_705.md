# 6.3.3 Exponential Stability with Estimate Error

Consider next the constrained system evolution with estimate error

$$
\left[ \begin{array}{c} \hat {x} ^ {+} \\ \mathbf {u} ^ {+} \\ e ^ {+} \end{array} \right] = \left[ \begin{array}{c} A \hat {x} + \overline {{B}} _ {1} u _ {1} + \overline {{B}} _ {2} u _ {2} + L e \\ g ^ {p} (\hat {x}, \mathbf {u}) \\ A _ {L} e \end{array} \right] \tag {6.22}
$$

The estimate error is globally exponentially stable so we know from Lemma 6.6 that there exists a Lipschitz continuous Lyapunov function $J ( \cdot )$ such that for all $e \in \mathbb { R } ^ { n }$

$$\overline {{a}} | e | \leq J (e) \leq \overline {{b}} | e |J (e ^ {+}) - J (e) \leq - \overline {{c}} | e |$$

in which $\overline { { b } } \ > \ 0 , \ \overline { { a } } \ > \ 0$ , and we can choose constant $\tau > 0$ as large as desired. In the subsequent development, we require this Lyapunov function to be based on the first power of the norm rather than the usual square of the norm to align with Lipschitz continuity of the Lyapunov function. From the stability of the solution $x ( k ) = 0$ for all k for the nominal system, the cost function $V ( \hat { x } , { \mathbf { u } } )$ satisfies for all $\hat { x } \in \mathcal { X } _ { N }$ , $\mathbf { u } \in \mathbb { U } ^ { N }$

$$\tilde {a} | (\hat {x}, \mathbf {u}) | ^ {2} \leq V (\hat {x}, \mathbf {u}) \leq \tilde {b} | (\hat {x}, \mathbf {u}) | ^ {2}V (A \hat {x} + \overline {{B}} _ {1} u _ {1} + \overline {{B}} _ {2} u _ {2}, \mathbf {u} ^ {+}) - V (\hat {x}, \mathbf {u}) \leq - \widetilde {c} | \hat {x} | ^ {2}| \mathbf {u} | \leq d | \hat {x} | \quad \hat {x} \in \tilde {\gamma} \mathcal {B}$$

in which $\tilde { a } , \tilde { b } , \tilde { c } , \tilde { r } > 0$ . We propose $W ( \hat { x } , { \mathbf { u } } , e ) = V ( \hat { x } , { \mathbf { u } } ) + J ( e )$ as a Lyapunov function candidate for the perturbed system. We next derive the required properties of $W ( \cdot )$ to establish exponential stability of the solution $( x ( k ) , e ( k ) ) = 0$ . From the definition of $W ( \cdot )$ we have for all $( \hat { x } , \mathbf { u } , e ) \in \mathcal { X } _ { N } \times \mathbb { U } ^ { N } \times \mathbb { R } ^ { n }$

$$\tilde {a} | (\hat {x}, \mathbf {u}) | ^ {2} + \overline {{a}} | e | \leq W (\hat {x}, \mathbf {u}, e) \leq \tilde {b} | (\hat {x}, \mathbf {u}) | ^ {2} + \overline {{b}} | e |a \left(\left| (\hat {x}, \mathbf {u}) \right| ^ {2} + | e |\right) \leq W (\hat {x}, \mathbf {u}, e) \leq b \left(\left| (\hat {x}, \mathbf {u}) \right| ^ {2} + | e |\right) \tag {6.23}$$
