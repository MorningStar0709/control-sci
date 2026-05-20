# Plotting Polar Grids in the Root-Locus Diagram. The command

sgrid

overlays lines of constant damping ratio $( \zeta = 0 \sim 1$ with 0.1 increment) and circles of constant $\omega _ { n }$ on the root-locus plot. See MATLAB Program 6–5 and the resulting diagram shown in Figure 6–22.

<table><tr><td>MATLAB Program 6-5</td></tr><tr><td>sgridv = [-3 3 -3 3]; axis(v); axis(&#x27;square&#x27;)title(&#x27;Constant \zeta Lines and Constant \omega_n Circles&#x27;)xlabel(&#x27;Real Axis&#x27;)ylabel(&#x27;Imag Axis&#x27;)</td></tr></table>

If only particular constant $\zeta$ lines (such as the $\zeta = 0 . 5$ line and $\zeta = 0 . 7 0 7$ line) and particular constant $\omega _ { n }$ circles (such as the $\omega _ { n } = 0 . 5$ circle, $\omega _ { n } = 1$ circle, and $\omega _ { n } = 2 { \mathrm { c i r } } .$ - cle) are desired, use the following command:

$$\operatorname{sgrid} ([ 0. 5, 0. 7 0 7 ], [ 0. 5, 1, 2 ])$$

If we wish to overlay lines of constant $\zeta$ and circles of constant $\omega _ { n }$ as given above to a root-locus plot of a negative feedback system with

$$\text { num } = [ 0 0 0 1 ]\mathrm{den} = [ 1 \quad 4 \quad 5 \quad 0 ]$$

Constant z Lines and Constant $\omega _ { n }$ Circles   
![](image/072c41ceeb97bf47d9daba27d740823f84ab0febd53dc6a164b4db6cf77eaa4b.jpg)

<details>
<summary>radar</summary>

| Real Axis | Imag Axis | Value |
| --- | --- | --- |
| -2.5 | 2.5 | 0.64 |
| -2.0 | 2.0 | 0.5 |
| -1.5 | 1.5 | 0.34 |
| -1.0 | 1.0 | 0.16 |
| -0.5 | 0.5 | 0 |
| 0.0 | 0.0 | 0 |
| 0.5 | -0.5 | 0 |
| 1.0 | -1.0 | 0 |
| 1.5 | -1.5 | 0 |
| 2.0 | -2.0 | 0 |
| 2.5 | -2.5 | 0 |
| -2.5 | -2.5 | 0.76 |
| -2.0 | -2.0 | 0.86 |
| -1.5 | -1.5 | 0.94 |
| -1.0 | -1.0 | 0.985 |
| -0.5 | -0.5 | 0.985 |
| 0.0 | 0.0 | 0 |
| 0.5 | 0.5 | 0 |
| 1.0 | 1.0 | 0 |
| 1.5 | 1.5 | 0 |
| 2.0 | 2.0 | 0 |
| 2.5 | 2.5 | 0 |
| -2.5 | -2.5 | 0.86 |
| -2.0 | -2.0 | 0.94 |
| -1.5 | -1.5 | 0.985 |
| -1.0 | -1.0 | 0.985 |
| -0.5 | -0.5 | 0 |
| 0.0 | 0.0 | 0 |
| 0.5 | -0.5 | 0 |
| 1.0 | -1.0 | 0 |
| 1.5 | -1.5 | 0 |
| 2.0 | -2.0 | 0 |
| 2.5 | -2 .5 | 0 |
| -2.5 | -2.5 | 0.76 |
| -2.0 | -2.0 | 0.86 |
| -1.5 | -1.5 | 0.94 |
| -1.0 | -1.0 | 0.985 |
| -0.5 | -0.5 | 1 |
| 0.0 | 0.0 | 1 |
| 0.5 | -0.5 | 1 |
| 1.0 | -1.0 | 1 |
| 1.5 | -1.5 | 1 |
| 2.0 | -2.0 | 1 |
| 2.5 | -2 .5 | 1 |
| -2.5 | -2 .5 | 0 |
| -2.0 | -2 .0 | 0 |
| -1.5 | -1 .5 | 0 |
| -1.0 | -1.0 | 0 |
| -0.5 | -0.5 | 0 |
| 0.0 | 0 | 0 |
| 0.5 | -0.5 | 0 |
| 1.0 | -1.0 | 0 |
| 1.5 | -1 .5 | 0 |
| 2.0 | -2 .5 | 0 |
| 2.5 | -3 | 0 |
The chart displays a scatter plot with 'Real Axis' on the x-axis and 'Imag Axis' on the y-axis, showing a series of data points for each 'Real Axis' value.
</details>
