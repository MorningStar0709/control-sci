# Example 7.2

Determine the complete solution $y ( t )$ of the following second-order linear differential equation

$$2 \ddot {y} + 8 \dot {y} + 6 y = 1 0 \sin 4 t \tag {7.9}$$

with initial conditions $y ( 0 ) = 2$ and $\dot { y } ( 0 ) = - 1$ .

First, we write the second-order characteristic equation for this differential equation

$$2 r ^ {2} + 8 r + 6 = 0$$

This characteristic equation can be factored as $2 ( r ^ { 2 } + 4 r + 3 ) = 2 ( r + 1 ) ( r + 3 ) = 0$ , and therefore the two roots are $r _ { 1 } = - 1$ and $r _ { 2 } = - 3$ . Hence, the homogeneous solution has the form

$$y _ {H} (t) = c _ {1} e ^ {- t} + c _ {2} e ^ {- 3 t} \tag {7.10}$$

Because the particular solution must have the same form as the forcing function $f ( t ) = 1 0 \sin 4 t ,$ , we can select

$$y _ {P} (t) = a \sin 4 t + b \cos 4 t \tag {7.11}$$

The successive derivatives of the particular solution are $\dot { y } _ { P } = 4 a \cos 4 t - 4 b \sin 4 t$ and $\ddot { y } _ { P } = - 1 6 a \sin { 4 t } -$ 16b cos 4t. Substituting for $y _ { P } ( t )$ and its derivatives in the original differential equation (7.9) yields

$$2 (- 1 6 a \sin 4 t - 1 6 b \cos 4 t) + 8 (4 a \cos 4 t - 4 b \sin 4 t) + 6 (a \sin 4 t + b \cos 4 t) = 1 0 \sin 4 t$$

After equating the cos 4t and sin 4t terms from both sides of the equal sign, we obtain

$$\cos 4 t \text { terms: } - 3 2 b + 3 2 a + 6 b = 0\sin 4 t \text { terms: } - 3 2 a - 3 2 b + 6 a = 1 0$$

Solving these two equations for the two unknowns yields $a = - 0 . 1 5 2 9 , b = - 0 . 1 8 8 2$ . The complete solution is the sum of the homogeneous solution Eq. (7.10) and the particular solution Eq. (7.11)

$$y (t) = c _ {1} e ^ {- t} + c _ {2} e ^ {- 3 t} - 0. 1 5 2 9 \sin 4 t - 0. 1 8 8 2 \cos 4 t \tag {7.12}$$

Applying the first initial condition y(0) = 2 to Eq. (7.12) yields

$$y (0) = c _ {1} e ^ {0} + c _ {2} e ^ {0} - 0. 1 8 8 2 = 2 \tag {7.13}$$

The first time derivative of Eq. (7.12) is

$$\dot {y} (t) = - c _ {1} e ^ {- t} - 3 c _ {2} e ^ {- 3 t} - 0. 6 1 1 8 \cos 4 t + 0. 7 5 2 9 \sin 4 t \tag {7.14}$$

Applying the second initial condition ẏ (0) = −1 to Eq. (7.14) yields

$$\dot {y} (0) = - c _ {1} e ^ {0} - 3 c _ {2} e ^ {0} - 0. 6 1 1 8 = - 1 \tag {7.15}$$

We obtain the unknown coefficients from the simultaneous solution of Eqs. (7.13) and (7.15), and the result is $c _ { 1 } = 3 . 0 8 8 2$ and $c _ { 2 } = - 0 . 9 0 0 0$ . Finally, the complete solution is determined from Eq. (7.12)

$$y (t) = 3. 0 8 8 2 e ^ {- t} - 0. 9 0 0 0 e ^ {- 3 t} - 0. 1 5 2 9 \sin 4 t - 0. 1 8 8 2 \cos 4 t$$

As a final check, we see that the initial conditions

$$
\begin{array}{l} y (0) = 3. 0 8 8 2 - 0. 9 - 0. 1 8 8 2 = 2 \\ \dot {y} (0) = - 3. 0 8 8 2 - (- 3) (0. 9) - (4) (0. 1 5 2 9) = - 1 \\ \end{array}
$$

are satisfied as expected.
