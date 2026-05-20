将式(3.1.9c)代入式(3.1.9a)和式(3.1.9b)并进行调整,得到

$$L _ {1} \frac {\mathrm{d} i _ {1} (t)}{\mathrm{d} t} + i _ {1} (t) \left(R _ {1} + R _ {3}\right) - i _ {2} (t) R _ {3} = e _ {1} (t) \tag {3.1.9d}L _ {2} \frac {\mathrm{d} i _ {2} (t)}{\mathrm{d} t} + i _ {2} (t) (R _ {2} + R _ {3}) - i _ {1} (t) R _ {3} = e _ {2} (t) \tag {3.1.9e}$$

选取系统的状态变量 $z(t) = [z_{1}(t), z_{2}(t)]^{\mathrm{T}}$ ，其中

$$z _ {1} (t) = i _ {1} (t) \tag {3.1.10a}z _ {2} (t) = i _ {2} (t) \tag {3.1.10b}$$

将式(3.1.10a)、式(3.1.10b)代入式(3.1.9d)和式(3.1.9e)，调整后可得

$$\frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} = - \left(\frac {R _ {1} + R _ {3}}{L _ {1}}\right) z _ {1} (t) + \frac {R _ {3}}{L _ {1}} z _ {2} (t) + \frac {1}{L _ {1}} e _ {1} (t) \tag {3.1.11a}\frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} = \frac {R _ {3}}{L _ {2}} z _ {1} (t) - \left(\frac {R _ {2} + R _ {3}}{L _ {2}}\right) z _ {2} (t) + \frac {1}{L _ {2}} e _ {2} (t) \tag {3.1.11b}$$

将式(3.1.11a)、式(3.1.11b)写成紧凑的矩阵形式,得到

$$
\left[ \begin{array}{c} \frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} \\ \frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} \end{array} \right] = \left[ \begin{array}{c c} - \left(\frac {R _ {1} + R _ {3}}{L _ {1}}\right) & \frac {R _ {3}}{L _ {1}} \\ \frac {R _ {3}}{L _ {2}} & - \left(\frac {R _ {2} + R _ {3}}{L _ {2}}\right) \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + \left[ \begin{array}{c c} \frac {1}{L _ {1}} & 0 \\ 0 & \frac {1}{L _ {2}} \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] \tag {3.1.12}
$$

系统输出 $y(t)=[i_{1}(t),e_{R_{3}}(t)]^{\mathrm{T}}$ ，可以表达为

$$
\mathbf {y} (t) = \left[ \begin{array}{l} i _ {1} (t) \\ e _ {R _ {3}} (t) \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ R _ {3} & - R _ {3} \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{l} e _ {1} (t) \\ e _ {2} (t) \end{array} \right] \tag {3.1.13}
$$

将式(3.1.12)和式(3.1.13)写成一般形式,可以得到系统的状态空间方程,即

$$\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t)\mathbf {y} (t) = \mathbf {C z} (t) + \mathbf {D u} (t)$$

其中
