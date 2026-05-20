# 例 7.15 无阻尼振荡器的阿克曼公式

(1) 使用阿克曼公式求解例 7.14 中无阻尼振荡器的增益。  
(2) 取 $\omega_{0}=1$ ，用 Matlab 验证计算结果。

解答。

(1) 期望的特征方程为 $\alpha_{c}(s)=(s+2\omega_{0})^{2}$ 因此，期望特征多项式的系数为

$$\alpha_ {1} = 4 \omega_ {0}, \quad \alpha_ {2} = 4 \omega_ {0} ^ {2}$$

代入到式 $(7.90)$ 得

$$
\begin{array}{l} \alpha_ {c} (\mathbf {A}) = \left[ \begin{array}{c c} - \omega_ {0} ^ {2} & 0 \\ 0 & - \omega_ {0} ^ {2} \end{array} \right] + 4 \omega_ {0} \left[ \begin{array}{c c} 0 & 1 \\ - \omega_ {0} ^ {2} & 0 \end{array} \right] + 4 \omega_ {0} ^ {2} \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right] (7.91a) \\ = \left[ \begin{array}{c c} 3 \omega_ {0} ^ {2} & 4 \omega_ {0} \\ - 4 \omega_ {0} ^ {3} & 3 \omega_ {0} ^ {2} \end{array} \right] (7.91b) \\ \end{array}
$$

能控性矩阵为

$$
\boldsymbol {C} = \left[ \begin{array}{l l} \boldsymbol {B} & \boldsymbol {A B} \end{array} \right] = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right].
$$

由此得到

$$
\boldsymbol {C} ^ {- 1} = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \tag {7.92}
$$

最后，将式(7.92)和式(7.91a)代入式(7.88)，得到

$$
\begin{array}{l} \boldsymbol {K} = \left[ \begin{array}{l l} K _ {1} & K _ {2} \end{array} \right] \\ = [ 0 \quad 1 ] \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c c} 3 \omega_ {0} ^ {2} & 4 \omega_ {0} \\ - 4 \omega_ {0} ^ {3} & 3 \omega_ {0} ^ {2} \end{array} \right] \\ \end{array}
$$

因此，

$$
\boldsymbol {K} = \left[ \begin{array}{c c} 3 \omega_ {0} ^ {2} & 4 \omega_ {0} \end{array} \right]
$$

这与之前我们得到的结果是一样的。

(2) Matlab 语句如下。

```matlab
wo = 1;
A = [0 1; -wo * wo 0];
B = [0; 1];
pc = [-2 * wo; -2 * wo];
K = acker(A, B, pc) 
```

470

得到 K=[3 4]，这与手工计算结果一样。

正如前面提到的，可控性矩阵的计算数值精度很差，这使得我们将注意力转移到阿克曼公式上去。式(7.88)在Matlab中可用acker函数来实现，可用该式对状态数目不多（≤10）的单输入单输出系统进行设计。对于更复杂的情况，可以找到更可靠的公式，而这个公式可在Matlab中用place函数实现。关于place函数有一个适当的限制条件，因为place函数是建立在分配闭环特征矢量的基础上的，所以期望的闭环极点不可以重叠；即极点必须是不相同的 $^{①}$ ，但是对于acker函数就没有这样的限制条件。
