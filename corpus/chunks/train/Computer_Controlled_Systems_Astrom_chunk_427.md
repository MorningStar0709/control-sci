# Example 7.1 Aliasing

Figure 7.9 is a process diagram of feed-water heating in a boiler of a ship. A valve controls the flow of water. There is a backlash in the valve positioner due to wear. This causes the temperature and the pressure to oscillate. Figure 7.10 shows a sampled recording of the temperature and a continuous recording of the pressure.

From the temperature recording one might believe that there is an oscillation with a period of about 38 min. The pressure recording reveals, however, that the oscillation in pressure has a period of 2.11 min. Physically the two variables are coupled and should oscillate with the same frequency.

The temperature is sampled every other minute. The sampling frequency is $\omega_{s} = 2\pi/2 = 3.142$ rad/min and the frequency of the pressure oscillation is $\omega_{0} = 2\pi/2.11 = 2.978$ rad/min. The lowest aliasing frequency is $\omega_{s} - \omega_{0} = 0.1638$ rad/min. This corresponds to a period of 38 min, which is the period of the recorded oscillation in the temperature.

![](image/7feca7e757bd8fe000ddba6d5e5a7c09993df137f7e93e479e4182d4c87d71d1.jpg)

<details>
<summary>line</summary>

| Time | Temperature | Pressure |
| --- | --- | --- |
| 0 | 38 | 2.11 |
| 2 | 2 | 2.11 |
</details>

Figure 7.10 Recordings of temperature and pressure.

![](image/efb5a0924c887894f0cfe550c41b1ff25e75819bb186826a3e5b484057bdfe99.jpg)  
Figure 7.11 Frequency folding.
