This analysis assumes that the motor is well coupled to the mass and that the time constant of the inductor is small enough that it doesn’t factor into the motor equations. The latter is a pretty good assumption for a CIM motor (see figures E.15 and E.16). If more mass is added to the motor armature, the response timescales increase and the inductance matters even less.

![](image/9fe31c1be64ebed49aea54e883e63f29575e696d6a5af4faa6c52efbc7be7ec6.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference | Step response |
| -------- | --------- | ------------- |
| 0.00     | 1.0       | 0.0           |
| 0.05     | 1.0       | 0.9           |
| 0.10     | 1.0       | 1.0           |
| 0.15     | 1.0       | 1.0           |
| 0.20     | 1.0       | 1.0           |
| 0.25     | 1.0       | 1.0           |
</details>

![](image/1f7936a9f101de05f2cd0173b9281e2f05f89850b4ebc1547aa91322cf02af4c.jpg)

<details>
<summary>line</summary>

| Time (s) | Reference | Step response |
| -------- | --------- | ------------- |
| 0.00     | 1.0       | 0.0           |
| 0.05     | 1.0       | 0.9           |
| 0.10     | 1.0       | 1.0           |
| 0.15     | 1.0       | 1.0           |
| 0.20     | 1.0       | 1.0           |
| 0.25     | 1.0       | 1.0           |
</details>

Figure E.15: Step response of secondorder DC motor plant augmented with position $( L = 2 3 0 \mu \mathrm { H } )$   
Figure E.16: Step response of first-order DC motor plant augmented with position (L = 0 μH)

Next, we’ll try a PD loop. (This will use a perfect derivative, but anyone following along closely already knows that we can’t really take a derivative here, so the math will need to be updated at some point. We could switch to discrete time and pick a differentiation method, or pick some other way of modeling the derivative.)

$$V = K _ {p} (\omega_ {g o a l} - \omega) + K _ {d} s (\omega_ {g o a l} - \omega)$$

Substitute this controller into equation (E.13).

$$s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t}}{J R} \left(K _ {p} (\omega_ {g o a l} - \omega) + K _ {d} s (\omega_ {g o a l} - \omega)\right)s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t} K _ {p}}{J R} (\omega_ {g o a l} - \omega) + \frac {K _ {t} K _ {d} s}{J R} (\omega_ {g o a l} - \omega)s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t} K _ {p}}{J R} \omega_ {g o a l} - \frac {K _ {t} K _ {p}}{J R} \omega + \frac {K _ {t} K _ {d} s}{J R} \omega_ {g o a l} - \frac {K _ {t} K _ {d} s}{J R} \omega$$

Collect the common terms on separate sides and refactor.
