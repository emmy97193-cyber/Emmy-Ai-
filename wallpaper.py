from PIL import Image
def make_wallpapers(im):
 w,h=im.size
 # home square crop
 s=min(w,h)
 l=(w-s)//2
 t=(h-s)//2
 home=im.crop((l,t,l+s,t+s))
 home=home.resize((1080,1080))
 # lock with dark top for clock
 lock=Image.new("RGBA",(1080,1920),(5,20,10,255))
 im2=im.copy()
 im2.thumbnail((1080,1080))
 x=(1080-im2.width)//2
 y=400
 lock.alpha_composite(im2,(x,y))
 return home,lock
