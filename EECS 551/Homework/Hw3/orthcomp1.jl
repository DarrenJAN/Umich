"""
z = orthcomp1(y, x)
Project `y` onto the orthogonal complement of `Span({x})`
In:
* `y` vector
* `x` nonzero vector of same length, both possibly very long
Out:
* `z` vector of same length
For full credit, your solution should be computationally efficient.
"""
function orthcomp1(y, x)
    z = y - ((x' * y) / ( x' * x)) * x
    return z 
end 