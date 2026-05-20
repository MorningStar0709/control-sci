# EXAMPLE 1.1 Different open-loop responses

Consider systems with the open-loop transfer functions

$$G _ {0} (s) = \frac {1}{(s + 1) (s + a)}$$

where $a = -0.01, 0$ , and $0.01$ . The dynamics of these processes are quite different, as is illustrated in Fig. 1.4(a). Notice that the responses are significantly different. The system with $a = 0.01$ is stable; the others are unstable. The initial parts of the step responses, however, are very similar for all systems. The closed-loop systems obtained by introducing the proportional feedback with unit gain, that is, $u = u_c - y$ , give the step responses shown in Fig. 1.4(b). Notice that the responses of the closed-loop systems are virtually identical. Some insight is obtained from the frequency responses. Bode diagrams for the

![](image/38458f8fa3680f800d4d04527095a51d2a0ff82624b9ec15834c9febe9a1db5c.jpg)

<details>
<summary>line</summary>

| Time | α = -0.01 | α = 0 | α = 0.01 |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 100 | ~150 | ~75 | ~25 |
| 200 | ~300 | ~150 | ~50 |
| 300 | ~450 | ~225 | ~75 |
</details>

![](image/5da93f82a9168e5a6d5e62a1aad8239d1db50fb2616b441ad1cc108acf88ee64.jpg)

<details>
<summary>line</summary>

| Time | Output y |
| --- | --- |
| 0 | 0.0 |
| 5 | 1.0 |
| 10 | 1.0 |
</details>

Figure 1.4 (a) Open-loop unit step responses for the process in Example 1.1 with $a = -0.01$ , 0, and 0.01. (b) Closed-loop step responses for the same system, with the feedback $u = u_{c} - y$ . Notice the difference in time scales.

![](image/b9effeb2da8509dd9ee6e7d559fa915251b743153567dbf6ae04380d2b0b43d3.jpg)

(b)   
![](image/f09a40f4a3e616af19b2e3a84f64bdffd6a490efe6963658e6654252d15ef104.jpg)

<details>
<summary>line</summary>

| x | Magnitude |
| --- | --- |
| 10^-3 | 10^0 |
| 10^-2 | 10^0 |
| 10^-1 | 10^0 |
| 10^0 | 10^0 |
| 10^1 | 10^0 |
</details>

![](image/23f01e9db39ea8ecff6d5166fb30589a2b68a900d353beaffce1ad7aac350633.jpg)

<details>
<summary>line</summary>

| Frequency [rad/s] | Phase [deg] |
| --- | --- |
| 10⁻³ | 0 |
| 10⁻² | 0 |
| 10⁻¹ | -50 |
| 10⁰ | -150 |
| 10¹ | -200 |
</details>

Figure 1.5 (a) Open-loop and (b) closed-loop Bode diagrams for the process in Example 1.1.

![](image/35a1bbd51fc0b50cc58ff010a392e786a4d75970b9eab564f7fab06ec6597538.jpg)

<details>
<summary>line</summary>

| Time | Output y |
| --- | --- |
| 0 | 0.0 |
| 1 | ~0.6 |
| 2 | ~0.8 |
| 3 | ~0.9 |
| 4 | ~0.95 |
| 5 | ~0.98 |
</details>
