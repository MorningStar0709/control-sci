# 6-DOF Initialization

Before processing begins, these initialization functions must be performed. Compute the initialized Earth reference velocity:

$$
\begin{array}{l} U _ {e} = V * \cos (\theta) * \cos (\psi), \\ V _ {e} = V * \cos (\phi) * \sin (\psi), \\ W _ {e} = - V * \sin (\theta), \\ \end{array}
$$

where

$$U _ {e} = \text { Earth } X \text {-velocity },V _ {e} = \text { Earth } Y \text {-velocity },W _ {e} = \text { Earth Z - velocity },\theta = \text { pitch angle },\phi = \text { roll angle },\psi = \text { yaw angle },V = \text { a i r s p e e d }.$$

Compute Initialized Quaternions

$$A = \left[ \sin (\psi / 2) * \sin (\theta / 2) * \cos (\phi / 2) \right] - \left[ \cos (\psi / 2) * \cos (\theta / 2) * \sin (\phi / 2) \right],B = - 1 * \left[ \cos (\psi / 2) * \sin (\theta / 2) * \cos (\phi / 2) \right] - \left[ \sin (\psi / 2) * \cos (\theta / 2) * \sin (\phi / 2) \right],C = - 1 * [ \sin (\psi / 2) * \cos (\theta / 2) * \cos (\phi / 2) ] + [ \cos (\psi / 2) * \sin (\theta / 2) * \sin (\phi / 2) ],D = - 1 * \left[ \cos (\psi / 2) * \cos (\theta / 2) * \cos (\phi / 2) \right] - \left[ \sin (\psi / 2) * \sin (\theta / 2) * \sin (\phi / 2) \right],$$

where A, B, C, D = quaternion parameters of the direction cosine matrix.

Now compute the initialized direction cosine matrix:

$$C m (1, 1) = A ^ {2} - B ^ {2} - C ^ {2} + D ^ {2},C m (1, 2) = 2 * (A * B - C * D),C m (1, 3) = 2 * (A * C + B * D),C m (2, 1) = 2 * (A * B + C * D),C m (2, 2) = - 1 * A ^ {2} + B ^ {2} - C ^ {2} + D ^ {2},C m (2, 3) = 2 * (B * C - A * D),C m (3, 1) = 2 * (A * C - B * D),C m (3, 2) = 2 * (B * C + A * D),C m (3, 3) = - 1 * A ^ {2} - B ^ {2} + C ^ {2} + D ^ {2},$$

where Cm direction cosine matrix.

Compute the initial body velocity

$$U _ {b} = C m (1, 1) * U _ {e} + C m (2, 1) * V _ {e} + C m (3, 1) * W _ {e},V _ {b} = C m (1, 2) * U _ {e} + C m (2, 2) * V _ {e} + C m (3, 2) * W _ {e},W _ {b} = C m (1, 3) * U _ {e} + C m (2, 3) * V _ {e} + C m (3, 3) * W _ {e},$$

where

$$U _ {b} = \text { body } X \text {-velocity },V _ {b} = \text { body } Y \text {-velocity},W _ {b} = \text { body } Z \text {-velocity. }$$
