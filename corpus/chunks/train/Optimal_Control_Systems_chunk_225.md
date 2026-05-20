$$\dot {\bar {\mathbf {g}}} (t) = \left[ \bar {\mathbf {P}} \mathbf {E} - \mathbf {A} ^ {\prime} \right] \bar {\mathbf {g}} (t) - \mathbf {W} \mathbf {z} (t) \tag {4.2.6}$$

where, $E = BR^{-1}B'$ and $W = C'Q$ . The optimal control (4.1.31) becomes

$$\boxed {\mathbf {u} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \left[ \bar {\mathbf {P}} \mathbf {x} (t) - \bar {\mathbf {g}} (t) \right].} \tag {4.2.7}$$

Further details on this are available in Anderson and Moore [3].

![](image/563f58cc97c0a2c5f88343519d35dda63860ac316f41afcdca2eb9d3b04ed158.jpg)

<details>
<summary>line</summary>

| t | g₁(t) | g₂(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2 | 5 | 1 |
| 4 | 10 | 2 |
| 6 | 15 | 3 |
| 8 | 20 | 4 |
| 10 | 25 | 5 |
| 12 | 30 | 6 |
| 14 | 35 | 7 |
| 16 | 40 | 8 |
| 18 | 45 | 9 |
| 20 | 47 | 0 |
</details>

Figure 4.7 Coefficients $g_{1}(t)$ and $g_{2}(t)$ for Example 4.2   
![](image/7de1181b46b5925eb84aa5a12c9e80f203e49857b160bb4453e8e5128d8dec3e.jpg)

<details>
<summary>line</summary>

| t | x₁(t) | x₂(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 2 | 5 | 0 |
| 4 | 10 | 0 |
| 6 | 15 | 0 |
| 8 | 20 | 0 |
| 10 | 25 | 0 |
| 12 | 30 | 0 |
| 14 | 35 | 0 |
| 16 | 40 | 0 |
| 18 | 45 | 0 |
| 20 | 35 | -20 |
</details>

Figure 4.8 Optimal Control and States for Example 4.2

![](image/3d85239f2faecb14f2c7a3d99f233b2314de7d0022ec4e2c5731caab4d6f4ab1.jpg)

<details>
<summary>line</summary>

| t | Optimal Control |
| --- | --- |
| 0 | 0 |
| 2 | -100 |
| 4 | -200 |
| 6 | -300 |
| 8 | -400 |
| 10 | -500 |
| 12 | -550 |
| 14 | -500 |
| 16 | -400 |
| 18 | -300 |
| 20 | 0 |
</details>

Figure 4.9 Optimal Control and States for Example 4.2
