$$
\left[ \begin{array}{c} \tilde {\dot {\eta}} _ {2} \\ \tilde {\dot {\eta}} _ {3} \end{array} \right] = \left[ \begin{array}{c c} - 1 4 & 1 \\ - 1 6 & - 6 \end{array} \right] \left[ \begin{array}{c} \tilde {\eta} _ {2} \\ \tilde {\eta} _ {3} \end{array} \right] + \left[ \begin{array}{c} - 1 9 1 \\ - 2 6 0 \end{array} \right] y + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u
$$

where

$$
\left[ \begin{array}{c} \widetilde {\eta} _ {2} \\ \widetilde {\eta} _ {3} \end{array} \right] = \left[ \begin{array}{c} \widetilde {x} _ {2} \\ \widetilde {x} _ {3} \end{array} \right] - \mathbf {K} _ {e} y
$$

or

$$
\left[ \begin{array}{c} \widetilde {x} _ {2} \\ \widetilde {x} _ {3} \end{array} \right] = \left[ \begin{array}{c} \widetilde {\eta} _ {2} \\ \widetilde {\eta} _ {3} \end{array} \right] + \mathbf {K} _ {e} x _ {1}
$$

If the observed-state feedback is used, then the control signal u becomes

$$
u = - \mathbf {K} \widetilde {\mathbf {x}} = - \mathbf {K} \left[ \begin{array}{c} x _ {1} \\ \widetilde {x} _ {2} \\ \widetilde {x} _ {3} \end{array} \right]
$$

where K is the state feedback gain matrix. Figure 10–18 is a block diagram showing the configuration of the system with observed-state feedback, where the observer is the minimum-order observer.

![](image/371e462c7fff063ae1918759afeab97e042041ec47f309d39690e92c948f244b.jpg)

<details>
<summary>flowchart</summary>
