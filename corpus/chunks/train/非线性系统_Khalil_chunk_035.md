![](image/6aecbf7a372612fec0f1c6a211ef0d19f70ff6a502d1e670f4059b5c606b3da6.jpg)

<details>
<summary>text_image</summary>

F_f
v
</details>

(a) 库仑摩擦力

![](image/c1eb8b116bf7ce8dc2ab624bd93446aa0abecb046e518c9d7517412952f791c0.jpg)

<details>
<summary>text_image</summary>

F_f
v
</details>

(b) 库仑摩擦力加线性摩擦力

![](image/48477c97095ba41a869e9838ae176bf6e67f424da5bbcb20864378afbd562629.jpg)

<details>
<summary>text_image</summary>

F_f
v
</details>

(c) 静摩擦力、库仑摩擦力和线性黏滞摩擦力

![](image/bac0771d3a471815c488be05479517716eacae824f501f308e896f7fe47e7dea.jpg)

<details>
<summary>text_image</summary>

F_f
v
</details>

(d) 静摩擦力、库仑摩擦力和线性黏滞摩擦力——Stribeck效应   
图 1.5 摩擦力模型示例

注意该状态模型的两个特点。首先,它有一组平衡点,而不是一个孤立的平衡点;其次,等式右边的函数是状态变量的不连续函数,这是由于在建立摩擦力模型时的理想化造成的。人们希望物理摩擦力由其静态摩擦力平滑地转化到滑动摩擦力,而不是理想情况下的突变①。但理想化的不连续简化了分析,例如,当 $x_{2}>0$ 时可由线性模型

$$
\begin{array}{r c l} \dot {x} _ {1} & = & x _ {2} \\ \dot {x} _ {2} & = & - \frac {k}{m} x _ {1} - \frac {c}{m} x _ {2} - \mu_ {k} g \end{array}
$$

建立系统模型。同样，当 $x_{2}<0$ 时可由线性模型

$$
\begin{array}{r c l} \dot {x} _ {1} & = & x _ {2} \\ \dot {x} _ {2} & = & - \frac {k}{m} x _ {1} - \frac {c}{m} x _ {2} + \mu_ {k} g \end{array}
$$

建立系统模型。这样,在每个区域都可以通过线性分析预测系统特性。这就是一个所谓分段线性分析的例子,系统在状态空间的不同区域都可用线性模型表示,当从一个区域变化到另一个区域时只是系数改变而已。
