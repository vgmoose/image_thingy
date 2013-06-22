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

def fake_trans(a):
    p = a[3]/255.0
    return to_rgb(to_argb(( int((1-p)*255 + p*a[0]), int((1-p)*255 + p*a[1]), int((1-p)*255 + p*a[2] ))))

def get_color(a):
    b = to_argb(a)
    if (len(b)==6):
        return b
    else:
        return fake_trans(a)

print( "<style>td{height:1px;width:1px;padding:0px;}</style>")

print ("<table style='border-spacing:0px;left:0;top:0;position:absolute;'>")
for x in range(0, size[1]):
    print("<tr>")
    for y in range(0, size[0]):
        print("<td style='background-color:"+get_color(pix[y,x])+";'></td>")
    print("</tr>")
print "</table>"