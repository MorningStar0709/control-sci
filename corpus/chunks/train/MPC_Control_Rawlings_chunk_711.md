$$
\min _ {\tilde {\mathbf {u}} _ {1}} V (\tilde {x} _ {1} (0), \tilde {x} _ {2} (0), \tilde {\mathbf {u}} _ {1}, \tilde {\mathbf {u}} _ {2})
\text {s.t.} \left[ \begin{array}{c} \widetilde {x} _ {1} \\ \widetilde {x} _ {2} \end{array} \right] ^ {+} = \left[ \begin{array}{c c} A _ {1} & 0 \\ 0 & A _ {2} \end{array} \right] \left[ \begin{array}{c} \widetilde {x} _ {1} \\ \widetilde {x} _ {2} \end{array} \right] + \left[ \begin{array}{c} \overline {{B}} _ {1 1} \\ \overline {{B}} _ {2 1} \end{array} \right] \widetilde {u} _ {1} + \left[ \begin{array}{c} \overline {{B}} _ {1 2} \\ \overline {{B}} _ {2 2} \end{array} \right] \widetilde {u} _ {2}
\widetilde {\mathbf {u}} _ {1} \in \mathbb {U} _ {1} \ominus u _ {s} (k)S _ {1 u} ^ {\prime} \tilde {x} _ {1} (N) = 0\left| \tilde {\mathbf {u}} _ {1} \right| \leq d _ {1} \left| \tilde {x} _ {1} (0) \right|
$$

Notice that because the input constraint is shifted by the input target, we must retain feasibility of the regulation problem by restricting also the plant disturbance and its initial estimate error. If the two players’ regulation problems remain feasible as the estimate error converges to zero, we have exponential stability of the zero solution from Lemma 6.13. Therefore we conclude

$$(\tilde {x} (k), \tilde {u} (k)) \rightarrow (0, 0) \quad \text { Lemma 6.13 }\Rightarrow (\hat {x} (k), u (k)) \rightarrow (x _ {s} (k), u _ {s} (k)) \quad \text { definition of deviation variables }\Rightarrow (\hat {x} (k), u (k)) \rightarrow \left(x _ {s} ^ {*}, u _ {s} ^ {*}\right) \quad \text { target problem convergence }\Rightarrow x (k) \rightarrow x _ {s} ^ {*} \quad \text { estimator stability }\Rightarrow r (k) \rightarrow r _ {\mathrm{sp}} \quad \text { target equality constraint }$$

and we have zero offset in the plant controlled variable $r = H y$ . The rate of convergence of $r ( k )$ to $r _ { \mathrm { s p } }$ is also exponential. As we saw here, this convergence depends on maintaining feasibility in both the target problem and the regulation problem at all times.
