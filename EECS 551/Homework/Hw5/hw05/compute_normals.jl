using LinearAlgebra
"""
N = compute_normals(data, L)
In:
− `data` `m × n × d` matrix whose `d` slices contain `m × n` images
of a common scene under different lighting conditions
− `L` `3 × d` matrix whose columns are the lighting direction vectors
for the images in data, with `d   3`
Out:
− `N` `m × n × 3` matrix containing the unit−norm surface normal vectors
for each pixel in the scene
"""
function compute_normals(data, L)
    
    m, n, d= size(data) 
    data =reshape(data, m * n, d) # data become (m*n) * d matrix 
    
    L = mapslices(normalize, L, dims=1) #norm vectors of lighting direction
    
    N = data * pinv(L)
    N = reshape(N, m, n, 3)
    N = mapslices(normalize, N, dims = 3)  #unit-norm surface normal vectors for each pixel in a scene
    
    return N
    
end 

