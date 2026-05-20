<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["安排过渡过程"] --> B["v1"]
    A --> C["v2"]
    B --> D["非线性组合"]
    C --> D
    D --> E["u1"]
    D --> F["u2"]
    E --> G["1/θ1"]
    F --> H["f1(ω₁,ω2)"]
    G --> I["z1"]
    H --> J["z2"]
    I --> K["扩张状态观测器"]
    J --> K
    K --> L["对象"]
    L --> M["y"]
    M --> N["反馈回路"]
    N --> O["ε1"]
    N --> P["ε2"]
    O --> Q["ε3"]
    P --> R["ε4"]
```
</details>

图5.2.4  
![](image/5222c4bcb079a52b26c2381b2dac09202ca88432e35652d9ee618c8544fd022a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["安排过渡过程"] --> B["v1"]
    B --> C["非线性组合"]
    C --> D["u1"]
    D --> E["1/b1"]
    E --> F["y"]
    G["扩张状态观测器"] --> H["z1"]
    H --> I["z2"]
    I --> J["+"]
    J --> K["f(z1,z2)"]
    K --> L["b1"]
    L --> M["对象"]
    M --> N["y"]
    O["v2"] --> P["v1"]
    P --> Q["e2"]
    Q --> R["非线性组合"]
    R --> S["u2"]
    S --> T["1/b2"]
    T --> U["u"]
```
</details>

图5.2.5

$$
\left\{ \begin{array}{l} \mathrm{fh} = \mathrm{fhan} (v _ {1} - v, v _ {2}, r _ {0}, h) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \end{array} \right. \tag {5.2.6}

\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(f _ {0} \left(z _ {1}, z _ {2}\right) + z _ {3} - \beta_ {0 1} \mathrm{fe} + b _ {0} u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {5.2.7}

\left\{ \begin{array}{l} e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u _ {0} = k (e _ {1}, e _ {2}, p) \end{array} \right.
u = u _ {0} - \frac {f _ {0} (z _ {1} , z _ {2}) + z _ {3} (t)}{b _ {0}} \tag {5.2.8}
$$

或

$$
\left\{ \begin{array}{l} \mathrm{fh} = \mathrm{fhan} (v _ {1} - v, v _ {2}, r _ {0}, h) \\ v _ {1} = v _ {1} + h v _ {2} \\ v _ {2} = v _ {2} + h \mathrm{fh} \end{array} \right. \tag {5.2.9}

\left\{ \begin{array}{l} e = z _ {1} - y, \mathrm{fe} = \operatorname{fal} (e, 0. 5, h), \mathrm{fe} _ {1} = \operatorname{fal} (e, 0. 2 5, h) \\ z _ {1} = z _ {1} + h \left(z _ {2} - \beta_ {0 1} e\right) \\ z _ {2} = z _ {2} + h \left(f _ {0} \left(z _ {1}, z _ {2}\right) + z _ {3} - \beta_ {0 1} \mathrm{fe} + b _ {0} u\right) \\ z _ {3} = z _ {3} + h \left(- \beta_ {0 3} \mathrm{fe} _ {1}\right) \end{array} \right. \tag {5.2.10}

\left\{ \begin{array}{l} e _ {1} = v _ {1} - z _ {1}, e _ {2} = v _ {2} - z _ {2} \\ u _ {0} = k (e _ {1}, e _ {2}, p) \end{array} \right.
u = \frac {u _ {0} - f _ {0} (z _ {1} , z _ {2}) - z _ {3} (t)}{b _ {0}} \tag {5.2.11}
$$

式中， $p$ 为一组参数。函数 $k(e_1, e_2, p)$ 的具体形式，除式(5.2.1)给出的形式外，还可以有各种不同的取法。

这些自抗扰控制器信息流的基本框架如图 5.2.6 所示.

![](image/56c60929ce976fc0c14fc02596086ee427b427ac2982dbd8f4b1da87990ade6d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["被控输出y"] --> C["控制器"]
    B["设定值v"] --> C
    C --> D["控制量u"]
```
</details>

图5.2.6

自抗扰控制器是以系统设定值v、系统被控输出y和上一步算出的控制量为其输入确定出新的控制量 u 的装置。这里和上一节的信息流框图图 5.1.11 不同的是多了一个控制量的返回通道，正是这个通道的增添才有可能实现控制器的“自抗扰”能力。
