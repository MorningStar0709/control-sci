| ω in rad/sec | dB (Top Line) | dB (Bottom Line) |
| --- | --- | --- |
| 0.001/T₁ | 0 | 0 |
| 0.01/T₁ | 0 | -5 |
| 0.1/T₁ | -20 | -75 |
| 1/T₁ | -20 | 0 |
| 10/T₁ | 0 | 5 |
| 100/T₁ | 0 | 0 |
</details>

Lag–Lead Compensation Based on the Frequency-Response Approach. The design of a lag–lead compensator by the frequency-response approach is based on the combination of the design techniques discussed under lead compensation and lag compensation.

Let us assume that the lag–lead compensator is of the following form:

$$G _ {c} (s) = K _ {c} \frac {\left(T _ {1} s + 1\right) \left(T _ {2} s + 1\right)}{\left(\frac {T _ {1}}{\beta} s + 1\right) \left(\beta T _ {2} s + 1\right)} = K _ {c} \frac {\left(s + \frac {1}{T _ {1}}\right) \left(s + \frac {1}{T _ {2}}\right)}{\left(s + \frac {\beta}{T _ {1}}\right) \left(s + \frac {1}{\beta T _ {2}}\right)} \tag {7-28}$$

where $\beta > 1$ . The phase-lead portion of the lag–lead compensator (the portion involving $T _ { 1 } )$ alters the frequency-response curve by adding phase-lead angle and increasing the phase margin at the gain crossover frequency.The phase-lag portion (the portion involving $T _ { 2 } )$ provides attenuation near and above the gain crossover frequency and thereby allows an increase of gain at the low-frequency range to improve the steady-state performance.

We shall illustrate the details of the procedures for designing a lag–lead compensator by an example.
