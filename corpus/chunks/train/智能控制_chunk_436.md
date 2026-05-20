# 9.8.1 问题的提出

设 $n$ 关节机械手的动力学方程为

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) = \tau + \boldsymbol {d} \tag {9.39}$$

式中， $D(q)$ 为 $n \times n$ 阶正定惯性矩阵， $C(q, \dot{q})$ 为 $n \times n$ 阶惯性矩阵， $G(q)$ 为 $n \times 1$ 阶惯性向量。

如果模型建模精确,且 d = 0, 则控制律可设计为

$$\boldsymbol {\tau} = \boldsymbol {D} (\boldsymbol {q}) \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \boldsymbol {k} _ {\mathrm{v}} \dot {\boldsymbol {e}} - \boldsymbol {k} _ {\mathrm{p}} \boldsymbol {e}\right) + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) \tag {9.40}$$

将控制律式(9.40)代入式(9.39)中,得到稳定的闭环系统为

$$\ddot {\boldsymbol {e}} + \boldsymbol {k} _ {\mathrm{v}} \dot {\boldsymbol {e}} + \boldsymbol {k} _ {\mathrm{p}} \boldsymbol {e} = 0 \tag {9.41}$$

式中， $q_{d}$ 为理想的角度， $e=q-q_{d},\dot{e}=\dot{q}-\dot{q}_{d}$ 。

在实际工程中,对象的实际模型很难得到,即无法得到精确的 $D(q)$ 、 $C(q,\dot{q})$ 、 $G(q)$ , 只能建立理想的名义模型。

将机器人名义模型(已知)表示为 $D_{0}(q)$ 、 $C_{0}(q,\dot{q})$ 、 $G_{0}(q)$ ，针对名义模型，控制律设计为

$$\boldsymbol {\tau} = \boldsymbol {D} _ {0} (\boldsymbol {q}) \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - \boldsymbol {k} _ {v} \dot {\boldsymbol {e}} - \boldsymbol {k} _ {\mathrm{p}} e\right) + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) \tag {9.42}$$

将控制律式(9.42)代入式(9.39)中,得

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) = \boldsymbol {D} _ {0} (\boldsymbol {q}) \left(\ddot {\boldsymbol {q}} _ {\mathrm{d}} - k _ {\mathrm{v}} \dot {\boldsymbol {e}} - k _ {\mathrm{p}} \boldsymbol {e}\right) + \boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} _ {0} (\boldsymbol {q}) + \boldsymbol {d} \tag {9.43}$$

取 $\Delta D = D_{0} - D, \Delta C = C_{0} - C, \Delta G = G_{0} - G,$ 则
