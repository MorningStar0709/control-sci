# Compatible Criteria for Identification and Control

So far, we have treated identification and control as two different tasks. The criterion for the identification (least squares) was chosen largely on an ad hoc basis. It is clearly desirable to try to find a criterion for identification that matches the final use of the model. This is in general a very complicated problem. We therefore discuss a simplified case. Consider a process described by the model

$$A (q) y (t) = B (q) u (t) \tag {11.39}$$

where u is the control signal and y is the measured variable. Let the controller be

$$R (q) u (t) = T (q) u _ {c} (t) - S (q) y (t) \tag {11.40}$$

where $u_{c}$ is the setpoint and $R(q)$ , $S(q)$ , and $T(q)$ are polynomials. The polynomials $R(q)$ and $S(q)$ satisfy the Diophantine equation

$$A (q) R (q) + B (q) S (q) = A _ {m} (q) A _ {o} (q) \tag {11.41}$$

where the desired closed-loop polynomial is $A_{o}(q)A_{m}(q)$ . This equation has many solutions. It is customary to choose the simplest one that gives a causal controller, but it is also possible to introduce an auxiliary condition. Integral action is obtained by finding a solution such that $R(1)=0$ . High-frequency roll-off is obtained by requiring that $S(-1)=0$ .

The polynomial $T(q)$ is given by

$$T (q) = t _ {0} A _ {\mathrm{o}} (q) \tag {11.42}$$

where $t_0 = A_m(1) / B(1)$ . If $R(1) = 0$ , it also follows that $T(1) = S(1)$ . Combining Eqs. (11.39) and (11.40), we get

$$y (t) = t _ {0} \frac {B (q)}{A _ {m} (q)} u _ {c} (t) \tag {11.43}u (t) = t _ {0} \frac {A (q)}{A _ {m} (q)} u _ {c} (t)$$

Polynomials $A_{o}(q)$ and $A_{m}(q)$ are typically chosen to give good rejection of disturbances and insensitivity to modeling errors and measurement noise.

It is desirable to formulate the adaptive control problem in such a way that the goals for control and identification are compatible. If this is done, it means that a model is fitted in such a way that it matches the ultimate use of of the model.
