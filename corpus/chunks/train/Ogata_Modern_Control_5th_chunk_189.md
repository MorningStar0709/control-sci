The unit-ramp input and the system output are shown in Figure 5–3. The error in following the unit-ramp input is equal to T for sufficiently large t. The smaller the time constant T, the smaller the steady-state error in following the ramp input.

Unit-Impulse Response of First-Order Systems. For the unit-impulse input, R(s)=1 and the output of the system of Figure 5–1(a) can be obtained as

$$C (s) = \frac {1}{T s + 1} \tag {5-7}$$

The inverse Laplace transform of Equation (5–7) gives

$$c (t) = \frac {1}{T} e ^ {- t / T}, \quad \text { for } t \geq 0 \tag {5-8}$$

The response curve given by Equation (5–8) is shown in Figure 5–4.

![](image/486b1d5335dc77f8ef827be6a3cf8214f2157bee42a1a8fe4fbd4d73b3f13989.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 1/T |
| T | (estimated) |
| 2T | (estimated) |
| 3T | (estimated) |
| 4T | (estimated) |
</details>

Figure 5–4 Unit-impulse response of the system shown in Figure 5–1(a).

An Important Property of Linear Time-Invariant Systems. In the analysis above, it has been shown that for the unit-ramp input the output c(t) is

$$c (t) = t - T + T e ^ {- t / T}, \quad \text { for } t \geq 0 \quad \text { [See Equation (5 - 6).] }$$

For the unit-step input, which is the derivative of unit-ramp input, the output c(t) is

$$c (t) = 1 - e ^ {- t / T}, \quad \text { for } t \geq 0 \quad \text { [See Equation (5 - 3).] }$$

Finally, for the unit-impulse input, which is the derivative of unit-step input, the output c(t) is

$$c (t) = \frac {1}{T} e ^ {- t / T}, \quad \text { for } t \geq 0 \quad [ \text { See Equation(5 - - 8). } ]$$

Comparing the system responses to these three inputs clearly indicates that the response to the derivative of an input signal can be obtained by differentiating the response of the system to the original signal. It can also be seen that the response to the integral of the original signal can be obtained by integrating the response of the system to the original signal and by determining the integration constant from the zero-output initial condition. This is a property of linear time-invariant systems. Linear time-varying systems and nonlinear systems do not possess this property.
