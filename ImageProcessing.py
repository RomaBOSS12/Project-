import ImageWriter 
import cv2
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import cv2
import np 
from PIL import Image
from PIL import Image, ImageFont, ImageDraw
#pic = ImageWriter.loadPicture("p3.bmp")
# Here is our helper function that turns the colorful picture into white&black 


class ImageP():
    def __init__(self, mypic, ext, state):
        self.state = state 
        self.ext = ext 
        self.mypic = mypic 
        #print("picture is loaded", mypic)

        
        self.ratio =  (450) // self.ext 
        print("ratiooooooooooooooooooooo", self.ratio) 

        im = Image.open(mypic) 
        # resize the image accodring to the size of the widget
        im_resize = im.resize((450 - (self.ext//5) * self.ratio, 450 - (self.ext//5) * self.ratio)) 

        # self.ratio2 =  (450 - (self.ext//5) * self.ratio) // self.ext  
        # print("ratiooooooooooooooooooooo", self.ratio2)

        # save the photo in the batch folder
        Resized = im_resize.save(mypic)  

        self.convertBlackWhite(mypic) 


        
    def convertBlackWhite(self, mypic): 
        self.mypic = mypic 
        self.Batch = self.mypic
        self.pic = ImageWriter.loadPicture(self.mypic)
        
        print("picture is loaded") 
        # Get the width and height (in pixels) of the image 
        self.rows = ImageWriter.getHeight(self.pic)
        self.columns = ImageWriter.getWidth(self.pic)
        backgr = 0
        # Iterate over every pixel
        for i in range(0,self.rows): 

            c = ImageWriter.getColor(self.pic,0,i)
            # Asking if the color is brighter than darker
            backgr += sum(c)/(3 *self.rows) 
                
        
        
        
        
        # Iterate over every pixel
        for i in range(0,self.rows):
            for j in range(0,self.columns): 
                c = ImageWriter.getColor(self.pic,j,i)
                if backgr <= 127: 
                    # Asking if the color is brighter than darker
                    if sum(c)/3 >= 20:
                        # if yes turn it white, otherwise, turn it into black
                        ImageWriter.setColor(self.pic,j,i,[0,0,0])
                    else:
                        ImageWriter.setColor(self.pic,j,i,[255,255,255])
                else: 
                    # Asking if the color is brighter than darker
                    if sum(c)/3 >= 100:
                        # if yes turn it white, otherwise, turn it into black
                        ImageWriter.setColor(self.pic,j,i,[255,255,255])
                    else:
                        ImageWriter.setColor(self.pic,j,i,[0,0,0])
        # Update the picture with changes
        #ImageWriter.updatePicture(self.pic) 
    
        #ImageWriter.closeWindow(self.pic) 
        self.REPIXEL()

    
    
    def REPIXEL(self):
        avg = [0,0,0]
        #ImageWriter.showPicture(self.pic) 
        


        # im = Image.open(self.Batch)
        # # resize the image accodring to the size of the widget
        # im_resize = im.resize((450 - 5 * self.ratio, 450 - 5 * self.ratio))

        # # save the photo in the batch folder
        # Resized = im_resize.save(self.Batch) 
        
        # im = Image.open(self.Batch)
        # width, height = im.size
        # new_width = width + 5 * self.ratio 
        # new_height = height + 5 * self.ratio 
        # result = Image.new(im.mode, (new_width, new_height), (255,255,255))
        # result.paste(im, (0, 0))
        # result.save(self.Batch, quality = 500)



        for i in range(0,self.rows-self.ratio+1,self.ratio):
            for j in range(0,self.columns-self.ratio+1, self.ratio):  
                for x in range(0,self.ratio):
                    for y in range(0,self.ratio):  
                        c = ImageWriter.getColor(self.pic,j+y,i+x) 
                        #print("before", avg[0], c[0]) 
                        avg[0] += c[0]/(self.ratio**2)
                        #print("oops")
                        avg[1] += c[1]/(self.ratio**2)
                        avg[2] += c[2]/(self.ratio**2)
                       
                if sum(avg) > 500:
                    for x in range(0,self.ratio):
                        for y in range(0,self.ratio):
                            ImageWriter.setColor(self.pic,j+y,i+x,[255,255,255])
                else: 
                    for x in range(0,self.ratio):
                        for y in range(0,self.ratio):
                            ImageWriter.setColor(self.pic,j+y,i+x,[0,0,0])
                avg = [0,0,0]


        ImageWriter.savePicture(self.pic, 'Batch/re' + self.Batch[13:])
        #print("aaaaaaaaaaaaaaaaa", self.pic)   
        print("AAAAAAAAAAAAAAAAA", self.Batch)  

        #ImageWriter.closeWindow(self.pic) 
        if self.state == True: 
            listrow = [] 
            listcol = []
            for i in range(0,self.rows-self.ratio+1,self.ratio):
                for j in range(0,self.columns-self.ratio+1, self.ratio):
                    c = ImageWriter.getColor(self.pic,j,i)
                    if c == [0,0,0]:
                        listrow += [i]
                        break 
            for j in range(0,self.columns-self.ratio+1, self.ratio):
                for i in range(0,self.rows-self.ratio+1,self.ratio):
                    c = ImageWriter.getColor(self.pic,j,i)
                    if c == [0,0,0]:
                        listcol += [j] 
                        break 
            topx = listrow[0] - 1
            bottomx = listrow[-1] + 1
            lefty = listcol[0] - 1
            righty = listcol[-1] + 1 
            maxdif = max([bottomx - topx, righty - lefty]) 

            img = cv2.imread('Batch/re' + self.Batch[13:])
            #print(img.shape) # Print image shape
            #cv2.imshow("original", img)
            
            # Cropping an image
            cropped_image = img[topx:topx + maxdif, lefty:lefty + maxdif] 
            
            # Display cropped image
            #cv2.imshow("cropped", cropped_image)
            
            # Save the cropped image
            cv2.imwrite('Batch/re' + self.Batch[13:], cropped_image)
            print("reached")

            img = cv2.imread('Batch/re' + self.Batch[13:])
            #cv2.imshow("image",img)
            
            #cv2.waitKey(10000) 
            
            

            im = Image.open('Batch/re' + self.Batch[13:]) 
            # resize the image accodring to the size of the widget
            im_resize = im.resize((450 - (self.ext//5) * self.ratio, 450 - (self.ext//5) * self.ratio)) 

            # self.ratio2 =  (450 - (self.ext//5) * self.ratio) // self.ext  
            # print("ratiooooooooooooooooooooo", self.ratio2)

            # save the photo in the batch folder
            Resized = im_resize.save('Batch/re' + self.Batch[13:])
            ForGUI = im_resize.save('Batch/GUI' + self.Batch[13:])

            #cv2.destroyAllWindows()
            
             
        #ImageWriter.updatePicture(self.pic)  
        #ImageWriter.cv2.waitKey(0)  
        
        
        im = Image.open('Batch/re' + self.Batch[13:])
        width, height = im.size
        new_width = width + (self.ext//5) * self.ratio 
        new_height = height + (self.ext//5) * self.ratio 
        result = Image.new(im.mode, (new_width, new_height), (255,255,255))
        result.paste(im, (0, 0))
        result.save('Batch/re' + self.Batch[13:], quality = 500)
            
        self.grid()
        
        # ImageWriter.closeWindow(self.pic) 
        # Batch = 'Batch/re' + self.mypic[13:]
        # print("What is next", self.mypic[13:])
        # ImageWriter.savePicture(self.pic, Batch)
        # print("aaaaaaaaaaaaaaaaa", self.pic) 
        # print("AAAAAAAAAAAAAAAAA", Batch)
        # return Batch  
        
    def grid(self): 
        GRID_SIZE = self.ratio

        img = cv2.imread('Batch/re' + self.Batch[13:])
        height, width, channel = img.shape

        for y in range(0, height - (self.ext//5)*self.ratio, GRID_SIZE):
            for x in range(0, width - (self.ext//5)*self.ratio, GRID_SIZE):
                # if x % 5 == 4 or y % 5 == 4: 
                #     cv2.rectangle(img, pt1=(x,y), pt2=(x+GRID_SIZE,y+GRID_SIZE), color=(0, 0, 0), thickness=3)
                # else:
                    cv2.rectangle(img, pt1=(x,y), pt2=(x+GRID_SIZE,y+GRID_SIZE), color=(0, 0, 0), thickness=1)
        for y in range(0, height - (self.ext//5)*self.ratio, GRID_SIZE):
            # if y % 5 == 4:     
            #     cv2.rectangle(img, pt1=(width-3*self.ratio,y), pt2=(width,y+GRID_SIZE), color=(0, 0, 0), thickness=3)
            # else: 
                cv2.rectangle(img, pt1=(width-(self.ext//5)*self.ratio,y), pt2=(width,y+GRID_SIZE), color=(0, 0, 0), thickness=1)

        for x in range(0, width - (self.ext//5)*self.ratio, GRID_SIZE):
            # if x % 5 == 4:   
            #     cv2.rectangle(img, pt1=(x,height - 3*self.ratio), pt2=(x + GRID_SIZE, height), color=(0, 0, 0), thickness=3)
            # else: 
                cv2.rectangle(img, pt1=(x,height - (self.ext//5)*self.ratio), pt2=(x + GRID_SIZE, height), color=(0, 0, 0), thickness=1)

        for y in range(0, height, (self.ext//5) * GRID_SIZE):
            for x in range(0, width, (self.ext//5) * GRID_SIZE):
                cv2.rectangle(img, pt1=(x,y), pt2=(x+(self.ext//5)*GRID_SIZE,y+(self.ext//5)*GRID_SIZE), color=(0, 0, 0), thickness=2)
        
        print("stops here")
        #cv2.imshow('Output', img)
        #key = cv2.waitKey(0) 

        
        
        #print("What is next", img, self.Batch)  
        cv2.imwrite('Batch/re' + self.Batch[13:], img)  
        #print("aaaaaaaaaaaaaaaaa", self.pic) 
        #print("AAAAAAAAAAAAAAAAA", self.Batch)
         

#************* Adding text on the image ******************************************************************************************
        # choose and open an image
        my_image = Image.open('Batch/re' + self.Batch[13:])  
        # Select the font
        title_font = ImageFont.truetype('Yagora.ttf', self.ratio) 


        #pic = ImageWriter.loadPicture('Batch/re' + self.Batch[13:]) 
        self.numRow = {}
        self.numPixels = 0
        self.breaks = []

        black = 0
        line = []
        grid = []

        for y in range(0, height-(self.ext//5)*self.ratio, GRID_SIZE):
            for x in range(0, width -(self.ext//5)*self.ratio, GRID_SIZE):    
                if ImageWriter.getColor(self.pic,x,y) == [0,0,0]:    
                    self.numPixels += 1
                    black = 1 
                else: 
                    black = 0
                    if self.numPixels != 0:    
                        self.breaks += [str(self.numPixels)]
                        self.numPixels = 0
                line += [black]
            grid+= [line] 
            line = []
            self.numRow[y] = self.breaks 
            self.breaks = [] 
            #print("the number of pixels in a row", self.numRow)  
        


        self.numPixels = 0
        self.numCol = {} 
        self.breaks = []
        for x in range(0, width-(self.ext//5)*self.ratio, GRID_SIZE):    
            for y in range(0, height-(self.ext//5)*self.ratio, GRID_SIZE):
                if ImageWriter.getColor(self.pic,x,y) == [0,0,0]:
                    self.numPixels += 1
                else: 
                    if self.numPixels != 0:    
                        self.breaks += [str(self.numPixels)]
                        self.numPixels = 0
            self.numCol[x] = self.breaks 
            self.breaks = [] 
            #print("the number of pixels in a column", self.numCol)  


        for y in self.numRow:
                # Write numbers 
                title_text = " ".join(self.numRow[y])   
                # Converting the image into editable format
                image_editable = ImageDraw.Draw(my_image)
                title_text = title_text.replace("\n", "")
                # render the image
                image_editable.text((width - (self.ext/6)*self.ratio,y), title_text, (0, 0, 0), font=title_font) 

        for x in self.numCol: 
                y = height - (self.ext/6)*self.ratio
                for i in self.numCol[x]:
                    # Write numbers 
                    title_text = str(i) 
                    # Converting the image into editable format
                    image_editable = ImageDraw.Draw(my_image)
                    title_text = title_text.replace("\n", "")
                    # render the image
                    image_editable.text((x, y), title_text, (0, 0, 0), font=title_font)
                    y += self.ratio
        print("it went through numbering")

        # save the result
        my_image.save('Batch/re' + self.Batch[13:])  

        #my_image.show()
        return 'Batch/re' + self.Batch[13:] 



    
    # def REPIXEL(self):
    #     avg = [0,0,0]
    #     ImageWriter.showPicture(self.pic) 
    #     ratio =  self.rows // self.ext 
    #     for i in range(0,self.rows,ratio):
    #         for j in range(0,self.columns, ratio):  
    #             for x in range(0,ratio):
    #                 for y in range(0,ratio):  
    #                     c = ImageWriter.getColor(self.pic,j+y,i+x) 
    #                     avg[0] += c[0]/(ratio**2)
    #                     avg[1] += c[1]/(ratio**2)
    #                     avg[2] += c[2]/(ratio**2)
    #             for x in range(0,ratio):
    #                 for y in range(0,ratio):
    #                     ImageWriter.setColor(self.pic,j+y,i+x,avg)
    #             avg = [0,0,0]
    #     ImageWriter.updatePicture(self.pic) 
    #     ImageWriter.cv2.waitKey(0)
    #     #ImageWriter.closeWindow(self.pic) 
    #     Batch = 'Batch/re' + self.mypic[13:]
    #     print("What is next", self.mypic[13:])
    #     ImageWriter.savePicture(self.pic, Batch)
    #     print("aaaaaaaaaaaaaaaaa", self.pic) 
    #     print("AAAAAAAAAAAAAAAAA", Batch)
    #     return Batch   

    # def crop_square(img, size, interpolation=cv2.INTER_AREA):
    #     img = cv2.imread(img) 
    #     h, w = img.shape[:2]
    #     min_size = np.amin([h,w])

    # # #     # Centralize and crop
    #     crop_img = img[int(h/2-min_size/2):int(h/2+min_size/2), int(w/2-min_size/2):int(w/2+min_size/2)]
    #     resized = cv2.resize(crop_img, (size, size), interpolation=interpolation)
    #     #cv2.imshow('hvjhvh',resized)
    #     #cv2.waitKey(0)
    #     return resized
     

    
    # def add_margin(pil_img, top, right, bottom, left, color):
    #     width, height = pil_img.size
    #     new_width = width + right + left
    #     new_height = height + top + bottom
    #     result = Image.new(pil_img.mode, (new_width, new_height), color)
    #     result.paste(pil_img, (left, top))
    #     return result
    # im = Image.open('Plane.jpg')
    # im_new = add_margin(im, 0, 20, 20, 0, (255, 255, 255))
    # im_new.save('paddedPlane.jpg', quality=95)

#App = ImageP("Batch/resizedkitty.jpg", 60) 