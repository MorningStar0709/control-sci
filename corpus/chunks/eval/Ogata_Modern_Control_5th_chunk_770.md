As a matter of course, we get the same $\mathbf { K } _ { e }$ regardless of the method employed.

The equation for the full-order state observer is given by Equation (10–57),

$$\dot {\widetilde {\mathbf {x}}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \widetilde {\mathbf {x}} + \mathbf {B} u + \mathbf {K} _ {e} y$$

or

$$
\left[ \begin{array}{c} \dot {\widetilde {x}} _ {1} \\ \dot {\widetilde {x}} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & - 1 0 0 \\ 1 & - 2 0 \end{array} \right] \left[ \begin{array}{c} \widetilde {x} _ {1} \\ \widetilde {x} _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u + \left[ \begin{array}{c} 1 2 0. 6 \\ 2 0 \end{array} \right] y
$$

Finally, it is noted that, similar to the case of pole placement, if the system order n is 4 or higher, methods 1 and 3 are preferred, because all matrix computations can be carried out by a computer, while method 2 always requires hand computation of the characteristic equation involving unknown parameters $k _ { e 1 } , k _ { e 2 } , \ldots , k _ { e n } .$ .

Effects of the Addition of the Observer on a Closed-Loop System. In the pole-placement design process, we assumed that the actual state ${ \bf x } ( t )$ was available for feedback. In practice, however, the actual state ${ \bf x } ( t )$ may not be measurable, so we will need to design an observer and use the observed state $\widetilde { \mathbf { x } } \left( t \right)$ for feedback as shown in Figure 10–12. The design process, therefore, becomes a two-stage process, the first stage being the determination of the feedback gain matrix K to yield the desired characteristic equation and the second stage being the determination of the observer gain matrix $\mathbf { K } _ { e }$ to yield the desired observer characteristic equation.

Let us now investigate the effects of the use of the observed state $\widetilde { \mathbf { x } } \left( t \right)$ rather than, the actual state ${ \bf x } ( t )$ , on the characteristic equation of a closed-loop control system.

Figure 10–12 Observed-state feedback control system.   
![](image/ee45195ae8eb975fcfa9dd6958752185256d283b53e66e0ae3a9a44e3a5597ec.jpg)

<details>
<summary>flowchart</summary>
