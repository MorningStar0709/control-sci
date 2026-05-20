$$\dot {\boldsymbol {\lambda}} _ {1} = - \frac {\partial H _ {1}}{\partial \boldsymbol {x}} = - \frac {\partial F (\boldsymbol {x} ^ {*} , \boldsymbol {u} ^ {*} , \boldsymbol {v} ^ {*} , t)}{\partial \boldsymbol {x}} - \boldsymbol {\lambda} _ {1} ^ {\mathrm{T}} \frac {\partial f (\boldsymbol {x} ^ {*} , \boldsymbol {u} ^ {*} , \boldsymbol {v} ^ {*} , t)}{\partial \boldsymbol {x}} \tag {10-47}\boldsymbol {\lambda} _ {1} \left(t _ {\mathrm{f}}\right) = \frac {\partial \boldsymbol {\Phi}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v}$$

和

$$\dot {\boldsymbol {\lambda}} _ {2} = - \frac {\partial H _ {2}}{\partial \boldsymbol {x}} = - \frac {\partial F (\boldsymbol {x} ^ {*} , \boldsymbol {u} ^ {*} , \boldsymbol {v} ^ {*} , t)}{\partial \boldsymbol {x}} - \boldsymbol {\lambda} _ {2} ^ {\mathrm{T}} \frac {\partial f (\boldsymbol {x} ^ {*} , \boldsymbol {u} ^ {*} , \boldsymbol {v} ^ {*} , t)}{\partial \boldsymbol {x}} \tag {10-48}\boldsymbol {\lambda} _ {2} \left(t _ {\mathrm{f}}\right) = \frac {\partial \boldsymbol {\Phi}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} + \frac {\partial \boldsymbol {G} ^ {\mathrm{T}}}{\partial \boldsymbol {x} \left(t _ {\mathrm{f}}\right)} \boldsymbol {v}$$

由式(10-47)、(10-48)可见， $\pmb{\lambda}_1(t)$ 和 $\pmb{\lambda}_2(t)$ 满足相同的线性非齐次方程，且其终端条件相同。根据线性非齐次方程的终值问题的唯一性定理知

$$\boldsymbol {\lambda} _ {1} (t) = \boldsymbol {\lambda} _ {2} (t), \quad \forall t \in [ t _ {0}, t _ {f} ]$$

令

$$\boldsymbol {\lambda} (t) = \boldsymbol {\lambda} _ {1} (t) = \boldsymbol {\lambda} _ {2} (t), \quad \forall t \in [ t _ {0}, t _ {\mathrm{f}} ] \tag {10-49}$$

再由哈密顿函数 $H_{1}$ 和 $H_{2}$ 取极值的表达式(10-36)和(10-45)可得

$$
\begin{array}{l} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) = H _ {1} \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda} _ {1}, t\right) \\ = H _ {2} \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \lambda_ {2}, t\right) \\ \end{array}
$$

上式可写成
