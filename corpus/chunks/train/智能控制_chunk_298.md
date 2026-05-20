# 1. 自适应控制律的设计

设计控制律为

$$\tau = \boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {F} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} | \boldsymbol {\Theta}) - \boldsymbol {K} _ {\mathrm{D}} s \tag {5.72}$$

式中， $K_{D}=\mathrm{diag}(K_{i}),K_{i}>0,i=1,2,\cdots,n$ ，且

构造模糊系统如下

$$
\widehat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta}) = \left[ \begin{array}{c} F _ {1} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta} _ {1}) \\ \widehat {F} _ {2} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta} _ {2}) \\ \vdots \\ \widehat {F} _ {n} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta} _ {n}) \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {\Theta} _ {1} ^ {\mathrm{T}} \xi (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) \\ \boldsymbol {\Theta} _ {2} ^ {\mathrm{T}} \xi (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) \\ \vdots \\ \boldsymbol {\Theta} _ {n} ^ {\mathrm{T}} \xi (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) \end{array} \right] \tag {5.73}
$$

式中， $\xi(q,\dot{q},\ddot{q})$ 为模糊系统基函数向量， $\theta$ 为模糊系统自适应调节参数。

模糊逼近误差为

$$\boldsymbol {\omega} = \boldsymbol {F} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}}) - \widehat {\boldsymbol {F}} (\boldsymbol {q}, \dot {\boldsymbol {q}}, \ddot {\boldsymbol {q}} \mid \boldsymbol {\Theta} ^ {*}) \tag {5.74}$$

定义 Lyapunov 函数为

$$V (t) = \frac {1}{2} \left(\mathbf {s} ^ {\mathrm{T}} \mathbf {D} \mathbf {s} + \sum_ {i = 1} ^ {n} \widetilde {\boldsymbol {\theta}} _ {i} ^ {\mathrm{T}} \boldsymbol {\Gamma} _ {i} \widetilde {\boldsymbol {\theta}} _ {i}\right)$$

式中， $\widetilde{\theta}_{i}=\theta_{i}^{*}-\theta_{i},\theta_{i}^{*}$ 为理想调节参数， $\theta_{i}$ 为实际调节参数。

参考式(5.71)，将控制律式(5.72)代入 $\dot{V}(t)$ ，得
