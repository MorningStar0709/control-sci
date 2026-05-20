$$
\mathcal {U} = \{U \in \boldsymbol {\Delta}: U U ^ {*} = I _ {n} \} \tag {10.7}
\mathcal {D} = \left\{ \begin{array}{c} \operatorname{diag} \left[ D _ {1}, \dots , D _ {S}, d _ {1} I _ {m _ {1}}, \dots , d _ {F - 1} I _ {m _ {F - 1}}, I _ {m _ {F}} \right]: \\ D _ {i} \in \mathbb {C} ^ {r _ {i} \times r _ {i}}, D _ {i} = D _ {i} ^ {*} > 0, d _ {j} \in \mathbb {R}, d _ {j} > 0 \end{array} \right\}. \tag {10.8}
$$

Note that for any $\Delta \in \Delta , U \in \mathcal { U }$ , and $D \in \mathcal { D }$ ,

$$U ^ {*} \in \mathcal {U} \quad U \Delta \in \boldsymbol {\Delta} \quad \Delta U \in \boldsymbol {\Delta} \quad \overline {{\sigma}} (U \Delta) = \overline {{\sigma}} (\Delta U) = \overline {{\sigma}} (\Delta) \tag {10.9}D \Delta = \Delta D. \tag {10.10}$$

Consequently, we have the following:

Theorem 10.2 For all $U \in \mathcal { U }$ and $D \in \mathcal { D }$

$$\mu_ {\Delta} (M U) = \mu_ {\Delta} (U M) = \mu_ {\Delta} (M) = \mu_ {\Delta} \left(D M D ^ {- 1}\right). \tag {10.11}$$

Proof. For all $D \in \mathcal { D }$ and $\Delta \in \Delta$ ,

$$\det (I - M \Delta) = \det (I - M D ^ {- 1} \Delta D) = \det (I - D M D ^ {- 1} \Delta)$$

since D commutes with ∆. Therefore $\begin{array} { r l } { \mu _ { \pmb { \Delta } } ( M ) } & { { } = \mu _ { \pmb { \Delta } } \left( D M D ^ { - 1 } \right) } \end{array}$ . Also, for each $U \in { \mathcal { U } } ,$ det $\left( I - M \Delta \right) = 0$ if and only if det $( I - M U U ^ { * } \Delta ) = 0 .$ Since $U ^ { * } \Delta \in \Delta$ and $\overline { { \sigma } } \left( U ^ { * } \Delta \right) = \overline { { \sigma } } \left( \Delta \right)$ , we get $\mu _ { \pmb { \Delta } } \left( M U \right) = \mu _ { \pmb { \Delta } } ( M )$ as desired. The argument for $U M$ is the same. ✷

Therefore, the bounds in equation (10.6) can be tightened to

$$\max _ {U \in \mathcal {U}} \rho (U M) \leq \max _ {\Delta \in \mathbf {B} \Delta} \rho (\Delta M) = \mu_ {\boldsymbol {\Delta}} (M) \leq \inf _ {D \in \mathcal {D}} \overline {{\sigma}} (D M D ^ {- 1}) \tag {10.12}$$

where the equality comes from Lemma 10.1. Note that the last element in the D matrix is normalized to 1 since for any nonzero scalar $\gamma , D M D ^ { - 1 } = ( \gamma D ) M ( \gamma D ) ^ { - 1 }$ .
