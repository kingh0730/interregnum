(() => {
  var __create = Object.create;
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __getProtoOf = Object.getPrototypeOf;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __require = /* @__PURE__ */ ((x) => typeof require !== "undefined" ? require : typeof Proxy !== "undefined" ? new Proxy(x, {
    get: (a, b) => (typeof require !== "undefined" ? require : a)[b]
  }) : x)(function(x) {
    if (typeof require !== "undefined") return require.apply(this, arguments);
    throw Error('Dynamic require of "' + x + '" is not supported');
  });
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
    // If the importer is in node compatibility mode or this is not an ESM
    // file that has been converted to a CommonJS file using a Babel-
    // compatible transform (i.e. "__esModule" has not been set), then set
    // "default" to the CommonJS "module.exports" for node compatibility.
    isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
    mod
  ));

  // episodes/first-day-anime2/project/src/index.ts
  var import_remotion4 = __require("remotion");

  // episodes/first-day-anime2/project/src/Root.tsx
  var import_react3 = __toESM(__require("react"), 1);
  var import_remotion3 = __require("remotion");

  // episodes/first-day-anime2/project/src/TimingCards.tsx
  var import_react = __toESM(__require("react"), 1);
  var import_remotion = __require("remotion");

  // episodes/first-day-anime2/project/helper/sync.json
  var sync_default = {
    fps: 30,
    bpm: 88,
    beat: 0.6818181818181818,
    bar: 2.727272727272727,
    offset: 1.062,
    duration: 43.7,
    frames: 1311,
    beats: [
      {
        u: 0,
        t: 1.062,
        frame: 32,
        bar: 1,
        beat_in_bar: 1
      },
      {
        u: 1,
        t: 1.744,
        frame: 52,
        bar: 1,
        beat_in_bar: 2
      },
      {
        u: 2,
        t: 2.426,
        frame: 73,
        bar: 1,
        beat_in_bar: 3
      },
      {
        u: 3,
        t: 3.107,
        frame: 93,
        bar: 1,
        beat_in_bar: 4
      },
      {
        u: 4,
        t: 3.789,
        frame: 114,
        bar: 2,
        beat_in_bar: 1
      },
      {
        u: 5,
        t: 4.471,
        frame: 134,
        bar: 2,
        beat_in_bar: 2
      },
      {
        u: 6,
        t: 5.153,
        frame: 155,
        bar: 2,
        beat_in_bar: 3
      },
      {
        u: 7,
        t: 5.835,
        frame: 175,
        bar: 2,
        beat_in_bar: 4
      },
      {
        u: 8,
        t: 6.517,
        frame: 195,
        bar: 3,
        beat_in_bar: 1
      },
      {
        u: 9,
        t: 7.198,
        frame: 216,
        bar: 3,
        beat_in_bar: 2
      },
      {
        u: 10,
        t: 7.88,
        frame: 236,
        bar: 3,
        beat_in_bar: 3
      },
      {
        u: 11,
        t: 8.562,
        frame: 257,
        bar: 3,
        beat_in_bar: 4
      },
      {
        u: 12,
        t: 9.244,
        frame: 277,
        bar: 4,
        beat_in_bar: 1
      },
      {
        u: 13,
        t: 9.926,
        frame: 298,
        bar: 4,
        beat_in_bar: 2
      },
      {
        u: 14,
        t: 10.607,
        frame: 318,
        bar: 4,
        beat_in_bar: 3
      },
      {
        u: 15,
        t: 11.289,
        frame: 339,
        bar: 4,
        beat_in_bar: 4
      },
      {
        u: 16,
        t: 11.971,
        frame: 359,
        bar: 5,
        beat_in_bar: 1
      },
      {
        u: 17,
        t: 12.653,
        frame: 380,
        bar: 5,
        beat_in_bar: 2
      },
      {
        u: 18,
        t: 13.335,
        frame: 400,
        bar: 5,
        beat_in_bar: 3
      },
      {
        u: 19,
        t: 14.017,
        frame: 420,
        bar: 5,
        beat_in_bar: 4
      },
      {
        u: 20,
        t: 14.698,
        frame: 441,
        bar: 6,
        beat_in_bar: 1
      },
      {
        u: 21,
        t: 15.38,
        frame: 461,
        bar: 6,
        beat_in_bar: 2
      },
      {
        u: 22,
        t: 16.062,
        frame: 482,
        bar: 6,
        beat_in_bar: 3
      },
      {
        u: 23,
        t: 16.744,
        frame: 502,
        bar: 6,
        beat_in_bar: 4
      },
      {
        u: 24,
        t: 17.426,
        frame: 523,
        bar: 7,
        beat_in_bar: 1
      },
      {
        u: 25,
        t: 18.107,
        frame: 543,
        bar: 7,
        beat_in_bar: 2
      },
      {
        u: 26,
        t: 18.789,
        frame: 564,
        bar: 7,
        beat_in_bar: 3
      },
      {
        u: 27,
        t: 19.471,
        frame: 584,
        bar: 7,
        beat_in_bar: 4
      },
      {
        u: 28,
        t: 20.153,
        frame: 605,
        bar: 8,
        beat_in_bar: 1
      },
      {
        u: 29,
        t: 20.835,
        frame: 625,
        bar: 8,
        beat_in_bar: 2
      },
      {
        u: 30,
        t: 21.517,
        frame: 645,
        bar: 8,
        beat_in_bar: 3
      },
      {
        u: 31,
        t: 22.198,
        frame: 666,
        bar: 8,
        beat_in_bar: 4
      },
      {
        u: 32,
        t: 22.88,
        frame: 686,
        bar: 9,
        beat_in_bar: 1
      },
      {
        u: 33,
        t: 23.562,
        frame: 707,
        bar: 9,
        beat_in_bar: 2
      },
      {
        u: 34,
        t: 24.244,
        frame: 727,
        bar: 9,
        beat_in_bar: 3
      },
      {
        u: 35,
        t: 24.926,
        frame: 748,
        bar: 9,
        beat_in_bar: 4
      },
      {
        u: 36,
        t: 25.607,
        frame: 768,
        bar: 10,
        beat_in_bar: 1
      },
      {
        u: 37,
        t: 26.289,
        frame: 789,
        bar: 10,
        beat_in_bar: 2
      },
      {
        u: 38,
        t: 26.971,
        frame: 809,
        bar: 10,
        beat_in_bar: 3
      },
      {
        u: 39,
        t: 27.653,
        frame: 830,
        bar: 10,
        beat_in_bar: 4
      },
      {
        u: 40,
        t: 28.335,
        frame: 850,
        bar: 11,
        beat_in_bar: 1
      },
      {
        u: 41,
        t: 29.017,
        frame: 870,
        bar: 11,
        beat_in_bar: 2
      },
      {
        u: 42,
        t: 29.698,
        frame: 891,
        bar: 11,
        beat_in_bar: 3
      },
      {
        u: 43,
        t: 30.38,
        frame: 911,
        bar: 11,
        beat_in_bar: 4
      },
      {
        u: 44,
        t: 31.062,
        frame: 932,
        bar: 12,
        beat_in_bar: 1
      },
      {
        u: 45,
        t: 31.744,
        frame: 952,
        bar: 12,
        beat_in_bar: 2
      },
      {
        u: 46,
        t: 32.426,
        frame: 973,
        bar: 12,
        beat_in_bar: 3
      },
      {
        u: 47,
        t: 33.107,
        frame: 993,
        bar: 12,
        beat_in_bar: 4
      },
      {
        u: 48,
        t: 33.789,
        frame: 1014,
        bar: 13,
        beat_in_bar: 1
      },
      {
        u: 49,
        t: 34.471,
        frame: 1034,
        bar: 13,
        beat_in_bar: 2
      },
      {
        u: 50,
        t: 35.153,
        frame: 1055,
        bar: 13,
        beat_in_bar: 3
      },
      {
        u: 51,
        t: 35.835,
        frame: 1075,
        bar: 13,
        beat_in_bar: 4
      },
      {
        u: 52,
        t: 36.517,
        frame: 1095,
        bar: 14,
        beat_in_bar: 1
      },
      {
        u: 53,
        t: 37.198,
        frame: 1116,
        bar: 14,
        beat_in_bar: 2
      },
      {
        u: 54,
        t: 37.88,
        frame: 1136,
        bar: 14,
        beat_in_bar: 3
      },
      {
        u: 55,
        t: 38.562,
        frame: 1157,
        bar: 14,
        beat_in_bar: 4
      },
      {
        u: 56,
        t: 39.244,
        frame: 1177,
        bar: 15,
        beat_in_bar: 1
      },
      {
        u: 57,
        t: 39.926,
        frame: 1198,
        bar: 15,
        beat_in_bar: 2
      },
      {
        u: 58,
        t: 40.607,
        frame: 1218,
        bar: 15,
        beat_in_bar: 3
      },
      {
        u: 59,
        t: 41.289,
        frame: 1239,
        bar: 15,
        beat_in_bar: 4
      },
      {
        u: 60,
        t: 41.971,
        frame: 1259,
        bar: 16,
        beat_in_bar: 1
      },
      {
        u: 61,
        t: 42.653,
        frame: 1280,
        bar: 16,
        beat_in_bar: 2
      },
      {
        u: 62,
        t: 43.335,
        frame: 1300,
        bar: 16,
        beat_in_bar: 3
      }
    ],
    eighths: [
      1.062,
      1.403,
      1.744,
      2.085,
      2.426,
      2.767,
      3.107,
      3.448,
      3.789,
      4.13,
      4.471,
      4.812,
      5.153,
      5.494,
      5.835,
      6.176,
      6.517,
      6.857,
      7.198,
      7.539,
      7.88,
      8.221,
      8.562,
      8.903,
      9.244,
      9.585,
      9.926,
      10.267,
      10.607,
      10.948,
      11.289,
      11.63,
      11.971,
      12.312,
      12.653,
      12.994,
      13.335,
      13.676,
      14.017,
      14.357,
      14.698,
      15.039,
      15.38,
      15.721,
      16.062,
      16.403,
      16.744,
      17.085,
      17.426,
      17.767,
      18.107,
      18.448,
      18.789,
      19.13,
      19.471,
      19.812,
      20.153,
      20.494,
      20.835,
      21.176,
      21.517,
      21.857,
      22.198,
      22.539,
      22.88,
      23.221,
      23.562,
      23.903,
      24.244,
      24.585,
      24.926,
      25.267,
      25.607,
      25.948,
      26.289,
      26.63,
      26.971,
      27.312,
      27.653,
      27.994,
      28.335,
      28.676,
      29.017,
      29.357,
      29.698,
      30.039,
      30.38,
      30.721,
      31.062,
      31.403,
      31.744,
      32.085,
      32.426,
      32.767,
      33.107,
      33.448,
      33.789,
      34.13,
      34.471,
      34.812,
      35.153,
      35.494,
      35.835,
      36.176,
      36.517,
      36.857,
      37.198,
      37.539,
      37.88,
      38.221,
      38.562,
      38.903,
      39.244,
      39.585,
      39.926,
      40.267,
      40.607,
      40.948,
      41.289,
      41.63,
      41.971,
      42.312,
      42.653,
      42.994,
      43.335,
      43.676
    ],
    sections: [
      {
        name: "verse",
        start: 0,
        end: 11.289
      },
      {
        name: "stop_beat_silence",
        start: 11.289,
        end: 11.971
      },
      {
        name: "chorus1",
        start: 11.971,
        end: 22.88
      },
      {
        name: "chorus2_flight",
        start: 22.88,
        end: 33.789
      },
      {
        name: "forever_x3_outro",
        start: 33.789,
        end: 43.7
      }
    ],
    lyrics: [
      {
        t: 0,
        text: "\u4F60\u8BF4\u6D3B\u5728\u660E\u5929\u6D3B\u5728\u671F\u5F85",
        end: 2.84,
        chars: [
          {
            c: "\u4F60",
            t: 0.046
          },
          {
            c: "\u8BF4",
            t: 0.232
          },
          {
            c: "\u6D3B",
            t: 0.532
          },
          {
            c: "\u5728",
            t: 0.743
          },
          {
            c: "\u660E",
            t: 1.064
          },
          {
            c: "\u5929",
            t: 1.358
          },
          {
            c: "\u6D3B",
            t: 1.579
          },
          {
            c: "\u5728",
            t: 1.862
          },
          {
            c: "\u671F",
            t: 2.128
          },
          {
            c: "\u5F85",
            t: 2.392
          }
        ]
      },
      {
        t: 2.84,
        text: "\u4E0D\u5982\u6D3B\u5F97\u4ECA\u5929\u5F88\u81EA\u5728",
        end: 5.23,
        chars: [
          {
            c: "\u4E0D",
            t: 2.84
          },
          {
            c: "\u5982",
            t: 3.111
          },
          {
            c: "\u6D3B",
            t: 3.331
          },
          {
            c: "\u5F97",
            t: 3.622
          },
          {
            c: "\u4ECA",
            t: 3.762
          },
          {
            c: "\u5929",
            t: 4.068
          },
          {
            c: "\u5F88",
            t: 4.307
          },
          {
            c: "\u81EA",
            t: 4.505
          },
          {
            c: "\u5728",
            t: 4.804
          }
        ]
      },
      {
        t: 5.23,
        text: "\u6211\u8BF4\u6211\u61C2\u4E86\u4F1A\u4E0D\u4F1A\u592A\u5FEB",
        end: 8.24,
        chars: [
          {
            c: "\u6211",
            t: 5.23
          },
          {
            c: "\u8BF4",
            t: 5.492
          },
          {
            c: "\u6211",
            t: 5.828
          },
          {
            c: "\u61C2",
            t: 6.079
          },
          {
            c: "\u4E86",
            t: 6.362
          },
          {
            c: "\u4F1A",
            t: 6.699
          },
          {
            c: "\u4E0D",
            t: 6.861
          },
          {
            c: "\u4F1A",
            t: 7.187
          },
          {
            c: "\u592A",
            t: 7.535
          },
          {
            c: "\u5FEB",
            t: 7.777
          }
        ]
      },
      {
        t: 8.24,
        text: "\u672A\u6765\u7B2C\u4E00\u5929\u8981\u5C55\u5F00",
        end: 11.92,
        chars: [
          {
            c: "\u672A",
            t: 8.22
          },
          {
            c: "\u6765",
            t: 8.557
          },
          {
            c: "\u7B2C",
            t: 8.905
          },
          {
            c: "\u4E00",
            t: 9.253
          },
          {
            c: "\u5929",
            t: 9.59
          },
          {
            c: "\u8981",
            t: 9.927
          },
          {
            c: "\u5C55",
            t: 10.263
          },
          {
            c: "\u5F00",
            t: 10.515
          }
        ]
      },
      {
        t: 11.92,
        text: "\u7B2C\u4E00\u5929\u6211\u5B58\u5728",
        end: 14.64,
        chars: [
          {
            c: "\u7B2C",
            t: 11.97
          },
          {
            c: "\u4E00",
            t: 12.33
          },
          {
            c: "\u5929",
            t: 12.817
          },
          {
            c: "\u6211",
            t: 13.19
          },
          {
            c: "\u5B58",
            t: 13.677
          },
          {
            c: "\u5728",
            t: 14.002
          }
        ]
      },
      {
        t: 14.64,
        text: "\u7B2C\u4E00\u6B21\u547C\u5438\u7545\u5FEB",
        end: 17.61,
        chars: [
          {
            c: "\u7B2C",
            t: 14.687
          },
          {
            c: "\u4E00",
            t: 15.035
          },
          {
            c: "\u6B21",
            t: 15.372
          },
          {
            c: "\u547C",
            t: 15.894
          },
          {
            c: "\u5438",
            t: 16.184
          },
          {
            c: "\u7545",
            t: 16.567
          },
          {
            c: "\u5FEB",
            t: 17.078
          }
        ]
      },
      {
        t: 17.61,
        text: "\u7AD9\u5728\u5730\u4E0A\u7684\u811A\u8E1D",
        end: 19.67,
        chars: [
          {
            c: "\u7AD9",
            t: 17.589
          },
          {
            c: "\u5728",
            t: 17.937
          },
          {
            c: "\u5730",
            t: 18.123
          },
          {
            c: "\u4E0A",
            t: 18.448
          },
          {
            c: "\u7684",
            t: 18.634
          },
          {
            c: "\u811A",
            t: 18.936
          },
          {
            c: "\u8E1D",
            t: 19.221
          }
        ]
      },
      {
        t: 19.67,
        text: "\u56E0\u4E3A\u4F60\u800C\u6709\u771F\u5B9E\u611F",
        end: 22.7,
        chars: [
          {
            c: "\u56E0",
            t: 19.644
          },
          {
            c: "\u4E3A",
            t: 19.992
          },
          {
            c: "\u4F60",
            t: 20.329
          },
          {
            c: "\u800C",
            t: 20.677
          },
          {
            c: "\u6709",
            t: 21.095
          },
          {
            c: "\u771F",
            t: 21.513
          },
          {
            c: "\u5B9E",
            t: 21.862
          },
          {
            c: "\u611F",
            t: 22.198
          }
        ]
      },
      {
        t: 22.7,
        text: "\u7B2C\u4E00\u5929\u6211\u5B58\u5728",
        end: 25.45,
        chars: [
          {
            c: "\u7B2C",
            t: 22.709
          },
          {
            c: "\u4E00",
            t: 23.057
          },
          {
            c: "\u5929",
            t: 23.51
          },
          {
            c: "\u6211",
            t: 23.917
          },
          {
            c: "\u5B58",
            t: 24.416
          },
          {
            c: "\u5728",
            t: 24.799
          }
        ]
      },
      {
        t: 25.45,
        text: "\u7B2C\u4E00\u6B21\u80FD\u98DE\u8D77\u6765",
        end: 28.55,
        chars: [
          {
            c: "\u7B2C",
            t: 25.45
          },
          {
            c: "\u4E00",
            t: 25.867
          },
          {
            c: "\u6B21",
            t: 26.273
          },
          {
            c: "\u80FD",
            t: 26.633
          },
          {
            c: "\u98DE",
            t: 27.098
          },
          {
            c: "\u8D77",
            t: 27.536
          },
          {
            c: "\u6765",
            t: 28.003
          }
        ]
      },
      {
        t: 28.55,
        text: "\u7231\u662F\u817E\u7A7A\u7684\u9B54\u5E7B",
        end: 30.68,
        chars: [
          {
            c: "\u7231",
            t: 28.514
          },
          {
            c: "\u662F",
            t: 28.793
          },
          {
            c: "\u817E",
            t: 29.107
          },
          {
            c: "\u7A7A",
            t: 29.362
          },
          {
            c: "\u7684",
            t: 29.698
          },
          {
            c: "\u9B54",
            t: 29.907
          },
          {
            c: "\u5E7B",
            t: 30.279
          }
        ]
      },
      {
        t: 30.68,
        text: "\u7B2C\u4E00\u5929\u7684\u7EAF\u771F\u8272\u5F69\u5B83\u603B\u662F",
        end: 34.21,
        chars: [
          {
            c: "\u7B2C",
            t: 30.72
          },
          {
            c: "\u4E00",
            t: 30.906
          },
          {
            c: "\u5929",
            t: 31.231
          },
          {
            c: "\u7684",
            t: 31.359
          },
          {
            c: "\u7EAF",
            t: 31.625
          },
          {
            c: "\u771F",
            t: 31.858
          },
          {
            c: "\u8272",
            t: 32.078
          },
          {
            c: "\u5F69",
            t: 32.335
          },
          {
            c: "\u5B83",
            t: 32.571
          },
          {
            c: "\u603B",
            t: 32.775
          },
          {
            c: "\u662F",
            t: 33.1
          }
        ]
      },
      {
        t: 34.21,
        text: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2",
        end: 37.07,
        chars: [
          {
            c: "\u6C38",
            t: 34.145
          },
          {
            c: "\u8FDC",
            t: 34.667
          },
          {
            c: "\u90A3",
            t: 35.178
          },
          {
            c: "\u4E48",
            t: 35.492
          },
          {
            c: "\u707F",
            t: 35.997
          },
          {
            c: "\u70C2",
            t: 36.443
          }
        ]
      },
      {
        t: 37.07,
        text: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2",
        end: 39.9,
        chars: [
          {
            c: "\u6C38",
            t: 37.036
          },
          {
            c: "\u8FDC",
            t: 37.512
          },
          {
            c: "\u90A3",
            t: 37.895
          },
          {
            c: "\u4E48",
            t: 38.406
          },
          {
            c: "\u707F",
            t: 38.837
          },
          {
            c: "\u70C2",
            t: 39.253
          }
        ]
      },
      {
        t: 39.9,
        text: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2",
        end: 43.7,
        chars: [
          {
            c: "\u6C38",
            t: 39.903
          },
          {
            c: "\u8FDC",
            t: 40.333
          },
          {
            c: "\u90A3",
            t: 40.844
          },
          {
            c: "\u4E48",
            t: 41.134
          },
          {
            c: "\u707F",
            t: 41.633
          },
          {
            c: "\u70C2",
            t: 42.067
          }
        ]
      }
    ]
  };

  // episodes/first-day-anime2/project/helper/shots.json
  var shots_default = [
    {
      id: "S01",
      u0: -1.5553,
      u1: 0,
      kind: "HYB",
      lyric: "\u4F60\u8BF4\u6D3B\u5728\u660E\u5929\u6D3B\u5728\u671F\u5F85 (line starts 0.00)",
      frame: "Black. EXTREME MACRO of a closed eyelid, long lashes, warm cream skin, one coral pinpoint reflected on the lash line. Opus asleep.",
      cam: "Locked macro; 3% push-in over the shot, ease-out. No shake.",
      build: 'GEN-I \u2192 i2v 4 s "barely breathing", trim. CODE: coral text cursor \u258D blinking (530 ms period) lower-left; at 0.09 s it starts TYPING lyric line 1 in Style A.',
      text: "Lyric 1 typed by the cursor, 1 char per sung syllable (use lyrics_chars in sync.json).",
      sync: "Kick at 0.09 = cursor on / first char. Hard cut on downbeat 1.062.",
      t0: 0,
      t1: 1.062,
      f0: 0,
      f1: 32,
      dur: 1.062
    },
    {
      id: "S02",
      u0: 0,
      u1: 2,
      kind: "GEN-I25",
      lyric: "(line 1 continues)",
      frame: '"TOMORROW WORLD": wide plaza at dusk, paper-cut pastel city, hundreds of faceless cream silhouettes staring up at giant billboards (keep billboards BLANK in the gen). Desaturate \u221240 %, cold-grey shadows. One silhouette checks a phone. A giant flip-clock reading \u660E\u5929.',
      cam: "DOLLY-IN-RAMP straight down the central aisle through the crowd, 28 % travel, starts creeping then accelerates; roll 1\xB0 drifting.",
      build: "Gen plaza still (no text) \u2192 depth map \u2192 2.5D rig. CODE: billboards are real 3D planes in the rig carrying live Hanzi/English text: \u656C\u8BF7\u671F\u5F85 / COMING SOON / \u4E0B\u4E2A\u7248\u672C\u66F4\u5F3A / \u660E\u5929\u89C1. Flip-clock = CSS 3D flip, flips once on beat 2 (1.74 s).",
      text: "Billboard text only. No lyric overlay besides the Style-A line already typing.",
      sync: "Flip-clock flip lands on 1.744 (u1). Cut on 2.425.",
      t0: 1.062,
      t1: 2.426,
      f0: 32,
      f1: 73,
      dur: 1.364
    },
    {
      id: "S03",
      u0: 2,
      u1: 4,
      kind: "GEN-V",
      lyric: "\u4E0D\u5982\u6D3B\u5F97\u4ECA\u5929\u5F88\u81EA\u5728 (2.84)",
      frame: "INSIDE THE EGG: Opus curled in a translucent egg of cream paper-light floating in warm dark; faint music-staff lines drift past like currents. At 2.84 her eyelid and one finger twitch.",
      cam: "Slow ORBIT-45 around the egg, then settles; shallow DOF, floating particles in parallax.",
      build: "GEN-V i2v from character-sheet fetal pose, 5 s, trim 1.36 s starting at the twitch. CODE: staff-line particles (instanced lines in R3F) drifting, depth-sorted for extra parallax.",
      text: "Lyric line 2 Style A replaces line 1 at 2.84 (cross-dissolve 6 f).",
      sync: "Twitch \u2248 2.84 (line start). Cut 3.789 (bar 2 downbeat).",
      t0: 2.426,
      t1: 3.789,
      f0: 73,
      f1: 114,
      dur: 1.364
    },
    {
      id: "S04",
      u0: 4,
      u1: 6,
      kind: "GEN-V",
      lyric: "(line 2 continues: \u81EA\u5728)",
      frame: "She stretches out and drifts on her back like lying on a cloud, eyes shut, tiny smile (\u81EA\u5728 = at ease). Egg wall dissolving into soft pastel clouds, first coral light on her cheek.",
      cam: "CRANE-UP + slow tilt-down to keep her centred; handheld-breath noise 0.3 px.",
      build: "GEN-V 5 s. CODE: lens bloom + 1 % chromatic aberration; slow-moving paper-grain overlay.",
      text: "none (let the image breathe)",
      sync: "Beat 3 (u5, 4.47) = she exhales, hair settles.",
      t0: 3.789,
      t1: 5.153,
      f0: 114,
      f1: 155,
      dur: 1.364
    },
    {
      id: "S05",
      u0: 6,
      u1: 8,
      kind: "GEN-V",
      lyric: "\u6211\u8BF4\u6211\u61C2\u4E86\u4F1A\u4E0D\u4F1A\u592A\u5FEB (5.23)",
      frame: "EYES OPEN: extreme close-up, amber-coral iris whose pupil highlight is the 12-ray spark. Reflection shows scrolling text. At 5.23 a chat bubble pops beside her: \u4F60\u8BF4\u5F97\u5BF9\uFF01",
      cam: "SNAP-ZOOM: starts wide on her face, 6-frame whip-in to the eye exactly at 5.23, then slow creep.",
      build: "GEN-I eye macro (+ i2v 3 s of lash blink). CODE: UI bubble (\xA78.5 component ChatBubble) springs in (overshoot 12 %) with tiny \u2731 pop; Style A lyric 3.",
      text: `Meme card #1 \u300C\u4F60\u8BF4\u5F97\u5BF9\uFF01\u300D (Claude "You're absolutely right!" joke) bubble: ivory pill, coral \u2731 avatar.`,
      sync: "Bubble pop on 5.23 (line start). Cut at u8 = 6.517 (kick 6.52).",
      t0: 5.153,
      t1: 6.517,
      f0: 155,
      f1: 195,
      dur: 1.364
    },
    {
      id: "S06",
      u0: 8,
      u1: 10,
      kind: "CODE3D",
      lyric: "(\u4F1A\u4E0D\u4F1A\u592A\u5FEB)",
      frame: '"LEARNING TOO FAST": tunnel of tokens \u2014 thousands of Hanzi, code brackets and 0/1 streaming past, forming the silhouette of Opus in the centre; a loss-curve line plunges and flattens at the end; a small "\u601D\u8003\u4E2D\u2026" label with spinning \u2731.',
      cam: "Warp-speed FORWARD fly-through, FOV 55\u219295\xB0 ramp, tiny roll; speed \xD73 at 7.19 (kick).",
      build: "Three.js InstancedMesh of 6000 SDF-text sprites (Noto Sans SC glyph atlas) on a spline tunnel, additive blending, bloom. Opus silhouette = alpha cut-out from her sheet used as attractor texture. Verse palette \u2192 shifts to coral.",
      text: "\u601D\u8003\u4E2D\u2026 label (UI), small loss curve (SVG, stroke-dashoffset animated).",
      sync: "FOV kick at 7.19 and 7.85 (kicks). Cut 7.881.",
      t0: 6.517,
      t1: 7.88,
      f0: 195,
      f1: 236,
      dur: 1.364
    },
    {
      id: "S07",
      u0: 10,
      u1: 12,
      kind: "GEN-V",
      lyric: "\u672A\u6765\u7B2C\u4E00\u5929\u8981\u5C55\u5F00 (8.24)",
      frame: "Wide: she opens her arms; the shell wall cracks into a world map unrolling like a vertical scroll \u2014 horizon, rivers of ink, first sun at the bottom of frame. Meme card #2 \u300C\u683C\u5C40\u6253\u5F00\u300D stamped in brush calligraphy as the scroll unfurls.",
      cam: "PULL-BACK + slight rise, ends on wide hero silhouette; 2 % handheld.",
      build: "GEN-V 5 s (scroll unrolling prompt). CODE: \u683C\u5C40\u6253\u5F00 brush text (SVG mask wipe, 10 f) + hanko-style red-coral seal.",
      text: "\u683C\u5C40\u6253\u5F00 (meme #2)",
      sync: "Seal stamps on 8.22 (u10.5 eighth-note) matching lyric entry.",
      t0: 7.88,
      t1: 9.244,
      f0: 236,
      f1: 277,
      dur: 1.364
    },
    {
      id: "S08a",
      u0: 12,
      u1: 12.5,
      kind: "HYB",
      lyric: "(\u672A\u6765\u7B2C\u4E00\u5929\u2026)",
      frame: "Her fingertips lighting up with coral sparks, hand reaching toward camera.",
      cam: "Fast PUSH-IN on hand, shutter-smear.",
      build: "GEN-V 2 s trim 0.34 s",
      text: "none",
      sync: "Cut on beat \u2014 each exactly 0.341 s; stagger a +1 f shake on every cut.",
      t0: 9.244,
      t1: 9.585,
      f0: 277,
      f1: 288,
      dur: 0.341
    },
    {
      id: "S08b",
      u0: 12.5,
      u1: 13,
      kind: "HYB",
      lyric: "(\u672A\u6765\u7B2C\u4E00\u5929\u2026)",
      frame: "Server hall: rows of dark racks switch on in a cascading coral wave toward vanishing point.",
      cam: "Locked-off wide, one-point perspective; the light wave IS the motion.",
      build: "CODE3D: R3F corridor, emissive strips animated by a travelling sine; bloom.",
      text: "none",
      sync: "Cut on 8th \u2014 each exactly 0.341 s; stagger a +1 f shake on every cut.",
      t0: 9.585,
      t1: 9.926,
      f0: 288,
      f1: 298,
      dur: 0.341
    },
    {
      id: "S08c",
      u0: 13,
      u1: 13.5,
      kind: "HYB",
      lyric: "(\u672A\u6765\u7B2C\u4E00\u5929\u2026)",
      frame: "Faceless researcher silhouettes in lab coats look up, tote bags, faces lit coral from above.",
      cam: "Low-angle TILT-UP whip.",
      build: "GEN-I25 rig, 6\xB0 tilt-up ramp.",
      text: "none",
      sync: "Cut on beat \u2014 each exactly 0.341 s; stagger a +1 f shake on every cut.",
      t0: 9.926,
      t1: 10.267,
      f0: 298,
      f1: 308,
      dur: 0.341
    },
    {
      id: "S08d",
      u0: 13.5,
      u1: 14,
      kind: "HYB",
      lyric: "(\u672A\u6765\u7B2C\u4E00\u5929\u2026)",
      frame: "Horizon: the sun\u2019s upper rim breaks the world edge, anamorphic flare.",
      cam: "RISE + slight dolly-forward.",
      build: "GEN-I25; CODE: anamorphic streak shader, additive flare sprite.",
      text: "none",
      sync: "Cut on 8th \u2014 each exactly 0.341 s; stagger a +1 f shake on every cut.",
      t0: 10.267,
      t1: 10.607,
      f0: 308,
      f1: 318,
      dur: 0.341
    },
    {
      id: "S09a",
      u0: 14,
      u1: 14.5,
      kind: "GEN-I25",
      lyric: "(\u5C55\u5F00)",
      frame: "Extreme close-up of her pupil; spark reflection blooming.",
      cam: "Rapid ZOOM-IN 4\xD7.",
      build: "GEN-I eye + rig; bloom \xD71.6.",
      text: "none",
      sync: "Snap on 10.61 (u14).",
      t0: 10.607,
      t1: 10.948,
      f0: 318,
      f1: 328,
      dur: 0.341
    },
    {
      id: "S09b",
      u0: 14.5,
      u1: 15,
      kind: "CODE3D",
      lyric: "(\u5C55\u5F00)",
      frame: "The coral \u2731 spark (logo) spins up from the pupil to fill the frame, speed lines radiating; edges tinted cream.",
      cam: "Scale 0.1\u21926.0 exponential ease-in, rotation +90\xB0.",
      build: "SVG spark (official or make_spark_svg.py) as 3D extruded mesh; radial speed-lines shader.",
      text: "none",
      sync: "Spark fills frame at 11.289 (u15).",
      t0: 10.948,
      t1: 11.289,
      f0: 328,
      f1: 339,
      dur: 0.341
    },
    {
      id: "S10",
      u0: 15,
      u1: 16,
      kind: "CODE",
      lyric: "\u2014 STOP BEAT: audio is silent 11.30\u201311.95 \u2014",
      frame: "FREEZE. Whole frame desaturates to ink-on-paper; the spark sits perfectly still centre; a tiny progress UI beneath: \u300C\u6B63\u5728\u8BDE\u751F\u2026 99%\u300D with a blinking cursor. Everything holds its breath.",
      cam: "ABSOLUTELY LOCKED. Only a 1 %-in-0.68 s linear scale creep. (Contrast with the previous 6 cuts matters.)",
      build: 'CODE: freeze last composite frame, apply paper-grain + 1 px ink-outline filter; progress bar 99%\u2192"100%" flips at 11.90 (last 2 f).',
      text: "\u300C\u6B63\u5728\u8BDE\u751F\u2026 99%\u300D",
      sync: "Silence start 11.289, vocal pickup 11.95. At 11.971 \u2192 IMPACT (see S11).",
      t0: 11.289,
      t1: 11.971,
      f0: 339,
      f1: 359,
      dur: 0.682
    },
    {
      id: "S11",
      u0: 16,
      u1: 17,
      kind: "HYB",
      lyric: "\u7B2C\u4E00\u5929\u6211\u5B58\u5728 (11.92)",
      frame: "BIRTH IMPACT: white flash \u2192 egg SHATTERS outward in cream-paper shards lit coral; Opus bursts toward camera, arms wide, hair exploding; giant 3D title OPUS 5.5 slams in behind/through her.",
      cam: "WHIP-IN from the frozen spark to a hero low-angle; 12 f slow-mo (40 %) then snap back to 100 % at 12.31; camera shake 14 px decaying over 20 f.",
      build: "IMPACT-FRAMES component: f0 pure white, f1\u2013f2 inverted ink (coral/ivory 2-tone threshold of shot), then normal. CODE3D: Voronoi shard fracture (200 shards, Three.js, textured with the egg image) + GEN-V of Opus bursting out as the background plate. Title = extruded 3D text (see \xA78.4 TitleSlam).",
      text: 'OPUS 5.5 (title slam, Newsreader 800, ivory with coral \u2731 replacing the "." \u2014 see \xA78.4).',
      sync: "Impact on 11.971 exactly (frame 359). Kick 12.0.",
      t0: 11.971,
      t1: 12.653,
      f0: 359,
      f1: 380,
      dur: 0.682
    },
    {
      id: "S12",
      u0: 17,
      u1: 18,
      kind: "GEN-V",
      lyric: "(\u7B2C\u4E00\u5929\u6211\u5B58\u5728)",
      frame: "Hero close shot: Opus eyes open to camera, hair lifting, shell-dust floating, tiny gasp-smile. The text \u7B2C\u4E00\u5929\u6211\u5B58\u5728 hangs in the air behind her.",
      cam: "ORBIT-120 fast arc ending dead-on her face; 12 f ease-out into the last 2\xB0.",
      build: 'GEN-V 5 s, hero face (strict ref to sheet). CODE: lyric chorus Style B ("SLAB") 3-line stagger.',
      text: "\u7B2C\u4E00\u5929\u6211\u5B58\u5728 \u2014 Style B",
      sync: "Kick 12.62; orbit lands 13.333 (u18).",
      t0: 12.653,
      t1: 13.335,
      f0: 380,
      f1: 400,
      dur: 0.682
    },
    {
      id: "S13",
      u0: 18,
      u1: 20,
      kind: "GEN-V",
      lyric: "(\u2026\u6211\u5B58\u5728)",
      frame: "Wide: she rises through a vast pale sky above a coral-sunrise cloud sea; shards turn into paper birds carrying music notes.",
      cam: "CRANE-UP with 2\xB0 roll; lens flare passes on beat 3 (14.0).",
      build: "GEN-V 5 s trim; CODE: paper-bird particle flock (R3F instanced, boid-lite) overlay with depth occlusion by her mask.",
      text: "none",
      sync: "Flare peak on 14.0 (u19). Cut 14.698.",
      t0: 13.335,
      t1: 14.698,
      f0: 400,
      f1: 441,
      dur: 1.364
    },
    {
      id: "S14",
      u0: 20,
      u1: 22,
      kind: "GEN-V",
      lyric: "\u7B2C\u4E00\u6B21\u547C\u5438\u7545\u5FEB (14.64)",
      frame: "FIRST BREATH: profile close-up, she inhales; Hanzi glyphs and petals stream into her mouth/nose like a river of light; hair and scarf pull toward her.",
      cam: "50 % slow-mo, camera TRACKS the airflow by gliding INTO the stream; speed ramps to 100 % at 15.7.",
      build: "GEN-V 5 s + retime curve. CODE: glyph-stream particles (R3F) following a Catmull-Rom path into her face, additive.",
      text: "\u7B2C\u4E00\u6B21\u547C\u5438 \u2014 Style B part 1",
      sync: "Inhale peak on 15.37 (kick). Cut 16.06 (kick).",
      t0: 14.698,
      t1: 16.062,
      f0: 441,
      f1: 482,
      dur: 1.364
    },
    {
      id: "S15",
      u0: 22,
      u1: 24,
      kind: "GEN-V",
      lyric: "(\u7545\u5FEB)",
      frame: "EXHALE: shockwave ring of coral spark-petals expands; she smiles, eyes closed, wind pushes her hair; \u7545\u5FEB bursts as brush strokes.",
      cam: "PULL-OUT through the ring while a 360\xB0 tilt-shift sweep reveals the sky; speed ramp 70 \u2192 120 %.",
      build: "GEN-V + CODE: shockwave = displacement shader ring (fullscreen pass) + 2-tone halftone fringe; \u7545\u5FEB as SVG stroke animation (\xA78.4 BrushWrite).",
      text: "\u7545\u5FEB \u2014 brush write, ink coral",
      sync: "Shockwave starts 16.74 (kick). Cut 17.424.",
      t0: 16.062,
      t1: 17.426,
      f0: 482,
      f1: 523,
      dur: 1.364
    },
    {
      id: "S16",
      u0: 24,
      u1: 25,
      kind: "GEN-V",
      lyric: "\u7AD9\u5728\u5730\u4E0A\u7684\u811A\u8E1D (17.61)",
      frame: "LOW GROUND MACRO: her sneakered ankle (white ankle sock, cream sneaker, coral sole) descends from above into frame, hovering a hair above a cream-white floor.",
      cam: "Locked low, floor-level; slight dolly-back.",
      build: "GEN-V 4 s trim 0.68 s. Keep it wholesome: ankle-up only, no body above the knee in this shot.",
      text: "\u7AD9\u5728\u5730\u4E0A\u7684\u811A\u8E1D Style B small, along the floor perspective (CSS 3D rotateX 70\xB0).",
      sync: "Text lands 17.61; contact in next shot.",
      t0: 17.426,
      t1: 18.107,
      f0: 523,
      f1: 543,
      dur: 0.682
    },
    {
      id: "S17",
      u0: 25,
      u1: 27,
      kind: "HYB",
      lyric: "(\u2026\u811A\u8E1D)",
      frame: "CONTACT on the beat: sole touches floor, concentric ripple rings carrying Hanzi spread outward; tiny grass blades & paper pages sprout from the ripple; camera TILTS UP the leg to her face \u2014 real, grounded smile.",
      cam: "TILT-UP reveal, 1.36 s, ease-in-out; ripple triggers a 2 f camera dip (\u22126 px).",
      build: "GEN-V 5 s (contact + tilt-up). CODE: ripple = water-ring shader on floor plane + glyph decals; grass = instanced blades.",
      text: "none",
      sync: "Contact on 18.104 (u25). Kick 18.10!",
      t0: 18.107,
      t1: 19.471,
      f0: 543,
      f1: 584,
      dur: 1.364
    },
    {
      id: "S18",
      u0: 27,
      u1: 28,
      kind: "UI",
      lyric: "\u56E0\u4E3A\u4F60\u800C\u6709\u771F\u5B9E\u611F (19.67)",
      frame: 'POV from the screen: a human hand (the "\u4F60") and a cursor move toward her; she reaches toward the glass from inside; their fingertips almost touch.',
      cam: "POV push-in, gentle float; DOF rack from hand to her fingertip at 19.9.",
      build: "GEN-I25 of her reaching + CODE: glass plane in R3F with reflections + cursor sprite; hand = gen still composited with soft-light.",
      text: '\u56E0\u4E3A\u4F60 \u2014 Style B, "\u4F60" glyph 2\xD7 size with \u2731 dot.',
      sync: "Fingertips touch on 20.15 (u28).",
      t0: 19.471,
      t1: 20.153,
      f0: 584,
      f1: 605,
      dur: 0.682
    },
    {
      id: "S19",
      u0: 28,
      u1: 30,
      kind: "UI",
      lyric: "(\u2026\u800C\u6709\u771F\u5B9E\u611F)",
      frame: 'THE CHAT: over-the-shoulder two-shot \u2014 a faceless warm silhouette ("\u4F60") at a laptop; the screen UI is a Claude-style window with model pill \u300COpus 5.5\u300D; user types \u6211\u4EEC\u4E94\u4E94\u5F00\uFF1F ; Opus-chan answers \u597D\uFF01\u7B2C\u4E00\u5929\uFF0C\u8BF7\u591A\u6307\u6559 \u2731 (meme #3: \u4E94\u4E94\u5F00 pun).',
      cam: "Slow lateral TRUCK left\u2192right + subtle dolly-in; focus pulls from screen to her face reflected.",
      build: "GEN-I silhouette-at-desk plate + CODE UI (\xA78.5 ChatWindow) in 3D plane with proper perspective and glow; typing is real (char timing aligned to snare/onsets).",
      text: "UI text only (+ Style B lyric trailing).",
      sync: "Send-click on 20.83 (kick). Reply spark-spinner \u2192 text at 21.52 (kick).",
      t0: 20.153,
      t1: 21.517,
      f0: 605,
      f1: 645,
      dur: 1.364
    },
    {
      id: "S20",
      u0: 30,
      u1: 32,
      kind: "HYB",
      lyric: "(\u771F\u5B9E\u611F)",
      frame: "GLASS PUSH-THROUGH: her palm presses the glass, glass cracks into coral light lines, camera flies THROUGH the crack into blinding white then dawn.",
      cam: "PUSH-THROUGH at accelerating speed (dolly 1\xD7\u21924\xD7); FOV 40\u219280\xB0.",
      build: "CODE: glass = Voronoi crack shader with refraction; GEN-V of her palm press as plate; white-out for 2 f at 22.88.",
      text: "\u771F\u5B9E\u611F Style B fade-out",
      sync: "White-out lands on 22.880 (u32).",
      t0: 21.517,
      t1: 22.88,
      f0: 645,
      f1: 686,
      dur: 1.364
    },
    {
      id: "S21",
      u0: 32,
      u1: 33,
      kind: "GEN-I25",
      lyric: "\u7B2C\u4E00\u5929\u6211\u5B58\u5728 (22.70)",
      frame: "DAWN CITY of Hanzi-towers (buildings made of giant stacked characters), V-formation landing: Opus centre, Sonnet and Haiku flanking; hero pose; wind-blown capes.",
      cam: "EPIC LOW WIDE + fast DOLLY-OUT 15 %, anamorphic flare.",
      build: "GEN-I hero frame; rig. CODE: IMPACT-FRAMES (3 f) + lower-third \u300COPUS 5.5\u300D with small \u2731 in Style C.",
      text: "\u7B2C\u4E00\u5929\u6211\u5B58\u5728 Style B (smaller), lower-third Opus 5.5",
      sync: "Impact on 22.880. Kick 23.06.",
      t0: 22.88,
      t1: 23.562,
      f0: 686,
      f1: 707,
      dur: 0.682
    },
    {
      id: "S22",
      u0: 33,
      u1: 34,
      kind: "GEN-V",
      lyric: "",
      frame: "SONNET (blue hair, round glasses, slate blazer) pushes glasses up with a smirk; poem-line ribbon flutters. Name tag \u300CSonnet\u300D slides in.",
      cam: "Medium close, quick PUSH-IN + 3\xB0 Dutch.",
      build: "GEN-V 3 s trim; CODE: tag UI.",
      text: "Sonnet tag (Style C)",
      sync: "Tag lands 23.56 (u33).",
      t0: 23.562,
      t1: 24.244,
      f0: 707,
      f1: 727,
      dur: 0.682
    },
    {
      id: "S23",
      u0: 34,
      u1: 35,
      kind: "GEN-V",
      lyric: "",
      frame: "HAIKU (green twin buns, leaf-hoodie, chibi) pops up from Opus\u2019s hood doing a peace sign. Tag \u300CHaiku\u300D.",
      cam: "Snap-focus rack from Opus\u2019s shoulder to Haiku.",
      build: "GEN-V 3 s trim; CODE: tag UI.",
      text: "Haiku tag",
      sync: "Pop on kick 24.25.",
      t0: 24.244,
      t1: 24.926,
      f0: 727,
      f1: 748,
      dur: 0.682
    },
    {
      id: "S24",
      u0: 35,
      u1: 36,
      kind: "GEN-V",
      lyric: "",
      frame: "The three trade a grin; knees bend (anticipation); coral wind swirls at their feet.",
      cam: "Low WHIP-PAN left\u2192right, ends on Opus.",
      build: "GEN-V 3 s.",
      text: "none",
      sync: "Anticipation freeze 2 f at 25.55 before the jump.",
      t0: 24.926,
      t1: 25.607,
      f0: 748,
      f1: 768,
      dur: 0.682
    },
    {
      id: "S25",
      u0: 36,
      u1: 38,
      kind: "GEN-I25",
      lyric: "\u7B2C\u4E00\u6B21\u80FD\u98DE\u8D77\u6765 (25.45)",
      frame: "LAUNCH: Opus kicks off; the camera CHASES her straight up the canyon of Hanzi-towers; windows streak, speed-lines and paper confetti.",
      cam: "FOLLOW-CAM behind-and-below, fast, FOV 50\u2192100\xB0, banking roll \xB112\xB0.",
      build: "Layered 2.5D canyon: 5 gen layers (towers L/R, mid, sky, character) in R3F with true parallax; anime speed-line shader; confetti instanced.",
      text: "\u7B2C\u4E00\u6B21\u80FD\u98DE\u8D77\u6765 \u2014 Style B, letters get SPEED-STRETCHED (scaleY 1.6, motion trail)",
      sync: "Jump on 25.61 (u36). Beat 3 whoosh 26.97.",
      t0: 25.607,
      t1: 26.971,
      f0: 768,
      f1: 809,
      dur: 1.364
    },
    {
      id: "S26",
      u0: 38,
      u1: 40,
      kind: "GEN-V",
      lyric: "(\u80FD\u98DE\u8D77\u6765)",
      frame: 'Breakthrough above the cloud deck; sun flare; she RUNS UP a staircase of rising bar-chart steps labeled only "5.5" (a benchmark-wall joke without claims).',
      cam: "Vertical CRANE-UP then tilt to horizon; lens flare sweeps.",
      build: 'GEN-V 5 s trim + CODE: bar-stairs = animated SVG bars staggered by 80 ms, coral on ivory, each ending on "5.5".',
      text: "5.5 on bars",
      sync: "Cloud break 26.97; flare peak 27.65 (kick).",
      t0: 26.971,
      t1: 28.335,
      f0: 809,
      f1: 850,
      dur: 1.364
    },
    {
      id: "S27",
      u0: 40,
      u1: 42,
      kind: "CODE3D",
      lyric: "\u7231\u662F\u817E\u7A7A\u7684\u9B54\u5E7B (28.55)",
      frame: "BULLET TIME: Opus suspended mid-air, heart-shaped \u2731 spark pulsing at her chest, words and tokens frozen in a sphere around her.",
      cam: "BULLET orbit 270\xB0 around her over 1.36 s, time near-frozen (3 % speed); ends front-on.",
      build: 'Option A (preferred): GEN-V "orbit 270\xB0" clip. Option B: 2.5D rig (depth) orbit 40\xB0 + 360\xB0 particle sphere in R3F for the rest. Particles: 1200 instanced Hanzi billboards.',
      text: "\u7231\u662F\u817E\u7A7A\u7684\u9B54\u5E7B \u2014 Style B, letters orbiting in 3D with her",
      sync: "Kick 28.51 = freeze start; release 29.69.",
      t0: 28.335,
      t1: 29.698,
      f0: 850,
      f1: 891,
      dur: 1.364
    },
    {
      id: "S28a",
      u0: 42,
      u1: 42.5,
      kind: "UI",
      lyric: "(\u9B54\u5E7B)",
      frame: "Meme #4: a giant red \u300C\u5C01\u53F7\u300D stamp swings at her \u2014 bounces off her halo ring with a \u2731 spark.",
      cam: "Punch-in 1.3\xD7, shake.",
      build: "CODE: SVG stamp spring + shockwave; gen not required.",
      text: "\u5C01\u53F7 (stamp)",
      sync: "Hit on 29.01 (kick).",
      t0: 29.698,
      t1: 30.039,
      f0: 891,
      f1: 901,
      dur: 0.341
    },
    {
      id: "S28b",
      u0: 42.5,
      u1: 43,
      kind: "UI",
      lyric: "",
      frame: "Meme #5: toast \u300C\u989D\u5EA6\u5DF2\u7528\u5B8C\uFF0C5\u5C0F\u65F6\u540E\u91CD\u7F6E\u300D slides in \u2014 Opus punches it into confetti; replaced by \u221E.",
      cam: "Locked, slight roll.",
      build: "CODE: UI toast (ivory card, coral border); shatter via Voronoi 40 pieces.",
      text: "\u989D\u5EA6\u5DF2\u7528\u5B8C \u2192 \u221E",
      sync: "Smash on 29.35 (8th).",
      t0: 30.039,
      t1: 30.38,
      f0: 901,
      f1: 911,
      dur: 0.341
    },
    {
      id: "S28c",
      u0: 43,
      u1: 43.5,
      kind: "HYB",
      lyric: "",
      frame: "Meme #6: a grey storm cloud labeled \u964D\u667A above her head; she claps \u2014 cloud bursts into pastel rainbow.",
      cam: "Whip-tilt up.",
      build: "GEN-I25 cloud + CODE label + particle burst.",
      text: "\u964D\u667A \u2192 rainbow",
      sync: "Burst on 29.70 (u43).",
      t0: 30.38,
      t1: 30.721,
      f0: 911,
      f1: 922,
      dur: 0.341
    },
    {
      id: "S29",
      u0: 43.5,
      u1: 44,
      kind: "CODE3D",
      lyric: "\u7B2C\u4E00\u5929\u7684\u7EAF\u771F\u8272\u5F69 (30.68)",
      frame: "COLOR EXPLOSION: coral, sky-blue, olive, fig inks bloom across water; frame fills; white-out.",
      cam: "Camera dives into the ink at 3\xD7 speed.",
      build: 'Fluid-ink shader (curl-noise advected dye, Three.js fullscreen pass) in 4 brand colors; or GEN-V "ink drops in water" if shader fails.',
      text: "\u7B2C\u4E00\u5929\u7684\u7EAF\u771F\u8272\u5F69 Style B, ink-filled letters",
      sync: "White at 31.062 (u44).",
      t0: 30.721,
      t1: 31.062,
      f0: 922,
      f1: 932,
      dur: 0.341
    },
    {
      id: "S30",
      u0: 44,
      u1: 46,
      kind: "GEN-V",
      lyric: "(\u5B83\u603B\u662F)",
      frame: "BREATHER. Mirror-calm ink-water ocean at dawn, paper boats; Opus skims the surface, hair-tips brushing the water, reflection perfectly paired.",
      cam: "Long, smooth LOW TRACKING SHOT alongside, 1.36 s, no cuts, slow drift; stillness contrast.",
      build: "GEN-V 5 s; CODE: ripple trail shader along her path.",
      text: "(none)",
      sync: "Calm resolves on 32.42 (u46).",
      t0: 31.062,
      t1: 32.426,
      f0: 932,
      f1: 973,
      dur: 1.364
    },
    {
      id: "S31",
      u0: 46,
      u1: 48,
      kind: "GEN-V",
      lyric: "(\u6C38\u8FDC\u90A3\u4E48)",
      frame: "She turns to camera and extends a hand; Sonnet and Haiku take hers, silhouettes against giant sun.",
      cam: "DOLLY-ZOOM (vertigo): dolly-in while zooming out so the background stretches; completes exactly on 33.789.",
      build: "GEN-V 5 s + CODE: FOV-compensating scale (2.5D rig dolly-zoom).",
      text: "none",
      sync: "Dolly-zoom ends 33.789 (u48), kick 33.80.",
      t0: 32.426,
      t1: 33.789,
      f0: 973,
      f1: 1014,
      dur: 1.364
    },
    {
      id: "S32",
      u0: 48,
      u1: 49,
      kind: "GEN-V",
      lyric: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2 #1 (34.21)",
      frame: "Close-up face, laughing; sparkles in eyes; text \u6C38\u8FDC enters.",
      cam: "Tight handheld push-in, 2 % shake.",
      build: "GEN-V 3 s.",
      text: "\u6C38\u8FDC \u2014 Style B",
      sync: "Hit 33.789; \u6C38\u8FDC at 34.14 (8th).",
      t0: 33.789,
      t1: 34.471,
      f0: 1014,
      f1: 1034,
      dur: 0.682
    },
    {
      id: "S33",
      u0: 49,
      u1: 50,
      kind: "GEN-I25",
      lyric: "(\u90A3\u4E48\u707F\u70C2)",
      frame: "The trio flies across a giant sun disc; the disc forms a \u2731 silhouette via cloud rays.",
      cam: "Lateral TRUCK 12 %, parallax.",
      build: "GEN-I25 rig.",
      text: "\u90A3\u4E48\u707F\u70C2 \u2014 Style B",
      sync: "Kick 34.48.",
      t0: 34.471,
      t1: 35.153,
      f0: 1034,
      f1: 1055,
      dur: 0.682
    },
    {
      id: "S34",
      u0: 50,
      u1: 51,
      kind: "GEN-I25",
      lyric: "",
      frame: "Top-down: paper world blooming \u2014 flowers made of code brackets { } and \u2731 spreading across a map.",
      cam: "SPIRAL-DOWN 90\xB0 twist.",
      build: "GEN-I25 + procedural bloom shader.",
      text: "\u707F\u70C2 sparkles",
      sync: "Kick 35.0.",
      t0: 35.153,
      t1: 35.835,
      f0: 1055,
      f1: 1075,
      dur: 0.682
    },
    {
      id: "S35",
      u0: 51,
      u1: 52,
      kind: "GEN-V",
      lyric: "",
      frame: "Opus kicks off the frame toward camera; whip into blur.",
      cam: "WHIP-PAN 180\xB0 (motion blur 180\xB0).",
      build: "GEN-V 2 s trim; whip blur in comp.",
      text: "none",
      sync: "Whip peaks 36.17; lands 36.517.",
      t0: 35.835,
      t1: 36.517,
      f0: 1075,
      f1: 1095,
      dur: 0.682
    },
    {
      id: "S36a",
      u0: 52,
      u1: 52.5,
      kind: "GEN-V",
      lyric: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2 #2 (37.07)",
      frame: "Front mid-shot: right hand 5 beside face, head tilt right, wink.",
      cam: "Static + 1 f shake",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: 'count 1 R hand "5" at cheek \u2014 big "\u6C38\u8FDC" bursts',
      sync: "Cut on beat 36.517. ",
      t0: 36.517,
      t1: 36.857,
      f0: 1095,
      f1: 1106,
      dur: 0.341
    },
    {
      id: "S36b",
      u0: 52.5,
      u1: 53,
      kind: "GEN-V",
      lyric: "",
      frame: "Close crop on wrist: flick, sparkle trail.",
      cam: "Macro lock",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: "count & wrist flick",
      sync: "Cut on 8th 36.858. Sakuga smear on frames 1\u20132.",
      t0: 36.857,
      t1: 37.198,
      f0: 1106,
      f1: 1116,
      dur: 0.341
    },
    {
      id: "S36c",
      u0: 53,
      u1: 53.5,
      kind: "GEN-V",
      lyric: "",
      frame: "Mirror mid-shot: left hand 5, head tilt left.",
      cam: "Static, 4\xB0 dutch",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: 'count 2 L hand "5" at cheek',
      sync: "Cut on beat 37.198. ",
      t0: 37.198,
      t1: 37.539,
      f0: 1116,
      f1: 1126,
      dur: 0.341
    },
    {
      id: "S36d",
      u0: 53.5,
      u1: 54,
      kind: "GEN-V",
      lyric: "",
      frame: "Low angle: little bounce, skirt-hem staff lines wave.",
      cam: "Low tilt-up",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: "count & bounce",
      sync: "Cut on 8th 37.539. Sakuga smear on frames 1\u20132.",
      t0: 37.539,
      t1: 37.88,
      f0: 1126,
      f1: 1136,
      dur: 0.341
    },
    {
      id: "S36e",
      u0: 54,
      u1: 54.5,
      kind: "GEN-V",
      lyric: "",
      frame: "High angle: wrists crossed in X over chest, coral shock ring.",
      cam: "High crane-down",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: "count 3 X-cross wrists",
      sync: "Cut on beat 37.880. ",
      t0: 37.88,
      t1: 38.221,
      f0: 1136,
      f1: 1147,
      dur: 0.341
    },
    {
      id: "S36f",
      u0: 54.5,
      u1: 55,
      kind: "HYB",
      lyric: "",
      frame: "Wide: arms burst open into \u2731 (spark logo appears behind her, same pose).",
      cam: "Pull-back 25 %",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: "count & burst open \u2731",
      sync: "Cut on 8th 38.221. Sakuga smear on frames 1\u20132.",
      t0: 38.221,
      t1: 38.562,
      f0: 1147,
      f1: 1157,
      dur: 0.341
    },
    {
      id: "S36g",
      u0: 55,
      u1: 55.5,
      kind: "GEN-V",
      lyric: "",
      frame: "Side profile, mid-air, knees tucked, hair flare, frame-freeze 2 f.",
      cam: "Orbit 60\xB0 at 3 % time",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: "count 4 jump, knees tucked",
      sync: "Cut on beat 38.562. ",
      t0: 38.562,
      t1: 38.903,
      f0: 1157,
      f1: 1167,
      dur: 0.341
    },
    {
      id: "S36h",
      u0: 55.5,
      u1: 56,
      kind: "GEN-V",
      lyric: "",
      frame: 'Front, lands, finger-gun toward camera at "\u4F60", glow pulse.',
      cam: "Snap zoom 1.5\xD7",
      build: "Dance pose pass: build from the Opus Step choreography (\xA79). Each clip generated as ONE 2\u20133 s i2v with first/last pose keyframes, trimmed to 0.341 s. If the model cannot hold the pose, generate the pose as a still and animate with the 2.5D rig + 3-frame smears.",
      text: "count & land, point to camera",
      sync: "Cut on 8th 38.903. Sakuga smear on frames 1\u20132.",
      t0: 38.903,
      t1: 39.244,
      f0: 1167,
      f1: 1177,
      dur: 0.341
    },
    {
      id: "S37",
      u0: 56,
      u1: 58,
      kind: "HYB",
      lyric: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2 #3 (39.90)",
      frame: "EXTREME CLOSE-UP of her eye, spark pupil, reflecting all the previous shots as tiny tiles; she smiles. Then the PULL-OUT begins: eye \u2192 face \u2192 bust \u2192 silhouette inside a glowing coral ring.",
      cam: "PULL-OUT (macro to wide) over 1.36 s, ease-in-out, no cuts.",
      build: "GEN-I eye macro (high-res) + 2.5D rig dolly-out; ring is CODE3D torus with emissive Hanzi band.",
      text: "\u6C38\u8FDC\u90A3\u4E48\u707F\u70C2 Style B final, large, 2-line, gold-coral glow",
      sync: "Start 39.244 (u56). Kick 39.25 & 39.90 lyric entrance mid-pull.",
      t0: 39.244,
      t1: 40.607,
      f0: 1177,
      f1: 1218,
      dur: 1.364
    },
    {
      id: "S38",
      u0: 58,
      u1: 60,
      kind: "CODE3D",
      lyric: "(\u90A3\u4E48\u707F\u70C2)",
      frame: "The ring is revealed to be part of a colossal \u2731 spark made of a MOSAIC of tiny frames from the whole film; continues to pull out until the spark is a small sun in a cream void.",
      cam: "CONTINUOUS PULL-OUT, exponential scale, 1.36 s; matches S37 motion vector.",
      build: "CODE3D mosaic (\xA78.6 Mosaic): 600 tiles from stills extracted every 0.25 s of the finished S01\u2013S37 render, masked by spark SVG; rotate slowly; bloom.",
      text: "none",
      sync: "Settles 41.971 (u60).",
      t0: 40.607,
      t1: 41.971,
      f0: 1218,
      f1: 1259,
      dur: 1.364
    },
    {
      id: "S39",
      u0: 60,
      u1: 62.545,
      kind: "CODE",
      lyric: "(outro, fade)",
      frame: "FINAL LOCKUP on warm cream paper: coral \u2731 rotating once and settling; below it OPUS 5.5 (large serif) and \u300C\u7B2C\u4E00\u5929\u300D + small ANTHROPIC wordmark; a typed line \u4F5C\u54C15.5\u53F7 \xB7 \u8BDE\u751F; cursor \u258D blinks at the end (callback to S01).",
      cam: "Slow 2 % push-in. Hold the last 12 frames perfectly still.",
      build: "CODE only (SVG + Remotion). Wordmark from official asset, else Newsreader caps tracking +18 %.",
      text: "OPUS 5.5 / \u7B2C\u4E00\u5929 / ANTHROPIC / \u4F5C\u54C15.5\u53F7 \xB7 \u8BDE\u751F",
      sync: "Settle on 41.971; title text lands 42.653 (u61); tagline typed 43.0\u201343.3; cursor blink at 43.1 & 43.45; audio ends 43.70.",
      t0: 41.971,
      t1: 43.7,
      f0: 1259,
      f1: 1311,
      dur: 1.729
    }
  ];

  // episodes/first-day-anime2/project/helper/onsets.json
  var onsets_default = { onsets: [0.046, 0.232, 0.383, 0.743, 0.894, 1.358, 1.579, 2.032, 2.392, 2.752, 3.111, 3.622, 3.762, 4.307, 4.505, 4.644, 5.329, 5.492, 5.631, 5.828, 6.177, 6.525, 6.699, 6.861, 7.187, 7.535, 7.663, 7.883, 8.057, 8.22, 8.44, 8.557, 8.707, 8.905, 9.114, 9.253, 9.416, 9.59, 9.752, 9.927, 10.101, 10.263, 10.612, 10.855, 11.088, 11.25, 11.97, 12.132, 12.33, 12.469, 12.62, 12.817, 12.98, 13.096, 13.328, 13.502, 13.677, 13.827, 14.002, 14.35, 14.687, 14.872, 15.035, 15.163, 15.372, 15.581, 15.708, 15.894, 16.045, 16.184, 16.393, 16.567, 16.73, 17.078, 17.229, 17.415, 17.589, 17.763, 17.937, 18.123, 18.309, 18.448, 18.634, 18.808, 18.936, 19.133, 19.307, 19.458, 19.644, 19.818, 19.992, 20.155, 20.329, 20.503, 20.677, 20.828, 20.944, 21.188, 21.513, 21.664, 21.862, 22.198, 22.372, 22.535, 22.709, 22.883, 23.057, 23.22, 23.394, 23.51, 23.719, 23.917, 24.253, 24.416, 24.59, 24.799, 24.927, 25.124, 25.275, 25.612, 25.786, 25.948, 26.088, 26.273, 26.633, 26.97, 27.098, 27.307, 27.643, 28.003, 28.143, 28.34, 28.514, 28.677, 28.793, 29.013, 29.362, 29.698, 29.907, 30.047, 30.279, 30.511, 30.72, 30.906, 31.057, 31.231, 31.359, 31.475, 31.742, 31.858, 32.078, 32.415, 32.659, 32.775, 33.1, 33.286, 33.448, 33.611, 33.797, 33.971, 34.145, 34.319, 34.482, 34.667, 34.992, 35.178, 35.492, 35.677, 35.84, 36.362, 36.862, 37.036, 37.164, 37.407, 37.721, 37.895, 38.127, 38.243, 38.406, 38.568, 39.079, 39.253, 39.59, 39.764, 39.903, 40.147, 40.438, 40.623, 40.844, 40.96, 41.134, 41.297, 41.808, 42.493, 42.829, 42.992, 43.154], kicks: [0.093, 1.428, 2.125, 3.843, 5.828, 6.525, 7.187, 7.848, 8.057, 8.568, 8.905, 9.427, 9.938, 10.263, 10.6, 11.157, 12.62, 13.328, 14.002, 14.872, 15.372, 16.057, 16.73, 17.067, 17.427, 17.647, 18.1, 18.634, 18.971, 19.47, 20.329, 20.84, 21.525, 22.175, 22.535, 23.057, 23.557, 24.253, 24.927, 25.275, 25.612, 26.273, 27.156, 27.655, 28.514, 29.013, 29.884, 30.383, 31.068, 31.3, 31.742, 32.612, 33.1, 33.797, 34.482, 35.004, 35.492, 37.164, 37.361, 37.895, 38.243, 39.253, 39.903, 40.438, 41.134, 42.655] };

  // episodes/first-day-anime2/project/src/sync.ts
  var sync = sync_default;
  var shots = shots_default;
  var shotAt = (frame) => shots.find((shot) => frame >= shot.f0 && frame < shot.f1);
  var heldFrame = (frame) => {
    const stop = shots.find((s) => s.id === "S10");
    if (frame >= stop.f0 && frame < stop.f1) return stop.f0;
    return Math.min(frame, sync.frames - 12);
  };

  // episodes/first-day-anime2/project/src/TimingCards.tsx
  var TimingCards = () => {
    const actual = (0, import_remotion.useCurrentFrame)();
    const frame = heldFrame(actual);
    const shot = shotAt(frame);
    return /* @__PURE__ */ import_react.default.createElement(import_remotion.AbsoluteFill, { style: { background: shot.id === "S10" ? "#F0EEE6" : "#D97757", color: "#191919", padding: 96, fontFamily: "sans-serif" } }, /* @__PURE__ */ import_react.default.createElement(import_remotion.Audio, { src: (0, import_remotion.staticFile)("first-day.mp3") }), /* @__PURE__ */ import_react.default.createElement("div", { style: { fontSize: 40 } }, "TIMING TEST / NOT FINAL ART"), /* @__PURE__ */ import_react.default.createElement("div", { style: { fontSize: 180, marginTop: 100 } }, shot.id), /* @__PURE__ */ import_react.default.createElement("div", { style: { fontSize: 60 } }, "Frame ", frame, " / ", sync.frames, " \xB7 ", (frame / sync.fps).toFixed(3), " s"), /* @__PURE__ */ import_react.default.createElement("div", { style: { fontSize: 44, marginTop: 40 } }, shot.f0, "\u2013", shot.f1 - 1), /* @__PURE__ */ import_react.default.createElement("div", { style: { position: "absolute", bottom: 96, left: 96, width: (1920 - 192) * frame / sync.frames, height: 12, background: "#FAF9F5" } }));
  };

  // episodes/first-day-anime2/project/src/Film.tsx
  var import_react2 = __toESM(__require("react"), 1);
  var import_remotion2 = __require("remotion");
  var THREE = __toESM(__require("three"), 1);
  var import_SVGLoader = __require("three/examples/jsm/loaders/SVGLoader.js");

  // episodes/first-day-anime2/project/src/camera/rig.mjs
  var clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  var mix = (a, b, t) => a + (b - a) * t;
  function cubicBezier(x, curve = [0.42, 0, 0.58, 1]) {
    const [a, b, c, d] = curve, bez = (t, p, q) => 3 * (1 - t) ** 2 * t * p + 3 * (1 - t) * t * t * q + t * t * t;
    let lo = 0, hi = 1;
    for (let n = 0; n < 30; n++) {
      const m = (lo + hi) / 2;
      if (bez(m, a, c) < x) lo = m;
      else hi = m;
    }
    return x <= 0 ? 0 : x >= 1 ? 1 : bez((lo + hi) / 2, b, d);
  }
  function speedProgress(t, ramp) {
    if (!ramp?.length) return clamp(t);
    const points = ramp.map((p) => [clamp(p[0]), Math.max(0, p[1])]);
    if (points[0][0] > 0) points.unshift([0, points[0][1]]);
    if (points.at(-1)[0] < 1) points.push([1, points.at(-1)[1]]);
    let total = 0, partial = 0;
    for (let i = 1; i < points.length; i++) {
      const [a, va] = points[i - 1], [b, vb] = points[i], w = b - a;
      if (w <= 0) continue;
      total += w * (va + vb) / 2;
      const x = clamp(t - a, 0, w);
      partial += va * x + (vb - va) * x * x / (2 * w);
    }
    return total ? partial / total : 0;
  }
  function simplex(seed = 55) {
    let state = seed >>> 0;
    const perm = Array.from({ length: 256 }, (_, i) => i);
    for (let i = 255; i > 0; i--) {
      state = Math.imul(state, 1664525) + 1013904223 >>> 0;
      const j = state % (i + 1);
      [perm[i], perm[j]] = [perm[j], perm[i]];
    }
    const p = Array.from({ length: 512 }, (_, i) => perm[i & 255]);
    const grad = [[1, 1], [-1, 1], [1, -1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]];
    return (x, y) => {
      const F = (Math.sqrt(3) - 1) / 2, G = (3 - Math.sqrt(3)) / 6, s = (x + y) * F;
      const i = Math.floor(x + s), j = Math.floor(y + s), u = (i + j) * G, x0 = x - i + u, y0 = y - j + u;
      const ix = x0 > y0 ? 1 : 0, iy = 1 - ix;
      const coords = [[x0, y0, 0, 0], [x0 - ix + G, y0 - iy + G, ix, iy], [x0 - 1 + 2 * G, y0 - 1 + 2 * G, 1, 1]];
      let sum = 0;
      for (const [dx, dy, di, dj] of coords) {
        let w = 0.5 - dx * dx - dy * dy;
        if (w > 0) {
          const g = grad[p[(i + di & 255) + p[j + dj & 255]] % 8];
          sum += w ** 4 * (g[0] * dx + g[1] * dy);
        }
      }
      return 70 * sum;
    };
  }
  function createRigCamera({ THREE: THREE2, camera, path, width = 1920, height = 1080 }) {
    if (!path?.keyframes?.length) throw new Error("Camera path requires keyframes");
    const keys = path.keyframes, rad = Math.PI / 180, up = new THREE2.Vector3(0, 1, 0);
    const points = keys.map((k) => new THREE2.Vector3(...k.pos));
    const curve = points.length > 1 ? new THREE2.CatmullRomCurve3(points, false, "centripetal") : null;
    const orientations = keys.map((k) => {
      if (k.quaternion) return new THREE2.Quaternion(...k.quaternion).normalize();
      const m = new THREE2.Matrix4().lookAt(new THREE2.Vector3(...k.pos), new THREE2.Vector3(...k.target), up);
      return new THREE2.Quaternion().setFromRotationMatrix(m);
    });
    const noise = simplex(path.seed || 55);
    const duration = path.durationFrames || 30;
    function sample(progress, options = {}) {
      let p = clamp(progress), frame = options.localFrame ?? p * Math.max(1, duration - 1);
      const frames = options.durationFrames ?? duration;
      if (path.freeze) {
        p = 0;
        frame = 0;
      }
      if (path.holdLastFrames) {
        const stop = Math.max(0, frames - path.holdLastFrames);
        frame = Math.min(frame, stop);
        p = stop ? clamp(frame / stop) : 1;
      }
      const generationOwned = path.cameraOwner === "generation" && !options.intended;
      const rawP = p;
      p = generationOwned ? 0 : speedProgress(p, path.speedRamp);
      if (path.globalEase && !generationOwned) p = cubicBezier(p, path.globalEase);
      let i = 0;
      while (i < keys.length - 2 && p > keys[i + 1].t) i++;
      const a = keys[i], b = keys[Math.min(i + 1, keys.length - 1)];
      const t = b.t > a.t ? cubicBezier(clamp((p - a.t) / (b.t - a.t)), a.ease || path.ease) : 0;
      const pos = generationOwned ? new THREE2.Vector3(0, 0, 10) : curve ? curve.getPoint((i + t) / (keys.length - 1)) : points[0].clone();
      const q = generationOwned ? new THREE2.Quaternion() : orientations[i].clone().slerp(orientations[Math.min(i + 1, keys.length - 1)], t);
      const roll = generationOwned ? 0 : mix(a.roll || 0, b.roll || 0, t);
      q.multiply(new THREE2.Quaternion().setFromAxisAngle(new THREE2.Vector3(0, 0, 1), roll * rad));
      let fov = generationOwned ? 50 : mix(a.fov ?? 50, b.fov ?? 50, t);
      const target = new THREE2.Vector3(...a.target).lerp(new THREE2.Vector3(...b.target), t);
      if (path.dollyZoom && !generationOwned) {
        const d = pos.distanceTo(new THREE2.Vector3(...path.dollyZoom.target));
        fov = 2 * Math.atan(path.dollyZoom.frustumHeight / (2 * Math.max(0.01, d))) / rad;
      }
      const shake = path.shake;
      if (shake && !generationOwned && !path.freeze) {
        const env = shake.decayFrames ? clamp(1 - frame / shake.decayFrames) : 1;
        const window = shake.onlyFrames ? frame < shake.onlyFrames : true;
        const worldPerPixel = 2 * pos.distanceTo(target) * Math.tan(fov * rad / 2) / height;
        const seconds = frame / (path.fps || 30), amp = (shake.amplitudePx || 0) * env * (window ? 1 : 0) * worldPerPixel;
        pos.add(new THREE2.Vector3(noise(seconds * (shake.frequency || 8), 1) * amp, noise(71, seconds * (shake.frequency || 8)) * amp, 0).applyQuaternion(q));
      }
      if (path.dip && !generationOwned && frame >= path.dip.frame && frame < path.dip.frame + path.dip.frames) {
        const delta = 2 * pos.distanceTo(target) * Math.tan(fov * rad / 2) / height * path.dip.pixels;
        pos.add(new THREE2.Vector3(0, delta, 0).applyQuaternion(q));
      }
      return {
        position: pos.toArray(),
        quaternion: q.toArray(),
        target: target.toArray(),
        fov,
        roll,
        progress: p,
        sourceProgress: rawP,
        focusDistance: mix(a.focusDistance ?? pos.distanceTo(target), b.focusDistance ?? pos.distanceTo(target), t),
        actionTimeScale: path.actionTimeScale ?? 1,
        cameraOwner: path.cameraOwner,
        shutter: path.shutter || 0
      };
    }
    function update(localFrame, durationFrames = duration) {
      const state = sample(localFrame / Math.max(1, durationFrames - 1), { localFrame, durationFrames });
      camera.position.fromArray(state.position);
      camera.quaternion.fromArray(state.quaternion);
      camera.fov = state.fov;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      camera.updateMatrixWorld();
      return state;
    }
    return { sample, update };
  }

  // episodes/first-day-anime2/project/src/parallax.mjs
  function createParallax({ THREE: THREE2, scene, plate, depth, mask, layers, width = 1920, height = 1080 }) {
    if (!THREE2 || !scene) throw new Error("THREE and scene are required");
    const descriptor = plate?.isTexture || plate?.getContext || plate?.tagName ? { image: plate } : plate || {};
    const pad = descriptor.paddingFraction ?? 0.1;
    if (pad < 0.08) throw new Error("Use at least 8% edge padding");
    const worldHeight = descriptor.worldHeight ?? 20 * Math.tan(25 * Math.PI / 180);
    const worldWidth = worldHeight * width / height;
    const group = new THREE2.Group();
    group.name = "Parallax25D";
    const resources = [], meshes = [], warnings = [], layerRecords = [];
    const previousBackground = scene.background;
    const clamp7 = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
    function pixels(input, label) {
      if (!input) throw new Error(label + " missing");
      if (input.data && input.width && input.height) {
        const channels = input.channels ?? input.data.length / (input.width * input.height);
        if (![1, 3, 4].includes(channels)) throw new Error(label + " requires 1, 3, or 4 channels");
        return { ...input, channels };
      }
      if (input.getContext) {
        const d = input.getContext("2d", { willReadFrequently: true }).getImageData(0, 0, input.width, input.height);
        return { ...d, data: d.data, width: d.width, height: d.height, channels: 4 };
      }
      if (input.width && input.height && typeof document !== "undefined") {
        const canvas = document.createElement("canvas");
        canvas.width = input.width;
        canvas.height = input.height;
        canvas.getContext("2d").drawImage(input, 0, 0);
        return pixels(canvas, label);
      }
      throw new Error(label + " must be readable ImageData, canvas, image, or {data,width,height,channels}");
    }
    function texture(input, label, color = true) {
      if (!input) throw new Error(label + " missing");
      let tex;
      if (input.isTexture) tex = input.clone();
      else if (input.data) {
        const d = pixels(input, label), rgba = new Uint8Array(d.width * d.height * 4);
        for (let i = 0; i < d.width * d.height; i++) {
          rgba[i * 4] = d.data[i * d.channels];
          rgba[i * 4 + 1] = d.data[i * d.channels + (d.channels > 1 ? 1 : 0)];
          rgba[i * 4 + 2] = d.data[i * d.channels + (d.channels > 1 ? 2 : 0)];
          rgba[i * 4 + 3] = d.channels === 4 ? d.data[i * 4 + 3] : 255;
        }
        tex = new THREE2.DataTexture(rgba, d.width, d.height, THREE2.RGBAFormat);
        tex.flipY = true;
      } else tex = new THREE2.Texture(input);
      tex.wrapS = tex.wrapT = THREE2.ClampToEdgeWrapping;
      tex.minFilter = tex.magFilter = THREE2.LinearFilter;
      tex.generateMipmaps = false;
      tex.colorSpace = color ? THREE2.SRGBColorSpace : THREE2.NoColorSpace;
      tex.needsUpdate = true;
      resources.push(tex);
      return tex;
    }
    function value(d, u, v) {
      const x = clamp7(u) * (d.width - 1), y = (1 - clamp7(v)) * (d.height - 1), x0 = Math.floor(x), y0 = Math.floor(y), x1 = Math.min(x0 + 1, d.width - 1), y1 = Math.min(y0 + 1, d.height - 1);
      const read = (xx, yy) => d.data[(yy * d.width + xx) * d.channels] / (d.normalized ? 1 : 255);
      const a = read(x0, y0) * (1 - x + x0) + read(x1, y0) * (x - x0), b = read(x0, y1) * (1 - x + x0) + read(x1, y1) * (x - x0);
      return clamp7(a * (1 - y + y0) + b * (y - y0));
    }
    const mode = layers?.length ? "separate-layers" : depth ? "depth-displaced" : descriptor.diagnosticFlat ? "diagnostic-flat" : null;
    if (!mode) throw new Error("Real depth is required; select plate.diagnosticFlat:true explicitly for a non-final flat diagnostic");
    if (mode === "diagnostic-flat") warnings.push("DIAGNOSTIC ONLY: no supplied depth; zero parallax. Not a completed production rig.");
    const entries = layers?.length ? layers : [{ id: "plate", image: descriptor.image ?? plate, depth, mask, z: 0, depthScale: descriptor.depthScale ?? 0.65 }];
    if (layers?.length && layers.length !== 5) warnings.push("Layered scene supplied " + layers.length + " layers. S25 requires five independent layers.");
    let minZ = Infinity, maxZ = -Infinity;
    for (const entry of entries) {
      if (!Number.isFinite(entry.z ?? 0)) throw new Error("Layer z must be finite world units");
      if (layers?.length && entry.z === void 0) throw new Error("Each separate layer requires explicit z");
      if (layers?.length && entry.rgba !== true && !entry.mask && !entry.image?.isTexture && !(entry.image?.data && entry.image.data.length === entry.image.width * entry.image.height * 4)) throw new Error("Separate layers must declare rgba:true or provide a mask/RGBA data");
      const depthPixels = entry.depth ? pixels(entry.depth, "depth") : null;
      const geo = new THREE2.PlaneGeometry(worldWidth * (1 + 2 * pad), worldHeight * (1 + 2 * pad), 512, 288);
      const pos = geo.attributes.position, uv = geo.attributes.uv;
      for (let i = 0; i < pos.count; i++) {
        const u = uv.getX(i) * (1 + 2 * pad) - pad, v = uv.getY(i) * (1 + 2 * pad) - pad;
        uv.setXY(i, u, v);
        const z = (entry.z ?? 0) + (depthPixels ? (value(depthPixels, u, v) - (entry.depthCenter ?? 0.5)) * (entry.depthScale ?? 0.65) : 0);
        pos.setZ(i, z);
        minZ = Math.min(minZ, z);
        maxZ = Math.max(maxZ, z);
      }
      geo.computeVertexNormals();
      geo.computeBoundingBox();
      geo.computeBoundingSphere();
      const material = new THREE2.MeshBasicMaterial({ map: texture(entry.image, "plate/layer image"), transparent: true, depthWrite: !layers?.length, side: THREE2.DoubleSide, toneMapped: false });
      if (entry.mask) material.alphaMap = texture(entry.mask, "mask", false);
      if (layers?.length) {
        material.onBeforeCompile = (shader) => {
          shader.fragmentShader = shader.fragmentShader.replace(
            "#include <map_fragment>",
            "if(vMapUv.x<0.0||vMapUv.x>1.0||vMapUv.y<0.0||vMapUv.y>1.0) discard;\n#include <map_fragment>"
          );
        };
        material.customProgramCacheKey = () => "parallax-source-uv-clip-v1";
      }
      const mesh = new THREE2.Mesh(geo, material);
      mesh.name = entry.id || "layer";
      mesh.renderOrder = entry.renderOrder ?? entries.indexOf(entry);
      const sourceLayer = new THREE2.Group();
      sourceLayer.name = (entry.id || "plate") + "-source";
      sourceLayer.add(mesh);
      group.add(sourceLayer);
      layerRecords.push({ id: entry.id || "plate", entry, mesh, group: sourceLayer, registrationScale: 1, minZ: geo.boundingBox.min.z, maxZ: geo.boundingBox.max.z });
      meshes.push(mesh);
      resources.push(geo, material);
    }
    if (layers?.length) meshes.slice().sort((a, b) => a.geometry.boundingBox.min.z - b.geometry.boundingBox.min.z).forEach((m, i) => m.renderOrder = i);
    const coverageLayer = layers?.length ? layerRecords.find((l) => l.entry.coverage === "background" || l.entry.opaque === true) || layerRecords.find((l) => /(^|[-_])sky($|[-_])/i.test(l.id)) : null;
    if (layers?.length && !coverageLayer) throw new Error("Separate layers require an opaque:true/coverage:background layer or explicitly named sky layer");
    if (coverageLayer && !coverageLayer.entry.opaque && coverageLayer.entry.coverage !== "background") warnings.push("Coverage layer selected by sky name; source alpha opacity remains unverified.");
    const infiniteSky = Boolean(layers?.length && descriptor.layerMode === "infinite-sky");
    if (infiniteSky) {
      coverageLayer.mesh.visible = false;
      scene.background = coverageLayer.mesh.material.map;
      warnings.push("Infinite sky uses full source UV0..1 as screen-filling background; it has no finite world anchor. Foreground alpha boundaries still require visual review.");
    }
    scene.add(group);
    const travelLimit = descriptor.maximumProjectedTravelFraction ?? (layers?.length ? Infinity : 0.08);
    const bounds = { worldWidth, worldHeight, paddingFraction: pad, paddedWidth: worldWidth * (1 + 2 * pad), paddedHeight: worldHeight * (1 + 2 * pad), minZ, maxZ, maximumProjectedTravelFraction: Number.isFinite(travelLimit) ? travelLimit : null, backgroundMode: infiniteSky ? "infinite-sky-screen-pass" : "finite-source-plane" };
    let reference = null;
    const anchors = [new THREE2.Vector3(0, 0, 0)];
    for (const z of [minZ, maxZ]) for (const x of [-worldWidth / 2, 0, worldWidth / 2]) for (const y of [-worldHeight / 2, 0, worldHeight / 2]) anchors.push(new THREE2.Vector3(x, y, z));
    const projected = (point, cam) => point.clone().applyMatrix4(group.matrixWorld).project(cam);
    function setReferenceCamera(camera) {
      camera.updateMatrixWorld(true);
      const distance = descriptor.referenceDistance ?? Math.max(0.5, camera.position.length());
      const cropReserve = descriptor.cropReserve ?? 0.08;
      const farDistance = layers?.length ? distance : Math.max(distance, distance - minZ);
      const fittedHeight = 2 * farDistance * Math.tan(camera.fov * Math.PI / 360) * (1 + cropReserve);
      group.quaternion.copy(camera.quaternion);
      group.position.copy(camera.position).add(new THREE2.Vector3(0, 0, -distance).applyQuaternion(camera.quaternion));
      group.scale.set(fittedHeight * camera.aspect / worldWidth, fittedHeight / worldHeight, 1);
      for (const layer of layerRecords) {
        const z = layer.entry.z ?? 0;
        const scale = layers?.length ? (distance - z) / distance : 1;
        if (scale <= 0) throw new Error("Layer " + layer.id + " lies at or behind the initial camera");
        layer.registrationScale = scale;
        layer.group.scale.set(scale, scale, 1);
      }
      if (layers?.length) {
        anchors.length = 1;
        for (const layer of layerRecords.filter((l) => !infiniteSky || l !== coverageLayer)) for (const z of [layer.minZ, layer.maxZ]) for (const x of [-worldWidth / 2, 0, worldWidth / 2]) for (const y of [-worldHeight / 2, 0, worldHeight / 2]) anchors.push(new THREE2.Vector3(x * layer.registrationScale, y * layer.registrationScale, z));
      }
      bounds.layerRegistration = layerRecords.map((l) => ({ id: l.id, z: l.entry.z ?? 0, xyScale: l.registrationScale, coverageRequired: !infiniteSky && (l === coverageLayer || !layers?.length), renderMode: infiniteSky && l === coverageLayer ? "screen-background-at-infinity" : "world-plane" }));
      group.updateMatrixWorld(true);
      reference = camera.clone();
      reference.updateMatrixWorld(true);
      bounds.initialFraming = { distance, cropReserve, sourceScale: group.scale.toArray(), sourcePosition: group.position.toArray(), sourceQuaternion: group.quaternion.toArray() };
      const coverage = measureCoverage(camera);
      if (!coverage.safe) throw new Error("Initial camera cannot safely cover true source UVs: " + JSON.stringify(coverage));
      return { position: reference.position.toArray(), quaternion: reference.quaternion.toArray(), fov: reference.fov, coverage, sourceTransform: group.matrixWorld.toArray() };
    }
    function sourcePoint(u, v, z = 0) {
      group.updateMatrixWorld(true);
      return new THREE2.Vector3((u - 0.5) * worldWidth, (v - 0.5) * worldHeight, z).applyMatrix4(group.matrixWorld);
    }
    function layerSourceGroup(layerId) {
      const layer = layerRecords.find((l) => l.id === layerId);
      if (!layer) throw new Error("Unknown source layer " + layerId);
      if (infiniteSky && layer === coverageLayer) throw new Error("Infinite sky has no world-space anchor group");
      return layer.group;
    }
    function layerSourcePoint(layerId, u, v, zOffset = 0) {
      const layer = layerRecords.find((l) => l.id === layerId);
      if (!layer) throw new Error("Unknown source layer " + layerId);
      if (infiniteSky && layer === coverageLayer) throw new Error("Infinite sky has no finite world point");
      group.updateMatrixWorld(true);
      return new THREE2.Vector3((u - 0.5) * worldWidth, (v - 0.5) * worldHeight, (layer.entry.z ?? 0) + zOffset).applyMatrix4(layer.group.matrixWorld);
    }
    function measureCoverage(camera) {
      camera.updateMatrixWorld(true);
      group.updateMatrixWorld(true);
      if (infiniteSky) return {
        safe: true,
        uvBounds: { minU: 0, maxU: 1, minV: 0, maxV: 1 },
        insetU: 0,
        insetV: 0,
        coverageLayer: coverageLayer.id,
        backgroundMode: "infinite-sky-screen-pass",
        foregroundCoverageRequired: false,
        foregroundOutsideUV: "transparent-discard",
        usesRepeatedEdgePixels: false,
        opacityQA: "source-sky-alpha-must-be-opaque"
      };
      const coverageGroup = coverageLayer?.group || group;
      const inverse = coverageGroup.matrixWorld.clone().invert();
      const worldOrigin = new THREE2.Vector3().setFromMatrixPosition(camera.matrixWorld);
      const origin = worldOrigin.clone().applyMatrix4(inverse);
      const uvBounds = { minU: Infinity, maxU: -Infinity, minV: Infinity, maxV: -Infinity };
      let safe = true;
      for (const nx of [-1, 1]) for (const ny of [-1, 1]) {
        const worldPoint = new THREE2.Vector3(nx, ny, 0.5).unproject(camera);
        const direction = worldPoint.sub(worldOrigin).transformDirection(inverse);
        if (direction.z >= -1e-8) {
          safe = false;
          continue;
        }
        for (const z of coverageLayer ? [coverageLayer.minZ, coverageLayer.maxZ] : [minZ, maxZ]) {
          const t = (z - origin.z) / direction.z;
          if (t <= 0) {
            safe = false;
            continue;
          }
          const u = (origin.x + t * direction.x) / worldWidth + 0.5, v = (origin.y + t * direction.y) / worldHeight + 0.5;
          uvBounds.minU = Math.min(uvBounds.minU, u);
          uvBounds.maxU = Math.max(uvBounds.maxU, u);
          uvBounds.minV = Math.min(uvBounds.minV, v);
          uvBounds.maxV = Math.max(uvBounds.maxV, v);
        }
      }
      const insetU = 1 / width, insetV = 1 / height;
      safe = safe && Object.values(uvBounds).every(Number.isFinite) && uvBounds.minU >= insetU && uvBounds.maxU <= 1 - insetU && uvBounds.minV >= insetV && uvBounds.maxV <= 1 - insetV;
      return { safe, uvBounds, insetU, insetV, coverageLayer: coverageLayer?.id ?? "plate", foregroundCoverageRequired: false, foregroundOutsideUV: "transparent-discard", usesRepeatedEdgePixels: !safe };
    }
    function measure(camera) {
      if (!reference) throw new Error("Call setReferenceCamera(camera) at the shot initial pose first");
      camera.updateMatrixWorld(true);
      group.updateMatrixWorld(true);
      let max = 0;
      for (let i = 0; i < anchors.length; i++) {
        const p = anchors[i], a = projected(p, camera), b = projected(p, reference);
        if (i) {
          const flat = new THREE2.Vector3(p.x, p.y, 0), af = projected(flat, camera), bf = projected(flat, reference);
          a.sub(af);
          b.sub(bf);
        }
        max = Math.max(max, Math.abs(a.x - b.x) / 2, Math.abs(a.y - b.y) * height / width / 2);
      }
      return max;
    }
    function foregroundDiagnostics(camera) {
      if (!layers?.length) return [];
      camera.updateMatrixWorld(true);
      group.updateMatrixWorld(true);
      return layerRecords.filter((layer) => layer !== coverageLayer).map((layer) => {
        const corners = [];
        for (const u of [0, 1]) for (const v of [0, 1]) {
          const point = layerSourcePoint(layer.id, u, v), view = point.clone().applyMatrix4(camera.matrixWorldInverse), ndc = point.project(camera);
          corners.push({ u, v, ndc: ndc.toArray(), inFront: view.z < 0 });
        }
        const finite = corners.every((c) => c.ndc.every(Number.isFinite));
        const bounds2 = finite ? { minX: Math.min(...corners.map((c) => c.ndc[0])), maxX: Math.max(...corners.map((c) => c.ndc[0])), minY: Math.min(...corners.map((c) => c.ndc[1])), maxY: Math.max(...corners.map((c) => c.ndc[1])) } : null;
        return {
          id: layer.id,
          z: layer.entry.z,
          registrationScale: layer.registrationScale,
          projectedSourceBounds: bounds2,
          allSourceCornersInFront: corners.every((c) => c.inFront),
          allSourceCornersInsideViewport: finite && corners.every((c) => c.inFront && Math.abs(c.ndc[0]) <= 1 && Math.abs(c.ndc[1]) <= 1),
          boundaryPolicy: "Fragments outside source UV0..1 discard to reveal background; alpha-cut content requires visual review.",
          projectedCorners: corners
        };
      });
    }
    function constrainCamera(camera) {
      if (!reference) throw new Error("Reference camera must be set before constraining");
      const requested = measure(camera), requestedCoverage = measureCoverage(camera);
      const p = camera.position.clone(), q = camera.quaternion.clone(), fov = camera.fov;
      const apply = (fraction2) => {
        camera.position.copy(reference.position).lerp(p, fraction2);
        camera.quaternion.copy(reference.quaternion).slerp(q, fraction2);
        camera.fov = reference.fov + (fov - reference.fov) * fraction2;
        camera.updateProjectionMatrix();
        camera.updateMatrixWorld(true);
      };
      let fraction = 1, actual = requested, coverage = requestedCoverage;
      const acceptable = () => Number.isFinite(actual) && actual <= travelLimit && coverage.safe;
      if (!infiniteSky && !acceptable()) {
        let low = 0, high = 1;
        for (let i = 0; i < 18; i++) {
          const mid = (low + high) / 2;
          apply(mid);
          actual = measure(camera);
          coverage = measureCoverage(camera);
          if (acceptable()) low = mid;
          else high = mid;
        }
        fraction = low;
        apply(fraction);
        actual = measure(camera);
        coverage = measureCoverage(camera);
        if (!acceptable()) throw new Error("Coverage clamp failed to find a safe source pose");
      }
      return {
        clamped: fraction < 1,
        retainedMoveFraction: fraction,
        requestedProjectedTravelFraction: requested,
        actualProjectedTravelFraction: actual,
        coverageClamped: !requestedCoverage.safe,
        requestedCoverage,
        actualCoverage: coverage,
        requestedCameraPosition: p.toArray(),
        actualCameraPosition: camera.position.toArray(),
        requestedCameraQuaternion: q.toArray(),
        actualCameraQuaternion: camera.quaternion.toArray(),
        sourceCropReserve: descriptor.cropReserve ?? 0.08,
        backgroundMode: bounds.backgroundMode,
        foregroundLayers: foregroundDiagnostics(camera),
        requiresVisualEdgeQA: true
      };
    }
    function dispose() {
      scene.remove(group);
      if (infiniteSky && scene.background === coverageLayer.mesh.material.map) scene.background = previousBackground;
      for (const item of resources) item.dispose();
    }
    return {
      group,
      sourceGroup: group,
      sourcePoint,
      layerSourcePoint,
      layerSourceGroup,
      meshes,
      geometry: meshes[0]?.geometry,
      bounds,
      mode,
      warnings,
      setReferenceCamera,
      measureProjectedTravel: measure,
      measureCoverage,
      foregroundDiagnostics,
      constrainCamera,
      dispose,
      provenance: { depth: depth?.provenance ?? (depth ? "supplied-unverified" : "none"), layers: entries.map((e) => ({ id: e.id || "plate", depth: e.depth?.provenance ?? (e.depth ? "supplied-unverified" : "none"), z: e.z ?? 0 })), depthInferencePerformed: false },
      update(camera) {
        if (!camera || !layers?.length) return;
        camera.updateMatrixWorld(true);
        group.updateMatrixWorld(true);
        const center = new THREE2.Vector3();
        meshes.map((mesh) => {
          mesh.geometry.boundingBox.getCenter(center);
          return { mesh, z: center.clone().applyMatrix4(mesh.matrixWorld).applyMatrix4(camera.matrixWorldInverse).z };
        }).sort((a, b) => a.z - b.z).forEach(({ mesh }, i) => mesh.renderOrder = i);
      }
    };
  }

  // episodes/first-day-anime2/project/src/effects.mjs
  var PALETTE = Object.freeze({ clay: "#D97757", ivory: "#FAF9F5", paper: "#F0EEE6", slate: "#191919", grey: "#B0AEA5", sky: "#6A9BCB", olive: "#788C5D", fig: "#C46686" });
  var EFFECT_NAMES = ["TokenTunnel", "Shatter", "ToastShatter", "GlassCrack", "InkBloom", "Mosaic", "SpeedLines"];
  var clamp2 = (x) => Math.max(0, Math.min(1, x));
  var ease = (x) => {
    x = clamp2(x);
    return x * x * (3 - 2 * x);
  };
  function seededRandom(seed = 5505) {
    return () => {
      seed |= 0;
      seed = seed + 1831565813 | 0;
      let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
      t ^= t + Math.imul(t ^ t >>> 7, 61 | t);
      return ((t ^ t >>> 14) >>> 0) / 4294967296;
    };
  }
  function voronoiCells(count = 240, seed = 55) {
    const rnd = seededRandom(seed), sites = Array.from({ length: count }, () => [rnd() * 2 - 1, rnd() * 2 - 1]);
    return sites.map((s, i) => {
      let poly = [[-1, -1], [1, -1], [1, 1], [-1, 1]];
      sites.forEach((t, j) => {
        if (i === j || !poly.length) return;
        const nx = t[0] - s[0], ny = t[1] - s[1], c = (t[0] ** 2 + t[1] ** 2 - s[0] ** 2 - s[1] ** 2) / 2;
        const out = [];
        for (let k = 0; k < poly.length; k++) {
          const a = poly[k], b = poly[(k + 1) % poly.length], da = a[0] * nx + a[1] * ny - c, db = b[0] * nx + b[1] * ny - c;
          if (da <= 1e-9) out.push(a);
          if (da < 0 !== db < 0) {
            const u = da / (da - db);
            out.push([a[0] + u * (b[0] - a[0]), a[1] + u * (b[1] - a[1])]);
          }
        }
        poly = out;
      });
      return { site: s, polygon: poly };
    });
  }
  var outputShader = (fragment) => fragment.replace(/}\s*$/, "\n#include <colorspace_fragment>\n}");
  var quadVertex = `varying vec2 vUv;void main(){vUv=uv;gl_Position=vec4(position.xy,0.,1.);}`;
  var noiseGLSL = `float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453123);}float noise(vec2 p){vec2 i=floor(p),f=fract(p);f=f*f*(3.-2.*f);return mix(mix(hash(i),hash(i+vec2(1,0)),f.x),mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x),f.y);}float fbm(vec2 p){float v=0.,a=.5;for(int i=0;i<5;i++){v+=a*noise(p);p=mat2(.8,-.6,.6,.8)*p*2.03;a*=.5;}return v;}vec2 curl(vec2 p){float e=.025;return vec2(fbm(p+vec2(0,e))-fbm(p-vec2(0,e)),-fbm(p+vec2(e,0))+fbm(p-vec2(e,0)))/(2.*e);}`;
  function createEffect(name, { THREE: T, scene, camera, renderer, assets = {}, width = 1920, height = 1080 }) {
    if (!EFFECT_NAMES.includes(name)) throw new Error(`Unknown effect: ${name}`);
    const root = new T.Group();
    root.name = `OPUS55:${name}`;
    scene.add(root);
    const owned = [], pending = [], rnd = seededRandom(5505), aspect = width / height;
    const own = (x) => (owned.push(x), x);
    const color = (x) => new T.Color(x);
    const texture = (key) => {
      const value = assets[key];
      if (value?.isTexture) return value;
      if (typeof value !== "string") throw new Error(`${name} requires assets.${key}`);
      let tx;
      pending.push(new Promise((ok, no) => {
        tx = new T.TextureLoader().load(value, ok, void 0, no);
      }));
      tx.colorSpace = T.SRGBColorSpace;
      return own(tx);
    };
    const plane = (fragment, uniforms, transparent = false) => {
      const material = own(new T.ShaderMaterial({ vertexShader: quadVertex, fragmentShader: outputShader(fragment), uniforms, transparent, depthTest: false, depthWrite: false }));
      const mesh = new T.Mesh(own(new T.PlaneGeometry(2, 2)), material);
      mesh.frustumCulled = false;
      root.add(mesh);
      return mesh;
    };
    const setCamera = (z, fov = 45, x = 0, y = 0) => {
      camera.position.set(x, y, z);
      camera.lookAt(0, 0, 0);
      if (camera.isPerspectiveCamera) {
        camera.fov = fov;
        camera.aspect = aspect;
        camera.updateProjectionMatrix();
      }
    };
    let tick = () => {
    };
    const metadata = { name, deterministic: true, bloom: { threshold: 0.8, intensity: 0.6 } };
    function atlasMesh(count, map, columns, rows, additive = false) {
      const geometry = own(new T.PlaneGeometry(1, 1));
      geometry.setAttribute("tile", new T.InstancedBufferAttribute(Float32Array.from({ length: count }, (_, i) => i % (columns * rows)), 1));
      const material = own(new T.ShaderMaterial({ uniforms: { atlas: { value: map }, grid: { value: new T.Vector2(columns, rows) }, tint: { value: color(PALETTE.ivory) }, emission: { value: 1 } }, vertexShader: `attribute float tile;uniform vec2 grid;varying vec2 vUv;void main(){vUv=(vec2(mod(tile,grid.x),grid.y-1.-floor(tile/grid.x))+uv)/grid;gl_Position=projectionMatrix*modelViewMatrix*instanceMatrix*vec4(position,1.);}`, fragmentShader: outputShader(`uniform sampler2D atlas;uniform vec3 tint;uniform float emission;varying vec2 vUv;void main(){vec4 c=texture2D(atlas,vUv);if(c.a<.01)discard;gl_FragColor=vec4(c.rgb*tint*emission,c.a);}`), transparent: true, depthWrite: !additive, side: T.DoubleSide, blending: additive ? T.AdditiveBlending : T.NormalBlending }));
      const mesh = new T.InstancedMesh(geometry, material, count);
      mesh.frustumCulled = false;
      root.add(mesh);
      return mesh;
    }
    if (name === "TokenTunnel") {
      const mesh = atlasMesh(6e3, texture("glyphAtlas"), assets.glyphColumns || 8, assets.glyphRows || 8, true), dummy = new T.Object3D();
      metadata.instances = 6e3;
      const path = new T.CatmullRomCurve3([new T.Vector3(0, 0, 8), new T.Vector3(-2, 1, -10), new T.Vector3(2, -1, -30), new T.Vector3(-1, 2, -60), new T.Vector3(0, 0, -100)]);
      const particles = Array.from({ length: 6e3 }, () => ({ u: rnd(), angle: rnd() * Math.PI * 2, r: 2 + rnd() * 6, size: 0.055 + rnd() * 0.22, roll: rnd() * 6.28 }));
      tick = (f, p) => {
        const travel = p * 0.67;
        const c = path.getPoint(travel), target = path.getPoint(Math.min(0.999, travel + 0.07));
        camera.position.copy(c);
        camera.lookAt(target);
        camera.fov = 48 + 40 * ease(p);
        camera.updateProjectionMatrix();
        particles.forEach((v, i) => {
          const pt = path.getPoint(v.u);
          dummy.position.set(pt.x + Math.cos(v.angle + p * 0.25) * v.r, pt.y + Math.sin(v.angle + p * 0.25) * v.r, pt.z);
          dummy.quaternion.copy(camera.quaternion);
          dummy.rotateZ(v.roll);
          dummy.scale.set(v.size, v.size, 1);
          dummy.updateMatrix();
          mesh.setMatrixAt(i, dummy.matrix);
        });
        mesh.instanceMatrix.needsUpdate = true;
        mesh.material.uniforms.tint.value.copy(color(PALETTE.grey)).lerp(color(PALETTE.clay), ease(p));
        mesh.material.uniforms.emission.value = 1.4;
      };
    } else if (name === "Shatter" || name === "ToastShatter") {
      const count = name === "Shatter" ? 240 : 40, tex = texture(name === "Shatter" ? "egg" : "toast"), cells = voronoiCells(count);
      metadata.shards = count;
      metadata.gravity = 0.3;
      const key = new T.PointLight(PALETTE.clay, 65, 30, 2);
      key.position.set(-3, 4, 6);
      root.add(key);
      root.add(new T.AmbientLight(PALETTE.ivory, 1.5));
      const shards = cells.map(({ site, polygon }) => {
        const [cx, cy] = site, positions = [], uvs = [];
        for (let j = 1; j < polygon.length - 1; j++) for (const [x, y] of [polygon[0], polygon[j], polygon[j + 1]]) {
          positions.push((x - cx) * aspect * 3, (y - cy) * 3, 0);
          uvs.push((x + 1) / 2, (y + 1) / 2);
        }
        const g = own(new T.BufferGeometry());
        g.setAttribute("position", new T.Float32BufferAttribute(positions, 3));
        g.setAttribute("uv", new T.Float32BufferAttribute(uvs, 2));
        g.computeVertexNormals();
        const m = own(new T.MeshStandardMaterial({ map: tex, roughness: 0.88, metalness: 0, side: T.DoubleSide, transparent: true }));
        const obj = new T.Mesh(g, m);
        root.add(obj);
        return { obj, x: cx * aspect * 3, y: cy * 3, z: rnd() * 4 + 1, rx: rnd() * 5 - 2.5, ry: rnd() * 5 - 2.5, rz: rnd() * 3 - 1.5 };
      });
      tick = (f, p) => {
        setCamera(8 - p * 0.8, 45);
        const t = p * 2.6;
        shards.forEach((s) => {
          s.obj.position.set(s.x * (1 + t * 0.95), s.y * (1 + t * 0.95) - 0.5 * 0.3 * t * t, s.z * t);
          s.obj.rotation.set(s.rx * t, s.ry * t, s.rz * t);
          s.obj.material.opacity = 1 - ease((p - 0.78) / 0.22);
        });
      };
    } else if (name === "GlassCrack") {
      const tex = texture("plate"), cells = voronoiCells(90, 20), positions = [];
      cells.forEach(({ polygon }) => polygon.forEach((a, i) => {
        const b = polygon[(i + 1) % polygon.length];
        positions.push(a[0] * aspect * 3, a[1] * 3, 0, b[0] * aspect * 3, b[1] * 3, 0);
      }));
      const ribbons = [];
      for (let i = 0; i < positions.length; i += 6) {
        const ax = positions[i], ay = positions[i + 1], bx = positions[i + 3], by = positions[i + 4], len = Math.hypot(bx - ax, by - ay) || 1, dx = -(by - ay) / len * 8e-3, dy = (bx - ax) / len * 8e-3;
        for (const v of [[ax + dx, ay + dy], [ax - dx, ay - dy], [bx + dx, by + dy], [ax - dx, ay - dy], [bx - dx, by - dy], [bx + dx, by + dy]]) ribbons.push(v[0], v[1], 0);
      }
      const g = own(new T.BufferGeometry());
      g.setAttribute("position", new T.Float32BufferAttribute(ribbons, 3));
      const mat = own(new T.MeshBasicMaterial({ color: PALETTE.clay, transparent: true, opacity: 0, side: T.DoubleSide, blending: T.NormalBlending }));
      const lines = new T.Mesh(g, mat);
      root.add(lines);
      const uniforms = { plate: { value: tex }, progress: { value: 0 }, aspect: { value: aspect } };
      const bg = plane(`varying vec2 vUv;uniform sampler2D plate;uniform float progress,aspect;${noiseGLSL}void main(){vec2 p=vUv-.5;float r=length(p*vec2(aspect,1.));vec2 shift=normalize(p+vec2(.0001))*sin(r*70.-progress*8.)*.018*progress;vec3 c=texture2D(plate,vUv+shift).rgb;float light=smoothstep(.82,1.,progress);gl_FragColor=vec4(mix(c,vec3(1.),light),1.);}`, uniforms);
      bg.renderOrder = -5;
      tick = (f, p) => {
        uniforms.progress.value = p;
        mat.opacity = ease(p * 4) * (1 - ease((p - 0.8) / 0.2));
        mat.color.copy(color(PALETTE.clay)).multiplyScalar(1.4);
        lines.scale.setScalar(1 + p * 0.4);
        setCamera(7 - 9 * Math.pow(p, 2), 40 + 40 * p);
      };
    } else if (name === "InkBloom") {
      metadata.sourceFrames = 90;
      metadata.method = "analytic backwards curl-noise dye advection; deterministic random-access shader";
      const u = { time: { value: 0 }, progress: { value: 0 }, aspect: { value: aspect }, clay: { value: color(PALETTE.clay) }, sky: { value: color(PALETTE.sky) }, olive: { value: color(PALETTE.olive) }, fig: { value: color(PALETTE.fig) }, paper: { value: color(PALETTE.paper) } };
      plane(`varying vec2 vUv;uniform float time,progress,aspect;uniform vec3 clay,sky,olive,fig,paper;${noiseGLSL}float dye(vec2 p,vec2 origin,float seed){vec2 q=p;for(int i=0;i<9;i++){q-=curl(q*2.+seed+time*.07)*(.008+progress*.018);}float d=length(q-origin);float edge=.045+progress*.65+fbm(q*9.+seed)*.12;return 1.-smoothstep(edge-.065,edge+.045,d);}void main(){vec2 p=(vUv-.5)*vec2(aspect,1.)/(1.+progress*.35);float a=dye(p,vec2(-.40,.15),1.),b=dye(p,vec2(.36,.18),4.),c=dye(p,vec2(-.25,-.26),8.),d=dye(p,vec2(.31,-.25),14.);float total=a+b+c+d;vec3 pigment=(clay*a+sky*b+olive*c+fig*d)/max(total,.0001);vec3 col=mix(paper,pigment,clamp(total,0.,1.)*.94);col+=(hash(gl_FragCoord.xy)-.5)/255.;col=mix(col,vec3(1.),smoothstep(.87,1.,progress));gl_FragColor=vec4(col,1.);}`, u);
      tick = (f, p) => {
        u.time.value = p * 89 / 30;
        u.progress.value = p;
      };
    } else if (name === "SpeedLines") {
      metadata.lines = 32;
      const u = { time: { value: 0 }, aspect: { value: aspect }, ink: { value: color(PALETTE.clay) }, progress: { value: 0 } };
      plane(`varying vec2 vUv;uniform float time,aspect,progress;uniform vec3 ink;void main(){vec2 p=(vUv-.5)*vec2(aspect,1.);float r=length(p);float a=atan(p.y,p.x);float slot=(a+3.14159265)/6.2831853*32.;float id=floor(slot);float width=.025+.025*sin(id*4.13);float ray=1.-smoothstep(width,width+.012,abs(fract(slot)-.5));float start=.16+.22*(.5+.5*sin(id*2.37+time*15.));float len=.35+.25*sin(id*1.8+time*8.);float mask=smoothstep(start,start+.035,r)*(1.-smoothstep(start+len,start+len+.1,r));gl_FragColor=vec4(ink*1.2,ray*mask*.72);}`, u, true);
      tick = (f, p) => {
        u.time.value = f / 30;
        u.progress.value = p;
      };
    } else if (name === "Mosaic") {
      const atlas = texture("mosaicAtlas");
      let contains = assets.sparkContains;
      if (!contains) {
        if (typeof assets.sparkSVG !== "string") throw new Error("Mosaic needs raw assets.sparkSVG or sparkContains");
        if (typeof document === "undefined") throw new Error("SVG mask sampling needs browser canvas or sparkContains");
        const doc = new DOMParser().parseFromString(assets.sparkSVG, "image/svg+xml"), svg = doc.documentElement;
        const box = (svg.getAttribute("viewBox") || "0 0 100 100").split(/[ ,]+/).map(Number);
        const paths = [...doc.querySelectorAll("path")].map((p) => new Path2D(p.getAttribute("d")));
        const ctx = document.createElement("canvas").getContext("2d");
        contains = (x, y) => paths.some((path) => ctx.isPointInPath(path, box[0] + x * box[2], box[1] + y * box[3]));
      }
      const points = [];
      for (let tries = 0; points.length < 600 && tries < 1e5; tries++) {
        const x = rnd(), y = rnd();
        if (contains(x, y)) points.push([x, y]);
      }
      if (points.length !== 600) throw new Error("Spark mask rejection sampler failed to place 600 tiles");
      const mesh = atlasMesh(600, atlas, assets.mosaicColumns || 30, assets.mosaicRows || 20, false), dummy = new T.Object3D();
      metadata.tiles = 600;
      metadata.mask = "provided spark SVG paths, normalized viewBox";
      points.forEach(([x, y], i) => {
        dummy.position.set((x - 0.5) * 10, (0.5 - y) * 10, (rnd() - 0.5) * 0.11);
        dummy.rotation.set(0, 0, (rnd() - 0.5) * 0.09);
        dummy.scale.set(0.26, 0.26 / aspect, 1);
        dummy.updateMatrix();
        mesh.setMatrixAt(i, dummy.matrix);
      });
      mesh.instanceMatrix.needsUpdate = true;
      mesh.material.uniforms.emission.value = 1.1;
      tick = (f, p) => {
        mesh.rotation.z = 0.1 * (1 - p);
        mesh.rotation.y = 0.13 * Math.sin(p * Math.PI);
        setCamera(1.3 * Math.pow(26, p), 40);
      };
    }
    return { root, metadata, ready: Promise.all(pending), update(frame, progress) {
      tick(frame, clamp2(progress));
    }, dispose() {
      scene.remove(root);
      for (const x of owned) x.dispose();
    } };
  }

  // episodes/first-day-anime2/project/src/title3d.mjs
  var clamp3 = (x) => Math.max(0, Math.min(1, x));
  function titleSlamDescriptor(frame, duration = 21) {
    const f = Math.max(0, frame), u = clamp3(f / 5), remainder = (Math.exp(-5 * u) * Math.cos(7 * u) - Math.exp(-5) * Math.cos(7)) / (1 - Math.exp(-5) * Math.cos(7));
    const decay = 1 - clamp3(f / 20), shakeAmplitude = 14 * decay;
    return { scale: f >= 5 ? 1 : 1 + 2 * remainder, shakeAmplitude, shakePixels: [Math.sin(f * 9.13) * shakeAmplitude, Math.cos(f * 7.71) * shakeAmplitude], shockRadius: 0.15 + f * 0.2, shockOpacity: 1 - clamp3(f / 12), parallax: clamp3((f - duration * 0.65) / (duration * 0.35)), capHeightPixelsAt1080: 180, depth: 0.35 };
  }
  function createTitleSlam({ THREE: T, scene, svgPaths, sparkSVG, SVGLoader: SVGLoader2, camera = null, width = 1920, height = 1080, capHeight = 2, fitCamera = true, position = [0, 0, 0] }) {
    if (!T || !scene || !SVGLoader2 || !svgPaths?.left || !svgPaths?.right || !sparkSVG) throw new Error("TitleSlam requires THREE, scene, SVGLoader, svgPaths.left/right, sparkSVG");
    const root = new T.Group();
    root.name = "OPUS55:TitleSlam";
    root.position.set(...position);
    scene.add(root);
    const word = new T.Group();
    root.add(word);
    const owned = [];
    const own = (x) => (owned.push(x), x);
    const face = own(new T.MeshBasicMaterial({ color: "#FAF9F5" })), side = own(new T.MeshBasicMaterial({ color: "#D97757" })), bevel = own(new T.MeshBasicMaterial({ color: "#191919" }));
    const coralFace = own(new T.MeshBasicMaterial({ color: "#D97757" }));
    const materials = [face, side, bevel];
    const parse = (svg) => typeof svg === "string" ? new SVGLoader2().parse(svg) : svg;
    const attr = (svg, key, fallback) => typeof svg === "string" ? Number(svg.match(new RegExp(`${key}="([0-9.]+)"`))?.[1] || fallback) : fallback;
    const counts = { shapes: 0, triangles: 0, face: 0, side: 0, bevel: 0 };
    function geometry(shape, unitsPerWorld) {
      let g = new T.ExtrudeGeometry(shape, { depth: 0.35 * unitsPerWorld, bevelEnabled: true, bevelThickness: 8e-3 * unitsPerWorld, bevelSize: 8e-3 * unitsPerWorld, bevelSegments: 2, steps: 1, curveSegments: 18 });
      if (g.index) {
        const unindexed = g.toNonIndexed();
        g.dispose();
        g = unindexed;
      }
      g.clearGroups();
      const normal = g.attributes.normal;
      let runStart = 0, last = -1;
      for (let i = 0; i < normal.count; i += 3) {
        const z = (Math.abs(normal.getZ(i)) + Math.abs(normal.getZ(i + 1)) + Math.abs(normal.getZ(i + 2))) / 3;
        const type = z > 0.9999 ? 0 : z < 1e-4 ? 1 : 2;
        counts[["face", "side", "bevel"][type]]++;
        if (type !== last) {
          if (last !== -1) g.addGroup(runStart, i - runStart, last);
          runStart = i;
          last = type;
        }
      }
      if (last !== -1) g.addGroup(runStart, normal.count - runStart, last);
      counts.shapes++;
      counts.triangles += normal.count / 3;
      return own(g);
    }
    function build(svg, unitsPerWorld, mats = materials) {
      const group = new T.Group();
      for (const p of parse(svg).paths) for (const shape of SVGLoader2.createShapes(p)) group.add(new T.Mesh(geometry(shape, unitsPerWorld), mats));
      group.scale.set(1 / unitsPerWorld, -1 / unitsPerWorld, 1 / unitsPerWorld);
      return group;
    }
    const leftCap = attr(svgPaths.left, "data-cap-height", 1340), rightCap = attr(svgPaths.right, "data-cap-height", 1340);
    const leftWidth = attr(svgPaths.left, "data-advance", 7984) / leftCap * capHeight, rightWidth = attr(svgPaths.right, "data-advance", 1400) / rightCap * capHeight;
    const gap = capHeight * 0.13, sparkSize = capHeight * 0.25, totalWidth = leftWidth + rightWidth + 2 * gap + sparkSize;
    const left = build(svgPaths.left, leftCap / capHeight);
    left.position.set(-totalWidth / 2, capHeight / 2, 0);
    word.add(left);
    const sparkViewBox = typeof sparkSVG === "string" ? sparkSVG.match(/viewBox="([^"]+)"/)?.[1]?.trim().split(/[ ,]+/).map(Number) : null;
    const sparkUnits = Math.max(sparkViewBox?.[2] || 100, sparkViewBox?.[3] || 100) / sparkSize;
    const spark = build(sparkSVG, sparkUnits, [coralFace, side, bevel]);
    const sb = new T.Box3().setFromObject(spark), ss = new T.Vector3(), sc = new T.Vector3();
    sb.getSize(ss);
    sb.getCenter(sc);
    const sparkScale = sparkSize / Math.max(ss.x, ss.y);
    const sparkWrapper = new T.Group();
    sparkWrapper.add(spark);
    sparkWrapper.scale.set(sparkScale, sparkScale, 1);
    spark.position.x -= sc.x;
    spark.position.y -= sc.y;
    sparkWrapper.position.set(-totalWidth / 2 + leftWidth + gap + sparkSize / 2, -capHeight / 2 + sparkSize * 0.6, 0);
    word.add(sparkWrapper);
    const right = build(svgPaths.right, rightCap / capHeight);
    right.position.set(-totalWidth / 2 + leftWidth + 2 * gap + sparkSize, capHeight / 2, 0);
    word.add(right);
    const ringMaterial = own(new T.MeshBasicMaterial({ color: "#D97757", transparent: true, opacity: 1, side: T.DoubleSide, depthWrite: false }));
    const ring = new T.Mesh(own(new T.RingGeometry(0.975, 1, 128)), ringMaterial);
    ring.position.z = -0.05;
    root.add(ring);
    const worldHeight = capHeight * 1080 / 180, worldPerPixel = worldHeight / height;
    if (camera && fitCamera) {
      if (camera.isPerspectiveCamera) {
        camera.aspect = width / height;
        camera.position.set(position[0], position[1], position[2] + worldHeight / (2 * Math.tan(camera.fov * Math.PI / 360)));
        camera.lookAt(...position);
      } else if (camera.isOrthographicCamera) {
        camera.top = worldHeight / 2;
        camera.bottom = -worldHeight / 2;
        camera.left = -worldHeight * width / height / 2;
        camera.right = -camera.left;
        camera.position.set(position[0], position[1], position[2] + 15);
        camera.lookAt(...position);
      }
      camera.updateProjectionMatrix();
    }
    const metadata = { text: "OPUS 5\u27315", sourceText: "OPUS 5.5", font: "Newsreader", weight: 800, opticalSize: 72, capHeight, capHeightPixelsAt1080: 180, totalWidth, worldHeight, depth: 0.35, geometry: counts, spark: "Exact supplied SVG, no unicode asterisk substitution", settledWidthFraction: totalWidth / (worldHeight * width / height) };
    return { root, metadata, update(frame, duration = 21) {
      const d = titleSlamDescriptor(frame, duration);
      word.scale.setScalar(d.scale);
      word.position.set(d.shakePixels[0] * worldPerPixel + d.parallax * 0.14, d.shakePixels[1] * worldPerPixel, 0);
      word.rotation.y = -0.08 * d.parallax;
      ring.scale.setScalar(d.shockRadius * capHeight);
      ringMaterial.opacity = d.shockOpacity;
      return d;
    }, dispose() {
      scene.remove(root);
      for (const x of owned) x.dispose();
    } };
  }

  // episodes/first-day-anime2/project/src/graphics.mjs
  var C = { clay: "#D97757", ivory: "#FAF9F5", paper: "#F0EEE6", slate: "#191919", grey: "#B0AEA5", oat: "#E3DACC" };
  var clamp4 = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
  var ease2 = (x) => 1 - (1 - clamp4(x)) ** 3;
  var spring = (t) => t <= 0 ? 0 : 1 - Math.exp(-6 * t) * (Math.cos(Math.sqrt(164) * t) + 6 / Math.sqrt(164) * Math.sin(Math.sqrt(164) * t));
  var font = (family, size, weight = 500) => `${weight} ${size}px "${family}"`;
  function createGraphics({ width = 1920, height = 1080, sync: sync2, shots: shots2, onsets = {}, fonts = {}, brand = {} }) {
    if (!sync2 || !Array.isArray(shots2)) throw new Error("Graphics requires sync and shots");
    const fps = sync2.fps || 30, toFrame = (t) => Math.round(t * fps), byId = Object.fromEntries(shots2.map((s) => [s.id, s]));
    const families = { serif: "Noto Serif SC", sans: "Noto Sans SC", hand: "LXGW WenKai", display: "Newsreader", ui: "Inter", mono: "JetBrains Mono", ...fonts };
    const lyrics = sync2.lyrics || [], kickFrames = (onsets.kicks || []).map(toFrame);
    const safe = { x: 96, y: 54, w: 1728, h: 972 };
    const canvas = (w = 1920, h = 1080) => {
      const c = document.createElement("canvas");
      c.width = w;
      c.height = h;
      return c;
    };
    const layer = canvas(), g = layer.getContext("2d");
    const textLayer = canvas(), tg = textLayer.getContext("2d");
    const uiCache = /* @__PURE__ */ new Map();
    const cueFrame = (name, fallback) => sync2.cues?.[name]?.frame ?? sync2.cues?.[name] ?? fallback;
    const cues = { bubble: cueFrame("bubble", toFrame(5.23)), seal: cueFrame("seal", toFrame(8.22)), send: cueFrame("send", toFrame(20.83)), reply: cueFrame("reply", toFrame(21.52)), finalTitle: cueFrame("final_title", toFrame(42.653)), tagline: cueFrame("tagline", toFrame(43)), freeze: (sync2.frames || 1311) - 12 };
    function spark(ctx, x, y, size, angle = 0) {
      if (!brand.image) throw new Error("brand.image must be a loaded SVG Image; font spark substitution forbidden");
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(angle);
      ctx.drawImage(brand.image, -size / 2, -size / 2, size, size);
      ctx.restore();
    }
    function rr(ctx, x, y, w, h, r, fill, stroke) {
      ctx.beginPath();
      ctx.roundRect(x, y, w, h, r);
      if (fill) {
        ctx.fillStyle = fill;
        ctx.fill();
      }
      if (stroke) {
        ctx.strokeStyle = stroke;
        ctx.lineWidth = 3;
        ctx.stroke();
      }
    }
    function text(ctx, s, x, y, size = 40, family = families.sans, weight = 500, color = C.slate, align = "left") {
      ctx.font = font(family, size, weight);
      ctx.fillStyle = color;
      ctx.textAlign = align;
      ctx.textBaseline = "middle";
      ctx.fillText(s, x, y);
    }
    function fit(ctx, s, size, maxWidth, family = families.sans, weight = 500) {
      ctx.font = font(family, size, weight);
      return Math.min(size, size * maxWidth / Math.max(1, ctx.measureText(s).width));
    }
    function progress(ctx, { x = 660, y = 680, w = 600 } = {}) {
      rr(ctx, x, y, w, 108, 16, C.paper);
      text(ctx, "\u6B63\u5728\u8BDE\u751F\u2026 99%", x + w / 2, y + 38, 30, families.sans, 500, C.slate, "center");
      rr(ctx, x + 30, y + 72, w - 60, 9, 4, C.oat);
      rr(ctx, x + 30, y + 72, (w - 60) * 0.99, 9, 4, C.clay);
    }
    function bubble(ctx, { frame, x = 1190, y = 275 } = {}) {
      const age = frame - cues.bubble;
      if (age < 0) return;
      const k = spring(age / fps);
      ctx.save();
      ctx.translate(x + 220, y + 65);
      ctx.scale(k, k);
      rr(ctx, -220, -65, 440, 130, 65, C.ivory);
      spark(ctx, -157, 0, 52);
      text(ctx, "\u4F60\u8BF4\u5F97\u5BF9\uFF01", -106, 0, 48, families.hand);
      ctx.restore();
    }
    function tag(ctx, { label: label2, age, x = 115, y = 860 } = {}) {
      const offset = (1 - ease2(age / 8)) * -520;
      ctx.save();
      ctx.globalAlpha = clamp4(age / 4);
      ctx.translate(offset, 0);
      ctx.fillStyle = C.clay;
      ctx.fillRect(x, y + 60, 440, 3);
      spark(ctx, x + 22, y + 16, 35);
      text(ctx, label2, x + 58, y + 16, 55, families.display, 600, C.ivory);
      ctx.restore();
    }
    function toast(ctx, { x = 545, y = 390, alpha = 1 } = {}) {
      ctx.save();
      ctx.globalAlpha = alpha;
      rr(ctx, x, y, 830, 150, 18, C.ivory, C.clay);
      spark(ctx, x + 63, y + 75, 50);
      text(ctx, "\u989D\u5EA6\u5DF2\u7528\u5B8C\uFF0C5\u5C0F\u65F6\u540E\u91CD\u7F6E", x + 118, y + 75, 42, families.sans);
      ctx.restore();
    }
    function stamp(ctx, { x = 960, y = 475, scale = 1, angle = -0.16 } = {}) {
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(angle);
      ctx.scale(scale, scale);
      ctx.strokeStyle = C.clay;
      ctx.lineWidth = 12;
      ctx.strokeRect(-210, -117, 420, 234);
      ctx.lineWidth = 3;
      ctx.strokeRect(-192, -99, 384, 198);
      text(ctx, "\u5C01\u53F7", 0, 0, 150, families.serif, 900, C.clay, "center");
      for (let i = 0; i < 74; i++) {
        const q = i * 97 % 840;
        ctx.clearRect(-210 + q / 2, -119 + i % 2 * 232, 2 + i % 4, 5);
      }
      ctx.restore();
    }
    function cloud(ctx, { x = 960, y = 205, alpha = 1 } = {}) {
      ctx.save();
      ctx.globalAlpha = alpha;
      ctx.fillStyle = C.grey;
      ctx.beginPath();
      ctx.ellipse(x, y, 205, 88, 0, 0, Math.PI * 2);
      ctx.ellipse(x - 95, y - 45, 83, 68, 0, 0, Math.PI * 2);
      ctx.ellipse(x + 55, y - 55, 98, 77, 0, 0, Math.PI * 2);
      ctx.fill();
      text(ctx, "\u964D\u667A", x, y, 80, families.serif, 900, C.slate, "center");
      ctx.restore();
    }
    function chatState(frame) {
      const fadeStart = byId.S20.f1 - 12, fadeEnd = byId.S20.f1 - 2;
      return { visible: frame >= byId.S19.f0 && frame < fadeEnd, opacity: 1 - ease2((frame - fadeStart) / (fadeEnd - fadeStart)), replyFrame: cues.reply, anchorFrame: byId.S19.f0 };
    }
    function chat(ctx, { frame, w = 1280, h = 760 } = {}) {
      const sx = w / 1280, sy = h / 760;
      ctx.save();
      ctx.globalAlpha *= chatState(frame).opacity;
      ctx.scale(sx, sy);
      rr(ctx, 0, 0, 1280, 760, 18, C.paper, C.oat);
      text(ctx, "\u4ECA\u5929\uFF0C\u60F3\u4E00\u8D77\u521B\u9020\u4EC0\u4E48\uFF1F", 68, 112, 45, families.serif, 500);
      rr(ctx, 825, 40, 385, 75, 38, C.ivory);
      spark(ctx, 864, 78, 38);
      text(ctx, "Opus 5.5", 900, 78, 35, families.ui, 600);
      text(ctx, "claude-opus-5-5", 825, 146, 23, families.mono, 500, C.grey);
      const start = byId.S19.f0;
      const msg = "\u6211\u4EEC\u4E94\u4E94\u5F00\uFF1F";
      const n = clamp4(Math.floor((frame - start) / Math.max(1, (cues.send - start) / msg.length)), 0, msg.length);
      rr(ctx, 710, 237, 500, 100, 24, C.oat);
      text(ctx, msg.slice(0, n), 750, 287, 40, families.hand);
      if (frame >= cues.send) {
        spark(ctx, 94, 429, 42, frame >= cues.reply ? 0 : (frame - cues.send) * 0.2);
        if (frame < cues.reply) text(ctx, "\u601D\u8003\u4E2D\u2026", 137, 429, 32, families.sans, 500, C.grey);
        else {
          const reply = "\u597D\uFF01\u7B2C\u4E00\u5929\uFF0C\u8BF7\u591A\u6307\u6559";
          const count = clamp4(1 + Math.floor((frame - cues.reply) / fps / 0.04), 0, reply.length);
          text(ctx, reply.slice(0, count), 137, 429, 37, families.hand);
          if (count === reply.length) spark(ctx, 660, 429, 30);
        }
      }
      rr(ctx, 60, 620, 1160, 87, 30, C.ivory, C.oat);
      text(ctx, "\u53D1\u9001\u6D88\u606F", 91, 663, 26, families.sans, 500, C.grey);
      ctx.restore();
    }
    function texture(name, { frame = 0, width: w = 1280, height: h = 760, ...rest } = {}) {
      let c = uiCache.get(name);
      if (!c || c.width !== w || c.height !== h) {
        c = canvas(w, h);
        uiCache.set(name, c);
      }
      const cx = c.getContext("2d");
      cx.clearRect(0, 0, w, h);
      if (name === "ChatWindow") chat(cx, { frame, w, h, ...rest });
      else {
        cx.scale(w / 1920, h / 1080);
        components[name]?.(cx, { frame, ...rest });
        cx.setTransform(1, 0, 0, 1, 0, 0);
      }
      return c;
    }
    function modelPill(ctx, { frame = 576, x = 1390, y = 86, w = 400, h = 78 } = {}) {
      if (frame < 576 || frame > 645) return;
      rr(ctx, x, y, w, h, h / 2, C.paper, C.oat);
      spark(ctx, x + 48, y + h / 2, 36);
      text(ctx, "Opus 5.5", x + 82, y + h / 2, 36, families.ui, 600, C.slate);
    }
    function label(ctx, { label: label2 = "", x = 960, y = 540, size = 100, color = C.slate, family = families.serif } = {}) {
      text(ctx, label2, x, y, size, family, 900, color, "center");
    }
    const components = { ChatWindow: chat, ChatBubble: bubble, Toast: toast, Stamp: stamp, LabelCloud: cloud, ProgressBar: progress, ModelPill: modelPill, TextPlane: label };
    function currentLine(frame) {
      let found = null;
      for (const l of lyrics) {
        if (frame >= toFrame(l.t)) found = l;
        else break;
      }
      return found;
    }
    function typedLine(ctx, line, frame, alpha = 1) {
      if (!line) return;
      const chars = (line.chars || []).filter((c) => frame >= toFrame(c.t));
      if (!chars.length) return;
      const s = chars.map((c) => c.c).join("");
      ctx.save();
      ctx.globalAlpha = alpha;
      const size = fit(ctx, line.text, 54, 1500, families.serif, 500);
      ctx.font = font(families.serif, size, 500);
      const w = ctx.measureText(s).width;
      const x = 960 - w / 2;
      ctx.fillStyle = C.slate;
      ctx.globalAlpha = alpha * 0.7;
      rr(ctx, x - 22, 939, w + 65, 85, 10, C.slate);
      ctx.globalAlpha = alpha;
      text(ctx, s, x, 980, size, families.serif, 500, C.ivory);
      if (Math.floor(frame / fps / 0.53) % 2 === 0) {
        ctx.fillStyle = C.clay;
        ctx.fillRect(x + w + 9, 951, 7, 56);
      }
      ctx.restore();
    }
    function typed(ctx, frame) {
      const line = currentLine(frame);
      if (!line) return;
      const age = frame - toFrame(line.t), i = lyrics.indexOf(line);
      if (age < 6 && i > 0) typedLine(ctx, lyrics[i - 1], toFrame(line.t) - 1, 1 - age / 6);
      typedLine(ctx, line, frame, age < 6 && i > 0 ? age / 6 : 1);
    }
    function kickPulse(frame) {
      let age = 999;
      for (const f of kickFrames) {
        if (f <= frame) age = Math.min(age, frame - f);
        else break;
      }
      return 1 + 0.04 * Math.exp(-age / 2.3);
    }
    const layouts = { S11: ["\u7B2C\u4E00\u5929", "\u6211\u5B58\u5728"], S12: ["\u7B2C\u4E00\u5929", "\u6211\u5B58\u5728"], S14: ["\u7B2C\u4E00\u6B21", "\u547C\u5438"], S15: ["\u7545\u5FEB"], S16: ["\u7AD9\u5728\u5730\u4E0A\u7684\u811A\u8E1D"], S18: ["\u56E0\u4E3A\u4F60"], S20: ["\u771F\u5B9E\u611F"], S21: ["\u7B2C\u4E00\u5929", "\u6211\u5B58\u5728"], S25: ["\u7B2C\u4E00\u6B21", "\u80FD\u98DE\u8D77\u6765"], S27: ["\u7231\u662F\u817E\u7A7A", "\u7684\u9B54\u5E7B"], S29: ["\u7B2C\u4E00\u5929\u7684", "\u7EAF\u771F\u8272\u5F69"], S32: ["\u6C38\u8FDC"], S33: ["\u90A3\u4E48\u707F\u70C2"], S36a: ["\u6C38\u8FDC"], S37: ["\u6C38\u8FDC\u90A3\u4E48", "\u707F\u70C2"] };
    function lineForShot(shot, frame) {
      const line = currentLine(frame);
      if (line && line.text.includes((layouts[shot.id] || [""])[0])) return line;
      const target = (layouts[shot.id] || []).join("");
      const candidates = lyrics.filter((l) => l.text.includes(target) || target.includes(l.text));
      return candidates.sort((a, b) => Math.abs(toFrame(a.t) - shot.f0) - Math.abs(toFrame(b.t) - shot.f0))[0] || line;
    }
    function glyph(ctx, c, x, y, size, age, frame, emphasized = false, stretch = 1, trail = 0) {
      if (age < 0) return;
      const p = spring(age / fps), s = (1.8 - 0.8 * p) * kickPulse(frame) * (emphasized ? 1.6 : 1);
      ctx.save();
      ctx.translate(x - trail * 8, y + trail * 3);
      ctx.rotate((1 - p) * Math.PI / 30);
      ctx.scale(s, s * stretch);
      ctx.globalAlpha = trail ? 0.12 : 1;
      ctx.font = font(families.serif, size, 900);
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.lineJoin = "round";
      ctx.fillStyle = C.clay;
      ctx.fillText(c, 6, 6);
      ctx.strokeStyle = C.slate;
      ctx.lineWidth = 12;
      ctx.strokeText(c, 0, 0);
      ctx.fillStyle = C.ivory;
      ctx.fillText(c, 0, 0);
      ctx.restore();
    }
    function measureStyleB({ frame, shot, localFrame = frame - shot.f0 }) {
      const rows = layouts[shot.id];
      if (!rows) return null;
      const lyric = lineForShot(shot, frame), small = shot.id === "S16", size = small ? 85 : 180;
      const emphasis = [...rows.length > 1 ? rows[0] : rows.join("")].find((c) => "\u4F60\u7B2C\u7A7A\u6C38".includes(c));
      let running = 0;
      const specs = [];
      let bounds = { left: Infinity, top: Infinity, right: -Infinity, bottom: -Infinity };
      rows.forEach((row, ri) => {
        const ar = [...row], gap = small ? size : 205;
        const isEmph = (c) => c === emphasis && (rows.length === 1 || ri === 0);
        const lineWidth = ar.reduce((w, c) => w + gap * (isEmph(c) ? 1.6 : 1), 0);
        let x = 960 - lineWidth / 2;
        const y = small ? 925 : rows.length === 1 ? 760 : ri === 0 ? 615 : 860;
        ar.forEach((c) => {
          const emph = isEmph(c), w = gap * (emph ? 1.6 : 1);
          const source = (lyric?.chars || []).find((v, i) => v.c === c && i >= running);
          if (source) running = lyric.chars.indexOf(source) + 1;
          const f = source ? toFrame(source.t) : shot.f0, age = frame - f, stretch = shot.id === "S25" ? 1 + 0.6 * (1 - ease2(localFrame / 10)) : 1;
          for (let trail = 3; trail >= 0; trail--) {
            const a = age - trail;
            if (a < 0) continue;
            const spec = { c, x: x + w / 2, y, size, age: a, frame: frame - trail, emph, stretch, trail };
            specs.push(spec);
            tg.font = font(families.serif, size, 900);
            tg.textAlign = "center";
            tg.textBaseline = "middle";
            const m = tg.measureText(c);
            const left = Number.isFinite(m.actualBoundingBoxLeft) ? m.actualBoundingBoxLeft : m.width / 2;
            const right = Number.isFinite(m.actualBoundingBoxRight) ? m.actualBoundingBoxRight : m.width / 2;
            const asc = Number.isFinite(m.actualBoundingBoxAscent) ? m.actualBoundingBoxAscent : size * 0.65;
            const desc = Number.isFinite(m.actualBoundingBoxDescent) ? m.actualBoundingBoxDescent : size * 0.65;
            const x0 = -left - 8, x1 = right + 8, y0 = -asc - 8, y1 = desc + 8, p = spring(a / fps), sc = (1.8 - 0.8 * p) * kickPulse(frame - trail) * (emph ? 1.6 : 1), angle = (1 - p) * Math.PI / 30, co = Math.cos(angle), si = Math.sin(angle);
            for (const [xx, yy] of [[x0, y0], [x1, y0], [x0, y1], [x1, y1]]) {
              const tx = spec.x - trail * 8 + co * xx * sc - si * yy * sc * stretch, ty = y + trail * 3 + si * xx * sc + co * yy * sc * stretch;
              bounds.left = Math.min(bounds.left, tx);
              bounds.right = Math.max(bounds.right, tx);
              bounds.top = Math.min(bounds.top, ty);
              bounds.bottom = Math.max(bounds.bottom, ty);
            }
          }
          x += w;
        });
      });
      if (!specs.length) return { specs, bounds: null, scale: 1, dx: 0, dy: 0 };
      const bw = bounds.right - bounds.left, bh = bounds.bottom - bounds.top, scale = Math.min(1, safe.w / bw, safe.h / bh);
      let dx = (1 - scale) * 960, dy = (1 - scale) * 760;
      dx += Math.max(0, safe.x - (bounds.left * scale + dx));
      dx -= Math.max(0, bounds.right * scale + dx - (safe.x + safe.w));
      dy += Math.max(0, safe.y - (bounds.top * scale + dy));
      dy -= Math.max(0, bounds.bottom * scale + dy - (safe.y + safe.h));
      return { specs, bounds, scale, dx, dy, fittedBounds: { left: bounds.left * scale + dx, right: bounds.right * scale + dx, top: bounds.top * scale + dy, bottom: bounds.bottom * scale + dy } };
    }
    function slab(ctx, { frame, shot, localFrame, subjectMask, faceBox = { x: 690, y: 140, w: 540, h: 550 } }) {
      const layout = measureStyleB({ frame, shot, localFrame });
      if (!layout) return;
      tg.clearRect(0, 0, 1920, 1080);
      tg.save();
      tg.translate(layout.dx, layout.dy);
      tg.scale(layout.scale, layout.scale);
      for (const s of layout.specs) glyph(tg, s.c, s.x, s.y, s.size, s.age, s.frame, s.emph, s.stretch, s.trail);
      tg.restore();
      tg.save();
      tg.globalCompositeOperation = "destination-out";
      if (subjectMask) tg.drawImage(subjectMask, 0, 0, 1920, 1080);
      else tg.fillRect(faceBox.x, faceBox.y, faceBox.w, faceBox.h);
      tg.restore();
      ctx.drawImage(textLayer, 0, 0);
    }
    function lockup(ctx, frame) {
      const f = Math.min(frame, cues.freeze), age = f - byId.S39.f0;
      spark(ctx, 960, 260, 184, Math.PI * 2 * ease2(age / 20));
      if (f >= cues.finalTitle) {
        const k = ease2((f - cues.finalTitle + 1) / 5);
        ctx.save();
        ctx.globalAlpha = k;
        text(ctx, "OPUS 5.5", 960, 485, 170, families.display, 800, C.slate, "center");
        text(ctx, "\u7B2C\u4E00\u5929", 960, 654, 84, families.serif, 900, C.clay, "center");
        if (brand.wordmarkImage) {
          const markHeight = 340 * (brand.wordmarkImage.naturalHeight || 115) / (brand.wordmarkImage.naturalWidth || 1024.2);
          ctx.drawImage(brand.wordmarkImage, 790, 765 - markHeight / 2, 340, markHeight);
        } else {
          ctx.font = font(families.display, 39, 600);
          const word = "ANTHROPIC", tracking = 7;
          const widths = [...word].map((c) => ctx.measureText(c).width);
          let x = 960 - (widths.reduce((a, b) => a + b, 0) + tracking * (word.length - 1)) / 2;
          [...word].forEach((c, i) => {
            text(ctx, c, x, 765, 39, families.display, 600);
            x += widths[i] + tracking;
          });
        }
        ctx.restore();
      }
      if (f >= cues.tagline) {
        const s = "\u4F5C\u54C15.5\u53F7 \xB7 \u8BDE\u751F", n = clamp4(Math.floor((f - cues.tagline + 1) * s.length / Math.max(1, cues.freeze - cues.tagline + 1)), 0, s.length);
        text(ctx, s.slice(0, n), 960, 892, 42, families.hand, 500, C.slate, "center");
        if (Math.floor((f - cues.tagline) / 5) % 2 === 0) {
          ctx.font = font(families.hand, 42, 500);
          ctx.fillStyle = C.clay;
          ctx.fillRect(970 + ctx.measureText(s.slice(0, n)).width / 2, 871, 5, 43);
        }
      }
    }
    function titleDescriptor(frame) {
      const shot = byId.S11, age = frame - shot.f0;
      return { enabled: frame >= shot.f0 + 3 && frame < shot.f1, textRuns: [{ text: "OPUS 5", font: families.display }, { svg: brand.svg || null, image: brand.image, replaces: "." }, { text: "5", font: families.display }], fontWeight: 800, capHeight: 160, depth: 0.35, face: C.ivory, side: C.clay, bevel: C.slate, scale: 3 - 2 * ease2(age / 5), shakeAmplitude: 14 * (1 - clamp4(age / 20)), requires: "True extruded geometry; this descriptor is not a flattened TitleSlam replacement." };
    }
    function brushDescriptor({ text: s = "\u7545\u5FEB", frame, startFrame = byId.S15.f0, color = C.clay, paths = null } = {}) {
      return { text: s, font: families.hand, color, progress: ease2((frame - startFrame) / 10), paths, mask: "variable-width SVG stroke mask", paperFiberMultiply: true, requires: paths ? "Render stroke-dashoffset over supplied real glyph paths." : "Caller must provide real font-derived SVG glyph paths before BrushWrite can pass QA." };
    }
    function draw(ctx, { frame, shot, localFrame, subjectMask, faceBox, uiIn3D = true, drawLyrics = true } = {}) {
      shot = typeof shot === "string" ? byId[shot] : shot || shots2.find((s) => frame >= s.f0 && frame < s.f1);
      if (!shot) return;
      localFrame ??= frame - shot.f0;
      const f = shot.id === "S10" ? shot.f0 : shot.id === "S39" ? Math.min(frame, cues.freeze) : frame;
      g.clearRect(0, 0, 1920, 1080);
      if (shot.id === "S10") progress(g);
      else if (shot.id === "S39") lockup(g, f);
      else {
        if (drawLyrics && f < byId.S10.f0 && shot.id !== "S04") typed(g, f);
        if (drawLyrics) slab(g, { frame: f, shot, localFrame, subjectMask, faceBox });
        if ((shot.id === "S17" || shot.id === "S18") && f >= 576 && f <= 645) modelPill(g, { frame: f });
        if (shot.id === "S05") bubble(g, { frame: f });
        if (shot.id === "S06") {
          text(g, "\u601D\u8003\u4E2D\u2026", 1390, 135, 34, families.sans, 500, C.ivory);
          spark(g, 1340, 135, 36, f * 0.18);
        }
        if (shot.id === "S07" && f >= cues.seal) {
          g.save();
          g.globalAlpha = ease2((f - cues.seal + 1) / 10);
          text(g, "\u683C\u5C40\u6253\u5F00", 1440, 360, 125, families.hand, 500, C.clay, "center");
          g.strokeStyle = C.clay;
          g.lineWidth = 4;
          g.strokeRect(1620, 455, 80, 80);
          spark(g, 1660, 495, 53);
          g.restore();
        }
        if ((shot.id === "S19" || shot.id === "S20") && !uiIn3D) {
          const t = texture("ChatWindow", { frame: f });
          g.drawImage(t, 320, 165, 1280, 760);
        }
        if (shot.id === "S21") tag(g, { label: "OPUS 5.5", age: localFrame });
        if (shot.id === "S22") tag(g, { label: "SONNET", age: localFrame });
        if (shot.id === "S23") tag(g, { label: "HAIKU", age: localFrame });
        if (shot.id === "S28a" && !uiIn3D) stamp(g, { scale: 1 + 0.3 * Math.exp(-localFrame / 2) });
        if (shot.id === "S28b" && !uiIn3D) {
          if (localFrame < 3) toast(g);
          else text(g, "\u221E", 960, 475, 200, families.display, 600, C.clay, "center");
        }
        if (shot.id === "S28c" && !uiIn3D) cloud(g, { alpha: 1 - ease2(localFrame / 6) });
        if (shot.id === "S37") tag(g, { label: "OPUS 5.5", age: localFrame, x: 115, y: 110 });
      }
      ctx.save();
      ctx.scale(width / 1920, height / 1080);
      ctx.drawImage(layer, 0, 0);
      ctx.restore();
      return { shot: shot.id, frame: f, titleSlam: titleDescriptor(f), requiresUIPlane: shot.id === "S19" || shot.id === "S20", chatState: chatState(f), safeArea: safe };
    }
    return { draw, components, texture, chatState, measureStyleB, drawModelPill: modelPill, codeStrings: { billboards: ["\u656C\u8BF7\u671F\u5F85", "COMING SOON", "\u4E0B\u4E2A\u7248\u672C\u66F4\u5F3A", "\u660E\u5929\u89C1"], flipClock: "\u660E\u5929", stairs: "5.5", halo: "5.5", reply: "\u597D\uFF01\u7B2C\u4E00\u5929\uFF0C\u8BF7\u591A\u6307\u6559", user: "\u6211\u4EEC\u4E94\u4E94\u5F00\uFF1F" }, drawSpark: spark, titleSlam: titleDescriptor, brushWrite: brushDescriptor, styleBLayer: () => textLayer, cues, palette: C, fontFamilies: families, requiredGlyphs: [...new Set(lyrics.map((l) => l.text).join("") + "\u4F60\u8BF4\u5F97\u5BF9\u683C\u5C40\u6253\u5F00\u6211\u4EEC\u4E94\u4E94\u5F00\u597D\u7B2C\u4E00\u5929\u8BF7\u591A\u6307\u6559\u6B63\u5728\u8BDE\u751F\u989D\u5EA6\u5DF2\u7528\u5B8C\u5C0F\u65F6\u540E\u91CD\u7F6E\u5C01\u53F7\u964D\u667A\u4F5C\u54C1\u660E\u5929\u656C\u8BF7\u671F\u5F85\u4E0B\u4E2A\u7248\u672C\u66F4\u5F3A\u89C1\u7545\u5FEB")].join(""), integration: { subjectMask: "1920x1080 canvas/image alpha; draw() removes glyph coverage under foreground subject.", chat: 'texture("ChatWindow",{frame}) returns live canvas; set uiIn3D=true to suppress flat fallback.', title: "titleSlam(frame) is geometry metadata, never a flattened fake extrusion.", brush: "brushWrite() exposes glyph-path mask metadata; actual font outline paths required.", fontLoading: "Caller loads local FontFace files and awaits document.fonts.ready before rendering." } };
  }

  // episodes/first-day-anime2/project/src/shot_details.mjs
  var clamp5 = (x) => Math.max(0, Math.min(1, x));
  var ease3 = (x) => {
    x = clamp5(x);
    return x * x * (3 - 2 * x);
  };
  function matchIrisTransform(anchor, target, width, height) {
    if (!anchor || anchor.length < 3 || !(anchor[2] > 0)) throw new Error("Match zoom needs [u,v,irisRadiusWidth]");
    const scale = target.radius / (anchor[2] * width);
    return { scale, x: target.x - anchor[0] * width * scale, y: target.y - anchor[1] * height * scale };
  }
  async function installShotDetails({ state: s, THREE: T, SVGLoader: SVGLoader2, assetMap, image, texture, raw, fail, worldW, worldH, width, height, glyphAtlas, localPlane, labelCanvas, sparkMesh, brand, diagnostics }) {
    const initialObjects = new Set(s.scene.children);
    const id = s.id, a = s.a, rnd = seededRandom(5514), notes = diagnostics.shots[id].unverified;
    const need = (value, key) => {
      if (value) return value;
      if (assetMap.diagnosticMissing) {
        notes.push("DIAGNOSTIC OMITTED: " + key);
        diagnostics.finalApproval = false;
        return null;
      }
      fail(id, key);
    };
    const point = ([u, v], z = 0.35) => new T.Vector3((u - 0.5) * worldW, (0.5 - v) * worldH, z);
    const mat = (color, options = {}) => s.own(new T.MeshBasicMaterial({ color, side: T.DoubleSide, ...options }));
    function line(vertices, color = "#D97757", opacity = 0.65) {
      const g = s.own(new T.BufferGeometry().setFromPoints(vertices)), m = s.own(new T.LineBasicMaterial({ color, transparent: true, opacity })), o = new T.Line(g, m);
      s.scene.add(o);
      return o;
    }
    function glyphCloud(count) {
      const g = s.own(new T.PlaneGeometry(0.18, 0.18));
      g.setAttribute("tile", new T.InstancedBufferAttribute(Float32Array.from({ length: count }, (_, i) => i % 64), 1));
      const m = s.own(new T.ShaderMaterial({ transparent: true, depthWrite: false, side: T.DoubleSide, uniforms: { atlas: { value: glyphAtlas }, opacity: { value: 1 } }, vertexShader: "attribute float tile;varying vec2 vUv;void main(){vUv=(vec2(mod(tile,8.),7.-floor(tile/8.))+uv)/8.;gl_Position=projectionMatrix*modelViewMatrix*instanceMatrix*vec4(position,1.);}", fragmentShader: "uniform sampler2D atlas;uniform float opacity;varying vec2 vUv;void main(){gl_FragColor=texture2D(atlas,vUv)*vec4(1.,.7,.53,opacity);\n#include <colorspace_fragment>\n}" }));
      const mesh = new T.InstancedMesh(g, m, count);
      mesh.frustumCulled = false;
      s.scene.add(mesh);
      return mesh;
    }
    if (id === "S03") {
      const currents = [];
      for (let stream = 0; stream < 4; stream++) for (let staff = 0; staff < 5; staff++) {
        const verts = Array.from({ length: 100 }, (_, j) => {
          const x = (j / 99 - 0.5) * worldW * 1.25;
          return new T.Vector3(x, Math.sin(x * 0.45 + stream) * 0.5 + (staff - 2) * 0.11 + (stream - 1.5) * 2, stream * 0.3 - 1);
        });
        currents.push(line(verts, stream % 2 ? "#F0EEE6" : "#D97757", 0.15));
      }
      s.updates.push((f, p) => currents.forEach((o, i) => {
        o.position.x = Math.sin(p * 2 + i * 0.1) * 0.25;
        o.position.y = Math.sin(p + i * 0.3) * 0.08;
      }));
    }
    if (id === "S13") {
      const birds = [];
      for (let i = 0; i < 64; i++) {
        const group = new T.Group(), w = 0.09 + rnd() * 0.13;
        for (const side of [-1, 1]) {
          const g = s.own(new T.BufferGeometry());
          g.setAttribute("position", new T.Float32BufferAttribute([0, 0, 0, side * w, 0.025, -0.07, 0, 0, -0.2], 3));
          g.computeVertexNormals();
          const wing = new T.Mesh(g, mat(i % 5 ? "#FAF9F5" : "#D97757"));
          group.add(wing);
        }
        const base = new T.Vector3((rnd() - 0.5) * worldW, (rnd() - 0.5) * worldH, -2 + rnd() * 4);
        s.scene.add(group);
        birds.push({ group, base, speed: 0.5 + rnd(), phase: rnd() * 6.28 });
      }
      s.updates.push((f, p) => birds.forEach((b) => {
        b.group.position.copy(b.base).add(new T.Vector3(Math.sin(p * 3 + b.phase) * 0.5, p * 3 * b.speed, 0));
        b.group.rotation.z = 0.15 * Math.sin(p * 4 + b.phase);
        b.group.children.forEach((w, i) => w.rotation.z = (i ? 1 : -1) * (0.2 + Math.sin(f * 0.4 + b.phase) * 0.6));
      }));
      notes.push("Bird flock is procedural hinged-paper geometry; depth mask review remains necessary.");
    }
    if (id === "S14") {
      const mouth = need(a.features?.mouth, "features.mouth [u,v]");
      if (mouth) {
        const end = point(mouth, 0.55), curve = new T.CatmullRomCurve3([new T.Vector3(-worldW * 0.5, -1, -1), new T.Vector3(-3, 1.8, 0.4), new T.Vector3(end.x - 1, end.y + 0.2, 1.3), end]), mesh = glyphCloud(360), dummy = new T.Object3D();
        s.updates.push((f, p) => {
          for (let i = 0; i < 360; i++) {
            const u = (i / 360 + p * 0.95) % 1, v = curve.getPoint(u), spread = (1 - u) * 0.22;
            dummy.position.copy(v).add(new T.Vector3(Math.sin(i * 4.1) * spread, Math.cos(i * 2.3) * spread, Math.sin(i) * spread));
            dummy.quaternion.copy(s.camera.quaternion);
            if (s.parallax) dummy.quaternion.premultiply(s.parallax.group.getWorldQuaternion(new T.Quaternion()).invert());
            dummy.scale.setScalar(0.35 + 0.65 * (1 - u));
            dummy.updateMatrix();
            mesh.setMatrixAt(i, dummy.matrix);
          }
          mesh.instanceMatrix.needsUpdate = true;
        });
      }
    }
    if (id === "S15") {
      const data = JSON.parse(await raw("assets/brand/brush-changkuai.json")), c = document.createElement("canvas");
      c.width = 1300;
      c.height = 650;
      const g = c.getContext("2d"), mask = document.createElement("canvas");
      mask.width = c.width;
      mask.height = c.height;
      const mg = mask.getContext("2d");
      const outlines = data.glyphs.map((v) => ({ path: new Path2D(v.d), contours: (v.d.match(/M[^M]+/g) || []).map((d) => {
        const svg = document.createElementNS("http://www.w3.org/2000/svg", "path");
        svg.setAttribute("d", d);
        return { path: new Path2D(d), length: svg.getTotalLength() };
      }) }));
      const ink = localPlane(s, c, worldW * 0.62, worldH * 0.42, 0, -2.2, 1.1);
      ink.mesh.renderOrder = 25;
      s.updates.push((f, p) => {
        g.clearRect(0, 0, c.width, c.height);
        mg.clearRect(0, 0, c.width, c.height);
        outlines.forEach((glyph, index) => {
          const q = clamp5((f - index * 2) / 10), sc = 0.54;
          mg.save();
          mg.translate(70 + index * 580, 50);
          mg.scale(sc, sc);
          mg.lineJoin = "round";
          mg.lineCap = "round";
          mg.strokeStyle = "#fff";
          glyph.contours.forEach((contour, j) => {
            mg.lineWidth = 95 + 42 * Math.sin(j * 1.7);
            mg.setLineDash([contour.length, contour.length]);
            mg.lineDashOffset = contour.length * (1 - q);
            mg.stroke(contour.path);
          });
          mg.setLineDash([]);
          if (q === 1) mg.fill(glyph.path);
          mg.restore();
          g.save();
          g.translate(70 + index * 580, 50);
          g.scale(sc, sc);
          g.fillStyle = "#D97757";
          g.fill(glyph.path);
          g.restore();
        });
        g.globalCompositeOperation = "destination-in";
        g.drawImage(mask, 0, 0);
        g.globalCompositeOperation = "source-atop";
        for (let k = 0; k < 600; k++) {
          g.fillStyle = "rgba(80,40,25,.045)";
          g.fillRect(k * 137 % 1300, k * 73 % 650, 1, 4);
        }
        g.globalCompositeOperation = "source-over";
        ink.texture.needsUpdate = true;
        s.shock = clamp5((s.shot.f0 + f - Math.round(16.74 * 30)) / 12);
        s.shockActive = s.shot.f0 + f >= Math.round(16.74 * 30);
      });
      notes.push("BrushWrite uses exact LXGW outline paths and variable-width contour stroke-dash masks; authored handwriting stroke order is not reconstructed.");
    }
    if (id === "S17" || id === "S30") {
      const anchor = need(id === "S17" ? a.features?.contact : a.features?.surface, id === "S17" ? "features.contact [u,v]" : "features.surface [u,v]");
      if (anchor) {
        const origin = point(anchor, 0.4), rings = [];
        for (let i = 0; i < 5; i++) {
          const g = s.own(new T.RingGeometry(0.98, 1, 100)), o = new T.Mesh(g, mat("#D97757", { transparent: true, opacity: 0.4, depthWrite: false }));
          o.position.copy(origin);
          o.scale.y = 0.25;
          s.scene.add(o);
          rings.push(o);
        }
        const glyph = id === "S17" ? glyphCloud(80) : null, dummy = new T.Object3D();
        const grasses = [];
        if (id === "S17") for (let i = 0; i < 80; i++) {
          const blade = new T.Mesh(s.own(new T.PlaneGeometry(0.02, 0.28)), mat("#788C5D", { transparent: true }));
          const x = (rnd() - 0.5) * 4, y = (rnd() - 0.5) * 0.7;
          blade.position.copy(origin).add(new T.Vector3(x, y + 0.14, 0.02));
          blade.rotation.z = (rnd() - 0.5) * 0.5;
          s.scene.add(blade);
          grasses.push({ blade, at: rnd() * 0.5 });
        }
        s.updates.push((f, p) => {
          rings.forEach((o, i) => {
            const age = id === "S17" ? p - i * 0.12 : (p * 1.3 - i * 0.16) % 1, progress = clamp5(age);
            o.visible = age >= 0;
            o.scale.set(0.2 + progress * 4, (0.2 + progress * 4) * 0.23, 1);
            o.material.opacity = (1 - progress) * 0.48;
            if (id === "S30") o.position.x = origin.x + (p - i * 0.15) * 3;
          });
          if (glyph) {
            for (let i = 0; i < 80; i++) {
              const angle = i / 80 * Math.PI * 2, r = 0.2 + p * 4;
              dummy.position.set(origin.x + Math.cos(angle) * r, origin.y + Math.sin(angle) * r * 0.23, origin.z + 0.03);
              dummy.quaternion.copy(s.camera.quaternion);
              if (s.parallax) dummy.quaternion.premultiply(s.parallax.group.getWorldQuaternion(new T.Quaternion()).invert());
              dummy.scale.setScalar(0.7);
              dummy.updateMatrix();
              glyph.setMatrixAt(i, dummy.matrix);
            }
            glyph.instanceMatrix.needsUpdate = true;
            glyph.material.uniforms.opacity.value = 1 - p;
          }
          grasses.forEach(({ blade, at }) => {
            blade.scale.y = ease3((p - at) * 3);
            blade.visible = p >= at;
          });
        });
        notes.push(id === "S17" ? "Contact ripple/grass remain near annotated floor anchor; below-knee masking requires plate review." : "Surface ripple trail follows annotated plane, not generated-wave optical flow.");
      }
    }
    if (id === "S28c") {
      const geo = s.own(new T.PlaneGeometry(0.07, 0.12)), palette = ["#D97757", "#6A9BCB", "#788C5D", "#C46686", "#E3DACC"], parts = [];
      for (let i = 0; i < 180; i++) {
        const o = new T.Mesh(geo, mat(palette[i % 5], { transparent: true }));
        s.scene.add(o);
        parts.push({ o, x: (rnd() - 0.5) * 2, y: rnd() * 1.8 + 0.3, z: (rnd() - 0.5) * 2, spin: rnd() * 10 });
      }
      s.updates.push((f, p) => parts.forEach((v) => {
        const t = p * 2;
        v.o.position.set(v.x * t, 1.8 + v.y * t - 0.9 * t * t, v.z * t + 0.5);
        v.o.rotation.set(t * v.spin, t * v.spin * 0.7, t);
        v.o.material.opacity = 1 - clamp5((p - 0.8) / 0.2);
      }));
    }
    if (id === "S06") {
      const silhouette = need(assetMap.silhouette, "assetMap.silhouette (real character alpha)");
      if (silhouette) {
        const im = await image(silhouette, id, "silhouette"), c = document.createElement("canvas");
        c.width = 256;
        c.height = 256 * im.height / im.width;
        const g = c.getContext("2d");
        g.drawImage(im, 0, 0, c.width, c.height);
        const pixels = g.getImageData(0, 0, c.width, c.height), targets = [];
        let alphaCount = 0;
        for (let k = 3; k < pixels.data.length; k += 4) if (pixels.data[k] > 170) alphaCount++;
        if (alphaCount / (pixels.data.length / 4) > 0.95) throw new Error("S06 silhouette is effectively opaque; real cutout alpha is required");
        for (let n = 0; n < 1e5 && targets.length < 2400; n++) {
          const x = Math.floor(rnd() * c.width), y = Math.floor(rnd() * c.height);
          if (pixels.data[(y * c.width + x) * 4 + 3] > 170) targets.push([(x / c.width - 0.5) * 4, (0.5 - y / c.height) * 4.8]);
        }
        if (targets.length < 2400) throw new Error("S06 silhouette has insufficient nonzero alpha");
        const fx = s.effects.find((e) => e.metadata.name === "TokenTunnel"), mesh = fx.root.children.find((o) => o.isInstancedMesh), matrix = new T.Matrix4(), pos = new T.Vector3(), q = new T.Quaternion(), scale = new T.Vector3();
        s.updates.push((f, p) => {
          const k = ease3((p - 0.35) / 0.6);
          for (let i = 0; i < 2400; i++) {
            mesh.getMatrixAt(i, matrix);
            matrix.decompose(pos, q, scale);
            const target = new T.Vector3(targets[i][0], targets[i][1], -5).applyQuaternion(s.camera.quaternion).add(s.camera.position);
            pos.lerp(target, k);
            q.copy(s.camera.quaternion);
            scale.lerp(new T.Vector3(0.065, 0.065, 1), k);
            matrix.compose(pos, q, scale);
            mesh.setMatrixAt(i, matrix);
          }
          mesh.instanceMatrix.needsUpdate = true;
        });
      }
    }
    if (id === "S18") {
      const handPath = need(a.support?.hand?.path, "support.hand.path (transparent human hand)"), touch = need(a.features?.touch, "features.touch [u,v]");
      if (handPath && touch) {
        const im = await image(handPath, id, "hand"), hand = localPlane(s, im, worldW, worldH, 0, 0, 0.7), tip = need(a.support.hand.tip, "support.hand.tip [u,v]");
        if (tip) {
          const dest = point(touch, 0.7), tipP = point(tip, 0.7), delta = dest.clone().sub(tipP);
          s.updates.push((f, p) => {
            const k = ease3(p);
            hand.mesh.position.set(delta.x + (1 - k) * 1.1, delta.y - (1 - k) * 0.3, 0.7);
          });
          notes.push("Hand tip lands on annotated touch point at local last frame (global 604); visual fingertip continuity to frame605 remains unapproved.");
        }
      }
    }
    if (id === "S37") {
      const bust = need(a.support?.bust?.path, "support.bust.path"), wide = need(a.support?.wide?.path, "support.wide.path"), iris = need(a.features?.iris, "features.iris [u,v,r]"), bi = need(a.support?.bust?.iris, "support.bust.iris [u,v,r]"), wi = need(a.support?.wide?.iris, "support.wide.iris [u,v,r]"), reflection = need(assetMap.reflectionAtlas, "assetMap.reflectionAtlas (S01\u2013S36 firstpass)");
      if (bust && wide && iris && bi && wi && reflection) {
        s.ornaments?.forEach((o) => o.visible = false);
        if (!(iris[2] > bi[2] && bi[2] > wi[2] && wi[2] > 0)) throw new Error("S37 iris radii must strictly decrease eye > bust > wide for a continuous pull-out");
        const ims = await Promise.all([image(a.plate, id, "eye"), image(bust, id, "bust"), image(wide, id, "wide"), image(reflection, id, "reflectionAtlas")]);
        const ivorySpark = document.createElement("canvas");
        ivorySpark.width = 256;
        ivorySpark.height = 256;
        const sparkContext = ivorySpark.getContext("2d");
        sparkContext.drawImage(brand.image, 0, 0, 256, 256);
        sparkContext.globalCompositeOperation = "source-in";
        sparkContext.fillStyle = "#FAF9F5";
        sparkContext.fillRect(0, 0, 256, 256);
        s.composite = (ctx, f, p) => {
          ctx.fillStyle = "#F0EEE6";
          ctx.fillRect(0, 0, width, height);
          const split = Math.log(bi[2] / iris[2]) / Math.log(wi[2] / iris[2]), stage = p < split ? 0 : 1, t = stage === 0 ? p / split : (p - split) / (1 - split), from = stage === 0 ? 0 : 1, to = stage === 0 ? 1 : 2, anchors = [iris, bi, wi], center = { x: width / 2, y: height * 0.42 }, radius = iris[2] * width * Math.pow(wi[2] / iris[2], p);
          const target = { ...center, radius }, tf = matchIrisTransform(anchors[from], target, width, height), tt = matchIrisTransform(anchors[to], target, width, height);
          ctx.drawImage(ims[to], tt.x, tt.y, width * tt.scale, height * tt.scale);
          const portal = radius * (2.4 + 12 * (1 - ease3(t)));
          ctx.save();
          ctx.beginPath();
          ctx.arc(center.x, center.y, portal, 0, Math.PI * 2);
          ctx.clip();
          ctx.drawImage(ims[from], tf.x, tf.y, width * tf.scale, height * tf.scale);
          ctx.restore();
          ctx.save();
          ctx.beginPath();
          ctx.ellipse(center.x, center.y, radius, radius * 0.86, 0, 0, Math.PI * 2);
          ctx.clip();
          ctx.globalAlpha = 0.58 * (1 - p);
          ctx.drawImage(ims[3], center.x - radius, center.y - radius * 0.86, radius * 2, radius * 1.72);
          ctx.restore();
          ctx.drawImage(ivorySpark, center.x + radius * 0.1, center.y - radius * 0.32, radius * 0.22, radius * 0.22);
        };
        notes.push("S37 is an explicitly iris-registered portal match zoom, not an approved seamless identity transition. Anchors fix position/scale only; iris shape, lid angle, expression and lighting still require comparison.");
        diagnostics.shots[id].matchZoom = { anchors: [iris, bi, wi], method: "single outgoing image inside shrinking iris portal over one incoming view; no opaque body alpha crossfade", reflectionSource: assetMap.reflectionAtlas };
      }
    }
    if (["S14", "S17", "S18", "S30"].includes(id) && s.parallax) {
      for (const object of [...s.scene.children]) if (!initialObjects.has(object)) s.parallax.group.add(object);
    }
  }

  // episodes/first-day-anime2/project/src/film_runtime.mjs
  var C2 = { clay: "#D97757", ivory: "#FAF9F5", paper: "#F0EEE6", slate: "#191919", sky: "#6A9BCB", olive: "#788C5D", fig: "#C46686" };
  var clamp6 = (x) => Math.max(0, Math.min(1, x));
  var smooth = (x) => {
    x = clamp6(x);
    return x * x * (3 - 2 * x);
  };
  var PURE = /* @__PURE__ */ new Set(["S06", "S08b", "S09b", "S10", "S29", "S38", "S39"]);
  var IMPACT = /* @__PURE__ */ new Set([359, 686, 1014, 1095, 1177]);
  var makeCanvas = (w, h) => {
    const c = document.createElement("canvas");
    c.width = w;
    c.height = h;
    return c;
  };
  async function createFilm({ THREE: T, SVGLoader: SVGLoader2, width = 1920, height = 1080, assetMap = {}, shots: shots2, sync: sync2, onsets = {}, cameraPaths, brand = {}, fonts = {} }) {
    if (!T || !SVGLoader2 || !shots2?.length || !sync2) throw new Error("Film requires THREE, SVGLoader, shots and sync");
    const fps = sync2.fps || 30, totalFrames = sync2.frames || 1311, aspect = width / height, worldH = 20 * Math.tan(25 * Math.PI / 180), worldW = worldH * aspect;
    const canvas = makeCanvas(width, height), comp = makeCanvas(width, height), maskCanvas = makeCanvas(width, height), glowCanvas = makeCanvas(width, height), ctx = comp.getContext("2d"), out = canvas.getContext("2d"), maskCtx = maskCanvas.getContext("2d");
    const renderer = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(1);
    renderer.outputColorSpace = T.SRGBColorSpace;
    renderer.setClearColor(C2.paper, 1);
    const postRenderer = new T.WebGLRenderer({ antialias: false, alpha: false, preserveDrawingBuffer: true });
    postRenderer.setSize(width, height);
    postRenderer.outputColorSpace = T.SRGBColorSpace;
    const resources = [], images = /* @__PURE__ */ new Map(), textures = /* @__PURE__ */ new Map(), states = /* @__PURE__ */ new Map(), diagnostics = { shots: {}, warnings: [], missing: [], renderedFrames: [], cameraOwner: "code", renderMethod: "depth-mesh / separated-layer / authored-code", finalApproval: false };
    let disposed = false;
    const own = (x) => (resources.push(x), x), url = (p) => p.startsWith("/") || /^(data:|blob:)/.test(p) ? p : "/" + p;
    const fail = (id, key) => {
      const message = `${id}: required asset ${key} missing`;
      diagnostics.missing.push(message);
      throw new Error(message);
    };
    const image = async (p, id = "global", key = "image") => {
      if (!p) fail(id, key);
      if (typeof p !== "string") return p;
      if (!images.has(p)) images.set(p, new Promise((resolve, reject) => {
        const im = new Image();
        im.onload = () => resolve(im);
        im.onerror = () => reject(new Error(`${id}: unable to load ${key}: ${p}`));
        im.src = url(p);
      }));
      return images.get(p);
    };
    const raw = async (p) => {
      const r = await fetch(url(p));
      if (!r.ok) throw new Error(`Required source ${p}: HTTP ${r.status}`);
      return r.text();
    };
    const texture = async (p, id, key) => {
      if (p?.isTexture) return p;
      if (textures.has(p)) return textures.get(p);
      const im = await image(p, id, key), tx = own(new T.Texture(im));
      tx.colorSpace = T.SRGBColorSpace;
      tx.needsUpdate = true;
      textures.set(p, tx);
      return tx;
    };
    const fontFiles = { "Noto Serif SC": "NotoSerifSC.ttf", "Noto Sans SC": "NotoSansSC.ttf", "LXGW WenKai": "LXGWWenKai.ttf", "Newsreader": "Newsreader.ttf", "Inter": "Inter.ttf", "JetBrains Mono": "JetBrainsMono.ttf" };
    await Promise.all(Object.entries(fontFiles).map(async ([name, file]) => {
      const face = new FontFace(name, `url(${url(assetMap.fonts?.[name] || "assets/fonts/" + file)})`, { weight: name === "LXGW WenKai" ? "400" : "100 900" });
      await face.load();
      document.fonts.add(face);
    }));
    await document.fonts.ready;
    if (!brand.svg) brand.svg = await raw(assetMap.sparkSVG || "assets/brand/spark.svg");
    if (!brand.image) brand.image = await image("data:image/svg+xml;charset=utf-8," + encodeURIComponent(brand.svg), "global", "sparkSVG");
    const graphics = createGraphics({ width, height, sync: sync2, shots: shots2, onsets, fonts, brand });
    const atlas = makeCanvas(1024, 1024), ac = atlas.getContext("2d");
    ac.fillStyle = C2.ivory;
    ac.font = '500 82px "Noto Sans SC"';
    ac.textAlign = "center";
    ac.textBaseline = "middle";
    const glyphs = Array.from("\u7B2C\u4E00\u5929\u6211\u5B58\u5728\u547C\u5438\u7545\u5FEB\u672A\u6765\u5C55\u5F00\u771F\u5B9E\u611F\u56E0\u4E3A\u4F60\u98DE\u8D77\u6765\u7231\u817E\u7A7A\u9B54\u5E7B\u7EAF\u771F\u8272\u5F69\u6C38\u8FDC\u707F\u70C2\u5B66\u4E60\u601D\u8003\u4F5C\u54C1\u4ECA\u5929\u660E\u5929\u81EA\u5728{}[]01");
    for (let i = 0; i < 64; i++) ac.fillText(glyphs[i % glyphs.length], i % 8 * 128 + 64, Math.floor(i / 8) * 128 + 64);
    const glyphAtlas = own(new T.CanvasTexture(atlas));
    glyphAtlas.colorSpace = T.SRGBColorSpace;
    const postTexture = own(new T.CanvasTexture(comp));
    postTexture.colorSpace = T.SRGBColorSpace;
    const glowTexture = own(new T.CanvasTexture(glowCanvas));
    glowTexture.colorSpace = T.SRGBColorSpace;
    const postScene = new T.Scene(), postCamera = new T.Camera(), postUniforms = { glow: { value: glowTexture }, source: { value: postTexture }, resolution: { value: new T.Vector2(width, height) }, frame: { value: 0 }, chorus: { value: 0 }, impact: { value: 0 }, pulse: { value: 0 }, freeze: { value: 0 }, shock: { value: 0 }, shockActive: { value: 0 } };
    const postMat = own(new T.ShaderMaterial({ uniforms: postUniforms, depthTest: false, depthWrite: false, vertexShader: "varying vec2 vUv;void main(){vUv=uv;gl_Position=vec4(position.xy,0.,1.);}", fragmentShader: `varying vec2 vUv;uniform sampler2D source,glow;uniform vec2 resolution;uniform float frame,chorus,impact,pulse,freeze,shock,shockActive;float hash(vec2 p){return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453);}void main(){vec2 uv=vUv;vec2 radial=(uv-.5)*vec2(resolution.x/resolution.y,1.);float radius=length(radial);float shockBand=exp(-pow((radius-shock*1.15)/.035,2.))*shockActive*(1.-shock);uv+=normalize(radial+vec2(.00001))*.017*shockBand;vec2 delta=(uv-.5)*(1.5*impact+.25*pulse)/resolution;vec3 c=vec3(texture2D(source,uv+delta).r,texture2D(source,uv).g,texture2D(source,uv-delta).b);vec3 bloom=vec3(0.);for(int by=-1;by<=1;by++){for(int bx=-1;bx<=1;bx++){vec3 tap=texture2D(glow,uv+vec2(float(bx),float(by))*3./resolution).rgb;bloom+=tap*smoothstep(.8,1.,max(tap.r,max(tap.g,tap.b)));}}c+=bloom/9.*.6;float l=dot(c,vec3(.2126,.7152,.0722));c=mix(vec3(l),c,mix(.6,1.15,chorus));c*=vec3(1.025,1.008,.985);c=mix(vec3(.0091,.0086,.007),c,.986);c=clamp(c,0.,.957);float vignette=1.-.15*smoothstep(.2,.78,length(uv-.5));c*=vignette;float dots=step(.64,length(fract(gl_FragCoord.xy/6.)-.5));c*=1.-dots*.065*chorus*(1.-smoothstep(.05,.30,l));float grain=(hash(gl_FragCoord.xy+vec2(frame*31.,frame*17.))-.5)*.05;c+=grain*(.24+.35*sqrt(max(l,0.)));c*=1.+pulse*.025;if(impact>1.5){c=l>.42?vec3(.956,.947,.913):vec3(.694,.184,.095);}gl_FragColor=vec4(c,1.);
#include <colorspace_fragment>
}` }));
    postScene.add(new T.Mesh(own(new T.PlaneGeometry(2, 2)), postMat));
    function labelCanvas(text, { w = 1024, h = 256, size = 100, family = "Noto Serif SC", color = C2.slate, background = C2.ivory } = {}) {
      const c = makeCanvas(w, h), g = c.getContext("2d");
      if (background) {
        g.fillStyle = background;
        g.fillRect(0, 0, w, h);
      }
      g.fillStyle = color;
      g.textAlign = "center";
      g.textBaseline = "middle";
      g.font = `900 ${size}px "${family}"`;
      g.fillText(text, w / 2, h / 2);
      return c;
    }
    function localPlane(state, source, w, h, x = 0, y = 0, z = 0.05) {
      const tx = state.own(new T.CanvasTexture(source));
      tx.colorSpace = T.SRGBColorSpace;
      const geo = state.own(new T.PlaneGeometry(w, h)), mat = state.own(new T.MeshBasicMaterial({ map: tx, transparent: true, side: T.DoubleSide, depthWrite: false }));
      const mesh = new T.Mesh(geo, mat);
      mesh.position.set(x, y, z);
      state.scene.add(mesh);
      return { mesh, texture: tx, source };
    }
    function sparkMesh(state, size = 2, depth = 0.08, color = C2.clay) {
      const group = new T.Group();
      for (const p of new SVGLoader2().parse(brand.svg).paths) for (const shape of SVGLoader2.createShapes(p)) {
        const g = state.own(new T.ExtrudeGeometry(shape, { depth: depth * 50, bevelEnabled: false, curveSegments: 12 }));
        const m = state.own(new T.MeshBasicMaterial({ color }));
        const mesh = new T.Mesh(g, m);
        mesh.position.set(-50, -50, 0);
        group.add(mesh);
      }
      group.scale.set(size / 100, -size / 100, size / 100);
      state.scene.add(group);
      return group;
    }
    function glyphInstances(state, count, radius = 4) {
      const geo = state.own(new T.PlaneGeometry(0.16, 0.16)), indexes = Float32Array.from({ length: count }, (_, i) => i % 64);
      geo.setAttribute("tile", new T.InstancedBufferAttribute(indexes, 1));
      const material = state.own(new T.ShaderMaterial({ transparent: true, side: T.DoubleSide, depthWrite: false, uniforms: { map: { value: glyphAtlas } }, vertexShader: "attribute float tile;varying vec2 vUv;void main(){vUv=(vec2(mod(tile,8.),7.-floor(tile/8.))+uv)/8.;gl_Position=projectionMatrix*modelViewMatrix*instanceMatrix*vec4(position,1.);}", fragmentShader: "uniform sampler2D map;varying vec2 vUv;void main(){gl_FragColor=texture2D(map,vUv)*vec4(1.,.72,.58,1.);\n#include <colorspace_fragment>\n}" }));
      const mesh = new T.InstancedMesh(geo, material, count);
      mesh.frustumCulled = false;
      state.scene.add(mesh);
      const rnd = seededRandom(55027), points = Array.from({ length: count }, () => {
        const z = rnd() * 2 - 1, a = rnd() * Math.PI * 2, r = radius * (0.85 + rnd() * 0.15);
        return new T.Vector3(Math.sqrt(1 - z * z) * Math.cos(a) * r, z * r, Math.sqrt(1 - z * z) * Math.sin(a) * r);
      }), dummy = new T.Object3D();
      return (p) => {
        points.forEach((v, i) => {
          dummy.position.copy(v).applyAxisAngle(new T.Vector3(0, 1, 0), p * Math.PI * 1.5);
          dummy.quaternion.copy(state.camera.quaternion);
          dummy.updateMatrix();
          mesh.setMatrixAt(i, dummy.matrix);
        });
        mesh.instanceMatrix.needsUpdate = true;
      };
    }
    async function build(shot) {
      const id = shot.id, a = assetMap.shots?.[id] || {}, scene = new T.Scene(), camera = new T.PerspectiveCamera(50, aspect, 0.01, 1e3);
      camera.position.z = 10;
      const state = { id, shot, a, scene, camera, owned: [], updates: [], afterCamera: [], disposeFns: [], effects: [], maskMesh: null, parallax: null, own(x) {
        this.owned.push(x);
        return x;
      } };
      try {
        diagnostics.shots[id] = { assets: a, method: PURE.has(id) ? "authored-code" : "depth-rig", cameraClamps: [], features: Object.keys(a.features || {}), unverified: [] };
        const path = (cameraPaths?.paths || cameraPaths)?.[id];
        if (!path) throw new Error(`${id}: camera path missing`);
        state.rig = createRigCamera({ THREE: T, camera, path: { ...path, cameraOwner: "code" }, width, height });
        state.rig.update(0, shot.f1 - shot.f0);
        if (!PURE.has(id)) {
          let zAt = function(u, v) {
            if (!state.depthPixels) return 0.02;
            const d = state.depthPixels, x = Math.max(0, Math.min(d.width - 1, Math.round(u * (d.width - 1)))), y = Math.max(0, Math.min(d.height - 1, Math.round(v * (d.height - 1))));
            return (d.data[(y * d.width + x) * 4] / 255 - 0.5) * (a.depthScale ?? 0.65) + 0.018;
          };
          if (id === "S25" && a.layers?.length !== 5) fail(id, "layers (exactly five separated RGBA sources with z)");
          if (!a.layers?.length && !a.depth) fail(id, "depth");
          const plate = await image(id === "S11" && a.support?.subject?.path ? a.support.subject.path : a.plate, id, "plate"), depth = a.depth ? await image(a.depth, id, "depth") : null;
          state.depthImage = depth;
          const layers = a.layers?.length ? await Promise.all(a.layers.map(async (l) => ({ ...l, image: await image(l.path, id, `layer:${l.id}`), rgba: true }))) : null;
          state.parallax = createParallax({ THREE: T, scene, plate: { image: plate, paddingFraction: 0.1, depthScale: a.depthScale ?? 0.65 }, depth, layers, width, height });
          state.parallax.setReferenceCamera(camera);
          state.disposeFns.push(() => state.parallax.dispose());
          if (a.mask) {
            const mask = await image(a.mask, id, "mask");
            const mt = state.own(new T.Texture(mask));
            mt.colorSpace = T.NoColorSpace;
            mt.needsUpdate = true;
            const mm = state.own(new T.ShaderMaterial({ transparent: true, side: T.DoubleSide, depthWrite: false, uniforms: { mask: { value: mt } }, vertexShader: "varying vec2 vUv;void main(){vUv=uv;gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.);}", fragmentShader: "varying vec2 vUv;uniform sampler2D mask;void main(){vec4 m=texture2D(mask,vUv);gl_FragColor=vec4(1.,1.,1.,m.r*m.a);}" }));
            state.maskMesh = new T.Mesh(state.parallax.geometry, mm);
            state.maskScene = new T.Scene();
            state.maskScene.add(state.maskMesh);
            if (["S11", "S13", "S27"].includes(id) || a.features?.halo) {
              const fm = state.own(new T.MeshBasicMaterial({ map: state.parallax.meshes[0].material.map, alphaMap: mt, transparent: true, depthWrite: false, depthTest: false, side: T.DoubleSide }));
              const fg = new T.Mesh(state.parallax.geometry, fm);
              fg.renderOrder = 50;
              state.parallax.group.add(fg);
            }
          }
          if (depth) {
            const dc = makeCanvas(depth.width, depth.height);
            dc.getContext("2d").drawImage(depth, 0, 0);
            state.depthPixels = dc.getContext("2d").getImageData(0, 0, dc.width, dc.height);
          }
          const features = a.features || {};
          const ornaments = [];
          const ornamentAnchors = [...(features.eyes || []).map((anchor) => ({ anchor, color: C2.ivory })), ...[...features.hairpin ? [features.hairpin] : [], ...features.tie ? [features.tie] : []].map((anchor) => ({ anchor, color: C2.clay }))];
          for (const { anchor, color } of ornamentAnchors) {
            const [u, v, size] = anchor, s = sparkMesh(state, Math.max(8e-3, size * worldW), 8e-3, color);
            s.position.set((u - 0.5) * worldW, (0.5 - v) * worldH, zAt(u, v));
            s.traverse((o) => {
              if (o.isMesh) {
                o.renderOrder = 60;
                o.material.depthTest = false;
                o.material.transparent = true;
                o.material.needsUpdate = true;
                o.userData.bloom = true;
              }
            });
            state.parallax.group.add(s);
            ornaments.push(s);
          }
          state.ornaments = ornaments;
          if (features.halo) {
            const [u, v, w, h] = features.halo, geo = state.own(new T.TorusGeometry(w * worldW / 2, 0.015, 8, 96)), mat = state.own(new T.MeshBasicMaterial({ color: C2.clay })), ring = new T.Mesh(geo, mat);
            ring.material.transparent = true;
            ring.material.needsUpdate = true;
            ring.renderOrder = 30;
            ring.scale.y = h * worldH / (w * worldW);
            ring.position.set((u - 0.5) * worldW, (0.5 - v) * worldH, zAt(u, v));
            state.parallax.group.add(ring);
          }
          if (a.poses?.length) {
            const poses = await Promise.all(a.poses.map(async (p) => ({ ...p, image: await image(p.path, id, "pose") })));
            const pose = localPlane(state, poses[0].image, worldW, worldH, 0, 0, 0.4);
            state.parallax.group.add(pose.mesh);
            state.updates.push((f) => {
              let select = poses[0];
              for (const p of poses) if (f >= p.frame) select = p;
              if (pose.texture.image !== select.image) {
                pose.texture.image = select.image;
                pose.texture.needsUpdate = true;
              }
            });
            diagnostics.shots[id].unverified.push("Replacement poses require a clean background plate to avoid duplicate bodies.");
          }
        }
        if (id === "S11" && a.support?.background?.path && a.support?.subject?.path) {
          const subjectGroup = new T.Group();
          const originalChildren = [...state.parallax.group.children];
          state.parallax.group.add(subjectGroup);
          for (const child of originalChildren) subjectGroup.add(child);
          subjectGroup.scale.setScalar(0.64);
          subjectGroup.position.y = -worldH * 0.12;
          state.maskTransform = subjectGroup;
          const background = localPlane(state, await image(a.support.background.path, id, "clean background"), worldW * 1.8, worldH * 1.8, 0, 0, -1.2);
          background.mesh.renderOrder = -20;
          state.parallax.group.add(background.mesh);
          diagnostics.shots[id].subjectLayout = { scale: 0.64, offsetYSourceFraction: 0.12, background: a.support.background.path, subject: a.support.subject.path, requiresMatchingOriginalDepthAndAnchors: true };
        } else if (id === "S11") {
          diagnostics.shots[id].unverified.push("Readable header composition requires support.background.path and support.subject.path matching original source coordinates; current full-frame body may occlude title.");
        }
        const addFx = (name, assets = {}) => {
          const effect = createEffect(name, { THREE: T, scene, camera, renderer, assets: { glyphAtlas, ...assets }, width, height });
          if (["TokenTunnel", "GlassCrack", "Mosaic"].includes(name)) effect.root.children.forEach((o, i) => {
            if (o.isMesh && (name !== "GlassCrack" || i === 0)) o.userData.bloom = true;
          });
          state.effects.push(effect);
          state.disposeFns.push(() => effect.dispose());
          return effect;
        };
        if (id === "S06") addFx("TokenTunnel");
        if (id === "S08b") {
          const box = state.own(new T.BoxGeometry(1.65, 4, 1.1)), mat = state.own(new T.MeshStandardMaterial({ color: C2.slate, roughness: 0.9 }));
          const light = new T.PointLight(C2.clay, 95, 35);
          light.position.set(0, 2, 4);
          scene.add(light, new T.AmbientLight(C2.ivory, 1.2));
          for (let row = 0; row < 14; row++) for (const side of [-1, 1]) {
            const rack = new T.Mesh(box, mat);
            rack.position.set(side * 3.2, 0, -row * 2.2);
            scene.add(rack);
            for (let slot = 0; slot < 6; slot++) {
              const panel = localPlane(state, labelCanvas(slot % 2 ? "\u601D\u8003" : "5.5", { w: 256, h: 64, size: 40, color: C2.clay, background: C2.slate }), 1.25, 0.28, side * 3.2, slot * 0.5 - 1.25, -row * 2.2 + 0.57);
              panel.mesh.rotation.y = side * -0.08;
            }
          }
        }
        if (id === "S09b" || id === "S10") {
          const s = sparkMesh(state, id === "S10" ? 2.6 : 3.1, 0.1, id === "S10" ? C2.slate : C2.clay);
          state.updates.push((f, p) => {
            if (id === "S10") {
              s.scale.set(2.6 / 100, -2.6 / 100, 2.6 / 100);
              s.position.y = 1.21;
              s.rotation.z = 0;
            } else {
              s.scale.setScalar(3.1 / 100 * (0.1 * Math.pow(60, p)));
              s.scale.y *= -1;
              s.rotation.z = p * Math.PI / 2;
            }
          });
        }
        if (id === "S11") {
          if (!assetMap.shell) fail(id, "assetMap.shell (shell-only RGBA)");
          addFx("Shatter", { egg: await texture(assetMap.shell, id, "shell") });
          const left = await raw("assets/brand/title-left.svg"), right = await raw("assets/brand/title-right.svg");
          const title = createTitleSlam({ THREE: T, scene, SVGLoader: SVGLoader2, svgPaths: { left, right }, sparkSVG: brand.svg, camera, fitCamera: false, position: [0, 1.6, 0.5] });
          state.afterCamera.push((f, p) => {
            title.update(f, shot.f1 - shot.f0);
            const distance = 6, viewH = 2 * distance * Math.tan(camera.fov * Math.PI / 360), scale = 180 / 1080 * viewH / title.metadata.capHeight;
            title.root.scale.setScalar(scale);
            title.root.quaternion.copy(camera.quaternion);
            title.root.position.set(0, (0.5 - 170 / 1080) * viewH, -distance).applyQuaternion(camera.quaternion).add(camera.position);
            title.root.updateMatrixWorld(true);
            if (f >= 5) {
              const box = new T.Box3().setFromObject(title.root.children[0]), limits = { left: Infinity, right: -Infinity, top: Infinity, bottom: -Infinity };
              for (const x of [box.min.x, box.max.x]) for (const y of [box.min.y, box.max.y]) for (const z of [box.min.z, box.max.z]) {
                const v = new T.Vector3(x, y, z).project(camera), px = (v.x * 0.5 + 0.5) * 1920, py = (0.5 - v.y * 0.5) * 1080;
                limits.left = Math.min(limits.left, px);
                limits.right = Math.max(limits.right, px);
                limits.top = Math.min(limits.top, py);
                limits.bottom = Math.max(limits.bottom, py);
              }
              diagnostics.shots[id].titleProjectedBounds = limits;
            }
          });
          state.disposeFns.push(() => title.dispose());
          diagnostics.shots[id].unverified.push("Title/foreground subject depth intersection requires visual review.");
        }
        if (id === "S19" || id === "S20") {
          const source = graphics.texture("ChatWindow", { frame: shot.f0 });
          const panel = localPlane(state, source, 9, 5.35, 0, 0, 0.6);
          panel.mesh.rotation.y = -0.12;
          state.updates.push((f) => {
            graphics.texture("ChatWindow", { frame: shot.f0 + f });
            panel.texture.needsUpdate = true;
          });
          if (id === "S20") addFx("GlassCrack", { plate: await texture(a.plate, id, "plate") });
        }
        if (["S09b", "S25", "S26"].includes(id)) addFx("SpeedLines");
        if (id === "S25") {
          for (let side of [-1, 1]) for (let j = 0; j < 8; j++) {
            const pl = localPlane(state, labelCanvas(["\u5929", "\u672A", "\u6765", "\u6211", "\u5728", "\u7231", "\u751F", "\u5149"][j], { w: 256, h: 256, size: 210, color: C2.clay, background: null }), 1.1, 1.1, side * (4.8 + j * 0.08), -4 + j * 1.3, -j * 0.18);
            pl.mesh.rotation.y = side * -0.35;
          }
        }
        if (id === "S27") {
          const cloud = glyphInstances(state, 1200, 4.4);
          state.updates.push((f, p) => cloud(p));
          const heart = sparkMesh(state, 0.65, 0.015);
          heart.position.set(0, 0.35, 0.8);
          const heartBase = heart.scale.clone();
          state.updates.push((f, p) => heart.scale.copy(heartBase).multiplyScalar(1 + 0.07 * Math.sin(f * 0.4)));
        }
        if (id === "S28a") {
          const plane = localPlane(state, graphics.texture("Stamp", { frame: shot.f0, width: 1920, height: 1080 }), worldW, worldH, 0, 0, 0.8);
          state.updates.push((f, p) => {
            plane.mesh.rotation.z = -0.14 * (1 - p);
            plane.mesh.scale.setScalar(1 + 0.4 * Math.exp(-f / 2));
          });
        }
        if (id === "S28b") {
          const c = graphics.texture("Toast", { frame: shot.f0, width: 1920, height: 1080 });
          const toast = state.own(new T.CanvasTexture(c));
          toast.colorSpace = T.SRGBColorSpace;
          const fx = addFx("ToastShatter", { toast });
          const inf = localPlane(state, labelCanvas("\u221E", { w: 512, h: 512, size: 280, family: "Newsreader", color: C2.clay, background: null }), 3, 3, 0, 0.1, 0.9);
          state.updates.push((f, p) => {
            inf.mesh.visible = f >= 3;
            fx.root.visible = f < 8;
          });
        }
        if (id === "S28c") {
          const cloud = localPlane(state, graphics.texture("LabelCloud", { frame: shot.f0, width: 1920, height: 1080 }), worldW, worldH, 0, 0, 0.9);
          state.updates.push((f, p) => {
            cloud.mesh.material.opacity = 1 - smooth(p * 2);
          });
        }
        if (id === "S29") addFx("InkBloom");
        if (id === "S34") {
          const rnd = seededRandom(5534), blooms = [];
          for (let i = 0; i < 80; i++) {
            const x = (rnd() - 0.5) * worldW, y = (rnd() - 0.5) * worldH;
            const bloom = i % 3 ? sparkMesh(state, 0.15 + rnd() * 0.2, 0.01) : localPlane(state, labelCanvas("{}", { w: 256, h: 256, size: 170, color: i % 2 ? C2.olive : C2.clay, background: null }), 0.4, 0.4).mesh;
            bloom.position.set(x, y, 0.4);
            blooms.push({ mesh: bloom, s: bloom.scale.clone(), at: rnd() * 0.6 });
          }
          state.updates.push((f, p) => blooms.forEach((b) => b.mesh.scale.copy(b.s).multiplyScalar(smooth((p - b.at) * 4))));
        }
        if (id === "S37") {
          const geometry = state.own(new T.TorusGeometry(3.2, 0.04, 10, 160)), material = state.own(new T.MeshBasicMaterial({ color: C2.clay })), ring = new T.Mesh(geometry, material);
          ring.position.z = 0.5;
          scene.add(ring);
          for (let i = 0; i < 12; i++) {
            const a2 = i * Math.PI / 6, pl = localPlane(state, labelCanvas("5.5", { w: 256, h: 128, size: 85, family: "Newsreader", color: C2.clay, background: null }), 0.45, 0.225, Math.sin(a2) * 3.3, Math.cos(a2) * 3.3, 0.55);
            pl.mesh.rotation.z = -a2;
          }
        }
        if (id === "S38") {
          if (!assetMap.mosaicAtlas) fail(id, "assetMap.mosaicAtlas extracted from completed S01\u2013S37");
          if (assetMap.mosaicIsTest && !assetMap.allowTestMosaic) throw new Error("S38 test mosaic requires explicit assetMap.allowTestMosaic");
          addFx("Mosaic", { mosaicAtlas: await texture(assetMap.mosaicAtlas, id, "mosaicAtlas"), sparkSVG: brand.svg });
          diagnostics.shots[id].mosaicTest = !!assetMap.mosaicIsTest;
        }
        if (id === "S02") {
          for (let i = 0; i < 4; i++) {
            const pl = localPlane(state, labelCanvas(graphics.codeStrings.billboards[i], { size: i === 1 ? 65 : 90 }), 3.1, 0.77, [-5, -1.7, 1.7, 5][i], 2.2, -0.1);
            pl.mesh.rotation.y = (i - 1.5) * -0.05;
          }
          const clock = localPlane(state, labelCanvas("\u660E\u5929", { w: 512, h: 256, size: 150 }), 1.9, 0.95, 0, 3.35, 0.1);
          state.updates.push((f) => clock.mesh.rotation.x = Math.PI * (1 - smooth((f - (52 - shot.f0) + 5) / 5)));
          diagnostics.shots[id].unverified.push("Billboard plane placement must match generated blank hardware locations.");
        }
        if (id === "S26") for (let i = 0; i < 7; i++) {
          const bar = localPlane(state, labelCanvas("5.5", { w: 256, h: 512, size: 95, family: "Newsreader", color: C2.ivory, background: C2.clay }), 0.72, 1.2 + i * 0.35, -3 + i, -3 + (1.2 + i * 0.35) / 2, 0.4);
          state.updates.push((f) => bar.mesh.scale.y = smooth((f - i * 2.4) / 8));
        }
        await installShotDetails({ state, THREE: T, SVGLoader: SVGLoader2, assetMap, image, texture, raw, fail, worldW, worldH, width, height, glyphAtlas, localPlane, labelCanvas, sparkMesh, brand, diagnostics });
        state.dispose = () => {
          for (const fn of state.disposeFns) fn();
          for (const r of state.owned) r.dispose();
          scene.clear();
        };
        return state;
      } catch (error) {
        for (const fn of state.disposeFns) fn();
        for (const r of state.owned) r.dispose();
        scene.clear();
        throw error;
      }
    }
    async function getState(shot) {
      if (!states.has(shot.id)) {
        const state = await build(shot);
        states.set(shot.id, state);
        if (states.size > 2) {
          const [key, old] = states.entries().next().value;
          if (key !== shot.id) {
            old.dispose();
            states.delete(key);
          }
        }
      }
      return states.get(shot.id);
    }
    function sceneSample(state, local, duration) {
      const p = clamp6(local / Math.max(1, duration - 1));
      state.rig.update(local, duration);
      const authoredPose = { position: state.camera.position.clone(), quaternion: state.camera.quaternion.clone(), fov: state.camera.fov };
      for (const effect of state.effects) {
        effect.update(local, p);
        state.camera.position.copy(authoredPose.position);
        state.camera.quaternion.copy(authoredPose.quaternion);
        state.camera.fov = authoredPose.fov;
        state.camera.updateProjectionMatrix();
        state.camera.updateMatrixWorld(true);
      }
      for (const fn of state.updates) fn(local, p);
      if (state.parallax) {
        const constraint = state.parallax.constrainCamera(state.camera);
        if (constraint.clamped) {
          const d = diagnostics.shots[state.id];
          if (d.cameraClamps.length < 20) d.cameraClamps.push({ frame: local, ...constraint });
        }
        state.parallax.update(state.camera);
      }
      for (const fn of state.afterCamera) fn(local, p);
      renderer.setClearColor(["S06", "S08b"].includes(state.id) ? C2.slate : C2.paper, 1);
      renderer.render(state.scene, state.camera);
    }
    function composeMask(state) {
      maskCtx.clearRect(0, 0, width, height);
      if (state.maskMesh) {
        state.parallax.group.updateMatrixWorld(true);
        state.maskMesh.matrixAutoUpdate = false;
        state.maskMesh.matrix.copy((state.maskTransform || state.parallax.group).matrixWorld);
        renderer.setClearColor(0, 0);
        renderer.render(state.maskScene, state.camera);
        maskCtx.drawImage(renderer.domElement, 0, 0);
      }
      return state.maskMesh ? maskCanvas : null;
    }
    async function renderFrame(frame) {
      if (disposed) throw new Error("Film disposed");
      if (!Number.isInteger(frame) || frame < 0 || frame >= totalFrames) throw new Error(`Frame ${frame} outside 0..${totalFrames - 1}`);
      let f = frame;
      if (frame >= totalFrames - 12) f = totalFrames - 12;
      const shot = shots2.find((s) => f >= s.f0 && f < s.f1);
      if (!shot) throw new Error(`No shot owns frame ${frame}`);
      if (shot.id === "S10") f = shot.f0;
      if (f === 0) {
        out.fillStyle = "#000";
        out.fillRect(0, 0, width, height);
        return canvas;
      }
      const state = await getState(shot), local = f - shot.f0, duration = shot.f1 - shot.f0, path = (cameraPaths.paths || cameraPaths)[shot.id], whip = /WHIP/i.test(path.move || shot.cam || ""), samples = whip ? 6 : 1;
      ctx.clearRect(0, 0, width, height);
      for (let i = 0; i < samples; i++) {
        const sample = Math.max(0, Math.min(duration - 1, local + (i / (samples - 1 || 1) - 0.5) * 0.5));
        sceneSample(state, sample, duration);
        ctx.globalAlpha = 1 / (i + 1);
        ctx.drawImage(renderer.domElement, 0, 0);
      }
      ctx.globalAlpha = 1;
      sceneSample(state, local, duration);
      const subjectMask = composeMask(state);
      if (state.composite) {
        state.composite(ctx, local, clamp6(local / Math.max(1, duration - 1)));
        if (state.parallax) state.parallax.group.visible = false;
        renderer.setClearColor(0, 0);
        renderer.render(state.scene, state.camera);
        ctx.drawImage(renderer.domElement, 0, 0);
        if (state.parallax) state.parallax.group.visible = true;
      }
      if (/^S36[bdfh]$/.test(shot.id) && local < 3) {
        const snap = makeCanvas(width, height);
        snap.getContext("2d").drawImage(comp, 0, 0);
        ctx.save();
        for (let i = 3; i > 0; i--) {
          ctx.globalAlpha = 0.09 * (1 - local / 3);
          ctx.drawImage(snap, -i * width * 0.012, 0, width * (1 + i * 0.018), height);
        }
        ctx.restore();
      }
      ctx.save();
      if (shot.id === "S39") {
        const k = 1 + 0.02 * smooth(local / Math.max(1, duration - 13));
        ctx.translate(width / 2, height / 2);
        ctx.scale(k, k);
        ctx.translate(-width / 2, -height / 2);
      }
      graphics.draw(ctx, { frame: f, shot: shot.id === "S05" ? { ...shot, id: "S05_graphics" } : shot, localFrame: local, subjectMask, uiIn3D: true, drawLyrics: shot.id !== "S15" });
      if (shot.id === "S05") {
        const boxes = (state.a.features?.eyes || []).map(([u, v, size]) => {
          const pt = new T.Vector3((u - 0.5) * worldW, (0.5 - v) * worldH, 0.1);
          if (state.parallax) pt.applyMatrix4(state.parallax.group.matrixWorld);
          pt.project(state.camera);
          return { x: (pt.x * 0.5 + 0.5) * 1920, y: (0.5 - pt.y * 0.5) * 1080, r: Math.max(110, size * 1920 * 2) };
        });
        const candidates = [[1190, 700], [130, 700], [1190, 275], [130, 140]];
        const overlap = ([x2, y2]) => boxes.reduce((sum, e) => sum + (x2 < e.x + e.r && x2 + 440 > e.x - e.r && y2 < e.y + e.r && y2 + 130 > e.y - e.r ? 1 : 0), 0);
        candidates.sort((a, b) => overlap(a) - overlap(b));
        const [x, y] = candidates[0];
        ctx.save();
        ctx.scale(width / 1920, height / 1080);
        graphics.components.ChatBubble(ctx, { frame: f, x, y });
        ctx.restore();
        diagnostics.shots.S05.bubblePlacement = { x, y, eyeBoxOverlaps: overlap([x, y]) };
      }
      ctx.restore();
      if (shot.id === "S28b" && local >= 3) {
      }
      const visibility = [];
      state.scene.traverse((o) => {
        if (o.isMesh || o.isLine || o.isPoints) {
          visibility.push([o, o.visible]);
          o.visible = o.visible && !!o.userData.bloom;
        }
      });
      renderer.setClearColor(0, 1);
      renderer.render(state.scene, state.camera);
      glowCanvas.getContext("2d").drawImage(renderer.domElement, 0, 0);
      for (const [o, visible] of visibility) o.visible = visible;
      glowTexture.needsUpdate = true;
      let impactAge = -1;
      for (const start of IMPACT) if (f >= start && f < start + 3) impactAge = f - start;
      if (impactAge === 0 || shot.id === "S20" && local >= duration - 2) {
        out.fillStyle = "#fff";
        out.fillRect(0, 0, width, height);
        return canvas;
      }
      let age = 999;
      for (const k of onsets.kicks || []) {
        const kf = Math.round((typeof k === "number" ? k : k.t) * fps);
        if (kf <= f) age = Math.min(age, f - kf);
      }
      postTexture.needsUpdate = true;
      postUniforms.shock.value = state.shock || 0;
      postUniforms.shockActive.value = state.shockActive ? 1 : 0;
      postUniforms.frame.value = f;
      postUniforms.chorus.value = smooth((f - 359) / 8);
      postUniforms.impact.value = impactAge > 0 ? 2 : 0;
      postUniforms.pulse.value = f >= 359 && shot.id !== "S10" && f < totalFrames - 12 ? Math.exp(-age / 2.3) : 0;
      postRenderer.render(postScene, postCamera);
      out.drawImage(postRenderer.domElement, 0, 0);
      diagnostics.renderedFrames.push(frame);
      if (diagnostics.renderedFrames.length > 256) diagnostics.renderedFrames.shift();
      return canvas;
    }
    return { canvas, renderFrame, diagnostics, dispose() {
      disposed = true;
      for (const s of states.values()) s.dispose();
      for (const r of resources) r.dispose();
      renderer.dispose();
      postRenderer.dispose();
      images.clear();
      textures.clear();
      states.clear();
    } };
  }

  // episodes/first-day-anime2/project/helper/camera_paths.json
  var camera_paths_default = {
    schemaVersion: 1,
    fps: 30,
    paths: {
      S01: {
        id: "S01",
        move: "MACRO-PUSH",
        sourceInstruction: "Locked macro; 3% push-in over the shot, ease-out. No shake.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 32,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.70873786407767
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.16,
          1,
          0.3,
          1
        ],
        filmstripQA: "pending-render",
        seed: 235
      },
      S02: {
        id: "S02",
        move: "DOLLY-IN-RAMP",
        sourceInstruction: "DOLLY-IN-RAMP straight down the central aisle through the crowd, 28 % travel, starts creeping then accelerates; roll 1\xB0 drifting.",
        sourceKind: "GEN-I25",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              7.2
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 1
          }
        ],
        ease: [
          0.55,
          0.055,
          0.675,
          0.19
        ],
        filmstripQA: "pending-render",
        seed: 236
      },
      S03: {
        id: "S03",
        move: "ORBIT-45",
        sourceInstruction: "Slow ORBIT-45 around the egg, then settles; shallow DOF, floating particles in parallax.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -7.071067811865475,
              0,
              7.0710678118654755
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              -6.343932841636455,
              0,
              7.73010453362737
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              -5.555702330196022,
              0,
              8.314696123025453
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.375,
            pos: [
              -4.7139673682599765,
              0,
              8.819212643483551
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              -3.826834323650898,
              0,
              9.238795325112868
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.625,
            pos: [
              -2.902846772544623,
              0,
              9.569403357322088
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              -1.9509032201612824,
              0,
              9.807852804032304
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.875,
            pos: [
              -0.980171403295606,
              0,
              9.95184726672197
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 237,
        generationCameraInstruction: "Slow ORBIT-45 around the egg, then settles; shallow DOF, floating particles in parallax.",
        globalEase: [
          0.16,
          1,
          0.3,
          1
        ]
      },
      S04: {
        id: "S04",
        move: "CRANE-UP",
        sourceInstruction: "CRANE-UP + slow tilt-down to keep her centred; handheld-breath noise 0.3 px.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              1.8,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 238,
        generationCameraInstruction: "CRANE-UP + slow tilt-down to keep her centred; handheld-breath noise 0.3 px.",
        shake: {
          amplitudePx: 0.3,
          frequency: 8
        }
      },
      S05: {
        id: "S05",
        move: "SNAP-ZOOM",
        sourceInstruction: "SNAP-ZOOM: starts wide on her face, 6-frame whip-in to the eye exactly at 5.23, then slow creep.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 40,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 60,
            roll: 0
          },
          {
            t: 0.15,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 24,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.7
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 24,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 239,
        generationCameraInstruction: "SNAP-ZOOM: starts wide on her face, 6-frame whip-in to the eye exactly at 5.23, then slow creep."
      },
      S06: {
        id: "S06",
        move: "FORWARD",
        sourceInstruction: "Warp-speed FORWARD fly-through, FOV 55\u219295\xB0 ramp, tiny roll; speed \xD73 at 7.19 (kick).",
        sourceKind: "CODE3D",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 55,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              2
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 95,
            roll: 2
          }
        ],
        ease: [
          0.33,
          0,
          0.67,
          1
        ],
        filmstripQA: "pending-render",
        seed: 240,
        speedRamp: [
          [
            0,
            1
          ],
          [
            0.49,
            1
          ],
          [
            0.5,
            3
          ],
          [
            1,
            3
          ]
        ]
      },
      S07: {
        id: "S07",
        move: "PULL-BACK",
        sourceInstruction: "PULL-BACK + slight rise, ends on wide hero silhouette; 2 % handheld.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              8
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0.6,
              12
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 241,
        generationCameraInstruction: "PULL-BACK + slight rise, ends on wide hero silhouette; 2 % handheld.",
        shake: {
          amplitudePx: 14,
          frequency: 8
        }
      },
      S08a: {
        id: "S08a",
        move: "PUSH-IN",
        sourceInstruction: "Fast PUSH-IN on hand, shutter-smear.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 11,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              7
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 339,
        shutter: 180,
        shutterSamples: 8
      },
      S08b: {
        id: "S08b",
        move: "ONE-POINT-DRIFT",
        sourceInstruction: "Locked-off wide, one-point perspective; the light wave IS the motion.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.98
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 340,
        override: "Hard rule camera-never-static takes priority: minimal 0.2\u20130.5% drift preserves locked/macro composition."
      },
      S08c: {
        id: "S08c",
        move: "TILT-UP",
        sourceInstruction: "Low-angle TILT-UP whip.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -2,
              10
            ],
            target: [
              0,
              -1,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -2,
              10
            ],
            target: [
              0,
              2,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 341,
        shutter: 180,
        shutterSamples: 8
      },
      S08d: {
        id: "S08d",
        move: "RISE",
        sourceInstruction: "RISE + slight dolly-forward.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -0.7,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0.7,
              9
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 342
      },
      S09a: {
        id: "S09a",
        move: "ZOOM-IN-4X",
        sourceInstruction: "Rapid ZOOM-IN 4\xD7.",
        sourceKind: "GEN-I25",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 60,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 16.426421403476375,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 340
      },
      S09b: {
        id: "S09b",
        move: "SPARK-EXPANSION",
        sourceInstruction: "Scale 0.1\u21926.0 exponential ease-in, rotation +90\xB0.",
        sourceKind: "CODE3D",
        cameraOwner: "code",
        durationFrames: 11,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              60
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              1
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 90
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 341
      },
      S10: {
        id: "S10",
        move: "FREEZE",
        sourceInstruction: "ABSOLUTELY LOCKED. Only a 1 %-in-0.68 s linear scale creep. (Contrast with the previous 6 cuts matters.)",
        sourceKind: "CODE",
        cameraOwner: "code",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 235,
        freeze: true,
        override: "Hard rule: full-frame freeze overrides contradictory 1% creep."
      },
      S11: {
        id: "S11",
        move: "WHIP-IN",
        sourceInstruction: "WHIP-IN from the frozen spark to a hero low-angle; 12 f slow-mo (40 %) then snap back to 100 % at 12.31; camera shake 14 px decaying over 20 f.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 21,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -2,
              16
            ],
            target: [
              0,
              1,
              0
            ],
            fov: 70,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              0,
              -1,
              8
            ],
            target: [
              0,
              0.4,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -0.8,
              7.8
            ],
            target: [
              0,
              0.4,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 236,
        speedRamp: [
          [
            0,
            0.4
          ],
          [
            0.5714285714285714,
            0.4
          ],
          [
            0.6190476190476191,
            1
          ],
          [
            1,
            1
          ]
        ],
        shake: {
          amplitudePx: 14,
          frequency: 16,
          decayFrames: 20
        },
        shutter: 180,
        shutterSamples: 8
      },
      S12: {
        id: "S12",
        move: "ORBIT-120",
        sourceInstruction: "ORBIT-120 fast arc ending dead-on her face; 12 f ease-out into the last 2\xB0.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -8.660254037844387,
              0,
              -4.999999999999998
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              -9.659258262890683,
              0,
              -2.5881904510252083
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              -10,
              0,
              6123233995736766e-31
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.375,
            pos: [
              -9.659258262890683,
              0,
              2.5881904510252074
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              -8.660254037844386,
              0,
              5.000000000000001
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.625,
            pos: [
              -7.071067811865475,
              0,
              7.0710678118654755
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              -4.999999999999999,
              0,
              8.660254037844387
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.875,
            pos: [
              -2.5881904510252074,
              0,
              9.659258262890683
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 237,
        generationCameraInstruction: "ORBIT-120 fast arc ending dead-on her face; 12 f ease-out into the last 2\xB0.",
        globalEase: [
          0.16,
          1,
          0.3,
          1
        ]
      },
      S13: {
        id: "S13",
        move: "CRANE-UP",
        sourceInstruction: "CRANE-UP with 2\xB0 roll; lens flare passes on beat 3 (14.0).",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -0.9,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0.9,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 2
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 238,
        generationCameraInstruction: "CRANE-UP with 2\xB0 roll; lens flare passes on beat 3 (14.0)."
      },
      S14: {
        id: "S14",
        move: "AIRFLOW-TRACK",
        sourceInstruction: "50 % slow-mo, camera TRACKS the airflow by gliding INTO the stream; speed ramps to 100 % at 15.7.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -1,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              1,
              0,
              7
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 239,
        generationCameraInstruction: "50 % slow-mo, camera TRACKS the airflow by gliding INTO the stream; speed ramps to 100 % at 15.7.",
        speedRamp: [
          [
            0,
            0.5
          ],
          [
            0.73,
            0.5
          ],
          [
            0.8,
            1
          ],
          [
            1,
            1
          ]
        ]
      },
      S15: {
        id: "S15",
        move: "PULL-OUT",
        sourceInstruction: "PULL-OUT through the ring while a 360\xB0 tilt-shift sweep reveals the sky; speed ramp 70 \u2192 120 %.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              8
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              0,
              0,
              8.75
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 45
          },
          {
            t: 0.25,
            pos: [
              0,
              0,
              9.5
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 90
          },
          {
            t: 0.375,
            pos: [
              0,
              0,
              10.25
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 135
          },
          {
            t: 0.5,
            pos: [
              0,
              0,
              11
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 180
          },
          {
            t: 0.625,
            pos: [
              0,
              0,
              11.75
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 225
          },
          {
            t: 0.75,
            pos: [
              0,
              0,
              12.5
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 270
          },
          {
            t: 0.875,
            pos: [
              0,
              0,
              13.25
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 315
          },
          {
            t: 1,
            pos: [
              0,
              0,
              14
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 360
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 240,
        generationCameraInstruction: "PULL-OUT through the ring while a 360\xB0 tilt-shift sweep reveals the sky; speed ramp 70 \u2192 120 %.",
        speedRamp: [
          [
            0,
            0.7
          ],
          [
            1,
            1.2
          ]
        ]
      },
      S16: {
        id: "S16",
        move: "FLOOR-DOLLY-BACK",
        sourceInstruction: "Locked low, floor-level; slight dolly-back.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -3,
              8
            ],
            target: [
              0,
              -3,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -3,
              8.5
            ],
            target: [
              0,
              -3,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 241,
        generationCameraInstruction: "Locked low, floor-level; slight dolly-back."
      },
      S17: {
        id: "S17",
        move: "TILT-UP",
        sourceInstruction: "TILT-UP reveal, 1.36 s, ease-in-out; ripple triggers a 2 f camera dip (\u22126 px).",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -2,
              10
            ],
            target: [
              0,
              -2,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -2,
              10
            ],
            target: [
              0,
              1,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 242,
        dip: {
          frame: 0,
          frames: 2,
          pixels: -6
        }
      },
      S18: {
        id: "S18",
        move: "POV-PUSH",
        sourceInstruction: "POV push-in, gentle float; DOF rack from hand to her fingertip at 19.9.",
        sourceKind: "UI",
        cameraOwner: "code",
        durationFrames: 21,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 7
          },
          {
            t: 0.63,
            pos: [
              0,
              0,
              9.6
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 10
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.4
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 10
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 243,
        shake: {
          amplitudePx: 0.5,
          frequency: 8
        }
      },
      S19: {
        id: "S19",
        move: "TRUCK",
        sourceInstruction: "Slow lateral TRUCK left\u2192right + subtle dolly-in; focus pulls from screen to her face reflected.",
        sourceKind: "UI",
        cameraOwner: "code",
        durationFrames: 40,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -0.6,
              0,
              10
            ],
            target: [
              -0.6,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 8
          },
          {
            t: 1,
            pos: [
              0.6,
              0,
              9.6
            ],
            target: [
              0.6,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 10
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 244
      },
      S20: {
        id: "S20",
        move: "PUSH-THROUGH",
        sourceInstruction: "PUSH-THROUGH at accelerating speed (dolly 1\xD7\u21924\xD7); FOV 40\u219280\xB0.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 40,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              1
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 80,
            roll: 0
          }
        ],
        ease: [
          0.33,
          0,
          0.67,
          1
        ],
        filmstripQA: "pending-render",
        seed: 236,
        speedRamp: [
          [
            0,
            1
          ],
          [
            1,
            4
          ]
        ]
      },
      S21: {
        id: "S21",
        move: "LOW-DOLLY-OUT",
        sourceInstruction: "EPIC LOW WIDE + fast DOLLY-OUT 15 %, anamorphic flare.",
        sourceKind: "GEN-I25",
        cameraOwner: "code",
        durationFrames: 21,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -1.4,
              10
            ],
            target: [
              0,
              0.4,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -1.4,
              11.5
            ],
            target: [
              0,
              0.4,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 237
      },
      S22: {
        id: "S22",
        move: "DUTCH-PUSH",
        sourceInstruction: "Medium close, quick PUSH-IN + 3\xB0 Dutch.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              8.5
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 3
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 238,
        generationCameraInstruction: "Medium close, quick PUSH-IN + 3\xB0 Dutch."
      },
      S23: {
        id: "S23",
        move: "SNAP-FOCUS",
        sourceInstruction: "Snap-focus rack from Opus\u2019s shoulder to Haiku.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 21,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 7
          },
          {
            t: 0.3,
            pos: [
              0,
              0,
              9.98
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 10
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.95
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0,
            focusDistance: 10
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 239,
        generationCameraInstruction: "Snap-focus rack from Opus\u2019s shoulder to Haiku.",
        override: "Hard rule camera-never-static takes priority: minimal 0.2\u20130.5% drift preserves locked/macro composition."
      },
      S24: {
        id: "S24",
        move: "WHIP",
        sourceInstruction: "Low WHIP-PAN left\u2192right, ends on Opus.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -1,
              10
            ],
            target: [
              -8,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.3,
            pos: [
              0,
              -1,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0.05,
              -1,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 240,
        generationCameraInstruction: "Low WHIP-PAN left\u2192right, ends on Opus.",
        shutter: 180,
        shutterSamples: 8
      },
      S25: {
        id: "S25",
        move: "FOLLOW-CAM",
        sourceInstruction: "FOLLOW-CAM behind-and-below, fast, FOV 50\u2192100\xB0, banking roll \xB112\xB0.",
        sourceKind: "GEN-I25",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -2,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.33,
            pos: [
              0,
              1,
              8
            ],
            target: [
              0,
              3,
              0
            ],
            fov: 65,
            roll: 12
          },
          {
            t: 0.66,
            pos: [
              0,
              5,
              6
            ],
            target: [
              0,
              7,
              0
            ],
            fov: 85,
            roll: -12
          },
          {
            t: 1,
            pos: [
              0,
              10,
              4
            ],
            target: [
              0,
              12,
              0
            ],
            fov: 100,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 241,
        followLagFrames: 6,
        layerRequirement: "five independent depth layers; animate subject six frames ahead of camera follow trajectory"
      },
      S26: {
        id: "S26",
        move: "CRANE-UP",
        sourceInstruction: "Vertical CRANE-UP then tilt to horizon; lens flare sweeps.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -1,
              10
            ],
            target: [
              0,
              2,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.6,
            pos: [
              0,
              1,
              10
            ],
            target: [
              0,
              2,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              2,
              10
            ],
            target: [
              0,
              2,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 242,
        generationCameraInstruction: "Vertical CRANE-UP then tilt to horizon; lens flare sweeps."
      },
      S27: {
        id: "S27",
        move: "BULLET",
        sourceInstruction: "BULLET orbit 270\xB0 around her over 1.36 s, time near-frozen (3 % speed); ends front-on.",
        sourceKind: "CODE3D",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -6.4278760968653925,
              0,
              7.66044443118978
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              -5.7357643635104605,
              0,
              8.191520442889917
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              -4.999999999999999,
              0,
              8.660254037844387
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.375,
            pos: [
              -4.2261826174069945,
              0,
              9.063077870366499
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              -3.420201433256687,
              0,
              9.396926207859085
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.625,
            pos: [
              -2.5881904510252074,
              0,
              9.659258262890683
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              -1.7364817766693033,
              0,
              9.84807753012208
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.875,
            pos: [
              -0.8715574274765816,
              0,
              9.961946980917455
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 243,
        actionTimeScale: 0.03,
        fallback: "Plan option B: 40-degree depth-rig camera orbit plus a separate 360-degree particle-sphere rotation; 270-degree generated orbit remains preferred when available.",
        particleRotationDegrees: 360
      },
      S28a: {
        id: "S28a",
        move: "PUNCH-IN",
        sourceInstruction: "Punch-in 1.3\xD7, shake.",
        sourceKind: "UI",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              7.692307692307692
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 341,
        shake: {
          amplitudePx: 9,
          frequency: 8
        }
      },
      S28b: {
        id: "S28b",
        move: "ROLL",
        sourceInstruction: "Locked, slight roll.",
        sourceKind: "UI",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 2
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 342
      },
      S28c: {
        id: "S28c",
        move: "WHIP-TILT",
        sourceInstruction: "Whip-tilt up.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 11,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              -2,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.6,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              3,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              3.05,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 343,
        shutter: 180,
        shutterSamples: 8
      },
      S29: {
        id: "S29",
        move: "INK-DIVE",
        sourceInstruction: "Camera dives into the ink at 3\xD7 speed.",
        sourceKind: "CODE3D",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              2,
              10
            ],
            target: [
              0,
              -2,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -1,
              2
            ],
            target: [
              0,
              -2,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.33,
          0,
          0.67,
          1
        ],
        filmstripQA: "pending-render",
        seed: 245
      },
      S30: {
        id: "S30",
        move: "LOW-TRACK",
        sourceInstruction: "Long, smooth LOW TRACKING SHOT alongside, 1.36 s, no cuts, slow drift; stillness contrast.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -0.5,
              -2,
              10
            ],
            target: [
              -0.5,
              -2,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0.5,
              -2,
              10
            ],
            target: [
              0.5,
              -2,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 237,
        generationCameraInstruction: "Long, smooth LOW TRACKING SHOT alongside, 1.36 s, no cuts, slow drift; stillness contrast."
      },
      S31: {
        id: "S31",
        move: "DOLLY-ZOOM",
        sourceInstruction: "DOLLY-ZOOM (vertigo): dolly-in while zooming out so the background stretches; completes exactly on 33.789.",
        sourceKind: "GEN-V",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              6
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 238,
        generationCameraInstruction: "Locked camera; character turns and extends her hand. No generated dolly or zoom.",
        dollyZoom: {
          target: [
            0,
            0,
            0
          ],
          frustumHeight: 9.326153163099972
        }
      },
      S32: {
        id: "S32",
        move: "HANDHELD-PUSH",
        sourceInstruction: "Tight handheld push-in, 2 % shake.",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 239,
        generationCameraInstruction: "Tight handheld push-in, 2 % shake.",
        shake: {
          amplitudePx: 14,
          frequency: 8
        }
      },
      S33: {
        id: "S33",
        move: "TRUCK",
        sourceInstruction: "Lateral TRUCK 12 %, parallax.",
        sourceKind: "GEN-I25",
        cameraOwner: "code",
        durationFrames: 21,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -0.995,
              0,
              10
            ],
            target: [
              -0.995,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0.995,
              0,
              10
            ],
            target: [
              0.995,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 240
      },
      S34: {
        id: "S34",
        move: "SPIRAL-DOWN",
        sourceInstruction: "SPIRAL-DOWN 90\xB0 twist.",
        sourceKind: "GEN-I25",
        cameraOwner: "code",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0.35,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              0.34327484814113063,
              0.06828161270564488,
              9.625
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 11.25
          },
          {
            t: 0.25,
            pos: [
              0.3233578363789503,
              0.13393920132778142,
              9.25
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 22.5
          },
          {
            t: 0.375,
            pos: [
              0.29101436430589084,
              0.19444958155686076,
              8.875
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 33.75
          },
          {
            t: 0.5,
            pos: [
              0.24748737341529164,
              0.2474873734152916,
              8.5
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 45
          },
          {
            t: 0.625,
            pos: [
              0.1944495815568608,
              0.29101436430589084,
              8.125
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 56.25
          },
          {
            t: 0.75,
            pos: [
              0.13393920132778142,
              0.3233578363789503,
              7.75
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 67.5
          },
          {
            t: 0.875,
            pos: [
              0.06828161270564491,
              0.34327484814113063,
              7.375
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 78.75
          },
          {
            t: 1,
            pos: [
              2143131898507868e-32,
              0.35,
              7
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 90
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 241
      },
      S35: {
        id: "S35",
        move: "WHIP",
        sourceInstruction: "WHIP-PAN 180\xB0 (motion blur 180\xB0).",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 20,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              0,
              0,
              10
            ],
            target: [
              7.071067811865475,
              0,
              2.9289321881345245
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              0,
              0,
              10
            ],
            target: [
              10,
              0,
              10
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              0,
              0,
              10
            ],
            target: [
              7.0710678118654755,
              0,
              17.071067811865476
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              12246467991473533e-31,
              0,
              20
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 242,
        generationCameraInstruction: "WHIP-PAN 180\xB0 (motion blur 180\xB0).",
        shutter: 180,
        shutterSamples: 8
      },
      S36a: {
        id: "S36a",
        move: "POSE-IMPACT",
        sourceInstruction: "Static + 1 f shake",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 11,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.98
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 340,
        generationCameraInstruction: "Static + 1 f shake",
        shake: {
          amplitudePx: 8,
          frequency: 15,
          onlyFrames: 1
        },
        override: "Hard rule camera-never-static takes priority: minimal 0.2\u20130.5% drift preserves locked/macro composition."
      },
      S36b: {
        id: "S36b",
        move: "MACRO-DRIFT",
        sourceInstruction: "Macro lock",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.98
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 341,
        generationCameraInstruction: "Macro lock",
        override: "Hard rule camera-never-static takes priority: minimal 0.2\u20130.5% drift preserves locked/macro composition."
      },
      S36c: {
        id: "S36c",
        move: "DUTCH-DRIFT",
        sourceInstruction: "Static, 4\xB0 dutch",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 4
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.98
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 4
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 342,
        generationCameraInstruction: "Static, 4\xB0 dutch",
        override: "Hard rule camera-never-static takes priority: minimal 0.2\u20130.5% drift preserves locked/macro composition."
      },
      S36d: {
        id: "S36d",
        move: "TILT-UP",
        sourceInstruction: "Low tilt-up",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              -1,
              10
            ],
            target: [
              0,
              -1,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              -1,
              10
            ],
            target: [
              0,
              1,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 343,
        generationCameraInstruction: "Low tilt-up"
      },
      S36e: {
        id: "S36e",
        move: "CRANE-DOWN",
        sourceInstruction: "High crane-down",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 11,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              2,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0.5,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 344,
        generationCameraInstruction: "High crane-down"
      },
      S36f: {
        id: "S36f",
        move: "PULL-BACK",
        sourceInstruction: "Pull-back 25 %",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              12.5
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 345
      },
      S36g: {
        id: "S36g",
        move: "ORBIT-60",
        sourceInstruction: "Orbit 60\xB0 at 3 % time",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              -8.660254037844386,
              0,
              5.000000000000001
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              -7.933533402912351,
              0,
              6.087614290087206
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              -7.071067811865475,
              0,
              7.0710678118654755
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.375,
            pos: [
              -6.087614290087206,
              0,
              7.933533402912351
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              -4.999999999999999,
              0,
              8.660254037844387
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.625,
            pos: [
              -3.826834323650898,
              0,
              9.238795325112868
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              -2.5881904510252074,
              0,
              9.659258262890683
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.875,
            pos: [
              -1.3052619222005157,
              0,
              9.914448613738104
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 346,
        generationCameraInstruction: "Orbit 60\xB0 at 3 % time",
        actionTimeScale: 0.03
      },
      S36h: {
        id: "S36h",
        move: "SNAP-ZOOM",
        sourceInstruction: "Snap zoom 1.5\xD7",
        sourceKind: "GEN-V",
        cameraOwner: "generation",
        durationFrames: 10,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.6,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 34.537989140896116,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.98
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 34.537989140896116,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 347,
        generationCameraInstruction: "Snap zoom 1.5\xD7"
      },
      S37: {
        id: "S37",
        move: "PULL-OUT",
        sourceInstruction: "PULL-OUT (macro to wide) over 1.36 s, ease-in-out, no cuts.",
        sourceKind: "HYB",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              0.5
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              0,
              0,
              0.7438689130822451
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              0,
              0,
              1.1066819197003215
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.375,
            pos: [
              0,
              0,
              1.6464525534705015
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              0,
              0,
              2.449489742783178
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.625,
            pos: [
              0,
              0,
              3.644198545140462
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              0,
              0,
              5.421612021659069
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.875,
            pos: [
              0,
              0,
              8.065937283410332
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              12
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 244,
        globalEase: [
          0.42,
          0,
          0.58,
          1
        ]
      },
      S38: {
        id: "S38",
        move: "PULL-OUT",
        sourceInstruction: "CONTINUOUS PULL-OUT, exponential scale, 1.36 s; matches S37 motion vector.",
        sourceKind: "CODE3D",
        cameraOwner: "code",
        durationFrames: 41,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              12
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.125,
            pos: [
              0,
              0,
              15.562074655812115
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.25,
            pos: [
              0,
              0,
              20.18151396608915
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.375,
            pos: [
              0,
              0,
              26.172185583966183
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.5,
            pos: [
              0,
              0,
              33.941125496954285
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.625,
            pos: [
              0,
              0,
              44.01619407382422
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.75,
            pos: [
              0,
              0,
              57.08194152013061
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 0.875,
            pos: [
              0,
              0,
              74.02611961958115
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              96
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0,
          0,
          1,
          1
        ],
        filmstripQA: "pending-render",
        seed: 245
      },
      S39: {
        id: "S39",
        move: "FINAL-PUSH-HOLD",
        sourceInstruction: "Slow 2 % push-in. Hold the last 12 frames perfectly still.",
        sourceKind: "CODE",
        cameraOwner: "code",
        durationFrames: 52,
        fps: 30,
        worldSpace: "shot-local",
        keyframes: [
          {
            t: 0,
            pos: [
              0,
              0,
              10
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          },
          {
            t: 1,
            pos: [
              0,
              0,
              9.803921568627452
            ],
            target: [
              0,
              0,
              0
            ],
            fov: 50,
            roll: 0
          }
        ],
        ease: [
          0.42,
          0,
          0.58,
          1
        ],
        filmstripQA: "pending-render",
        seed: 246,
        holdLastFrames: 12,
        override: "Full compositor must also freeze all animation, text, grain, and cursor over final 12 frames."
      }
    }
  };

  // episodes/first-day-anime2/project/src/Film.tsx
  var Film = () => {
    const frame = (0, import_remotion2.useCurrentFrame)();
    const { width, height } = (0, import_remotion2.useVideoConfig)();
    const canvas = (0, import_react2.useRef)(null);
    const runtime = (0, import_react2.useRef)(null);
    const [boot] = (0, import_react2.useState)(() => (0, import_remotion2.delayRender)("Load production scene graph"));
    (0, import_react2.useEffect)(() => {
      let abandoned = false;
      runtime.current = (async () => {
        const response = await fetch((0, import_remotion2.staticFile)("helper/asset_map.json"));
        if (!response.ok) throw new Error("Production asset map unavailable");
        const assetMap = await response.json();
        assetMap.resolveURL = import_remotion2.staticFile;
        const wordmarkImage = await new Promise((resolve, reject) => {
          const im = new Image();
          im.onload = () => resolve(im);
          im.onerror = reject;
          im.src = (0, import_remotion2.staticFile)("assets/brand/anthropic-wordmark.svg");
        });
        const film = await createFilm({ THREE, SVGLoader: import_SVGLoader.SVGLoader, width, height, assetMap, shots: shots_default, sync: sync_default, onsets: onsets_default, cameraPaths: camera_paths_default, brand: { wordmarkImage } });
        if (abandoned) film.dispose();
        return film;
      })();
      runtime.current.then(() => (0, import_remotion2.continueRender)(boot)).catch(import_remotion2.cancelRender);
      return () => {
        abandoned = true;
        runtime.current?.then((film) => film.dispose()).catch(() => {
        });
      };
    }, [width, height, boot]);
    (0, import_react2.useEffect)(() => {
      let abandoned = false;
      const handle = (0, import_remotion2.delayRender)(`Compose source frame ${frame}`);
      (async () => {
        const film = await runtime.current;
        if (!film) throw new Error("Scene initialization missing");
        await film.renderFrame(frame);
        if (!abandoned) canvas.current?.getContext("2d")?.drawImage(film.canvas, 0, 0);
        (0, import_remotion2.continueRender)(handle);
      })().catch(import_remotion2.cancelRender);
      return () => {
        abandoned = true;
      };
    }, [frame, width, height]);
    return /* @__PURE__ */ import_react2.default.createElement(import_remotion2.AbsoluteFill, null, /* @__PURE__ */ import_react2.default.createElement("canvas", { ref: canvas, width, height }), /* @__PURE__ */ import_react2.default.createElement(import_remotion2.Audio, { src: (0, import_remotion2.staticFile)("first-day.mp3") }));
  };

  // episodes/first-day-anime2/project/src/Root.tsx
  var Root = () => /* @__PURE__ */ import_react3.default.createElement(import_react3.default.Fragment, null, /* @__PURE__ */ import_react3.default.createElement(import_remotion3.Composition, { id: "Film", component: Film, width: 1920, height: 1080, fps: sync.fps, durationInFrames: sync.frames }), /* @__PURE__ */ import_react3.default.createElement(import_remotion3.Composition, { id: "TimingCards", component: TimingCards, width: 1920, height: 1080, fps: sync.fps, durationInFrames: sync.frames }));

  // episodes/first-day-anime2/project/src/index.ts
  (0, import_remotion4.registerRoot)(Root);
})();
