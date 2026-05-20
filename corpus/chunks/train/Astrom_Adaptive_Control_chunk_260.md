# PROBLEMS

4.1 Consider the process and controller in Example 4.4. The controller parameter $\hat{s}_0$ may be very large if $\hat{b}$ is small. Discuss alternatives to ensure that the controller parameter stays bounded.

4.2 Consider the basic direct self-tuning controller in Algorithm 4.1. Discuss different ways to incorporate reference values in the controller. What are the properties of the following three ways for taking care of the reference value?

(a) Use the difference $y - u_{c}$ instead of $y$ in the algorithm, and introduce an integrator in the controller.

(b) Estimate the parameters using the model

$$y (t + d) = R ^ {*} u + S ^ {*} y - T ^ {*} u _ {c} + \varepsilon$$

and let the controller be

$$R ^ {*} u = - S ^ {*} y + T ^ {*} u _ {c}$$

(c) Use the difference $u_{c} - y$ instead of $y$ in the algorithm, and introduce an integrator in the controller.

4.3 Show that the control equation (4.37) minimizes the loss function (4.36).

4.4 Consider the system in Example 4.6. Assume that the process is known. Compute the optimal minimum-variance controller and the least attainable output variance when (a) $\tau = 0.4$ (the minimum-phase case) and (b) $\tau = 0.6$ (the nonminimum-phase case). (Hint: Use Theorem 4.3 for the nonminimum-phase case.)

4.5 Make the same calculations as in Problem 4.4 but for the moving-average controller with $d = 2$ .

4.6 Consider the generalized minimum-variance controller of Eq. (4.37). Compute the closed-loop characteristic equation. Discuss when the design method may give an unstable closed-loop system. For instance, is it useful for the process in Example 4.6 when $\tau = 0.6$ ?

4.7 Consider the process in Example 4.6 when $\tau = 0.6$ and $C = 0$ . Use Eq. (4.67) to compute the closed-loop poles for different values of $N$ when $N_{u} = 1$ .

4.8 Show that the moving-average controller with $B^{+*} = 1$ and d = n corresponds to a state deadbeat controller.

4.9 Consider the process in Example 4.3. Assume that

$$
\begin{array}{l} A (q) = q ^ {2} - 1. 5 q + 0. 7 \\ B (q) = q + b _ {1} \\ C (q) = q ^ {2} - q + 0. 2 \\ \end{array}
$$

Determine the variance of the closed-loop system as a function of $b_{1}$ when the moving-average controller is used. Compare with the lowest achievable variance.

4.10 Show that the control law (4.66) minimizes the loss function (4.65).
