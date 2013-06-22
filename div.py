import Image, sys
im = Image.open(sys.argv[1])
pix = im.load()
size = im.size

def to_argb(argb):
    return "".join(map(chr, argb)).encode('hex')

def to_rgb(rgb):
    return rgb[0:6]

def to_opacity(a):
    return int(a[6:8], 16)/255.0
print "<style>#a{float:left;height:1px;width:1px}</style>"

print "<div style=\"width:"+str(size[0])+"px;height:"+str(size[1])+"px;left:0;top:0;position:absolute\">"
for x in range(0, size[1]):
    for y in range(0, size[0]):
        value = to_argb(pix[y,x])
        sys.stdout.write("<div id=a style=background-color:#"+to_rgb(value)+";")
        if (len(value) == 8):
            sys.stdout.write("opacity:"+str(to_opacity(value))+";")
        sys.stdout.write("></div>")
print "</div>"