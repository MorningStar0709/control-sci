# 例3.8 阶跃和斜坡函数的拉普拉斯变换

求阶跃函数 $a1(t)$ 和斜坡函数 $bt1(t)$ 的拉普拉斯变换。

解答。对于幅值为 a 的阶跃函数， $f(t)=a1(t)$ ，由式(3.32)，得

$$F (s) = \int_ {0} ^ {+ \infty} a \mathrm{e} ^ {- s t} \mathrm{d} t = \frac {- a \mathrm{e} ^ {- s t}}{s} \Big | _ {0} ^ {+ \infty} = 0 - \frac {- a}{s} = \frac {a}{s}, \quad \mathrm{Re} (s) > 0$$

对于斜坡信号 $f(t)=bt1(t)$ ，由式(3.32)，得

$$F (s) = \int_ {0} ^ {\infty} b t \mathrm{e} ^ {- s t} \mathrm{d} t = \left[ - \frac {b t \mathrm{e} ^ {- s t}}{s} - \frac {b \mathrm{e} ^ {- s t}}{s ^ {2}} \right] _ {0} ^ {\infty} = \frac {b}{s ^ {2}}, \quad \mathrm{Re} (s) > 0$$

这里用到分部积分法，即

$$\int u \mathrm{d} v = u v - \int v \mathrm{d} u$$

其中：u=bt； $dv=e^{-st}dt$ 。然后，除了在极点即原点位置，我们可以扩展 $F(s)$ 的有效性到整个的s平面（见附录A）。

更为巧妙的例子是脉冲函数的拉普拉斯变换。
