| Time | u |
| --- | --- |
| 0.0 | 0.0 |
| 0.5 | -2.0 |
| 1.0 | -7.0 |
| 1.5 | -1.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
</details>

![](image/ea30c71fae5f108ae61f08ad28ca479ec9da4512fdf0b883067e0e8e13d0b418.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | 0 |
| 1 | 100 |
| 2 | 0 |
| 3 | 0 |
</details>

Figure 6.21 Simulation of the control law of Eqs. (6.94) applied to the plants (a) $G(s) = 1 / (1 - s)$ and (b) $G(s) = 1 / (s - 1)$ .

Integration of the equation for $\hat{\theta}$ gives

$$\hat {\theta} (t) = \int_ {0} ^ {t} y ^ {2} (t) d t$$

It then follows that

$$\lim _ {t \rightarrow \infty} y (t) = 0$$

![](image/0f4f7d564915931c0e6e630c76823276b11d69c16e824757b431f18e88231dbd.jpg)

The behavior of a universal stabilizer is illustrated in Fig. 6.21. A reference value is used in the simulations, and the control law is then modified to

$$f (\hat {\theta}, y) = (u _ {c} - y) \hat {\theta} ^ {2} \cos \hat {\theta} \tag {6.94}g (\hat {\theta}, y) = (u _ {c} - y) ^ {2}$$

Notice that the control law of Eqs. (6.94) can be interpreted as proportional feedback with the gain $k = \hat{\theta}^{2} \cos \hat{\theta}$ . The behavior of the control law can be interpreted as follows. Sweep over all possible controller gains and stop when a stabilizing gain has been found. The function g can be interpreted as the rate of change of the gain sweep. The rate is large for large errors and small for small errors. The form $\cos \hat{\theta}$ makes sure that the gains can be both positive and negative. Universal stabilizers may show very violent behavior. This not surprising, since the system may be temporarily unstable during the sweep over the gains.

The control law of Eqs. (6.94) is useful because it does not contain any parameters that relate to the system that it stabilizes. It is therefore called a universal stabilizer. However, the control law is restricted to a first-order system. In attempting to generalize Theorem 6.10 to higher-order systems, the following question was posed. How much prior information about an unknown system is required to stabilize it? This question was answered in a general setting by Mårtensson (1985), who showed that it is sufficient to know the order of a stabilizing fixed-gain controller. If a transfer function is given, it is unfortunately a nontrivial task to find the minimal order of a stabilizing controller.
