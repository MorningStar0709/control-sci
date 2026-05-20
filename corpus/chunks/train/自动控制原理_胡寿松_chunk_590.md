```mermaid
graph LR
    A["r=0"] --> B["+"]
    B --> C["e(t)"]
    C --> D["5"]
    D --> E["1/0 (0.2)"]
    E --> F["2/(s(s+1))"]
    F --> G["c"]
    G --> H["-"]
    H --> B
```
</details>

图 8-87 题 8-18 的非线性系统

8-19 试用描述函数法说明图 8-88 所示系统必然存在自振，并确定 c 的自振振幅和频率，画出 c, x, y 的稳态波形。

8-20 试用描述函数法和相平面法分析图 8-89 所示非线性系统的稳定性及自振。

8-21 已知非线性系统的输入和输出关系式

$$\ddot {y} + a f (\ddot {y}, \dot {y}, y) = \ddot {u} + b g (\dot {u}, u)$$

试求伪线性系统的结构及实现形式。

![](image/d1bad5be4670aa9fd2b66df6c3e199dcb1723f155be17e3353c1990714691f5b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r=0"] --> B["+"]
    B --> C["x"]
    C --> D["1"]
    D --> E["y"]
    E --> F["(s(s+2)²)"]
    F --> G["c"]
    G --> H["2"]
    H --> I["-"]
    I --> B
```
</details>

图 8-88 题 8-19 的非线性系统

![](image/ba5ca84f5da063003b54e38de3eb8038727518b12f521c70b87fe5239bb8db4c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r=0"] --> B["+"]
    B --> C["+"]
    C --> D["K"]
    D --> E["1/(Js²)"]
    E --> F["c"]
    F --> G["s"]
    G --> H["1/sink graph"]
    H --> I["1"]
    I --> J["-"]
    J --> B
    style H stroke-dasharray: 5 5
```
</details>

图 8-89 题 8-20 的非线性系统

8-22 已知带速度反馈的非线性系统如图 8-90 所示。系统原来处于静止状态，且 $0 < \beta < 1$ ，输入 $r(t) = -R \cdot 1(t) (R > a)$ ，试分别画出有速度反馈和无速度反馈时的系统相轨迹。

![](image/7102ddeb7dc12962ccae66864365ba1ecfaf823e6b57dbb715057f7756854dd7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r(t)"] --> B["+"]
    B --> C["e(t)"]
    C --> D["+"]
    D --> E["∫(x(t))^(b/a)"]
    E --> F["1/s"]
    F --> G["1/s"]
    G --> H["c(t)"]
    H --> I["β"]
    I --> J["-"]
    J --> B
    style E stroke-dasharray: 5 5
```
</details>

图 8-90 非线性系统

8-23 非线性系统如图 8-91 所示, 其中非线性环节的描述函数 $N(A)=\frac{4M}{\pi A}$ 。试问:

![](image/03245a22b73da970903f3b799aacc84bd4d75d62471145269981622b78107bb1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input"] --> B["Block M=1"]
    B --> C["0"]
    B --> D["-1"]
    C --> E["Block Ke⁻ᵗᵗ / (s(s+1)(s+2))"]
    E --> F["c(t)"]
    F --> G["Output"]
    G --> H["Feedback"]
    H --> A
```
</details>

图 8-91 非线性系统

(1) 当 $\tau=0$ 时, 系统受扰动后的稳定运动状态呈现什么形式?  
(2) 当 $\tau \neq 0$ 时, 要使系统产生频率 $\omega = 1$ , 幅值 $A = 2$ 的自振, $\tau$ 与 $K$ 应取何值?

8-24 若要求图 8-92 所示非线性系统输出量 c 的自振振幅 $A_{c}=0.1$ ，角频率 $\omega=10$ ，试确定参数 T 及 K 的数值 (T, K 均大于零)。

![](image/c80ff929d9957f31d492578da2d8a768f0810c33979bad874eb9275164e70979.jpg)

<details>
<summary>flowchart</summary>
