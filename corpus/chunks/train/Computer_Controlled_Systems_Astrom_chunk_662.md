# The Riccati Equation

Equation (11.17) is called the discrete-time Riccati equation. It is possible to use the Riccati equation to rewrite the loss function of (11.9), which gives the following theorem.

THEOREM 11.2 DISCRETE-TIME RICCATI EQUATION Assume that the Riccati equation of (11.17) has a solution that is nonnegative definite in the interval

$0 \leq k \leq N$ ; then

$$
\begin{array}{l} x ^ {T} (N) Q _ {0} x (N) + \sum_ {k = 0} ^ {N - 1} \left(x ^ {T} (k) Q _ {1} x (k) + u ^ {T} (k) Q _ {2} u (k) + 2 x ^ {T} (k) Q _ {1 2} u (k)\right) \\ = x ^ {T} (0) S (0) x (0) + \sum_ {k = 0} ^ {N - 1} \left(u (k) + L (k) x (k)\right) ^ {T} \\ \times \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) \left(u (k) + L (k) x (k)\right) \\ + \sum_ {k = 0} ^ {N - 1} \left(v ^ {T} (k) S (k + 1) (\Phi x (k) + \Gamma u (k)) + (\Phi x (k) + \Gamma u (k)) ^ {T} S (k + 1) v (k)\right) \\ + \sum_ {k = 0} ^ {N - 1} v ^ {T} (k) S (k + 1) v (k) (11.22) \\ = x ^ {T} (0) S (0) x (0) + \sum_ {k = 0} ^ {N - 1} \left(u (k) + L (k) x (k) + L _ {v} (k) v (k)\right) ^ {T} \\ \times \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) \left(u (k) + L (k) x (k) + L _ {v} (k) v (k)\right) \\ + \sum_ {k = 0} ^ {N - 1} v ^ {T} (k) \left(S (k + 1) - L _ {v} ^ {T} (k) \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) L _ {v} (k)\right) v (k) \\ + \sum_ {k = 0} ^ {N - 1} v ^ {T} (k) S (k + 1) (\Phi - \Gamma L (k)) x (k) \\ + \sum_ {k = 0} ^ {N - 1} x ^ {T} (k) (\Phi - \Gamma L (k)) ^ {T} S (k + 1) v (k) (11.23) \\ \end{array}
$$

where $L(k)$ is defined by (11.19) and

$$L _ {v} (k) = \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) ^ {- 1} \Gamma^ {T} S (k + 1) \tag {11.24}$$

and $x(k + 1)$ is given by (11.3).

Proof. We have the identity

$$
\begin{array}{l} \boldsymbol {x} ^ {T} (N) Q _ {0} \boldsymbol {x} (N) = \boldsymbol {x} ^ {T} (N) S (N) \boldsymbol {x} (N) \\ = x ^ {T} (0) S (0) x (0) + \sum_ {k = 0} ^ {N - 1} \left(x ^ {T} (k + 1) S (k + 1) x (k + 1) - x ^ {T} (k) S (k) x (k)\right) \tag {11.25} \\ \end{array}
$$

Consider the different terms in the sum and use (11.3) and (11.17). Then

$$
\begin{array}{l} x ^ {T} (k + 1) S (k + 1) x (k + 1) \\ = \left(\Phi x (k) + \Gamma u (k) + v (k)\right) ^ {T} S (k + 1) \left(\Phi x (k) + \Gamma u (k) + v (k)\right) \tag {11.26} \\ \end{array}
$$

and

$$
\begin{array}{l} x ^ {T} (k) S (k) x (k) = x ^ {T} (k) \left(\Phi^ {T} S (k + 1) \Phi + Q _ {1} \right. \tag {11.27} \\ \left. - L ^ {T} (k) \left(\Gamma^ {T} S (k + 1) \Gamma + Q _ {2}\right) L (k)\right) x (k) \\ \end{array}
$$

Introducing (11.26) and (11.27) in (11.25) gives
