由于 $\forall t\in [0,T],\forall \tau \in [0,t],\forall \sigma \in [0,\tau ]$ ，则有 $\| e_k(\sigma)\|_{\lambda}\leqslant \| e_k(\tau)\|_{\lambda}$

将式(11.19)的结果应用于下式,得式(11.18)不等式右边第三项为

$$\exp (- \lambda t) \int_ {0} ^ {t} \int_ {0} ^ {\tau} b _ {2} \| \boldsymbol {e} _ {k} (\sigma) \| d \sigma d \tau = \exp (- \lambda t) \int_ {0} ^ {t} \exp (\lambda \tau) \exp (- \lambda \tau) \int_ {0} ^ {\tau} b _ {2} \| \boldsymbol {e} _ {k} (\sigma) \| d \sigma d \tau\leqslant \exp (- \lambda t) \int_ {0} ^ {t} \exp (\lambda \tau) b _ {2} \frac {1 - \exp (- \lambda t)}{\lambda} \| e _ {k} (\sigma) \| _ {\lambda} d \tau\leqslant b _ {2} \frac {1 - \exp (- \lambda T)}{\lambda} \exp (- \lambda t) \int_ {0} ^ {t} \exp (\lambda \tau) \| e _ {k} (\tau) \| _ {\lambda} d \tau= b _ {2} \frac {1 - \exp (- \lambda T)}{\lambda} \exp (- \lambda t) \| \boldsymbol {e} _ {k} (\tau) \| _ {\lambda} \int_ {0} ^ {t} \exp (\lambda t) d \tau= b _ {2} \frac {1 - \exp (- \lambda T)}{\lambda} \exp (- \lambda t) \| \boldsymbol {e} _ {k} (\tau) \| _ {\lambda} \frac {\exp (\lambda t) - 1}{\lambda}= b _ {2} \frac {1 - \exp (- \lambda T)}{\lambda} \| \boldsymbol {e} _ {k} (\tau) \| _ {\lambda} \frac {1 - \exp (- \lambda t)}{\lambda}\leqslant b _ {2} \left(\frac {1 - \exp (- \lambda T)}{\lambda}\right) ^ {2} \| \boldsymbol {e} _ {k} (\tau) \| _ {\lambda}$$

式中， $0 < \frac{1 - \exp(-\lambda t)}{\lambda} \leqslant \frac{1 - \exp(-\lambda T)}{\lambda}$ 。则

$$\exp (- \lambda t) \int_ {0} ^ {t} \int_ {0} ^ {\tau} b _ {2} \| \boldsymbol {e} _ {k} (\sigma) \| \mathrm{d} \sigma \mathrm{d} \tau \leqslant b _ {2} \left(\frac {1 - \exp (- \lambda T)}{\lambda}\right) ^ {2} \| \boldsymbol {e} _ {k} (\tau) \| _ {\lambda} \tag {11.20}$$

将式(11.19)和式(11.20)代入式(11.18)，考虑到 $\| e_k(\tau)\|_{\lambda}\leqslant \| e_k(t)\|_{\lambda}$ ，得

$$\left\| \boldsymbol {e} _ {k + 1} (t) \right\| _ {\lambda} \leqslant \widetilde {\rho} \left\| \boldsymbol {e} _ {k} (t) \right\| _ {\lambda} \tag {11.21}$$

式中， $\widetilde{\rho} = \bar{\rho} + b_1 \frac{1 - \exp(-\lambda T)}{\lambda} + b_2 \left( \frac{1 - \exp(-\lambda T)}{\lambda} \right)^2$ 。由于 $\bar{\rho} < 1$ ，则当 $\lambda$ 取足够大时，可使 $\widetilde{\rho} < 1$ 。因此 $\lim_{k \to \infty} \| e_k(t) \|_{\lambda} = 0$ 。定理得证。

如果将控制律式(11.14)中的 $e_{k}(t)$ 改为 $e_{k+1}(t)$ ，则为闭环PID型迭代学习控制律。同定理1的证明过程，可证明闭环PID迭代学习控制律的收敛性。
