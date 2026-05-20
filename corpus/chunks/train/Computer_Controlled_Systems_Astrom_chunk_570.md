# Well-Conditioned Realizations

The difficulty associated with the companion form can be avoided simply by representing the system as a combination of first- and second-order systems. If the dynamic system representing the controller has $n_{r}$ distinct real poles and $n_{c}$ complex-pole pairs, the control algorithm may be transformed to the modal form

$$
z _ {i} (k + 1) = \lambda_ {i} z _ {i} (k) + \beta_ {i} y (k) \quad i = 1, \dots , n,
v _ {i} (k + 1) = \left( \begin{array}{c c} \sigma_ {i} & \omega_ {i} \\ - \omega_ {i} & \sigma_ {i} \end{array} \right) v _ {i} (k) + \binom {\gamma_ {i 1}} {\gamma_ {i 2}} y (k) \quad i = 1, \dots , n _ {c} \tag {9.19}
u (k) = D y (k) + \sum_ {i = 1} ^ {n _ {r}} \gamma_ {i} z _ {i} (k) + \sum_ {i = 1} ^ {n _ {c}} \delta_ {i} ^ {T} v _ {i} (k)
$$

where the complex poles are represented using real variables. Notice that $z_{i}$ are scalars and $v_{i}$ are vectors with two elements. To avoid numerical difficulties, the control law should be transformed to the form of (9.19), which is then implemented in the control computer. The transformation may easily be done in a package for computer-aided design. It is easy to use fixed-point calculations and scaling for equations in the form of (9.19). If the control law has multiple eigenvalues, a Jordan canonical form replaces (9.19). An eigenvalue $\lambda$ of multiplicity 3 thus corresponds to a block

$$
z (k + 1) = \left( \begin{array}{l l l} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{array} \right) z (k) + \left( \begin{array}{l} \beta_ {1} \\ \beta_ {2} \\ \beta_ {3} \end{array} \right) y (k)
$$
