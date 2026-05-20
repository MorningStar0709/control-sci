The solution to the LQ-problem gives a time-varying controller. The feedback matrix does not depend on x and can be precomputed from k = N to k = 0 and stored in the computer. For time-invariant processes and loss functions, usually only the stationary controller—the constant controller obtained when the Riccati equation is iteratad until a constant S is obtained—is used. $S(k)$ will—under quita general assumptions—converge to a constant matrix as the time horizon increases. In general, there exist several solutions resulting from different $Q_{0}$ .

The stationary solution can be obtained by iterating (11.17) or by solving the algebraic Riccati equation

$$\bar {S} = \Phi^ {T} \bar {S} \Phi + Q _ {1} - \left(\Phi^ {T} \bar {S} \Gamma + Q _ {1 2}\right) \left(\Gamma^ {T} \bar {S} \Gamma + Q _ {2}\right) ^ {- 1} \left(\Gamma^ {T} \bar {S} \Phi + Q _ {1 2} ^ {T}\right) \tag {11.33}$$

Because $Q$ in (11.10) is symmetric and positive semidefinite we can write

$$
Q = \left( \begin{array}{c c} C _ {l} & D _ {l} \end{array} \right) ^ {T} \left( \begin{array}{c c} C _ {l} & D _ {l} \end{array} \right)
$$

If the system of (11.16) is reachable and if

$$
\left( \begin{array}{c c} - z I + \Phi & \Gamma \\ C _ {l} & D _ {l} \end{array} \right)
$$

has full column rank for $|z| \geq 1$ , that is, there are no unstable zeros to the system defined by $\Phi$ , $\Gamma$ , $C_{l}$ , and $D_{l}$ , then there exists only one symmetric nonnegative definite solution to the algebraic Riccati equation (11.33).

![](image/c1b8bb953efdfdcadfeb670edf35521ca91a7653c22d74f829807386854a633d.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | -1 |
| 1 | 1 |
| 2 | -1 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

![](image/0958a66a2c4f02caa68b77b0ed223226fd03ed0516a92e8582eb018a1f78f7f9.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | -1 |
| 1 | 1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |
| 6 | 0 |
| 7 | 0 |
| 8 | 0 |
| 9 | 0 |
| 10 | 0 |
</details>

![](image/8274fbad3d179ba2157570b6ab5b8c484517fa25455507968201f64b32f7e02d.jpg)

<details>
<summary>line</summary>

| Time | Value |
| --- | --- |
| 0 | -0.5 |
| 1 | 0.5 |
| 2 | 0.0 |
| 3 | 0.0 |
| 4 | 0.0 |
| 5 | 0.0 |
| 6 | 0.0 |
| 7 | 0.0 |
| 8 | 0.0 |
| 9 | 0.0 |
| 10 | 0.0 |
</details>

![](image/98ad43eaa7b705eeedffdac55536891dbf40018f9717bef26205c54ee1666be0.jpg)

<details>
<summary>line</summary>

| Time | Solid Line | Dashed Line |
| --- | --- | --- |
| 0 | 0 | 1 |
| 10 | 0 | 0 |
</details>

Figure 11.2 Linear quadratic control of the double-integrator plant for different weightings, $\rho$ , on the control signal. The initial value of the state is $x(0) = [1 - 0]$ . The position $x_{1}$ (dashed), velocity $x_{2}$ (dashed-dotted), and the control signal $u$ (solid) are shown. (a) $\rho = 0.01563$ , (b) $\rho = 0.05$ , (c) $\rho = 0.5$ , and (d) $\rho = 10$ .
