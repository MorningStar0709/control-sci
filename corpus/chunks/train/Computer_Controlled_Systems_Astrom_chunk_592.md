9.15 Three different algorithms for a PI-controller are listed. Use the linear model for roundoff to analyze the sensitivity of the algorithms to quantization in A-D and D-A converters and roundoff in the multiplications. Assume fixed-point calculations. Also, discuss the word lengths necessary for the algorithms.

Algorithm 1:

```txt
e:=uc-y
u:=k*(e+h*i/ti)
i:=i+e*h 
```

Algorithm 2:

```txt
e:=uc-y
u:=k*(e+i)
i:=i+e*h/ti 
```

Algorithm 3:

```txt
e:=uc-y
u:=i+k*e
i:=i+k*h*e/ti 
```

9.16 Consider a dynamic system with the pulse-transfer function

$$H (z) = \frac {b _ {0} z ^ {n} + b _ {1} z ^ {n - 1} + \cdots + b _ {n}}{z ^ {n} + a _ {1} z ^ {n - 1} + \cdots a _ {n}}$$

There are many ways to introduce the states in a state-space representation. Show that the system has the following state descriptions:

(a)

$$
x (k + 1) = \left( \begin{array}{c c c c c} {- a _ {1}} & {1} & {0} & {\dots} & {0} \\ {- a _ {2}} & {0} & {1} & {\dots} & {0} \\ {\vdots} & {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {- a _ {n - 1}} & {0} & {0} & {\dots} & {1} \\ {- a _ {n}} & {0} & {0} & {\dots} & {0} \end{array} \right) x (k) + \left( \begin{array}{c} {b _ {1} - b _ {0} a _ {1}} \\ {b _ {2} - b _ {0} a _ {2}} \\ {\vdots} \\ {b _ {n - 1} - b _ {0} a _ {n - 1}} \\ {b _ {n} - b _ {0} a _ {n}} \end{array} \right) u (k)

y (k) = \left( \begin{array}{c c c c c} 1 & 0 & 0 & \dots & 0 \end{array} \right) x (k) + b _ {0} u (k)
$$

(b)

$$
x (k + 1) = \left( \begin{array}{c c c c c} {- a _ {1}} & {1} & {0} & {\dots} & {0} \\ {- a _ {2}} & {0} & {1} & {\dots} & {0} \\ {\vdots} & {\vdots} & {\vdots} & {\ddots} & {\vdots} \\ {- a _ {n}} & {0} & {0} & {\dots} & {1} \\ {0} & {0} & {0} & {\dots} & {0} \end{array} \right) x (k) + \left( \begin{array}{c} {b _ {0}} \\ {b _ {1}} \\ {\vdots} \\ {b _ {n - 1}} \\ {b _ {n}} \end{array} \right) u (k + 1)

y (k) = \left( \begin{array}{c c c c c} 1 & 0 & 0 & \dots & 0 \end{array} \right) x (k)
$$

(c)

$$
x (k + 1) = \left( \begin{array}{c c c c c c c c c c} - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} & - a _ {n} & b _ {1} & b _ {2} & \dots & b _ {n - 1} & b _ {n} \\ 1 & 0 & \dots & 0 & 0 & 0 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 & 0 & 0 & \dots & 0 & 0 \\ 0 & 0 & \dots & 0 & 0 & 0 & 0 & \dots & 0 & 0 \\ 0 & 0 & \dots & 0 & 0 & 1 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 0 & 0 & 0 & 0 & \dots & 1 & 0 \end{array} \right) x (k)

+ \left( \begin{array}{c} b _ {0} \\ 0 \\ \vdots \\ 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{array} \right) u (k + 1)
