"""
R = orthcompnull(A, X)
Project each column of `X` onto the orthogonal complement of the null space
of the input matrix `A`.
In:
* `A` `M × N` matrix
* `X` vector of length `N`, or matrix with `N` rows and many columns
Out:
* `R` : vector or matrix of size ??? (you determine this)
For full credit, your solution should be computationally efficient!
"""

using LinearAlgebra
function orthcompnull(A, X)
    r = rank(A)
    u, s, v = svd(A)
    vr = v[:, 1:r]
    R = vr * (vr' * X)
    return R 
end