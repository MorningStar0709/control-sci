- $\| (0.1 / s)W_1(s)T_{de}\|_{\infty} \leq 1, W_1(s) = 10 / (\frac{s}{6} + 1)$ .   
- $\| (0.1 / s)W_1(s)T_{d\theta_i}\|_\infty \leq 1, i = 1,2.$   
$\| (0.1 / s)T_{dF}\|_{\infty}\leq \alpha .$

With $x, \theta_1$ , and $\theta_2$ as measurements, find a design that satisfies the first two specifications while minimizing $\alpha$ , i.e., using the least amount of control. (Do this approximately, by trial and error.) Display the weighted transmission corresponding to the specifications. (It may be necessary to add fictitious noise to the measurements.)

![](image/37a523a4702284fd09837df0b4250fb8fcf2c6e787d3cf686248b7acfeb6cbc4.jpg)

8.18 Maglev This problem addresses the control of the magnetically levitated vehicle of Problem 2.20 (Chapter 2), in the face of guideway elevation changes $z_G$ and wind forces $F_W$ . A model for $z_G$ [7] is obtained by passing a signal of unit norm through $W_G(s) = 0.01 / (s + 0.5)$ . The wind forces may be modeled as the output of a transfer function, $W_w(s) = 1000 / (s + 3)$ , driven by a signal of unit 2-norm.

The design must be such that (i) magnet gaps are kept near their nominal values, (ii) inputs are positive at all times (recall that $u = i^{2}$ ), and (iii) accelerations satisfy the requirements for passenger comfort.

Let $z_{G} = W_{G}w_{1}$ and $F_{W} = W_{W}w_{2}$ . The specifications are as follows:

- $\| 500(\Delta S_{Li} / w_j)\|_\infty \leq 1, i = 1,2, j = 1,2.$   
- $\|500(\Delta S_{GLi}/w_j)\|_\infty \leq 1, i = 1, 2, j = 1, 2.$   
- $\| .01(\Delta u_i / w_j)\|_{\infty} \leq 1, i = 1, 2, 3, 4, j = 1, 2.$   
- $\| W_1(\Delta z / w_1) \|_{\infty} \leq 1$ .   
- $\| 2W_{1}(\Delta y / w_{2})\|_{\infty}\leq 1.$

where $W_{1}(s) = \frac{(s / 6.28 + 1)}{0.0283(s / 39.6 + 1)(s / 163.3 + 1)}$ . (See Example 8.10; $1 / W_{1}$ is an approximation to the TACV ride specification, for vertical motion.)

a. To ascertain feasibility, assume that all state variables (including disturbances $z_{G}$ and $F_{W}$ ) are measured, and compute a controller that meets the specifications. (It will be necessary to assume measurement noise inputs; model these by unit-norm signals passed through small gains.)   
b. If part (a) yields a successful design, try a design that uses the four gap lengths $\Delta S_{L1}$ , $\Delta S_{L2}$ , $\Delta S_{G1}$ , and $\Delta S_{G2}$ as measurements.

In all cases, display the frequency responses corresponding to the specifications.
