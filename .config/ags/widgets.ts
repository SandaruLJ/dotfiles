import { Binding } from 'resource:///com/github/Aylur/ags/service.js';
import { Window } from 'resource:///com/github/Aylur/ags/widgets/window.js';

export const OsdSlider = (
  name: string,
  icon: Binding<any, string, string>,
  value: Binding<any, string, number>,
): Window<any, unknown> => {
  return Widget.Window({
    name: name,
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
          className: 'osd-slider-icon',
          widthRequest: 24,
          icon: icon,
        }),
        Widget.LevelBar({
          widthRequest: 160,
          value: value,
        }),
      ],
    }),
  });
};
