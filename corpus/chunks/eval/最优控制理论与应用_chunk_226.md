将式(11-4)代入式(11-3)，消去 $y$ ，得从 $\pmb{w}$ 到 $\pmb{z}$ 的闭环传递函数为

$$\boldsymbol {F} _ {1} (\boldsymbol {P}, \boldsymbol {K}) = \boldsymbol {P} _ {1 1} + \boldsymbol {P} _ {1 2} \boldsymbol {K} \left(\boldsymbol {I} - \boldsymbol {P} _ {2 2} \boldsymbol {K}\right) ^ {- 1} \boldsymbol {P} _ {2 1} \tag {11-5}$$

由此， $H_{\infty}$ 标准问题可表述如下：

对于一个给定的广义被控对象 P，求取一个反馈控制器 K，使闭环系统内稳定，且使闭环传递函数 $F_{1}(P,K)$ 的 $H_{\infty}$ 范数达到极小，即

$$\min _ {\boldsymbol {K}} \left\| \boldsymbol {F} _ {1} (\boldsymbol {P}, \boldsymbol {K}) \right\| _ {\infty} \tag {11-6}$$

式 $(11-6)$ 表示 $H_{\infty}$ 最优控制问题。

其中,对应于图 11-3 中的闭环系统内稳定是指当 $t \to +\infty$ 时,闭环系统的状态(原开环系统和动态补偿器的状态)趋于零。

若给定 $\gamma > 0$ ，求取镇定反馈控制器 K，使得

$$\| \boldsymbol {F} _ {1} (\boldsymbol {P}, \boldsymbol {K}) \| _ {\infty} < \gamma \tag {11-7}$$

则表示 $H_{\infty}$ 次优控制问题。
