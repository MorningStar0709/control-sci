# 2. 实际映射 $(\mathbf{AC} \rightarrow \mathbf{AP})$

实际映射是指由概念存储器 AC 中的 c 个单元映射至实际存储器 AP 的 c 个单元, c 个单元中存放着相应权值。网络的输出为 AP 中 c 个单元的权值的和。

采用杂散编码技术中除留余数法实现 CMAC 的实际映射。设杂凑表长为 $m(m$ 为正整数），

以元素值 $s_{i}(k)$ 除以某数 $N(c \leqslant N \leqslant m)$ 后所得余数 +1 作为杂凑地址，实现实际映射，即

$$\mathrm{ad} (i) = (s _ {i} (k) \mathrm{MOD} N) + 1 \tag {8.10}$$

式中，MOD()为取余的Matlab函数， $i=1,2,\cdots,c$ 。

若只考虑单输出,则输出为

$$y _ {n} = \sum_ {i = 1} ^ {c} w (\mathrm{ad} (i)) \tag {8.11}$$

CMAC 采用的学习算法如下：

采用 $\delta$ 学习规则调整权值, 权值调整指标为

$$E = \frac {1}{2} e (t) ^ {2} \tag {8.12}$$

式中， $e(t)=y(t)-y_{n}(t)$ ， $y(t)$ 为理想的输出。

采用梯度下降法,权值按下式调整

$$\Delta w _ {j} (t) = - \eta \frac {\partial E}{\partial w _ {j}} = \eta (y (t) - y _ {n} (t)) \frac {\partial y _ {n}}{\partial w _ {j}} = \eta e (t) \tag {8.13}w _ {j} (t) = w _ {j} (t - 1) + \Delta w _ {j} (t) + \alpha (w _ {j} (t - 1) - w _ {j} (t - 2)) \tag {8.14}$$

式中， $\eta$ 为学习速率， $\alpha$ 为动量因子， $\eta\in(0,1),\alpha\in(0,1),j=\mathrm{ad}(i),i=1,2,\cdots,c$ 。
