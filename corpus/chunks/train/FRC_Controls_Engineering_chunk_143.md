# 6.6.5 Examples

Snippet 6.1 shows how one packs together the following augmented matrix in Python using np.block().

$$
\left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {C} & \mathbf {D} \end{array} \right]
$$

```python
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5], [6]])
C = np.array([[7, 8]])
D = np.array([[9]])
tmp = np.block([[A, B], [C, D]]) 
```  
Snippet 6.1. Matrix augmentation example: block

Snippet 6.2 shows how one packs together the same augmented matrix in Python using array slices.

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5], [6]])
C = np.array([[7, 8]])
D = np.array([[9]])
tmp = np.empty((3, 3))
tmp[:2, :2] = A # tmp[0:2, 0:2] = A
tmp[:2, 2:] = B # tmp[0:2, 2:3] = B
tmp[2:, :2] = C # tmp[2:3, 0:2] = C
tmp[2:, 2:] = D # tmp[2:3, 2:3] = D 
```  
Snippet 6.2. Matrix augmentation example: array slices

Section 6.7 demonstrates model augmentation for different types of integral control.
