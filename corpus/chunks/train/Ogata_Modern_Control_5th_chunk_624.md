where $\hat { G } _ { c } ( s )$ is to be determined later. Since the static velocity error constant is specified as $\boldsymbol { \downarrow } \sec ^ { - 1 }$ , we have

$$K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) \frac {s + 0 . 1}{s ^ {2} + 1} = \lim _ {s \rightarrow 0} s \frac {K}{s} \hat {G} _ {c} (s) \frac {s + 0 . 1}{s ^ {2} + 1} = 0. 1 K = 4$$

Figure 8–52 Control system.   
![](image/bcb64fbf54e1eebbe32c45a5a3086ab70534e92c56f28454ca1ad21b5486e727.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["s + 0.1/(s² + 1)"]
    C --> D
    D --> E
    E --> F
```
</details>

Thus, K = 40. Hence

$$G _ {c} (s) = \frac {4 0}{s} \hat {G} _ {c} (s)$$

Next, we plot a Bode diagram of

$$G (s) = \frac {4 0 (s + 0 . 1)}{s (s ^ {2} + 1)}$$

MATLAB Program 8–10 produces a Bode diagram of G(s) as shown in Figure 8–53.

<table><tr><td>MATLAB Program 8-10</td></tr><tr><td>% ***** Bode Diagram *****</td></tr><tr><td>num = [40 4];</td></tr><tr><td>den = [1 0.000000001 1 0];</td></tr><tr><td>bode(num,den)</td></tr><tr><td>title(&#x27;Bode Diagram of G(s) = 40(s+0.1)/[s(s^2+1)]&#x27;)</td></tr></table>

We need the phase margin of $5 0 ^ { \circ }$ and gain margin of 10 dB or more. Let us choose $\hat { G } _ { c } ( s )$ to be

$$\hat {G} _ {c} (s) = a s + 1 \quad (a > 0)$$

Then $G _ { c } ( s )$ will contribute up to $9 0 ^ { \circ }$ phase lead in the high-frequency region. By simple MATLAB trials, we find that $a = 0 . 1 5 2 6$ gives the phase margin of $5 0 ^ { \circ }$ and gain margin of dB. +q

![](image/2866e296bcb685bb7d52e02adacc8f55b96b3e26a0368ed6994050b9c99fe341.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.001 | -100 | 75 |
| 0.01 | -90 | 60 |
| 0.1 | -50 | 40 |
| 1 | -20 | 60 |
| 10 | -20 | 0 |
</details>

Figure 8–53

Bode diagram of

$$G (s) =4 0 (s + 0. 1) / [ s (s ^ {2} + 1) ].$$

See MATLAB Program 8–11 and the resulting Bode diagram shown in Figure 8–54. From this Bode diagram we see that the static velocity error constant is 4 sec−1 , phase margin is 50° and gain margin is dB. Therefore, the designed system satisfies all the requirements. + q

MATLAB Program 8–11   
% ***** Bode Diagram *****
num = conv([40 4],[0.1526 1]);
den = [1 0.000000001 1 0];
sys = tf(num,den);
w = logspace(-2,2,100);
bode(sys,w)
[Gm,pm,wcp,wcg] = margin(sys);
GmdB = 20*log10(Gm);
[GmdB,pm,wcp,wcg]
ans =
Inf 50.0026 NaN 8.0114
title('Bode Diagram of G(s) = 40(s+0.1)(0.1526s+1)/[s(s^2+1)]')
