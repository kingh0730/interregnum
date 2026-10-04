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
  var import_remotion3 = __require("remotion");

  // episodes/first-day-anime2/project/src/Root.tsx
  var import_react2 = __toESM(__require("react"), 1);
  var import_remotion2 = __require("remotion");

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

  // episodes/first-day-anime2/project/src/Root.tsx
  var Root = () => /* @__PURE__ */ import_react2.default.createElement(import_remotion2.Composition, { id: "TimingCards", component: TimingCards, width: 1920, height: 1080, fps: sync.fps, durationInFrames: sync.frames });

  // episodes/first-day-anime2/project/src/index.ts
  (0, import_remotion3.registerRoot)(Root);
})();
