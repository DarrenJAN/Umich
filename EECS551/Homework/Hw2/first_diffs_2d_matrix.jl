using LinearAlgebra
using SparseArrays
"""
D = Construct_D(m)
In:
 `m` is positive number
Out:
 `D` is a `mxm' circulant first finite difference matrix
"""
function Construct_D(m)
    # D = spdiagm(0 => -1* ones(m), 1 => ones(m-1), 1-m => [-1])
    D = spdiagm(0 => -1* ones(m), 1 => ones(m-1))
    D[m ,1 ] = 1
    return D
end 
   

"""
A = first_diffs_2d_matrix(m, n)
In:
    `m` and `n` are positive integers
Out:
     `A` is a `2mn * mn` sparse matrix such that `A * vec(X)` computes the
first differences down the columns (along x direction)
and across the (along y direction) of the `m * n` matrix `X`.
"""
function first_diffs_2d_matrix(m, n)
    A = zeros(eltype(0.0), 2*m*n, m*n)
    Dm = Construct_D(m)
    Dn = Construct_D(n)
    # display(Dm)
    # display(Dn)
    Im = I(m)
    In = I(n)

    A = [kron(In, Dm) ; kron(Dn, Im)]
    return A 
end 
 

# A = first_diffs_2d_matrix(2,3)
# display(A)

# fxy = [0, 4 ,1, 9, 3, 15]
# dfdx = [4, -4, 8, -8, 12, -12]
# dfdy = [1, 5, 2, 6,-3,-11]

# A * fxy == vcat(dfdx, dfdy)


# m = 30; n = 20 ;
# X = Float64.([(x-12)^2+(y-8)^2 < 5^2 for x=1:m, y=1:n])
# dfdx = diff(X; dims=1)
# dfdy = diff(X; dims=2)
# jim(
#     jim(X, "FXY: f(x,y)"; xlabel="x", ylabel="y"),
#     jim(dfdx, "DFDX: df(x,y) / dx"; xlabel="x", ylabel="y"),
#     jim(dfdy, "DFDY: df(x,y) / dy"; xlabel="x", ylabel="y"),
# )




