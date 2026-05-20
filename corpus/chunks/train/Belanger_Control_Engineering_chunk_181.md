# 4.2.2 Time-Domain Specifications

A time-domain specification describes the characteristics of the response (output or error) to a given set point or to disturbance time functions. Those functions may be specific to the particular application—for example, the set of signals used by an aircraft control system for typical maneuvers. In the absence of such specific signals, a unit step is often used as a test input. Figure 4.5 shows the output response $y(t)$ to a unit step in $y_{d}(t)$ (stability is assumed). Specifications are given in terms of the following features of the response:

1. The steady-state error, $e_{ss}$ . This is the difference between the desired final value, 1.0, and the final value of $y(t)$ .   
2. The delay time $T_{d}$ , defined as the time required for the response to reach 50% of its final value (the percentage may vary according to the application).   
3. The rise time $T_{r}$ , defined as the time required for the response to go from 10% to 90% of its final value.

![](image/fb0646cac68d23f8dc574d6f442e83154210ac5743c778debd0b629d2242eaa7.jpg)

<details>
<summary>line</summary>

| Time(s) | Response |
| --- | --- |
| 0 | 0 |
| 2 | 0.5 |
| 4 | 1.1 |
| 6 | 0.9 |
| 8 | 0.9 |
| 10 | 0.95 |
| 12 | 0.95 |
| 14 | 0.95 |
</details>

Figure 4.5 The step response and its main parameters

4. The percent peak overshoot, defined from the maximum value of the response as a percentage of the final value. More precisely, with reference to Figure 4.5, the percent overshoot is $100(y_{p} - y_{ss}) / y_{ss}$ .   
5. The settling time $T_{s}$ , defined as the time at which the response enters for the last time a $\pm 5\%$ band about the final value.

In the next chapter we shall address the question of time-domain specifications more fully and explore connections with the frequency-domain specifications that are used in the remainder of this chapter.
