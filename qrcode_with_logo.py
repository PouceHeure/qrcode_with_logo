import pyqrcode
from PIL import Image

LOGO_FILE = "logo/test_transparent.png"
LOGO_PERCENT_SIZE = 0.4
LOGO_BACKGROUND_COLOR = None #(255,255,255)
LOGO_BACKGROUND_PADDING = 0.10

QRCODE_CONTENT = "https://github.com/PouceHeure/qrcode_with_logo/"
QRCODE_FILE_SAVE = "demo/demo_transparent_without_bg.png"
QRCODE_QUITE_ZONE = 1
QRCODE_SCALE = 10
QRCODE_COLOR_BG = (255,255,255)
QRCODE_COLOR_CONTENT = (0,200,120)

if __name__=="__main__":
    # generate Qrcode image
    url = pyqrcode.QRCode(QRCODE_CONTENT,error = 'H')
    url.png(QRCODE_FILE_SAVE,scale=QRCODE_SCALE,
                              quiet_zone=QRCODE_QUITE_ZONE,
                              background=QRCODE_COLOR_BG,
                              module_color=QRCODE_COLOR_CONTENT)
    
    # load qrcode image as Pil object
    im_qrcode = Image.open(QRCODE_FILE_SAVE)
    im_qrcode = im_qrcode.convert("RGBA")
    # load logo image
    im_logo = Image.open(LOGO_FILE)
    im_logo = im_logo.convert('RGBA')

    # edit logo image
    w_logo, h_logo = im_logo.size
    if(LOGO_BACKGROUND_COLOR != None):
        # add padding
        padding_w, padding_h = int(w_logo*LOGO_BACKGROUND_PADDING), int(h_logo*LOGO_BACKGROUND_PADDING)
        size_with_padding = (w_logo + 2*padding_w, h_logo + 2*padding_h)
        # create bg image with color given
        im_logo_with_bg = Image.new("RGBA", size_with_padding, LOGO_BACKGROUND_COLOR)
        im_logo_with_bg.paste(im_logo, (padding_w, padding_h), im_logo)
        # replace pil object by the new one with bg
        im_logo = im_logo_with_bg

    # resize logo image
    w_qrcode,h_qrcode = im_qrcode.size
    new_w_logo, new_h_logo = (int(w_logo*LOGO_PERCENT_SIZE),int(h_logo*LOGO_PERCENT_SIZE))
    im_logo = im_logo.resize((new_w_logo, new_h_logo))
    
    # paste logo image on qrcode image
    x_paste, y_paste = (int(w_qrcode//2 - new_w_logo//2),int(h_qrcode//2 - new_h_logo//2))
    im_qrcode.paste(im_logo,(x_paste, y_paste),mask=im_logo)
    im_qrcode.save(QRCODE_FILE_SAVE)