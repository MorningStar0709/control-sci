<table><tr><td>MATLAB Program 8-13</td></tr><tr><td>% ***** Unit-Ramp Response *****</td></tr><tr><td>num = [0 0 6.104 40.6104 4];den = [1 6.104 41.6104 4 0];t = 0:0.01:20;c = step(num,den,t);plot(t,c,&#x27;-.&#x27;,t,t,&#x27;-&#x27;)title(&#x27;Unit-Ramp Response&#x27;)xlabel(&#x27;t(sec)&#x27;)ylabel(&#x27;Input Ramp Function and Output&#x27;)text(3,11.5,&#x27;Input Ramp Function&#x27;)text(13.8,11.2,&#x27;Output&#x27;)</td></tr></table>

Nyquist Plot. Earlier we found that the three closed-loop poles of the designed system are all in the left-half s plane. Hence the designed system is stable. The purpose of plotting Nyquist diagram here is not to test the stability of the system, but to enhance our understanding of Nyquist stability analysis. For a complicated system, Nyquist plot will look complicated enough that it is not easy to count the number of encirclements of the −1+j0 point.

Figure 8–57

(a) Modified Nyquist path in the s plane; (b) Nyquist path in the $s _ { 1 }$ plane.

![](image/8f377cae36b11a6e474f46944488eb0e8ef1b94f838bdedcaf652fbeff9c1c3e.jpg)

<details>
<summary>text_image</summary>

jω
s plane
σ
0
σ₀
</details>

(a)

![](image/b2d419638d5826445f3fe87009ecd6bc15a5df022909cb078c04a3cf78ddf549.jpg)

<details>
<summary>text_image</summary>

jω
s₁ plane
X
0
σ
X
</details>

(b)

Because the designed system involves three open-loop poles on the $j w$ axis, the Nyquist diagram will look quite complicated as we will see in what follows:

Define the open-loop transfer function of the designed system as $G ( s )$ . Then

$$G (s) = G _ {c} (s) \frac {s + 0 . 1}{s ^ {2} + 1} = \frac {6 . 1 0 4 s ^ {2} + 4 0 . 6 1 0 4 s + 4}{s \left(s ^ {2} + 1\right)}$$

Let us choose a modified Nyquist path in the s plane as shown in Figure 8–57(a). The modified path encloses three open-loop poles $( s = 0 , s = j 1 , s = - j 1 )$ . Now define $s _ { 1 } = s + \sigma _ { 0 }$ . Then, the Nyquist path in the $s _ { 1 }$ plane becomes as shown in Figure 8–57(b). In the $s _ { 1 }$ plane, the openloop transfer function has three poles in the right-half $s _ { 1 }$ plane.

Let us choose $\sigma _ { 0 } = 0 . 0 1$ Since. $s = s _ { 1 } - \sigma _ { 0 }$ we have,

$$G (s) = G \left(s _ {1} - 0. 0 1\right)$$

Open-loop transfer function in the $s _ { 1 }$ plane

$$
\begin{array}{l} = \frac {6 . 1 0 4 \left(s _ {1} ^ {2} - 0 . 0 2 s _ {1} + 0 . 0 0 0 1\right) + 4 0 . 6 1 0 4 \left(s _ {1} - 0 . 0 1\right) + 4}{\left(s _ {1} - 0 . 0 1\right) \left(s _ {1} ^ {2} - 0 . 0 2 s _ {1} + 1 . 0 0 0 1\right)} \\ = \frac {6 . 1 0 4 s _ {1} ^ {2} + 4 0 . 4 8 8 3 2 s _ {1} + 3 . 5 9 4 5 0 6 4}{s _ {1} ^ {3} - 0 . 0 3 s _ {1} ^ {2} + 1 . 0 0 0 3 s _ {1} - 0 . 0 1 0 0 0 1} \\ \end{array}
$$

A MATLAB program to obtain the Nyquist plot is shown in MATLAB Program 8–14. The resulting Nyquist plot is shown in Figure 8–58.
