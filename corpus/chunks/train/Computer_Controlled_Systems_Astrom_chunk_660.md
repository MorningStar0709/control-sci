Proof. To prove the theorem, dynamic programming will be used. We start from the end point and iterate backwards in time. See Fig. 11.1. Introduce

$$
\begin{array}{l} V _ {k} = \min _ {u (k), \dots , u (N - 1)} \left(\sum_ {i = k} ^ {N - 1} \left(x ^ {T} (i) Q _ {1} x (i) + u ^ {T} (i) Q _ {2} u (i) + 2 x ^ {T} (i) Q _ {1 2} u (i)\right) \right. \\ \left. + x ^ {T} (N) Q _ {0} x (N)\right) \\ \end{array}
$$

$V_{k}$ can be interpreted as the loss from k to N (loss-to-go) and is a function of the state $x(k)$ at time k. For k = N we have

$$V _ {N} = x ^ {T} (N) S (N) x (N)$$

where

$$S (N) = Q _ {0}$$

We will now show that $V_{k}$ will be quadratic in $x(k)$ for all $k$ . For $k = N - 1$ ,

$$V _ {N - 1} = \min _ {u (N - 1)} \left(x ^ {T} (N - 1) Q _ {1} x (N - 1) + u ^ {T} (N - 1) Q _ {2} u (N - 1) \right. \tag {11.20}\left. + 2 x ^ {T} (N - 1) Q _ {1 2} u (N - 1) + V _ {N}\right)$$

Using (11.16) for $k = N - 1$ gives

$$
\begin{array}{l} V _ {N - 1} = \min _ {u (N - 1)} \left(x ^ {T} (N - 1) Q _ {1} x (N - 1) + u ^ {T} (N - 1) Q _ {2} u (N - 1) \right. \\ + 2 x ^ {T} (N - 1) Q _ {1 2} u (N - 1) \\ \left. + \left(\Phi x (N - 1) + \Gamma u (N - 1)\right) ^ {T} S (N) \left(\Phi x (N - 1) + \Gamma u (N - 1)\right)\right) \\ = \min _ {u (N - 1)} \left(x ^ {T} (N - 1) \left(Q _ {1} + \Phi^ {T} S (N) \Phi\right) x (N - 1) \right. \\ + x ^ {T} (N - 1) \left(\Phi^ {T} S (N) \Gamma + Q _ {1 2}\right) u (N - 1) \\ + u ^ {T} (N - 1) \left(\Gamma^ {T} S (N) \Phi + Q _ {1 2} ^ {T}\right) x (N - 1) \\ \left. + u ^ {T} (N - 1) \left(\Gamma^ {T} S (N) \Gamma + Q _ {2}\right) u (N - 1)\right) \\ = \min _ {u (N - 1)} \left( \begin{array}{l l} x ^ {T} (N - 1) & u ^ {T} (N - 1) \end{array} \right) \\ \times \left( \begin{array}{c c} Q _ {1} + \Phi^ {T} S (N) \Phi & \Gamma^ {T} S (N) \Phi + Q _ {1 2} ^ {T} \\ \Phi^ {T} S (N) \Gamma + Q _ {1 2} & \Gamma^ {T} S (N) \Gamma + Q _ {2} \end{array} \right) \binom{x (N - 1)}{u (N - 1)} \\ \end{array}
$$

This is a function that is quadratic in $u(N - 1)$ . By using (11.14) and (11.15), the control law

$$u (N - 1) = - L (N - 1) x (N - 1)$$

gives the minimum loss

$$V _ {N - 1} = x ^ {T} (N - 1) S (N - 1) x (N - 1)$$

which is quadratic in $x(N - 1)$ and where

$$S (N - 1) = \Phi^ {T} S (N) \Phi + Q _ {1} - L ^ {T} (N - 1) \left(Q _ {2} + \Gamma^ {T} S (N) \Gamma\right) L (N - 1)$$

and

$$L (N - 1) = \left(Q _ {2} + \Gamma^ {T} S (N) \Gamma\right) ^ {- 1} \left(\Gamma^ {T} S (N) \Phi + Q _ {1 2} ^ {T}\right)$$

Because $V_{N-1}$ is positive semidefinite, so is its minimum, that is, $S(N - 1)$ is positive semidefinite. Dynamic programming now gives
