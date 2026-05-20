![](image/229ff2246f9cd2deab6bd33cf56c597eaa9360289ea6cc4ec2f9ab7f7e432094.jpg)

<details>
<summary>line</summary>

| Time, s | Reference and actual piston position, x(t), cm | Nonlinear and linear EHA responses |
| --- | --- | --- |
| 0.0 | 30 | 30 |
| 0.5 | 40 | 45 |
| 1.0 | 20 | 20 |
| 1.5 | 40 | 45 |
| 2.0 | 20 | 20 |
</details>

Figure 11.46 Closed-loop responses of the nonlinear and linear EHA models with sinusoidal ${ \boldsymbol { x } } _ { \mathrm { r e f } } ( t )$ and proportional gain $K _ { P } = 5 0 0 \mathrm { V / m }$ .

We can use the following MATLAB commands to compute the magnitude and phase of the closed-loop frequency response of the linear EHA model:

$$
\begin{array}{l} > > \mathrm{Kp} = 5 0 0; \\ > > \text {sysT} = \operatorname{tf} (2 6 4 8. 1 5 * \mathrm{Kp}, [ 1 6 3 0 1 2 2 5 0 0 2 6 4 8. 1 5 * \mathrm{Kp} ]) \quad \% \text {closed - loop transfer function} T (s) \\ > > w = 2 * 2 * p i; \\ > > [ \text { mag }, \text { phase } ] = \text { bode } (\text { sysT }, w) \\ \% \text{P - gain} \\ \% \text { closed - loop transfer function } T (s) \\ \% 2 \mathrm{Hz} \text { frequency, rad / s} \\ \% \text{closed - loop freq response} \\ \end{array}
$$

The magnitude and phase are $\mathtt { m a g } \ = \ 0 . 6 7 3 7$ and $\mathtt { p h a s e \ = \ - 5 1 . 4 6 ^ { \circ } \ ( = - 0 . 8 9 8 2 \mathrm { r a d } ) }$ . The magnitude value matches the simulation results shown in Fig. 11.46 because the output/input amplitude ratio is roughly $( 1 0 \mathrm { c m } ) / ( 1 5 \mathrm { c m } ) = 0 . 6 6 6 7$ (note that the amplitude is measured relative to the 30-cm mid-point of the hydraulic cylinder). We can use the phase lag to compute the time lag as $0 . 8 9 8 2 \mathrm { r a d } / ( 4 \pi \mathrm { r a d } / \mathrm { s } ) = 0 . 0 7 2 \mathrm { s } ,$ , which is the time delay between the peaks of the input and output sinusoids in Fig. 11.46.

One way to improve the tracking performance would be to replace the proportional controller with a lead controller. Recall that a lead controller approximates PD control and hence “anticipates” the reference signal due to the derivative term. We can replace the gain $K _ { P }$ in Fig. 11.45 with the following lead controller

$$G _ {C} (s) = \frac {K _ {\mathrm{LF}} (s + 1 0)}{s + 4 0} \tag {11.63}$$
