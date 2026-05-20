# Example 7.7 (Pendulum on a Cart)

For the linearized model of the pendulum and cart of Example 2.9 using the numerical values of Example 2.5 (Chapter 2), design an optimal LQ feedback to regulate to the vertical equilibrium with $x = 0$ . For an initial state $\theta = 15^{\circ}$ , $\omega = x = v = 0$ , the transient should be such that $|x(t)| \leq 0.5 \, \text{m}$ and $|\theta(t)| \leq 20^{\circ} = 0.35 \, \text{rad}$ . Simulate the transient response for this control system used on the nonlinear model of Example 2.9, with different initial state values, to explore the applicability of the linear design.

Solution The $A$ and $B$ matrices are as in Example 7.3. We must carry out a trial-and-error process to choose the proper weights. (Note that there is no guarantee that the specifications can be met, even by the optimal system; they may need to be relaxed.)

One way to begin the process is to use weights that normalize the variables with respect to their largest permissible values. Thus, we try

$$J = \int_ {0} ^ {\infty} \left[ \left(\frac {x}{x _ {\max}}\right) ^ {2} + \left(\frac {\theta}{\theta_ {\max}}\right) ^ {2} + \left(\frac {F}{F _ {\max}}\right) ^ {2} \right] d t$$

where $x_{max} = 0.5 \, m$ and $\theta_{max} = 0.35 \, rad$ . The value of $F_{max}$ is not specified. A reasonable order of magnitude is the force required to hold the cart and pendulum against gravity—say, $F_{\text{max}} = (M + m)g = 20 \, \text{N}$ .

From the integral, we see that $Q_{11} = 1 / x_{\max}^2$ , $Q_{33} = 1 / \theta_{\max}^2$ , and $R = 1 / F_{\max}^2$ . (This assumes that the states are ordered within the state vector as in Example 7.3.) All other elements of $Q$ are zero.

Figure 7.10 shows the transient responses for $x(t)$ and $\theta(t)$ (MATLAB lqr, initial); it turns out that the initial guesses for $Q$ and $R$ are satisfactory. The responses should be compared to those obtained by pole placement in Example 7.3. The LQ responses are somewhat faster, and the maximum distance excursion of the cart is lessened.
