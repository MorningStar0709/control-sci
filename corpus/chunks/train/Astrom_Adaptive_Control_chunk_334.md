$$S _ {2} = - \left(I - \frac {1}{2} (I - H _ {2})\right) ^ {- 1} \frac {1}{2} (I - H _ {2}) = (H _ {2} + I) ^ {- 1} (H _ {2} - I)$$

The system obtained after the transformations is shown in Fig. 5.17(d).

The systems in Fig. 5.17(a) and Fig. 5.17(d) are equivalent. We use their equivalence to prove the result. First we observe that if the system $(H + I)^{-1}$ exists, it commutes with H. To prove this, use the identity

$$H + H ^ {2} = H (H + I) = (H + I) H$$

and multiply from the left and the right by $(I + H)^{-1}$ ; then

$$(H + I) ^ {1} H = H (H + I) ^ {- 1}$$

Subtracting $(H + I)^{-1}$ from both sides gives

$$(H + I) ^ {- 1} (H - I) = (H - I) (H + I) ^ {- 1}$$

The systems S and H are related through

$$S = (H - I) (H + I) ^ {- 1} = (H + I) ^ {- 1} (H - I)$$

The input-output relation for the system S is

$$y = S u = (H - I) (H + I) ^ {- 1} u$$

Introduce

$$x = (H + I) ^ {- 1} u$$

We find that

$$\mathbf {y} = (H - I) \mathbf {x}u = (H + I) x$$

Hence

$$\left\| y \right\| ^ {2} = \langle y | y \rangle = \langle H x - x | H x - x \rangle = \langle H x | H x \rangle + \langle x | x \rangle - 2 \langle H x | x \rangle$$

Similarly, we find that

$$\left\| u \right\| ^ {2} = \langle u | u \rangle = \langle H x + x | H x + x \rangle = \langle H x | H x \rangle + \langle x | x \rangle + 2 \langle H x | x \rangle$$

Hence

$$\| y \| ^ {2} = \| u \| ^ {2} - 4 \langle H x | x \rangle \tag {5.56}$$

If $H$ is passive, we have $\langle Hx|x\rangle \geq 0$ ; hence $\| y\| \leq \| u\|$ , which implies that $\gamma(S) \leq 1$ . Similarly, we find that $\gamma(S) < 1$ if $H$ is strictly output passive.

It follows from Eq. (5.56) that

$$\langle H x | x \rangle = \frac {\| u \| ^ {2} - \| y \| ^ {2}}{4} = \frac {\| u \| ^ {2} - \| S u \| ^ {2}}{4} \geq (1 - \gamma (S)) \frac {\| u \| ^ {2}}{4}$$

This implies that $H$ is passive if $\gamma(S) \leq 1$ and strictly output passive if $\gamma(S) < 1$ .

Notice that the argument would be the same if S and H were complex numbers. The result is an example of the equivalence between complex numbers and operators on inner product spaces.
