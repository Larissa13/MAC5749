def bitmap2setPoints(bitmap,adj=4):
    adjx = []
    adjy = []
    if adj == 8:
        adjx = [-1,0,1,-1,1,-1,0,1];
        adjy = [-1,-1,-1,0,0,1,1,1];
    else:
        adjx = [0,-1,1,0];
        adjy = [-1,0,0,1];
        
    adjn = len(adjx)
    nrows,ncols = bitmap.shape
    setPoints = set();
    for i in range(0,nrows):
        for j in range(0,ncols):
            if bitmap[i,j] == 1:
                for dx,dy in zip(adjx,adjy):        
                    x = i + dx
                    y = j + dy
                    if x >= 0 and x < ncols and y >=0 and y < nrows:
                        if bitmap[x,y] == 0:                        
                            setPoints.add(tuple([x,y]))
    return list(setPoints)