# MATLAB Program 8–1

% --- ------- Unit-step response

num = [6.3223 18 12.811];

den = [1 6 11.3223 18 12.811];

step(num,den)

grid

title('Unit-Step Response')

Figure 8–8

Unit-step response curve of PIDcontrolled system designed by use of the Ziegler–Nichols tuning rule (second method).

![](image/ed73cf83b2f9eb399c153cec2758d0a27e27761790c709edcf6c420ad8a54b16.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 2 | 1.6 |
| 4 | 0.7 |
| 6 | 1.15 |
| 8 | 0.9 |
| 10 | 1.0 |
| 12 | 0.98 |
| 14 | 1.0 |
</details>

Figure 8–9 Unit-step response of the system shown in Figure 8–6 with PID controller having parameters $K _ { p } = 1 8 ,$ $T _ { i } = 3 . 0 7 7 ,$ and $T _ { d } = 0 . 7 6 9 2 .$ .   
![](image/6ee78757557b204690f0c0c410740bccabd0a3f89035bfbd7e2fa8d58d0b78b0.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0 |
| 1 | 1.2 |
| 2 | 1.1 |
| 3 | 1.05 |
| 4 | 1.02 |
| 5 | 1.01 |
| 6 | 1.005 |
| 7 | 1.0 |
</details>

then the speed of response is increased, but the maximum overshoot is also increased to approximately 28%, as shown in Figure 8–10. Since the maximum overshoot in this case is fairly close to 25% and the response is faster than the system with $G _ { c } ( s )$ given by Equation (8–1), we may consider $G _ { c } ( s )$ as given by Equation (8–2) as acceptable. Then the tuned values of $K _ { p } , T _ { i } ,$ and, $T _ { d }$ become

$$K _ {p} = 3 9. 4 2, \quad T _ {i} = 3. 0 7 7, \quad T _ {d} = 0. 7 6 9 2$$

It is interesting to observe that these values respectively are approximately twice the values suggested by the second method of the Ziegler–Nichols tuning rule.The important thing to note here is that the Ziegler–Nichols tuning rule has provided a starting point for fine tuning.
