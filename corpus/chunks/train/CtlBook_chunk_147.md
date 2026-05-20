# 5.4.5 Combining Magnitude Plots

Consider the more realistic transfer function which has one zero and two poles:

$$G _ {3} (s) = \frac {(s + b)}{(s + a) (s + c)}$$

We will dene the features of the transfer function to be the poles and zeros. In $G _ { 3 }$ for example,

$$\frac {1}{(s + a)} \qquad (s + b) \qquad \frac {1}{(s + c)}$$

which we may just call $a , b , c$ for short, are all features of $G _ { 3 } ( s )$ .

To make a Bode Asymptotic Magnitude plot of this more interesting function, we recognize that it is the product of two poles and one zero:

$$G _ {d} (s) = \frac {1}{(s + b)} \frac {(s + a)}{1} \frac {1}{(s + c)}$$

and since we are plotting in a dB scale that

$$d B (| G _ {3} (s) |) = d B (\left| \frac {1}{(s + b)} \right|) + d B (\left| \frac {(s + a)}{1} \right|) + d B (\left| \frac {1}{(s + c)} \right|)$$

In other words, we can just add the three Bode plots together. This is a valid way to do it but is still time consuming because four total plots have to be made. To nd a simpler way, let's constrain the rst asympotic frequency range slightly so that it is below the lowest feature, i.e.

$$\omega < < \min (a, b, c)$$

For this case

$$| G _ {3} (\omega) | = d B (a) - d B (b) - d B (c)$$

at this point we know where the low frequency (horizontal) asymptote intersects the dB axis. Assume that in $G _ { 3 } ( s )$ the smallest feature is a. An important way to look at the basic plots of Figures 5.4 and 5.5 is that they are horizontal for $\omega <$ the lowest feature, and sloped (either down for poles or up for zeros) for ω > the lowest feature. Thus, the quickest way to draw the Bode Asymptotic Magnitude plot is to start from the horizontal asymptote and then, as log frequency increases, to add in a component of slope as ω gets to each pole or zero.
