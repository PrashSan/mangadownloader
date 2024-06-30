import requests

def download_manga(name,url):
     pass

def chapter_link(url):
    pass
    



def main():
    url=input("please enter the url of manga :")
    print("url" +url)

    chapters=chapter_link(url)
    for chapter in chapters:
        print(chapter +":" +chapters[chapter])
        ask=input("do you want to download it (y/n)")
        if ask=="y":
            download_manga(chapter,chapters[chapter])

        just checking 
        else:
            continue  

