# Mona Sans

[Download Mona Sans](https://github.com/github/mona-sans/releases/latest) • [Typeface microsite](https://github.com/mona-sans) ↗️

A strong and versatile typeface, designed together with [Degarism](https://degarism.com/) and inspired by industrial-era grotesques. Mona Sans works well across product, web, and print. Made to work well together with  Mona Sans's sidekick, [Hubot Sans](https://github.com/github/hubot-sans).

Mona Sans is a [variable font](https://web.dev/variable-fonts/). Variable fonts enable different variations of a typeface to be incorporated into one single file, and are supported by all major browsers, allowing for performance benefits and granular design control of the typeface's weight, width, and slant.

![mona-sans](https://user-images.githubusercontent.com/99746865/200648883-dbd47e9a-9d95-483e-aef6-1bfa602eb942.png)

## Usage

For web, we recommend using `Mona Sans.woff2`. Define the font with a `@font-face` rule, set its **weight** and **stretch** ranges, and use it:

```css
@font-face {
  font-family: 'Mona Sans';
  src:
    url('Mona-Sans.woff2') format('woff2 supports variations'),
    url('Mona-Sans.woff2') format('woff2-variations');
  font-weight: 200 900;
  font-stretch: 75% 125%;
}

html {
  font-family: 'Mona Sans';
}
```

To reduce [CLS](https://web.dev/cls/), you can preload the font in the `head` of your document:

```html
<link rel="preload" href="Mona-Sans.woff2" as="font" type="font/woff2" crossorigin>
```

## Styles
| Style Name | Italic Name | Weight | Width |
| --- | --- | --- | --- |
| UltraLight Narrow | UltraLight Narrow Italic | 200 | 75 |
| Light Narrow | Light Narrow Italic | 300 | 75 |
| Regular Narrow | Regular Narrow Italic | 400 | 75 |
| Medium Narrow | Medium Narrow Italic | 500 | 75 |
| SemiBold Narrow | SemiBold Narrow Italic | 600 | 75 |
| Bold Narrow | Bold Narrow Italic | 700 | 75 |
| ExtraBold Narrow | ExtraBold Narrow Italic | 800 | 75 |
| Black Narrow | Black Narrow Italic | 900 | 75 |
| UltraLight | UltraLight Italic | 200 | 100 |
| Light | Light Italic | 300 | 100 |
| Regular | Regular Italic | 400 | 100 |
| Medium | Medium Italic | 500 | 100 |
| SemiBold | SemiBold Italic | 600 | 100 |
| Bold | Bold Italic | 700 | 100 |
| ExtraBold | ExtraBold Italic | 800 | 100 |
| Black | Black Italic | 900 | 100 |
| UltraLight Wide | UltraLight Wide Italic | 200 | 125 |
| Light Wide | Light Wide Italic | 300 | 125 |
| Regular Wide | Regular Wide Italic | 400 | 125 |
| Medium Wide | Medium Wide Italic | 500 | 125 |
| SemiBold Wide | SemiBold Wide Italic | 600 | 125 |
| Bold Wide | Bold Wide Italic | 700 | 125 |
| ExtraBold Wide | ExtraBold Wide Italic | 800 | 125 |
| Black Wide | Black Wide Italic | 900 | 125 |

## Stylistic sets

Mona Sans has eight stylistic sets:

| Set | Description | Example |
| --- | --- | --- | 
| ss01 | Square diacritical marks | ![ss01](https://github.com/user-attachments/assets/18fa3132-6839-4ef9-afd9-c75a082899ef) |
| ss02 | Wide uppercase I | ![ss02](https://github.com/user-attachments/assets/a0de7f9c-f9c0-4583-ac32-a10d25a54328) |
| ss03 | Lowercase l with tail | ![ss03](https://github.com/user-attachments/assets/8594effd-0528-4af9-8c58-0dfba66b2b45) |
| ss04 | Lowercase l with top serif | ![ss04](https://github.com/user-attachments/assets/7c7610a9-947e-45d5-80fc-71849a257d82) |
| ss05 | Double-storey a | ![ss05](https://github.com/user-attachments/assets/d31a11b8-1809-4a34-bbcb-b8b7057ddef0) |
| ss06 | Double-storey g | ![ss06](https://github.com/user-attachments/assets/ca8bef04-68d8-4c36-bfa6-8313d5642a9d) |
| ss07 | Round G | ![ss07](https://github.com/user-attachments/assets/4d5fb045-df90-4dc7-8dbb-3f2a271477df) |
| ss08 | Tabular zero with straight bar | ![ss08](https://github.com/user-attachments/assets/6c54f0eb-0054-4876-a366-1c00d955b89b) |

When using Mona Sans on the web, you can control each stylistic set with the syntax `"ssXX" on/off`, e.g.:

```css
html {
  font-family: 'Mona Sans';
  font-feature-settings: "ss01" on, "ss03" on, "ss05" on; /* Turns on square diacritical marks, small letter L distinct from capital I, and alternative small letter g */
}
```

## Ligatures

Mona Sans comes with seven ligatures:

| Ligature | Example |
| --- | --- | 
| ff | ![ff](https://github.com/user-attachments/assets/257cf188-808c-4bfc-9087-61dedf4c1e6f) | 
| ffi | ![ffi](https://github.com/user-attachments/assets/f7c92ef1-90ef-4bec-9f00-1a4c522e1c73) | 
| fy | ![fy](https://github.com/user-attachments/assets/232ead1c-09bd-4567-b17f-9d2651edef63) | 
| fi | ![fi](https://github.com/user-attachments/assets/2cd901e4-f077-449d-ad6a-eec683b7f402) | 
| fl | ![fl](https://github.com/user-attachments/assets/c0591522-f273-48fd-a0f5-0e2c77df6e9a) | 
| ti | ![ti](https://github.com/user-attachments/assets/556aab9f-e8f5-40dd-b8d2-70903d0cab65) | 
| tt | ![tt](https://github.com/user-attachments/assets/d0392c30-2b8c-4646-b578-0ae66a328505) | 

## License
Mona Sans is licensed under the [SIL Open Font License v1.1](https://scripts.sil.org/OFL).
