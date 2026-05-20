![](image/3b22bce0733975d0f0d200a719ba81bd9bd10478e83615f5e27115537ff96078.jpg)  
图9.5.2 串联系统

分析其频率响应,需要将 $s=j\omega_{i}$ 代入 $G_{1}(s)G_{2}(s)$ , 根据复数的性质, 可得

$$
\left| G _ {1} \left(\mathrm{j} \omega_ {\mathrm{i}}\right) G _ {2} \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \right| = \left| G _ {1} \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \right| \left| G _ {2} \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \right| \tag {9.5.5}
$$

在经过对数运算之后，式(9.5.5)可以写成

$$
2 0 \log | G _ {1} (\mathrm{j} \omega_ {\mathrm{i}}) G _ {2} (\mathrm{j} \omega_ {\mathrm{i}}) | = 2 0 \log | G _ {1} (\mathrm{j} \omega_ {\mathrm{i}}) | + 2 0 \log | G _ {2} (\mathrm{j} \omega_ {\mathrm{i}}) | \tag {9.5.6a}
$$

相位为

$$
\angle G _ {1} (\mathrm{j} \omega_ {\mathrm{i}}) G _ {2} (\mathrm{j} \omega_ {\mathrm{i}}) = \angle G _ {1} (\mathrm{j} \omega_ {\mathrm{i}}) + \angle G _ {1} (\mathrm{j} \omega_ {\mathrm{i}}) \tag {9.5.6b}
$$

式(9.5.6)说明串联系统的伯德图等于其子系统伯德图的叠加。因此,如果我们掌握了一些典型系统的伯德图,就可以分析复杂的串联系统了。同时,它也为滤波器的设计提供了思路。
