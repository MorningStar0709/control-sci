# 7.6.5 The Reduced-Order Observer

Occasionally, some of the state variables are measured directly with good precision. In such cases, it makes little sense to estimate them, since they are directly available. The reduced-order observer, or Luenberger observer [8], uses the available information to reduce the order of the observer by the number of directly measured state variables.

Let us assume that the first $m$ components of the state, $m < n$ , are measured. (We can always rearrange the state equations so that the measured states are numbered 1 to $m$ .) We write

$$
\mathbf {x} = \left[ \begin{array}{l} \mathbf {x} _ {m} \\ - - \\ \mathbf {x} _ {u} \end{array} \right] \} m
$$

![](image/d937ef396b97e433a87aa5bab20fc6ac39dd09e658b5b25abf36fde26c616849.jpg)

<details>
<summary>line</summary>

| Time(s) | Extension (m) |
| --- | --- |
| 0 | 0 |
| 1 | 11.0e-4 |
| 2 | 2.0e-4 |
| 3 | 7.0e-4 |
| 4 | 5.0e-4 |
| 5 | 6.0e-4 |
| 6 | 5.0e-4 |
| 7 | 5.0e-4 |
| 8 | 5.0e-4 |
| 9 | 5.0e-4 |
| 10 | 5.0e-4 |
| 11 | -5.0e-4 |
| 12 | 3.0e-4 |
| 13 | -2.0e-4 |
| 14 | 2.0e-4 |
| 15 | -1.0e-4 |
| 16 | 0.0e-4 |
| 17 | -1.0e-4 |
| 18 | 0.0e-4 |
| 19 | 0.0e-4 |
| 20 | 0.0e-4 |
</details>

![](image/9ab85c0cd491be81b9f727aa4248633fee5daa31e309c25baa9536d4c1c4d459.jpg)

<details>
<summary>line</summary>

| Time(s) | Velocity (m/s) |
| --- | --- |
| 0 | 0.0 |
| 2 | 0.05 |
| 4 | 0.1 |
| 6 | 0.18 |
| 8 | 0.25 |
| 10 | 0.3 |
| 12 | 0.3 |
| 14 | 0.3 |
| 16 | 0.3 |
| 18 | 0.3 |
| 20 | 0.3 |
</details>

Figure 7.22 Estimates (dotted) and actual variables for the train problem: coupler 4 extension, car 5 velocity. This is the nominal case.

![](image/90461f11aea322cdfb1a713648c20a41288441aa393ae7742e6c01ecb6b3f211.jpg)

<details>
<summary>line</summary>

| Time(s) | Extension (m) |
| --- | --- |
| 0 | 0 |
| 1 | 8e-4 |
| 2 | 5e-4 |
| 3 | 6e-4 |
| 4 | 5e-4 |
| 5 | 4e-4 |
| 6 | 3e-4 |
| 7 | 4e-4 |
| 8 | 3e-4 |
| 9 | 3e-4 |
| 10 | 3e-4 |
| 11 | -4e-4 |
| 12 | 3e-4 |
| 13 | -2e-4 |
| 14 | 1e-4 |
| 15 | 0 |
| 16 | 0 |
| 17 | 0 |
| 18 | 0 |
| 19 | 0 |
| 20 | 0 |
</details>

![](image/16c7d75e94b11bf9ca372a33ea71450eea6293a4764b99b919a1b368616ab52c.jpg)

<details>
<summary>line</summary>

| Time(s) | Velocity (m/s) - Solid Line | Velocity (m/s) - Dashed Line |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 2 | 0.05 | 0.04 |
| 4 | 0.12 | 0.10 |
| 6 | 0.18 | 0.16 |
| 8 | 0.25 | 0.22 |
| 10 | 0.30 | 0.28 |
| 12 | 0.31 | 0.29 |
| 14 | 0.31 | 0.29 |
| 16 | 0.31 | 0.29 |
| 18 | 0.31 | 0.29 |
| 20 | 0.31 | 0.29 |
</details>
