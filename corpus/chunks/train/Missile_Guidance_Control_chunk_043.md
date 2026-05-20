# 2.1.2 Linear Vector Functions

If a vector is a function of a single scalar variable, such as time, each component of the vector is independently a function of this variable. If the vector is a linear function of time, then each component is proportional to the time. A vector may also be a function of another vector. In general, this implies that each component of the function depends on each component of the independent vector. Moreover, a vector is a linear function of another vector if each component of the first is a linear function of the three components of the second. This requires nine independent coefficients of proportionality. The statement that a is a linear function of b means that

$$a _ {1} = C _ {1 1} b _ {1} + C _ {1 2} b _ {2} + C _ {1 3} b _ {3},a _ {2} = C _ {2 1} b _ {1} + C _ {2 2} b _ {2} + C _ {2 3} b _ {3}, \tag {2.5}a _ {3} = C _ {3 1} b _ {1} + C _ {3 2} b _ {2} + C _ {3 3} b _ {3}.$$

Using the summation convention as in (2.4), this becomes

$$a _ {i} = C _ {i j} b _ {j}. \tag {2.6}$$

A relationship such as that in (2.6) must be independent of the coordinate system in spite of the fact that the notation is clearly based on specific coordinates. The components $a _ { i }$ and $b _ { i }$ are with reference to a particular coordinate system. The constants $C _ { i j }$ also have reference to specific axes, but they must so transform with a rotation of axes that a given vector b always leads to the same vector a.

If the coordinate system is rotated about the origin, the vector components will change so that

$$a _ {i} = \gamma_ {i j ^ {\prime}} a _ {j ^ {\prime}} = C _ {i j} \gamma_ {j k ^ {\prime}} b _ {k ^ {\prime}}. \tag {2.7}$$

If both sides of this equation are multiplied by $\gamma _ { l ^ { \prime } i }$ and the equations for the three values of i are added, the result is

$$\gamma_ {l ^ {\prime} i} \gamma_ {i j ^ {\prime}} a _ {j ^ {\prime}} = a _ {l ^ {\prime}} = (\gamma_ {l ^ {\prime} i} C _ {i j} \gamma_ {j k ^ {\prime}}) b _ {k ^ {\prime}}. \tag {2.8}$$

If the quantity $\gamma _ { l ^ { \prime } i } C _ { i j } \gamma _ { j k ^ { \prime } }$ is called $C _ { l ^ { \prime } k ^ { \prime } }$ , then

$$a _ {i ^ {\prime}} = C _ {l ^ {\prime} k ^ {\prime}} b _ {k ^ {\prime}}. \tag {2.9}$$

This relationship between the components in this system of coordinates is the same vector relationship as was expressed by the $C _ { i k }$ in the original system of coordinates.
