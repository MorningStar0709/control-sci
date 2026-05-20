Response to Unit-Acceleration Reference Input   
![](image/0138c2a8cca2e754a5136b028b1cadb8d85c83fe61384c7d01c57bfb0dbe7bd4.jpg)

<details>
<summary>line</summary>

| t (sec) | Input | Output |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.2 | 0.05 | 0.04 |
| 0.4 | 0.15 | 0.12 |
| 0.6 | 0.30 | 0.25 |
| 0.8 | 0.50 | 0.45 |
| 1.0 | 0.75 | 0.65 |
| 1.2 | 1.05 | 0.95 |
| 1.4 | 1.40 | 1.35 |
| 1.6 | 1.80 | 1.65 |
| 1.8 | 2.25 | 2.10 |
| 2.0 | 2.75 | 2.55 |
</details>

Figure 8–43 (continued)   
(c)

The response exhibits the maximum overshoot of 21% and the settling time is approximately 1.6 sec. Figures 8–43(b) and (c) show the ramp response and acceleration response. The steadystate errors in both responses are zero.The response to the step disturbance was satisfactory.Thus, the designed controllers $G _ { c 1 } ( s )$ and $G _ { c 2 } ( s )$ given by Equations (8–12) and (8–13), respectively, are satisfactory.

If the response characteristics to the unit-step reference input are not satisfactory, we need to change the location of the dominant closed-loop poles and repeat the design process. The dominant closed-loop poles should lie in a certain region in the left-half s plane (such as $2 \leq a \leq 6$ , $2 \leq b \leq 6 , 6 \leq c \leq 1 2 )$ . If the computational search is desired, write a computer program (similar to MATLAB Program 8–8) and execute the search process. Then a desired set or sets of values of $a , b .$ , and c may be found such that the system response to the unit-step reference input satisfies all requirements on maximum overshoot and settling time.
