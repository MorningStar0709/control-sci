# 8.6.2 反馈特性

在连续系统中，我们采用以下典型的环节开始设计过程：比例、积分或微分控制规律或它们的某种组合，有时还包含滞后。同样的思想可应用在离散化设计中。换句话说，对连续设计的 $D_{c}(s)$ 进行数字化得到的 $D_{d}(z)$ 将产生上述典型设计环节，这些可以作为一个离散化设计的起点。离散控制律如下。

对于比例控制，有

$$u (k) = K e (k) \Rightarrow D _ {\mathrm{d}} (z) = K \tag {8.43}$$

对于微分控制，有

$$u (k) = K T _ {\mathrm{D}} [ e (k) - e (k - 1) ] \tag {8.44}$$

其传递函数为

$$D _ {\mathrm{d}} (z) = K T _ {\mathrm{D}} \left(1 - z ^ {- 1}\right) = K T _ {\mathrm{D}} \frac {z - 1}{z} = k _ {\mathrm{D}} \frac {z - 1}{z} \tag {8.45}$$

对于积分控制，有

$$u (k) = u (k - 1) + \frac {K _ {\mathrm{p}}}{T _ {\mathrm{I}}} e (k) \tag {8.46}$$

其传递函数为

$$D _ {\mathrm{d}} (z) = \frac {K}{T _ {\mathrm{I}}} \Big (\frac {1}{1 - z ^ {- 1}} \Big) = \frac {K}{T _ {\mathrm{I}}} \Big (\frac {z}{z - 1} \Big) = k _ {\mathrm{I}} (\frac {z}{z - 1}) \tag {8.47}$$

对于超前补偿，8.3节的例子表明由连续超前补偿得到的差分方程是如下形式的：

$$u (k + 1) = \beta u (k) + K [ e (k + 1) - \alpha e (k) ] \tag {8.48}$$

其传递函数为

$$D _ {\mathrm{d}} (z) = K \frac {1 - \alpha z ^ {- 1}}{1 - \beta z ^ {- 1}} \tag {8.49}$$
