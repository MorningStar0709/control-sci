$$
\begin{array}{l} \mathrm{e} ^ {A t} = I + A t + \frac {1}{2} A ^ {2} t ^ {2} + \dots + \frac {1}{(n - 1) !} A ^ {n - 1} t ^ {n - 1} \\ + \frac {1}{n !} A ^ {n} t ^ {n} + \frac {1}{(n + 1) !} A ^ {n + 1} t ^ {n + 1} + \dots + \frac {1}{k !} A ^ {k} t ^ {k} + \dots \\ = I + A t + \frac {1}{2} A ^ {2} t ^ {2} + \dots + \frac {1}{(n - 1) !} A ^ {n - 1} t ^ {n - 1} \\ + \frac {1}{n !} \left(- a _ {n - 1} \mathbf {A} ^ {n - 1} - a _ {n - 2} \mathbf {A} ^ {n - 2} - \dots - a _ {1} \mathbf {A} - a _ {0} \mathbf {I}\right) t ^ {n} \\ + \frac {1}{(n + 1) !} \left[ \left(a _ {n - 1} ^ {2} - a _ {n - 2}\right) A ^ {n - 1} + \left(a _ {n - 1} a _ {n - 2} - a _ {n - 3}\right) A ^ {n - 2} + \dots \right. \\ \left. + \left(a _ {n - 1} a _ {2} - a _ {1}\right) \mathbf {A} ^ {2} + \left(a _ {n - 1} a _ {1} - a _ {0}\right) \mathbf {A} + a _ {n - 1} a _ {0} I \right] t ^ {n + 1} + \dots \\ = \left(1 - \frac {1}{n !} a _ {0} t ^ {n} + \frac {1}{(n + 1) !} a _ {n - 1} a _ {0} t ^ {n + 1} + \dots\right) I + \left[ t - \frac {1}{n !} a _ {1} t ^ {n} \right. \\ \left. + \frac {1}{(n + 1) !} \left(a _ {n - 1} a _ {1} - a _ {0}\right) t ^ {n + 1} + \dots \right] A + \left[ \frac {1}{2} t ^ {2} - \frac {1}{n !} a _ {2} t ^ {n} \right. \\ \left. + \frac {1}{(n + 1) !} \left(a _ {n - 1} a _ {2} - a _ {1}\right) t ^ {n + 1} + \dots \right] A ^ {2} + \dots \\ \end{array}
+ \left[ \frac {1}{(n - 1) !} t ^ {n - 1} - \frac {1}{n !} a _ {n - 1} t ^ {n} + \frac {1}{(n + 1) !} (a _ {n - 1} ^ {2} - a _ {n - 2}) t ^ {n + 1} + \dots \right] A ^ {n - 1}
$$

令 $\alpha_{0}(t)=1-\frac{1}{n!}a_{0}t^{n}+\frac{1}{(n+1)!}a_{n-1}a_{0}t^{n+1}+\cdots$

$$\alpha_ {1} (t) = t - \frac {1}{n !} a _ {1} t ^ {n} + \frac {1}{(n + 1) !} \left(a _ {n - 1} a _ {1} - a _ {0}\right) t ^ {n + 1} + \dots\alpha_ {2} (t) = \frac {1}{2} t ^ {2} - \frac {1}{n !} a _ {2} t ^ {n} + \frac {1}{(n + 1) !} \left(a _ {n - 1} a _ {2} - a _ {1}\right) t ^ {n + 1} + \dots$$

•
•
•

$$\alpha_ {n - 1} (t) = \frac {1}{(n - 1) !} t ^ {n - 1} - \frac {1}{n !} a _ {n - 1} t ^ {n} + \frac {1}{(n + 1) !} \left(a _ {n - 1} ^ {2} - a _ {n - 2}\right) t ^ {n + 1} + \dots$$

则有 $\mathrm{e}^{\mathbf{A}t} = \alpha_{0}(t)\mathbf{I} + \alpha_{1}(t)\mathbf{A} + \alpha_{2}(t)\mathbf{A}^{2} + \cdots + \alpha_{n-1}(t)\mathbf{A}^{n-1} = \sum_{m=0}^{n-1}\alpha_{m}(t)\mathbf{A}^{m}$

故推论2成立。式(9-102)中的 $\alpha_{m}(t)(m=0,1,2,\cdots,n-1)$ 均为t的幂函数，对于 $t\in[0,t_{f}]$ ，不同时刻构成的向量组 $[\alpha_{0}(0),\cdots,\alpha_{n-1}(0)],\cdots,[\alpha_{0}(t_{f}),\cdots,\alpha_{n-1}(t_{f})]$ 是线性无关的向量组，其中任一向量都无法表示成为其他向量的线性组合。同理， $e^{-At}$ 也可表示为A的n-1阶多项式

$$\mathrm{e} ^ {- A t} = \sum_ {m = 0} ^ {n - 1} \alpha_ {m} ^ {\prime} (t) A ^ {m} \tag {9-103}$$

式中
