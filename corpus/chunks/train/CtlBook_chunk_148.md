# 5.4.6 Cartoon Bode Magnitude Plot

It is useful at this stage to make a cartoonish version of the Bode Magnitude plot using only our knowledge of the order of the features (from low to high frequency). This can be done in seconds. Suppose

$$G _ {4} (s) = \frac {(s + 1)}{(s + 5 0) (s + 1 0 0 0)}$$

in frequency order we have:

1. A zero at s = 1   
2. A pole at s = 50   
3. A pole at s = 1000

Without worrying about precise locations in the log-log plane, we can immediately draw:

![](image/e990ccd5fc81cad7ff0d15fa036ed4ba590b512386b3ebb5d9b26c2e0982c542.jpg)

<details>
<summary>text_image</summary>

Pole1
Pole 2
+1 slope
+1-1-1
= -1 slope
Zero
+1-1 = 0
slope
</details>

This works because we are always adding the basic pole zero responses together (multiplication in a log axis) which have either +1 or -1 slope after their pole/zero frequency but not before. This gives us the basic idea of how the graph will look.

The quick cartoon Bode plot is useful for example, to determine what range of dBs to use on our y axis and what frequencies to use on our x axis.
