由于 $\left\| \frac{\partial g}{\partial x_1} \right\|_{\infty} = \sup_{x \in U} |0.1 - 0.06x_2| = 0.16, \left\| \frac{\partial g}{\partial x_2} \right\|_{\infty} = \sup_{x \in U} |0.28 - 0.06x_1| = 0.34,$ 由式(5.3)可知，取 $h_1 = 0.2, h_2 = 0.2$ 时，有 $\| g - f \|_{\infty} \leqslant 0.16 \times 0.2 + 0.34 \times 0.2 = 0.1$ ，满足精度要求。由于 $L = 2$ ，此时模糊集的个数为 $N = \frac{L}{h} + 1 = 11$ ，即 $x_1$ 和 $x_2$ 分别在 $U = [-1, 1]$ 上定义11个具有三角形隶属函数的模糊集 $A^j$ 。

所设计的模糊系统为

$$f (x) = \frac {\sum_ {i _ {1} = 1} ^ {1 1} \sum_ {i _ {2} = 1} ^ {1 1} g (e ^ {i _ {1}} , e ^ {i _ {2}}) \mu_ {A} ^ {i _ {1}} (x _ {1}) \mu_ {A} ^ {i _ {2}} (x _ {2})}{\sum_ {i _ {1} = 1} ^ {1 1} \sum_ {i _ {2} = 1} ^ {1 1} \mu_ {A} ^ {i _ {1}} (x _ {1}) \mu_ {A} ^ {i _ {2}} (x _ {2})} \tag {5.6}$$

该模糊系统由 $11 \times 11 = 121$ 条规则来逼近函数 $g(x)$ 。

二维函数逼近仿真程序见本章附录程序 chap5-2. m。 $x_{1}$ 和 $x_{2}$ 的隶属函数及 $g(x)$ 的逼近效果如图 5-4 至图 5-7 所示。

![](image/9784908174dbcb4700ab9021cf395148edbe6e94c16ed2f65441ec7eda06a5ba.jpg)

<details>
<summary>line</summary>

| x₁ | Membership function |
| --- | --- |
| -1.0 | 1.0 |
| -0.8 | 0.5 |
| -0.6 | 1.0 |
| -0.4 | 0.5 |
| -0.2 | 1.0 |
| 0.0 | 0.5 |
| 0.2 | 1.0 |
| 0.4 | 0.5 |
| 0.6 | 1.0 |
| 0.8 | 0.5 |
| 1.0 | 1.0 |
</details>

图5-4 $x_{1}$ 的隶属函数

![](image/d692ec65e932a77f8895a4b8f8fee4a17950d06a4a30b97eb28ce6e3f7feaaa3.jpg)

<details>
<summary>line</summary>

| x₂ | Membership function |
| --- | --- |
| -1.0 | 1.0 |
| -0.8 | 0.0 |
| -0.6 | 1.0 |
| -0.4 | 0.0 |
| -0.2 | 1.0 |
| 0.0 | 0.0 |
| 0.2 | 1.0 |
| 0.4 | 0.0 |
| 0.6 | 1.0 |
| 0.8 | 0.0 |
| 1.0 | 1.0 |
</details>

图5-5 $x_{2}$ 的隶属函数

![](image/b131d4cade767f6762dcd8f4573e00a5cefb07f10a179f487e6d6ea7bbb41cec.jpg)

<details>
<summary>surface_3d</summary>

| x | y | f(x) |
| --- | --- | --- |
| -1 | 0 | 0.5 |
| -0.5 | 0.5 | 0.75 |
| 0 | 1 | 1 |
| 0.5 | 0.5 | 0.75 |
| 1 | 0 | 0.5 |
</details>

![](image/32f9250b11f6fadf72ddfe142a2ae37411ed087cc320135b6c64c0c88960b115.jpg)

<details>
<summary>surface_3d</summary>

| x | y | g(x) |
| --- | --- | --- |
| -1 | 0 | 0.5 |
| -0.5 | 0.5 | 0.75 |
| 0 | 1 | 1 |
| 0.5 | 0.5 | 0.75 |
| 1 | 0 | 0.5 |
</details>

图5-6 模糊逼近

![](image/9ebed38b0d590d1b103dad64449607ed05fddce26f65ea9c6a851fe75fee073e.jpg)

<details>
<summary>surface_3d</summary>

| X | Y | Z |
| --- | --- | --- |
| -1 | 0.02 | 0.0 |
| -0.5 | 0.01 | 0.0 |
| 0 | 0.00 | 0.0 |
| 0.5 | -0.01 | 0.0 |
| 1 | -0.02 | 0.0 |
</details>

图5-7 逼近误差
