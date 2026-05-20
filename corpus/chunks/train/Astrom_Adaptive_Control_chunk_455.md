# Measurement Noise

We now investigate the effects of measurement noise. The simulation shown in Fig. 6.13 indicates that measurement noise may cause the parameters to drift. Figure 6.17 shows parameter $\hat{\theta}_2$ as a function of parameter $\hat{\theta}_1$ with and without measurement noise. The simulation indicates that the equilibrium is lost in the presence of measurement noise. The parameters move toward a set close to the equilibrium set, oscillate rapidly in the neighborhood of this set, and drift along the set. The analysis tools developed will now be used to explain the behavior of the system. Assume that the command signal is a step with amplitude $u_0$ and that the measurement noise can be modeled as an additive zero mean signal $n$ at the process output. It follows from Eqs. (6.57) that the error cannot be made identically zero by proper choice of the parameters. Hence no true equilibrium exists such that the parameters are constant. The phenomenon is a typical behavior of a system that lacks structural stability. Intuitively, the results can be explained as follows: A step input is persistently exciting of order 1 only, which means that it admits consistent estimation of one parameter only. When two parameters are adjusted, the equilibrium values of the parameters make a submanifold, not a point. Measurement errors and other disturbances may cause the parameters to drift along the equilibrium set. In the presence of unmodeled dynamics, the feedback gain may then become so large that the closed-loop system becomes unstable. By using averaging, the equilibrium set and the drift rate along the set can be determined.

![](image/14c44f948a876365c3d4b5ecd1cad2bdbe5a98be4f7e4aebc7362ee878599be5.jpg)

<details>
<summary>line</summary>

| θ̂₁ | θ̂₂ (a) | θ̂₂ (b) |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.2 | ~0.0 | ~-0.05 |
| 0.4 | ~-0.05 | ~-0.1 |
| 0.6 | ~0.15 | — |
| 0.8 | ~0.35 | — |
| 1.0 | ~0.45 | — |
</details>

Figure 6.17 Phase plane of the controller parameters (a) with and (b) without measurement noise.

The parameter values will drift also in the nominal case. However, the closed-loop system is stable for all parameter values.
