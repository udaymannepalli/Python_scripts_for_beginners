f = open('image.jpg', 'rb')
f1 = open('new_image.jpg', 'wb')
for i in f:
    f1.write(i)



