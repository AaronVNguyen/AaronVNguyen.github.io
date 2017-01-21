def avg_pixel(row_min, row_max, col_min, col_max, width, height, pixelList):
        avgPixel = [0,0,0]
        for i in range(row_min, row_max + 1):
                for j in range(col_min, col_max + 1):
                        avgPixel[0] += pixelList[i][j][0]
                        avgPixel[1] += pixelList[i][j][1]
                        avgPixel[2] += pixelList[i][j][2]
        totalPixels = int((row_max - row_min + 1) * (col_max - col_min + 1))
        for i in range(len(avgPixel)):
                avgPixel[i] /= totalPixels
        return avgPixel
