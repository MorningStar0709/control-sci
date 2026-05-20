$$K _ {a} = \lim _ {s \rightarrow 0} \frac {s ^ {2} K (T _ {a} s + 1) (T _ {b} s + 1) \cdots}{s ^ {N} (T _ {1} s + 1) (T _ {2} s + 1) \cdots} = \infty , \quad \text { for } N \geq 3$$

Thus, the steady-state error for the unit parabolic input is

$$e _ {\mathrm{ss}} = \infty , \quad \text { for type 0 and type 1 systems }e _ {\mathrm{ss}} = \frac {1}{K}, \quad \text { for type 2 systems }e _ {\mathrm{ss}} = 0, \quad \text { for type 3 or higher systems }$$

Figure 5–48 Response of a type 2 unity-feedback system to a parabolic input.   
![](image/f82d897238c8de772bd9cede40bb9359983e12aefc8064721b322ddc81d0dc29.jpg)

<details>
<summary>line</summary>

| t | r(t) | c(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| >0   | >r(t)| >c(t)
</details>

Note that both type 0 and type 1 systems are incapable of following a parabolic input in the steady state. The type 2 system with unity feedback can follow a parabolic input with a finite error signal. Figure 5–48 shows an example of the response of a type 2 system with unity feedback to a parabolic input. The type 3 or higher system with unity feedback follows a parabolic input with zero error at steady state.

Summary. Table 5–1 summarizes the steady-state errors for type 0, type 1, and type 2 systems when they are subjected to various inputs. The finite values for steadystate errors appear on the diagonal line.Above the diagonal, the steady-state errors are infinity; below the diagonal, they are zero.

Table 5–1 Steady-State Error in Terms of Gain K

<table><tr><td></td><td>Step Input $r(t) = 1$ </td><td>Ramp Input $r(t) = t$ </td><td>Acceleration Input $r(t) = \frac{1}{2}t^{2}$ </td></tr><tr><td>Type 0 system</td><td> $\frac{1}{1 + K}$ </td><td> $\infty$ </td><td> $\infty$ </td></tr><tr><td>Type 1 system</td><td>0</td><td> $\frac{1}{K}$ </td><td> $\infty$ </td></tr><tr><td>Type 2 system</td><td>0</td><td>0</td><td> $\frac{1}{K}$ </td></tr></table>

Remember that the terms position error, velocity error, and acceleration error mean steady-state deviations in the output position. A finite velocity error implies that after transients have died out, the input and output move at the same velocity but have a finite position difference.
