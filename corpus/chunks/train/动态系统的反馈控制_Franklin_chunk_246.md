(c) 试确定系统由参考输入所决定的系统类型，并求出对应的误差常数。

(d) 试确定系统由干扰输入 w 所决定的系统类型及相应的误差系数。

4.19 如图 4.34 所示反馈系统，试求 $\alpha$ 值使系统在 K=5 时为 1 型系统。给出相应的速度常数。证明在该 $\alpha$ 值时，系统不具有鲁棒性，并计算在单位阶跃信号作用下，K=4 和 K=6 时系统的稳态误差 e=r-y。

![](image/c9380ee4b3b2d369b66be43784fac2735e8883cf466b30d33527c21e78bbfa86.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R --> α
    α --> sum["Σ"]
    sum --> K["K/(s+2)"]
    K --> Y
    Y -->|-| sum
```
</details>

图 4.34 习题 4.19 控制系统

4.20 假设给定系统如图 4.35a 所示，其中被控对象参数 a 是变量。

(a) 求出 $G(s)$ 使图 4.35b 和图 4.35a 所示的系统从 r 到 y 具有相同的的传递函数。

(b) 假设 a=1 是被控对象参数的标称值。
试求此时系统类型和误差常数。

(c) 假设 $a=1+\delta a$ ，其中 $\delta a$ 是被控对象的某一摄动。试求摄动系统的类型和误差常数。

![](image/acf7e98caf097ea8aa5d9de772eb03429b5bc887a8a37a4f20cb0a4f5ad03070.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    R0["RO"] --> Sum1["Σ"]
    Sum1 --> 4["4"]
    4 --> U["U"]
    U --> Int["1/(s + a)"]
    Int --> x["x"]
    x --> Sum2["Σ"]
    Sum2 --> Int2["1/s"]
    Int2 --> Y["Y"]
    y --> Sum3["Σ"]
    Sum3 --> -1["−1/4"]
    -1 --> Sum2
    Sum2 --> Sum3
    Sum3 --> Sum4["+"]
    Sum4 --> Sum3
```
</details>

a)

![](image/6a43527259510bb0c7197e8e172fb0b53b722c69fa17957b09d18ad4cd83d9bd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum -->|E(t)| Gs["G(s)"]
    Gs --> Y
    Y -->|-| Sum
```
</details>

b)   
图 4.35 习题 4.20 控制系统

4.21 如图 4.36 所示的两个反馈系统。

(a) 试确定 $K_{1}$ 、 $K_{2}$ 、 $K_{3}$ 的值，使得

(i) 在阶跃输入信号作用下，两个系统都具有零稳态误差(即都是1型系统)。

(ii) 当 $K_{0}=1$ 时，它们的静态速度误差常数 $K_{v}=1$ 。

(b) 假设 $K_{0}$ 有一个小的摄动： $K_{0} \rightarrow K_{0} + \delta K_{0}$ 。这对每种情况下的系统有什么影响？哪一种系统类型是鲁棒的？你认为哪个系统更好？

![](image/3143234b647b7a37a43608b0f173cef7f587ebc58d574f9d22b3d7c4b2283d00.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum1["Σ"]
    Sum1 --> K1s["K₁/s"] --> U --> K0["/(4s+1)"] --> Y
    Y -->|-| Sum1
    Sum1 -->|+| Sum2["Σ"]
    Sum2 --> K3["K₃"] --> U --> K02["/(4s+1)"] --> Y
    Y -->|-| Sum2
```
</details>

图4.36 习题4.21的两个反馈控制系统

4.22 给定如图 4.37 所示的控制系统，其中反馈增益 $\beta$ 是一个变量。试设计一个控制器，使输出 $y(t)$ 精确跟踪参考输入信号 $r(t)$ 。

![](image/4338d5d140fcea573fd661c460c0536ede33a37c7e30c3ed32af620aba617491.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    R -->|+| Sum
    Sum -->|a| Dci(s)
    Dci -->|10/(s+1)(s+10)| Sum
    Sum -->|-| β
    β -->|feedback| Sum
    Sum --> Y
```
</details>

图 4.37 习题 4.22 控制系统

(a) 令 $\beta = 1$ ，控制器 $D_{ci}(s)$ 可选如下形式：
