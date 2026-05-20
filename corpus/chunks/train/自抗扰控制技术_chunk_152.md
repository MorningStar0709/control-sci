$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = f (x _ {1}, x _ {2}, t) + b u \\ y = x _ {1} \end{array} \right. \tag {4.3.20}
$$

![](image/6a52eff4f27ca6b8fdf6ee8aa173c768854706f0ca81b8a129114a8ef6b5d0bd.jpg)

<details>
<summary>line</summary>

| x | x1 | x2 | x3 |
| --- | --- | --- | --- |
| 20 | 0 | 0 | 0 |
| 40 | 50 | 50 | 50 |
| 60 | 100 | 100 | 100 |
| 80 | 150 | 150 | 150 |
| 100 | 200 | 200 | 200 |
| 120 | 250 | 250 | 250 |
| 140 | 300 | 300 | 300 |
| 160 | 350 | 350 | 350 |
| 180 | 400 | 400 | 400 |
| 200 | 450 | 450 | 450 |

Legend:
- x1 = x1 * x2
- x2 = x3
- x3 = x4
- x4 = x5
- x5 = x6
- x6 = x7
- x7 = x8
- x8 = x9
- x9 = x10
- x11 = x12
- x13 = x14
- x15 = x16
- x17 = x18
- x19 = x20
- x21 = x22
- x23 = x24
- x25 = x26
- x27 = x28
- x29 = x30
- x31 = x32
- x33 = x34
- x35 = x36
- x37 = x38
- x39 = x40
- x41 = x42
- x43 = x44
- x45 = x46
- x47 = x48
- x49 = x50
- x51 = x52
- x53 = x54
- x55 = x56
- x57 = x58
- x59 = x60
- x61 = x62
- x63 = x64
- x65 = x66
- y-axis labeled as 'x1' and 'x2' with a note that 'x1*sign(xin(0.5))+o*sign(xin(0.3))/ion(0.2)/r' is shown in the chart.
</details>

图4.3.5

可以建立如下扩张状态观测器

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} g _ {1} (e) \\ \dot {z} _ {2} = z _ {3} - \beta_ {0 2} g _ {2} (e) \\ \dot {z} _ {3} = z _ {4} - \beta_ {0 3} g _ {3} (e) + b u \\ \dot {z} _ {4} = - \beta_ {0 4} g _ {4} (e) \end{array} \right.
$$

或

$$
\left\{ \begin{array}{l} e = z _ {1} - y \\ \dot {z} _ {1} = z _ {2} - \beta_ {0 1} e \\ \dot {z} _ {2} = z _ {3} - \beta_ {0 2} \text {fal} (e, 0. 5, \delta) \\ \dot {z} _ {3} = z _ {4} - \beta_ {0 3} \text {fal} (e, 0. 2 5, \delta) + b u \\ \dot {z} _ {4} = - \beta_ {0 4} \text {fal} (e, 0. 1 2 5, \delta) \end{array} \right. \tag {4.3.21}
$$

用这个扩张状态观测器来观测对象

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = \operatorname{sign} (\sin (t / 2)) \\ y = x _ {1} \end{array} \right.
$$

的状态和被扩张的状态的仿真结果如图4.3.6所示.这里取了如

下参数：

$$h = 0. 0 1, \delta = 5 h, \beta_ {0 1} = 1 0 0, \beta_ {0 2} = 3 0 0, \beta_ {0 3} = 1 0 0 0, \beta_ {0 4} = 1 8 0 0.$$

有意思的是在前一例子中用过的前三个参数 $\beta_{01}=100,\beta_{02}=300,\beta_{03}=1000$ 照样可以在这个例子中使用.这种现象称作扩张状态观测器参数对系统阶的“继承性”.

![](image/42eeab58eb7390028e4ed00c2b91efee1076d7cce3bd04331ccd540ace41ccfd.jpg)  
图4.3.6
