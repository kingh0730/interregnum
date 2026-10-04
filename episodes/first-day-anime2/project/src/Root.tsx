import React from 'react';
import {Composition} from 'remotion';
import {TimingCards} from './TimingCards';
import {Film} from './Film';
import {sync} from './sync';

export const Root: React.FC = () => <>
  <Composition id="Film" component={Film} width={1920} height={1080} fps={sync.fps} durationInFrames={sync.frames}/>
  <Composition id="TimingCards" component={TimingCards} width={1920} height={1080} fps={sync.fps} durationInFrames={sync.frames}/>
</>;
