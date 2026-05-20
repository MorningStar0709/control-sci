# ◆ ◆ ◆ REMARK

Different algorithms are used in numerical computation (MATLAB commands acker and place). ♦

To summarize the procedure for pole-placement design:

1. Calculate the determinant and the adjoint of $(sI - A)$ .   
2. Compute the desired closed-loop characteristic polynomial.   
3. Apply Equation 7.18 to generate linear equations for the gain components.   
4. Calculate the dc steady state ( $x^{*}$ and $u^{*}$ ) in terms of the desired output.   
5. Obtain the control law $u = u^{*} - \mathbf{k}^{T}(\mathbf{x} - \mathbf{x}^{*})$ .   
7. If the transfer function $y / y_{d}$ is desired, it has the same zeros as the plant, and the specified closed-loop poles. Furthermore, since the state tends to the dc steady

state that yields $y_{d}$ as the output, $y$ tends to $y_{d}$ for constant $y_{d}$ , so the transfer function $y / y_{d} = 1$ at $s = 0$ . This fact is used to calculate the gain.

8. If the time response is desired, use the procedure indicated by Equations 7.8 and 7.9.
