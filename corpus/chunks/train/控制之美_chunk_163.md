$$
\begin{array}{l} \left(A \omega_ {i} + B s\right) N (s) = K _ {1} \left(s - j \omega_ {i}\right) D (s) + K _ {2} \left(s + j \omega_ {i}\right) D (s) + \\ C _ {1} \left(s + \mathrm{j} \omega_ {\mathrm{i}}\right) \left(s - \mathrm{j} \omega_ {\mathrm{i}}\right) \left(s - s _ {\mathrm{p} 2}\right) \dots \left(s - s _ {\mathrm{p} n}\right) + \\ C _ {2} \left(s + \mathrm{j} \omega_ {\mathrm{i}}\right) \left(s - \mathrm{j} \omega_ {\mathrm{i}}\right) \left(s - s _ {\mathrm{p} 1}\right) \left(s - s _ {\mathrm{p} 3}\right) \dots \left(s - s _ {\mathrm{p} n}\right) + \dots + \\ C _ {n} \left(s - \mathrm{j} \omega_ {\mathrm{i}}\right) \left(s + \mathrm{j} \omega_ {\mathrm{i}}\right) \left(s - s _ {\mathrm{pl}}\right) \dots \left(s - s _ {\mathrm{pn} - 1}\right) \tag {9.2.9} \\ \end{array}
$$

将 $s = -j\omega_{i}$ 代入式(9.2.9)，得到

$$
\begin{array}{l} \left(A \omega_ {i} + B (- j \omega_ {i})\right) N (- j \omega_ {i}) = K _ {1} \left(- j \omega_ {i} - j \omega_ {i}\right) D (- j \omega_ {i}) \\ \Rightarrow K _ {1} = \frac {A \omega_ {\mathrm{i}} + B (- \mathrm{j} \omega_ {\mathrm{i}})}{- 2 \mathrm{j} \omega_ {\mathrm{i}}} \frac {N (- \mathrm{j} \omega_ {\mathrm{i}})}{D (- \mathrm{j} \omega_ {\mathrm{i}})} = \frac {B + A \mathrm{j}}{2} G (- \mathrm{j} \omega_ {\mathrm{i}}) \tag {9.2.10} \\ \end{array}
$$

将 $s=j\omega_{i}$ 代入式(9.2.9)，得到

$$
\begin{array}{l} \left(A \omega_ {\mathrm{i}} + B \left(\mathrm{j} \omega_ {\mathrm{i}}\right)\right) N \left(\mathrm{j} \omega_ {\mathrm{i}}\right) = K _ {2} \left(\mathrm{j} \omega_ {\mathrm{i}} + \mathrm{j} \omega_ {\mathrm{i}}\right) D \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \\ \Rightarrow K _ {2} = \frac {A \omega_ {\mathrm{i}} + B (\mathrm{j} \omega_ {\mathrm{i}})}{2 \mathrm{j} \omega_ {\mathrm{i}}} \frac {N (\mathrm{j} \omega_ {\mathrm{i}})}{D (\mathrm{j} \omega_ {\mathrm{i}})} = \frac {B - A \mathrm{j}}{2} G (\mathrm{j} \omega_ {\mathrm{i}}) \tag {9.2.11} \\ \end{array}
$$

其中， $G(\mathrm{j}\omega_{\mathrm{i}})$ 是一个复数，可以写成指数形式，即

$$
G \left(\mathrm{j} \omega_ {\mathrm{i}}\right) = \left| G \left(\mathrm{j} \omega_ {\mathrm{i}}\right) \right| \mathrm{e} ^ {\mathrm{j} \angle G \left(\mathrm{j} \omega_ {\mathrm{i}}\right)} \tag {9.2.12}
$$

传递函数 $G(s)$ 是输出与输入的拉普拉斯变换的比值。当 $s = j\omega_{i}$ 的时候，拉普拉斯变换变成了傅里叶变换。实信号函数的傅里叶变换属于埃尔米特函数（Hermitian Function），符合共轭对称（有兴趣的读者可以参考附录 B）。
