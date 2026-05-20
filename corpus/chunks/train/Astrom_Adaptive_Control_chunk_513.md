# Multistep Optimization

The general multistep optimization problem can be solved by using dynamic programming. The fact that the conditional distributions are Gaussian will simplify the problem.

It follows from a fundamental result of stochastic control theory (see Åström (1970), Lemma 8:3.2) that

$$
\begin{array}{l} \min _ {u (t - 1) \dots u (N - 1)} E \left\{\sum_ {k = t} ^ {N} (y (k) - u _ {c} (k)) ^ {2} \right\} \\ = E \mathcal {Y} _ {t - 1} \left(\min E \left\{\sum_ {k = t} ^ {N} (y (k) - u _ {c} (k)) ^ {2} \mid \mathcal {Y} _ {t - 1} \right\}\right) \\ \end{array}
$$

and it is assumed that the minimum exists. $E(\cdot |\mathcal{Y}_{t-1})$ is a function of the hyperstate of Eq. (7.10) and $t$ . Define

$$V (\xi (t), t) = \min _ {u (t - 1) \dots u (N - 1)} E \left\{\sum_ {k = t} ^ {N} (y (k) - u _ {c} (k)) ^ {2} \mid \mathcal {Y} _ {t - 1} \right\}$$

$V(\xi(t), t)$ can be interpreted as the minimum expected loss for the remaining part of the control horizon given the data up to t - 1.

Consider the situation at time N - 1. When $u(N - 1)$ is changed, only $y(N)$ will be influenced. This means that we have the same situation as for the one-step minimization. From Eq. (7.16) we get

$$
\begin{array}{l} V (\xi (N), N) \\ = \left(\tilde {\varphi} ^ {T} (N - 1) \hat {x} (N) - u _ {c} (N)\right) ^ {2} + R _ {2} + \tilde {\varphi} ^ {T} (N - 1) P (N) \bar {\varphi} (N - 1) \\ - \frac {\left(\hat {b} _ {0} (N) u _ {c} (N) - \tilde {\varphi} ^ {T} (N - 1) \left(\hat {b} _ {0} (N) \hat {x} (N) + P (N) \ell\right)\right) ^ {2}}{\hat {b} _ {0} ^ {2} (N) + p _ {b _ {0}} (N)} \\ \end{array}
$$

At time $N - 1$ we get

$$
\begin{array}{l} V (\xi (N - 1), N - 1) \\ = \min _ {u (N - 2)} E \left\{\left(y (N - 1) - u _ {c} (N - 1)\right) ^ {2} + V (\xi (N), N) \mid \mathcal {Y} _ {N - 2} \right\} \\ \end{array}
$$

Notice that the minimization is done only over $u(N - 2)$ , since $u(N - 1)$ was eliminated in the previous minimization. This recursively defines the loss at time N - 1, which then can be used for iteration backwards one more step of time, and so on. This dynamic programming procedure leads to a recursive equation, which defines the minimum expected loss. At time t we get

$$V (\xi (t), t) = \min _ {u (t - 1)} E \left\{\left(y (t) - u _ {c} (t)\right) ^ {2} + V (\xi (t + 1), t + 1) \mid \mathcal {Y} _ {t - 1} \right\} \tag {7.17}$$
