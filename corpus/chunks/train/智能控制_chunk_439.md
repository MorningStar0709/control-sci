# 9.8.3 控制器的设计及分析

控制器设计为

$$\pmb {\tau} = \pmb {\tau} _ {1} + \pmb {\tau} _ {2} \tag {9.53}$$

其中

$$\boldsymbol {\tau} _ {1} = \boldsymbol {D} _ {0} (\boldsymbol {q}) (\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \boldsymbol {k} _ {\mathrm{v}} \dot {\boldsymbol {e}} - \boldsymbol {k} _ {\mathrm{p}} \boldsymbol {e}) + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) \tag {9.54}\pmb {\tau} _ {2} = - \pmb {D} _ {0} (\pmb {q}) \widehat {\pmb {f}} \tag {9.55}$$

式中， $\hat{\theta}$ 为 $\theta^{*}$ 的估计值， $\hat{f} = \hat{\theta}^{\mathrm{T}}\varphi(x)$ 。

同理,将控制律式(9.53)代入式(9.39)中,得

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q})= \boldsymbol {D} _ {0} (\boldsymbol {q}) \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \boldsymbol {k} _ {\mathrm{v}} \dot {\boldsymbol {e}} - \boldsymbol {k} _ {\mathrm{p}} \boldsymbol {e}\right) + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) - \boldsymbol {D} _ {0} (\boldsymbol {q}) \hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta}) + \boldsymbol {d}$$

将 $D_{0}(q)\ddot{q}+C_{0}(q,\dot{q})\dot{q}+G_{0}(q)$ 分别减去上式两边，得

$$
\begin{array}{l} \Delta D (q) \ddot {q} + \Delta C (q, \dot {q}) \dot {q} + \Delta G (q) + d \\ = \boldsymbol {D} _ {0} (q) \ddot {\boldsymbol {q}} - \boldsymbol {D} _ {0} (\boldsymbol {q}) (\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \boldsymbol {k} _ {\mathrm{v}} \dot {\boldsymbol {e}} - \boldsymbol {k} _ {\mathrm{p}} \boldsymbol {e}) + \boldsymbol {D} _ {0} (\boldsymbol {q}) \hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta}) \\ \end{array}
$$

即

$$\Delta D (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \Delta C (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \Delta G (\boldsymbol {q}) + \boldsymbol {d} = D _ {0} (\boldsymbol {q}) (\ddot {\boldsymbol {e}} + k _ {\mathrm{v}} \dot {\boldsymbol {e}} + k _ {\mathrm{p}} \boldsymbol {e} + \hat {\boldsymbol {f}} (\boldsymbol {x}, \boldsymbol {\theta}))$$
