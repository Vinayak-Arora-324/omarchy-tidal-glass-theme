-- Tidal Glass: hairline neutral borders, rounded corners, wide soft shadow.
-- (Used when the theme is a copy in ~/.config/omarchy/themes; installed from
-- git, Omarchy generates the border colors from colors.toml.)
local active_border_color = "rgba(ffffff2e)"
local inactive_border_color = "rgba(ffffff14)"

hl.config({
  general = {
    border_size = 1,
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
    rounding = 11,
    rounding_power = 4,
    shadow = {
      enabled = true,
      range = 40,
      render_power = 3,
      offset = "0 10",
      color = "rgba(00000099)",
      color_inactive = "rgba(00000055)",
    },
  },
})
