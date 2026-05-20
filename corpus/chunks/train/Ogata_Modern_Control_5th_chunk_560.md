# MATLAB Program 7–25

```matlab
num = [20];
den = [1 1 0];
w = logspace(0,1,100);
bode(num,den,w)
title('Bode Diagram of G1(s) = 20/[s(s + 1)]') 
```

Figure 7–146 Bode diagram of G1(s).   
![](image/798e838e5ea7bcc93daf964310dc658036ac6a7de7ff15c4a05b31ec087005ff.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 1 | -138 | 23 |
| 10 | -178 | -15 |
</details>

The lead compensator thus determined is

$$G _ {c} (s) = K _ {c} \frac {s + 3 . 0 1 0 1}{s + 1 4 . 3 3 3 9} = K _ {c} \alpha \frac {0 . 3 3 2 2 s + 1}{0 . 0 6 9 7 6 s + 1}$$

where $K _ { c }$ is determined as

$$K _ {c} = \frac {K}{\alpha} = \frac {2}{0 . 2 1} = 9. 5 2 3 8$$

Thus, the transfer function of the compensator becomes

$$G _ {c} (s) = 9. 5 2 3 8 \frac {s + 3 . 0 1 0 1}{s + 1 4 . 3 3 3 9} = 2 \frac {0 . 3 3 2 2 s + 1}{0 . 0 6 9 7 6 s + 1}$$

MATLAB Program 7–26 produces the Bode diagram of this lead compensator, which is shown in Figure 7–147.

<table><tr><td>MATLAB Program 7-26</td></tr><tr><td>numc = [9.5238 28.6676];denc = [1 14.3339];w = logspace(-1,3,100);bode(numc,denc,w)title(&#x27;Bode Diagram of Gc(s) = 9.5238(s + 3.0101)/(s + 14.3339&#x27;)</td></tr></table>

Figure 7–147 Bode diagram of $G _ { c } ( s )$ .   
![](image/5da2e0556a2fb72ba4b02050fbd197975bf5a09ebdad7bf599b1f028999299f2.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.1 | 0 | 6 |
| 1 | 10 | 7 |
| 10 | 40 | 15 |
| 100 | 10 | 20 |
| 1000 | 0 | 20 |
</details>

The open-loop transfer function of the designed system is

$$
\begin{array}{l} G _ {c} (s) G (s) = 9. 5 2 3 8 \frac {s + 3 . 0 1 0 1}{s + 1 4 . 3 3 3 9} \frac {1 0}{s (s + 1)} \\ = \frac {9 5 . 2 3 8 s + 2 8 6 . 6 7 5 9}{s ^ {3} + 1 5 . 3 3 3 9 s ^ {2} + 1 4 . 3 3 3 9 s} \\ \end{array}
$$

MATLAB Program 7–27 will produce the Bode diagram of $G _ { c } ( s ) G ( s )$ , which is shown in Figure 7–148.

<table><tr><td>MATLAB Program 7-27</td></tr><tr><td>num = [95.238 286.6759];den = [1 15.3339 14.3339 0];sys = tf(num,den);w = logspace(-1,3,100);bode(sys,w);grid;title(&#x27;Bode Diagram of Gc(s)G(s)&#x27;)[Gm,pm,wcp,wcg] = margin(sys);GmdB = 20*log10(Gm);[Gmdb,pm,wcp,wcg]ans =Inf 49.4164 Inf 6.5686</td></tr></table>

Figure 7–148 Bode diagram of Gc(s)G(s).   
![](image/08eee3d2c5306112167ab03f67cbc5f361620e420c0fa1739f6b4f67c412b74c.jpg)

<details>
<summary>line</summary>
