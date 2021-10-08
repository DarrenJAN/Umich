function compute(N)
    res = 0
    for k in 0:100 
        res = res + binomial(BigInt(N), BigInt(k)) * 75* k *  (0.92)^k * (0.08)^(N-k)
    end 
    for k in 101:N
        res = res  + binomial(BigInt(N), BigInt(k)) * (17500 - 100* k)  *  (0.92)^k * (0.08)^(N-k)
    end 
    return res  
end 

function Find_max_N()
    res = 0
    Max_N = 0
    for N in 0:150
        cur_res =  compute(N)
        if cur_res > res
            Max_N = N
            res = cur_res
        end 
    end 
    return Max_N
end 
        
display(Find_max_N())