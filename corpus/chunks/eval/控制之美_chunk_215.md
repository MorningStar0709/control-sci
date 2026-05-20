# - 观测器设计：

- 系统能观测的充分必要条件：能观测矩阵 $O=[C\quad CA\quad CA^{2}\quad\cdots\quad CA^{n-1}]^{T}$ 的秩为 n。  
- 线性观测器: $\frac{\mathrm{d}\hat{z}(t)}{\mathrm{d}t} = (A - LC)\hat{z}(t) + (B - LD)u(t) + Ly(t)$ , 设计 $L$ 使得 $(A - LC)$ 的特征值实部都为负数。  
- 当控制器与观测器结合的时候，观测器的收敛速度要快于控制器。
