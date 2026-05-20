# (2) 朱利稳定判据

朱利判据是直接在 $z$ 域内应用的稳定性判据，类似于连续系统中的赫尔维茨判据，朱利判据是根据离散系统的闭环特征方程 $D(z) = 0$ 的系数，判别其根是否位于 $z$ 平面上的单位圆内，从而判断该离散系统是否稳定。

设离散系统 n 阶闭环特征方程可以写为

$$D (z) = a _ {0} + a _ {1} z + a _ {2} z ^ {2} + \dots + a _ {n} z ^ {n} = 0, \quad a _ {n} > 0$$

利用特征方程的系数,按照下述方法构造 $(2n-3)$ 行、 $(n+1)$ 列朱利阵列,如表7-4所示。

表 7-4 朱利阵列

<table><tr><td>行数</td><td> $z^1$ </td><td> $z^1$ </td><td> $z^2$ </td><td> $z^3$ </td><td>...</td><td> $z^{n-k}$ </td><td>...</td><td> $z^{n-1}$ </td><td> $z^n$ </td></tr><tr><td>1</td><td> $a_0$ </td><td> $a_1$ </td><td> $a_2$ </td><td> $a_3$ </td><td>...</td><td> $a_{n-k}$ </td><td>...</td><td> $a_{n-1}$ </td><td> $a_n$ </td></tr><tr><td>2</td><td> $a_n$ </td><td> $a_{n-1}$ </td><td> $a_{n-2}$ </td><td> $a_{n-3}$ </td><td>...</td><td> $a_k$ </td><td>...</td><td> $a_1$ </td><td> $a_0$ </td></tr><tr><td>3</td><td> $b_0$ </td><td> $b_1$ </td><td> $b_2$ </td><td> $b_3$ </td><td>...</td><td> $b_{n-k}$ </td><td>...</td><td> $b_{n-1}$ </td><td></td></tr><tr><td>4</td><td> $b_{n-1}$ </td><td> $b_{n-2}$ </td><td> $b_{n-3}$ </td><td> $b_{n-4}$ </td><td>...</td><td> $b_{k-1}$ </td><td>...</td><td> $b_0$ </td><td></td></tr><tr><td>5</td><td> $c_0$ </td><td> $c_1$ </td><td> $c_2$ </td><td> $c_3$ </td><td>...</td><td> $c_{n-2}$ </td><td></td><td></td><td></td></tr><tr><td>6</td><td> $c_{n-2}$ </td><td> $c_{n-3}$ </td><td> $c_{n-4}$ </td><td> $c_{n-5}$ </td><td>...</td><td> $c_0$ </td><td></td><td></td><td></td></tr><tr><td>:</td><td>:</td><td>:</td><td>:</td><td>:</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2n-5</td><td> $p_0$ </td><td> $p_1$ </td><td> $p_2$ </td><td> $p_3$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2n-4</td><td> $p_3$ </td><td> $p_2$ </td><td> $p_1$ </td><td> $p_0$ </td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2n-3</td><td> $q_0$ </td><td> $q_1$ </td><td> $q_2$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

在朱利阵列中, 第 $2k + 2$ 行各元, 是 $2k + 1$ 行各元的反序排列。从第三行起, 阵列中各元的定义如下:
