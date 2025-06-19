def γ():
    a = [70, 73, 65]  
    b1 = [123]        
    b2 = [125]        

    trash = lambda: [chr(x) for x in range(65, 91) if x % 2 == 0] 
    _ = i.cycle(trash())

    enc = "315a5136453063457637455a69317149795832755670397256594268496e474d3f7573703d64726976655f6c696e6b"
    content = ψ(map(ord, β(enc)))

    return ψ(a) + ψ(b1) + content + ψ(b2)