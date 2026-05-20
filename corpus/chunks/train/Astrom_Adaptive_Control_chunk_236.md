# EXAMPLE 4.7 Effect of filtering

Consider the process

$$y (t) + a y (t - 1) = b u (t - 1) + e (t) + c e (t - 1)$$

where $a = -0.9$ , $b = 3$ , and $c = -0.3$ , which is the same process as in Examples 4.4 and 4.5. Let the filter be

$$\frac {Q ^ {*}}{P ^ {*}} = \frac {1 + q _ {1} q ^ {- 1}}{1 + p _ {1} q ^ {- 1}}$$

The identity of Eq. (4.34) gives the solution

$$s _ {0} = c + q _ {1} - a - p _ {1}s _ {1} = c q _ {1} - a p _ {1}$$

The control law is given by Eq. (4.35), with

$$R _ {1} ^ {*} P ^ {*} B ^ {+ *} = b (1 + p _ {1} q ^ {- 1})$$

![](image/60b230cbc3deb44f5d356ab1ec5d23c6b6a77c1064472a672086484e1c0e865e.jpg)

<details>
<summary>line</summary>

| p1 | Curve Type | Description |
| --- | --- | --- |
| -0.3 | Curve | p1 = -0.3 |
| 0 | Curve | p1 = 0 |
| 0.3 | Curve | p1 = 0.3 |
| q1 | Point | p1 = -0.3 |
| q1 | Point | p1 = 0 |
| q1 | Point | p1 = 0.3 |
</details>

Figure 4.10 The output variance, $V_{y}$ , and input variance, $V_{u}$ , as functions of $q_{1}$ of the system in Example 4.7 when $p_{1} = -0.3, 0$ , and 0.3. Three different cases are indicated by dots: (a) $p_{1} = q_{1} = 0$ ; (b) $p_{1} = 0$ , $q_{1} = -0.3$ ; (c) $p_{1} = -0.3$ , $q_{1} = -0.9$ .

![](image/53cb28bdc296e9444cb199465c41540c06fb031f12efb4e6b03e6d1bdc61264a.jpg)

<details>
<summary>line</summary>

| Time | Σy²(k) (a) | Σy²(k) (b) | Σy²(k) (c) | Σu²(k) (a) | Σu²(k) (b) | Σu²(k) (c) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 100 | ~100 | ~150 | ~250 | ~5 | ~3 | ~1 |
| 200 | ~200 | ~250 | ~450 | ~8 | ~5 | ~2 |
| 300 | ~300 | ~350 | ~650 | ~12 | ~7 | ~3 |
| 400 | ~400 | ~450 | ~750 | ~16 | ~9 | ~4 |
| 500 | ~500 | ~550 | ~850 | ~22 | ~11 | ~5 |
</details>

Figure 4.11 Simulation of the generalized self-tuning algorithm on the system in Example 4.7 when (a) $p_{1} = q_{1} = 0$ (minimum-variance control); (b) $p_{1} = 0$ , $q_{1} = -0.3$ ; (c) $p_{1} = -0.3$ , $q_{1} = -0.9$ (open-loop system).

The closed-loop system becomes

$$y (t) = \frac {1 + p _ {1} q ^ {- 1}}{1 + q _ {1} q ^ {- 1}} e (t)u (t) = - \frac {s _ {0} + s _ {1} q ^ {- 1}}{b (1 + q _ {1} q ^ {- 1})} e (t)$$
