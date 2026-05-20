1998年在科罗拉多的Vail举行的SEMATECH AEC/APC会议，设计、建立 $\Theta$ 并阐述了RTP 实验模型的原型。该操作系统如图 10.74 所示，其本质上是一个多变量系统。原型系统使用三输入三输出多变量控制器，采用与步骤 7 相同的设计方法，在一个使用实时操作系统的嵌入式控制平台中得以实现。

连续控制器(即组合式内部模型控制器和估计器)的形式为

$$\dot {x} ^ {\mathrm{c}} = A ^ {\mathrm{c}} x ^ {\mathrm{c}} + B ^ {\mathrm{c}} e\boldsymbol {u} = \boldsymbol {C} ^ {\mathrm{c}} \boldsymbol {x} ^ {\mathrm{c}} \tag {10.52}$$

![](image/985dda141eeb5a3744d540e382a6fdcc8ae24370defa4dfef1f8335f65e21d9f.jpg)

<details>
<summary>natural_image</summary>

Exterior view of a mechanical device with internal components (no visible text or symbols)
</details>

图 10.74 RTP 温度控制实验模型  
(图片来源：Abbas Emami-Naeimi)

其中： $x^{c}=\left[x_{c}^{T}\quad\hat{T}^{T}\right]^{T}$

$$
\boldsymbol {A} ^ {\mathrm{c}} = \left[ \begin{array}{c c} \boldsymbol {0} & \boldsymbol {0} \\ \boldsymbol {B C} _ {\mathrm{c}} & \boldsymbol {A} - \boldsymbol {B K} _ {0} - \boldsymbol {L C} \end{array} \right], \quad \boldsymbol {B} ^ {\mathrm{c}} = \left[ \begin{array}{c} \boldsymbol {B} _ {\mathrm{c}} \\ \boldsymbol {L} \end{array} \right]

\boldsymbol {C} ^ {\mathrm{c}} = \left[ \begin{array}{l l} \boldsymbol {C} _ {\mathrm{c}} & - \boldsymbol {K} _ {0} \end{array} \right] \tag {10.53}
$$

使用 $T_{s}=0.1s$ 的采样时间将控制器离散化(详见第8章)，数字化实现为(用合适的抗饱和逻辑):

$$\boldsymbol {x} _ {k + 1} ^ {\mathrm{c}} = \Phi^ {\mathrm{c}} \boldsymbol {x} _ {k} ^ {\mathrm{c}} + \Gamma^ {\mathrm{c}} \boldsymbol {e} _ {k}\boldsymbol {u} _ {k} = \boldsymbol {C} ^ {\mathrm{c}} \boldsymbol {x} _ {k} ^ {\mathrm{c}} \tag {10.54}$$

实际系统对带有三个灯管电压的参考温度轨线的响应如图 10.75 所示。它与系统的非线性闭环仿真保持很好的一致性(考虑到噪声)。

![](image/826879193f71103831dd9da8eb7cb138b4de4a6af527b11fd0e1eaffb2478ddc.jpg)

<details>
<summary>line</summary>

| 时间/s | T_r | T_y1 | T_y2 | T_y3 |
| --- | --- | --- | --- | --- |
| 0 | 40 | 40 | 40 | 40 |
| 20 | 60 | 50 | 45 | 40 |
| 40 | 60 | 60 | 55 | 40 |
| 60 | 60 | 60 | 60 | 40 |
| 80 | 60 | 60 | 60 | 40 |
| 100 | 50 | 50 | 50 | 40 |
| 120 | 40 | 40 | 40 | 40 |
| 140 | 40 | 40 | 40 | 40 |
</details>

![](image/8e295ff53fc6c0e8ec2a998fcd9a1ef5ec8de83222318b95f4e8894fd48f9d6f.jpg)

<details>
<summary>line</summary>

| 时间/s | Vcmd1 | Vcmd2 | Vcmd3 |
| --- | --- | --- | --- |
| 0 | 1.5 | 1.5 | 1.5 |
| 20 | 2.5 | 2.5 | 2.5 |
| 40 | 3.0 | 2.8 | 2.7 |
| 60 | 2.8 | 2.6 | 2.5 |
| 80 | 2.5 | 2.3 | 2.2 |
| 100 | 2.0 | 1.8 | 1.7 |
| 120 | 1.5 | 1.4 | 1.3 |
| 140 | 1.5 | 1.4 | 1.3 |
</details>

图 10.75 RTP 温度控制实验模型响应

关于 RTP 系统控制及模型化的更多资料，请读者参见 Emami-Naeini 等(2003)、Ebrt 等(1995a, b)、de Roover 等(1998)以及 Gyugyi 等(1993)著作。
