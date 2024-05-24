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

Mona Sans has five stylistic sets:

| Set | Description | Examples |
| --- | --- | --- | 
| ss01 | Square diacritical marks (i, j, ä, etc; defaults to round) | tbd |
| ss02 | Small latin letter L distinct from capital I (option 1) | tbd |
| ss03 | Small latin letter L distinct from capital I (option 2) | tbd |
| ss04 | Alternative (open) small letter a | tbd |
| ss05 | Alternative small letter g | tbd |

When using Mona Sans on the web, you can control each stylistic set with the syntax `"ssXX" on/off`, e.g.:

```css
html {
  font-family: 'Mona Sans';
  font-feature-settings: "ss01" on, "ss03" on, "ss05" on; /* Turns on square diacritical marks, small letter L distinct from capital I, and alternative small letter g */
}
```

## Ligatures

Mona Sans comes with seven ligatures:

| Character combination | Examples |
| --- | --- | 
| ff | tbd | 
| ffi | tbd | 
| fy | tbd | 
| fi | tbd | 
| fl | tbd | 
| ti | tbd | 
| tt | tbd | 

## License
Mona Sans is licensed under the [SIL Open Font License v1.1](https://scripts.sil.org/OFL).
