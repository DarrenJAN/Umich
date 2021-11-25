using LinearAlgebra
"""
haveCommonRoot = common_root(a, b ; atol)
Determine if the polynomials described by input coefficient vectors `a`
and `b` share a common root, to within an absolute tolerance parameter `atol`.
Assume leading coefficients `a[end]` and `b[end]` are nonzero.
In:
− `a` : vector of length `m + 1` with `a[m+1] != 0` and `m   0`
defining a degree `m` polynomial of the form:
`p(z) = a[m+1] z^m + a[m] z^(m − 1) + ... + a[2] z + a[1]`
− `b` : vector of length `n + 1` with `b[n+1] != 0` and `n   0`
defining a degree `n` polynomial of the form:
`q(z) = b[n+1] z^n + b[n] z^(n − 1) + ... + b[1] z + b[1]`
Option:
− `atol::Real` absolute tolerance for calling `isapprox`
Out:
− `haveCommonRoot` = `true` when `p` and `q` share a common root, else `false`
"""
function common_root(a::AbstractVector, b::AbstractVector ; atol::Real=1e-6)
    m = size(a,1)
    n = size(b,1)
    if (m == 1 || n == 1)
        return false
    end
    # companion matrix maker:
    compan = c-> [-transpose(reverse(c)); [I zeros(length(c)-1)]]
    A = compan(a[1:end-1] / a[end])
    B = compan(b[1:end-1] / b[end])
    
    kron_A_B = kron(A, I(n-1)) + kron(I(m-1), -B)
    return isapprox(det(kron_A_B), 0.0,atol = atol)
end