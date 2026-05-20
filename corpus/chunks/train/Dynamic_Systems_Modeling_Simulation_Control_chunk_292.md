Supply pressure
Drain
Return spring
Electromagnetic force, f(t)
Spool-valve mass, m
y
Fluid flow
</details>

Figure 6.3 Three-way spool valve for Example 6.2.

![](image/383470d6cb03a8c3ccda342210f1a6aefe9727a2314a5db357252a047a263f51.jpg)

<details>
<summary>line</summary>

| Time, s | Spool-valve position, y(t), m (×10⁻³) |
| --- | --- |
| 0.00 | 0.000 |
| 0.02 | 0.000 |
| 0.03 | 2.000 |
| 0.04 | 1.700 |
| 0.06 | 1.750 |
| 0.07 | -0.400 |
| 0.08 | 0.100 |
| 0.10 | 0.000 |
</details>

Figure 6.4 Spool-valve response to a 12-N pulse force (Example 6.2).

MATLAB’s plot command can be used to create the plot of y(t) shown in Fig. 6.4. Note that valve position begins at zero (its initial condition), responds to the 12-N step force applied at t = 0.02 s, reaches a peak response of about 0.002 m (2 mm), and finally settles to a constant displacement of 0.0017 m (1.7 mm). At time t = 0.06 s the applied force is instantly stepped to zero and it is clear that the valve responds in a reversed but symmetric manner as it returns to the zero position.
