# Example 9.15 cont.

The resulting root locus is

![](image/b1679b163baeaec7ce54d3f9e0ad6bcdbf94ea8c6c3e09f6c44a8b0a3c3cb5fa.jpg)

<details>
<summary>scatter</summary>

| Point | Real | Imaginary |
| --- | --- | --- |
| Black Square | 1.6 | 0.98 |
| Blue X | 0.8 | 0.98 |
| Blue Square | 0.34 | 0.98 |
| Blue X | 0.77 | 0.98 |
| Blue X | 1.6 | 0.98 |
| Blue X | 2.4 | 0.98 |
| Blue X | 0.34 | 0.98 |
| Blue X | 0.77 | 0.98 |
| Blue X | 1.6 | 0.98 |
| Blue X | 2.4 | 0.98 |
| Blue X | 0.34 | 0.98 |
| Blue X | 0.77 | 0.98 |
| Blue X | 1.6 (at origin) | 0.98 |
| Green Vertical Line (Real axis) | 0.0 | 0.0 |
| Arrows indicate directional changes along axes.
</details>

The two origin poles are now going unstable! Clicking the RL shows that the origin poles are already seriously unstable when the CC poles at s = −1 are just going below the purple %OS line and not even close to the TS region. A very bad option.

Even worse, lots of further root locus experimentation did not yield any controller which could be stable and have poles in the desired region!

What to do? We must be sure to consider other controllers. Since we have a stability problem, we should seriously consider removing the pole we added at the origin (remember, the plant also put one there.) The poles at s = 0 are good for steady state error, but make stability harder. We can eliminate the PID controller's pole at zero if we get rid of the integrator in the PID controller: $K _ { I } = 0$ but this also eliminates one zero. Using this PD controller we have a zero and a gain as our remaining design parameters:

$$C _ {P D} = K _ {D} (s - z) = K _ {D} s + K _ {P}$$

where $K _ { P } = K _ { D } ( - z ) .$

Try 3:

$$C _ {3} (s) = K (s + 0. 1)$$

(to which we must add the regularization pole as before.) Modifying the code a bit:

```txt
