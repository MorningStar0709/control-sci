# 16.1.5 基于 LMI 的 $H_{\infty}$ 控制

定理 $^{[3]}$ 对于式（16.4），给定 $\gamma>0$ ，存在 $P_{1}=P_{1}^{T}>0$ 和 $P_{2}$ ，如果满足不等式：

$$
\left[ \begin{array}{c c} A P _ {1} + P _ {1} A ^ {\mathrm{T}} + B _ {2} P _ {2} + P _ {2} ^ {\mathrm{T}} B _ {2} ^ {\mathrm{T}} + \gamma^ {- 2} B _ {1} B _ {1} ^ {\mathrm{T}} & \left(C _ {1} P _ {1} + D _ {1 2} P _ {2}\right) ^ {\mathrm{T}} \\ C _ {1} P _ {1} + D _ {1 2} P _ {2} & - I \end{array} \right] <   0 \tag {16.13}
$$

则状态反馈控制器为

$$u = K x = P _ {2} P _ {1} ^ {- 1} x \tag {16.14}$$

式中， $K=\left[k_{1}\quad k_{2}\quad k_{3}\quad k_{4}\right]$ 。

实现倒立摆控制律的设计，采用定理求解倒立摆系统式（16.4）的状态反馈控制增益 K 时，需要两个 LMI，其中一个 LMI 为式（16.13），另一个 LMI 为 $P_{1} > 0$ ，即

$$- P _ {1} < 0 \tag {16.15}$$

![](image/8554228d53e98a5eacdf89b7c6fe837fdac17777de1ba70176ad33ccc93d8006.jpg)
