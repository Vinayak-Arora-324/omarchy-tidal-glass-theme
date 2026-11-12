# Tidal Glass

A calm, glassy, ocean-at-night theme for [Omarchy](https://omarchy.org). It takes
its poise from macOS (quiet hairline borders, soft depth, frosted surfaces) and
sets it in deep navy water with aqua and periwinkle light.

![Tidal Glass preview](preview.png)

## Install

```bash
omarchy theme install https://github.com/Vinayak-Arora-324/omarchy-tidal-glass-theme.git
```

The repo is private, so `git` needs access to GitHub first (for example
`gh auth login` followed by `gh auth setup-git`).

Switch to it later with `omarchy theme set tidal-glass`.

## What's inside

| File | Purpose |
|------|---------|
| `colors.toml` | The palette. Omarchy generates terminal, editor, btop, browser and app themes from it. It also defines the aqua-to-periwinkle glass gradient on the focused window border. |
| `shell.toml` | Frosted shell surfaces: translucent menus, launcher and notifications with fine 1px hairline borders and an aqua selection tint. |
| `hyprland.lua` | 12px rounded corners and soft drop shadows. |
| `icons.theme` | `Yaru-blue-dark` |
| `backgrounds/` | Four original wallpapers: **Tide**, **Glass**, **Abyss**, **Lagoon**. |
| `unlock.png`, `preview.png` | Lock-screen logo and theme-picker preview. |
| `tools/make-backgrounds.py` | Regenerates the wallpapers (SVG → `rsvg-convert` → WebP). |

### Rounded corners and shadows

When a theme is installed from git, Omarchy won't load its `hyprland.lua`, so
that file is skipped. To get the corners and shadows anyway, copy the theme
locally as your own:

```bash
rm -rf ~/.config/omarchy/themes/tidal-glass/.git
omarchy theme set tidal-glass
```

You can also put `rounding = 12` in `~/.config/hypr/looknfeel.lua` instead.

## Palette

| Role | Hex | | Role | Hex |
|---|---|---|---|---|
| background | `#0d1520` | | accent | `#6cc7e8` |
| foreground | `#d6e1eb` | | selection | `#213448` |
| red | `#ef7f86` | | green | `#82d4b2` |
| yellow | `#efd08a` | | cyan | `#74d2d6` |
| orange | `#f2a77c` | | blue | `#6fa9f2` |
| magenta | `#b7a2f0` | | muted | `#4c5d70` |

## Regenerating wallpapers

```bash
python3 tools/make-backgrounds.py build
for f in build/*.svg; do
  n=$(basename "$f" .svg)
  rsvg-convert -w 3840 -h 2400 "$f" -o "build/$n.png"
  magick "build/$n.png" -quality 90 "backgrounds/$n.webp"
done
```
