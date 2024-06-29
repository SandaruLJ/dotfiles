import { Binding } from 'resource:///com/github/Aylur/ags/service.js';
import { Window } from 'resource:///com/github/Aylur/ags/widgets/window.js';

export const OsdSlider = (
  name: string,
  icon: Binding<any, string, string>,
  value: Binding<any, string, number>,
): Window<any, unknown> => {
  return Widget.Window({
    name: name,
    className: 'osd-slider-container',
    visible: false,
    layer: 'overlay',
    exclusivity: 'ignore',
    keymode: 'none',
    anchor: ['top'],
    margins: [24, 0],
    heightRequest: 24,
    child: Widget.Box({
      children: [
        Widget.Icon({
          icon: icon,
          className: 'osd-slider-icon',
          widthRequest: 32,
        }),
        Widget.LevelBar({
          value: value,
          className: 'osd-slider-level',
          widthRequest: 160,
        }),
      ],
    }),
  });
};
