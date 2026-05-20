# U-D Covariance Factorization

Equation (13.15) is one way to mechanize the recursive updates of the estimates and the covariance matrix. These equations are not well-conditioned from a numerical point of view, however. A better way of doing the calculation is to update the square-root of P instead of updating P. Another way to do the calculations is to use the U-D algorithm by Bierman and Thorton. This method is based on a factorization of P as

$$P = U D U ^ {T}$$

where D is diagonal and U is an upper-triangular matrix. This method is a square-root type as $UD^{1/2}$ is the square root of P. The U-D factorization method does not include square-root calculations and is therefore well suited for small computers and real-time applications. Details about the algorithm can be found in the References.

A Pascal program for least-squares estimation based on U-D factorization is given in Listing 13.1. The program gives estimates of the parameters of the process

$$
\begin{array}{l} y (k) + a _ {1} y (k - 1) + \dots + a _ {n a} y (k - n a) \\ = b _ {1} u (k - 1) + \dots + b _ {n b} u (k - n b) + e (k) \tag {13.16} \\ \end{array}
$$

The notations used in the program are

<table><tr><td>Variable</td><td>Notation in the program</td></tr><tr><td>u(k)</td><td>u</td></tr><tr><td>y(k)</td><td>y</td></tr><tr><td>na</td><td>na</td></tr><tr><td>na + nb</td><td>n</td></tr><tr><td>n(n - 1)/2</td><td>noff</td></tr><tr><td> $\hat{\theta}(k)$  compare (13.6)</td><td>theta</td></tr><tr><td> $\varphi^{T}(k)$  compare (13.7)</td><td>fi</td></tr><tr><td> $\lambda$ </td><td>lambda</td></tr></table>

Listing 13.1 Pascal program for least-squares estimation of the parameters of the process of (13.16) using U-D factorization.   
```txt
const npar=10; {maximum number of estimated parameters}
    noff=45; {noff=npar*(npr-1)/2}

type vec1=array[1..npar] of real;
    vec2=array[1..noff] of real;
    estpartyp = record
    n,na:integer;
    theta:vec1;
    fi:vec1;
    diag:vec1;
    offdiag:vec2;
    end;
var y,u,lambda:real;
    eststate:estpartyp;

Procedure LS(u,y,lambda:real;var eststate:estpartyp);
{Computes the least-squares estimate using the U-D method after Bierman and Thornton}

var kf,ku,i,j:integer;
    perr,fj,vj,alphaj,ajlast,pj,w:real;
    k:vec1;

begin
    with eststate do {Calculate prediction error}
    begin
    perr = y;
    for i:=1 to n do perr:=perr-theta[i]*fi[i]; 
```
