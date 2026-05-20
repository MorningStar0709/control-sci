# 8.3.4 改进的零极点匹配(MMPZ)法

由式(8.29)中的 $D_{\mathrm{d}}(z)$ 能得到的 $u(k)$ 取决于同一时间点上的输入 $e(k)$ 。如果计算机的硬件结构禁止将读取和写入的时间最小化，或者这一计算过程特别冗长，那么最好

![](image/96c1df7930f76ecfc69d09bf9a34614a9a415cf152ac8e724109d2f4c9f5068c.jpg)

<details>
<summary>line</summary>

| 时间/s | Continuous design | Discrete equivalent design, T=1sec | Discrete equivalent design, T=0.5 sec |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 5 | 1.2 | 1.4 | 1.3 |
| 10 | 1.1 | 1.2 | 1.1 |
| 15 | 1.0 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 | 1.0 |
| 25 | 1.0 | 1.0 | 1.0 |
| 30 | 1.0 | 1.0 | 1.0 |
</details>

图 8.14 连续实现与数字实现的阶跃响应

能推导出一个 $D_{\mathrm{d}}(z)$ ，其分子 $z$ 的指数幂比分母少1。这样计算机的输出 $u(k)$ 将仅需要前一时刻的输入，即 $e(k - 1)$ 。为了实现这个想法，我们仅需修改零极点匹配法中的第二步，使得分子的阶次比分母小1。比如，若

$$D _ {\mathrm{c}} (s) = K _ {\mathrm{c}} \frac {s + a}{s (s + b)}$$

跳过第二步可得

$$D _ {\mathrm{d}} (z) = K _ {\mathrm{d}} \frac {z - \mathrm{e} ^ {- a T}}{(z - 1) (z - \mathrm{e} ^ {- b T})} \tag {8.36}K _ {\mathrm{d}} = K _ {\mathrm{c}} \frac {a}{b} (\frac {1 - \mathrm{e} ^ {- b T}}{1 - \mathrm{e} ^ {- a T}})$$

为得到差分方程，将式(8.36)的分子分母均乘以 $z^{-2}$ 得

$$D _ {\mathrm{d}} (z) = K _ {\mathrm{d}} \frac {z ^ {- 1} (1 - \mathrm{e} ^ {- a T} z ^ {- 1})}{1 - z ^ {- 1} (z + \mathrm{e} ^ {- b T}) + z ^ {- 2} \mathrm{e} ^ {- b T}} \tag {8.37}$$

通过观察式(8.37)可以得到差分方程为

$$u (k) = (1 + \mathrm{e} ^ {- b T}) u (k - 1) - \mathrm{e} ^ {- b T} u (k - 2) + K _ {\mathrm{d}} [ e (k - 1) - \mathrm{e} ^ {- a T} e (k - 2) ]$$

在该方程中， $u(k)$ 仅依赖于 $e(k-1)$ ，整个采样周期可用于计算并输出 $u(k)$ ，该控制器的离散分析会更加准确地说明实际系统的行为。但由于该控制器使用的是一个周期的旧数据，当系统期望输出的偏差出现随机扰动时，通常它的性能没有 MPZ 控制器的性能好。
