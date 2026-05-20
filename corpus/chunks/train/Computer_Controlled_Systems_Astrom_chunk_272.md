![](image/44101501eabca4e4e66b6114d05bf49a3f586fe051500ba587fff60888f4dd63.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 2 |
| 10 | 1 | 1 |
| 20 | 1 | 0 |
| 30 | 1 | -1 |
| 40 | 1 | 0 |
| 50 | 1 | 0 |
| 60 | 1 | 0 |
| 70 | 1 | 0 |
| 80 | 1 | 0 |
</details>

Figure 4.20 Output and input when the reference signal $u_{c}$ is a step and the disturbance v a short pulse.

Observer design. It is now assumed that only the output can be measured. The other states are reconstructed using a full-state observer of the form (4.28). The eigenvalues of $\Phi - KC$ are chosen in the same pattern as the closed-loop poles but a factor $\alpha_{0}$ farther away from the origin, that is, in continuous time we assume that we have

$$\left(s ^ {2} + 2 \zeta_ {m} \alpha_ {0} \omega_ {m} s + (\alpha_ {0} \omega_ {m}) ^ {2}\right) (s + \alpha_ {0} \alpha_ {1} \omega_ {m}) = 0$$

This characteristic equation is transferred to sampled-data form using h = 0.5. Figure 4.21 shows the same as Fig. 4.20 when an observer is used. The output is shown for $\alpha_{0} = 2$ . The continuous-time equivalence of the fastest pole of the closed-loop system when using the observer is $-\alpha_{0}\alpha_{1}\omega_{m}$ . For $\alpha_{0} = 2$ , $\alpha_{1} = 2$ , and $\omega_{m} = 0.5$ , we get the pole -2. This implies that the used sampling interval (h = 0.5) is a little too long. There is, however, no significant difference in the response when h is decreased to 0.25.

Summary. The example shows the design using state feedback and the observer. The response to the reference value change is the same, because the system and the observer have the same initial values. The response to the disturbance deteriorates slightly when the observer is used compared to direct-state feedback. The observer is twice as fast as the desired closed-loop response. One important aspect of the control problem that has not been captured is the effect of model uncertainty. This will be discussed in the next chapter. Notice that there is no integrator in the controller. The steady-state error will be zero even in the presence of a disturbance because the process dynamics has an integrator.

![](image/5f9a1c5df510a0d80ac6ddbc480194d9b0de745e63a29e1aa8143c9f86bfd1c0.jpg)

<details>
<summary>line</summary>

| Time | Output | Input |
| --- | --- | --- |
| 0 | 0 | 2 |
| 10 | 1 | 0 |
| 20 | 1 | 0 |
| 30 | 1 | -1 |
| 40 | 1 | 0 |
| 50 | 1 | 0 |
| 60 | 1 | 0 |
| 70 | 1 | 0 |
| 80 | 1 | 0 |
</details>

Figure 4.21 The same as Fig. 4.20, but using state feedback from observed states when $\alpha_{0}=2$ .
