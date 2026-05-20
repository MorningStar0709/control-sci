# A.16.1 Statistical Independence and Correlation

We say two random variables $\xi , \eta$ are statistically independent or simply independent if

$$p _ {\xi , \eta} (x, y) = p _ {\xi} (x) p _ {\eta} (y), \quad \text { all } x, y$$

The covariance of two random variables $\xi , \eta$ is defined as

$$\operatorname{cov} (\xi , \eta) = \mathcal {E} \left(\left(\xi - \mathcal {E} (\xi)\right) (\eta - \mathcal {E} (\eta))\right)$$

The covariance of the vector-valued random variable $\xi$ with components $\xi _ { i } , i = 1 , \ldots n$ can be written as

$$
\begin{array}{l} P _ {i j} = \operatorname{cov} (\xi_ {i}, \xi_ {j}) \\ P = \left[ \begin{array}{c c c c} \operatorname{var} (\xi_ {1}) & \operatorname{cov} (\xi_ {1}, \xi_ {2}) & \dots & \operatorname{cov} (\xi_ {1}, \xi_ {n}) \\ \operatorname{cov} (\xi_ {2}, \xi_ {1}) & \operatorname{var} (\xi_ {2}) & \dots & \operatorname{cov} (\xi_ {2}, \xi_ {n}) \\ \vdots & \vdots & \ddots & \vdots \\ \operatorname{cov} (\xi_ {n}, \xi_ {1}) & \operatorname{cov} (\xi_ {n}, \xi_ {2}) & \dots & \operatorname{var} (\xi_ {n}) \end{array} \right] \\ \end{array}
$$

We say two random variables, $\xi$ and η, are uncorrelated if

$$\operatorname{cov} (\xi , \eta) = 0$$
