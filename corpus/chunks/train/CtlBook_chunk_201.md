# Example 7.1

Use the computer to plot a Root Locus diagram for the system of Section 6.6.

$$G (s) = C P H (s) = \frac {K}{(s + 1) (s + 2) (s + 3)}$$

Using python by default enter the system with K = 1 (Listing 7.1).:

![](image/4762c67718cf700a400594261920caa89b08bd81df0523b18c5f1f935d7c9b1b.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -4 | 0 |
| -1 | 1.5 |
| -1 | -2 |
</details>

This plot shows rst the three open loop poles as ${ \mathrm { X } } { \mathrm { s } } ,$ all on the negative real axis. Lines show the path of the poles as $K  \infty .$ Notice that the angled lines cross the imaginary axis, at about ±3.5j, a result consistent with the computation of Section 6.6. The pole eventually follow straight line asymptotes, the curved lines (in two cases) are the actual paths. Note: Using ctl.root\_locus\_plot() the lines are clickable! As shown I have clicked one of the three black squares (near −1 + 1.6j), and the gain value is shown. Also shown is where the pole at -3 is for that gain.

```txt
s=ctl.TransferFunction.s
K =1
ccp = -1+3j
ccp2 = -1-3j
num = K*(s+4)*(s+5)
denom = ((s-ccp)*(s-ccp2))
sys = ctl.TransferFunction(num/denom)
figRL = plt.Figure()
ax = plt.gca()
plt.title('Root Locus Diagram: Example 7.2')
ctl.root_locus_plot(sys, ax=ax)
plt.grid()
plt.show() 
```

Listing 7.2. Draw Root Locus of system with poles and zeros
