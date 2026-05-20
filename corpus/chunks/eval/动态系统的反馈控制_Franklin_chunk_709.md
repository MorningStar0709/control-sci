# 例A.7 一阶系统的斜坡响应

求极点为 $+a$ 的一阶系统的斜坡响应。

解答。令 $f_{1}(t)=t$ 为斜坡输入信号， $f_{2}(t)=\mathrm{e}^{at}$ 为一阶系统的脉冲响应。则由式(A.15)得到

$$\mathcal {L} ^ {- 1} \left\{\frac {1}{s ^ {2}} \frac {1}{s - a} \right\} = f _ {1} (t) * f _ {2} (t) = \int_ {0} ^ {t} f _ {1} (\tau) f _ {2} (t - \tau) \mathrm{d} \tau = \int_ {0} ^ {t} \tau \mathrm{e} ^ {a (t - \tau)} \mathrm{d} \tau = \frac {1}{a ^ {2}} (\mathrm{e} ^ {a t} - a t - 1)$$

在 Matlab 中使用如下命令也可以得到相同的结果，

syms s ta

ilaplace(1/(s^3-a\*s^2)).

![](image/cf085961ee304a890e5f3c236c2b682d6e73282c5f23e557ca43327decd18fab.jpg)

<details>
<summary>text_image</summary>

t
t = τ
0
τ
τ
</details>

图A.1 积分逆的阶数图
