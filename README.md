# Mona Sans

[Download Mona Sans](https://github.com/github/mona-sans/releases/latest) • [Typeface microsite](https://github.com/mona-sans) ↗️

A strong and versatile typeface, designed together with [Degarism](https://degarism.com/) and inspired by industrial-era grotesques. Mona Sans works well across product, web, and print. Made to work well together with  Mona Sans's sidekick, [Hubot Sans](https://github.com/github/hubot-sans).

Mona Sans is a [variable font](https://web.dev/variable-fonts/). Variable fonts enable different variations of a typeface to be incorporated into one single file, and are supported by all major browsers, allowing for performance benefits and granular design control of the typeface's weight, width, and slant.

![mona-sans](https://github.com/user-attachments/assets/3d9667f5-30ad-4b95-bc8a-58e38767187c)

## Variable font usage

The design space is large, so we've split the font up into a few variable fonts.

If you want to access the whole design space, use `MonaSansVF[wdth,wght,opsz,ital]`. On the web, you can utilize points on that space like this:

```css
@font-face {
  font-family: 'Mona Sans VF';
  src:
    url('MonaSansVF[wdth,wght,opsz,ital].woff2') format('woff2 supports variations'),
    url('MonaSansVF[wdth,wght,opsz,ital].woff2') format('woff2-variations');
  font-weight: 200 900;
  font-stretch: 75% 125%;
  font-optical-sizing: auto;
}

html {
  font-family: 'Mona Sans VF';
}
```

Mona Sans includes an optical size axis (`opsz`) that automatically adjusts the font's design for optimal readability at different sizes. The optical size range spans from 1 to 100, where smaller values (1-20) are optimized for body text with improved readability, while larger values (21-100) are designed for display use with refined details and tighter spacing. When `font-optical-sizing: auto` is set, browsers will automatically select the appropriate optical size based on the font size, or you can manually control it using `font-variation-settings: "opsz" [value]`. That looks like this:

```css
.heading {
  font-variation-settings: "wght" 700, "wdth" 125, "opsz" 72; /* Bold, Expanded, Display size */
}

.body-text {
  font-variation-settings: "wght" 400, "wdth" 100, "opsz" 12; /* Regular, Normal width, Text size */
}
```

To reduce [CLS](https://web.dev/cls/), you can preload the font in the `head` of your document:

```html
<link rel="preload" href="MonaSansVF[wdth,wght,opsz,ital].woff2" as="font" type="font/woff2" crossorigin>
```

## Stylistic sets

Mona Sans has ten stylistic sets:

| Set | Description | Example |
| --- | --- | --- | 
| ss01 | Square diacritical marks | <img src="https://github.com/user-attachments/assets/c8be9ca8-8d7a-46d5-843a-7dfc0ca9a171" width="400"> |
| ss02 | Wide uppercase I | <img src="https://github.com/user-attachments/assets/f971d907-c8a5-4fbf-ac75-bf3411a00f57" width="400"> |
| ss03 | Lowercase l with tail | <img src="https://github.com/user-attachments/assets/e20dd37c-f7ba-4964-8888-dd679ed7d3fc" width="400"> |
| ss04 | Lowercase l with top serif | <img src="https://github.com/user-attachments/assets/6aa71393-642e-4989-843d-4c2b9d6b5a1c" width="400"> |
| ss05 | Double-storey a | <img src="https://github.com/user-attachments/assets/c411d743-0bb8-4f15-ad30-769c6d5b83d5" width="400"> |
| ss06 | Double-storey g | <img src="https://github.com/user-attachments/assets/cc640587-6505-49a9-836c-a4a091b0a4cb" width="400"> |
| ss07 | Square G | <img src="https://github.com/user-attachments/assets/2c973b98-8398-4ab2-bb74-45980de799ea" width="400"> |
| ss08 | Tabular zero with straight bar | <img src="https://github.com/user-attachments/assets/1efe404b-ca17-4dbb-877e-47a7080d2785" width="400"> |
| ss09 | Q with diagonal arm | <img src="https://github.com/user-attachments/assets/5f7f28e7-d325-496a-8362-21d7a71b362a" width="400"> |
| ss10 | J with bowl | <img src="https://github.com/user-attachments/assets/5a0776c8-8acf-41ad-ba23-e26515bc1f8e" width="400"> |

When using Mona Sans on the web, you can control each stylistic set with the syntax `"ssXX" on/off`. If you wanted square diacritical marks, small letter L distinct from capital I, and alternative small letter g it would look like this:

```css
html {
  font-family: 'Mona Sans VF';
  font-feature-settings: "ss01" on, "ss03" on, "ss05" on;
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

## Mona Sans Styles

With the newly added monospace, display, and display italic styles, Mona Sans' design space now spans 168 instances. Below is a map for the whole space. Style entries with a hyphen are elidable, meaning they are the default and have no name.

| Axes | Mapping | Style name |
| --- | --- | --- |
| Weight (wght) | 200 | ExtraLight |
|  | 300 | Light |
| - | 400 | Regular |
| - | 500 | Medium |
| - | 600 | SemiBold |
| - | 700 | Bold |
| - | 800 | ExtraBold |
| - | 900 | Black |
| Width (wdth) | 75 | Condensed |
| - | 87.5 | SemiCondensed |
| - | 100 | - |
| - | 112.5 | SemiExpanded |
| - | 125 | Expanded |
| Italic (ital) | 0 | Roman |
| - | 1 | Italic |
| Optical Size (opsz) | 20 | - |
| - | 72 | Display |


### Mona Sans Mono Styles

![mona-sans-mono](https://github.com/user-attachments/assets/c627ca73-a4c5-483a-b95d-cbe0b07f5a23)

| Family or Axes | Mapping | Styles |
| --- | --- | --- |
| Weight (wght) | 200 | ExtraLight |
| - | 300 | Light |
| - | 400 | Regular |
| - | 500 | Medium |
| - | 600 | SemiBold |
| - | 700 | Bold |
| - | 800 | ExtraBold |
| - | 900 | Black |
| Width (wdth) | 75 | Condensed |
| - | 87.5 | SemiCondensed |
| - | 100 | - |
| - | 112.5 | SemiExpanded |
| - | 125 | Expanded |

## License
Mona Sans is licensed under the [SIL Open Font License v1.1](https://scripts.sil.org/OFL).
