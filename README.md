# opencv-python-vtube
This is by no means a replacement of any professional vtubing software. It takes up a bit too much cpu in my opinion.
However, it is still a viable option for those with higher end computers. 

Please refer to [my youtube](https://www.youtube.com/channel/UCbcNkZ6JhmzCwLJTwe5h4zg/) for the making process as well as how to setup OBS for it.

Feel free to modify the design of the avatar and the eyes as you see fit.

## modifying the code (avatar body)
The code below refers to placement of the avatar.

`back[int(hei/2)-240:int(hei/2)+240, fx-150:fx+150] = body`

when modifying `int(hei/2)-240:int(hei/2)+240`, please keep in mind that the difference of the two expressions should equal the **height** of the body's image

when modifying `fx-150:fx+150`, please keep in mind that the difference of the two expressions should equal the **width** of the body's image

## modifying the code (avatar eyes)

The code below refers to placement of the avatar.

`back[int(hei/2)-130:int(hei/2)-70, fx-64:fx+61] = eye_type`

when modifying `int(hei/2)-130:int(hei/2)-70`, please keep in mind that the difference of the two expressions should equal the **height** of the eyes' image

when modifying `fx-64:fx+61`, please keep in mind that the difference of the two expressions should equal the **width** of the eyes' image
