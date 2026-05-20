# Example 9.13 cont.

Now we consider the RL with $C _ { 2 } ( s ) .$ . First we sketch it without the performance regions for clarity.

![](image/83e4ef8585198bee7c25cf01f6fcfafbbfef3070d6017c0b2d87779e159acfd8.jpg)

<details>
<summary>text_image</summary>

-10
-2
-1
0
</details>

This root locus looks pretty close to what we had before. $C _ { 2 } ( s )$ contains a pole $( s = 0 )$ and zero $( s = - 0 . 1 )$ which are close together relative to the plant poles. Because of this they largely cancel their eects, but the system is still type 1(!). Adding the performance regions:

![](image/fd6c1712401a68d964b7899ded508a76b6256712276ce9c10e8918b7058ec727.jpg)

<details>
<summary>text_image</summary>

% 0S < 10%
-10
-2
-1
51°
σ ≤ -0.5
Ts ≤ 8sec
</details>

We can now hand-compute K:

1. We will aim for the highest possible K so we pick the point a little below where the RL crosses the diagonal %OS line: about $s \dot { = } - 1 . 2 + 1 . 2 j .$ .   
2. We know that all points on the RL satisfy the Magnitude Condition:

$$\left| K C P H \right| = 1$$

for our problem, K is included in $C _ { 2 } ( s )$ and $H ( s ) = 1$ so this is

$$| C _ {2} (s) | | P (s) | _ {(s = - 1. 2 + 1. 2 j)} = 1 \rightarrow \left| \frac {K (s + 0 . 1)}{s} \frac {1}{(s + 1) (s + 2) (s + 1 0)} \right| _ {(s = - 1. 2 + 1. 2 j)} = 1\frac {\mid - 1 . 2 + 1 . 2 j + 0 . 1 \mid}{\mid - 1 . 2 + 1 . 2 j \mid \mid - 0 . 2 + 1 . 2 j \mid \mid 0 . 8 + 1 . 2 j \mid \mid 8 . 8 + 1 . 2 j} = \frac {1}{K}$$

3. Solving for K (using python):

$$K = 1 6. 2 4$$
