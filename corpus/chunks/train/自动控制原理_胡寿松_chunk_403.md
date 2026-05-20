# 3. 香农采样定理

在设计离散系统时,香农采样定理是必须严格遵守的一条准则,因为它指明了从采样信号中不失真地复现原连续信号所必需的理论上的最小采样周期 T。

香农采样定理指出：如果采样器的输入信号 $e(t)$ 具有有限带宽，并且有直到 $\omega_h$ 的频率分量，则使信号 $e(t)$ 圆满地从采样信号 $e^*(t)$ 中恢复过来的采样周期 $T$ ，满足下列条件：

$$T \leqslant \frac {2 \pi}{2 \omega_ {h}} \tag {7-12}$$

采样定理表达式(7-12)与 $\omega_{s} \geqslant 2\omega_{h}$ 是等价的。由图7-13可见，在满足香农采样定理的条件下，要想不失真地复现采样器的输入信号，需要采用图7-15所示的理想滤波器，其频率特性的幅值 $|F(j\omega)|$ 必须在 $\omega = \omega_{s}/2$ 处突然截止，那么在理想滤波器的输出端便可以准确得到 $|E(j\omega)|/T$ 的连续频谱，除了幅值变化为 $1/T$ 外，频谱形状没有畸变。在满足香农采样定理条件下，理想采样器的特性如图7-16所示。图(a)为连续输入信号及其频谱；图(b)为理想单位脉冲序列及其频谱；图(c)为输出采样信号及其频谱。

应当指出,香农采样定理只是给出了一个选择采样周期 T 或采样频率 $f_{s}$ 的指导原则,它给出的是由采样脉冲序列无失真地再

![](image/9019170529d9b3f03495da01d70836c8ac379a49e8858222aac065999ebff444.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| 0 | 峰 |
| Peak | 高点 |
| End | 低点 |
</details>

(a)

![](image/3631d381bbce4da7b700d510b6c71e379ffd93f4dfac6be011ec4d6f45fc2886.jpg)

<details>
<summary>text_image</summary>

|E(jω)|
频域
-ωₕ 0 ωₕ
</details>

![](image/17b5c46e6ac8da9c9106baa99b5f1b776321fd43c4f59ffbd115ca72d5911134.jpg)

<details>
<summary>bar</summary>

| Time | δr(t) |
| --- | --- |
| T | 0 |
| 2T | 1 |
| 3T | 0 |
| 4T | 1 |
| 5T | 0 |
| 6T | 1 |
</details>

(b)   
![](image/27927c7416a172fe2458c32942baac4caf232e351ae976755b7462372ca168e5.jpg)

![](image/1d10594bd36601fcbbb5c18d7a926e84b656aa8b55cb839427f44b01c6b65c6f.jpg)

<details>
<summary>bar</summary>

| Time | e*(t) |
| --- | --- |
| 0 | 0 |
| T | 1 |
| 2T | 3 |
| 3T | 4 |
| 4T | 2 |
| 5T | 1 |
| 6T | 2 |
| 7T | 1 |
| 8T | 1 |
| 9T | 0 |
</details>

(c)   
![](image/c826545a17aab11cc909ac49adc6b49d3dca51367131d18c2fd342ed95374f06.jpg)  
图 7-16 理想采样器特性

现原连续信号所允许的最大采样周期，或最低采样频率。在控制工程实践中，一般总是取 $\omega_{s} > 2\omega_{h}$ 而不取恰好等于 $2\omega_{h}$ 的情形。
