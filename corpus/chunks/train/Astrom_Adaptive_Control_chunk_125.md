# EXAMPLE 2.15 Influence of forgetting factor

The recursive least-squares algorithm (2.21) has a forgetting factor $\lambda$ . The influence of the forgetting factor is shown in Figure 2.12. When $\lambda = 1$ , the estimates become smoother and smoother, since the gain $K(t)$ goes to zero. When $\lambda < 1$ , the estimator gain $K(t)$ does not go to zero, and the estimates will always fluctuate. The fluctuations increase with decreasing $\lambda$ . As a rule of thumb the “memory” of the estimator is

$$N = \frac {2}{1 - \lambda}$$

For $\lambda = 0.99$ the estimates are based on approximately the last 200 steps. ☐
