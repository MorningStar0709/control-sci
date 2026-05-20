4. Lead compensation may generate large signals in the system. Such large signals are not desirable because they will cause saturation in the system.   
5. Lag compensation reduces the system gain at higher frequencies without reducing the system gain at lower frequencies. Since the system bandwidth is reduced, the system has a slower speed to respond. Because of the reduced high-frequency gain, the total system gain can be increased, and thereby low-frequency gain can be increased and the steady-state accuracy can be improved. Also, any highfrequency noises involved in the system can be attenuated.   
6. Lag compensation will introduce a pole-zero combination near the origin that will generate a long tail with small amplitude in the transient response.   
7. If both fast responses and good static accuracy are desired, a lag–lead compensator may be employed. By use of the lag–lead compensator, the low-frequency gain can be increased (which means an improvement in steady-state accuracy), while at the same time the system bandwidth and stability margins can be increased.   
8. Although a large number of practical compensation tasks can be accomplished with lead, lag, or lag–lead compensators, for complicated systems, simple compensation by use of these compensators may not yield satisfactory results. Then, different compensators having different pole–zero configurations must be employed.

Graphical Comparison. Figure 7–115(a) shows a unit-step response curve and unit-ramp response curve of an uncompensated system. Typical unit-step response and unit-ramp response curves for the compensated system using a lead, lag, and lag–lead compensator, respectively, are shown in Figures 7–115(b), (c), and (d). The system with a lead compensator exhibits the fastest response, while that with a lag compensator exhibits the slowest response, but with marked improvements in the unit-ramp response. The system with a lag–lead compensator will give a compromise; reasonable improvements in both the transient response and steady-state response can be expected. The response curves shown depict the nature of improvements that may be expected from using different types of compensators.

![](image/a2726136264f2d844c30fdd5d625d37e6ad2b91b9c9bc30b93ff7a6a7783043c.jpg)

<details>
<summary>line</summary>

| t | c(t) |
| --- | --- |
| 0 | 0 |
| Peak | 1 |
| Low | 0.5 |
| High | 1 |
</details>
