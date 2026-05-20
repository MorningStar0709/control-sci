$$
\left[ \begin{array}{c c} \frac {\partial f _ {1}}{\partial z _ {1} (t)} & \frac {\partial f _ {1}}{\partial z _ {2} (t)} \\ \frac {\partial f _ {2}}{\partial z _ {1} (t)} & \frac {\partial f _ {2}}{\partial z _ {2} (t)} \end{array} \right] \Bigg | _ {z = z _ {\mathrm{f}}} = \left[ \begin{array}{c c} \frac {\partial (z _ {2} (t))}{\partial z _ {1} (t)} & \frac {\partial (z _ {2} (t))}{\partial z _ {2} (t)} \\ \frac {\partial \left(1 - \frac {1}{z _ {1} (t)} - z _ {2} (t)\right)}{\partial z _ {1} (t)} & \frac {\partial \left(1 - \frac {1}{z _ {1} (t)} - z _ {2} (t)\right)}{\partial z _ {2} (t)} \end{array} \right] \Bigg | _ {z = z _ {\mathrm{f}}}

= \left[ \begin{array}{c c} 0 & 1 \\ \frac {1}{z _ {1} ^ {2} (t)} & - 1 \end{array} \right] \Bigg | _ {z = z _ {\mathrm{f}}} = \left[ \begin{array}{c c} 0 & 1 \\ 1 & - 1 \end{array} \right] \tag {A.12}
$$

因此，它的线性化后的结果为

$$
\frac {\mathrm{d} \boldsymbol {z} _ {\delta} (t)}{\mathrm{d} t} = \left[ \begin{array}{c c} 0 & 1 \\ 1 & - 1 \end{array} \right] \boldsymbol {z} _ {\delta} (t) \tag {A.13}
$$

展开为

$$\frac {\mathrm{d} z _ {\delta 1} (t)}{\mathrm{d} t} = z _ {\delta 2} (t) \tag {A.14a}\frac {\mathrm{d} z _ {\delta 2} (t)}{\mathrm{d} t} = z _ {\delta 1} (t) - z _ {\delta 2} (t) \tag {A.14b}$$

其结果与式(A.7)所表达的结果一致。
