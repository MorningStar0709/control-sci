# Flight Control Systems

Figure 9.16 shows a block diagram of the pitch channel of a flight control system for a supersonic aircraft. The pitch stick signal is the command signal from the pilot. Position, acceleration, and pitch rate are feedback signals. There are three scheduling variables: height H, indicated airspeed $V_{IAS}$ , and Mach number M. The parameters of the controller that are scheduled are drawn as boxes; the arrows indicate the scheduling variables. The schedule for the gain $K_{QD}$ is given by

$$K _ {Q D} = K _ {Q D _ {I A S}} + (K _ {Q D _ {H}} - K _ {Q D _ {I A S}}) M F$$

where $K_{QD_{IAS}}$ is a function of indicated airspeed $V_{IAS}$ (shown in Fig. 9.17) and $K_{QD_{H}}$ is a function of height (also shown in Fig. 9.17). The variable MF is given by

$$M F = \frac {1}{s + 1} K _ {M F}$$

where $K_{MF}$ is a function of the Mach number and s is the Laplace transform variable.

![](image/c774464eb97e567c4177df96151abaaa05ec32c9f7ed13c4ba00fce84437fbc0.jpg)

<details>
<summary>line</summary>

| V_IAS (km/h) | K_QD_IAS |
| --- | --- |
| 0 | 0.3 |
| 1000 | 0.0 |
</details>

![](image/f75adc9909725fdc28547ee961fbd2929346e2b490978d66791912a1a2b313be.jpg)

<details>
<summary>line</summary>

| H (km) | K_QD_H |
| --- | --- |
| 0 | 0 |
| 10 | ~0.2 |
| 20 | ~0.5 |
</details>

Figure 9.17 Scheduling functions. The function $K_{QD_{IAS}}$ is also different for different flight modes.
