# Example 8.5

Calculate the final value $f ( \infty )$ (if it exists) and initial value f (0+) from the given Laplace transforms $F ( s )$

(a)

$$F (s) = \frac {7 (s + 3)}{s ^ {2} + 2 s + 1 0}$$

First, we check the poles of the $F ( s )$ to determine if we can use the final-value theorem. The poles of $F ( s )$ are the roots of its denominator polynomial $s ^ { 2 } + 2 s + 1 0 = 0$ , which yields the two complex poles $s = - 1 \pm j 3$ . Because the complex poles lie in the left half of the complex plane (i.e., the real part of the two poles is negative), we can use the final-value theorem Eq. (8.10)

$$f (\infty) = \lim _ {s \rightarrow 0} s F (s) = \lim _ {s \rightarrow 0} \frac {7 s (s + 3)}{s ^ {2} + 2 s + 1 0} = \frac {(0) (3)}{1 0} = 0$$

Hence, the steady-state value of $f ( t )$ is zero.

We find the initial value by using Eq. (8.11)

$$f (0 +) = \lim _ {s \rightarrow \infty} s F (s) = \lim _ {s \rightarrow \infty} \frac {7 s (s + 3)}{s ^ {2} + 2 s + 1 0} = \lim _ {s \rightarrow \infty} \frac {7 s ^ {2}}{s ^ {2}} = 7$$

Hence, the initial value of $f ( 0 + )$ is 7.

(b)

$$F (s) = \frac {3 (s ^ {2} + 2)}{s (s + 4) (s ^ {2} + 4 s + 5)}$$

First, we check the poles of the $F ( s )$ to determine if we can use the final-value theorem. The four poles are $s = 0 ,$ , $s = - 4 .$ , and $s = - 2 \pm j .$ . Because we have one pole at the origin and three poles strictly in the left-half plane, we can use the final-value theorem:

$$f (\infty) = \lim _ {s \rightarrow 0} s F (s) = \lim _ {s \rightarrow 0} \frac {3 s \left(s ^ {2} + 2\right)}{s (s + 4) \left(s ^ {2} + 4 s + 5\right)} = \frac {(3) (2)}{(4) (5)} = 0. 3$$

The initial value is

$$f (0 +) = \lim _ {s \rightarrow \infty} s F (s) = \lim _ {s \rightarrow \infty} \frac {3 s \left(s ^ {2} + 2\right)}{s (s + 4) \left(s ^ {2} + 4 s + 5\right)} = \lim _ {s \rightarrow \infty} \frac {3 s ^ {3}}{s ^ {4}} = 0$$

(c)

$$F (s) = \frac {3 (s ^ {3} + 2 s ^ {2} + 6 s + 1 2)}{s (s + 4) (s ^ {2} + 2 5)}$$

The four poles of $F ( s )$ are $s = 0 , s = - 4 .$ , and $s = \pm j 5$ . Because the Laplace transform has two poles on the imaginary axis at $s = \pm j 5$ , the time function f (t) will include the harmonic functions (sin 5t and cos 5t) and hence there is no final value $f ( \infty )$ .

The initial value is

$$f (0 +) = \lim _ {s \to \infty} s F (s) = \lim _ {s \to \infty} \frac {3 s (s ^ {3} + 2 s ^ {2} + 6 s + 1 2)}{s (s + 4) (s ^ {2} + 2 5)} = \lim _ {s \to \infty} \frac {3 s ^ {4}}{s ^ {4}} = 3$$
