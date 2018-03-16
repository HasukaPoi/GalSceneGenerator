from PIL import Image, ImageDraw, ImageFont

def gen(image="default/udx.png",
        filt="default/filter50.png",
        text0=None,text1=None,text2=None,text3=None,
        ttf="default/SourceHanSans-Medium.otf"):
    baseIm=Image.open(image).convert('RGBA') #如果是JPG的话必须转RGBA
    r,g,b,ab=baseIm.split() #分离出Alpha通道备用
    filterIm=Image.open(filt) #显然是PNG
    r,g,b,a=filterIm.split() #分离对话框背景通道
    baseIm.paste(filterIm,(246,551),mask=a) #用alpha通道作为蒙版把图像贴上去，但依然会复写原图的alpha通道
    r,g,b,a=baseIm.split()
    baseIm=Image.merge("RGBA",(r,g,b,ab)) #重组原图
    txtLayer=Image.new('RGBA',baseIm.size,(0,0,0,0)) #创建一个和基底等尺寸的RGBA
    font=ImageFont.truetype(ttf,24) #读字体

    if text0==text1==text2==text3==None:
        text0="您没有输入任何文本参数，因此自动生成本示例"
        text1="这是一个类GalGame场景生成示例by Hasuka"
        text2="暂时无法处理自动换行所以请分行输入，每行最多28个汉字。"
        text3="如果留空说话人名字，将不产生两侧的括号。"
    
    d=ImageDraw.Draw(txtLayer) #新建一个绘图对象
    if text0!="":
        d.text((251,521),'【'+text0+'】',font=font,fill=(255,255,255,255)) #写说话人名

    d.text((295,562),text1,font=font,fill=(255,255,255,255)) #写第1行
    d.text((295,602),text2,font=font,fill=(255,255,255,255)) #写第2行
    d.text((295,642),text3,font=font,fill=(255,255,255,255)) #写第3行
    baseIm=Image.alpha_composite(baseIm,txtLayer) #合并图层
    
    #baseIm.show()
    baseIm.save("out.png","PNG") #保存文件
	

if __name__=='__main__':
    gen()
