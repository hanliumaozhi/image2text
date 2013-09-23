#coding=utf-8

import argparse
import cv2


def imageToText(image, argvDict):
    charsList = "   ...',;:clodxkO0KXUNWMMM"
    height = image.shape[0]
    width = image.shape[1]
    
    if argvDict.width == -1 and argvDict.height == -1:
        print u"没指定长或宽"
        sys.exit(1)
    elif argvDict.width == -1 and argvDict.height != -1:
        height = argvDict.height
        width = int(height*width*1.0/image.shape[0])
    elif argvDict.width != -1 and argvDict.height == -1:
        width = argvDict.width
        height = int(height*width*1.0/image.shape[1])
    else:
        width = argvDict.width
        height = argvDict.height
    
    image = cv2.resize(image, (height, width))
    
    output = ''
    for i in xrange(height):
        for j in xrange(width):
            charIndex = image[i,j]/10
            output += charsList[charIndex]
        output += '\n'
        
    outputFile = open('img.txt', 'w')
    outputFile.write(output)
    outputFile.close()
            
        
    
    #cv2.imshow("simple", image)
    #cv2.waitKey(0)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--width', '-W', default=-1, type=int)
    parser.add_argument('--height', '-H', default=-1, type=int)
    parser.add_argument('filename', metavar='string', type=str, nargs='+')
    argvDict = parser.parse_args()
    for i in argvDict.filename:
        img = cv2.imread(i, 0)
        imageToText(img, argvDict)
    
    
if __name__ == '__main__':
    main()
