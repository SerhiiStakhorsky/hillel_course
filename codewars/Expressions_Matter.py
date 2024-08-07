def expression_matter(a, b, c):
    var1 = a + b + c
    var2 = a * b * c
    var3 = a + b * c
    var4 = a * b + c
    var5 = (a + b) * c
    var6 = a * (b + c)

    return max(var1, var2, var3, var4, var5, var6)
