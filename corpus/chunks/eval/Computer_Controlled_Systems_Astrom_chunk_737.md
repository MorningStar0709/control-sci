# Properties of the State-Space Solution

The problems discussed in this chapter was solved using state-space methods in Chapter 11. A stata-space representation of the model of (12.5) is first given. For this purpose it is assumed that the model is normalized, so that $\deg C(z) = \deg A(z)$ . The model of (12.5) can then be represented as

$$x (k + 1) = \Phi x (k) + \Gamma u (k) + K e (k)y (k) = C x (k) + e (k)$$

where

$$
\begin{array}{l} \Phi = \left( \begin{array}{c c c c c} - a _ {1} & 1 & 0 & \dots & 0 \\ - a _ {2} & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ - a _ {n - 1} & 0 & 0 & \dots & 1 \\ - a _ {n} & 0 & 0 & \dots & 0 \end{array} \right) \\ \Gamma = \left( \begin{array}{c} b _ {1} \\ b _ {2} \\ \vdots \\ b _ {n - 1} \\ b _ {n} \end{array} \right) \\ K = \left( \begin{array}{c} c _ {1} - a _ {1} \\ c _ {2} - a _ {2} \\ \vdots \\ c _ {n - 1} - a _ {n - 1} \\ c _ {n} - a _ {n} \end{array} \right) \\ C = \left( \begin{array}{l l l l} 1 & 0 & \dots & 0 \end{array} \right) \tag {12.38} \\ \end{array}
$$

Because this is an innovations representation if the matrix $\Phi - KC$ has all its eigenvalues inside the unit disc. The steady-state Kalman filter is then obtained by inspection:

$$\hat {x} (k + 1 \mid k) = \Phi \hat {x} (k \mid k - 1) + \Gamma u (k) + K (y (k) - C \hat {x} (k \mid k - 1)) \tag {12.39}$$

The Kalman filter has the characteristic polynomial

$$\det \left(z I - (\Phi - K C)\right) = C (z) \tag {12.40}$$

This implies that $C(z)$ are some of the closed-loop poles. Assume a computational delay of one sampling period in the control law. The optimal control law is then

$$u (k) = - L \hat {x} (k \mid k - 1)$$

and the transfer function of the controller is

$$H _ {r} (z) = - L (z I - \Phi + K C + \Gamma L) ^ {- 1} K = - \frac {S (z)}{R (z)} \tag {12.41}$$

where $R(z) = \det(zI - \Phi + KC + \Gamma L)$ , $\deg R(z) = n$ , and $\deg S(z) < n$ . It follows from this discussion and Sec. 11.4 that the closed-loop poles are $C(z)$ and

$$P (z) = \det (z I - \Phi + \Gamma L)$$

where $P(z)$ is obtained from the algebraic Riccati equation.

It is more complicated to derive the control law when the admissible control is such that $u(k)$ is a function of $y(k), y(k-1), \ldots$ . The loss function (12.8) corresponds to (11.9) with $Q_{1} = C^{T}C$ , $Q_{12} = 0$ , and $Q_{2} = \rho$ . From (11.19) and (11.24) it follows that $L = L_{v}\Phi$ . The results from state-space theory (Remark 2 of Theorem 11.7) show that the control law is
