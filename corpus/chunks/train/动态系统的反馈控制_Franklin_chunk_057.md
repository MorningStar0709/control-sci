$$b (\dot {y} - \dot {x}) + k _ {\mathrm{s}} (y - x) - k _ {\mathrm{w}} (x - r) = m _ {1} \ddot {x} \tag {2.8}- k _ {s} (y - x) - b (\dot {y} - \dot {x}) = m _ {2} \ddot {y} \tag {2.9}$$

重新整理得

$$\ddot {x} + \frac {b}{m _ {1}} (\dot {x} - \dot {y}) + \frac {k _ {\mathrm{s}}}{m _ {1}} (x - y) + \frac {k _ {\mathrm{w}}}{m _ {1}} x = \frac {k _ {\mathrm{w}}}{m _ {1}} r \tag {2.10}\ddot {y} + \frac {b}{m _ {2}} (\dot {y} - \dot {x}) + \frac {k _ {\mathrm{s}}}{m _ {2}} (y - x) = 0 \tag {2.11}$$

列写这样的系统方程，最常见的错误是符号错误。在上面的推导过程中，确保符号正确的方法是，需要仔细画出物体的位移和位移方向上产生的作用力。一旦获得系统的方程，由实际推理可知，系统明显是稳定的；可以很快地对其符号进行检查。正如我们在第3章的3.6节研究稳定性时可以了解到的，一个稳定系统中，相似的变量总是符号相同的。对于上述系统，方程(2.10)表明 $\ddot{x}$ 、 $\dot{x}$ 和x项的符号都为正，因为系统肯定是稳定的。同样地，在式(2.11)中， $\ddot{y}$ 、 $\dot{y}$ 和y项的符号也都为正。

在零初始条件下，用前面类似的方法可得传递函数。用 s 替代微分方程中的 d/dt，得

$$
\begin{array}{l} s ^ {2} X (s) + s \frac {b}{m _ {1}} (X (s) - Y (s)) + \frac {k _ {\mathrm{s}}}{m _ {1}} (X (s) - Y (s)) + \frac {k _ {\mathrm{w}}}{m _ {1}} X (s) = \frac {k _ {\mathrm{w}}}{m _ {1}} R (s) \\ s ^ {2} Y (s) + s \frac {b}{m _ {2}} (Y (s) - X (s)) + \frac {k _ {s}}{m _ {2}} (Y (s) - X (s)) = 0 \\ \end{array}
$$

经代数运算及重新消元整理，上式满足传递函数

$$\frac {Y (s)}{R (s)} = \frac {\frac {k _ {\mathrm{w}} b}{m _ {1} m _ {2}} \left(s + \frac {k _ {\mathrm{s}}}{b}\right)}{s ^ {4} + \left(\frac {b}{m _ {1}} + \frac {b}{m _ {2}}\right) s ^ {3} + \left(\frac {k _ {\mathrm{s}}}{m _ {1}} + \frac {k _ {\mathrm{s}}}{m _ {2}} + \frac {k _ {\mathrm{w}}}{m _ {1}}\right) s ^ {2} + \left(\frac {k _ {\mathrm{w}} b}{m _ {1} m _ {2}}\right) s + \frac {k _ {\mathrm{w}} k _ {\mathrm{s}}}{m _ {1} m _ {2}}} \tag {2.12}$$

为确定数值，我们从总的汽车质量 1580kg 中减去四个车轮的质量，再除以 4 得到 $m_{2}=375kg$ ，每个车轮的质量可直接测量，得 $m_{1}=20kg$ 。因此，带有数值的传递函数可表示为

$$\frac {Y (s)}{R (s)} = \frac {1 . 3 1 \mathrm{e} 0 6 (s + 1 3 . 3)}{s ^ {4} + (5 1 6 . 1) s ^ {3} + (5 . 6 8 5 \mathrm{e} 0 4) s ^ {2} + (1 . 3 0 7 \mathrm{e} 0 6) s + 1 . 7 3 3 \mathrm{e} 0 7} \tag {2.13}$$

在第 3 章和后面的章节中我们就会明白上述传递函数能够获得汽车行驶在颠簸路面上时，汽车车体对输入的响应。
