# Laplace Transform Using MATLAB

MATLAB’s Symbolic Math Toolbox can be used to compute the Laplace transform of a given time function $f ( t )$ . To do so, the user must define the time function f (t) as the symbolic object f and the corresponding

Table 8.1 Laplace Transforms of Common Time Functions 

<table><tr><td>Number</td><td>Time Function,  $f(t)$ </td><td>Laplace Transform,  $\mathcal{L}\{f(t)\} = F(s)$ </td></tr><tr><td>1</td><td>Unit impulse,  $\delta(t)$ </td><td>1</td></tr><tr><td>2</td><td>Unit step,  $U(t)$ </td><td> $\frac{1}{s}$ </td></tr><tr><td>3</td><td>A</td><td> $\frac{A}{s}$ </td></tr><tr><td>4</td><td>Unit ramp,  $t$ </td><td> $\frac{1}{s^{2}}$ </td></tr><tr><td>5</td><td> $t^{2}$ </td><td> $\frac{2}{s^{3}}$ </td></tr><tr><td>6</td><td> $e^{-at}$ </td><td> $\frac{1}{s + a}$ </td></tr><tr><td>7</td><td> $te^{-at}$ </td><td> $\frac{1}{(s + a)^{2}}$ </td></tr><tr><td>8</td><td> $\sin \omega t$ </td><td> $\frac{\omega}{s^{2} + \omega^{2}}$ </td></tr><tr><td>9</td><td> $\cos \omega t$ </td><td> $\frac{s}{s^{2} + \omega^{2}}$ </td></tr><tr><td>10</td><td> $e^{-at} \sin \omega t$ </td><td> $\frac{\omega}{(s + a)^{2} + \omega^{2}}$ </td></tr><tr><td>11</td><td> $e^{-at} \cos \omega t$ </td><td> $\frac{s + a}{(s + a)^{2} + \omega^{2}}$ </td></tr></table>

Laplace transform is computed using the single-line command F = laplace(f). For example, the following MATLAB commands will determine the Laplace transform of f (t) = 3 sin 2t

>> syms t % define variable t (time) as a symbolic object   
>> f = 3\*sin(2\*t) % define function f (t) = 3 sin 2t as a symbolic object   
>> F = laplace(f) % compute the Laplace transform F(s)   
>> pretty(F) % display F in a format similar to typeset mathematics

The third and fourth commands will display F(s) as a symbolic function of s. Typing all four line commands shown above results in

![](image/0087573fb4d4cd17b12a8ceb5f4374482779ae9b01d0edd84be1f1b96585682a.jpg)

which is easily identified as the answer for Example 8.3 with A = 3 and ?? = 2.
