from instapy_cli import client


username = 'jubara_abdallah' #your username

password = '**********' #your password 

image = 'Hi_instagram.png' #here you can put the image directory

text = 'Here you can put your caption for the post' + '\r\n' + 'you can also put your hashtags #pythondeveloper #webdeveloper'


with client(username, password) as cli:
    cli.upload(image, text)
