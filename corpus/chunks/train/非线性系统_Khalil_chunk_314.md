# 10.6 一般平均化法

设系统为 $\dot{x}=\varepsilon f(t,x,\varepsilon)$ (10.39)

其中，对于每个紧集 $D_0 \subset D$ ，以及 $(t, x, \varepsilon) \in [0, \infty) \times D_0 \times [0, \varepsilon_0]$ ， $f$ 及其对 $(x, \varepsilon)$ 的一阶和二阶偏导数是连续有界的,参数 $\varepsilon$ 是正数, $D \subset R^{n}$ 是定义域。平均化法应用于系统(10.39)的情况比应用于 $f(t,x,\varepsilon)$ 是 t 的周期函数中更具一般性,特别是当函数 $f(t,x,0)$ 有一个根据下面的定义进行严格定义的平均函数 $f_{\mathrm{av}}(x)$ 时。

定义10.2 对于连续有界函数 $g: [0, \infty) \times D \to R^n$ ，如果极限

$$g _ {\mathrm{av}} (x) = \lim _ {T \rightarrow \infty} \frac {1}{T} \int_ {t} ^ {t + T} g (\tau , x) d \tau$$

存在,且对于每个紧集 $D_{0}\subset D$ ,有

$$\left\| \frac {1}{T} \int_ {t} ^ {t + T} g (\tau , x) d \tau - g _ {\mathrm{av}} (x) \right\| \leqslant k \sigma (T), \forall (t, x) \in [ 0, \infty) \times D _ {0}$$

其中 $k$ 为正常数（可能与 $D_0$ 有关），且 $\sigma: [0, \infty) \to [0, \infty)$ 是严格递减的连续有界函数，使得当 $T$ 趋于无穷时， $\sigma(T)$ 趋于零，则称函数 $g$ 有一个平均函数 $g_{\mathrm{av}}(x)$ 。函数 $\sigma$ 称为收敛函数。
