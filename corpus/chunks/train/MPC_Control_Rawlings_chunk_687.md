No optimization, ${ \textbf { \em p } } = { \bf \epsilon 0 } .$ . If we do no further optimization, then we have $\mathbf { u } _ { 1 } ^ { + } = \widetilde { \mathbf { u } } _ { 1 } ^ { + } , \mathbf { u } _ { 2 } ^ { + } = \widetilde { \mathbf { u } } _ { 2 } ^ { + }$ , and the equality

$$V (x _ {1} ^ {+}, x _ {2} ^ {+}, \mathbf {u} _ {1} ^ {+}, \mathbf {u} _ {2} ^ {+}) = V (x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}) - \rho_ {1} \ell_ {1} (x _ {1}, u _ {1}) - \rho_ {2} \ell_ {2} (x _ {2}, u _ {2})$$

The input sequences add a zero at each sample until ${ \bf u } _ { 1 } = { \bf u } _ { 2 } = 0$ at time $k = N$ . The system decays exponentially under zero control and the closed loop is exponentially stable.

Further optimization, $\textbf { \textit { p } } \geq \textbf { 1 }$ . We next consider the case in which optimization is performed. Equation 6.15 then gives

$$
\begin{array}{l} V (x _ {1} ^ {+}, x _ {2} ^ {+}, \mathbf {u} _ {1} ^ {+}, \mathbf {u} _ {2} ^ {+}) \leq V (x _ {1} ^ {+}, x _ {2} ^ {+}, \tilde {\mathbf {u}} _ {1} ^ {+}, \tilde {\mathbf {u}} _ {2} ^ {+}) - \\ \left[ \tilde {\mathbf {u}} ^ {+} - \mathbf {u} ^ {0} (x ^ {+}) \right] ^ {\prime} P \left[ \tilde {\mathbf {u}} ^ {+} - \mathbf {u} ^ {0} (x ^ {+}) \right] \quad p \geq 1 \\ \end{array}
$$

with equality holding for $p = 1$ . Using this result in (6.17) gives

$$
\begin{array}{l} V \left(x _ {1} ^ {+}, x _ {2} ^ {+}, \mathbf {u} _ {1} ^ {+}, \mathbf {u} _ {2} ^ {+}\right) \leq V \left(x _ {1}, x _ {2}, \mathbf {u} _ {1}, \mathbf {u} _ {2}\right) - \rho_ {1} \ell_ {1} \left(x _ {1}, u _ {1}\right) - \rho_ {2} \ell_ {2} \left(x _ {2}, u _ {2}\right) \\ - \left[ \tilde {\mathbf {u}} ^ {+} - \mathbf {u} ^ {0} (x ^ {+}) \right] ^ {\prime} P \left[ \tilde {\mathbf {u}} ^ {+} - \mathbf {u} ^ {0} (x ^ {+}) \right] \\ \end{array}
$$
