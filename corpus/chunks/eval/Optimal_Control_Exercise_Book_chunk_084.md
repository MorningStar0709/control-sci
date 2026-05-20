# Solution:

We want to keep the pendulum in the upright position as much as possible. Therefore, we can choose the values of Q and R as following:

• Matrix Q: the values on the diagonal of the Q matrix act as ”penalties” for the corresponding state variable i.e. we want the θ, ˙θ as small as possible hence they have a greater penalty. As such, the designed matrix is:

$$
Q = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 0 0 & 0 \\ 0 & 0 & 0 & 1 0 0 \end{array} \right] \tag {387}
$$

where the greater values correspond to the penalties for θ and ˙θ

• Matrix R: in this case we just have a uni-dimensional matrix. The larger the R value, the larger the penalty on the input u(t) and therefore the system will use less energy. We set

$$R = [ 0. 1 ] \tag {388}$$

The Python code for setting the matrices is as following:

```python
