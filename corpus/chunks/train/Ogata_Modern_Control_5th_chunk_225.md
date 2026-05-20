<table><tr><td>MATLAB Program 5-11</td></tr><tr><td>% ---- Unit-ramp response ----</td></tr><tr><td>% ***** The unit-ramp response is obtained by adding a new % state variable x3. The dimension of the state equation % is enlarged by one *****</td></tr><tr><td>% ***** Enter matrices A, B, C, and D of the original state % equation and output equation *****</td></tr><tr><td>A = [0 1;-1 -1];</td></tr><tr><td>B = [0; 1];</td></tr><tr><td>C = [1 0];</td></tr><tr><td>D = [0];</td></tr><tr><td>% ***** Enter matrices AA, BB, CC, and DD of the new, % enlarged state equation and output equation *****</td></tr><tr><td>AA = [A zeros(2,1);C 0];</td></tr><tr><td>BB = [B;0];</td></tr><tr><td>CC = [0 0 1];</td></tr><tr><td>DD = [0];</td></tr><tr><td>% ***** Enter step-response command: [z,x,t] = step(AA,BB,CC,DD) *****</td></tr><tr><td>[z,x,t] = step(AA,BB,CC,DD);</td></tr><tr><td>% ***** In plotting x3 add the unit-ramp input t in the plot % by entering the following command: plot(t,x3,&#x27;o&#x27;,t,t,&#x27;-&#x27;) *****</td></tr><tr><td>x3 = [0 0 1]*x&#x27;; plot(t,x3,&#x27;o&#x27;,t,t,&#x27;-&#x27;) grid title(&#x27;Unit-Ramp Response&#x27;) xlabel(&#x27;t Sec&#x27;) ylabel(&#x27;Input and Output&#x27;)</td></tr></table>

![](image/70b29723c363e32456614cf3885bf7f7e270a9f014918e0a7ba4dd46613bff26.jpg)

<details>
<summary>line</summary>

| t Sec | Input and Output |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |
</details>

Figure 5–27 Unit-ramp response curve.

Obtaining Response to Arbitrary Input. To obtain the response to an arbitrary input, the command lsim may be used. The commands like

$$\operatorname{lsim} (\text { num }, \text { den }, r, t)\operatorname{Isim} (A, B, C, D, u, t)y = \operatorname{lsim} (\text { num }, \text { den }, r, t)y = \operatorname{Isim} (A, B, C, D, u, t)$$

will generate the response to input time function r or u. See the following two examples. (Also, see Problems A–5–14 through A–5–16.)

EXAMPLE 5–6 Using the lsim command, obtain the unit-ramp response of the following system:

$$\frac {C (s)}{R (s)} = \frac {2 s + 1}{s ^ {2} + s + 1}$$

We may enter MATLAB Program 5–12 into the computer to obtain the unit-ramp response.The resulting plot is shown in Figure 5–28.
