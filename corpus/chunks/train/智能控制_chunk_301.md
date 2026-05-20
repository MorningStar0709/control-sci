# 5.6.3 基于摩擦补偿的控制

当 $F(\pmb {q},\dot{\pmb{q}},\ddot{\pmb{q}})$ 只包括摩擦项 $\pmb{F}_{\mathrm{r}}$ 时，模糊系统输入变量由3个变为1个，规则总数由 $k^{3n}$ 变为 $k^n$ 。可只考虑针对摩擦进行模糊逼近的模糊补偿。由于摩擦力只与速度信号有关，用于逼近摩擦的模糊系统可表示为 $\widehat{F(\dot{\pmb{q}}|\pmb{\theta})}^{[15]}$ ，可根据基于传统模糊补偿的控制器设计方法，即式(5.72）、式(5.75）和式(5.76）来设计控制律。

模糊自适应控制律设计为

$$\boldsymbol {\tau} = \boldsymbol {D} (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {C} (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} _ {\mathrm{r}} + \boldsymbol {G} (\boldsymbol {q}) + \boldsymbol {F} (\dot {\boldsymbol {q}} \mid \boldsymbol {\theta}) - \boldsymbol {K} _ {\mathrm{D}} s \tag {5.77}$$

鲁棒模糊自适应控制律设计为

$$\tau = D (\boldsymbol {q}) \ddot {\boldsymbol {q}} _ {\mathrm{r}} + C (\boldsymbol {q}, \dot {\boldsymbol {q}}) \dot {\boldsymbol {q}} _ {\mathrm{r}} + G (\boldsymbol {q}) + F (\dot {\boldsymbol {q}} | \boldsymbol {\theta}) - K _ {\mathrm{D}} s - W \operatorname{sgn} (s) \tag {5.78}$$

自适应律设计为

$$\dot {\boldsymbol {\theta}} _ {i} = - \boldsymbol {\Gamma} _ {i} ^ {- 1} s _ {i} \xi (\dot {\boldsymbol {q}}), i = 1, 2, \dots , n \tag {5.79}$$

模糊系统设计为

$$
\widehat {\boldsymbol {F}} (\dot {\boldsymbol {q}} \mid \boldsymbol {\theta}) = \left[ \begin{array}{c} \widehat {F} _ {1} (\dot {\boldsymbol {q}} _ {1}) \\ \widehat {F} _ {2} (\dot {\boldsymbol {q}} _ {2}) \\ \vdots \\ \widehat {F} _ {n} (\dot {\boldsymbol {q}} _ {n}) \end{array} \right] = \left[ \begin{array}{c} \boldsymbol {\theta} _ {1} ^ {\mathrm{T}} \boldsymbol {\xi} ^ {1} (\dot {\boldsymbol {q}} _ {1}) \\ \boldsymbol {\theta} _ {2} ^ {\mathrm{T}} \boldsymbol {\xi} ^ {2} (\dot {\boldsymbol {q}} _ {2}) \\ \vdots \\ \boldsymbol {\theta} _ {n} ^ {\mathrm{T}} \boldsymbol {\xi} ^ {n} (\dot {\boldsymbol {q}} _ {n}) \end{array} \right]
$$
