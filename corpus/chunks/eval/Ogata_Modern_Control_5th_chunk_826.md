# Robust Stability. Let us define

$\widetilde { G }$ true plant dynamics=

G=model of plant dynamics

unstructured multiplicative uncertainty¢m =

We assume that $\Delta _ { m }$ is stable and its upper bound is known.We also assume that $\widetilde { G }$ and G are related by

$$\widetilde {G} = G (I + \Delta_ {m})$$

Consider the system shown in Figure 10–43(a). Let us examine the transfer function between point A and point B. Notice that Figure 10–43(a) can be redrawn as shown in Figure 10-43(b).The transfer function between point A and point B can be given by

$$\frac {K G}{1 + K G} = (1 + K G) ^ {- 1} K G$$

Define

$$(1 + K G) ^ {- 1} K G = T \tag {10-121}$$

Using Equation (10–121) we can redraw Figure 10–43(b) as Figure 10–43(c).Applying the smallgain theorem to the system consisting of $\Delta _ { m }$ and T as shown in Figure 10–43(c), we obtain the condition for stability to be

$$\left\| \Delta_ {m} T \right\| _ {\infty} < 1 \tag {10-122}$$

In general, it is impossible to precisely model $\Delta _ { m }$ Therefore, let us use a scalar transfer function. $W _ { m } ( j \omega )$ such that

$$\overline {{\sigma}} \{\Delta_ {m} (j \omega) \} < | W _ {m} (j \omega) |$$

where $\overline { { \sigma } } \{ \Delta _ { m } ( j \omega ) \}$ is the largest singular value of $\Delta _ { m } ( j \omega )$ .

Consider, instead of Inequality (10–122), the following inequality:

$$\left\| W _ {m} T \right\| _ {\infty} < 1 \tag {10-123}$$

If Inequality (10–123) holds true, Inequality (10–122) will always be satisfied. By making the $H _ { \infty }$ norm of $W _ { m } T$ to be less than 1, we obtain the controller K that will make the system stable.

Suppose that we cut the line at point A in Figure 10–43(a). Then we obtain Figure 10–43(d). Replacing $\Delta _ { m }$ by $W _ { m } I$ , we obtain Figure 10–43(e). Redrawing Figure 10–43(e), we obtain Figure 10–43(f). Figure 10–43(f) is called a generalized plant diagram.

Referring to Equation (10–121), T is given by

$$T = \frac {K G}{1 + K G} \tag {10-124}$$

Then Inequality (10–123) can be rewritten as

$$\left\| \frac {W _ {m} K (s) G (s)}{1 + K (s) G (s)} \right\| _ {\infty} < 1 \tag {10-125}$$
