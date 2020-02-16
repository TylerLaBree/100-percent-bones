import seaborn as sb

pal = sb.color_palette('coolwarm')
print(pal.as_hex())

colors = ['#6788ee', '#9abbff', '#c9d7f0', '#edd1c2', '#f7a889', '#e26952','bd2100']
sb.set_palette(sb.color_palette(colors))

