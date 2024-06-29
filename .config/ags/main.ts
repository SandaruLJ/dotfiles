import GLib from 'gi://GLib';
import { Window } from 'types/widgets/window';
import { Variable as VariableT } from 'types/variable';
import { getVolumeIcon } from 'utils';
import { OsdSlider } from 'widgets';

const audio = await Service.import('audio');

/* Widgets */

const osdVolume = OsdSlider(
  'osdVolume',
  audio.speaker.bind('volume').as(getVolumeIcon),
  audio.speaker.bind('volume'),
  {
    gobject: audio,
    callback: (self) => {
      self.icon = audio.speaker.is_muted
        ? getVolumeIcon(0)
        : getVolumeIcon(audio.speaker.volume);
    },
    signal: 'speaker-changed',
  },
  {
    gobject: audio,
    callback: (self) =>
      (self.value = audio.speaker.is_muted ? 0 : audio.speaker.volume),
    signal: 'speaker-changed',
  },
);

App.config({
  windows: [osdVolume],
  style: 'style.css',
});

/* Behaviour */

// Enabled OSD widgets
const osdWidgets = [osdVolume];
// Current display status of widgets
const displayedWidgets: { [key: string]: VariableT<boolean> } = {};

// Most recently displayed widget and its timeout
let latestWidget: Window<any, unknown> | undefined;
let activeTimeout: GLib.Source | undefined;

const hideOsd = () => {
  if (!latestWidget) return;

  latestWidget.hide();
  displayedWidgets[latestWidget.name!].value = false;
  latestWidget = undefined;
};

// Initialize displayed status and event listeners
for (const osd of osdWidgets) {
  if (!osd.name) continue;

  displayedWidgets[osd.name] = Variable(false);
  // Enable global access to make keybindings convenient
  globalThis[osd.name] = displayedWidgets[osd.name];

  // Listen to change events
  displayedWidgets[osd.name].connect('changed', ({ value }) => {
    if (!value) return;

    osd.show();
    latestWidget = osd;

    // Disable active timeout, if exists
    if (activeTimeout !== undefined) {
      activeTimeout.destroy();
      activeTimeout = undefined;
    }
    activeTimeout = setTimeout(hideOsd, 1000);
  });
}
