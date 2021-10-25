from PIL import Image
from os import listdir,rename
from os.path import isfile, join
NAME = 'UQ Holder\ '[:-1]

Ufiles = [f for f in listdir(NAME) if isfile(join(NAME, f))]



for i in Ufiles:
        for Type in ('.jpg','.png'):
                if i[1] == '_' and len(i)-4 == 3 and i[-4:]==Type: #7_5.jpg to 07__05.jpg
                        source = NAME+i
                        temp = '0'+i[:-5]+'_0'+i[-5]
                        dest = NAME+temp+Type
                        rename(source, dest)
                        #print(temp)
                elif i[2] == '_' and len(i)-4 == 4 and i[-4:]==Type: #10_5.jpg to 10__05.jpg
                        #print(i)
                        source = NAME+i
                        temp = i[:2]+'__0'+i[-5]
                        dest = NAME+temp+Type
                        rename(source, dest)
                        #print(temp)
                elif i[1] == '_' and len(i)-4 == 5 and i[-4:]==Type: #1_10.jpg to 01__10.jpg
                        #print(i)
                        source = NAME+i
                        temp = '0'+i[0]+'_'+i[:-4]
                        dest = NAME+temp+Type
                        rename(source, dest)
                        #print(temp)
                elif i[2] == '_' and len(i)-4 == 5 and i[-4:]==Type: #10_10.jpg to 10__10.jpg
                        #print(i)
                        source = NAME+i
                        temp = i[:2]+'__'+i[3:-4]
                        dest = NAME+temp+Type
                        rename(source, dest)
                        #print(temp)
                
#print(files) 

total = len(Ufiles)
out = []
count = 1
print(Ufiles)

for i in Ufiles:
        if i != 'desktop.ini':
                loc = NAME+i
                temp = Image.open(loc)
                
                out.append(temp.convert('RGB'))
                if count%10 ==0:
                        print(count,' done out of a total of :',total)
                count+=1
print('generating PDF')
out[0].save('output.pdf',save_all=True, append_images=out[1:])

