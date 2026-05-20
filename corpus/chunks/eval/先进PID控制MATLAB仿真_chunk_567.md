# 14.3.4 仿真实例

仿真对象为 14.2 节的对象，考虑平面两关节机械手，机械手的动力学方程为

$$D (q) \ddot {q} + C (q, \dot {q}) \dot {q} + G (q) = \tau$$

其中

$$
\boldsymbol {D} (\boldsymbol {q}) = \left[ \begin{array}{c c} m _ {1} + m _ {2} + 2 m _ {3} \cos q _ {2} & m _ {2} + m _ {3} \cos q _ {2} \\ m _ {2} + m _ {3} \cos q _ {2} & m _ {2} \end{array} \right]

C (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \left[ \begin{array}{c c} - m _ {3} \dot {q} _ {2} \sin q _ {2} & - m _ {3} \left(\dot {q} _ {1} + \dot {q} _ {2}\right) \sin q _ {2} \\ m _ {3} \dot {q} _ {1} \sin q _ {2} & 0. 0 \end{array} \right]

\boldsymbol {G} (\boldsymbol {q}) = \left[ \begin{array}{l} m _ {4} g \cos q _ {1} + m _ {5} g \cos (q _ {1} + q _ {2}) \\ m _ {5} g \cos (q _ {1} + q _ {2}) \end{array} \right]
$$

式中， $m_{i}$ 值由式 $M = P + p_{l}L$ 给出，有

$$
\boldsymbol {M} = \left[ \begin{array}{l l l l l} m _ {1} & m _ {2} & m _ {3} & m _ {4} & m _ {5} \end{array} \right] ^ {\mathrm{T}}

\boldsymbol {P} = \left[ \begin{array}{l l l l l} p _ {1} & p _ {2} & p _ {3} & p _ {4} & p _ {5} \end{array} \right] ^ {\mathrm{T}}

\boldsymbol {L} = \left[ \begin{array}{l l l l l} l _ {1} ^ {2} & l _ {2} ^ {2} & l _ {1} l _ {2} & l _ {1} & l _ {2} \end{array} \right] ^ {\mathrm{T}}
$$

式中， $p_{1}$ 为负载； $l_{1}$ 和 $l_{2}$ 分别为关节 1 和关节 2 的长度；P 为机械手自身的参数向量。机械力臂实际参数为 $p_{l}=0.50$ ， $P=\left[1.66\quad0.42\quad0.63\quad3.75\quad1.25\right]^{T}$ ， $l_{1}=l_{2}=1$ 。

在笛卡尔空间中的理想跟踪轨迹取 $x_{c1}=1.0-0.2\cos\pi t,\quad x_{c2}=1.0+0.2\sin\pi t$ ，该轨迹为一个半径为0.2、圆心在 $(x_{1},x_{2})=(1.0,1.0)$ 的圆。初始条件为 $\boldsymbol{x}(0)=[0.85\quad1.05]$ ， $\dot{\boldsymbol{x}}(0)=[0.0\quad0.0]$ 。

由于跟踪轨迹为工作空间中的直角坐标，而不是关节空间中的角位置，应按式（14.5）和式（14.6）将工作空间中的关节末端直角坐标 $(x_{1},x_{2})$ 转为关节角位置 $(q_{1},q_{2})$ 。

仿真中，首先通过式（14.14）求 $F_{e}$ ，然后由式（14.16）求 $x_{d}$ 。接触面在 $x_{1}=1.0$ 处，存在以下两种情况：

（1）当 $x_{1} \leqslant 1.0$ 时，机械手末端没有接触障碍物， $F_{\mathrm{e}} = [0 0]^{\mathrm{T}}$ ；  
（2）当 $x_{1}\geqslant1.0$ 时，机械手末端点停留在触障碍物上，此时 $x_{1}=1.0,\quad\dot{x}_{1}=0,\quad\ddot{x}_{1}=0$ 。

障碍物的阻尼参数为 $M_{m} = diag[1.0]$ ， $B_{m} = diag[10]$ 和 $K_{m} = diag[50]$ 。

控制器取式（14.17），控制器的增益选为 $K_{p}=\begin{bmatrix}30&0\\ 0&30\end{bmatrix}$ ， $K_{d}=\begin{bmatrix}30&0\\ 0&30\end{bmatrix}$ 。仿真结果如图 14-9～图 14-13 所示。

![](image/287321cf1c96d53fa03fbe7016e902eb1d7dc9c7c7fdd42a554ea04d48ebc945.jpg)

<details>
<summary>line</summary>
