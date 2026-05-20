# Exponential Forgetting

Exponential forgetting is a way to discard old data. It is based on the assumption that the least-squares loss function is replaced by a loss function in which old data is discounted exponentially. It follows from Theorem 2.4 that the recursive least-squares estimate with exponential forgetting is given by

$$\hat {\theta} (t) = \hat {\theta} (t - 1) + K (t) \left(y (t) - \varphi^ {T} (t) \hat {\theta} (t - 1)\right)K (t) = P (t - 1) \varphi (t) (\lambda + \varphi^ {T} (t) P (t - 1) \varphi (t)) ^ {- 1} \tag {11.19}P (t) = \frac {1}{\lambda} (I - K (t) \varphi^ {T} (t)) P (t - 1)$$

Table 11.3 Relations between the ratio $T_f / h$ and the coefficient $\lambda$ . 

<table><tr><td> $T_f/h$ </td><td> $\lambda$ </td></tr><tr><td>1</td><td>0.37</td></tr><tr><td>2</td><td>0.61</td></tr><tr><td>5</td><td>0.82</td></tr><tr><td>10</td><td>0.90</td></tr><tr><td>20</td><td>0.95</td></tr><tr><td>50</td><td>0.98</td></tr><tr><td>100</td><td>0.99</td></tr></table>

where the sampling period $h$ was chosen as the time unit. The forgetting factor is given by

$$\lambda = e ^ {h / T _ {j}}$$

where $T_{f}$ is the time constant for the exponential forgetting. To make an assessment of reasonable values of the forgetting factor, we give the values of the forgetting factor for different ratios $T_{f}/h$ in Table 11.3.

It is possible to generalize the method with exponential forgetting and have different forgetting factors for different parameters. However, this requires information about the nature of the changes in different parameters. Another modification is to modify Eqs. (11.19) so that only the diagonal elements are divided by $\lambda$ .

Tracking of a time-varying parameter is illustrated by an example.
