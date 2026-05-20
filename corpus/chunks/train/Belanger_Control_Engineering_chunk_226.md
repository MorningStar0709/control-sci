We now wish to enlarge the allowable class of plants to include those with j-axis poles and/or zeros. Let $p(s)$ be a polynomial whose roots are the j-axis poles of $P(s)$ ; i.e.,

$$P (s) = \frac {P ^ {\prime} (s)}{p (s)}$$

where $P'(s)$ has no j-axis poles. We restrict $W(s)$ to the form

$$W (s) = \frac {W ^ {\prime} (s)}{p (s)}$$

where W is a proper or strictly proper transfer function, and $W'$ has all its poles and zeros in the open LHP. Since S must be zero at the unstable poles of P, including the roots of $p(s)$ , we write

$$S = p S ^ {\prime}.$$

Clearly, $W S = W'S'$ , so that minimization of the $\infty$ norms of $W S$ and $W'S'$ is the same problem. The solution, as before, is

$$W ^ {\prime} S ^ {\prime} = k B _ {p} (s) B ^ {\prime} (s).$$

The interpolation conditions come from the fact that, at all $z_{i}$ such that $P(z_{i}) = 0$ ,

$$S (z _ {i}) = p (z _ {i}) S ^ {\prime} (z _ {i}) = 1$$

so that

$$W ^ {\prime} (z _ {i}) S ^ {\prime} (z _ {i}) = \frac {W ^ {\prime} (z _ {i})}{p (z _ {i})} = W (z _ {i}) = k B _ {p} (z _ {i}) B ^ {\prime} (z _ {i})$$

which is precisely Equation 4.59.

We illustrate with an example.

Example 4.10 The cart-and-inverted-pendulum system of Example 3.18 (Chapter 3) has the linearized transfer function

$$\frac {x}{F} = \frac {(s + 3 . 1 3) (s - 3 . 1 3)}{s ^ {2} (s - 4 . 4 3) (s + 4 . 4 3)}.$$

Find the compensator that solves the $H^{\infty}$ problem, with $W(s) = (s + 1)^2 / s^2$ . (Note that $W$ , like $P$ , has a double pole at $s = 0$ .)

Solution To satisfy the interpolation conditions at s = 4.43, we use

$$B _ {p} (s) = \frac {- s + 4 . 4 3}{s + 4 . 4 3}.$$

Because $M = 1$ (one RHP zero), $B'(s) = 1$ and

$$
\begin{array}{l} k = \frac {W (3 . 1 3)}{B _ {p} (3 . 1 3)} \\ = \frac {(4 . 1 3) ^ {2}}{(3 . 1 3) ^ {2}} \cdot \frac {(7 . 5 6)}{(1 . 3 0)} = 1 0. 1 2. \\ \end{array}
$$

Thus,

$$S (s) = 1 0. 1 2 \cdot \frac {- s + 4 . 4 3}{s + 4 . 4 3} \cdot \frac {s ^ {2}}{(s + 1) ^ {2}}.$$

To summarize the $H^{\infty}$ procedure:

1. Choose a minimum-phase weighting function $W(s)$ (i.e., no zeros in the closed RHP). $W(s)$ must have poles at the j-axis poles of $P(s)$ , if any, and may not have j-axis poles at zeros of $P(s)$ . It may have other j-axis poles.

2. From the poles of $P$ in the open RHP, form the Blaschke product $B_{p}(s)$ , if has no open RHP poles, $B_{p}(s) = 1$ .   
3. Form the Blaschke product $B'(s)$ , having $M - 1$ poles (and zeros), where $M$ is the number of zeros of $P$ in the closed RHP. If $M$ is a set of zeros,   
4. Use the interpolation condition of Equation 4.59 to write $M$ equations for $k$ and the poles of $B'$ . Solve to obtain $k$ and $B'(s)$ .   
5. Write $S(s)$ as in Equation 4.61.
