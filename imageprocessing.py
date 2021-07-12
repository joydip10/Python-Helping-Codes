#installation of pillow library
#changing image extension
#resize image
#resize multiple images using for loop
#sharpness
#brightness
#color
#contrast
#ImageBlur, GaussianBlurr


from PIL import Image,ImageEnhance,ImageFilter
import os

img1=Image.open("new\download.jpg")
img1.save('new/dog.png')  #----->changing image extension
img1.show()

#MAX_SIZE=(250,250)
#img1.thumbnail(MAX_SIZE)
#img1.save('new/resized_dog.jpg')



#for item in os.listdir('new'):
#    if item.endswith('.jpg') or item.endswith('.png') or item.endswith('.cms'):
#        name,extension=item.split('.')
#        img2=Image.open('new\\'+f'{item}')
#        img2.thumbnail((250,250))
#        img2.save('new\\movies/resized'+f'{item}')  
 

''''
for item in os.listdir('new'):
    if item.endswith('.jpg') or item.endswith('.png') or item.endswith('.jpeg'):
        name,extension=os.path.splitext(item)
        img2=Image.open('new\\'+f'{item}')
        img2.thumbnail((250,250))
        img2.save('new\\movies/resized_'+f'{item}')
'''


'''
##Sharpness
img3=Image.open('new\\green.jpeg')
enhancer=ImageEnhance.Sharpness(img3)
enhancer.enhance(3).save('new\\greensharped.jpg')
#0---blurry
#1---original
#>2---sharped  
'''        

'''        
##Color
img3=Image.open('new\\green.jpeg')
enhancer=ImageEnhance.Color(img3)
enhancer.enhance(0).save('new\\b&w_green.png') #0 means black and white
enhancer.enhance(5).save('new\\moreenhancedincolor_green.png') # >1 means more added colors where 1 means original
Image.open('new\\b&w_green.png').show()
Image.open('new\\moreenhancedincolor_green.png').show()       
'''

'''
##Brightness 
img3=Image.open('new\\green.jpeg')
enhancer=ImageEnhance.Brightness(img3)
enhancer.enhance(0).save("new\\0brightness_green.jpg") #0 means dark
enhancer.enhance(3).save("new\\3brightness_green.jpg") #>1 means more bright
Image.open("new\\0brightness_green.jpg").show()
Image.open("new\\3brightness_green.jpg").show()
'''

'''
Same codes as above to change the contrast
'''


##Image Filter
img3=Image.open('new\\green.jpeg')
#ImageBlurr
img3.filter(ImageFilter.GaussianBlur(radius=4)).save('new\\green_filtered.jpg')
Image.open('new\\green_filtered.jpg').show()































        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
        
        