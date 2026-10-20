from PIL import Image, ImageDraw

img = Image.open("your_robot.jpg").convert("RGBA")
W, H = img.size
draw = ImageDraw.Draw(img)

face_x, face_y = W*0.5, H*0.22
box_w, box_h = W*0.35, H*0.28

# Face box
draw.rectangle([face_x-box_w/2, face_y-box_h/2, face_x+box_w/2, face_y+box_h/2], outline=(168,85,247), width=3)

# Captions
draw.text((face_x-box_w/2-120, face_y-40), "NEURAL LINK: 99%", fill=(216,180,254))
draw.text((face_x-box_w/2-120, face_y-20), "FACE ID: VERIFIED", fill=(168,85,247))
draw.text((face_x+box_w/2+20, face_y-40), "SYSTEM: ONLINE", fill=(216,180,254))
draw.text((face_x+box_w/2+20, face_y-20), "AI BOOST: ACTIVE", fill=(168,85,247))
draw.text((W*0.5-40, H*0.45), "AI BOOST", fill=(216,180,254))

img.convert("RGB").save("robot_with_face_caption.jpg")
print("Done")
