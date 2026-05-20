# 9.3.1 Transient Performance Specications

The transient performance of second order systems (systems having 2 poles) is fairly easy to characterize. We develop intuition about the relationship of pole locations to time response from these second order systems.

![](image/c0a586276613885e2893a3f20294f379ec4e5ea7ae22e6a9655c81939ceadbc8.jpg)

<details>
<summary>line</summary>

| Input | System Type | Response/SSE |
| --- | --- | --- |
| 0 | 0 | ↑SSE |
| 1 | 1 | ↑SSE |
| 2 | 2 | ←SSE = 0 |
</details>

Figure 9.3: Qualitative Illustrations of dierent SSE and transient responses.

<table><tr><td>Type</td><td>C(s)P(s)</td><td>Step (n=1)</td><td>Ramp (n=2)</td><td>Parabola (n=3)</td></tr><tr><td>0</td><td>K...</td><td>finite</td><td>∞</td><td>∞</td></tr><tr><td>1</td><td> $\frac{K}{s}$ ...</td><td>0</td><td>finite</td><td>∞</td></tr><tr><td>2</td><td> $\frac{K}{s^2}$ ...</td><td>0</td><td>0</td><td>finite</td></tr></table>

Table 9.1: SSE vs. System Type and Input Type

![](image/75756bd22686dd71a742ebcd67753f5fdea2f50424866dae114f7ce64e18c249.jpg)

<details>
<summary>line</summary>

| Time Point | Value |
| --- | --- |
| T_r | 10% |
| T_p | 90% |
| T_s | 2Δ |
</details>

Figure 9.4: A step response with labels for percent overshoot (%OS) and settling time, TS.

Although practical systems are usually higher order and we use computer techniques to fully understand their dynamics, the relationship between time domain performance and 2nd order poles is important to learn.

Looking at a typical step response (Figure 9.4), the most basic measures are

1. the time it takes to settle down   
2. the time it takes to reach close to the target   
3. the amount the response overshoots the target before it settles down.
