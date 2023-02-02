import PIL.Image as plim
from PIL import ImageFont, ImageDraw
import moviepy.editor as mpy
from moviepy.video.io.bindings import PIL_to_npimage

# https://gist.github.com/Zulko/06f49f075fd00e99b4e6

fontname = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.FreeTypeFont(fontname, 100)
size=(320,200)

colours = {"red": (255,0,0), "yellow": (128,128,0), "green": (0,255,0), "blue": (0,0,255)}
def makeframe(t):
    W, H = size
    im = plim.new('RGB',size=size,color=colour_tuple)
    draw = ImageDraw.Draw(im)
    message="%.02f"%(t)
    _, _, w, h = draw.textbbox((0, 0), message, font=font)
    draw.text(((W-w)/2, (H-h)/2), message ,font=font)
    return PIL_to_npimage(im)

for colour_name, colour_tuple in colours.items():
    clip = mpy.VideoClip(makeframe, duration=10)
    clip.write_videofile(f"timer_{colour_name}.mp4", fps=20)