| t Sec | Uncompensated system | Compensated system |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.6 | 1.2 |
| 2 | 0.6 | 0.7 |
| 3 | 1.2 | 1.2 |
| 4 | 0.9 | 0.8 |
| 5 | 1.1 | 1.1 |
| 6 | 0.9 | 0.9 |
</details>

Figure 7–149

Unit-step responses of the uncompensated and compensated systems.

MATLAB Program 7–29 produces the unit-ramp response curves. [Note that the unit-ramp response is obtained as the unit-step response of $C ( s ) / s R ( s ) .$ ] The resulting curves are shown in Figure 7–150.The compensated system has a steady-state error equal to one-half that of the original uncompensated system.

<table><tr><td>MATLAB Program 7-29</td></tr><tr><td>%*****Unit-ramp responses*****</td></tr><tr><td>num1 = [10];</td></tr><tr><td>den1 = [1 1 10 0];</td></tr><tr><td>num2 = [95.238 286.6759];</td></tr><tr><td>den2 = [1 15.3339 110.5719 286.6759 0];</td></tr><tr><td>t = 0:0.01:3;</td></tr><tr><td>[c1,x1,t] = step(num1,den1,t);</td></tr><tr><td>[c2,x2,t] = step(num2,den2,t);</td></tr><tr><td>plot(t,c1,&#x27;.&#x27;,t,c2,&#x27;-&#x27;,t,t,&#x27;--&#x27;);</td></tr><tr><td>grid;</td></tr><tr><td>title(&#x27;Unit-Ramp Responses of Uncompensated System and Compensated System&#x27;);</td></tr><tr><td>xlabel(&#x27;t Sec&#x27;);</td></tr><tr><td>ylabel(&#x27;Outputs&#x27;)</td></tr><tr><td>text(1.2,0.65,&#x27;Uncompensated System&#x27;)</td></tr><tr><td>text(0.1,1.3,&#x27;Compensated System&#x27;)</td></tr></table>

![](image/732a4d51f5efd5f15aff0865a4443a1f0e0200d3ad5123abcf02fcd8eaf9a785.jpg)

<details>
<summary>line</summary>

| t Sec | Compensated System | Uncompensated System |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.5 | 0.2 |
| 1.0 | 1.0 | 0.8 |
| 1.5 | 1.5 | 1.4 |
| 2.0 | 2.0 | 1.8 |
| 2.5 | 2.5 | 2.2 |
| 3.0 | 3.0 | 2.8 |
</details>

Figure 7–150   
Unit-ramp responses of the uncompensated and compensated systems.

A–7–25. Consider a unity-feedback system whose open-loop transfer function is

$$G (s) = \frac {K}{s (s + 1) (s + 4)}$$

Design a lag–lead compensator $G _ { c } ( s )$ such that the static velocity error constant is $1 0 \mathrm { s e c } ^ { - 1 }$ , the phase margin is $5 0 ^ { \circ }$ , and the gain margin is 10 dB or more.

Solution. We shall design a lag–lead compensator of the form
