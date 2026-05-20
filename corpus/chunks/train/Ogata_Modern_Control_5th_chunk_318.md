Finding the Gain Value K at an Arbitrary Point on the Root Loci. In MAT-LAB analysis of closed-loop systems, it is frequently desired to find the gain value K at an arbitrary point on the root locus. This can be accomplished by using the following rlocfind command:

$$[ K, r ] = r l o c f i n d (n u m, d e n)$$

The rlocfind command, which must follow an rlocus command, overlays movable x-y coordinates on the screen. Using the mouse, we position the origin of the x-y coordinates over the desired point on the root locus and press the mouse button. Then MATLAB displays on the screen the coordinates of that point, the gain value at that point, and the closed-loop poles corresponding to this gain value.

If the selected point is not on the root locus, such as point A in Figure 6–29(a), the rlocfind command gives the coordinates of this selected point, the gain value of this point, such as K = 2, and the locations of the closed-loop poles, such as points B and C corresponding to this K value. [Note that every point on the s plane has a gain value. See, for example, Figures 6–29 (a) and (b).]
