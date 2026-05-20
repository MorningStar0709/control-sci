# 9-42 设单位斜坡内模控制系统如图 9-54 所示, 其中被控对象

![](image/e144a1b12dc12bd6d5f915f10460cffc90e334d7bf4e12c8aa59a79f708de777.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r_t["r(t)"] --> e_t["e(t)"]
    e_t --> k1["k₁"]
    k1 --> 1_s["1/s"]
    1_s --> add1["+"]
    add1 --> 1_s2["1/s"]
    1_s2 --> minus1["-"]
    minus1 --> u_t["u(t)"]
    u_t --> 1_s1["1/s+1"]
    1_s1 --> x2["x₂(t)"]
    x2 --> 1_s2["1/s+2"]
    1_s2 --> x1_t["y(t)"]
    x1_t --> k3["k₃"]
    k3 --> minus2["-"]
    minus2 --> sum1["-"]
    sum1 --> e_t
    e_t -->|+| add1
    add1 -->|+| minus1
    minus1 -->|+| sum2
    sum2 -->|+| minus2
    minus2 -->|+| sum3
    sum3 -->|+| plus1
    plus1 -->|+| sum4
    sum4 -->|+| minus3
    minus3 -->|+| sum5
    sum5 -->|+| plus4
    plus4 -->|+| sum6
    sum6 -->|+| minus5
    minus5 -->|+| sum7
    sum7 -->|+| plus6
    plus6 -->|+| sum8
    sum8 -->|+| minus7
    minus7 -->|+| sum9
    sum9 -->|+| plus8
    plus8 -->|+| sum10
    sum10 -->|+| minus10
    minus10 -->|+| sum11
    sum11 -->|+| plus12
    plus12 -->|+| sum13
    sum13 -->|+| minus13
    minus13 -->|+| sum14
    sum14 -->|+| plus15
    plus15 -->|+| sum16
    sum16 -->|+| minus16
    minus16 -->|+| sum17
    sum17 -->|+| plus18
    plus18 -->|+| sum19
    sum19 -->|+| minus20
    minus20 -->|+| sum20
    sum20 -->|+| plus22
    plus22 -->|+| sum23
    plus23 -->|+| minus24
    minus24 -->|+| sum25
    sum25 -->|+| plus26
    plus26 -->|+| minus28
    minus28 -->|+| sum29
    plus29 -->|+| sum30
    plus30 -->|+| minus30
    minus30 -->|+| sum32
    plus32 -->|+| sum34
    plus34 -->|+| minus34
    minus34 -->|+| sum36
    plus36 -->|+| sum38
    plus38 -->|+| minus36
```
</details>

图 9-54 单位斜坡内模控制系统

$$G _ {0} (s) = \frac {1}{(s + 1) (s + 2)}$$

$x_{1}(t)$ 和 $x_{2}(t)$ 为状态变量。试设计合适的内模控制器

$$G _ {c} (s) = \frac {k _ {1} + k _ {2} s}{s ^ {2}}$$

及状态反馈增益 $k_{3}$ 和 $k_{4}$ ，使系统的闭环极点为 $s_1 = s_2 = s_3 = s_4 = -2$ ，且系统对单位斜坡输入的稳态跟踪误差为零，最后绘出系统的单位斜坡响应曲线。

9-43 已知被控对象的动态方程

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {b} \boldsymbol {u} (t)y (t) = \mathbf {c x} (t)$$

其中

$$
\boldsymbol {A} = \left[ \begin{array}{l l} 0 & 1 \\ - 2 & - 2 \end{array} \right], \boldsymbol {b} = \left[ \begin{array}{l} 1 \\ 2 \end{array} \right], \boldsymbol {c} = [ 1 0 ]
$$

要求设计单位斜坡输入时的内模控制器，使系统闭环极点为 $s_{1,2} = -1 \pm j1, s_3 = s_4 = -10$ ，并给出单位斜坡内模控制系统结构图及跟踪误差 $e(t)$ 的响应曲线。

9-44 设单输入-单输出系统的状态空间表达式为

$$\dot {\boldsymbol {x}} (t) = \boldsymbol {A} \boldsymbol {x} (t) + \boldsymbol {b} \boldsymbol {u} (t)y (t) = \mathbf {c x} (t)$$
