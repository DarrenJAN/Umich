
using LinearAlgebra
"""
    zmax, zmin = outlying_roots(a, v0, nIters)
Use power iteration to compute the largest and smallest magnitude roots,
respectively, of the polynomial defined by the input coefficients
In:
−  a  coefficient vector of length  n + 1  defining the polynomial
p(x) = a[n+1] x^n + a[n−1] x^n−1 + ... + a[2] x + a[1] with a[n+1] != 0
Option:
− v0 vector of length n with initial guess of an eigenvector; default randn(n) − nIters number of power iterations to perform; default 100
Out:
−  zmax  root of  p(x)  with largest magnitude
−  zmin  root of  p(x)  with smallest magnitude
"""
function outlying_roots(a ; v0::AbstractVector{<:Real} = randn(length(a) - 1), nIters::Int=100)
    compan = c -> [-transpose(reverse(c)); [I zeros(length(c) - 1)]]
    b= reverse(a)
    
    A = compan(a[1:end - 1]/a[end])
    if(b[end] != 0)
        B = compan(b[1:end - 1]/b[end])
    end
    
    vk_max = v0
    vk_min = v0
    zmax = 0
    zmin = 0
    
    #compute zmax
    for i in 1:nIters
        vk_max = (A * vk_max ) / norm(A * vk_max)
    end
    zmax = vk_max' * A * vk_max
    
    #compute zmin
    if(b[end] != 0)
        for i in 1:nIters
            vk_min = (B * vk_min ) / norm(B * vk_min)
        end
        zmin = 1 / (vk_min' * B * vk_min)
    end
        
    return zmax, zmin
end