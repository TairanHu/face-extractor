import sys
import cv2
from PIL import Image, ImageEnhance

def threshold(face_path):
    face_img = cv2.imread(face_path, 0)
    ret, thresh = cv2.threshold(face_img, 160, 255, cv2.THRESH_TRUNC)
    cv2.imshow('after', thresh)
    cv2.imshow('before', face_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Contrast(face_path, contrast, brightness):
    gray_img = Image.open(face_path)
    contrast_enhancer = ImageEnhance.Contrast(gray_img)
    contrast_img = contrast_enhancer.enhance(contrast)
    #contrast_img.show("Contrast %f" % factor)
    bright_enhancer = ImageEnhance.Brightness(contrast_img)
    result = bright_enhancer.enhance(brightness)
    #result.show("Bright %f" % factor)
    result.save(face_path.split('.')[0]+'_baomanface.png')

def turn_to_gray(img_path):
    img = Image.open(img_path)
    gray_img = img.convert('L')
    gray_img.save(img_path.split('.')[0]+'_gray.png')

def make_baoman(face_path, contrast, brightness):
    Contrast(face_path, contrast, brightness)
    # Load two images
    img1 = cv2.imread('panda.jpg')
    img2 = cv2.imread(face_path.split('.')[0]+'_baomanface.png')
    y, x, c = img2.shape
    img2 = cv2.resize(img2, (348, 416))
    print 'size: ', 4.0*x, 4.0*y

    # I want to put logo on top-left corner, So I create a ROI
    height, width, c = img1.shape
    rows,cols,channels = img2.shape
    #roi = img1[height/2-rows/2:height/2-rows/2+rows, width/2-cols/2:width/2-cols/2+cols]

    # Now create a mask of logo and create its inverse mask also
    #img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    #ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    #mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    #img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    #img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

    # Put logo in ROI and modify the main image
    #dst = cv2.add(img1_bg,img2_fg)
    img1[height/2-rows/2:height/2-rows/2+rows, width/2-cols/2:width/2-cols/2+cols] = img2[:,:]
    cv2.imshow('res',img1)
    cv2.imwrite(face_path.split('.')[0] + '_baoman_panda.png', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    face_path = sys.argv[1]
    make_baoman(face_path)
