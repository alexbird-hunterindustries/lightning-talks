# Technical Notes

## Blurring Images

```shell
magick image.jpg -gaussian-blur 0x16 -channel RGB -negate -evaluate Multiply 0.2 -negate +channel image-blurred.jpg
```

Adjust 0x16 to increase or decrease the blur (smaller == less blur)

Adjust 0.2 to increase or decrease the lightness (smaller == more white)
