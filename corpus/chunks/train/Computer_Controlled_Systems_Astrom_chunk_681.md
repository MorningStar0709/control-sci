# The Filter Problem

The predictor in (11.43) has the property that the state at time k is reconstructed from $y(k-1)$ , $y(k-2)$ , .... It is also possible to derive the filter, which also uses $y(k)$ , to estimate $x(k)$ . In the filter case $y(k)$ will contain information about $v(k)$ , which will be reflected in the equations that follow.

THEOREM 11.6 KALMAN FILTER-FILTER CASE Consider the process (11.3) and let $Y_{k}$ be available for the estimation of $x(k)$ . If the matrix $R_{2} + CP(k|k - 1)C^{T}$ is positive definite then the optimal filter is given by the following equations:

$$
\hat {x} (k \mid k) = \hat {x} (k \mid k - 1) + K _ {f} (k) \left(y (k) - C \hat {x} (k \mid k - 1)\right)\hat {v} (k \mid k) = K _ {v} (k) \left(y (k) - C \hat {x} (k \mid k - 1)\right) \tag {11.50}
\begin{array}{l} \hat {x} (k + 1 \mid k) = \Phi \hat {x} (k \mid k) + \Gamma u (k) + \hat {v} (k \mid k) \\ = \Phi \hat {x} (k \mid k - 1) + \Gamma u (k) + K (k) (y (k) - C \hat {x} (k \mid k - 1)) \\ \end{array}
$$

where

$$
K _ {f} (k) = P (k \mid k - 1) C ^ {T} \left(C P (k \mid k - 1) C ^ {T} + R _ {2}\right) ^ {- 1} \tag {11.51}K _ {v} (k) = R _ {1 2} \left(C P (k \mid k - 1) C ^ {T} + R _ {2}\right) ^ {- 1} \tag {11.52}
\begin{array}{l} K (k) = \Phi K _ {f} (k) + K _ {v} (k) \\ = \left(\Phi P (k \mid k - 1) C ^ {T} + R _ {1 2}\right) \left(C P (k \mid k - 1) C ^ {T} + R _ {2}\right) ^ {- 1} \tag {11.53} \\ \end{array}
$$

The variance is given by the Riccati equation

$$
\begin{array}{l} P (k + 1 \mid k) = \Phi P (k \mid k - 1) \Phi^ {T} + R _ {1} \\ - K (k) \left(C P (k \mid k - 1) C ^ {T} + R _ {2}\right) K ^ {T} (k) \\ P (k \mid k) = P (k \mid k - 1) \\ - P (k \mid k - 1) C ^ {T} \left(C P (k \mid k - 1) C ^ {T} + R _ {2}\right) ^ {- 1} C P (k \mid k - 1) \\ P (0 \mid - 1) = R _ {0} \tag {11.54} \\ \end{array}

\begin{array}{l} P (k \mid k) = P (k \mid k - 1) \\ - P (k \mid k - 1) C ^ {T} \left(C P (k \mid k - 1) C ^ {T} + R _ {2}\right) ^ {- 1} C P (k \mid k - 1) \\ \end{array}
$$

Proof. The proof is based on expressions analogous to (11.45).

Remark 1. The notation $P(k \mid k - 1)$ is used here instead of $P(k)$ to specify the available data; $P(k \mid k)$ is the variance of the estimation error at time $k$ given $Y_k$ .

Remark 2. Notice that the expression for $\hat{x}(k + 1 \mid k)$ in (11.50) is the same as in (11.43).

Remark 3. Notice that $\hat{v}(k + 1 \mid k) = 0$ because $y(k)$ does not contain any information about $v(k + 1)$ .
