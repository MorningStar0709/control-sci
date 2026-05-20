$$
y = \left\{ \begin{array}{l l} \sin (2 \pi x), & 0 <   x <   1 \\ x - 1, & 1 <   x <   1. 5 \\ 0. 5 - (x - 1. 5), & 1. 5 <   x <   2. 5 \\ - 0. 5 + (x - 2. 5), & 2. 5 <   x <   3 \end{array} \right.
$$

可表示为

$$y = \frac {\sin (2 \pi x)}{2} \mathrm{f3g} (x, 0, 1) + (x - 1) \mathrm{fsg} (x, 1, 1. 5) -(x - 2) \operatorname{fsg} (x, 1 ^ {1}. 5, 2. 5) + (x - 3) \operatorname{fsg} (x, 2. 5, 3)$$

![](image/77467b4ba49618529a8a1a5cc0c9fc444d3a4f724e82d337b50140a4219b5fe8.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0 |
| 0.25 | 0.4 |
| 0.5 | -0.4 |
| 0.75 | -0.1 |
| 1.0 | 0.0 |
| 1.25 | 0.3 |
| 1.5 | 0.4 |
| 1.75 | 0.2 |
| 2.0 | -0.1 |
| 2.25 | -0.4 |
| 2.5 | -0.6 |
| 2.75 | -0.3 |
| 3.0 | 0.0 |
</details>

图3.8.6

例5 死区函数

$\mathrm{fdb}_{0}(x,d)=\frac{\mathrm{sign}(x+d)+\mathrm{sign}(x-d)}{2}$ ，其图形为图3.8.7(a)· $\mathrm{sign}(x)\mathrm{fdb}_{0}(x,d)$ 图形为图3.8.7(b).

例6 $f(x) = \mathrm{sign}(x)\sqrt{|x|},y = \mathrm{sign}(f)(|f| - \sqrt{d})(1 - \mathrm{fsg}_0(x,d))$ （图3.8.8）

![](image/ab2d5e328a90e12adee1aa7d8d053d1430ec91f9a0d9ffc5158d1a41fdf14d59.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2 | -1 |
| -1 | 0 |
| 0 | 1 |
| 1 | 1 |
| 2 | 1 |
</details>

(a)

![](image/eecb18467043b7946beba257a8e82af62772b90bd747af07a4d0008bf3902d26.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2 | 1 |
| -1 | 1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
</details>

(b)

图3.8.7  
![](image/9277d43560e74ccbae8b5acdd5b637b073d945a0c642ab1f76816e46fcb14dce.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -3 | -0.5 |
| -2 | -0.25 |
| -1 | 0 |
| 0 | 0 |
| 1 | -0.25 |
| 2 | 0.25 |
| 3 | 0.5 |
</details>

图 3.8.8

例7 $f = x|x|,y = \mathrm{sign}(f)(|f| - d^2)(1 - \mathrm{fsg}_0(x,d))$ （图3.8.9）

![](image/f4ec94231fea51d091c14e31532351073b83536fde3a960a9dbeaf0d44176260.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -3 | -10 |
| -2 | -5 |
| -1 | 0 |
| 0 | 0 |
| 1 | 0 |
| 2 | 5 |
| 3 | 10 |
</details>

图3.8.9
