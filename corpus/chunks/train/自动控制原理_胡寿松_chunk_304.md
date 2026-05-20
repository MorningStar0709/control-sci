当对数幅频特性 $20\lg |\Phi_1(\mathrm{j}\omega)|$ 和 $20\lg |\Phi_2(\mathrm{j}\frac{\omega}{\lambda})|$ 的横坐标分别取为 $\omega$ 和 $\frac{\omega}{\lambda}$ 时，其对数幅频特性曲线具有相同的形状，按带宽定义可得

$$\omega_ {b _ {1}} = \lambda \omega_ {b _ {2}}$$

即系统 $\Phi_1(s)$ 的带宽频率为系统 $\Phi_2(s)$ 带宽频率的 $\lambda$ 倍。设两个系统的单位阶跃响应分别为 $c_{1}(t)$ 和 $c_{2}(t)$ ，按拉氏变换，有

$$\frac {1}{s} \Phi_ {1} (s) = \int_ {0} ^ {\infty} c _ {1} (t) \mathrm{e} ^ {- s t} \mathrm{d} t = \frac {1}{\lambda} \cdot \frac {1}{\frac {s}{\lambda}} \Phi_ {2} \left(\frac {s}{\lambda}\right) = \int_ {0} ^ {\infty} c _ {2} (\lambda t) \mathrm{e} ^ {- s t} \mathrm{d} t$$

即得

$$c _ {1} (t) = c _ {2} (\lambda t) \tag {5-93}$$

由时域性能指标可知，系统 $\Phi_1(s)$ 的上升时间和过渡过程时间为 $\Phi_2(s)$ 的 $\frac{1}{\lambda}$ 倍。即当系统的带宽扩大 $\lambda$ 倍，系统的响应速度则加快 $\lambda$ 倍。鉴于系统复现输入信号的能力取决于系统的幅频特性和相频特性，对于输入端信号，带宽大，则跟踪控制信号的能力强；而在另一方面，抑制输入端高频干扰的能力则弱，因此系统带宽的选择在设计中应折中考虑，不能一味求大。
