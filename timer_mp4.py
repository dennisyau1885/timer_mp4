import PIL.Image as plim
from PIL import ImageFont, ImageDraw
import moviepy.editor as mpy
from moviepy.video.io.bindings import PIL_to_npimage

# https://gist.github.com/Zulko/06f49f075fd00e99b4e6

fontname = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.FreeTypeFont(fontname, 24)

colours = {"red": (255,0,0), "yellow": (128,128,0), "green": (0,255,0), "blue": (0,0,255)}
def makeframe(t):
    im = plim.new('RGB',(80,50),color=colour_tuple)
    draw = ImageDraw.Draw(im)
    draw.text((30, 20), "%.02f"%(t))
    return PIL_to_npimage(im)

for colour_name, colour_tuple in colours.items():
    clip = mpy.VideoClip(makeframe, duration=10)
    clip.write_videofile(f"timer_{colour_name}.mp4", fps=25)