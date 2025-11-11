import generate_qrcode

img = generate_qrcode.make("https://github.com/NbtKmy/ollamaintroduction")
type(img)  # qrcode.image.pil.PilImage
img.save("qrcode_repo.png")