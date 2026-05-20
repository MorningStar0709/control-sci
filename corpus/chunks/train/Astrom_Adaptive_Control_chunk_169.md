The true values are given in parentheses. The controller parameters at time t = 100 are

$$r _ {1} (1 0 0) = 0. 1 1 4 \quad (0. 1 1 1 1) \quad t _ {0} (1 0 0) = 0. 8 6 \quad (0. 8 9 5 1)s _ {0} (1 0 0) = 1. 4 4 \quad (1. 6 4 2 2) \quad s _ {1} (1 0 0) = - 0. 5 8 \quad (- 0. 7 4 7 1)$$

A comparison of Fig. 3.5 and Fig. 3.7 shows that it takes significantly longer for the estimates to converge when no zero is canceled. The reason for this is that the excitation is not as good as when there was “ringing” in the control signal.

There is very little excitation of the system in the periods when the output and the control signals are constant. This explains the steplike behavior of the estimates.

It may seem surprising that the controller already gives the correct steady-state value at time t = 20 when the parameter estimates differ so much from their correct values. The controller parameters are

$$
\begin{array}{l} r _ {1} (2 0) = 0. 0 9 0 \quad (0. 1 1 1 1) \quad t _ {0} (2 0) = 0. 8 3 \quad (0. 8 9 5 1) \\ s _ {0} (2 0) = 1. 1 3 \quad (1. 6 4 2 2) \quad s _ {1} (2 0) = - 0. 2 9 \quad (- 0. 7 4 7 1) \\ \end{array}
$$

Since the process has integral action, we have $A(1) = 0$ . It then follows from Eq. (3.3) that the static gain from command signal to output is

$$\frac {B (1) T (1)}{A (1) R (1) + B (1) S (1)} = \frac {T (1)}{S (1)}$$

To obtain the correct steady-state value, it is thus sufficient that the controller parameters are such that $S(1) = T(1)$ , which in the special case is the same as $t_{0} = s_{0} + s_{1}$ . When no poles are canceled, it follows from Eq. (3.12) that

$$T (1) = A _ {o} (1) B _ {m} ^ {\prime} (1) = A _ {o} (1) \frac {A _ {m} (1)}{\hat {B} (1)}$$

where $\hat{B}$ is the estimated B polynomial. Hence

$$\frac {T (1)}{S (1)} = \frac {A _ {o} (1) A _ {m} (1)}{\hat {B} (1) S (1)} = 1$$

where the last equality follows from Eq. (3.11). Notice that we have $A(1) = 0$ . We thus obtain the rather surprising conclusion that the adaptive controller in this case will automatically have parameters such that there will be no steady-state error.

These examples indicate that the indirect self-tuning algorithm behaves as can be expected and that the estimate of convergence time given by Eq. (3.23) is reasonable. The examples also show the importance of using a good underlying control design. With model-following design it is recommended that cancellation of process zeros is avoided.
