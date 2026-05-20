$$
\begin{array}{l} \frac {\partial \mathcal {L} (\mathbf {x} ^ {*} (k) , \mathbf {x} ^ {*} (k + 1) , \mathbf {u} ^ {*} (k) , \boldsymbol {\lambda} ^ {*} (k + 1))}{\partial \mathbf {x} ^ {*} (k)} \\ + \frac {\partial \mathcal {L} (\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , \mathbf {u} ^ {*} (k - 1) , \boldsymbol {\lambda} ^ {*} (k))}{\partial \mathbf {x} ^ {*} (k)} = 0 \tag {5.2.6} \\ \end{array}
\frac {\partial \mathcal {L} (\mathbf {x} ^ {*} (k) , \mathbf {x} ^ {*} (k + 1) , \mathbf {u} ^ {*} (k) , \boldsymbol {\lambda} ^ {*} (k + 1))}{\partial \mathbf {u} ^ {*} (k)}+ \frac {\partial \mathcal {L} (\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , \mathbf {u} ^ {*} (k - 1) , \boldsymbol {\lambda} ^ {*} (k))}{\partial \mathbf {u} ^ {*} (k)} = 0 \tag {5.2.7}\frac {\partial \mathcal {L} (\mathbf {x} ^ {*} (k) , \mathbf {x} ^ {*} (k + 1) , \mathbf {u} ^ {*} (k) , \boldsymbol {\lambda} ^ {*} (k + 1))}{\partial \boldsymbol {\lambda} ^ {*} (k)}+ \frac {\partial \mathcal {L} (\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , \mathbf {u} ^ {*} (k - 1) , \boldsymbol {\lambda} ^ {*} (k))}{\partial \boldsymbol {\lambda} ^ {*} (k)} = 0 \tag {5.2.8}
$$

and the boundary (final) condition (5.1.22) becomes

$$\left[ \frac {\partial \mathcal {L} (\mathbf {x} (k - 1) , \mathbf {x} (k) , \mathbf {u} (k - 1) , \boldsymbol {\lambda} (k))}{\partial \mathbf {x} (k)} + \frac {\partial S (\mathbf {x} (k) , k)}{\partial \mathbf {x} (k)} \right] _ {*} ^ {\prime} \delta \mathbf {x} (k) \Bigg | _ {k = k _ {0}} ^ {k = k _ {f}} = 0 \tag {5.2.9}$$

where, from (5.2.3),

$$S (\mathbf {x} (k _ {f}), k _ {f}) = \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F} (k _ {f}) \mathbf {x} (k _ {f}). \tag {5.2.10}$$

\- Step 4: Hamiltonian: Although relations (5.2.6) to (5.2.10) give the required conditions for optimum, we proceed to get the results in a more elegant manner in terms of the Hamiltonian which is defined as

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} ^ {*} (k), \mathbf {u} ^ {*} (k), \boldsymbol {\lambda} ^ {*} (k + 1)) = \frac {1}{2} \mathbf {x} ^ {* \prime} (k) \mathbf {Q} (k) \mathbf {x} ^ {*} (k) \\ + \frac {1}{2} \mathbf {u} ^ {* \prime} (k) \mathbf {R} (k) \mathbf {u} ^ {*} (k) \\ + \boldsymbol {\lambda} ^ {* \prime} (k + 1) [ \mathbf {A} (k) \mathbf {x} ^ {*} (k) + \mathbf {B} (k) \mathbf {u} ^ {*} (k) ]. \tag {5.2.11} \\ \end{array}
$$

Thus, the Lagrangian (5.2.5) and the Hamiltonian (5.2.11) are related as
