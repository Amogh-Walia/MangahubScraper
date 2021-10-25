from bs4 import *
import requests
import os



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}

try:
    os.mkdir(NAME)

# if folder exists with that name, ask another name
except:
    pass




  
# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(base,chapter,folder_name):
    
    # intitial count is zero
    count = 0
    # print total images found in URL
    go = True
    print('Chapter :',chapter)
    while go:
        url1 = base+str(chapter)+"/"+str(count+1)+".jpg"
        url2 = base+str(chapter)+"/"+str(count+1)+".png"
        request1 = requests.get(url1, headers=headers)
        
        if request1.status_code == 200:
            
            go = True
            with open(f"{folder_name}/{chapter}_{count+1}.jpg", "wb+") as f:
                f.write(request1.content)
            count+=1

        else:
            request2 = requests.get(url2, headers=headers)
            if request2.status_code == 200:
                go = True
                with open(f"{folder_name}/{chapter}_{count+1}.png", "wb+") as f:
                    f.write(request2.content)
                count+=1           
            else:
                go = False
            
    print(f"Total {count} Images Found and Downloaded!")
    if count == 0:
        with open("MISSING", "a") as f:
            f.write(chapter)
    # checking if images is not zero
        # There might be possible, that all
        # images not download
        # if all images download
  
# MAIN FUNCTION START
def main():
    print("Enter the img source Link (of the format: https://img.mghubcdn.com/file/imghub/MANGA_NAME/)")
    base = input()
    print("Enter the starting and the ending Chapters to scrap (of Format: start <space> end)")
    chapter,end = input().split()
    print("Enter the folder name:")
    NAME = input()
    while chapter != end+1 :
        download_images(base,chapter,NAME)
        chapter+=1
        
      

    
  

main()
