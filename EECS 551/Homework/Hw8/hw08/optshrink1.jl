using LinearAlgebra

function Dz(z, X)
    n = size(X)[1]
    m = size(X)[2]
    In = Diagonal(ones(n))
    Im = Diagonal(ones(m))
    z2IXXt = z^2*In - X*X';
    z2IXtX = z^2*Im - X'*X;
    invz2XtX = inv(z2IXtX);
    invz2XXt = inv(z2IXXt);

    D1z = 1/n*tr(z*invz2XXt);
    D2z = 1/m*tr(z*invz2XtX);

    Dz = D1z*D2z;

    return Dz
end 

function Dpz(z, X)
    n = size(X)[1]
    m = size(X)[2]
    In = Diagonal(ones(n))
    Im = Diagonal(ones(m))
    
    z2IXXt = z^2*In - X*X';
    z2IXtX = z^2*Im - X'*X;
    invz2XtX = inv(z2IXtX);
    invz2XXt = inv(z2IXXt);

    D1z = 1/n*tr(z*invz2XXt);
    D2z = 1/m*tr(z*invz2XtX);


    D1zp = 1/n*tr(-2*z^2*invz2XXt^2+invz2XXt);
    D2zp = 1/m*tr(-2*z^2*invz2XtX^2+invz2XtX);

    Dpz = D1z*D2zp+D1zp*D2z;
    return Dpz
end 


"""
Xh = optshrink1(Y::AbstractMatrix, r::Int)
Perform rank?r denoising of data matrix `Y` using the OptShrink method
by Prof. Nadakuditi in this May 2014 IEEE Tr. on Info. Theory paper:
http://doi.org/10.1109/TIT.2014.2311661
In:
? `Y` 2D array where `Y = X + noise` and goal is to estimate `X`
? `r` estimated rank of `X`
Out:
? `Xh` rank?`r` estimate of `X` using OptShrink weights for SVD components
This version works only if the size of `Y` is sufficiently small,
because it performs calculations involving arrays roughly of
`size(Y'*Y)` and `size(Y*Y')`, so neither dimension of `Y` can be large.
"""
function optshrink1(Y::AbstractMatrix, r::Int)
    (U, s, V)  = svd(Y)
    n = size(Y)[1]
    m = size(Y)[2]
    
    S_ = diagm(n-r, m-r, s[r+1:end])
    
    W =  Array{Float64}(undef, r)
    
    for i in 1:r
        d =  Dz(s[i], S_) 
        d_ = Dpz(s[i], S_)
        W[i] =  -2 * d / d_
    end 
    
    S_opt = U[:,1:r] * Diagonal(vec(W)) * V[:, 1:r]'
    return S_opt
    
end 

