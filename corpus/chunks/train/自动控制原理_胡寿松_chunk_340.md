# (3) 无源滞后-超前网络

无源滞后-超前网络的电路图如图6-16(a)所示，其传递函数

$$G _ {c} (s) = \frac {(1 + T _ {a} s) (1 + T _ {b} s)}{T _ {a} T _ {b} s ^ {2} + (T _ {a} + T _ {b} + T _ {a b}) s + 1} \tag {6-28}$$

式中 $T_{a} = R_{1}C_{1},\quad T_{b} = R_{2}C_{2},\quad T_{ab} = R_{1}C_{2}$

![](image/43ac98c6b35ac4422739889c263b2812cd3010d9dce382f523e2121a75844c64.jpg)

<details>
<summary>line</summary>

| b | 20lgb | φ_c(ω_c'') |
| --- | --- | --- |
| 0.01 | -40 | -6° |
| 0.02 | -35 | -5.5° |
| 0.03 | -30 | -5° |
| 0.04 | -25 | -4.5° |
| 0.06 | -20 | -4° |
| 0.08 | -15 | -3.5° |
| 0.1 | -10 | -3° |
| 0.2 | -5 | -2° |
| 0.3 | 0 | -1° |
| 0.4 | 5 | -1° |
| 0.6 | 10 | -1° |
| 0.8 | 15 | -1° |
| 1.0 | 20 | -1° |
</details>

图 6-15 无源滞后网络关系曲线 $(1/bT=0.1\omega_{c}^{\prime\prime})$

令式(6-28)的分母二项式有两个不相等的负实根,则式(6-28)可以写为

$$G _ {c} (s) = \frac {(1 + T _ {a} s) (1 + T _ {b} s)}{(1 + T _ {1} s) (1 + T _ {2} s)} \tag {6-29}$$

比较式(6-28)及式(6-29)，可得

$$T _ {1} T _ {2} = T _ {a} T _ {b}T _ {1} + T _ {2} = T _ {a} + T _ {b} + T _ {a b}$$

设 $T_{1} > T_{a},\quad \frac{T_{a}}{T_{1}} = \frac{T_{2}}{T_{b}} = \frac{1}{\alpha}$

其中 $\alpha > 1$ ，则有

$$T _ {1} = \alpha T _ {a}, \quad T _ {2} = \frac {T _ {b}}{\alpha}$$

于是，无源滞后-超前网络的传递函数最后可表示为

$$G _ {c} (s) = \frac {(1 + T _ {a} s) (1 + T _ {b} s)}{(1 + \alpha T _ {a} s) (1 + \frac {T _ {b}}{\alpha} s)} \tag {6-30}$$

其中， $(1 + T_{a}s) / (1 + \alpha T_{a}s)$ 为网络的滞后部分， $(1 + T_{b}s) / (1 + T_{b}s / \alpha)$ 为网络的超前部分。无源滞后-超前网络的对数幅频渐近特性如图6-16(b)所示，其低频部分和高频部分均起于和终于零分贝水平线。由图可见，只要确定 $\omega_{a}, \omega_{b}$ 和 $\alpha$ ，或者确定 $T_{a}, T_{b}$ 和 $\alpha$ 三个独立变量，图6-16(b)的形状即可确定。

![](image/08414cf301c0edbf98eb02a0a0287579812891affc5dde105e7212b4a76ee08b.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors and capacitors labeled R1, R2, C1, C2, U1, U2
</details>

(a)

![](image/832b9255a4ab3580b96d0bf7fd944f25b965e72332ec41045e38164cf67a0f68.jpg)

<details>
<summary>line</summary>

| Frequency | Value |
| --- | --- |
| 0 | ωₐ/α |
| ωₐ | ωₐ |
| ω_b | ω_b |
| αω_b | ω_b |
| 0dB/dec | -20dB/dec |
| 0dB/dec | 0dB/dec |
| 20dB/dec | 20dB/dec |
</details>

(b)   
图 6-16 无源滞后-超前网络及其特性

常用无源校正网络的电路图、传递函数及对数幅频渐近特性，如表 6-1 所示。

表 6-1 常用无源校正网络
