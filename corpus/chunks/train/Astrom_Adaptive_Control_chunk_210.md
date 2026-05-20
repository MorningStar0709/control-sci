where Eq. (4.9) has been used to obtain the last equality. The polynomials $qG$ , $qBF$ , and $C$ are all of degree $n$ . This implies that we have divided $y(t + d_0)$ in two parts. The first part, $F(q)e(t + 1)$ , depends on the noise acting on the system from $t + 1, \ldots, t + d_0$ . The second part,

$$\hat {y} (t + d _ {0} | t) = \frac {q B F}{C} u (t) + \frac {q G}{C} y (t) \tag {4.13}$$

depends on measured outputs and applied inputs, including the $u(t)$ that we want to determine. From Eqs. (4.12) it follows that $\hat{y}(t + d_{0}|t)$ is the mean square prediction of $y(t + d_{0})$ given data up to and including time t. The prediction error is given by

$$\bar {y} (t + d _ {0} | t) = y (t + d _ {0}) - \hat {y} (t + d _ {0} | t) = F (q) e (t + 1)$$

and the variance of the prediction error is

$$\operatorname{var} \tilde {y} (t + d _ {0} | t) = \sigma^ {2} (1 + f _ {1} ^ {2} + f _ {2} ^ {2} + \dots + f _ {d _ {0} - 1} ^ {2})$$

Minimum variance of the output is now obtained by the control law

$$u (t) = - \frac {G (q)}{B (q) F (q)} y (t) \tag {4.14}$$

Using this controller gives

$$
\begin{array}{l} y (t + d _ {0}) = F (q) e (t + 1) \\ = e \left(t + d _ {0}\right) + f _ {1} e \left(t + d _ {0} - 1\right) + \dots + f _ {d _ {0} - 1} e (t + 1) \tag {4.15} \\ \end{array}
$$

and the minimum output variance is

$$\operatorname{var} y (t) = \sigma^ {2} \left(1 + f _ {1} ^ {2} + f _ {2} ^ {2} + \dots + f _ {d _ {0} - 1} ^ {2}\right)$$

which is the same as the variance of the prediction error. Using the controller (4.14) gives the closed-loop characteristic equation

$$q ^ {d _ {0} - 1} C (q) B (q) = 0$$

This implies that there are $d_{0}-1$ poles at the origin, n poles at the zeros of the C polynomial, which are inside the unit disc, and $n-d_{0}$ poles at the zeros of the B polynomial. Since the system was assumed to be minimum-phase, these poles are also inside the unit disc. Observe that minimum-variance control is the same as predicting the output $d_{0}$ steps ahead and then choosing the control signal such that the predicted value is equal to the desired reference value. See Fig. 4.1.

The minimum-variance controller can be interpreted as a pole placement controller, which was discussed in Section 3.2. This is seen by multiplying Eq. (4.9) by B, that is,

$$q ^ {d _ {0} - 1} C B = A R + B S \tag {4.16}$$

where

$$R = B F\boldsymbol {S} = \boldsymbol {G}$$

The pole placement design leads to the controller

$$u (t) = - \frac {S}{R} y (t) = - \frac {G}{B F} y (t)$$
