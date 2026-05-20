| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 1 | 1.15 |
| 2 | 0.9 |
| 3 | 1.05 |
| 4 | 1.02 |
| 5 | 1.03 |
| 6 | 1.02 |
| 7 | 1.01 |
| 8 | 1.01 |
| 9 | 1.01 |
| 10 | 1.01 |
| 15 | 1.00 |
| 20 | 1.00 |
| 25 | 1.00 |
| 30 | 1.00 |
| 35 | 1.00 |
| 40 | 1.00 |
</details>

Figure 7–154   
Unit-step response curve of the compensated system.

Unit-Ramp Response: The unit-ramp response of the compensated system may be obtained by entering MATLAB Program 7–34 into the computer. Here we converted the unit-ramp response of $G _ { c } { \bar { G / ( 1 + G _ { c } G ) } }$ into the unit-step response of $G _ { c } G / { \bigl [ } s { \bigl ( } 1 + G _ { c } G { \bigr ) } { \bigr ] }$ D. The unit-ramp response curve obtained using this program is shown in Figure 7–155.

<table><tr><td>MATLAB Program 7-34</td></tr><tr><td>%*****Unit-ramp response*****</td></tr><tr><td>num = [40 24 3.2];</td></tr><tr><td>den = [1 9.02 24.18 56.48 24.32 3.2 0];</td></tr><tr><td>t = 0:0.05:20;</td></tr><tr><td>c = step(num,den,t);</td></tr><tr><td>plot(t,c,&#x27;-&#x27;,t,t,&#x27;.&#x27;)</td></tr><tr><td>grid</td></tr><tr><td>title(&#x27;Unit-Ramp Response of Compensated System&#x27;)</td></tr><tr><td>xlabel(&#x27;Time (sec)&#x27;)</td></tr><tr><td>ylabel(&#x27;Unit-Ramp Input and Output c(t)&#x27;)</td></tr></table>

![](image/dadf4d5d642bd5eac59d5fb9c135df301725589b6683fac5746d1a9c7b04635a.jpg)

<details>
<summary>line</summary>

| Time (sec) | Unit-Ramp Input and Output c(t) |
| --- | --- |
| 0 | 0 |
| 2 | 2 |
| 4 | 4 |
| 6 | 6 |
| 8 | 8 |
| 10 | 10 |
| 12 | 12 |
| 14 | 14 |
| 16 | 16 |
| 18 | 18 |
| 20 | 20 |
</details>

Figure 7–155 Unit-ramp response of the compensated system.
