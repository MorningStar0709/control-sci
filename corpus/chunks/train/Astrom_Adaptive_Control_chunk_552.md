# EXAMPLE 8.2 Auto-tuning of cascaded tanks

The properties of a relay auto-tuner are illustrated by an example. The process to be controlled consists of three cascaded tanks. The level of the lower tank is measured, and the control variable is the voltage to the amplifier driving the pump for the inlet. The signals are noisy. The relay in the auto-tuner has a hysteresis, which is determined automatically on the basis of measurements of the process disturbances. The relay amplitude is also adjusted automatically to keep a specified amplitude of the limit cycle. The limit cycle is judged to be stationary by measuring the periods and amplitudes of two positive half-periods. Figure 8.7 shows the process inputs and outputs in one experiment, illustrating the effect of amplitude adjustment. When the tuning is finished, the regulator is switched to PID control automatically. A change of the setpoint shows that the tuning has been successful.

![](image/9c54e523e7b2b06ec3714368f3964e1afb2792c21813adc7d04fb4c256bf1c39.jpg)

<details>
<summary>line</summary>

| Time (s) | Tuning Signal | PID Control Signal |
| --- | --- | --- |
| 0 | y | u_c |
| 200 | u | u |
</details>

Figure 8.7 Results obtained by applying an auto-tuner to level control of three cascaded tanks.
