# EXAMPLE 10.4 Second-order VSS

Consider the unstable system

$$
\frac {d x}{d t} = \left( \begin{array}{l l} 1 & 0 \\ 1 & 0 \end{array} \right) x + \binom{1}{0} u = A x + B u

y = \left( \begin{array}{c c} 0 & 1 \end{array} \right) x
$$

which has the transfer function

$$G (s) = \frac {1}{s (s - 1)}$$

To design a variable-structure controller we determine the closed-loop dynamics by choosing the switching line

$$\sigma (x) = p _ {1} x _ {1} + p _ {2} x _ {2} = x _ {1} + x _ {2}$$

Along the sliding line $\sigma = 0$ we have

$$\sigma (x) = x _ {1} + x _ {2} = \frac {d y}{d t} + y = 0$$

Since the system is in controllable form, the closed-loop behavior is independent of the system parameters at the sliding mode. The sliding mode controller

![](image/7fe4bc5d592624a00a47f9c93f394f46dc9fc93438a272dddaa79af5400a09d8.jpg)

<details>
<summary>other</summary>

| x1 | x2 |
| --- | --- |
| -1.5 | 0.8 |
| -1.2 | 0.6 |
| -0.8 | 0.4 |
| -0.5 | 0.2 |
| -0.2 | 0.0 |
| 0.0 | -0.2 |
| 0.2 | -0.4 |
| 0.5 | -0.6 |
| 0.8 | -0.8 |
| 1.0 | -1.0 |
| 1.2 | -1.2 |
| 1.5 | -1.4 |
</details>

Figure 10.14 Phase portrait of the system in Example 10.4. The dashed line shows $\sigma(x) = 0$ .

(a)   
![](image/e5c65b51cb0e37959771fe9cb630b80436422d6e7beb279696c71ea9ba5cdc1f.jpg)

<details>
<summary>line</summary>

| Time | x1 | x2 |
| --- | --- | --- |
| 0 | 1.2 | 0.0 |
| 2 | 0.8 | 0.8 |
| 4 | 0.3 | 0.2 |
| 6 | 0.1 | 0.05 |
| 8 | 0.05 | 0.02 |
| 10 | 0.02 | 0.01 |
</details>

(b)   
![](image/f2f8c70eae8e69cc031aba1ef1b9efc2198c9cbba8965fa2776a92ad809b4b8f.jpg)

<details>
<summary>line</summary>

| Time | x1 | x2 |
| --- | --- | --- |
| 0 | 1.5 | 0 |
| 2 | 0.8 | -0.5 |
| 4 | 0.2 | -0.2 |
| 6 | 0 | 0 |
| 8 | 0 | 0 |
| 10 | 0 | 0 |
</details>

![](image/915005aad4e644a33fc7bedbf81b9de7f557dd27d556644bc44395db7d408460.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | -4 |
| 2 | 0 |
| 4 | 0 |
| 6 | 0 |
| 8 | 0 |
| 10 | 0 |
</details>

![](image/dbada7f2daa608edc1b3e72d1b7aa6745734ff90f97350d4144553371cc1eb26.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | -3.5 |
| 2 | 0.0 |
| 4 | 0.5 |
| 6 | 0.0 |
| 8 | 0.0 |
| 10 | 0.0 |
</details>

Figure 10.15 The states and the output as a function of time in Example 10.4. The initial conditions are $x_{1}(0) = 1.5$ and $x_{2}(0) = 0$ . The controllers are (a) Eq. (10.10) with $\mu = 0.5$ ; (b) Eq. (10.12) with $\mu = 0.5$ and $\varepsilon = 0.01$ .

(10.10) is now
