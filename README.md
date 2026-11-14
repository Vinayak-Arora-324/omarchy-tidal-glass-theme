# Tidal Glass

A dark theme for [Omarchy](https://omarchy.org). Neutral graphite windows, grey
selection instead of an accent colour, and four near-monochrome photographs of
cold water.

![Tidal Glass preview](preview.png)

## Install

On any Omarchy system, run:

```bash
omarchy theme install https://github.com/Vinayak-Arora-324/omarchy-tidal-glass-theme.git
```

Or open the Omarchy menu (`Super + Space`), go to **Install → Style →
Theme** and paste the URL above.

Omarchy clones the repo into `~/.config/omarchy/themes/tidal-glass` and applies
it straight away. After that it shows up in the theme switcher
(`Super + Ctrl + Shift + Space`), or you can set it by name:

```bash
omarchy theme set tidal-glass
```

### Update

```bash
omarchy theme update
```

This pulls the latest version of every theme you installed from git.

### Remove

```bash
omarchy theme remove tidal-glass
```

## Files

| File | What it does |
|------|--------------|
| `colors.toml` | The palette. Omarchy builds the terminal, editor, btop and app themes from it. |
| `shell.toml` | Menus, launcher, notifications and lock screen. |
| `hyprland.lua` | 1px borders, 11px corners, window shadow. |
| `icons.theme` | `Yaru-sage-dark` |
| `backgrounds/` | The wallpapers. |

### Corners and shadows

For safety, Omarchy skips any `*.lua` file in a theme installed from git, so
`hyprland.lua` is not loaded and windows keep the default corners and shadow.
Everything else still applies. If you want the rounded corners and shadow, read
[`hyprland.lua`](hyprland.lua) first (it only sets border, rounding and shadow
values), then turn the install into a local copy:

```bash
rm -rf ~/.config/omarchy/themes/tidal-glass/.git
omarchy theme set tidal-glass
```

A local copy no longer gets `omarchy theme update`. To update it later, run the
install command again, then repeat these two lines.

## Palette

| | | | |
|---|---|---|---|
| background | `#1e1e20` | foreground | `#dcdcde` |
| accent | `#a3a4a8` | selection | `#3a3a3d` |
| red | `#d9757a` | orange | `#cd9063` |
| yellow | `#cdb67e` | green | `#93ae8b` |
| cyan | `#72acae` | blue | `#7c9cc0` |
| magenta | `#a893b9` | brown | `#9a8d80` |

Window borders are a plain white hairline at low opacity, a little brighter on
the focused window.

## Wallpapers

All ten are from [Pexels](https://www.pexels.com/license/), cropped to 16:10
and desaturated to sit with the grey windows.

| File | Photographer |
|------|--------------|
| `1-dusk.webp` | [Gilles Quertier](https://www.pexels.com/photo/misty-rocks-on-the-sea-at-dusk-in-bretagne-33401396/) |
| `2-current.webp` | [Kris Møklebust](https://www.pexels.com/photo/dark-ocean-waves-with-reflective-light-patterns-34155535/) |
| `3-deep.webp` | [Eyüpcan Timur](https://www.pexels.com/photo/deep-dark-ocean-waves-at-twilight-33333829/) |
| `4-ripple.webp` | [Franco Garcia](https://www.pexels.com/photo/view-of-dark-blue-water-surface-18785204/) |
| `5-ridge.webp` | [Denis Tuev](https://www.pexels.com/photo/gloomy-sky-over-the-mountain-8991676/) |
| `6-crag.webp` | [Frank Cone](https://www.pexels.com/photo/landscape-of-rocky-snowcapped-mountains-in-fog-15737041/) |
| `7-twilight.webp` | [Cencial _](https://www.pexels.com/photo/misty-mountain-landscape-at-twilight-35774948/) |
| `8-fjord.webp` | [Erik Mclean](https://www.pexels.com/photo/lake-in-a-mountain-valley-in-fog-17491756/) |
| `9-hamlet.webp` | [Антон Залевський](https://www.pexels.com/photo/aerial-photography-of-mountain-village-14951947/) |
| `10-mist.webp` | [Amina B](https://www.pexels.com/photo/dense-fog-in-a-forest-10486451/) |
