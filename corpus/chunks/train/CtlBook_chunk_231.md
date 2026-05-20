# 3.) The State Space method

The basic state space model from Chapter 4 is

$$
\dot {X} = A X + B U
\dot {X} = \left[ \begin{array}{c} \dot {x} \\ \ddot {x} \end{array} \right] \quad x = \left[ \begin{array}{c} x \\ \dot {x} \end{array} \right]
Y = C X + D U
$$

The matrices A, B determine how the state evolves from inputs U, and the matrices C, D determine how outputs are generated (if they are not already given by the state variables which can sometimes happen).

Let's say we have a 2 dimensional state vector $\dot { X _ { \mathrm { ~ } } } = [ x , \dot { x } ] ^ { T }$ and a single input, $f ( t ) / M .$ . The way this needs to be set up for state space is

$$
\dot {X} = A X + [ 0, 1 / M ] \left[ \begin{array}{c} 0 \\ f (t) \end{array} \right]
$$

or in more detail

$$
\left[ \begin{array}{c} \dot {x} \\ \ddot {x} \end{array} \right] = A \left[ \begin{array}{c} x \\ \dot {x} \end{array} \right] + [ 0, 1 ] \left[ \begin{array}{c} 0 \\ u \end{array} \right]
$$

other words, our input matrix

$$B = [ 0, 1 / M ]$$

which is a row vector or a 1x2 matrix.

python.control relies on numpy for matrix algebra but that is slightly nicky when it comes to 1 dimensional matrices, i.e. vectors. Thinking mathematically we could write

$$x = a ^ {T}$$

where

$$
a = [ 1, 2, 3 ], x = \left[ \begin{array}{l} 1 \\ 2 \\ 3 \end{array} \right]
$$

and be ne with it. Numpy needs vectors to be two-dimensional so that it can tell the dierence between row vectors and column vectors.

Here are some quick helper functions to always initialize vectors with your row/column intention:

```python
def RowVector(x):  # vectors in numpy have to be 2-dimensional(!)
    x = np.array(x)
    return np.atleast_2d(x)

def ColVector(x):
    return RowVector(x).T 
```

Also, for convenience, let's repeat the hints from Section 4.2 on dimensioning our matrices and vectors:
