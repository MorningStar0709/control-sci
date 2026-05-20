# (7) 相似定理

设 $F(s) = \mathcal{L}[f(t)]$ ，则有

$$\mathscr {L} \left[ f \left(\frac {t}{a}\right) \right] = a F (a s)$$

式中，a 为实常数。

上式表示, 原函数 $f(t)$ 自变量 $t$ 的比例尺改变时 (见图 A-4), 其象函数 $F(s)$ 具有类似的形式。

证明 由式(A-11),有

$$\mathscr {L} \left[ f \left(\frac {t}{a}\right) \right] = \int_ {0} ^ {\infty} f \left(\frac {t}{a}\right) \mathrm{e} ^ {- s} \mathrm{d} t$$

令 $t / a = \tau$ ，则有

![](image/0147bd74e891cc08135645a6370cf8444b0416de196b545aa03df07ebdce5484.jpg)

<details>
<summary>line</summary>

| t | f(t) |
| --- | --- |
| 0 | High |
| 1 | Low |
| 2 | Mid |
| 3 | Low |
</details>

(a)

![](image/a1b12f0289f1789e0bb05a3cd72e7605db5639754ce7c8c67837bbc7a2298119.jpg)

<details>
<summary>line</summary>

| t | f(2t) |
| --- | --- |
| 0 | 1 |
| 0.5 | -1 |
| 1 | 0 |
| 1.5 | 1 |
| 2 | 0 |
| 3 | 0 |
</details>

(b)

![](image/b8b434c1f6ac09b56496f8c0b1bd304d73f062600670dcb75066e4383a26438c.jpg)

<details>
<summary>line</summary>

| t | f(t/2) |
| --- | --- |
| 0 | high |
| 2 | low |
| 3 | medium |
| 4 | medium |
| 5 | high |
| 6 | low |
</details>

(c)   
图A-4 函数 $f(t), f(2t), f(t / 2)$

$$\mathcal {L} \left[ f \left(\frac {t}{a}\right) \right] = a \int_ {0} ^ {\infty} f (\tau) \mathrm{e} ^ {- a s \tau} \mathrm{d} \tau = a F (a s)$$
