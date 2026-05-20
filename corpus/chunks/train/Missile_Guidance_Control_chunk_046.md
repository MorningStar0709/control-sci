$$[ Q ] = q _ {0} + \mathbf {i} q _ {1} + \mathbf {j} q _ {2} + \mathbf {k} q _ {3} = (q _ {0}, q _ {1}, q _ {2}, q _ {3}) = (q _ {0}, \mathbf {q}), \tag {2.11}$$

where $q _ { 0 } , q _ { 1 } , q _ { 2 } , q _ { 3 }$ are real numbers and the set {i, j, k} forms a basis for a quaternion vector space. From the orthogonality property of quaternions, we have

$$q _ {0} ^ {2} + q _ {1} ^ {2} + q _ {2} ^ {2} + q _ {3} ^ {2} = 1. \tag {2.12}$$

In terms of the Euler angles φ, θ , ψ, we have

$$q _ {0} = \cos (\psi / 2) \cos (\theta / 2) \cos (\phi / 2) - \sin (\psi / 2) \sin (\theta / 2) \sin (\phi / 2),q _ {1} = \sin (\theta / 2) \sin (\phi / 2) \cos (\psi / 2) + \sin (\psi / 2) \cos (\theta / 2) \cos (\phi / 2),q _ {2} = \sin (\theta / 2) \cos (\psi / 2) \cos (\phi / 2) - \sin (\psi / 2) \sin (\phi / 2) \cos (\theta / 2),q _ {3} = \sin (\phi / 2) \cos (\psi / 2) \cos (\theta / 2) + \sin (\psi / 2) \sin (\theta / 2) \cos (\phi / 2).$$

Suppose now that we wish to transform any vector, say V, from body coordinates $\mathbf { V } ^ { b }$ into the navigational coordinates $\mathbf { V } ^ { n }$ . This transformation can be expressed as follows:

$$\mathbf {V} ^ {n} = C _ {b} ^ {n} \mathbf {V} ^ {b},$$

where $C _ { b } ^ { n }$ is the direction cosine matrix, or equivalently, using quaternions,

$$\mathbf {V} ^ {n} = q \mathbf {V} ^ {b} q ^ {*},$$

where $q ^ { * }$ is the conjugate of q. Then [7]

$$
C _ {b} ^ {n} = \left[ \begin{array}{c c c} q _ {0} ^ {2} + q _ {1} ^ {2} - q _ {2} ^ {2} - q _ {3} ^ {2} & 2 (q _ {1} q _ {2} - q _ {0} q _ {3}) & 2 (q _ {1} q _ {3} + q _ {0} q _ {2}) \\ 2 (q _ {1} q _ {2} + q _ {0} q _ {3}) & q _ {0} ^ {2} - q _ {1} ^ {2} + q _ {2} ^ {2} - q _ {3} ^ {2} & 2 (q _ {2} q _ {3} - q _ {0} q _ {1}) \\ 2 (q _ {1} q _ {3} - q _ {0} q _ {2}) & 2 (q _ {2} q _ {3} + q _ {0} q _ {1}) & q _ {0} ^ {2} - q _ {1} ^ {2} - q _ {2} ^ {2} + q _ {3} ^ {2} \end{array} \right].
$$

For more details on the quaternion and its properties, the reader is referred to [7].
