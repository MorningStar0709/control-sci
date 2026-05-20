# 9.2.1 控制律的设计

设性能指标为

$$E (k) = \frac {1}{2} \Bigl (P \bigl (y _ {\mathrm{d}} (k) - y (k) \bigr) ^ {2} + Q \Delta^ {2} u (k) \Bigr) \tag {9.8}$$

式中，P和Q分别为输出误差和控制增量的加权系数； $y_{\mathrm{d}}(k)$ 和 $y(k)$ 分别为k时刻的参考输入和输出。

神经元的输出为

$$u (k) = u (k - 1) + K \sum_ {i = 1} ^ {3} w _ {i} ^ {\prime} (k) x _ {i} (k) \tag {9.9}w _ {i} ^ {\prime} (k) = w _ {i} (k) / \sum_ {i = 1} ^ {3} \left| w _ {i} (k) \right| \quad (i = 1, 2, 3)w _ {1} (k) = w _ {1} (k - 1) + \eta_ {1} K \left[ P b _ {0} z (k) x _ {1} (k) - Q K \sum_ {i = 1} ^ {3} \left(w _ {i} (k) x _ {i} (k)\right) x _ {1} (k) \right] \tag {9.10}w _ {2} (k) = w _ {2} (k - 1) + \eta_ {\mathrm{p}} K \left[ P b _ {0} z (k) x _ {2} (k) - Q K \sum_ {i = 1} ^ {3} \left(w _ {i} (k) x _ {i} (k)\right) x _ {2} (k) \right]w _ {3} (k) = w _ {3} (k - 1) + \eta_ {\mathrm{D}} K \left[ P b _ {0} z (k) x _ {3} (k) - Q K \sum_ {i = 1} ^ {3} \left(w _ {i} (k) x _ {i} (k)\right) x _ {3} (k) \right]$$

式中， $b_{0}$ 为输出响应的第一个值，且

$$x _ {1} (k) = e (k)x _ {2} (k) = e (k) - e (k - 1) \tag {9.11}x _ {3} (k) = \Delta^ {2} e (k) = e (k) - 2 e (k - 1) + e (k - 2)z (k) = e (k)$$

![](image/b42d553c8d46cac46d504e9832378b109ebbc065b4f953ff78790f976e21d4a1.jpg)
