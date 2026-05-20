# 4.2 Introduction

In modern control theory, the system is represented as a rst order linear dierential equation in a high dimensional space known as state space. Each point in state space represents a unique dynamical state of the system. For example, a system with one mass could be described by a 2-dimensional state space consisting of the position, x and the velocity, x˙ (Figure 4.1). x and x˙ are the variables in the equations of motion for the mass (we consider x¨ separately).

The way to dene the dimensionality of a system's state space is to identify all system variables which describe an energy. Each one is a dimension of state space. In our single mass example, energy is stored in the spring and mass:

$$E _ {K} = \frac {1}{2} (K _ {1} + K _ {2}) x ^ {2} \qquad E _ {M} = \frac {1}{2} M \dot {x} ^ {2}$$

![](image/b80924472254d2c551745ee62cfaf03e4c144db01d45986962b572e4272ed1e7.jpg)

<details>
<summary>text_image</summary>

K₁
K₂
f(ε)
M
X(ε)
</details>

![](image/5c11dc0c290763fc2b5b6b63621db7f3d21ea35bf200a635e86753eb09401012.jpg)

<details>
<summary>text_image</summary>

Current System
State
X = [x̂]
x
</details>

Figure 4.1: Translational dynamic system for state space example.

So for this system we would use x and x˙ as state variables. We use a vector, X, to dene a point in state space such as:

$$
X = \left[ \begin{array}{c} x \\ \dot {x} \end{array} \right]
$$

Then the dynamics of the system are represented in a matrix rst order LODE:

$$\dot {X} = A X + B U$$

Where X is the state vector, X˙ is the rst derivative of the state vector,

$$
\dot {X} = \left[ \begin{array}{c} \dot {x} \\ \ddot {x} \end{array} \right]
$$

A is a matrix of constant coecients, U is the system input (like an applied force, f (t)), and B is another matrix. This form can represent systems with multiple inputs (the elements of U ), but here we will restrict ourselves to a single input (see below).

Sometimes the output of the system, Y , is not one of the state variables, but instead a linear combination of the state variables and possibly the input. For example, this could occur in a blood pressure controller where states could be blood volume, cardiac output, and vascular resistance, but output, blood pressure, is a linear combination of those states. In this case there is another equation

$$Y = C X + D U$$

where C, D are additional matrices of constant coecients. There is no Laplace transform and the equations come directly from the equations of motion. In many realistic systems, many elements of these matrices are zero.

In this course, we focus on systems with a single input and single output (known as a SISO system) and thus u and y are scalars and the matrices B, C, D are not square.
