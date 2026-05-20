| t | Value |
| --- | --- |
| t0 | +1 |
| t1 | -1 |
| t2 | 0 |
| t3 | -1 |
| t4 | 0 |
| tf* | +1 |
</details>

Figure 7.3 Normal Time-Optimal Control System

function $q_{j}^{*}(t)$ is zero only at four instants of time, and the time optimal control is piecewise constant function with simple switchings at $t_{1}, t_{2}, t_{3}$ , and $t_{4}$ . Thus, the optimal control $u_{j}^{*}(t)$ switches four times, or the number of switchings is four.

2. Singular Time-Optimal Control (STOC) System: Suppose that during the interval $[t_{0}, t_{f}^{*}]$ , there is one (or more) subintervals $[T_{1}, T_{2}]$ , such that

$$q _ {j} ^ {*} (t) = 0 \quad \forall t \in [ T _ {1}, T _ {2} ] \tag {7.1.30}$$

then, we have a singular time-optimal control (STOC) system, and the interval $[T_{1}, T_{2}]$ is called singularity intervals. The situation is shown in Figure 7.4. During this singularity intervals, the time-optimal control is not defined.
