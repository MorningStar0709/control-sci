$$\dot {\tilde {\boldsymbol {\eta}}} = \hat {\mathbf {A}} \tilde {\boldsymbol {\eta}} + \hat {\mathbf {B}} y + \hat {\mathbf {F}} u \tag {10-90}$$

Equation (10–90) and Equation (10–88) together define the minimum-order observer. Since

$$
\begin{array}{l} y = \left[ \begin{array}{c c} 1 & \mathbf {0} \end{array} \right] \left[ \begin{array}{c} x _ {a} \\ \hdashline \mathbf {x} _ {b} \end{array} \right] \\ \widetilde {\mathbf {x}} = \left[ \begin{array}{c} x _ {a} \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c} y \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c} \mathbf {0} \\ \mathbf {I} _ {n - 1} \end{array} \right] \left[ \widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} y \right] + \left[ \begin{array}{c} 1 \\ \mathbf {K} _ {e} \end{array} \right] y \\ \end{array}
$$

where 0 is a row vector consisting of (n-1) zeros, if we define

$$
\hat {\mathbf {C}} = \left[ \begin{array}{c} \mathbf {0} \\ \hline \mathbf {I} _ {n - 1} \end{array} \right], \qquad \hat {\mathbf {D}} = \left[ \begin{array}{c} 1 \\ \hline \mathbf {K} _ {e} \end{array} \right]
$$

then we can write $\widetilde { \mathbf { x } }$ in terms of $\widetilde { \pmb { \eta } }$ and y as follows:

$$\widetilde {\mathbf {x}} = \hat {\mathbf {C}} \widetilde {\boldsymbol {\eta}} + \hat {\mathbf {D}} y \tag {10-91}$$

This equation gives the transformation from $\widetilde { \pmb { \eta } }$ to $\widetilde { \mathbf { x } }$ .

Figure 10–17 shows the block diagram of the observed-state feedback control system with the minimum-order observer, based on Equations (10–79), (10–80), (10–90), (10–91) and $u = - \mathbf { K } \widetilde { \mathbf { x } }$ .

Next we shall derive the observer error equation. Using Equation (10–83), Equation (10–86) can be modified to

$$\dot {\widetilde {\mathbf {x}}} _ {b} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \widetilde {\mathbf {x}} _ {b} + \mathbf {A} _ {b a} x _ {a} + \mathbf {B} _ {b} u + \mathbf {K} _ {e} \mathbf {A} _ {a b} \mathbf {x} _ {b} \tag {10-92}$$

Figure 10–17 System with observed-state feedback, where the observer is the minimum-order observer.   
![](image/94eb755dbdeae982d76dd04c8e8766273922c4e9bb0b23ef796f7e8cdf402bf9.jpg)

<details>
<summary>flowchart</summary>
