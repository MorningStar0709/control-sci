# 7.3.2 鲁棒控制律的设计

定义误差为 $\boldsymbol{e}(t)=\boldsymbol{q}_{\mathrm{d}}(t)-\boldsymbol{q}(t)$ ，其中 $\boldsymbol{q}_{\mathrm{d}}(t)$ 为理想的位置指令， $\boldsymbol{q}(t)$ 为实际位置。定义误差函数为

$$\boldsymbol {r} = \dot {\boldsymbol {e}} + \Lambda \boldsymbol {e} \tag {7.11}$$

取 $\dot{\pmb{q}}_{\mathrm{r}} = \pmb {r}(t) + \dot{\pmb{q}}(t)$ 和 $\ddot{\pmb{q}}_{\mathrm{r}} = \dot{\pmb{r}}(t) + \ddot{\pmb{q}}(t)$ ，则

$$\dot {q} _ {\mathrm{r}} = \dot {q} _ {\mathrm{d}} + \Lambda \mathrm{e}\ddot {\boldsymbol {q}} _ {\mathrm{r}} = \ddot {\boldsymbol {q}} _ {\mathrm{d}} + \Lambda \dot {\boldsymbol {e}}$$

式中， $\Lambda>0$ 。

则由式（7.9）得

$$
\begin{array}{l} \boldsymbol {\tau} = \boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {d} (\dot {\boldsymbol {q}}) \\ = D (q) \ddot {q} _ {\mathrm{r}} + C (q, \dot {q}) \dot {q} _ {\mathrm{r}} + G (q) - D (q) \dot {r} - C (q, \dot {q}) r + d (\dot {q}) \tag {7.12} \\ = D _ {0} (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + C _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} _ {\mathrm{r}} + G _ {0} (\boldsymbol {q}) - D (\boldsymbol {q}) \dot {\boldsymbol {r}} - C (\boldsymbol {q}, \dot {\boldsymbol {q}}) \boldsymbol {r} + E _ {\mathrm{M}} + d (\dot {\boldsymbol {q}}) \\ \end{array}
$$

式中， $E_{\mathrm{M}}=\Delta D(\boldsymbol{q})\ddot{\boldsymbol{q}}_{\mathrm{r}}+\Delta C(\boldsymbol{q},\dot{\boldsymbol{q}})\dot{\boldsymbol{q}}_{\mathrm{r}}+\Delta G(\boldsymbol{q})$ ； $E=E_{\mathrm{M}}+d(\dot{\boldsymbol{q}})$ 。

控制律设计为

$$\boldsymbol {\tau} = \boldsymbol {\tau} _ {\mathrm{m}} + \boldsymbol {K} _ {\mathrm{p}} \mathrm{r} + \boldsymbol {K} _ {\mathrm{i}} \int r \mathrm{d} t + \boldsymbol {\tau} _ {\mathrm{r}} \tag {7.13}$$

式中， $K_{p}>0$ ； $K_{i}>0$ ； $\tau_{m}$ 为基于名义模型的控制项； $\tau_{r}$ 为用于建模误差和摩擦干扰的鲁棒项。

取

$$\boldsymbol {\tau} _ {\mathrm{m}} = \boldsymbol {D} _ {0} (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) \tag {7.14}\boldsymbol {\tau} _ {\mathrm{r}} = \boldsymbol {K} _ {\mathrm{r}} \operatorname{sgn} (\boldsymbol {r}) \tag {7.15}$$
