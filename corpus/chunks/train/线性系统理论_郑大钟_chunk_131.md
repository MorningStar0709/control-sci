$$
\begin{array}{l} \hat {A} (t) = R ^ {- 1} (t) A (t) R (t) + \dot {R} ^ {- 1} (t) R (t) \\ \hat {B} (t) = R ^ {- 1} (t) B (t), \quad \hat {C} (t) = C (t) R (t) \tag {3.229} \\ \end{array}
$$

考虑到 $\hat{x} = R^{-1}(t)x$ ，并利用状态运动的表达式，可有

$$
\begin{array}{l} \hat {\Phi} (t, t _ {0}) \hat {x} _ {0} + \int_ {t _ {0}} ^ {t} \hat {\Phi} (t, \tau) \hat {B} (\tau) u (\tau) d \tau \\ = R ^ {- 1} (t) \Phi (t, t _ {0}) x _ {0} + \int_ {t _ {0}} ^ {t} R ^ {- 1} (t) \Phi (t, \tau) B (\tau) u (\tau) d \tau \\ = R ^ {- 1} (t) \Phi (t, t _ {0}) R (t _ {0}) \hat {\boldsymbol {x}} _ {0} + \int_ {t _ {0}} ^ {t} R ^ {- 1} (t) \Phi (t, \tau) R (\tau) \hat {B} (\tau) \boldsymbol {u} (\tau) d \tau \tag {3.230} \\ \end{array}
$$

从而，由此得到

$$\hat {\Phi} (t, \tau) = R ^ {- 1} (t) \Phi (t, \tau) R (\tau) \tag {3.231}$$

利用上述关系式,进一步有

$$
\hat {W} _ {\varepsilon} \left[ t _ {0}, t _ {1} \right] = \int_ {t _ {0}} ^ {t _ {1}} \hat {\Phi} \left(t _ {0}, \tau\right) \hat {B} (\tau) \hat {B} ^ {T} (\tau) \hat {\Phi} ^ {T} \left(t _ {0}, \tau\right) d \tau
\begin{array}{l} = \int_ {t _ {0}} ^ {t _ {1}} R ^ {- 1} \left(t _ {0}\right) \Phi \left(t _ {0}, \tau\right) B (\tau) B ^ {T} (\tau) \Phi^ {T} \left(t _ {0}, \tau\right) \left[ R ^ {- 1} \left(t _ {0}\right) \right] ^ {T} d \tau \\ = R ^ {- 1} \left(t _ {0}\right) W _ {c} \left[ t _ {0}, t _ {1} \right] \left[ R ^ {- 1} \left(t _ {0}\right) \right] ^ {T} \tag {3.232} \\ \end{array}
$$

由 $\operatorname{rank} R(t_0) = n$ 和 $\operatorname{rank} W_c[t_0, t_1] \leqslant n$ ，故可导出

$$\operatorname{rank} \hat {W} _ {c} \left[ t _ {0}, t _ {1} \right] \leqslant \operatorname{rank} W _ {c} \left[ t _ {0}, t _ {1} \right] \tag {3.233}$$

再因

$$W _ {c} \left[ t _ {0}, t _ {1} \right] = R \left(t _ {0}\right) \hat {W} _ {c} \left[ t _ {0}, t _ {1} \right] R ^ {T} \left(t _ {0}\right) \tag {3.234}$$

又可导出

$$\operatorname{rank} W _ {c} \left[ t _ {0}, t _ {1} \right] \leqslant \operatorname{rank} \hat {W} _ {c} \left[ t _ {0}, t _ {1} \right] \tag {3.235}$$

于是，由（3.233）和（3.235）即可证得（3.226）。同理，也可证得（3.227）。这样，就完成了证明。

结论 1 和 2 说明, 对线性系统作线性非奇异变换, 不改变系统的能控性和能观测性, 也不改变其不完全能控和不完全能观测的程度。而正是这一点, 提供了采用线性非奇异变换, 来对系统实现结构分解的可能性和具体途径。

线性定常系统按能控性的结构分解 考虑不完全能控的多输入-多输出线性定常系统

$$
\begin{array}{l} \begin{array}{l} \dot {\boldsymbol {x}} = A \boldsymbol {x} + B \boldsymbol {u} \\ \boldsymbol {x} = C \boldsymbol {x} \end{array} \tag {3.236} \\ \mathbf {y} = C \mathbf {x} \\ \end{array}
$$

其中，x 为 n 维状态向量， $\operatorname{rank} Q_{c} = k < n$ 。再在能控性判别矩阵

$$Q _ {c} = [ B \mid A B \mid \dots \mid A ^ {n - 1} B ] \tag {3.237}$$
