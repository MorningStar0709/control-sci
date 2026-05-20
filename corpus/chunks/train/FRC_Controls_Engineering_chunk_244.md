# 8.7.4 Improving model accuracy

Figures 8.4 and 8.5 demonstrate the tracking behavior of the linearized differential drive controller.

![](image/4ae15d8fdb72833a287d1c303f500cd6182a9a2bbcd84c6d32e3c6abed6a11b0.jpg)

<details>
<summary>line</summary>

| x (m) | Reference | State |
| --- | --- | --- |
| 1 | 13.0 | 13.0 |
| 2 | 13.5 | 13.8 |
| 4 | 14.5 | 15.0 |
| 6 | 15.5 | 16.0 |
| 8 | 16.5 | 17.0 |
| 10 | 18.0 | 18.0 |
</details>

Figure 8.4: Linear time-varying differential drive controller x-y plot (first-order)

![](image/e5650c4b897e9e9653fe2a669e112abd0939e17c168ed2c6db82fbfff81ae343.jpg)  
Figure 8.5: Linear time-varying differential drive controller response (first-order)

The linearized differential drive model doesn’t track well because the first-order linearization of A doesn’t capture the full heading dynamics, making the model update inaccurate. This linearization inaccuracy is evident in the Hessian matrix (second partial derivative with respect to the state vector) being nonzero.

$$
\frac {\partial^ {2} f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x} ^ {2}} = \left[ \begin{array}{c c c c c} 0 & 0 & - \frac {v _ {l} + v _ {r}}{2} \cos \theta & 0 & 0 \\ 0 & 0 & - \frac {v _ {l} + v _ {r}}{2} \sin \theta & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right]
$$

The second-order Taylor series expansion of the model around $\mathbf { x } _ { \mathrm { 0 } }$ would be

$$f (\mathbf {x}, \mathbf {u} _ {0}) \approx f (\mathbf {x} _ {0}, \mathbf {u} _ {0}) + \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} (\mathbf {x} - \mathbf {x} _ {0}) + \frac {1}{2} \frac {\partial^ {2} f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x} ^ {2}} (\mathbf {x} - \mathbf {x} _ {0}) ^ {2}$$

To include higher-order dynamics in the linearized differential drive model integration, we’ll apply the Dormand-Prince integration method (RKDP) from theorem 7.9.3 to equation (8.12).

Figures 8.6 and 8.7 show a simulation using RKDP instead of the first-order model.   
![](image/64537b536329085552f921ee891f1441230a6c5c82dfcb50302245fa5b4ec25b.jpg)

<details>
<summary>line</summary>

| x (m) | Reference | State |
| --- | --- | --- |
| 1 | 13.0 | 13.5 |
| 2 | 13.5 | 14.0 |
| 4 | 14.5 | 15.0 |
| 6 | 15.5 | 16.0 |
| 8 | 16.5 | 17.0 |
| 10 | 17.5 | 18.0 |
</details>

Figure 8.6: Linear time-varying differential drive controller (global reference frame formulation) x-y plot
