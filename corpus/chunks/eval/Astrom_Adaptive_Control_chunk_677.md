# Robust Estimation

The least-squares estimate is optimal if the disturbances are Gaussian and such that the equation error is white noise. In practice the least-squares estimate has some drawbacks because the assumptions are violated. It is a direct consequence of the least-squares formulation that a single large error will have a drastic influence on the result because the errors are squared in the criterion. This is a consequence of the Gaussian assumption that implies that the probability of large errors is very small. Estimators with very different properties are obtained if it is assumed that the probability for large errors is not negligible. Without going into technicalities, we remark that the estimators will be replaced by equations such as

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + P (t) \varphi (t - 1) f (\varepsilon (t))\frac {d \hat {\theta}}{d t} = P \varphi f (\varepsilon)$$

where the function $f(\varepsilon)$ is linear for small $\varepsilon$ but increases more slowly than linear for large $\varepsilon$ . A typical example is

$$f (\varepsilon) = \frac {\varepsilon}{1 + a | \varepsilon |}$$

The net effect is to decrease the consequences of large errors. The estimators are then called robust.
