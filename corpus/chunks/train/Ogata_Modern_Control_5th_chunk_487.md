# EXAMPLE 7–23

Consider the system shown in Figure 7–78. Using MATLAB, obtain a Bode diagram for the closedloop transfer function. Obtain also the resonant peak, resonant frequency, and bandwidth.

MATLAB Program 7–12 produces a Bode diagram for the closed-loop system as well as the resonant peak, resonant frequency, and bandwidth. The resulting Bode diagram is shown in

MATLAB Program 7–12   
```matlab
nump = [1];
denp = [0.5 1.5 1 0];
sysp = tf(nump, denp);
sys = feedback(sysp, 1);
w = logspace(-1, 1);
bode(sys, w)
[mag, phase, w] = bode(sys, w);
[Mp, k] = max(mag);
resonant_peak = 20*log10(Mp)
resonant_peak =
    5.2388
resonant_frequency = w(k)
resonant_frequency =
    0.7906
n = 1;
while 20*log(mag(n)) > = -3; n = n + 1;
end
bandwidth = w(n)
bandwidth =
    1.2649 
```

Figure 7–78 Closed-loop system.   
![](image/a0b628ce3b7b62b9513acfc0e14ef47c8bb0cdc34314dee98f8963d0d7e62507.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["1/(s(0.5s+1)(s+1))"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

![](image/dbc911128e604106b5436e5f118e76d3c7af8a86bb548faca4f9e20f46393ef7.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.1 | 0 | 0 |
| 0.5 | 0 | -50 |
| 1 | 0 | -150 |
| 5 | -20 | -200 |
| 10 | -60 | -250 |
</details>

Figure 7–79 Bode diagram of the closed-loop transfer function of the system shown in Figure 7–78.   
Figure 7–79.The resonant peak is obtained as 5.2388 dB.The resonant frequency is 0.7906 radsec. The bandwidth is 1.2649 radsec. These values can be verified from Figure 7–78.
