#!/usr/bin/env node
// Verifies every character used on screen exists in the shipped fonts (no silent system-font fallback).
import fs from 'node:fs';
import opentype from 'opentype.js';
const args = Object.fromEntries(process.argv.slice(2).map((a) => { const m = a.match(/^--([^=]+)=(.*)$/); return [m[1], m[2]]; }));
const strings = JSON.parse(fs.readFileSync(args.strings, 'utf8'));
const fonts = args.fonts.split(',').map((p) => opentype.loadSync(p));
const chars = [...new Set(strings.join('').split('').filter((c) => !/\s/.test(c)))];
const missing = chars.filter((c) => !fonts.some((f) => f.charToGlyphIndex(c) > 0));
console.log(`${chars.length} unique chars, ${missing.length} missing`, missing.join(' '));
process.exit(missing.length ? 1 : 0);
