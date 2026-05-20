$$
\mathbf {S} _ {1} = \left[ \begin{array}{l l} \mathbf {G} (T) & \boldsymbol {\Phi} (T) \mathbf {G} (T) \end{array} \right] = \left[ \begin{array}{c c} \frac {1 - \cos \omega T}{\omega^ {2}} & \frac {\cos \omega T - \cos^ {2} \omega T + \sin^ {2} \omega T}{\omega^ {2}} \\ \frac {\sin \omega T}{\omega} & \frac {2 \sin \omega T \cos \omega T - \sin \omega T}{\omega} \end{array} \right]
$$

离散化后系统的可观测性矩阵为

$$
\mathbf {V} _ {1} = \left[ \begin{array}{l l} \mathbf {C} ^ {T} & \boldsymbol {\Phi} ^ {T} (T) \mathbf {C} ^ {T} \end{array} \right] = \left[ \begin{array}{l l} 1 & \cos \omega T \\ 0 & \frac {\sin \omega T}{\omega} \end{array} \right]
$$

当采样周期 $T=\frac{k\pi}{\omega}(k=1,2,\cdots)$ 时，可控性矩阵 $S_{1}$ 和可观测性矩阵 $V_{1}$ 均出现零行， $\operatorname{rank}S_{1}=1<n,\operatorname{rank}V_{1}=1<n$ ，系统不可控也不可观测。这表明连续系统可控或可观测时，若采样周期选择不当，对应的离散化系统便有可能不可控或不可观测，也有可能既不可控又不可观测。若连续系统不可控或不可观测，不管采样周期 T 如何选择，离散化后的系统一定是不可控或不可观测的。
