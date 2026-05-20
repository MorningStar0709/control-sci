$$
\begin{array}{l l} s ^ {6}: & 1 \\ s ^ {5}: & 4 \end{array} \quad \begin{array}{l l} 3 & 1 \\ 2 & 4 \end{array} \quad \begin{array}{l l} 4 \\ 0 \end{array}
s ^ {4}: \quad \frac {5}{2} = \frac {4 \times 3 - 1 \times 2}{4} \quad 0 = \frac {4 \times 1 - 4 \times 1}{4} \quad 4 = \frac {4 \times 4 - 1 \times 0}{4}s ^ {3}: \quad 2 = \frac {\frac {5}{2} \times 2 - 4 \times 0}{\frac {5}{2}} \quad - \frac {1 2}{5} = \frac {\frac {5}{2} \times 4 - 4 \times 4}{\frac {5}{2}} \quad 0s ^ {2}: \quad 3 = \frac {2 \times 0 - \frac {5}{2} \times \left(- \frac {1 2}{5}\right)}{2} \quad 4 = \frac {2 \times 4 - \left(\frac {5}{2} \times 0\right)}{2}s: - \frac {7 6}{1 5} = \frac {3 \left(- \frac {1 2}{5}\right) - 8}{3} \quad 0s ^ {0}: \quad 4 = \frac {- \frac {7 6}{1 5} \times 4 - 0}{- \frac {7 6}{1 5}}
$$

我们可推断出，由于第一列的元素不全为正，因此多项式在右半平面有根。事实上，因为有两次符号变化，所以有两个极点位于右半平面 $^{①}$ 。

注意，在计算劳斯阵列时，我们可以通过将某一行乘以或除以一个正数来简化剩余的计算。还要注意最后两行的每一行都具有一个非零元素。

劳斯判据在确定反馈系统保持稳定的参数范围方面也很有用。

例 3.33 相对于参数范围的稳定性

考虑图 3.39 所示的系统。系统的稳定性是

![](image/95f577bd41b342a222b5818efa519045d34c8cea832b431eebd5e5bc4f44125d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r -->|+| Sum
    Sum --> K
    K --> |s + 1 / (s(s + 1)(s + 6))| Output
    Output --> y
```
</details>

图 3.39 用于检验稳定性的反馈系统

一个比例反馈增益 K 的函数。确定系统稳定时 K 的范围。

解答。系统的特征方程为

$$1 + K \frac {s + 1}{s (s - 1) (s + 6)} = 0$$

或

$$s ^ {3} + 5 s ^ {2} + (K - 6) s + K = 0$$

对应的劳斯阵列为

$$
\begin{array}{l} s ^ {3}: \quad 1 \quad K - 6 \\ s ^ {2}: \quad 5 \quad K \\ s: \quad (4 K - 3 0) / 5 \\ s ^ {0}: \quad K \\ \end{array}
$$

系统若要稳定，则下式必须成立：

$$\frac {4 K - 3 0}{5} > 0, \quad K > 0$$

或

$$K > 7. 5, \quad K > 0$$

因此，劳斯方法为稳定性问题提供了一个解析方案。尽管任何满足该不等式的增益都可使系统稳定，但是动态响应也会因 K 值的不同而不同。给增益一个特定的值，我们就可通过求特征多项式的根来计算闭环极点。特征多项式的系数可通过行矢量来表示（按 s 降幂次序），即

$$\mathrm{denT} = [ 1 5 \mathrm{K} - 6 \mathrm{K} ]$$

并且我们可以使用 Matlab 函数计算上式的根，即

$$\text { roots } (\text { denT }).$$

当 K=7.5 时，根为 -5 和 $\pm1.22j$ ，系统是中性稳定的。注意当 K=7.5 时，劳斯方法预测 $j\omega$ 轴上存在极点。如果我们设 K=13，那么闭环极点位于 -0.46 和 $-0.47\pm1.7j$ 处，设 K=25，它们位于 -1.90 和 $-1.54\pm3.27j$ 处，在这两种情况下，系统都如劳斯方法预测的那样是稳定的。图 3.40 所示的为三种增益值的暂态响应曲线。为获取这些暂态响应，我们计算如下闭环传递函数：

![](image/dd24b6a18902e01010b956701446baded361ba87cc7ceef8255c6be273b26ea9.jpg)

<details>
<summary>line</summary>

| 时间/s | K = 7.5 | K = 13 | K = 25 |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 0.0 |
| 2 | 2.5 | 2.0 | 1.0 |
| 4 | -0.5 | 1.0 | 1.0 |
| 6 | 1.0 | 1.0 | 1.0 |
| 8 | 2.5 | 1.0 | 1.0 |
| 10 | -0.5 | 1.0 | 1.0 |
| 12 | 2.5 | 1.0 | 1.0 |
</details>

图 3.40 图 3.39 所示系统的暂态响应

$$T (s) = \frac {Y (s)}{R (s)} = \frac {K (s + 1)}{s ^ {3} + 5 s ^ {2} + (K - 6) s + K}$$

其 Matlab 语句如下。

$$
\begin{array}{l} s = t f \left(^ {\prime} s ^ {\prime}\right); \quad \% \text {define the Laplace variable} \\ \text { sysT } = K ^ {*} (s + 1) / (s ^ {3} + 5 ^ {*} s ^ {2} + (K - 6) ^ {*} s + K); \quad \% \text { define   transfer   function } \\ \text {step(sysT);} \quad \% \text {compute the step response} \\ \end{array}
$$

画出(单位)阶跃响应图。
