# 4.3.5 PID 控制

把三项放在一起得到比例积分微分(PID)控制器，它在时域里的控制方程为

$$u (t) = k _ {\mathrm{P}} e (t) + k _ {\mathrm{I}} \int_ {t _ {0}} ^ {t} e (\tau) \mathrm{d} \tau + k _ {\mathrm{D}} \dot {e} (t) \tag {4.74}$$

则图 4.2 所示的控制器传递函数变为

$$\frac {U (s)}{E (s)} = D _ {\mathrm{cl}} (s) = k _ {\mathrm{P}} + \frac {k _ {\mathrm{I}}}{s} + k _ {\mathrm{D}} s \tag {4.75}$$

为说明PID控制的效果，考虑式(4.58)所示的二阶被控对象的速度控制。在该例中由 $1+$ $GD_{\mathrm{cl}} = 0$ 得到的特征方程为

$$s ^ {2} + a _ {1} s + a _ {2} + A \left(k _ {\mathrm{P}} + \frac {k _ {\mathrm{I}}}{s} + k _ {\mathrm{D}} s\right) = 0s ^ {3} + a _ {1} s ^ {2} + a _ {2} s + A \left(k _ {\mathrm{P}} s + k _ {\mathrm{I}} + k _ {\mathrm{D}} s ^ {2}\right) = 0 \tag {4.76}$$

合并同类项整理得

$$s ^ {3} + (a _ {1} + A k _ {\mathrm{D}}) s ^ {2} + (a _ {2} + A k _ {\mathrm{P}}) s + A k _ {1} = 0 \tag {4.77}$$

在这个方程中，它的三个根决定系统动态响应的特征，在理论上任意选择方程的三个自由参数 $k_{\mathrm{P}}$ ， $k_{\mathrm{I}}$ 和 $k_{\mathrm{D}}$ ，可任意确定方程的根。若不含微分项，则方程只有两个自由参数，却有三个根，特征方程根的选择将会受到限制。下面用一个数值例子具体地说明这种影响结果。
