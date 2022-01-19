# TODO 
# make sure to include any using statements before submitting to the autograder 
using LinearAlgebra
using Statistics
"""
Xr = dist2locs(D, d)

In:
* `D` is an `n x n` matrix such that `D[i, j]` is the distance from object `i` to object `j`
* `d` is the desired embedding dimension.

Out:
* `Xr` is an `d x n` matrix whose columns contains the relative coordinates of the `n` objects

Note: MDS is only unique up to rotation and translation,
so we enforce the following conventions on Xr in this order:
* [ORDER] `Xr[i,:]` corresponds to ith largest eigenpair of `C' * C`
* [CENTER] The centroid of the coordinates is zero
* [SIGN] The largest magnitude element of `Xr[i,:]` is positive
"""
function dist2locs(D, d)
    #set up
    J = size(D,1)
    S = D .^2
    S = 0.5 * (S + S') 
    P_orth = Diagonal(ones(J)) - (1/J) * ones(J) * ones(J)'
    G = (-1 / 2) * P_orth * S * P_orth
    
    # e = eigvals(G)
    # V = eigvecs(G)

    # #Compute relative coordinates
    # d= min(d, count(e .>0))
    # inv_e = sort(e, rev=true)
    # Xr =  V[:, indexin(inv_e[1:d], e)] * Diagonal(sqrt.(inv_e[1:d]))

    # Xr .-= mean(Xr, dims= 1)
    
    # #Get rid of the sign ambiguity 
    # Xr_abs = abs.(Xr)
    # Xr .*= sign.(Xr[findmax(Xr_abs, dims=1)[2]])
    # Xr = Xr'

    (U, s, V) = svd(G)
    Xr = Diagonal( sqrt.(s[1:d])) * V[:,1:d]'
    Xr_abs = abs.(Xr)
    for i in 1:d

        index = indexin(maximum(Xr_abs, dims=2)[i], Xr_abs[i,:])[1]
        a = Xr[i,:][index]
        if a < 0.0
            Xr[i, :] = -1 .* Xr[i, :]
        end
    end

    return Xr
end
