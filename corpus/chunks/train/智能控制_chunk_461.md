# 9.11.4 稳定性分析

根据闭环系统的性能要求,定义离散时间 Lyapunov 函数为

$$V (k) = e _ {1} ^ {2} (k) + \gamma \tilde {\boldsymbol {w}} ^ {\mathrm{T}} (k) \tilde {\boldsymbol {w}} (k) \tag {9.89}$$

$V(k)$ 的一阶差分为

$$\Delta V (k) = V (k) - V (k - 1) = e _ {1} ^ {2} (k) - e _ {1} ^ {2} (k - 1) + \gamma \left(\tilde {\boldsymbol {w}} ^ {\mathrm{T}} (k) + \tilde {\boldsymbol {w}} ^ {\mathrm{T}} (k - 1)\right) (\tilde {\boldsymbol {w}} (k) - \tilde {\boldsymbol {w}} (k - 1))$$

稳定性分析分为以下三步进行。

(1) 将式(9.87)的 $e_{1}(k-1)$ 代入上式, 可得

$$
\begin{array}{l} \Delta V (k) = e _ {1} ^ {2} (k) - \frac {e _ {1} ^ {2} (k) + \beta^ {2} (\tilde {f} (\boldsymbol {x} (k - 1)) - v (k)) ^ {2} - 2 \beta (\tilde {f} (\boldsymbol {x} (k - 1)) - v (k)) e _ {1} (k)}{c _ {1} ^ {2}} + \\ \gamma \left(\left(\hat {w} (k) - w ^ {*}\right) ^ {\mathrm{T}} + \left(\hat {w} (k - 1) - w ^ {*}\right) ^ {\mathrm{T}}\right) \left(\left(\hat {w} (k) - w ^ {*}\right) - \left(\hat {w} (k - 1) - w ^ {*}\right)\right) \\ = - V _ {1} + \frac {2 \beta (\tilde {f} (\boldsymbol {x} (k - 1)) - v (k)) e _ {1} (k)}{c _ {1} ^ {2}} + \gamma (\Delta \hat {\boldsymbol {w}} ^ {\mathrm{T}} (k) + 2 \tilde {\boldsymbol {w}} ^ {\mathrm{T}} (k - 1)) \Delta \hat {\boldsymbol {w}} (k) \\ \end{array}
$$

式中， $V_{1} = \frac{e_{1}^{2}(k)(1 - c_{1}^{2})}{c_{1}^{2}} +\frac{\beta^{2}(\widetilde{f} (\pmb {x}(k - 1)) - v(k))^{2}}{c_{1}^{2}}\geqslant 0.$

(2) 将式(9.82)代入上式的 $\widetilde{f}(x(k-1))$ 中, 整理可得

$$\Delta V (k) = - V _ {1} + \frac {2 \beta (- \widetilde {w} (k - 1) ^ {\mathrm{T}} h (x (k - 1)) - \Delta_ {f} (x (k - 1)) - v (k)) e _ {1} (k)}{c _ {1} ^ {2}} +\gamma \Delta \hat {\boldsymbol {w}} ^ {\mathrm{T}} (k) \Delta \hat {\boldsymbol {w}} (k) + 2 \gamma \tilde {\boldsymbol {w}} ^ {\mathrm{T}} (k - 1) \Delta \hat {\boldsymbol {w}} (k)= - V _ {1} + 2 \tilde {\boldsymbol {w}} ^ {\mathrm{T}} (k - 1) \left(\gamma \Delta \hat {\boldsymbol {w}} (k) - \frac {\beta}{c _ {1} ^ {2}} \boldsymbol {h} (\boldsymbol {x} (k - 1)) e _ {1} (k)\right) -\frac {2 \beta}{c _ {1} ^ {2}} \left(\Delta_ {f} (\boldsymbol {x} (k - 1)) + v (k)\right) e _ {1} (k) + \gamma \Delta \hat {\boldsymbol {w}} ^ {\mathrm{T}} (k) \Delta \hat {\boldsymbol {w}} (k)$$

(3) 将自适应律式(9.88)代入上式, 可得
