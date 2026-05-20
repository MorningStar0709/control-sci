# (4) 将上述两个表进行“与”运算

得到每条规则总的可信度输出,见表 4-10。

表 4-9 规则前提可信度表

<table><tr><td rowspan="2" colspan="2">规则前提</td><td colspan="3">污泥x</td></tr><tr><td>SD</td><td>MD(4/5)</td><td>LD(1/5)</td></tr><tr><td rowspan="3">油脂y</td><td>NG</td><td>0</td><td>0</td><td>0</td></tr><tr><td>MG(3/5)</td><td>0</td><td>3/5</td><td>1/5</td></tr><tr><td>LG(2/5)</td><td>0</td><td>2/5</td><td>1/5</td></tr></table>

表 4-10 规则总的可信度输出

<table><tr><td rowspan="2" colspan="2">规则前提</td><td colspan="3">污泥x</td></tr><tr><td>SD</td><td>MD(4/5)</td><td>LD(1/5)</td></tr><tr><td rowspan="3">油脂y</td><td>NG</td><td>0</td><td>0</td><td>0</td></tr><tr><td>MG(3/5)</td><td>0</td><td> $\min\left(\frac{3}{5},\mu_{\mathrm {M}}(z)\right)$ </td><td> $\min\left(\frac{1}{5},\mu_{\mathrm {L}}(z)\right)$ </td></tr><tr><td>LG(2/5)</td><td>0</td><td> $\min\left(\frac{2}{5},\mu_{\mathrm {L}}(z)\right)$ </td><td> $\min\left(\frac{1}{5},\mu_{\mathrm {VL}}(z)\right)$ </td></tr></table>

(5) 模糊系统总的输出

模糊系统总的可信度为各条规则可信度推理结果的并集,即

$$
\begin{array}{l} \mu_ {\mathrm{agg}} (z) = \max \left\{\min \left(\frac {3}{5}, \mu_ {\mathrm{M}} (z)\right), \min \left(\frac {2}{5}, \mu_ {\mathrm{L}} (z)\right), \min \left(\frac {1}{5}, \mu_ {\mathrm{L}} (z)\right), \min \left(\frac {1}{5}, \mu_ {\mathrm{VL}} (z)\right) \right\} \\ = \max \left\{\min \left(\frac {3}{5}, \mu_ {\mathrm{M}} (z)\right), \min \left(\frac {2}{5}, \mu_ {\mathrm{L}} (z)\right), \min \left(\frac {1}{5}, \mu_ {\mathrm{VL}} (z)\right) \right\} \\ \end{array}
$$

可见,有3条规则被触发。

(6) 反模糊化

模糊系统总的输出 $\mu_{\mathrm{agg}}(z)$ 实际上是3个规则推理结果的并集，需要进行反模糊化，才能得到精确的推理结果。下面以最大隶属度平均法为例进行反模糊化。

洗衣机的模糊推理过程如图 4-17 和图 4-18 所示。由图 4-18 可知，洗涤时间隶属度最大值为 $\mu = \frac{3}{5}$ 。将 $\mu = \frac{3}{5}$ 代入洗涤时间隶属函数中的 $\mu_{\mathrm{M}}(z)$ ，得

![](image/520fd1c0b5d1edc11102e20742bae0dcccc5ce81952ad5c0874dd812270676cb.jpg)  
图 4-17 洗衣机的 3 个规则被触发

$$\mu_ {\mathrm{M}} (z) = \frac {z - 1 0}{1 5} = \frac {3}{5}, \mu_ {\mathrm{M}} (z) = \frac {4 0 - z}{1 5} = \frac {3}{5}$$

得 $z_{1}=19, z_{2}=31$ 。

![](image/1dc8d93948022e6b9946bdb5e3cfa7f0bfbb08504a4efabc5c37627eff9da3fe.jpg)

<details>
<summary>line</summary>

| z | μ |
| --- | --- |
| 10 | 0 |
| 19 | 3/5 |
| 31 | 3/5 |
| 40 | 2/5 |
| 60 | 1/5 |
| 1.0 | M |
| 1.0 | L |
| 1.0 | VL |
</details>

图 4-18 洗衣机的组合输出及反模糊化

采用最大平均法,可得精确输出为

$$z ^ {*} = \frac {z _ {1} + z _ {2}}{2} = \frac {1 9 + 3 1}{2} = 2 5$$

即所需要的洗涤时间为 25 分钟。
