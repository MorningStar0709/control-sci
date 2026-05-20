$$
\begin{array}{l} \min _ {u} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) = H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) \\ = \max _ {v} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v}, \lambda , t\right) \tag {10-50} \\ \end{array}
$$

类似于式(10-13)、(10-14)，有

$$\min _ {u} \max _ {v} H \left(x ^ {*}, u, v, \lambda , t\right) \leqslant \max _ {v} H \left(x ^ {*}, u ^ {*}, v, \lambda , t\right) \tag {10-51}\max _ {v} \min _ {u} H \left(x ^ {*}, u, v, \lambda , t\right) \geqslant \min _ {u} H \left(x ^ {*}, u, v ^ {*}, \lambda , t\right) \tag {10-52}$$

联合(10-50)、(10-51)和(10-52)，可得

$$
\begin{array}{l} \min _ {u} \max _ {v} H (x, u, v, \lambda , t) \leqslant H \left(x ^ {*}, u ^ {*}, v ^ {*}, \lambda , t\right) \\ \leqslant \max _ {v} \min _ {u} H (x ^ {*}, u, v, \lambda , t) \tag {10-53} \\ \end{array}
$$

另一方面,将矩阵对策中的引理1——关于“最小中的最大不大于最大中的最小”的结论用于 $H(x^{*},u,v,\lambda,t)$ ，得

$$\min _ {u} \max _ {v} H \left(x ^ {*}, u, v, \lambda , t\right) \geqslant \max _ {v} \min _ {u} H \left(x ^ {*}, u, v, \lambda , t\right) \tag {10-54}$$

联合式(10-53)和(10-54)，即得

$$
\begin{array}{l} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u} ^ {*}, \boldsymbol {v} ^ {*}, \boldsymbol {\lambda}, t\right) = \min _ {\boldsymbol {u}} \max _ {\boldsymbol {v}} H \left(\boldsymbol {x} ^ {*}, \boldsymbol {u}, \boldsymbol {v}, \boldsymbol {\lambda}, t\right) \\ = \max _ {v} \min _ {u} H \left(x ^ {*}, u, v, \lambda , t\right) \tag {10-55} \\ \end{array}
$$

上式即双方极值原理最优策略的必要条件中的式(10-26)。根据式(10-47)\~(10-49)式,可以得到必要条件中的其他几个式子。

注：当 $\pmb{u},\pmb{v}$ 为开集， $f(x,u,\pmb{v},t),F(x,u,\pmb{v},t),\Phi (x,t),G(x,t)$ 关于变元都是二次连续可微的，则双方极值原理中的式(10-26)或(10-55)与下列一组关系式等价：
