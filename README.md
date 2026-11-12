# Tidal Glass

A dark theme for [Omarchy](https://omarchy.org). Graphite blue-grey windows, one
sea-blue accent, and four photographs of cold water.

![Tidal Glass preview](preview.png)

## Install

```bash
omarchy theme install https://github.com/Vinayak-Arora-324/omarchy-tidal-glass-theme.git
```

The repo is private, so git needs GitHub access first (`gh auth login`, then
`gh auth setup-git`). Switch back to it any time with
`omarchy theme set tidal-glass`.

## Files

| File | What it does |
|------|--------------|
| `colors.toml` | The palette. Omarchy builds the terminal, editor, btop and app themes from it. |
| `shell.toml` | Menus, launcher, notifications and lock screen. |
| `hyprland.lua` | 1px borders, 11px corners, window shadow. |
| `icons.theme` | `Yaru-blue-dark` |
| `backgrounds/` | The wallpapers. |

### Corners and shadows

Omarchy ignores `hyprland.lua` in themes installed from git. To get the rounded
corners and shadow, make the theme a local copy:

```bash
rm -rf ~/.config/omarchy/themes/tidal-glass/.git
omarchy theme set tidal-glass
```

## Palette

| | | | |
|---|---|---|---|
| background | `#1a2028` | foreground | `#d9dce0` |
| accent | `#4a90c8` | selection | `#2c3f55` |
| red | `#d96a70` | orange | `#cf8c5c` |
| yellow | `#d3b878` | green | `#8db388` |
| cyan | `#6bb2b8` | blue | `#6a9ed2` |
| magenta | `#a590c0` | brown | `#9a8979` |

Window borders are a plain white hairline at low opacity, a little brighter on
the focused window.

## Wallpapers

All four are from [Pexels](https://www.pexels.com/license/), cropped to 16:10
and lightly graded.

| File | Photographer |
|------|--------------|
| `1-dusk.webp` | [Gilles Quertier](https://www.pexels.com/photo/misty-rocks-on-the-sea-at-dusk-in-bretagne-33401396/) |
| `2-current.webp` | [Kris Møklebust](https://www.pexels.com/photo/dark-ocean-waves-with-reflective-light-patterns-34155535/) |
| `3-deep.webp` | [Eyüpcan Timur](https://www.pexels.com/photo/deep-dark-ocean-waves-at-twilight-33333829/) |
| `4-ripple.webp` | [Franco Garcia](https://www.pexels.com/photo/view-of-dark-blue-water-surface-18785204/) |
