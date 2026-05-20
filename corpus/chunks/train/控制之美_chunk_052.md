# 3.1.1 状态空间方程表达式

从一个例子入手分析,如图 3.1.1(a) 所示的弹簧质量阻尼系统,在 2.1.2 节中曾经分析过,它的动态微分方程为

$$m \frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} + b \frac {\mathrm{d} x (t)}{\mathrm{d} t} + k x (t) = f (t) \tag {3.1.1}$$

其中， $x(t)$ 是位移，方向向右；m 是质量；b 是阻尼系数；k 是弹簧系数； $f(t)$ 是外力。

![](image/36b80afe51d3ca681271d0520d8d61ccea6e32c43bdbf4e5fa25ace43475b9b8.jpg)  
图 3.1.1 弹簧质量阻尼系统与框图

令此系统的输入等于外力, 即 $u(t) = f(t)$ , 系统的输出等于位移, 即 $y(t) = x(t)$ 。第 2 章介绍了经典控制理论中使用传递函数来描述系统的方法, 对式(3.1.1)等号两边分别进行拉普拉斯变换,并将 $u(t)=f(t)$ 、 $y(t)=x(t)$ 代入进行调整,同时假设零初始条件 $x(0)=\frac{\mathrm{d}x(t)}{\mathrm{d}t}\bigg|_{t=0}=0$ ,可以得到系统的传递函数为

$$G (s) = \frac {Y (s)}{U (s)} = \frac {1}{m s ^ {2} + b s + k} \tag {3.1.2}$$

式(3.1.2)所对应的系统框图如图3.1.1(b)所示。

对于同样的系统,在现代控制理论中则会使用状态空间方程的表达方式。状态空间方程是一个集合,它包含了系统的输入、输出及状态变量,并把它们用一系列的一阶微分方程表达出来。对于本例中的二阶系统,为了将其写成状态空间方程,需要选取合适的状态变量(State Variables),才能使二阶系统转化为一系列的一阶系统。根据这个要求,选取两个状态变量 $z_{1}(t)$ 和 $z_{2}(t)$ ,其中

$$z _ {1} (t) = x (t) \tag {3.1.3}z _ {2} (t) = \frac {\mathrm{d} z _ {1} (t)}{\mathrm{d} t} = \frac {\mathrm{d} x (t)}{\mathrm{d} t} \tag {3.1.4}$$

根据式(3.1.4)，取 $z_{2}(t)$ 对时间的导数，并将式(3.1.1)和 $u(t) = f(t)$ 代入其中，可得

$$
\begin{array}{l} \frac {\mathrm{d} z _ {2} (t)}{\mathrm{d} t} = \frac {\mathrm{d} ^ {2} x (t)}{\mathrm{d} t ^ {2}} = \frac {1}{m} (f (t) - b \frac {\mathrm{d} x (t)}{\mathrm{d} t} - k x (t)) \\ = \frac {1}{m} u (t) - \frac {b}{m} z _ {2} (t) - \frac {k}{m} z _ {1} (t) \tag {3.1.5} \\ \end{array}
$$

现在将式(3.1.3)到(3.1.5)写成紧凑的矩阵表达形式,可得

$$
\frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {k}{m} & - \frac {b}{m} \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + \left[ \begin{array}{l} 0 \\ \frac {1}{m} \end{array} \right] u (t) \tag {3.1.6}
$$

而系统的输出 $y(t) = x(t)$ 也可以写成矩阵形式，即

$$
y (t) = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} z _ {1} (t) \\ z _ {2} (t) \end{array} \right] + [ 0 ] [ u (t) ] \tag {3.1.7}
$$

式(3.1.6)和式(3.1.7)是图3.1.1中弹簧质量阻尼系统的状态空间方程。

上述形式可推广并得到状态空间方程的一般形式,即

$$\frac {\mathrm{d} \boldsymbol {z} (t)}{\mathrm{d} t} = \boldsymbol {A} \boldsymbol {z} (t) + \boldsymbol {B} \boldsymbol {u} (t) \tag {3.1.8a}\mathbf {y} (t) = \mathbf {C z} (t) + \mathbf {D u} (t) \tag {3.1.8b}$$

其中

$z(t)$ 是状态变量, 是一个 n 维向量, $z(t)=\left[z_{1}(t),z_{2}(t),\cdots,z_{n}(t)\right]^{\mathrm{T}}$ ;
