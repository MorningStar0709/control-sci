# DEFINITION

A state $x^{*} \neq 0$ is said to be unobservable if the zero-input solution $\mathbf{y}(t)$ , with $\mathbf{x}(0) = \mathbf{x}^{*}$ , is zero for all $t \geq 0$ .

Mathematically, $x^{*}$ is an unobservable state if $Ce^{At}x^{*}=0$ for all $t\geq0$ . For the sprung bar of Example 3.4, with a sensor measuring the height of the center of gravity referred to equilibrium, any state of the form

$$
\mathbf {x} ^ {*} = \left[ \begin{array}{l} 0 \\ 0 \\ \alpha \\ \beta \end{array} \right]
$$

with $\alpha$ and $\beta$ constants is unobservable. Such a state excites only pitch motion and causes no motion of the center of gravity. It can be formally verified that $Ce^{At}\mathbf{x}^* = \mathbf{0}$ for $C = \left[1\quad 0\quad 0\quad 0\right]$ , corresponding to a height sensor.

For a system with one output, the equation $y(t) = \mathbf{c}^{T}\mathbf{x}(t)$ expresses the geometric fact that $y(t)$ is the scalar product of the vectors c and $\mathbf{x}(t)$ . A state $x^{*}$ is unobservable if, for $\mathbf{x}(0) = \mathbf{x}^{*}$ , the zero-input solution $\mathbf{x}(t)$ is orthogonal to c for all t.

If, in the circuit of Example 3.2, $i_s = 0$ and the output is the voltage across the two top resistances of value $R$ , then $y = x_1 - x_2 = [1 - 1]\mathbf{x}$ . Figure 3.5 illustrates the vector $\mathbf{c} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ . The output for a state $\mathbf{x}(t)$ is the length (with a sign) of the projection of $\mathbf{x}(t)$ upon $\mathbf{c}$ , as shown. For any $\mathbf{x}(t)$ where $x_1(t) = x_2(t)$ , the output is zero.

In this particular case, if the initial state satisfies $x_{1}(0) = x_{2}(0)$ , it follows that $x_{1}(t) = x_{2}(t)$ —if the two voltages are initially equal, they remain so for all t > 0.

![](image/06c2647f32c66778169eb5cd4179067d5b301dc0dbe37416526757737c74fc6f.jpg)

<details>
<summary>text_image</summary>

x₂, c₂
X(t), x₁ = x₂
X(t)
1
x₁, c₁
-1
c
</details>

Figure 3.5 Illustration of observability for the circuit of Example 3.2

Therefore, the state space trajectory, or path, follows the line orthogonal to $\mathbf{c}$ , right to the origin, and $y(t)$ is always zero.

In the case of several outputs, the geometric interpretation is that it is possible to find an initial state such that $\mathbf{x}(t)$ is orthogonal to all rows of C, for all t > 0.

To establish the relationship between system observability and the existence of unobservable states, we shall need these results from the theory of quadratic forms:

- A real, symmetric matrix $M$ is positive definite if $\mathbf{x}^T M\mathbf{x} > 0$ for every $\mathbf{x} \neq \mathbf{0}$ .   
- A positive definite matrix is always nonsingular; i.e., $M^{-1}$ exists.

We now present our theorem.
