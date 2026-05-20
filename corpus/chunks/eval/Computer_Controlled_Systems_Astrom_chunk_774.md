12.33 Consider the process in Example 12.9. Compute the output variance when the controller does not cancel the zero, that is, when the controller is obtained from the identity

$$z C = A R + B S$$

Compare the variances.

12.34 Consider the process in Example 12.9. Compute the controller that minimizes the loss function (12.7).

12.35 Show that a system with the input-output description

$$A (q) y (k) = B (q) u (k) + C (q) e (k)$$

where

$$A (q) = q ^ {n} + a _ {1} q ^ {n - 1} + \dots + a _ {n}B (q) = b _ {1} q ^ {n - 1} + \dots + b _ {n}C (q) = q ^ {n} + c _ {1} q ^ {n - 1} + \dots + c _ {n}$$

has the following state-space description

$$x (k + 1) = \Phi x (k) + \Gamma u (k) + K e (k + 1)y (k) = C x (k)$$

where the state vector has dimension $n + 1$ and

$$
\Phi = \left( \begin{array}{c c c c c} {- a _ {1}} & {1} & {0} & {\dots} & {0} \\ {- a _ {2}} & {0} & {1} & {\dots} & {0} \\ {\vdots} & {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {- a _ {n}} & {0} & {0} & {\dots} & {1} \\ {0} & {0} & {0} & {\cdot} & {0} \end{array} \right) \quad \Gamma = \left( \begin{array}{c} {b _ {1}} \\ {b _ {2}} \\ {\vdots} \\ {b _ {n}} \\ {0} \end{array} \right) \quad K = \left( \begin{array}{c} {1} \\ {c _ {1}} \\ {\vdots} \\ {c _ {n - 1}} \\ {c _ {n}} \end{array} \right)

C = \left( \begin{array}{c c c c c} 1 & 0 & 0 & \dots & 0 \end{array} \right)
$$

12.36 Consider the system in Problem 12.35. Assume that the polynomial $C(z)$ has all its zeros inside the unit disc. Show that the Kalman filter for the system can be written as

$$\hat {x} (k + 1 \mid k) = \Phi \hat {x} (k \mid k) + \Gamma u (k)\hat {x} (k + 1 \mid k + 1) = \hat {x} (k + 1 \mid k) + K \left(y (k + 1) - C \hat {x} (k + 1 \mid k)\right)$$

and that the characteristic polynomial of the filter is $zC(z)$ .

12.37 Consider the system in Problem 12.35. Assume that minimization of a quadratic loss function gives the feedback law

$$u (k) = - L \hat {x} (k \mid k)$$

Show that the controller has the pulse-transfer function

$$H _ {c} (z) = z L \left(z I - (I - K C) (\Phi - \Gamma L)\right) ^ {- 1} \Gamma$$

Show that the results are the same as those given by

$$H _ {c} (z) = L _ {v} (\Phi - K C) \left(z I - \left(I - \Gamma L _ {v}\right) (\Phi - K C)\right) ^ {- 1} \left(I - \Gamma L _ {v}\right) K + L _ {v} K \tag {12.76}= z L _ {v} \left(z I - (\Phi - K C) (I - \Gamma L _ {v})\right) ^ {- 1} K$$
