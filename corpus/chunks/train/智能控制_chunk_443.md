# 9.8.4 仿真实例

选两关节机器人系统(不考虑摩擦力),其动力学模型为

$$\boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} + \boldsymbol {G} (\boldsymbol {q}) = \tau + \boldsymbol {d}$$

其中

$$
\boldsymbol {D} (\boldsymbol {q}) = \left[ \begin{array}{c c} v + q _ {0 1} + 2 \gamma \cos (q _ {2}) & q _ {0 1} + q _ {0 2} \cos (q _ {2}) \\ q _ {0 1} + q _ {0 2} \cos (q _ {2}) & q _ {0 1} \end{array} \right]

\boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) = \left[ \begin{array}{c c} - q _ {0 2} \dot {q} _ {2} \sin (q _ {2}) & - q _ {0 2} (\dot {q} _ {1} + \dot {q} _ {2}) \sin (q _ {2}) \\ q _ {0 2} \dot {q} _ {1} \sin (q _ {2}) & 0 \end{array} \right]

\mathbf {G} (\mathbf {q}) = \left[ \begin{array}{l} 1 5 g \cos q _ {1} + 8. 7 5 g \cos (q _ {1} + q _ {2}) \\ 8. 7 5 g \cos (q _ {1} + q _ {2}) \end{array} \right]
$$

式中， $v=13.33,q_{01}=8.98,q_{02}=8.75,g=9.8$ 。

上述模型可写为

$$\left(\boldsymbol {D} _ {0} (\boldsymbol {q}) - \Delta \boldsymbol {D} (\boldsymbol {q})\right) \ddot {\boldsymbol {q}} + \left(\boldsymbol {C} _ {0} (\boldsymbol {q}, \dot {\boldsymbol {q}}) - \Delta \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}})\right) \dot {\boldsymbol {q}} + \left(\boldsymbol {G} _ {0} (\boldsymbol {q}) - \Delta \boldsymbol {G} (\boldsymbol {q})\right) = \tau + d$$

即

$$\boldsymbol {D} _ {0} \ddot {\boldsymbol {q}} + \boldsymbol {C} _ {0} \dot {\boldsymbol {q}} + \boldsymbol {G} _ {0} = \tau + \boldsymbol {d} + \Delta \boldsymbol {D} \ddot {\boldsymbol {q}} + \Delta \boldsymbol {C} \dot {\boldsymbol {q}} + \Delta \boldsymbol {G}$$

由 $f$ 的定义可得

$$\ddot {\boldsymbol {q}} = \boldsymbol {D} _ {0} ^ {- 1} (\boldsymbol {\tau} - \boldsymbol {C} _ {0} \dot {\boldsymbol {q}} - \boldsymbol {G} _ {0}) + \boldsymbol {f}$$

仿真中用上式描述被控对象。

设误差扰动为

$$d _ {1} = 2, d _ {2} = 3, d _ {3} = 6\omega = d _ {1} + d _ {2} \| \boldsymbol {e} \| + d _ {3} \| \dot {\boldsymbol {e}} \|$$

位置指令为

$$
\left\{ \begin{array}{l} q _ {1 \mathrm{d}} = 1 + 0. 2 \sin (0. 5 \pi t) \\ q _ {2 \mathrm{d}} = 1 - 0. 2 \cos (0. 5 \pi t) \end{array} \right.
$$

被控对象的初值为 $[q_{1} q_{2} q_{3} q_{4}]^{\mathrm{T}} = [0.6 0.3 0.5 0.5]^{\mathrm{T}}$ ，控制参数取
