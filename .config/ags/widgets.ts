import { Binding } from 'types/service';
import { Connectable } from 'types/service';
import Icon from 'types/widgets/icon';
import LevelBar from 'types/widgets/levelbar';
import { Window } from 'types/widgets/window';

export const OsdSlider = (
  name: string,
  iconBinding: Binding<any, string, string> | string,
  valueBinding: Binding<any, string, number>,
  iconHook?: {
    gobject: Connectable;
    callback: (self: Icon<unknown>, ...args: any[]) => void;
    signal?: string;
  },
  valueHook?: {
    gobject: Connectable;
    callback: (self: LevelBar<unknown>, ...args: any[]) => void;
    signal?: string;
  },
): Window<any, unknown> => {
  const icon = Widget.Icon({
    icon: iconBinding,
    className: 'osd-slider-icon',
    widthRequest: 32,
  });

  const level = Widget.LevelBar({
    value: valueBinding,
    className: 'osd-slider-level',
    widthRequest: 160,
  });

  if (iconHook) icon.hook(iconHook.gobject, iconHook.callback, iconHook.signal);
  if (valueHook)
    level.hook(valueHook.gobject, valueHook.callback, valueHook.signal);

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
      children: [icon, level],
    }),
  });
};
