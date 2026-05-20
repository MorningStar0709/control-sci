$$
\begin{array}{l} z (t) = \left[ \begin{array}{c c} 2 & 2 \\ \mathrm{j} & - \mathrm{j} \end{array} \right] \left[ \begin{array}{l} C _ {1} \cos 2 t + C _ {1} \mathrm{j} \sin 2 t \\ C _ {2} \cos 2 t - C _ {2} \mathrm{j} \sin 2 t \end{array} \right] = \left[ \begin{array}{c} 2 C _ {1} \cos 2 t + 2 C _ {1} \mathrm{j} \sin 2 t + 2 C _ {2} \cos 2 t - 2 C _ {2} \mathrm{j} \sin 2 t \\ \mathrm{j} C _ {1} \cos 2 t - C _ {1} \sin 2 t - \mathrm{j} C _ {2} \cos 2 t - C _ {2} \sin 2 t \end{array} \right] \\ = \left[ \begin{array}{l} 2 (C _ {1} + C _ {2}) \cos 2 t + 2 (C _ {1} - C _ {2}) \mathrm{j} \sin 2 t \\ (C _ {1} - C _ {2}) \mathrm{j} \cos 2 t - (C _ {1} + C _ {2}) \sin 2 t \end{array} \right] \tag {3.3.17} \\ \end{array}
$$

令 $C_{1}+C_{2}=B_{1}, C_{1}-C_{2}=B_{2}$ ，则式(3.3.17)化简为

$$
\mathbf {z} (t) = \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] = \left[ \begin{array}{l} 2 B _ {1} \cos 2 t + 2 B _ {2} \mathrm{j} \sin 2 t \\ B _ {2} \mathrm{j} \cos 2 t - B _ {1} \sin 2 t \end{array} \right] \tag {3.3.18}
$$

根据式(3.3.18)可得

$$
\begin{array}{l} \left(\frac {z _ {1} (t)}{2}\right) ^ {2} + z _ {2} ^ {2} (t) = \left(B _ {1} \cos 2 t + B _ {2} \mathrm{j} \sin 2 t\right) ^ {2} + \left(B _ {2} \mathrm{j} \cos 2 t - B _ {1} \sin 2 t\right) ^ {2} \\ = B _ {1} ^ {2} \cos^ {2} 2 t + 2 B _ {1} B _ {2} \mathrm{j} \cos 2 t \sin 2 t - B _ {2} ^ {2} \sin^ {2} 2 t - \\ B _ {2} ^ {2} \cos^ {2} 2 t - 2 B _ {1} B _ {2} \mathrm{j} \cos 2 t \sin 2 t + B _ {1} ^ {2} \sin^ {2} 2 t \\ = B _ {1} ^ {2} \cos^ {2} 2 t - B _ {2} ^ {2} \sin^ {2} 2 t - B _ {2} ^ {2} \cos^ {2} 2 t + B _ {1} ^ {2} \sin^ {2} 2 t \\ = \left(B _ {1} ^ {2} - B _ {2} ^ {2}\right) \cos^ {2} 2 t + \left(B _ {1} ^ {2} - B _ {2} ^ {2}\right) \sin^ {2} 2 t = \left(B _ {1} ^ {2} - B _ {2} ^ {2}\right) \left(\cos^ {2} 2 t + \sin^ {2} 2 t\right) \\ = B _ {1} ^ {2} - B _ {2} ^ {2} \tag {3.3.19} \\ \end{array}
$$

将 $C_1 + C_2 = B_1, C_1 - C_2 = B_2$ 代入式(3.3.19)可得

$$\left(\frac {z _ {1} (t)}{2}\right) ^ {2} + z _ {2} ^ {2} (t) = \left(C _ {1} + C _ {2}\right) ^ {2} - \left(C _ {1} - C _ {2}\right) ^ {2} = 4 C _ {1} C _ {2} \tag {3.3.20}$$

两边同时乘以 $\frac{1}{4C_{1}C_{2}}$ ，整理后可得

$$\left(\frac {z _ {1} (t)}{4 \sqrt {C _ {1} C _ {2}}}\right) ^ {2} + \left(\frac {z _ {2} (t)}{2 \sqrt {C _ {1} C _ {2}}}\right) ^ {2} = 1 \tag {3.3.21}$$
