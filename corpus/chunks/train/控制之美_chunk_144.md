![](image/cf2a24e3608d7c650e205b9680396c14081bef28be35f90ee733ff2e3ccc05a3.jpg)

<details>
<summary>text_image</summary>

渐近线
分离点
-4 -3 -8/3 -2 -1 O σ
jω
</details>

图8.2.7 例8.2.7的根轨迹

根据规则 4, 从 $s_{\mathrm{p}2,3}$ 出发的两条根轨迹分支汇聚后将同时离开实轴。离开实轴的这个点称为分离点 (Breakaway Point)。通过下面的例子介绍分离点的计算方法。

例 8.2.8 使用根轨迹的方法验证二阶系统(如图 8.2.8 所示)中的阻尼比 $\zeta$ 对系统的作用(其中, $\omega_{n} > 0$ )。

解：将图8.2.8中的动态系统传递函数考虑为一个控制系统的闭环传递函数，并令 $K = \zeta$ ，得到

$$
G _ {\mathrm{cl}} (s) = \frac {2 K \omega_ {\mathrm{n}} s}{s ^ {2} + 2 K \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}} \tag {8.2.6}
$$

为分析其根轨迹,需要找到 $G_{\mathrm{cl}}(s)$ 所对应的开环系统传递函数,根据例 8.1.1,将闭环传递函数标准形式 $G_{\mathrm{cl}}(s)=\frac{KG(s)}{1+KG(s)}$ 代入式(8.2.6),得到

$$
\begin{array}{l} \frac {K G (s)}{1 + K G (s)} = \frac {2 K \omega_ {\mathrm{n}} s}{s ^ {2} + 2 K \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}} \\ \Rightarrow 2 K \omega_ {\mathrm{n}} s (1 + K G (s)) = \left(s ^ {2} + 2 K \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2}\right) K G (s) \\ \Rightarrow 2 K \omega_ {\mathrm{n}} s = (s ^ {2} + \omega_ {\mathrm{n}} ^ {2}) K G (s) \\ \Rightarrow G (s) = \frac {2 \omega_ {\mathrm{n}} s}{s ^ {2} + \omega_ {\mathrm{n}} ^ {2}} \tag {8.2.7} \\ \end{array}
$$

其对应的单位反馈闭环控制系统框图如图 8.2.9 所示。

![](image/14eeba798b7562791a9ad8eac90fc58caf76b2e618077264550cb2aac92dad67.jpg)  
图 8.2.8 二阶系统框图

![](image/171f3e682ca51515803b6ee4a1f93004bfce6a9a7051b18f28318e1b655cde49.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["U(s)"] --> B["+"]
    B --> C["K"]
    C --> D["G(s)=2ωₙs/(s²+ωₙ²)"]
    D --> E["X(s)"]
    E --> F["Feedback"]
    F --> B
```
</details>

图 8.2.9 二阶系统转化单位反馈闭环控制系统框图

分析其根轨迹, $G(s)$ 有n=2个极点 $s_{p1}=j\omega_{n}$ 和 $s_{p2}=-j\omega_{n}$ ，有m=1个零点 $s_{z1}=0$ 。根据规则1，根轨迹共有n=2条分支。根据规则2和规则5，将有n-m=1条根轨迹分支从极点指向零点，另一条从极点指向无穷。根据规则3，零点 $s_{p2}=-j\omega_{n}$ 的左边实轴上存在根轨迹。根据规则4，根轨迹关于实轴对称。综上所述，它的根轨迹如图8.2.10所示，两条分支分别从两个极点开始，呈对称形状向实轴移动，汇聚在实轴上某一点之后一条指向零点，另一条指向负无穷。下面来分析计算汇合点(Break-in Point)的位置。

![](image/c3b3adcb37d4683271af6c04bf4b296eb1ac84d5f1ad5603bd050b6bd91ae916.jpg)

<details>
<summary>text_image</summary>

jω
ωₙ
-ωₙ O σ
-ωₙ
</details>

图8.2.10 开环传递函数为 $G(s) = \frac{2\omega_{\mathrm{n}}s}{s^2 + \omega_{\mathrm{n}}^2}$ 的根轨迹

根据式 $(8.2.6)$ ，当闭环传递函数分母为0时，可得

$$
s ^ {2} + 2 K \omega_ {\mathrm{n}} s + \omega_ {\mathrm{n}} ^ {2} = 0
$$
