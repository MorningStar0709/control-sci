# EXAMPLE 6.7 Indirect adaptive system with design singularities

Consider the system in Example 6.6, and let the controller be an indirect adaptive system that is based on estimation of the parameters of the model. The desired dynamics $A_{m}$ are chosen to correspond to a second-order system with $\omega = 1.5$ and $\zeta = 0.707$ . The observer polynomial is chosen to be $A_{n} = z$ .

Figure 6.8 shows the results obtained when the adaptive algorithm is applied to a first-order system

$$G (s) = \frac {1}{s + 1}$$

Notice the strange behavior of the output. This would have been even worse if the control signal had not been kept bounded in the simulation. The parameter estimates converge very quickly to values such that A and B have a common factor. The Diophantine equation is then singular, as shown in Example 6.6, and the controller parameters become very large. The consequences of canceling a possible common factor and making a design for a first-order system are illustrated in Fig. 6.9. In this particular case a factor is canceled if poles and zeros are so close that

(a)   
![](image/d8ed995ad5dab1e0eee88c274df0b5eb3206b681939765074d37e281cad9d994.jpg)

<details>
<summary>line</summary>

| Time | u_e | y |
| --- | --- | --- |
| 0 | -2 | -2 |
| 10 | 2 | -2 |
| 20 | 2 | -2 |
| 30 | -2 | -2 |
| 40 | 2 | -2 |
| 50 | -2 | -2 |
</details>

(b)   
![](image/7c455146f2e36f27f8c093a1407f2c3ddc840e4f5fc231cdfea50f72c5e4145d.jpg)

<details>
<summary>line</summary>

| Time | u |
| --- | --- |
| 0 | -5 |
| 10 | -2 |
| 20 | -2 |
| 30 | -5 |
| 40 | -2 |
| 50 | -2 |
</details>

(c)   
![](image/99b492d1e88e148e49ceb984ac8b85815ca082440613714503de5b77cb78793f.jpg)

<details>
<summary>line</summary>

| Time | â₁ | â₂ |
| --- | --- | --- |
| 0 | -1.0 | 1.0 |
| 10 | -1.0 | 1.0 |
| 20 | -1.0 | 1.0 |
| 30 | -1.0 | 1.0 |
| 40 | -1.0 | 1.0 |
| 50 | -1.0 | 1.0 |
</details>

(d)   
![](image/93514773b69e2c68343a7c40b0ccbc450d736d9e1bea6ae6cbd7749fb1c53a40.jpg)

<details>
<summary>line</summary>

| Time | ŝ₁ | r̂₁ | t̂₀ |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 |
| 20 | 0 | 0 | 0 |
| 30 | 0 | 0 | 0 |
| 40 | 10^4 | 10^4 | 10^4 |
| 50 | 10^4 | 10^4 | 10^4 |
</details>

Figure 6.8 Simulation of an indirect adaptive pole placement controller based on a second-order process model of a first-order process. (a) Output and reference value. (b) Control signal. (c) Estimated process parameters. (d) Calculated controller parameters.

$$\left| A \left(\frac {- b _ {1}}{b _ {0}}\right) \right| = \left| \frac {b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}}{b _ {0} ^ {2}} \right| \leq 0. 0 1 \tag {6.37}$$

The performance is now very good.

![](image/af761b41f60d19113ad4791fedf0dbf1ca2a9263827a071fd851e6d867b1f92e.jpg)
