$$
\left[ \begin{array}{c} x (0) \\ y (0) \end{array} \right] \sim N \left(\left[ \begin{array}{c} \overline {{x}} (0) \\ C \overline {{x}} (0) \end{array} \right], \left[ \begin{array}{c c} Q (0) & Q (0) C ^ {\prime} \\ C Q (0) & C Q (0) C ^ {\prime} + R \end{array} \right]\right)
$$

Given this joint density, we then use the conditional of a joint normal result (1.23) to obtain

$$p _ {x (0) \mid y (0)} (x (0) \mid y (0)) = n (x (0), m, P)$$

in which

$$m = \overline {{{x}}} (0) + L (0) \left(y (0) - C \overline {{{x}}} (0)\right)L (0) = Q (0) C ^ {\prime} (C Q (0) C ^ {\prime} + R) ^ {- 1}P = Q (0) - Q (0) C ^ {\prime} (C Q (0) C ^ {\prime} + R) ^ {- 1} C Q (0)$$

We see that the conditional density $p _ { x ( 0 ) | y ( 0 ) }$ is normal. The optimal state estimate is the value of $x ( 0 )$ that maximizes this conditional density. For a normal, that is the mean, and we choose ${ \hat { x } } ( 0 ) = m$ . We also denote the variance in this conditional after measurement $y ( 0 )$ by $P ( 0 ) \ = \ P$ with P given in the previous equation. The change in variance after measurement $( Q ( 0 )$ to $P ( 0 ) )$ quantifies the information increase by obtaining measurement $y ( 0 )$ . The variance after measurement, $P ( 0 )$ , is always less than or equal to $Q ( 0 )$ , which implies that we can only gain information by measurement; but the information gain may be small if the measurement device is poor and the measurement noise variance R is large.

Forecasting the state evolution. Next we consider the state evolution from $k = 0 \mathrm { ~ t o ~ } k = 1$ , which satisfies

$$
x (1) = \left[ \begin{array}{c c} A & I \end{array} \right] \left[ \begin{array}{c} x (0) \\ w (0) \end{array} \right]
$$

in which $w ( 0 ) \sim N ( 0 , Q )$ is the process noise. If the state is subjected to large disturbances, then Q is large, and if the disturbances are small, Q is small. Again we choose zero mean for w because the nonzero mean disturbances should have been accounted for in the system model. We next calculate the conditional density $p _ { x ( 1 ) | y ( 0 ) }$ . Now we require the conditional version of the joint density $( x ( 0 ) , w ( 0 ) )$ . We assume that the process noise $\boldsymbol { w } \left( 0 \right)$ is statistically independent of both $x ( 0 )$ and $\nu ( 0 )$ , hence it is also independent of $y ( 0 )$ , which is a linear combination of $x ( 0 )$ and $\nu ( 0 )$ . Therefore we use (1.24) to obtain
