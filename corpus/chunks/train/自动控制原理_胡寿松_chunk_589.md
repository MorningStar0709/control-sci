(1) $G(s)=\frac{1}{s(0.1s+1)}$ ;   
(2) $G(s) = \frac{2}{s(s + 1)};$   
(3) $G(s) = \frac{2(1.5s + 1)}{s(s + 1)(0.1s + 1)}$ .

用描述函数法分析时,哪个系统分析的准确度高?

8-13 试推导下列非线性特性的描述函数：

(1) 变增益特性(见表 8-1 中第九项);  
(2) 具有死区的继电特性(见表 8-1 中第二项);  
(3) $y=x^{3}$ 。

8-14 将图 8-84 所示非线性系统简化成典型结构图形式，并写出线性部分的传递函数。

![](image/77cba58359cd00debb7a5f781a5eda61297363f12b510fadc3a96e9b469e4d68.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r=0"] --> B["+"]
    B --> C["+"]
    C --> D["N"]
    D --> E["G₁(s)"]
    E --> F["c"]
    F --> G["H₁(s)"]
    G --> H["-"]
    H --> B
```
</details>

(a)

![](image/4ee104d06389c95ecbbe5445140331a046d4c7446ad5bc8766a9903373a771f8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r=0"] --> B["+"]
    B --> C["+"]
    C --> D["G₁(s)"]
    D --> E["c"]
    E --> F["N"]
    F --> G["H₁(s)"]
    G --> H["-"]
    H --> B
```
</details>

(b)   
图 8-84 题 8-14 的非线性系统结构图

8-15 根据已知非线性特性的描述函数求图 8-85 所示各种非线性特性的描述函数。

![](image/0574aa02d97d0d93163d38a8b11795966aa4b31436212428d3503952ec444dbf.jpg)

<details>
<summary>text_image</summary>

-a
0 a
x
y
K
</details>

(a)

![](image/779d130722d54dec77bb9e3d215ec1960b4bb28993ca0c2c09efe89d77d1d6a6.jpg)

<details>
<summary>text_image</summary>

y
2M
M
0 a b x
</details>

(b)

![](image/686daa4c7cd9c6b69591e322ef64716befde8b5662fb1af0c5b49196ef2b197f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["x"] --> B["Block with gain K, delta"]
    B --> C["x"]
    C --> D["Block with gain M, delta, h"]
    D --> E["y"]
```
</details>

(c)   
图 8-85 题 8-15 的非线性特性

8-16 某单位反馈系统, 其前向通路中有一描述函数 $N(A) = \mathrm{e}^{-\mathrm{j}\frac{\pi}{4}} / A$ 的非线性元件, 线性部分的传递函数为 $G(s) = 15 / s(0.5s + 1)$ , 试用描述函数法确定系统是否存在自振? 若有, 参数是多少?  
8-17 已知非线性系统的结构图如图 8-86 所示, 图中非线性环节的描述函数 $N(A) = \frac{A + 6}{A + 2}$ ( $A > 0$ ), 试用描述函数法确定:

![](image/a3607e1bc5f975c6950f77bb81ca81220bef1b1f2f789d26f8bc59280be13eec.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["r=0"] --> B["+"]
    B --> C["N(A)"]
    C --> D["\frac{K}{s(s+1)^2}"]
    D --> E["c"]
    E --> F["-"]
    F --> B
```
</details>

图 8-86 题 8-17 的非线性系统

(1) 使该非线性系统稳定、不稳定以及产生周期运动时，线性部分的 K 值范围；  
(2) 判断周期运动的稳定性, 并计算稳定周期运动的振幅和频率。

8-18 非线性系统如图 8-87 所示,试用描述函数法分析周期运动的稳定性,并确定系统输出信号振荡的振幅和频率。

![](image/093fb8a060a9831316f42a0664c88d93e80150f9f3b891fac2a816a59e1a6fda.jpg)

<details>
<summary>flowchart</summary>
