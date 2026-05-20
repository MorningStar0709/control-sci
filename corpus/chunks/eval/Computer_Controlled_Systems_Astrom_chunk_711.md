# Minimum-Variance Control: An Example

The optimal-control problem defined by the model of (12.5) and the criterion of (12.6) is solved in a special case. The solution, which is easily obtained from first principles, gives good insight into the assumptions made. It also indicates how the general problem should be solved.

Consider the first-order system

$$y (k + 1) + a y (k) = b u (k) + e (k + 1) + c e (k) \tag {12.9}$$

where $|c| < 1$ and $e(k)$ is a sequence of independent random variables with unit variance.

Consider the situation at time k. The outputs $y(k)$ , $y(k-1)$ , ... have been observed. The control $u(k)$ should be determined so that the output is as close to zero as possible. It follows from (12.9) that $y(k + 1)$ may be changed arbitrarily by a proper choice of $u(k)$ . Because $e(k + 1)$ is independent of $y(k)$ and of the terms of the right-hand side of (12.9), it follows that

$$\operatorname{var} y (k + 1) \geq \operatorname{var} e (k + 1) = 1 \tag {12.10}$$

The term $e(k)$ may be computed in terms of the known data $y(k), y(k-1), \ldots$ and $u(k-1), u(k-2), \ldots$ . When the variables $y(k)$ and $e(k)$ are known, the control law

$$u (k) = \left(a y (k) - c e (k)\right) / b \tag {12.11}$$

gives

$$y (k + 1) = e (k + 1) \tag {12.12}$$

which corresponds to the lower bound in (12.10). If the control law in (12.11) is used in each step, Eq. (12.12) holds for all k. The computation of $e(k)$ from the data available at time k is then trivial and the control law in (12.11) can be written as

$$u (k) = - \frac {c - a}{b} y (k) \tag {12.13}$$

The optimal control is thus a proportional feedback with the gain $(c - a)/b$ .

To analyze the properties of the closed-loop system under optimal control, eliminate u between (12.9) and (12.13). This gives

$$y (k + 1) + c y (k) = e (k + 1) + c e (k)$$

Notice that the closed-loop system has the characteristic polynomial

$$C (z) = z + c$$

This shows the importance of the assumption that the polynomial $C(z)$ is stable. This difference equation has the solution

$$y (k) = e (k) + (- c) ^ {k - k _ {0}} \left(y \left(k _ {0}\right) - e \left(k _ {0}\right)\right)$$

Because c is less than one in magnitude, the last term goes to zero as $k - k_{0}$ increases toward infinity. Thus control law in (12.13) gives the minimum-variance in steady state.
