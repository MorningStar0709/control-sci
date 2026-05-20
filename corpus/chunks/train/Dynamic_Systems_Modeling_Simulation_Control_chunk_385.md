A more general expression is the maximum overshoot, $M _ { \mathrm { o s } }$ , which is defined as the difference between the peak $( y _ { \mathrm { m a x } } )$ and steady-state $( \boldsymbol { \gamma } _ { \mathrm { s s } } )$ values, normalized by the steady-state value

$$M _ {\mathrm{os}} = \frac {\left| y _ {\max} - y _ {\mathrm{ss}} \right|}{y _ {\mathrm{ss}}} \tag {7.76}$$

In our derivation of the peak output in Eq. (7.75), the steady-state output is unity. Therefore, an equation for maximum overshoot can be obtained by combining Eqs. (7.75) and (7.76) with $y _ { \mathrm { s s } } = 1$

$$M _ {\mathrm{os}} = e ^ {- \zeta \pi / \sqrt {1 - \zeta^ {2}}} \tag {7.77}$$

Now, the peak output for the general case can be written as

$$y _ {\max} = y _ {\mathrm{ss}} (1 + M _ {\mathrm{os}}) \tag {7.78}$$

Peak response and/or maximum overshoot depends only on damping ratio $\zeta$ and does not depend on the undamped natural frequency. The reader should note that when $M _ { \mathrm { o s } } = 0 . 4 5$ , the peak output overshoots its steady-state value by 45%.

The settling time, or time to reach steady state, can be estimated from the exponential envelope term $e ^ { \alpha t }$ in Eq. (7.72). When the envelope term $e ^ { \alpha t } = e ^ { - 4 }$ the transient response has essentially “died $\mathrm { o u t } ^ { \dag }$ as $e ^ { - 4 } = 0 . 0 1 8 3$ , and hence the magnitude of the transient sinusoidal terms are less than 2% of the steady-state response. Settling time $t _ { S }$ for an underdamped system is therefore $t _ { S } = - 4 / \alpha$ , where $\alpha = - \zeta \omega _ { n } \mathrm { , }$ , or

Table 7.4 Performance Equations for the Step Response of an Underdamped Second-Order System

<table><tr><td>Performance Criteria</td><td>Equation</td></tr><tr><td>Peak time,  $t_p$ </td><td> $t_p = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$ </td></tr><tr><td>Maximum overshoot,  $M_{\text{os}}$ </td><td> $M_{\text{os}} = e^{-\zeta \pi / \sqrt{1 - \zeta^2}}$ </td></tr><tr><td>Settling time to steady state,  $t_S$ </td><td> $t_S = \frac{4}{\zeta \omega_n}$ </td></tr><tr><td>Period of oscillation,  $T_{\text{period}}$ </td><td> $T_{\text{period}} = \frac{2\pi}{\omega_n \sqrt{1 - \zeta^2}}$ </td></tr><tr><td>Number of cycles to steady state,  $N_{\text{cycles}}$ </td><td> $N_{\text{cycles}} = \frac{2\sqrt{1 - \zeta^2}}{\pi \zeta}$ </td></tr></table>

$$t _ {S} = \frac {4}{\zeta \omega_ {n}} \tag {7.79}$$
