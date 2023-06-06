s={1,3,4,6}
for i  in range(10):
    if i in s:
        for j in range(10):
            if j in s and j!=i:
                for k in range(10):
                    if k in s and k!=i and k!=j:
                        for l in range(10):
                            if l in s and l!=k  and l!=j and l!=i:
                                print(f"{i}{j}{k}{l}",end=" ")
        