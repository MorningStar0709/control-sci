# EXAMPLE 7–22

Consider the following two systems:

$$\text { System I: } \quad \frac {C (s)}{R (s)} = \frac {1}{s + 1}, \quad \text { System II: } \quad \frac {C (s)}{R (s)} = \frac {1}{3 s + 1}$$

Compare the bandwidths of these two systems. Show that the system with the larger bandwidth has a faster speed of response and can follow the input much better than the one with the smaller bandwidth.

Figure 7–77(a) shows the closed-loop frequency-response curves for the two systems. (Asymptotic curves are shown by dashed lines.) We find that the bandwidth of system I is $0 \leq \omega \leq 1$ radsec and that of system II is $0 \leq \omega \leq 0 . 3 3$ radsec. Figures 7–77(b) and (c) show, respectively, the unit-step response and unit-ramp response curves for the two systems. Clearly, system I, whose bandwidth is three times wider than that of system II, has a faster speed of response and can follow the input much better.

Figure 7–77 Comparison of dynamic characteristics of the two systems considered in Example 7–22. (a) Closed-loop frequency-response curves; (b) unit-step response curves; (c) unit-ramp response curves.   
![](image/71f6eafbaa79752c1eace1b13244ade4ebbe5858835aa03fd1ea4dc368f83eea.jpg)

<details>
<summary>line</summary>

| ω (in log scale) | dB (Curve I) | dB (Curve II) |
| --- | --- | --- |
| 0.33 | 0 | 0 |
| 1 | -10 | -5 |
| >1 | -20 | -15 |
</details>

(a)

![](image/c9949851d1b635ca1994cc0e6456c19701a6c9cc83e95c81d739034b9293f627.jpg)

<details>
<summary>line</summary>

| t | r(t) | c(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 1 | 1 |
</details>

(b)

![](image/69792dad118b953b72e4f192d4de272e63ee6d6f3f129faa2e21300f64203c7e.jpg)

<details>
<summary>line</summary>

| t | r(t) | c(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 1 | 0.5 |
</details>

(c)

MATLAB Approach to Get Resonant Peak, Resonant Frequency, and Bandwidth. The resonant peak is the value of the maximum magnitude (in decibels) of the closed-loop frequency response.The resonant frequency is the frequency that yields the maximum magnitude. MATLAB commands to be used for obtaining the resonant peak and resonant frequency are as follows:

```matlab
[mag,phase,w] = bode(num,den,w); or [mag,phase,w] = bode(sys,w);
[Mp,k] = max(mag);
resonant_peak = 20*log10(Mp);
resonant_frequency = w(k) 
```

The bandwidth can be obtained by entering the following lines in the program:

n = 1;
while $20*\log10(\text{mag}(n)) > = -3$ ; n = n + 1;
end
bandwidth = w(n)

For a detailed MATLAB program, see Example 7–23.
