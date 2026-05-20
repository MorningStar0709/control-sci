# 2. 输入量和输出量的模糊化

将偏差 e 分为 5 个模糊集: 负大(NB), 负小(NS), 零(ZO), 正小(PS), 正大(PB)。将偏差 e 的变化分为 7 个等级: -3, -2, -1, 0, +1, +2, +3, 从而得到水位变化模糊表, 见表 4-1。

![](image/e5d182ba48a72382fddf5d1fb429bbce04fffec48e7e7cd9f2bd78750b1c555e.jpg)

<details>
<summary>text_image</summary>

O
h
h₀
</details>

图4-4 水箱液位控制

控制量 u 为调节阀门开度的变化。将其分为 5 个模糊集：负大(NB)，负小(NS)，零(ZO)，正小(PS)，正大(PB)。将 u 的变化分为 9 个等级：-4，-3，-2，-1，0，+1，+2，+3，+4，得到控制量模糊划分表，见表 4-2。

表 4-1 水位变化 $e$ 划分表

<table><tr><td rowspan="2" colspan="2">隶属度</td><td colspan="7">变化等级</td></tr><tr><td>-3</td><td>-2</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td rowspan="5">模糊集</td><td>PB</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1</td></tr><tr><td>PS</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0.5</td><td>0</td></tr><tr><td>ZO</td><td>0</td><td>0</td><td>0.5</td><td>1</td><td>0.5</td><td>0</td><td>0</td></tr><tr><td>NS</td><td>0</td><td>0.5</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>NB</td><td>1</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

表 4-2 控制量 u 变化划分表

<table><tr><td rowspan="2" colspan="2">隶属度</td><td colspan="9">变化等级</td></tr><tr><td>-4</td><td>-3</td><td>-2</td><td>-1</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td rowspan="5">模糊集</td><td>PB</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1</td></tr><tr><td>PS</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1</td><td>0.5</td><td>0</td></tr><tr><td>ZO</td><td>0</td><td>0</td><td>0</td><td>0.5</td><td>1</td><td>0.5</td><td>0</td><td>0</td><td>0</td></tr><tr><td>NS</td><td>0</td><td>0.5</td><td>1</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>NB</td><td>1</td><td>0.5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>
