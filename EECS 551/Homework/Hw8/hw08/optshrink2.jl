using LinearAlgebra
using Statistics
"""
Xh = optshrink2(Y::AbstractMatrix, r::Int)
Perform rank−`r` denoising of data matrix `Y` using the OptShrink method
by Prof. Nadakuditi in this May 2014 IEEE Tr. on Info. Theory paper:
http://doi.org/10.1109/TIT.2014.2311661
In:
− `Y` 2D array where `Y = X + noise` and goal is to estimate `X`
− `r` estimated rank of `X`
Out:
− `Xh` rank−`r` estimate of `X` using OptShrink weights for SVD components
This version works even if one of the dimensions of `Y` is large,
as long as the other is sufficiently small.

Cite: I find this code online 
"""
function optshrink2(Y::AbstractMatrix, r::Int)
    (U, s, V) = svd(Y)
    m = size(Y)[1]
    n = size(Y)[2]
    
    r = min(r, m, n)
    
    S = s[(r+1):end]
    
    w = zeros(r)
    for k = 1:r
        (D, Dder) = D_transform_from_matrix(s[k], S, max(m,n)-r, min(m,n)-r)
        w[k] = -2*D/Dder
    end
    
    Xh = U[:,1:r] * diagm(w) * V[:,1:r]'
    return Xh
end

function D_transform_from_matrix(z, sn, m, n)
    sm = [sn; zeros(m-n)]
    D11 = 1 ./ ((z^2) .- (sn.^2))
    D22 = 1 ./ ((z^2) .- (sm.^2))
    
    D1 = (1/n) * sum(z .* D11)
    D2 = (1/m) * sum(z .* D22)
    
    D = D1*D2
    
    D1_derivative = (1/n) * sum(-2 * (z^2) .* (D11.^2) + D11)
    D2_derivative = (1/m) * sum(-2 * (z^2) .* (D22.^2) + D22)
    
    D_der = D1 * D2_derivative + D2 * D1_derivative
   
    return (D, D_der)
end
    