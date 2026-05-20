# 3. 稳定性分析

参考文献[12],本控制算法的稳定性分析如下:

![](image/92c20f70004c80b94b4e7b38575eadd8b6565df7fe878073c1b7adc700ee9a72.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["被控对象 x=f(x)+g(x)u, y=x"] --> B["模糊控制器 u=1/(ĝ(x|θ_g)[-f̂(x|θ_f)+y_m^(n)+K^T e"]]
    B --> C["自适应律 θ_f(0), θ_g(0)"]
    C --> D["y_m"]
    D --> E["+"]
    E --> A
    B --> F["自适应律 θ_g=-γ_2e^T Pbηu"]
    F --> C
```
</details>

图 5-11 自适应模糊控制系统

将式(5.26)代入式(5.18)可得如下模糊控制系统的闭环动态方程式

$$\boldsymbol {e} ^ {(n)} = - \boldsymbol {K} ^ {\mathrm{T}} \boldsymbol {e} + [ \hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) - f (\boldsymbol {x}) ] + [ \hat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g}) - g (\boldsymbol {x}) ] u \tag {5.30}$$

令

$$
\boldsymbol {\Lambda} = \left[ \begin{array}{c c c c c c c} 0 & 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & 0 & 1 & 0 & \dots & 0 & 0 \\ \dots & \dots & \dots & \dots & \dots & \dots & \dots \\ 0 & 0 & 0 & 0 & \dots & 0 & 1 \\ - k _ {n} & - k _ {n - 1} & \dots & \dots & \dots & \dots & - k _ {1} \end{array} \right], \boldsymbol {b} = \left[ \begin{array}{c} 0 \\ 0 \\ \dots \\ 0 \\ 1 \end{array} \right] \tag {5.31}
$$

则动态方程式(5.30)可写为向量形式

$$\dot {\boldsymbol {e}} = \boldsymbol {\Lambda} \boldsymbol {e} + \boldsymbol {b} \left\{\left[ \hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) - f (\boldsymbol {x}) \right] + \left[ \hat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g}) - g (\boldsymbol {x}) \right] u \right\} \tag {5.32}$$

设最优参数为

$$\boldsymbol {\theta} _ {f} ^ {*} = \arg \min _ {\theta_ {f} \in \Omega_ {f}} \left[ \sup _ {x \in R ^ {n}} | \hat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f}) - f (\boldsymbol {x}) | \right] \tag {5.33}\boldsymbol {\theta} _ {g} ^ {*} = \arg \min _ {\theta_ {g} \in \Omega_ {g}} [ \sup _ {x \in R ^ {n}} | \hat {g} (\boldsymbol {x} | \boldsymbol {\theta} _ {g}) - g (\boldsymbol {x}) | ] \tag {5.34}$$

式中， $\Omega_{f}$ 和 $\Omega_{g}$ 分别为 $\theta_{f}$ 和 $\theta_{g}$ 的集合。

定义最小逼近误差为

$$\omega = \left[ \widehat {f} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {f} ^ {*}) - f (\boldsymbol {x}) \right] + \left[ \widehat {g} (\boldsymbol {x} \mid \boldsymbol {\theta} _ {g} ^ {*}) - g (\boldsymbol {x}) \right] u \tag {5.35}$$

式(5.32)可写为
