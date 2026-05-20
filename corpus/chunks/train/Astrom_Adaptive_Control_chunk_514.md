This functional equation is called the Bellman equation of the problem. The simplicity of the form of Eq. (7.17) is misleading. The equation cannot be solved analytically, but it requires extensive numerical computations to get the solution even for very simple problems.

The first term on the right-hand side of Eq. (7.17) can be evaluated in the same way as in the one-step minimization. The second term causes the difficulties in the optimization, since we have to evaluate

$$E \left\{V (\xi (t + 1), t + 1) \mid \mathcal {Y} _ {t - 1} ^ {\prime} \right\}$$

The average with respect to the distribution of $y(t)$ , given $Y_{t-1}$ , must be computed. According to Theorem 7.1 this distribution is Gaussian with mean $m_{y}(t)$ and variance $\sigma_{y}^{2}(t)$ . This gives

$$
\begin{array}{l} E \left\{V (\xi (t + 1), t + 1) \mid \mathcal {Y} _ {t - 1} \right\} \\ = \frac {1}{\sigma_ {y} \sqrt {2 \pi}} \int_ {- \infty} ^ {\infty} V (\tilde {\varphi} (t), \hat {x} (t + 1), P (t + 1), t + 1) e ^ {- (s - m _ {y}) ^ {2} / (2 \sigma_ {y} ^ {2})} d s \tag {7.18} \\ \end{array}
$$

where

$$\hat {x} (t + 1) = \Phi \hat {x} (t) + K (t) \left(s - \varphi^ {T} (t - 1) \hat {x} (t)\right)P (t + 1) = (\Phi - K (t) \varphi^ {T} (t - 1)) P (t) \Phi^ {T} + R _ {1}K (t) = \Phi P (t) \varphi (t - 1) / \sigma_ {y} ^ {2} (t)\sigma_ {y} ^ {2} (t) = R _ {2} + \varphi^ {T} (t - 1) P (t) \varphi (t - 1)\tilde {\varphi} _ {1} (t) = u (t - 1)\tilde {\varphi} _ {i} (t) = \tilde {\varphi} _ {i - 1} (t - 1) \quad i = 2, \dots , n, n + 2, \dots , 2 n\tilde {\varphi} _ {n + 1} (t) = s$$

These equations, together with Eq. (7.18), can be used to compute recursively the control signal and the loss as functions of the hyperstate. The control variable $u(t-1)$ influences the immediate loss (i.e., the first term on the right-hand side of Eq. (7.17)). Notice that $u(t-1)$ also influences the expected future loss, since it influences $\varphi(t-1)$ , which influences $\hat{x}(t+1)$ , $P(t+1)$ , and $\hat{\varphi}^{T}(t)$ . This means that the choice of the control signal $u(t-1)$ influences the immediate loss, the future parameter estimates, their accuracy, and also the future values of the output signal. The optimal controller is a dual controller. It makes a compromise between the control action and the probing action.

The probing action will add an active learning feature to the controller, in contrast to the cautious and certainty equivalence controllers, in which the learning is “accidental.” The optimal feedback will generate control actions that will improve the accuracy of the future estimates at the expense of the short-term loss. The cautious controller obtained when N = 1 will not benefit if probing is introduced; it only tries to make the loss as small as possible at the next instant of time.
