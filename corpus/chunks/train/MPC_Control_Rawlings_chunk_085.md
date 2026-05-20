# 1.4.2 Linear Optimal State Estimation

We start by assuming the initial state $x ( 0 )$ is normally distributed with some mean and covariance

$$x (0) \sim N (\overline {{x}} (0), Q (0))$$

In applications, we often do not know $\overline { { x } } ( 0 )$ or $Q ( 0 )$ . In such cases we often set $\overline { { x } } ( 0 ) ~ = ~ 0$ and choose a large value for $Q ( 0 )$ to indicate our lack of prior knowledge. This choice is referred to in the statistics literature as a noninformative prior. The choice of noninformative prior forces the upcoming $y ( k )$ measurements to determine the state estimate ${ \hat { x } } ( k )$ .

Combining the measurement. We obtain noisy measurement $y ( 0 )$ satisfying

$$\mathcal {Y} (0) = C x (0) + \nu (0)$$

in which $\nu ( 0 ) \sim N ( 0 , R )$ is the measurement noise. If the measurement process is quite noisy, then R is large. If the measurements are highly accurate, then R is small. We choose a zero mean for v because all of the deterministic effects with nonzero mean are considered part of the model, and the measurement noise reflects what is left after all these other effects have been considered. Given the measurement $y ( 0 )$ , we want to obtain the conditional density $p _ { x ( 0 ) | y ( 0 ) } ( x ( 0 ) | y ( 0 ) )$ . This conditional density describes the change in our knowledge about $x ( 0 )$ after we obtain measurement $y ( 0 )$ . This step is the essence of state estimation. To derive this conditional density, first consider the pair of variables $( x ( 0 ) , y ( 0 ) )$ given as

$$
\left[ \begin{array}{c} x (0) \\ y (0) \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ C & I \end{array} \right] \left[ \begin{array}{c} x (0) \\ v (0) \end{array} \right]
$$

We assume that the noise $\nu ( 0 )$ is statistically independent of $x ( 0 )$ , and use the independent joint normal result (1.21) to express the joint

density of $( x ( 0 ) , \nu ( 0 ) )$

$$
\left[ \begin{array}{c} x (0) \\ v (0) \end{array} \right] \sim N \left(\left[ \begin{array}{c} \overline {{x}} (0) \\ 0 \end{array} \right], \left[ \begin{array}{c c} Q (0) & 0 \\ 0 & R \end{array} \right]\right)
$$

From the previous equation, the pair $( x ( 0 ) , y ( 0 ) )$ is a linear transformation of the pair $( x ( 0 ) , \nu ( 0 ) )$ . Therefore, using the linear transformation of normal result (1.22), and the density of $( x ( 0 ) , \nu ( 0 ) )$ gives the density of $( x ( 0 ) , y ( 0 ) )$
