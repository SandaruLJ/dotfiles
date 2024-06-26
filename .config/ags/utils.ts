export const getVolumeIcon = (volume: number) => {
  let level = 'muted';

  if (volume > 1.0) level = 'overamplified';
  else if (volume > 0.66) level = 'high';
  else if (volume > 0.33) level = 'medium';
  else if (volume > 0) level = 'low';

  return `audio-volume-${level}-symbolic`;
};

export const getMicIcon = (mute: boolean | null, volume: number) => {
  let level = 'muted';

  if (!mute) {
    if (volume > 0.66) level = 'high';
    else if (volume > 0.33) level = 'medium';
    else if (volume > 0) level = 'low';
  }

  return `microphone-sensitivity-${level}-symbolic`;
};
