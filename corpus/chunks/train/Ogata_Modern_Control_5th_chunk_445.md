![](image/87f8ce786888115891cf62753d01d4c228b154b2aef2256f7790d26b15406a4f.jpg)

<details>
<summary>other</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -1.0 | 5.0 |
| -0.5 | 1.0 |
| 0.0 | 0.0 |
| 0.5 | -1.0 |
| 1.0 | -2.0 |
| 1.5 | -3.0 |
| 2.0 | -4.0 |
</details>

Figure 7–39   
Nyquist plot of

$$G (s) = \frac {1}{s (s + 1)}.$$

A MATLAB program using this nyquist command is shown in MATLAB Program 7–8. The resulting Nyquist plot is presented in Figure 7–40.

<table><tr><td>MATLAB Program 7-8</td></tr><tr><td>% ---- Nyquist plot----</td></tr><tr><td>num = [1];</td></tr><tr><td>den = [1 1 0];</td></tr><tr><td>w = 0.1:0.1:100;</td></tr><tr><td>[re,im,w] = nyquist(num,den,w);</td></tr><tr><td>plot(re,im)</td></tr><tr><td>v = [-2 2 -5 5]; axis(v)</td></tr><tr><td>grid</td></tr><tr><td>title(&#x27;Nyquist Plot of G(s) = 1/[s(s + 1)]&#x27;)</td></tr><tr><td>xlabel(&#x27;Real Axis&#x27;)</td></tr><tr><td>ylabel(&#x27;Imag Axis&#x27;)</td></tr></table>

![](image/b8b30af1ca0d0f9aeec95af55af19021a1b098f9832293f0eac058e8b6cfaaaa.jpg)

<details>
<summary>other</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -1.0 | -5.0 |
| -0.5 | -2.0 |
| 0.0 | 0.0 |
</details>

Figure 7–40

Nyquist plot of

$$G (s) = \frac {1}{s (s + 1)}$$

for v 7 0.

Drawing Nyquist Plots of a System Defined in State Space. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

where state vector (n-vector)x =

output vector (m-vector)y =

control vector (r-vector)u =

state matrix (n\*n matrix)A =

control matrix (n\*r matrix)B =

output matrix (m\*n matrix)C =

D = direct transmission matrix (m\*r matrix)

Nyquist plots for this system may be obtained by the use of the command

$$\text { nyquist } (A, B, C, D)$$

This command produces a series of Nyquist plots, one for each input and output combination of the system. The frequency range is automatically determined.

The command

$$\text { nyquist } (A, B, C, D, i u)$$

produces Nyquist plots from the single input iu to all the outputs of the system, with the frequency range determined automatically. The scalar iu is an index into the inputs of the system and specifies which input to use for the frequency response.

The command

$$\text { nyquist } (A, B, C, D, i u, w)$$

uses the user-supplied frequency vector w. The vector w specifies the frequencies in radians per second at which the frequency response should be calculated.
