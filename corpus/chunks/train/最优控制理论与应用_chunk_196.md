$$
\begin{array}{l} \dot {\boldsymbol {\lambda}} (t) = \dot {\boldsymbol {K}} (t) \boldsymbol {x} (t) + \boldsymbol {K} (t) \dot {\boldsymbol {x}} (t) \\ = \dot {\boldsymbol {K}} (t) \boldsymbol {x} (t) + \boldsymbol {K} (t) \left[ \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {u} (t) - \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {v} (t) \right] \\ = \dot {\boldsymbol {K}} (t) \boldsymbol {x} (t) - \boldsymbol {K} (t) \left[ \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} (t) - \right. \\ \left. \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \right] \boldsymbol {K} (t) \boldsymbol {x} (t) \\ = \left\{\dot {\boldsymbol {K}} (t) - \boldsymbol {K} (t) \left[ \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} (t) - \right. \right. \\ \left. \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \right] \boldsymbol {K} (t) \mid \boldsymbol {x} (t) \\ \end{array}
$$

因上式左端为零,且对任意的 $x(t)$ 均成立,故有

$$\dot {\boldsymbol {K}} (t) - \boldsymbol {K} (t) \left[ \boldsymbol {G} _ {\mathrm{p}} (t) \boldsymbol {R} _ {\mathrm{p}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{p}} ^ {\mathrm{T}} (t) - \right.\left. \boldsymbol {G} _ {\mathrm{e}} (t) \boldsymbol {R} _ {\mathrm{e}} ^ {- 1} (t) \boldsymbol {G} _ {\mathrm{e}} ^ {\mathrm{T}} (t) \right] \boldsymbol {K} (t) = \boldsymbol {0} \tag {10-103}$$

由 $(10-102)$ ， $\boldsymbol{\lambda}(t)=\boldsymbol{K}(t)\boldsymbol{x}(t)$ 和横截条件 $(10-100)$ ， $\boldsymbol{\lambda}(t_{f})=\boldsymbol{x}(t_{f})$ ，故得出

$$\boldsymbol {K} \left(t _ {\mathrm{f}}\right) = \boldsymbol {I} \tag {10-104}$$

(10-103) 是一个关于 $K(t)$ 的黎卡提型微分方程。由 $A_{p}, B_{p}, A_{e}, B_{e}$ 对 $t$ 连续和 $R_{p}, R_{e}$ 为正定的假设，带终端条件式 (10-104) 的黎卡提微分方程式 (10-103) 有唯一解；且由 (10-104) 知 $K(t_{\mathrm{f}}) = K^{\mathrm{T}}(t_{\mathrm{f}})$ ，故有 $K(t) = K^{\mathrm{T}}(t)$ 。

下面给出 $K(t)$ 解的解析式。因为
