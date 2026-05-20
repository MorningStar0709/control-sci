$$\lim _ {s \rightarrow \infty} \frac {K}{s ^ {3} + 3 s ^ {2} + 2 s} \div \lim _ {s \rightarrow \infty} \frac {K}{s ^ {3} + 3 s ^ {2} + 3 s + 1} = \frac {K}{(s + 1) ^ {3}}$$

the equation for the asymptotes may be given by

$$G _ {a} (s) = \frac {K}{(s + 1) ^ {3}}$$

Hence, for the system we have

$$\mathrm{num} = [ 1 ]\mathrm{den} = [ 1 \quad 3 \quad 2 \quad 0 ]$$

and for the asymptotes,

$$\mathrm{numa} = [ 1 ]\mathrm{dena} = [ 1 \quad 3 \quad 3 \quad 1 ]$$

In using the following root-locus and plot commands

$$r = r l o c u s (n u m, d e n)a = r l o c u s (n u m a, d e n a)\operatorname{plot} ([ r a ])$$

the number of rows of r and that of a must be the same. To ensure this, we include the gain constant K in the commands. For example,

$$\mathrm{K} 1 = 0: 0. 1: 0. 3;\mathrm{K} 2 = 0. 3: 0. 0 0 5: 0. 5:\mathrm{K} 3 = 0. 5: 0. 5: 1 0;\mathrm{K} 4 = 1 0: 5: 1 0 0;\mathrm{K} = [ \mathrm{K1} \quad \mathrm{K2} \quad \mathrm{K3} \quad \mathrm{K4} ]r = r l o c u s (n u m, d e n, K)a = r l o c u s (n u m a, d e n a, K)\mathrm{y} = [ \mathrm{r} \quad \mathrm{a} ]\operatorname{plot} (y, ^ {\prime} - ^ {\prime})$$

MATLAB Program 6–15 will generate a plot of root loci and their asymptotes as shown in Figure 6–70.

MATLAB Program 6–15   
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
y = [r a];
plot(y,'-')
v = [-4 4 -4 4]; axis(v)
grid
title('Root-Locus Plot of G(s) = K/[s(s + 1)(s + 2)] and Asymptotes')
xlabel('Real Axis')
ylabel('Imag Axis')
% ***** Manually draw open-loop poles in the hard copy ***** 
```

Root-Locus Plot of G(s) = K/[(s(s+1)(s+2)] and Asymptotes   
![](image/547d10fbaf81ce389278df969d59097cd3a90b7ee82a5a471a31febb76058e1b.jpg)

<details>
<summary>line</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -2 | 0 |
| -1 | 0 |
| 0 | 0 |
| 1 | -4 |
| 1.5 | -3 |
| 2 | -2 |
| 2.5 | -1 |
| 3 | 0 |
| 3.5 | 1 |
| 4 | 2 |
| 4.5 | 3 |
| 5 | 4 |
</details>

Figure 6–70 Root-locus plot.

Drawing two or more plots in one diagram can also be accomplished by using the hold command. MATLAB Program 6–16 uses the hold command. The resulting root-locus plot is shown in Figure 6–71.
