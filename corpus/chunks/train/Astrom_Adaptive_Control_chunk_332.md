# THEOREM 5.8 The passivity theorem

Consider a system obtained by connecting two systems $H_{1}$ and $H_{2}$ in a feedback loop as in Fig. 5.16. Let $H_{1}$ be strictly output passive and $H_{2}$ be passive. The closed-loop system is then BIBO stable.

Proof: Since $H_{1}$ is strictly output passive, we have

$$\langle y \mid e \rangle > \delta \| y \| ^ {2}$$

Since $e = u - H_2y$ , we have

$$\delta \| y \| ^ {2} \leq \langle y | e \rangle = \langle y | u \quad H _ {2} y \rangle = \langle y | u \rangle - \langle y | H _ {2} y \rangle \tag {5.55}$$

Since $H_{2}$ is passive, we have

$$\langle y \mid H _ {2} y \rangle \geq 0$$

and it then follows from Eq. (5.55) that

$$\delta \| y \| ^ {2} \leq \langle y | u \rangle \leq \| y \| \| u \|$$

where the last inequality follows from Schwartz inequality. We now get

$$\| y \| < \frac {1}{\delta} \| u \|$$

which proves the result.

Remark. The passivity theorem may also be regarded as an extension of Nyquist's stability theorem. Instability is avoided by having a loop transfer function with a phase lag less than $180^{\circ}$ . ☐
