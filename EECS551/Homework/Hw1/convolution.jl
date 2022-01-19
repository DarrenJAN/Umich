"""
`H, y = convolution(h, x)`
Compute discrete convolution of the input vectors via
matrix multiplication, returning both the matrix `H` and result `y`
In:
âˆ? `h` vector of length `K`
âˆ? `x` vector of length `N`
Out:
âˆ? `H` `M Ã— N` convolution matrix defined by `h`
âˆ? `y` vector of length `M` containing the discrete convolution of `h` and `x` computed using `H`.
"""
function convolution(h, x)
    K = length(h)
    N = length(x)
    
    M = N + K - 1
    H = zeros(eltype(h), M, N)
    for i in 1:M
        for j in 1:N 
            if i < j 
                H[i, j] = 0
            elseif i - j >= K
                H[i, j] = 0
            else 
                H[i, j] = h[i - j + 1]
            end
        end
    end
    
    y = H * x
    return H, y 
end

