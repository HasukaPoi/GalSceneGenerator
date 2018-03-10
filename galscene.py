from PIL import Image, ImageDraw, ImageFont

def gen(image="default/udx.png",filter="default/filter50.png",text="久ぶりにアキバに来たけど、立ててほどんと実感はない。",ttf="default/SourceHanSans-Medium.otf"):
    baseIm=Image.open(image).convert('RGBA') #如果是JPG的话必须转RGBA
    r,g,b,ab=baseIm.split() #分离出Alpha通道备用
    filterIm=Image.open(filter) #显然是PNG
    r,g,b,a=filterIm.split() #分离对话框背景通道
    baseIm.paste(filterIm,(246,551),mask=a) #用alpha通道作为蒙版把图像贴上去，这一步会复写原图的alpha通道
    r,g,b,a=baseIm.split()
    baseIm=Image.merge("RGBA",(r,g,b,ab)) #重组原图
    txtLayer=Image.new('RGBA',baseIm.size,(0,0,0,0)) #创建一个和基底等尺寸的RGBA
    font=ImageFont.truetype(ttf,24) #读字体
    d=ImageDraw.Draw(txtLayer) #新建一个绘图对象
    d.text((295,562),text,font=font,fill=(255,255,255,255)) #设置文字
    baseIm=Image.alpha_composite(baseIm,txtLayer) #写入行1
    # d.text((295,562),text,font=font,fill=(255,255,255,255))
    baseIm.save("out.png","PNG") #保存文件
	

if __name__=='__main__':
    gen()