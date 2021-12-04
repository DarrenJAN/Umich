# TODO 
using LinearAlgebra
"""
    labels = classify_image(test, train, K::Int)

Classify `test` signals using `K`-dimensional subspaces
found from `train`ing data via SVD

In:
* `test` `n x p` matrix whose columns are vectorized test images to be classified
* `train` `n x m x 10` array containing `m` training images for each digit 0-9 (in ascending order)
* `K` in `[1, min(n, m)]` is the number of singular vectors to use during classification

Out:
`labels` vector of length `p` containing the classified digits (0-9) for each test image
"""
function classify_image(test, train, K::Int)
    n = size(test)[1]
    p = size(test)[2]
    m = size(train)[2]
    d = size(train)[3]
    
    Q = zeros(n, K, d)
    for i in 1:d
        U, _, _= svd(train[:,:,i])
        Uk = U[:,1:K]
        Q[:,:,i] = Uk 
    end
    
    err = zeros(d, p)
    for i in 1:d
        err[i,:] = sum((test - Q[:,:,i]*(Q[:,:,i]'*test)).^2, dims=1)
    end
 
    labels = map(ii -> ii[1]-1, argmin(err, dims = 1));
    return labels
    
end
