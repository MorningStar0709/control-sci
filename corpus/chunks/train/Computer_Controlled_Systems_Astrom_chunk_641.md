# Example 10.8 First-order continuous-time system

Consider the scalar stochastic differential equation

$$d x = - a x d t + d vx \left(t _ {0}\right) = m _ {0} \quad \operatorname{var} \left(x \left(t _ {0}\right)\right) = r _ {0}$$

where the process $\{v(t), t \in T\}$ has incremental covariance $r_{1} dt$ . It follows from (10.28) that the mean-value function is given by

$$\frac {d m}{d t} = - a m \quad m (t _ {0}) = m _ {0}$$

This equation has the solution

$$m (t) = m _ {0} e ^ {- a (t - t _ {0})}$$

The covariance function is given by

$$r (s, t) = \operatorname{cov} (x (s), x (t)) = e ^ {- a (s - t)} P (t) \quad s \geq t$$

and

$$r (s, t) = e ^ {- a (t - s)} P (s) \quad s \geq t$$

Equation (10.30) gives the following differential equation for P.

$$\frac {d P}{d t} = - 2 a P + r _ {1} \quad P (t _ {0}) = r _ {0}$$

This differential equation has the solution

$$P (t) = e ^ {- 2 a (t - t _ {0})} r _ {0} + \int_ {t _ {0}} ^ {t} e ^ {- 2 a (t - s)} r _ {1} d s= e ^ {- 2 a (t - t _ {0})} r _ {0} + \frac {r _ {1}}{2 a} \left(1 - e ^ {- 2 a (t - t _ {0})}\right)$$

As $t_0 \to -\infty$ , the mean-value function goes to zero and the covariance function goes to

$$r (s, t) = \frac {r _ {1}}{2 a} e ^ {- a | t - s |}$$

because the limiting covariance function depends only on the argument difference $s - t$ , the limiting process is (weakly) stationary and its covariance function can be written as

$$r (\tau) = \frac {r _ {1}}{2 a} e ^ {- a | r |}$$

Equation (10.24) gives the corresponding spectral density

$$\phi (\omega) = \frac {r _ {1}}{2 \pi} \cdot \frac {1}{\omega^ {2} + a ^ {2}}$$
