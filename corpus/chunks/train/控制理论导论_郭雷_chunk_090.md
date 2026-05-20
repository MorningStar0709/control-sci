$$\boldsymbol {r} _ {0} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {R} = \boldsymbol {d} ^ {\mathrm{T}},\boldsymbol {r} _ {1} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \boldsymbol {R} = \boldsymbol {r} _ {0} ^ {\mathrm{T}} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) + \boldsymbol {a} _ {0} ^ {\mathrm{T}} \boldsymbol {C},\boldsymbol {r} _ {2} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {2} \boldsymbol {R} = \boldsymbol {r} _ {1} ^ {\mathrm{T}} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) + \boldsymbol {a} _ {1} ^ {\mathrm{T}} \boldsymbol {C},$$

▶
▶
■

$$\boldsymbol {r} _ {\nu_ {0} - 2} ^ {\mathrm{T}} = \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \boldsymbol {R} = \boldsymbol {r} _ {\nu_ {0} - 3} ^ {\mathrm{T}} (\boldsymbol {A} + \boldsymbol {b d} ^ {\mathrm{T}}) + \boldsymbol {a} _ {\nu_ {0} - 3} ^ {\mathrm{T}} \boldsymbol {C}.$$

由此得出

$$
\boldsymbol {R} = \left[ \begin{array}{c} \boldsymbol {h} ^ {\mathrm{T}} \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} \\ \vdots \\ \boldsymbol {h} ^ {\mathrm{T}} \boldsymbol {T} ^ {\nu_ {0} - 2} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} \boldsymbol {r} _ {0} ^ {\mathrm{T}} \\ \boldsymbol {r} _ {1} ^ {\mathrm{T}} \\ \vdots \\ \boldsymbol {r} _ {\nu_ {0} - 2} ^ {\mathrm{T}} \end{array} \right], \tag {1.6.33}
$$

从而由式 (1.6.23), (1.6.32) 和式 (1.6.33) 便得到了要求的 $d^{\mathrm{T}}$ , $\pmb{R}$ 和 $\pmb{B}_{c}$ .

取 $F_{0}=ze^{T}$ ，由 b 和 $d^{T}$ 的定义知， $A+bd^{T}=A+BHC, bh^{T}=BF_{c}$ 。于是

$$
\sigma \left(\left[ \begin{array}{c c} A + B F _ {0} C & B F _ {0} \\ B _ {c} C & A _ {c} \end{array} \right]\right) = \Lambda .
$$

这就完成了定理的证明.

从定理的证明中看出，用动态输出反馈做极点配置的问题，最终归结为寻找矩阵 $A_{c}, B_{c}, F_{c}$ 和 $F_{0}$ . 现把求这些矩阵的步骤归纳如下：

(1) 取 $H_{1}$ , 使得 $\pmb{A} + \pmb{B}\pmb{H}_{1}\pmb{C}$ 为循环矩阵, 令

$$\boldsymbol {A} _ {1} = \boldsymbol {A} + \boldsymbol {B} \boldsymbol {H} _ {1} \boldsymbol {C};$$

(2) 取 $b \in \text{Image}(B)$ , 使得 $(A_1, b)$ 完全能控, 并取 $z$ , 使得 $b = Bz$ ;

(3) 取 $(\nu_0 - 1) \times (\nu_0 - 1)$ 矩阵 $E$ , 向量 $g$ 和 $h$ 为

$$
\boldsymbol {E} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \dots & 1 \\ 0 & 0 & 0 & \dots & 0 \end{array} \right], \quad \boldsymbol {g} = \left[ \begin{array}{l} 0 \\ 0 \\ \vdots \\ 0 \\ 1 \end{array} \right], \quad \boldsymbol {h} ^ {\mathrm{T}} = [ 1 \quad 0 \quad 0 \quad \dots \quad 0 ];
$$
