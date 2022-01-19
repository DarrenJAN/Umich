using LinearAlgebra

"""
Ac, r = compress_image(A, p)
In:
* `A` `m × n` matrix
* `p` scalar in `(0, 1]`
Out:
* `Ac` a `m × n` matrix containing a compressed version of `A`
that can be represented using at most `(100 * p)%` as many bits
required to represent `A`
* `r` the rank of `Ac`
"""
function compress_image(A, p)
    m = size(A)[1]
    n = size(A)[2]
    
    (U, s, V) = svd(A)
    r = rank(Diagonal(s))
    k= Int(floor(p * m * n/(m+n+1)))

    r= min(r, k)
    Ac = U[:,1:r] * Diagonal(s[1:r]) * V[:,1:r]'
    
    return Ac, r
end 
