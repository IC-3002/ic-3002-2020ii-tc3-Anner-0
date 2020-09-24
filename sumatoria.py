def sumatoria_cubica(n):
    result=0
    for i in range(1, n+1):
        for j in range(1, i+1):
            for k in range(j, i+j+1):
                result+=1
    return(result)
    # raise NotImplementedError()

def sumatoria_constante(n):
    result=((n*(n+1)*(2*n+1))/6)+((n*(n+1))/2)
    return(result)
    # raise NotImplementedError()


