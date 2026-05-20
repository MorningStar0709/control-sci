# Solution

The definition of covariance gives

$$
\begin{array}{l} \operatorname{cov} (\xi , \eta) = \mathcal {E} ((\xi - \mathcal {E} (\xi)) (\eta - \mathcal {E} (\eta))) \\ = \mathcal {E} (\xi \eta - \xi \mathcal {E} (\eta) - \eta \mathcal {E} (\xi) + \mathcal {E} (\xi) \mathcal {E} (\eta)) \\ = \mathcal {E} (\xi \eta) - \mathcal {E} (\xi) \mathcal {E} (\eta) \\ \end{array}
$$

Taking the expectation of the product $\xi \eta$ and using the fact that $\xi$ and η are independent gives

$$
\begin{array}{l} \mathcal {E} (\xi \eta) = \iint_ {- \infty} ^ {\infty} x y p _ {\xi , \eta} (x, y) d x d y \\ = \iint_ {- \infty} ^ {\infty} x y p _ {\xi} (x) p _ {\eta} (y) d x d y \\ = \int_ {- \infty} ^ {\infty} x p _ {\xi} (x) d x \int_ {- \infty} ^ {\infty} y p _ {\eta} (y) d y \\ = \mathcal {E} (\xi) \mathcal {E} (\eta) \\ \end{array}
$$

Substituting this fact into the covariance equation gives

$$\operatorname{cov} (\xi , \eta) = 0$$
