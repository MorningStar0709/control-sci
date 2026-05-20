<table><tr><td>System Parameter</td><td>Value</td></tr><tr><td>Piston and load mass,  $m$ </td><td>12 kg</td></tr><tr><td>Viscous friction coefficient,  $b$ </td><td>250 N-s/m</td></tr><tr><td>Piston area,  $A$ </td><td> $6.33(10^{-4})$  m $^{2}$ </td></tr><tr><td>Minimum chamber volume,  $V_{0}$ </td><td> $1.64(10^{-4})$  m $^{3}$ </td></tr><tr><td>Piston stroke,  $L$ </td><td>0.6 m</td></tr><tr><td>Supply pressure,  $P_{S}$ </td><td> $17.2(10^{6})$  Pa</td></tr><tr><td>Reservoir (drain) pressure,  $P_{r}$ </td><td> $1.0133(10^{5})$  Pa</td></tr><tr><td>Fluid bulk modulus,  $\beta$ </td><td> $689(10^{6})$  Pa</td></tr><tr><td>Valve discharge coefficient,  $C_{d}$ </td><td>0.62</td></tr><tr><td>Fluid density,  $\rho$ </td><td>875 kg/m $^{3}$ </td></tr><tr><td>Valve orifice height,  $h$ </td><td>0.008 m</td></tr><tr><td>Solenoid–valve undamped natural frequency,  $\omega_{n}$ </td><td>350 rad/s</td></tr><tr><td>Solenoid–valve damping ratio,  $\zeta$ </td><td>0.9</td></tr><tr><td>Solenoid–valve DC gain,  $K_{v}$ </td><td> $2(10^{-5})$  m/V</td></tr></table>

where $\omega _ { n }$ is the undamped natural frequency, $\zeta$ is the damping ratio, and $K _ { \nu }$ is the DC gain of the solenoid. In many cases, we can determine the second-order modeling parameters $\omega _ { n } , \zeta $ , and $K _ { \nu }$ by open-loop experimental trials where we provide a step voltage signal $e _ { \mathrm { i n } } ( t )$ and measure the resulting valve position $y ( t )$ .

Finally, the spool-valve orifice area $A _ { \nu }$ is assumed to be a linear function of spool-valve position y

$$A _ {v} = h | y | \tag {11.42}$$

where h is the height of the valve opening. The absolute value of valve position y must be used because y can be positive (right) or negative (left). Valve orifice area is required in the nonlinear in/out-flow equations (11.39) and (11.40).

Equations (11.34)– (11.42) constitute the complete mathematical model of the EHA. Table 11.5 presents the numerical values for all parameters for the EHA system.
