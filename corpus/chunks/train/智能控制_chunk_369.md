# 7.3.6 控制系统设计中RBF网络的逼近

RBF 网络可对任意未知非线性函数进行任意精度的逼近 $^{[1,2]}$ 。在控制系统设计中，采用 RBF 网络可实现对未知函数的逼近。

例如,为了估计未知函数 $f(x)$ , 可采用如下 RBF 网络算法进行逼近

$$h _ {j} = g (\| \boldsymbol {x} - \boldsymbol {c} _ {i j} \| ^ {2} / b _ {j} ^ {2})f = \boldsymbol {W} ^ {*} \boldsymbol {h} (\boldsymbol {x}) + \varepsilon \tag {7.25}$$

式中，x 为网络输入，i 表示输入层节点，j 为隐含层节点， $h = [h_{1}, h_{2}, \cdots, h_{n}]^{T}$ 为隐含层的输出， $W^{*}$ 为理想权值， $\varepsilon$ 为网络的逼近误差， $\varepsilon \leqslant \varepsilon_{N}$ 。

在控制系统设计中,可采样 RBF 网络对未知函数 f 进行逼近。一般可采用系统状态作为网

![](image/4d96118b0379f059126ca21f74bc9c660f1bb837f57c2da74d9aa7fd79f49e6b.jpg)

<details>
<summary>line</summary>

| Input value of Redial Basis Function | Membership function degree |
| --- | --- |
| -1.0 | 0.35 |
| -0.8 | 0.45 |
| -0.6 | 0.55 |
| -0.4 | 0.65 |
| -0.2 | 0.75 |
| 0.0 | 0.85 |
| 0.2 | 0.90 |
| 0.4 | 0.85 |
| 0.6 | 0.75 |
| 0.8 | 0.65 |
| 1.0 | 0.35 |
</details>

图 7-31 7 个隐含层神经元的高斯基函数 $(m=7)$

![](image/573c31f78f456b92f66d8dfaf8dc6a55bdf1a5a1730be142ffe500824c9850ad.jpg)

<details>
<summary>line</summary>

| time(s) | Ideal value | Approximation value |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.8 | 0.8 |
| 1.0 | 1.2 | 1.2 |
| 1.5 | 1.4 | 1.4 |
| 2.0 | 1.3 | 1.3 |
| 2.5 | 1.0 | 1.0 |
| 3.0 | 0.5 | 0.5 |
| 3.5 | 0.0 | 0.0 |
| 4.0 | -0.8 | -0.8 |
| 4.5 | -1.2 | -1.2 |
| 5.0 | -1.5 | -1.5 |
</details>

![](image/6217370b84afc24323e4419a0445c57b5d84ba871801bf2684757a9ec7574ecc.jpg)

<details>
<summary>line</summary>

| time(s) | Approximation error (×10⁻³) |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | 1.0 |
| 1.0 | 2.0 |
| 1.5 | 1.5 |
| 2.0 | -2.5 |
| 2.5 | -1.0 |
| 3.0 | -0.5 |
| 3.5 | -1.5 |
| 4.0 | -2.0 |
| 4.5 | -1.0 |
| 5.0 | 2.0 |
</details>

图 7-32 含有 7 个隐含层神经元的逼近 $(m = 7)$

络的输入,网络输出为

$$\hat {f} (\boldsymbol {x}) = \hat {\boldsymbol {W}} ^ {\mathrm{T}} \boldsymbol {h} (\boldsymbol {x}) \tag {7.26}$$

式中， $\hat{W}$ 为估计权值。

在实际的控制系统设计中,为了保证网络的输入值处于高斯基函数的有效范围,应根据网络的输入值实际范围确定高斯基函数中心点坐标向量 c 值,为了保证高斯基函数的有效映射,需要将高斯基函数的宽度 $b_{j}$ 取适当的值。 $\hat{W}$ 的调节是通过闭环的 Lyapunov 函数的稳定性分析中进行设计的。
