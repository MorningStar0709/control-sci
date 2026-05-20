$$
\begin{array}{l} \sum_ {n = 1} ^ {\infty} \frac {a _ {n} + \mathrm{j} b _ {n}}{2} \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} = \sum_ {n = - \infty} ^ {- 1} \frac {a _ {(- n)} + \mathrm{j} b _ {(- n)}}{2} \mathrm{e} ^ {- \mathrm{j} (- n) \omega_ {T} t} \\ = \sum_ {n = - \infty} ^ {- 1} \frac {a _ {(- n)} + \mathrm{j} b _ {(- n)}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \tag {B.4.4b} \\ \end{array}
$$

将式(B.4.4a)和式(B.4.4b)代入式(B.4.3)，得到

$$f _ {T} (t) = \sum_ {n = 0} ^ {0} \frac {a _ {0}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} + \sum_ {1} ^ {\infty} \frac {a _ {n} - \mathrm{j} b _ {n}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} + \sum_ {n = - \infty} ^ {- 1} \frac {a _ {(- n)} + \mathrm{j} b _ {(- n)}}{2} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \tag {B.4.5}$$

观察式(B.4.5)，可以发现加和部分中的 $n$ 覆盖了 $[- \infty, \infty]$ 的全部整数，因此式(B.4.5)可以写成

$$f _ {T} (t) = \sum_ {n = - \infty} ^ {\infty} c _ {n} \mathrm{e} ^ {\mathrm{j} n \omega_ {T} t} \tag {B.4.6}$$

其中，

$$
c _ {n} = \left\{ \begin{array}{l l} \frac {a _ {0}}{2}, & n = 0 \\ \frac {a _ {n} - \mathrm{j} b _ {n}}{2}, & n = 1, 2, 3, \dots \\ \frac {a _ {(- n)} + \mathrm{j} b _ {(- n)}}{2}, & n = - 1, - 2, - 3, \dots \end{array} \right. \tag {B.4.7}
$$

计算 $c_{n}$ ，将式(B.3.8b)代入式(B.4.7)，其中

当 $n = 0$ 时

$$
\begin{array}{l} c _ {n} = \frac {a _ {0}}{2} = \frac {1}{2} \frac {2}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{d} t = \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{d} t \\ = \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{e} ^ {- \mathrm{j} 0 \omega_ {T} t} \mathrm{d} t \tag {B.4.8a} \\ \end{array}
$$

当 $n = 1,2,3,\dots$ 时

$$
\begin{array}{l} c _ {n} = \frac {a _ {n} - \mathrm{j} b _ {n}}{2} = \frac {1}{2} \left(\frac {2}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \cos n \omega_ {T} t \mathrm{d} t - \mathrm{j} \frac {2}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \sin n \omega_ {T} t \mathrm{d} t\right) \\ = \frac {1}{T} \left(\int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) (\cos n \omega_ {T} t - j \sin n \omega_ {T} t) d t \right. \\ = \frac {1}{T} \int_ {- \frac {T}{2}} ^ {\frac {T}{2}} f _ {T} (t) \mathrm{e} ^ {- \mathrm{j} n \omega_ {T} t} \mathrm{d} t \tag {B.4.8b} \\ \end{array}
$$

当 $n=-1,-2,-3,\cdots$ 时
