const entry = `${App.configDir}/main.ts`;
const main = '/tmp/ags/main.ts';

try {
  await Utils.execAsync([
    'esbuild',
    '--bundle',
    entry,
    '--format=esm',
    `--outfile=${main}`,
  ]);

  await import(`file://${main}`);
} catch (error) {
  console.error(error);
  App.quit();
}

export {};
