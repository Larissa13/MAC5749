def bitmap2pointsSet(bitmapImage):
    pointSet = []
    row = 0
    while row < bitmapImage.shape[0]:
        column = 0
        while column + 1 < bitmapImage.shape[1]:
            if (bitmapImage[row][column] != bitmapImage[row][column + 1]):
                 if ((not bitmapImage[row][column]) and (bitmapImage[row][column + 1])) or ((bitmapImage[row][column]) and not (bitmapImage[row][column + 1])):
                    pointSet.append([row + 1, column + 1])
            column += 1
        row += 1
    
    return (pointSet)