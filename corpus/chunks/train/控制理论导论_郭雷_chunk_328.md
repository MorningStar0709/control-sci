其中 $(A_{t},\mathcal{F}_{t}),(b_{t},\mathcal{F}_{t}),(D_{t},\mathcal{F}_{t})$ 都是适应过程，并且 $\| b_t\| \in \mathcal{P}_T,\| D_t\| \in \mathcal{P}_T,\| A_t\|^{\frac{1}{2}}\in$ $\mathcal{P}_T$

设 $\Phi_{t,s}$ 是线性常微分方程的基本解阵

$$\frac {\mathrm{d}}{\mathrm{d} t} \Phi_ {t, s} = A _ {t} \Phi_ {t, s}, \quad \Phi_ {s, s} = I, \quad \forall t > s, \quad \text { a.s. }$$

可以直接验证，方程(4.3.23)的强解是

$$\xi_ {t} = \Phi_ {t, 0} \xi_ {0} + \int_ {0} ^ {t} \Phi_ {t, s} b _ {s} \mathrm{d} s + \Phi_ {t, 0} \int_ {0} ^ {t} \Phi_ {s, 0} ^ {- 1} D _ {s} \mathrm{d} w _ {s}. \tag {4.3.24}$$

当 $A_{t}, b_{t}, D_{t}$ 为确定性时，由式 (4.3.24) 表达的 $\xi_{t}$ 是正态的.
