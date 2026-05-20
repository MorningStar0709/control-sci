MATLAB Program 6–16   
```matlab
% ---- Root-Locus Plots ----
num = [1];
den = [1 3 2 0];
numa = [1];
dena = [1 3 3 1];
K1 = 0:0.1:0.3;
K2 = 0.3:0.005:0.5;
K3 = 0.5:0.5:10;
K4 = 10:5:100;
K = [K1 K2 K3 K4];
r = rlocus(num,den,K);
a = rlocus(numa,dena,K);
plot(r,'o')
hold
Current plot held
plot(a,'-')
v = [-4 4 -4 4]; axis(v)
grid
title('Root-Locus Plot of G(s) = K/[s(s+1)(s+2)] and Asymptotes')
xlabel('Real Axis')
ylabel('Imag Axis') 
```

Root-Locus Plot of G(s) = K/[s(s+1)(s+2)] and Aysmptotes   
![](image/720407582c235ab286a2b8240aa2679de8afa63e02f983a23e86f1db7515a373.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -3.5 | 0.0 |
| -3.0 | 0.0 |
| -2.5 | 0.0 |
| -2.0 | 0.0 |
| -1.5 | 0.0 |
| -1.0 | 0.0 |
| -0.5 | 0.0 |
| 0.0 | 0.0 |
| 0.5 | 0.0 |
| 1.0 | 0.0 |
| 1.5 | 0.0 |
| 2.0 | 0.0 |
| 2.5 | 0.0 |
| 3.0 | 0.0 |
| 3.5 | 0.0 |
| 4.0 | 0.0 |
</details>

Figure 6–71 Root-locus plot.

A–6–9. Plot the root loci and asymptotes for a unity-feedback system with the following feedforward transfer function:

$$G (s) = \frac {K}{(s ^ {2} + 2 s + 2) (s ^ {2} + 2 s + 5)}$$

Determine the exact points where the root loci cross the jv axis

Solution. The feedforward transfer function $G ( s )$ can be written as

$$G (s) = \frac {K}{s ^ {4} + 4 s ^ {3} + 1 1 s ^ {2} + 1 4 s + 1 0}$$

Note that as s approaches infinity, $\operatorname* { l i m } _ { s \to \infty } G ( s )$ can be written as

$$
\begin{array}{l} \lim _ {s \rightarrow \infty} G (s) = \lim _ {s \rightarrow \infty} \frac {K}{s ^ {4} + 4 s ^ {3} + 1 1 s ^ {2} + 1 4 s + 1 0} \\ \div \lim _ {s \rightarrow \infty} \frac {K}{s ^ {4} + 4 s ^ {3} + 6 s ^ {2} + 4 s + 1} \\ = \lim _ {s \rightarrow \infty} \frac {K}{(s + 1) ^ {4}} \\ \end{array}
$$

where we used the following formula:

$$(s + a) ^ {4} = s ^ {4} + 4 a s ^ {3} + 6 a ^ {2} s ^ {2} + 4 a ^ {3} s + a ^ {4}$$

The expression

$$\lim _ {s \rightarrow \infty} G (s) = \lim _ {s \rightarrow \infty} \frac {K}{(s + 1) ^ {4}}$$

gives the equation for the asymptotes.

The MATLAB program to plot the root loci of G(s) and the asymptotes is given in MATLAB Program 6–17. Note that the numerator and denominator for G(s) are

$$\mathrm{num} = [ 1 ]\mathrm{den} = [ 1 \quad 4 \quad 1 1 \quad 1 4 \quad 1 0 ]$$

For the numerator and denominator of the asymptotes $\operatorname* { l i m } _ { s \to \infty } G ( s )$ we used

$$\mathrm{numa} = [ 1 ]\mathrm{dena} = [ 1 \quad 4 \quad 6 \quad 4 \quad 1 ]$$

Figure 6–72 shows the plot of the root loci and asymptotes.

Since the characteristic equation for the system is

$$(s ^ {2} + 2 s + 2) (s ^ {2} + 2 s + 5) + K = 0$$
