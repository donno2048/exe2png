from PIL.Image import fromarray, open as open_image
from numpy import frombuffer, uint8, pad, array
def encode(height, in_file, out_file, color_mode=False):
    colors = 1 + 2 * color_mode
    data = frombuffer(open(in_file, "rb").read(), dtype=uint8)
    data = pad(data, (0, height * colors - len(data) % (colors * height)))
    fromarray(data.reshape((height, len(data) // (colors * height), colors)[:2 + color_mode]), mode="RGB" if color_mode else "L").save(out_file)
def decode(in_file, out_file, color_mode=False):
    colors = 1 + 2 * color_mode
    data = array(open_image(in_file))
    open(out_file, "wb").write(data.reshape((colors * data.shape[0] * data.shape[1], 1)).tobytes().rstrip(b'\0'))