$$\mathbf {H} = \sum \mathbf {r} d m \times \mathbf {V} _ {c m} + \sum [ \mathbf {r} \times (\boldsymbol {\omega} \times \mathbf {r}) ] d m. \tag {2.37a}$$

As stated above, the first term on the right-hand side of (2.37a) is zero. Therefore, we have simply

$$\delta \mathbf {H} = \sum [ \mathbf {r} \times (\boldsymbol {\omega} \times \mathbf {r}) ] d m \tag {2.37b}$$

and

$$\mathbf {H} = \int \mathbf {r} \times (\boldsymbol {\omega} \times \mathbf {r}) d m. \tag {2.37c}$$

Performing the vector operations in (2.37c) and noting that

$$\boldsymbol {\omega} = \omega_ {x} \mathbf {i} + \omega_ {y} \mathbf {j} + \omega_ {z} \mathbf {k} = P \mathbf {i} + Q \mathbf {j} + R \mathbf {k},\mathbf {r} = x \mathbf {i} + y \mathbf {j} + z \mathbf {k},$$

we have

$$
\begin{array}{l} \boldsymbol {\omega} \times \mathbf {r} = \left[ \begin{array}{c c c} \mathbf {i} & \mathbf {j} & \mathbf {k} \\ P & Q & R \\ x & y & z \end{array} \right] \\ = (z Q - y R) \mathbf {i} + (x R - z P) \mathbf {j} + (y P - x Q) \mathbf {k}. \tag {2.38a} \\ \end{array}
$$

Finally,

$$
\begin{array}{l} \mathbf {r} \times (\boldsymbol {\omega} \times \mathbf {r}) = \left[ \begin{array}{c c c} \mathbf {i} & \mathbf {j} & \mathbf {k} \\ x & y & z \\ (z Q - y R) & (x R - z P) & (y P - x Q) \end{array} \right] \\ = \mathbf {i} [ (y ^ {2} + z ^ {2}) P - x y Q - x z R ] + \mathbf {j} [ (z ^ {2} + x ^ {2}) Q - y z R - x y P ] \\ + \mathbf {k} [ (x ^ {2} + y ^ {2}) R - x z P - y z Q ]. \tag {2.38b} \\ \end{array}
$$

Substituting (2.38b) into (2.37c), we have

$$
\begin{array}{l} \mathbf {H} = \int \mathbf {i} [ (y ^ {2} + z ^ {2}) P - x y Q - x z R ] d m + \int \mathbf {j} [ (z ^ {2} + x ^ {2}) Q - y z R - x y P ] d m \\ + \int \mathbf {k} [ (x ^ {2} + y ^ {2}) R - x z P - y z Q ] d m, \tag {2.38c} \\ \end{array}
$$

where the $\textstyle { \int { ( y ^ { 2 } + z ^ { 2 } ) } }$ is defined as the moment of inertia, $I _ { x }$ , and  xydm is defined as the product of inertia, $I _ { x y }$ . The remaining integrals in (2.38c) are similarly defined. By proper positioning of the body axis system, one can make the products of inertia $I _ { x y } = I _ { y z }$ equal to 0. This will be true if we can assume that the x-y plane is a plane of symmetry of the missile. Consequently, (2.38c) can be rewritten in component form as follows:

$$H _ {x} = P \int (y ^ {2} + z ^ {2}) d m - R \int x z d m = P I _ {x} - R I _ {x z}, \tag {2.39a}H _ {y} = Q \int (x ^ {2} + z ^ {2}) d m = Q I _ {y}, \tag {2.39b}H _ {z} = R \int (x ^ {2} + y ^ {2}) d m - P \int x z d m = R I _ {z} - P I _ {x z}. \tag {2.39c}$$
