we choose $a = 5$ . Then, $( a s + 1 )$ will contribute up to $9 0 ^ { \circ }$ phase lead in the highfrequency region. MATLAB Program 8–3 produces the Bode diagram of

$$\frac {4 (5 s + 1)}{s (s ^ {2} + 1)}$$

The resulting Bode diagram is shown in Figure 8–15.

<table><tr><td>MATLAB Program 8-3</td></tr><tr><td>num = [20 4];den = [1 0.00000000001 1 0];w = logspace(-2,1,101);bode(num,den,w)title(&#x27;Bode Diagram of G(s) = 4(5s+1)/[s(s^2+1)]&#x27;)</td></tr></table>

![](image/30834f613baeb3554055ca62667f3f80ce5f35b0887f5322692e41a6af69901b.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.01 | -90 | 50 |
| 0.1 | -60 | 30 |
| 1 | -20 | 50 |
| 10 | -200 | -10 |
</details>

Figure 8–15   
Bode diagram of

$$G (s) = 4 (5 s + 1) /\left[ s \left(s ^ {2} + 1\right) \right].$$

Based on the Bode diagram of Figure 8–15, we choose the value of b. The term $( b s + 1 )$ needs to give the phase margin of at least $5 0 ^ { \circ }$ . By simple MATLAB trials, we find $b = 0 . 2 5$ to give the phase margin of at least $5 0 ^ { \circ }$ and gain margin of ±q dB.Therefore, by choosing $b = 0 . 2 5$ , we have

$$G _ {c} (s) = \frac {4 (5 s + 1) (0 . 2 5 s + 1)}{s}$$

and the open-loop transfer function of the designed system becomes

$$
\begin{array}{l} \text { Open - loop   transfer   function } = \frac {4 (5 s + 1) (0 . 2 5 s + 1)}{s} \frac {1}{s ^ {2} + 1} \\ = \frac {5 s ^ {2} + 2 1 s + 4}{s ^ {3} + s} \\ \end{array}
$$

MATLAB Program 8–4 produces the Bode diagram of the open-loop transfer function. The resulting Bode diagram is shown in Figure 8–16. From it we see that the static velocity error constant is 4 $\sec ^ { - 1 }$ , the phase margin is 55°, and the gain margin is ±q dB.

<table><tr><td>MATLAB Program 8-4</td></tr><tr><td>num = [5 21 4];den = [1 0 1 0];w = logspace(-2,2,100);bode(num,den,w)title(&#x27;Bode Diagram of 4(5s+1)(0.25s+1)/[s(s^2+1)]&#x27;)</td></tr></table>

![](image/1536565a180bfd2acfa50e04ba5457a2eeb28bfb386fd4bd41a6298f31f9feb0.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.01 | 50 | 50 |
| 0.1 | 30 | 30 |
| 1 | 45 | 45 |
| 10 | -10 | -10 |
| 100 | -20 | -20 |
</details>

Figure 8–16   
Bode diagram of

$$4 (5 s + 1) (0. 2 5 s + 1) /\left[ s \left(s ^ {2} + 1\right) \right].$$
