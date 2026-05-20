# 10.2.2 混合策略

当不存在最优纯策略解(极小极大解)时,可以采用混合策略。这时局中人分别以不同的概率来混合选取纯策略。设 u 以概率 $P_{u}$ 使用策略 $u_{1}$ , 以概率 $(1 - P_{u})$ 使用策略 $u_{2}$ ; v 以概率 $P_{v}$ 使用策略 $v_{1}$ , 以概率 $(1 - P_{v})$ 使用策略 $v_{2}$ 。仍用图 10-2 所示的例子期望支付为

$$
\begin{array}{l} E \left(P _ {u}, P _ {v}\right) = L _ {1 1} P _ {u} P _ {v} + L _ {1 2} P _ {u} \left(1 - P _ {v}\right) + L _ {2 1} \left(1 - P _ {u}\right) P _ {v} + \\ L _ {2 2} \left(1 - P _ {u}\right) \left(1 - P _ {v}\right) \\ = 1 1 P _ {u} P _ {v} + 7 P _ {u} \left(1 - P _ {v}\right) + 5 \left(1 - P _ {u}\right) P _ {v} + \\ 9 (1 - P _ {u}) (1 - P _ {v}) \\ = 8 \left(P _ {u} - \frac {1}{2}\right) \left(P _ {v} - \frac {1}{4}\right) + 8 \tag {10-4} \\ \end{array}
$$

从上式可见, 当 $u$ 先开局, 取 $P_u = \frac{1}{2}$ 时, $u$ 方的最小期望支付为 8 , 他不能期望比这更小的支付, 因为 $v$ 方会取 $P_v = \frac{1}{4}$ 使得 $u$ 的支付 $E(P_u, P_v)$ 不小于 8 , 因此 8 是 $u$ 方所期望的最小支付。而 $u$ 的支付就是 $v$ 的赢得, 因此 $v$ 的最大期望赢得也是 8 , 他不能期望有更大的赢得, 因为 $u$ 会取 $P_u = \frac{1}{2}$ 使得 $v$ 的赢得不大于 8 , 这样就有

$$\min _ {P _ {u}} \max _ {P _ {v}} E (P _ {u}, P _ {v}) = \max _ {P _ {v}} \min _ {P _ {u}} E (P _ {u}, P _ {v}) = 8 \tag {10-5}$$

这种对策称为概率的混合对策，而 $\left(P_{u} = \frac{1}{2}, P_{v} = \frac{1}{4}\right)$ 就是最优对策解。

上述求解最优对策的过程可以化为求解一组不等式。设 u 的期望最小支付（即 v 的期望最大赢得）为 $E^{*}$ （上例中 $E^{*}=8$ ），于是有

$$
\left\{ \begin{array}{l l} 1 1 P _ {u} + 5 (1 - P _ {u}) \geqslant E ^ {*} & (\text {固定用} v _ {1}, u \text {可选}) \\ 7 P _ {u} + 9 (1 - P _ {u}) \geqslant E ^ {*} & (\text {固定用} v _ {2}, u \text {可选}) \end{array} \right. \tag {10-6-a}

\left\{ \begin{array}{l l} 1 1 P _ {v} + 7 (1 - P _ {v}) \leqslant E ^ {*} & (\text {固定用} u _ {1}, v \text {可选}) \\ 5 P _ {v} + 9 (1 - P _ {v}) \leqslant E ^ {*} & (\text {固定用} u _ {2}, v \text {可选}) \end{array} \right. \tag {10-6-b}
P _ {u} \geqslant 0, \quad P _ {v} \geqslant 0 \tag {10-6-c}
$$

用图形表示上述两组不等式的求解,如图 10-3 所示

![](image/d1031db852d25915d9cedb089d4c35ce7d9a41bff6148d68623caccea50d5ef1.jpg)

<details>
<summary>line</summary>

| P_u | u固定的支付 | v固定的支付 |
| --- | --- | --- |
| 0 | 9 | 5 |
| 1/2 | 9 | 8 |
| 1 | 11 | 7 |
</details>

![](image/6c57898d377b7ff37be738d9b2aceb4d7b1db9bd519ae153841b29506446656d.jpg)

<details>
<summary>line</summary>

| P_v | u1 固定 | u2 固定 |
| --- | --- | --- |
| 0 | 9 | 7 |
| 1/4 | 9 | 7 |
| 1 | 11 | 5 |
</details>

图10-3 不等式求解示意图

求解的结果是 $P_{u}=\frac{1}{2}, P_{v}=\frac{1}{4}, E^{*}=8$ 。不难发现，上述一组不等式的求解与线性规划理论有紧密联系。
