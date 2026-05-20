```mermaid
graph LR
    A["parts"] --> B["physical system"]
    B --> C["Lumped physical model"]
    C --> D["Differential equations"]
    D --> E["STATE SPACE MODEL"]
    E --> F["CONTROL DESIGN"]
    D --> G["LAPLACE TRANSFORM TRANSFER FUNCTION"]
    H["LINEARIZATION"] --> D
    I["× = Ax + Bu\ny = Cx + Du"] --> E
    J["V = Ld/i + ir·lf/i\nir + 1/sid\nF = kl = Mx + Bx"] --> D
    K["X(s)/V(s) = k(s+a)/s² + bs² + cs+d"] --> G
```
</details>

Figure 1.1: Conceptual ow of system analysis preceding control system design.s

Classical models are transfer functions based on use of the Laplace transform to convert LODEs into polynomials or ratios of polynomials. State Space models stay in the time domain and map a system of LODEs into a matrix version of a rst-order LODE.

The rest of this book will cover this process for the rst 4 Chapters. Then we will start designing controllers themselves in Chapters 5-11.
