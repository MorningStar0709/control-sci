$$
\begin{array}{l} x _ {\mathrm{ss}} (t) = K _ {1} \mathrm{e} ^ {- \mathrm{j} \omega_ {\mathrm{i}} t} + K _ {2} \mathrm{e} ^ {\mathrm{j} \omega_ {\mathrm{i}} t} \\ = \frac {B + A \mathrm{j}}{2} | G (\mathrm{j} \omega_ {\mathrm{i}}) | \mathrm{e} ^ {- \mathrm{j} \angle G (\mathrm{j} \omega_ {\mathrm{i}})} \mathrm{e} ^ {- \mathrm{j} \omega_ {\mathrm{i}} t} + \frac {B - A \mathrm{j}}{2} | G (\mathrm{j} \omega_ {\mathrm{i}}) | \mathrm{e} ^ {\mathrm{j} \angle G (\mathrm{j} \omega_ {\mathrm{i}})} \mathrm{e} ^ {\mathrm{j} \omega_ {\mathrm{i}} t} \\ = \frac {B + A \mathrm{j}}{2} | G (\mathrm{j} \omega_ {\mathrm{i}}) | \mathrm{e} ^ {\mathrm{j} (- \angle G (\mathrm{j} \omega_ {\mathrm{i}}) - \omega_ {\mathrm{i}} t)} + \frac {B - A \mathrm{j}}{2} | G (\mathrm{j} \omega_ {\mathrm{i}}) | \mathrm{e} ^ {\mathrm{j} (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t)} \\ = \frac {1}{2} \left| G (\mathrm{j} \omega_ {\mathrm{i}}) \right| \left[ (B + A \mathrm{j}) \mathrm{e} ^ {\mathrm{j} (- \angle G (\mathrm{j} \omega_ {\mathrm{i}}) - \omega_ {\mathrm{i}} t)} + (B - A \mathrm{j}) \mathrm{e} ^ {\mathrm{j} (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t)} \right] \tag {9.2.14} \\ \end{array}
$$

根据欧拉公式 $\cos\varphi+j\sin\varphi=e^{j\varphi}$ ，可得

$$
\begin{array}{l} \mathrm{e} ^ {\mathrm{j} (- \angle G (\mathrm{j} \omega_ {\mathrm{i}}) - \omega_ {\mathrm{i}} t)} = \cos (- \angle G (\mathrm{j} \omega_ {\mathrm{i}}) - \omega_ {\mathrm{i}} t) + \mathrm{j} \sin (- \angle G (\mathrm{j} \omega_ {\mathrm{i}}) - \omega_ {\mathrm{i}} t) \\ = \cos (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) - \mathrm{j} \sin (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) \tag {9.2.15a} \\ \end{array}
$$

$$
\mathrm{e} ^ {\mathrm{j} (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t)} = \cos (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) + \mathrm{j} \sin (\angle G (\mathrm{j} \omega_ {\mathrm{i}}) + \omega_ {\mathrm{i}} t) \tag {9.2.15b}
$$

将式(9.2.15a)和式(9.2.15b)代入式(9.2.14)，整理后可得
