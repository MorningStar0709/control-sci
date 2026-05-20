$$\dot {z} _ {i} = s _ {i} z _ {i} + \left(\mathbf {w} _ {i} ^ {T} B\right) \mathbf {u} \tag {3.66}\dot {z} _ {i + 1} = s _ {i} ^ {*} z _ {i + 1} + \left(\mathbf {w} _ {i} ^ {* T} B\right) \mathbf {u} \tag {3.67}\mathbf {y} = C \mathbf {v} _ {i} z _ {i} + C \mathbf {v} _ {i} ^ {*} z _ {i + 1}. \tag {3.68}$$

The contribution to the state at $t = 0$ is

$$z _ {i} (0) \mathbf {v} _ {i} + z _ {i + 1} (0) \mathbf {v} _ {i} ^ {*}$$

which must be real, so

$$R e z _ {i} (0) I _ {m} \mathbf {v} _ {i} + I _ {m} z _ {i} (0) R e \mathbf {v} _ {i} - R e z _ {i + 1} (0) I _ {m} \mathbf {v} _ {i} + I _ {m} z _ {i + 1} (0) R e \mathbf {v} _ {i} = 0$$

or

$$[ R e z _ {i} (0) - R e z _ {i + 1} (0) ] I _ {m} \mathbf {v} _ {i} + [ I _ {m} z _ {i} (0) + I _ {m} z _ {i + 1} (0) ] R e \mathbf {v} _ {i} = 0.$$

Since the real and imaginary parts of a complex eigenvector are linearly independent, the coefficients of both $I_{m}\mathbf{v}_{i}$ and $Rev_{i}$ are zero; i.e.,

$$R e z _ {i + 1} (0) = R e z _ {i} (0)I _ {m} z _ {i + 1} (0) = - I _ {m} z _ {i} (0)$$

or $z_{i + 1}(0) = z_i^* (0)$ .

Conjugating each side of Equation 3.66,

$$\dot {z} _ {i} ^ {*} = s _ {i} ^ {*} z _ {i} ^ {*} + (\mathbf {w} _ {i} ^ {* T} B) u$$

so that $z_{i}^{*}$ and $z_{i + 1}$ satisfy the same differential equation. Since $z_{i + 1}(0) = z_{i}^{*}(0)$ , it follows that $z_{i + 1}(t) = z_{i}^{*}(t)$ .

We transform Equations 3.66 and 3.67 by (1) addition and (2) subtraction and multiplication by -j. This amounts to taking the real and imaginary parts of Equation 3.66:

$$\frac {d}{d t} (R e z _ {i}) = (R e s _ {i}) (R e z _ {i}) - (I _ {m} s _ {i}) (I _ {m} z _ {i}) + (R e \mathbf {w} _ {i} ^ {T} B) \mathbf {u}\frac {d}{d t} (I _ {m} z _ {i}) = (I _ {m} s _ {i}) (R e z _ {i}) + (R e s _ {i}) (I _ {m} z _ {i}) + (I _ {m} \mathbf {w} _ {i} ^ {T} B) \mathbf {u} \tag {3.69}y = 2 C (R e \mathbf {v} _ {i}) (R e z _ {i}) - 2 C (I _ {m} \mathbf {v} _ {i}) (I _ {m} z _ {i}). \tag {3.70}$$

The two decoupled, complex differential equations are replaced by a pair of coupled, real equations. In the A matrix, a complex pair generates a $2 \times 2$ diagonal block.
