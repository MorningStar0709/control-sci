# Observable Canonical Form

Assume that the characteristic equation of $\Phi$ is (3.18) and that the observability matrix $W_{o}$ is nonsingular. Then there exists a transformation matrix such that

![](image/67f63775c7376dc14725c2d3708852bb2bf84448e9ba23c72cdeeed8a521ddee.jpg)

<details>
<summary>line</summary>

| x | Output |
| --- | --- |
| 0 | 0 |
| 1 | 0 |
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

![](image/b76bbef92223eeebfd24bcb840fb6c2a5821ac3a69ac430189f34a6deadfe2e0.jpg)

<details>
<summary>scatter</summary>

| x | Output |
| --- | --- |
| 0 | 1.2 |
| 1 | 0.8 |
| 2 | 0.5 |
| 3 | 0.3 |
| 4 | 0.2 |
| 5 | 0.1 |
| 6 | 0.05 |
| 7 | 0.02 |
| 8 | 0.01 |
| 9 | 0.005 |
| 10 | 0.0 |
</details>

![](image/3474a559433b59645f667a1a1967bde9acde99377f19c42b42bf98b96aba3219.jpg)

<details>
<summary>scatter</summary>

| Time | Output |
| --- | --- |
| 0 | 1.5 |
| 1 | 1.0 |
| 2 | 0.7 |
| 3 | 0.5 |
| 4 | 0.3 |
| 5 | 0.2 |
| 6 | 0.1 |
| 7 | 0.05 |
| 8 | 0.02 |
| 9 | 0.01 |
| 10 | 0.0 |
</details>

![](image/0204a5e748afc42be920b80deb5429973e63db01395da5bd6f388b3415c52790.jpg)

<details>
<summary>scatter</summary>

| Time | Output |
| --- | --- |
| 0 | 1.3 |
| 1 | 0.8 |
| 2 | 0.6 |
| 3 | 0.4 |
| 4 | 0.3 |
| 5 | 0.2 |
| 6 | 0.1 |
| 7 | 0.1 |
| 8 | 0.1 |
| 9 | 0.1 |
| 10 | 0.1 |
</details>

Figure 3.11 The output of the system in Example 3.10 for the initial states (a) $[0.5\quad 1]^T$ , (b) $[1.5\quad 0.5]^T$ , (c) $[2.5\quad 0]^T$ , and (d) $[1\quad -0.5]^T$ .

the transformed system is

$$
z (k + 1) = \left( \begin{array}{c c c c c} {- a _ {1}} & {1} & {0} & {\dots} & {0} \\ {- a _ {2}} & {0} & {1} & {\dots} & {0} \\ {\vdots} & {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {- a _ {n - 1}} & {0} & {0} & {\dots} & {1} \\ {- a _ {n}} & {0} & {0} & {\dots} & {0} \end{array} \right) z (k) + \left( \begin{array}{c} {b _ {1}} \\ {b _ {2}} \\ {\vdots} \\ {b _ {n - 1}} \\ {b _ {n}} \end{array} \right) u (k) \tag {3.23}

y (k) = \left( \begin{array}{c c c c} 1 & 0 & \dots & 0 \end{array} \right) z (k)
$$

which is called the observable canonical form. This form has the advantage that it is easy to find the input-output model and to determine a suitable observer. The transformation in this case is given by

$$\boldsymbol {T} = \tilde {\boldsymbol {W}} _ {0} ^ {- 1} \boldsymbol {W} _ {0}$$

where $\tilde{W}_{o}$ is the observability matrix for the representation (3.23).

Remark. The observable and controllable forms are also called companion forms.
