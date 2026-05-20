# Example 11.1 LQ-control of the double integrator

Consider the double integrator (see Example A.1) and use the sampling period $h = 1$ . Let the weighting matrices in (11.9) be

$$
Q _ {1} = \left( \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right) \quad \text { and } \quad Q _ {2} = \left(\rho\right)
$$

The influence of the weighting can now be investigated. The stationary feedback vector has been calculated for different values of $\rho$ . Figure 11.2 shows the states and the control signal for some values. When $\rho = 0$ , which means there is a penalty only on the output, then the resulting controller is the same as the deadbeat controller in Sec. 4.3. When $\rho$ is increased, then the magnitude of the control signal is decreased.

Figure 11.3 shows the stationary L vector as a function of the control weighting $\rho$ . When $\rho$ increases the gains go to zero and there will be almost no feedback.
