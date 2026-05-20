事实上，对于图7.5.4所示系统，令 $G(s) = \begin{bmatrix} T_1(s) & T_2(s) \\ T_3(s) & 0 \end{bmatrix}$ ， $K(s) = -Q(s)$ ，这里0为 $l \times l$ 零矩阵， $l > 0$ 为相应整数。模型匹配系统的 $H_\infty$ 控制问题即是上述标准 $H_\infty$ 控制问题。为此只须说明，对任意 $Q(s) \in \mathcal{R}H_\infty$ ，相应于 $u(s) = -Q(s)y(s)$ 的闭环系统当 $w(s) = 0$ 时都是内部渐近稳定的。注意到由于 $T_i(s) \in \mathcal{R}H_\infty, i = 1,2,3,$ 依定义存在多项式矩阵 $P_i(s), R_i(s), \det P_i(s) = 0$ 为稳定多项式， $i = 1,2,3,$ 并满

足

$$T _ {1} (s) = P _ {1} ^ {- 1} (s) R _ {1} (s),T _ {2} (s) = R _ {2} (s) P _ {2} ^ {- 1} (s),T _ {3} (s) = P _ {3} ^ {- 1} (s) R _ {3} (s).$$

易知

$$
\begin{array}{l} G (s) = \left[ \begin{array}{c c} T _ {1} (s) & T _ {2} (s) \\ T _ {3} (s) & 0 \end{array} \right] = \left[ \begin{array}{c c} P _ {1} ^ {- 1} (s) R _ {1} (s) & R _ {2} (s) P _ {2} ^ {- 1} (s) \\ P _ {3} ^ {- 1} (s) R _ {3} (s) & 0 \end{array} \right] \\ = \left[ \begin{array}{c c} P _ {1} ^ {- 1} (s) & 0 \\ 0 & P _ {3} ^ {- 1} (s) \end{array} \right] \left[ \begin{array}{c c} R _ {1} (s) & P _ {1} (s) R _ {2} (s) \\ R _ {3} (s) & 0 \end{array} \right] \left[ \begin{array}{c c} I & 0 \\ 0 & P _ {2} ^ {- 1} (s) \end{array} \right] \\ = \left[ \begin{array}{c c} P _ {1} (s) & 0 \\ 0 & P _ {3} (s) \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} R _ {1} (s) & P _ {1} (s) R _ {2} (s) P _ {2} ^ {- 1} (s) \\ R _ {3} (s) & 0 \end{array} \right]. \\ \end{array}
$$

由此可见 $G(s)$ 为稳定矩阵。此外，对任意 $Q(s) \in \mathcal{R}H_{\infty}$ ，将 $u(s) = -Q(s)y(s)$ 代入式(7.5.5)，则当 $w(s) = 0$ 时，相应闭环系统的传递函数阵为 $T_{2}(s)Q(s)$ 。由于 $T_{2}(s), Q(s)$ 都是稳定矩阵，所以相应闭环系统是内部稳定的。

由于模型匹配 $H_{\infty}$ 控制问题比较简单，且有较好的解法，而标准 $H_{\infty}$ 控制问题又可转化为它，因此研究模型匹配 $H_{\infty}$ 控制问题很有意义.

注意“最优问题”一般不易求解。另一方面，对一个实际工程设计问题，也未必要寻求到严格的“最优问题”的控制器，而只要求得到能满足工程设计要求的控制器即可。于是，可按求解如下“次优问题”进行设计：

系统 (7.5.1) 的 $H_{\infty}$ 控制次优问题是指：求控制矩阵 $K(s)$ ，使得当 $w(s) = 0$ 时， $u(s) = K(s)y(s)$ 能镇定系统 (7.5.1) 的同时，又能使不等式

$$\sup _ {\omega} \sigma_ {\max} \left[ F _ {l} ^ {\mathrm{H}} (\mathrm{j} \omega) F _ {l} (\mathrm{j} \omega) \right] < \gamma$$

对尽可能小的 $\gamma \in (0,1)$ 成立.

注意到 $H_{\infty}$ 控制问题要求解 $H_{2}$ 空间中的极小极大问题，因此次优问题求解也不容易。将干扰抑制问题放到状态空间中进行处理，可望得到相对容易的求解方法。特别地，可望得到一类非线性系统的 $H_{\infty}$ 控制设计方法。通过求得图7.5.3中对象 $G(s)$ 的状态空间实现，借助于有理分式阵的 $H_{\infty}$ 范数与其 $H_{2}$ 范数之间的联系，利用Laplace变换等工具，可将频域中的 $H_{\infty}$ 控制问题转到时域中的 $H_{\infty}$ 控制进行论述和处理。

时域中的 $H_{\infty}$ 控制.

考察受外干扰的线性定常系统，其状态空间描述如下：

$$
\left\{ \begin{array}{l} \dot {x} = A x + B _ {1} w + B _ {2} u, \\ z = C _ {1} x + D _ {1 1} w + D _ {1 2} u, \\ y = C _ {2} x + D _ {2 1} w, \end{array} \right. \tag {7.5.8}
$$
