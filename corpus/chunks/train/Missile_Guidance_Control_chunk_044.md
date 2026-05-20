# 2.1.3 Tensors

Tensor is a general name given to quantities that transform in prescribed ways when the coordinate system is rotated. A scalar is a tensor of rank 0, for it is independent of the coordinate system. A vector is a tensor of rank 1. Its components transform as do the coordinates of a point. A tensor of rank 2 has components that transform as do the quantities $C _ { i j }$ . Put another way, a scalar is a quantity whose specification (in any coordinate system) requires just one number. On the other hand, a vector (originally defined as a directed line segment) is a quantity whose specification requires three numbers, namely, its components with respect to some basis. In essence, scalars and vectors are both special cases of a more general object called a tensor of order n, whose specification in any given coordinate system require $3 ^ { n }$ numbers, again called the components of the tensor. In fact,

scalars are tensors of order 0, with $3 ^ { 0 } = 1$ components, vectors are tensors of order 1, with $3 ^ { 1 } = 3$ components.

Tensors can be added or subtracted by adding or subtracting their corresponding components. They can also be multiplied in various ways by multiplying components in various combinations. These and other possible operations with tensors will not be described here.

A tensor of the second rank is said to be symmetric if $C _ { i j } = C _ { j i }$ and to be antisymmetric if $C _ { i j } = - C _ { j i }$ . An antisymmetric tensor has its diagonal components equal to zero. Any tensor may be regarded as the sum of a symmetric and an antisymmetric part for

$$C _ {i j} = \frac {1}{2} \left[ C _ {i j} + C _ {j i} \right] + \frac {1}{2} \left[ C _ {i j} - C _ {j i} \right] \tag {2.10a}$$

and

$$\frac {1}{2} \left[ C _ {i j} + C _ {j i} \right] = S _ {i j} \quad \frac {1}{2} \left[ C _ {i j} - C _ {j i} \right] = A _ {i j}, \tag {2.10b}$$

where $S _ { i j }$ is symmetric and $A _ { i j }$ is antisymmetric. Numerous physical quantities have the properties of tensors of the second rank, so that the inertial properties of a rigid body can be described by the symmetric tensor of inertia. By way of illustration, consider that we are given two vectors A and B. There are nine products of a component of A with a component of B. Thus,

$$A _ {i} B _ {i} (i, k = 1, 2, 3).$$

Suppose we transform to a new coordinate system $K ^ { \prime }$ , in which A and B have components $A _ { i } ^ { \prime }$ and $B _ { k } ^ { \prime }$ . Then the transformation of a coordinate system can be expressed as

$$A _ {i} = \alpha_ {i ^ {\prime}} A _ {k},$$

where $A _ { k } , A _ { i } ^ { \prime }$ are the components of the vector in the old and new coordinate systems K and $K ^ { \prime }$ , respectively, and $\alpha _ { i ^ { \prime } k }$ is the cosine of the angle between the ith axis of $K ^ { \prime }$ and the kth axis of K. Thus,

$$A _ {i} ^ {\prime} = \alpha_ {i ^ {\prime} k} A _ {i}, B _ {k} ^ {\prime} = \alpha_ {k ^ {\prime} m} B _ {m},$$

and hence

$$A _ {i} ^ {\prime} B _ {k} ^ {\prime} = \alpha_ {i ^ {\prime} l} \alpha_ {k ^ {\prime} m} A _ {l} B _ {m}.$$

Therefore, $A _ { i } B _ { k }$ is a second-order tensor.
