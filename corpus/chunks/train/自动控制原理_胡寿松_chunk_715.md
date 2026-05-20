# (2) 线性定常离散系统渐近稳定性的判别

设线性定常离散系统状态方程为

$$\boldsymbol {x} (k + 1) = \Phi \boldsymbol {x} (k), \boldsymbol {x} (0) = \boldsymbol {x} _ {0}; k = 0, 1, 2, \dots \tag {9-266}$$

式中， $\Phi$ 阵非奇异；原点是平衡状态。取正定二次型函数

$$V (\boldsymbol {x} (k)) = \boldsymbol {x} ^ {\mathrm{T}} (k) \boldsymbol {P x} (k)$$

以 $\Delta V(x(k))$ 代替 $\dot{V}(x)$ ，有

$$\Delta V (\boldsymbol {x} (k)) = V (\boldsymbol {x} (k + 1)) - V (\boldsymbol {x} (k))$$

考虑到状态方程(9-266)有

$$
\begin{array}{l} \Delta V (\boldsymbol {x} (k)) = \boldsymbol {x} ^ {\mathrm{T}} (k + 1) \boldsymbol {P x} (k + 1) - \boldsymbol {x} ^ {\mathrm{T}} (k) \boldsymbol {P x} (k) \\ = [ \boldsymbol {\Phi} \mathbf {x} (k) ] ^ {\mathrm{T}} \mathbf {P} [ \boldsymbol {\Phi} \mathbf {x} (k) ] - \mathbf {x} ^ {\mathrm{T}} (k) \mathbf {P} \mathbf {x} (k) \\ = \boldsymbol {x} ^ {\mathrm{T}} (k) (\boldsymbol {\Phi} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {\Phi} - \boldsymbol {P}) \boldsymbol {x} (k) \\ \end{array}
$$

令 $\Phi^{T}P\Phi-P\doteq-Q$ (9-267)

于是有 $\Delta V(x(k)) = -x^{\mathrm{T}}(k)Qx(k)$

定理 9-14 系统(9-266)渐近稳定的充分必要条件是,给定任一正定对称矩阵 Q,存在一个正定对称矩阵 P 使式(9-267)成立。

$x^{\mathrm{T}}(k)Px(k)$ 是系统的一个李雅普诺夫函数,式(9-267)称为离散的李雅普诺夫代数方程,通常可取Q=I。

如果 $\Delta V(x(k))$ 沿任一解的序列不恒为零，则 Q 可取为正半定矩阵。

综上所述，李雅普诺夫稳定性判据如表9-1所示。

表 9-1 李雅普诺夫稳定性判据汇总表
