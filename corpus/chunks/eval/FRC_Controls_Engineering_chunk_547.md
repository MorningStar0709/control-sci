| Time (s) | Continuous | Zero-order hold (T=0.1 s) |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 1.5 | 1.5 |
| 2 | 1.5 | 1.5 |
| 3 | 1.5 | 1.5 |
| 4 | 1.5 | 1.5 |
| 5 | 1.5 | 1.5 |
| 6 | 0.0 | 0.0 |
</details>

![](image/ee1075cc3a5f31e4995aef91a183a2bd18a3289a52451e77dd2816012bacf7ae.jpg)

<details>
<summary>line</summary>

| Time (s) | Continuous | Forward Euler (T=0.1 s) | Backward Euler (T=0.1 s) | Bilinear transform (T=0.1 s) |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 1 | 1.5 | 1.5 | 1.5 | 1.5 |
| 2 | 0.0 | 0.0 | 0.0 | 0.0 |
| 3 | 0.0 | 0.0 | 0.0 | 0.0 |
| 4 | 0.0 | 0.0 | 0.0 | 0.0 |
| 5 | -1.5 | -1.5 | -1.5 | -1.5 |
| 6 | -1.5 | -0.5 | -1.5 | -1.5 |
</details>

Figure E.21: Zero-order hold of a system response   
Figure E.22: Discretization methods applied to velocity data   
![](image/10cb8b25f97308fc47cb02deec4b71cbd09bed5d8a321d5f125f46c596d9131e.jpg)

<details>
<summary>line</summary>

| Time (s) | Continuous | Forward Euler (T=0.1 s) | Backward Euler (T=0.1 s) | Bilinear transform (T=0.1 s) |
| --- | --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 | 0.0 |
| 1 | 1.5 | 1.45 | 1.45 | 1.45 |
| 2 | 1.5 | 1.45 | 1.45 | 1.45 |
| 3 | 1.5 | 1.45 | 1.45 | 1.45 |
| 4 | 1.5 | 1.45 | 1.45 | 1.45 |
| 5 | 1.5 | 1.45 | 1.45 | 1.45 |
| 6 | 0.0 | 0.0 | 0.0 | 0.0 |
</details>

Figure E.23: Position plot of discretization methods applied to velocity data

<table><tr><td>Method</td><td>Conversion to z</td><td>Taylor series expansion</td></tr><tr><td>Zero-order hold</td><td> $e^{Ts}$ </td><td> $1 + Ts + \frac{1}{2}T^{2}s^{2} + \frac{1}{6}T^{3}s^{3} + \ldots$ </td></tr><tr><td>Bilinear</td><td> $\frac{1+\frac{1}{2}Ts}{1-\frac{1}{2}Ts}$ </td><td> $1 + Ts + \frac{1}{2}T^{2}s^{2} + \frac{1}{4}T^{3}s^{3} + \ldots$ </td></tr><tr><td>Forward Euler</td><td> $1 + Ts$ </td><td> $1 + Ts$ </td></tr><tr><td>Backward Euler</td><td> $\frac{1}{1-Ts}$ </td><td> $1 + Ts + T^{2}s^{2} + T^{3}s^{3} + \ldots$ </td></tr></table>

Table E.3: Taylor series expansions of discretization methods (scalar case). The zeroorder hold discretization method is exact.

![](image/a3230622ebca21763ee3ad87d52e3edd3164e9511277e34d663e8e6bfa34f443.jpg)

<details>
<summary>line</summary>

| Time (s) | Zero-order hold (T=0.1 s) | Forward Euler (T=0.1 s) | Backward Euler (T=0.1 s) | Bilinear transform (T=0.1 s) |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 1.5 | 1.5 | 1.5 | 1.5 |
| 2 | 1.5 | 1.5 | 1.5 | 1.5 |
| 3 | 1.5 | 1.5 | 1.5 | 1.5 |
| 4 | 1.5 | 1.5 | 1.5 | 1.5 |
| 5 | 1.5 | 1.5 | 1.5 | 1.5 |
| 6 | 0 | 0 | 0 | 0 |
</details>
