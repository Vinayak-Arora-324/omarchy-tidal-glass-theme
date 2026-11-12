-- Tidal Glass: soft glass edges and generous, mac-like corner rounding.
-- (Applies when the theme lives in ~/.config/omarchy/themes as your own copy;
-- Omarchy regenerates borders from colors.toml when installed from git.)
local active_border_color = { colors = { "rgba(7fd3efcc)", "rgba(9aaefacc)" }, angle = 45 }
local inactive_border_color = "rgba(22303faa)"

hl.config({
  general = {
    col = {
      active_border = active_border_color,
      inactive_border = inactive_border_color,
    },
  },
  group = {
    col = {
      border_active = active_border_color,
      border_inactive = inactive_border_color,
    },
  },
  decoration = {
    rounding = 12,
    rounding_power = 4,
    shadow = {
      enabled = true,
      range = 28,
      render_power = 3,
      offset = "0 6",
      color = "rgba(02060bb0)",
      color_inactive = "rgba(02060b60)",
    },
  },
})
