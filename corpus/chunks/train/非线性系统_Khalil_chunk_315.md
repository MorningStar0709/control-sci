# 例10.12

\- 设 $g(t,x) = \sum_{k=1}^{N} g_k(t,x)$ , 其中 $g_k(t,x)$ 是以 $T_k$ 为周期的 $t$ 的函数, 当 $i \neq j$ 时, $T_i \neq T_j$ 。函数 $g$ 不是 $t$ 的周期函数①, 但它有平均函数

$$g _ {\mathrm{av}} (x) = \sum_ {k = 1} ^ {N} g _ {k _ {\mathrm{av}}} (x)$$

其中，如10.4节的定义， $g_{k_{\mathrm{av}}}$ 是周期函数 $g_{k}(t,x)$ 的平均。当 $T$ 趋于无穷时，收敛函数 $\sigma$ 是 $O(1 / T)$ ，可取其为 $\sigma (T) = 1 / (T + 1)$ 。

$$g (t, x) = \frac {1}{1 + t} h (x)$$

的平均为零,且收敛函数 $\sigma$ 可取为 $\sigma(T)=(1/T)\ln(T+1)$ 。

现在假设 $f(t,x,0)$ 的平均函数是 $f_{\mathrm{av}}(x)$ ，其收敛函数为 $\sigma$ 。设

$$h (t, x) = f (t, x, 0) - f _ {\mathrm{av}} (x) \tag {10.40}$$

函数 $h(t,x)$ 有一个零平均函数, $\sigma$ 为其收敛函数。假设雅可比矩阵 $\partial h/\partial x$ 有零平均和同一收敛函数 $\sigma$ 。定义

$$w (t, x, \eta) = \int_ {0} ^ {t} h (\tau , x) \exp [ - \eta (t - \tau) ] d \tau \tag {10.41}$$

$\eta$ 为正常数。当 $\eta=0$ 时，函数 $w(t,x,0)$ 满足

$$
\begin{array}{l} \| w (t + \delta , x, 0) - w (t, x, 0) \| = \left\| \int_ {0} ^ {t + \delta} h (\tau , x) d \tau - \int_ {0} ^ {t} h (\tau , x) d \tau \right\| \tag {10.42} \\ = \left\| \int_ {t} ^ {t + \delta} h (\tau , x) d \tau \right\| \leqslant k \delta \sigma (\delta) \\ \end{array}
$$

这就是说，在特殊情况下有

$$\| w (t, x, 0) \| \leqslant k t \sigma (t), \forall (t, x) \in [ 0, \infty) \times D _ {0}$$

因为 $w(0,x,0) = 0$ 。对式(10.41)右边进行分部积分可得

$$
\begin{array}{l} w (t, x, \eta) = w (t, x, 0) - \eta \int_ {0} ^ {t} \exp [ - \eta (t - \tau) ] w (\tau , x, 0) d \tau \\ = \exp (- \eta t) w (t, x, 0) - \eta \int_ {0} ^ {t} \exp [ - \eta (t - \tau) ] [ w (\tau , x, 0) - w (t, x, 0) ] d \tau \\ \end{array}
$$

其中第二个等号通过在右边加减一项

$$\eta \int_ {0} ^ {t} \exp [ - \eta (t - \tau) ] d \tau w (t, x, 0)$$

获得。运用式(10.42)，得

$$\| w (t, x, \eta) \| \leqslant k t \exp (- \eta t) \sigma (t) + k \eta \int_ {0} ^ {t} \exp [ - \eta (t - \tau) ] (t - \tau) \sigma (t - \tau) d \tau \tag {10.43}$$

该不等式可用于证明 $\eta \| w(t,x,\eta)\|$ 是一致有界的，其边界为 $k\alpha (\eta),\alpha$ 为K类函数。例如，如果 $\sigma (t) = 1 / (t + 1)$ ，则有

$$\eta \| w (t, x, \eta) \| \leqslant k \eta \exp (- \eta t) + k \eta^ {2} \int_ {0} ^ {t} \exp [ - \eta (t - \tau) ] d \tau = k \eta$$

定义 $\alpha (\eta) = \eta$ ，得到 $\eta \| w(t,x,\eta)\| \leqslant k\alpha (\eta)$ 。如果 $\sigma (t) = 1(t^r +1)$ ， $0 < r < 1$ ，则有
