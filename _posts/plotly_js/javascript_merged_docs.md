---
name: Stacked Histograms
suite: histogram
---
var x0 = Math.random() \* 500
var x1 = Math.random() \* 500 + 1
require('plotly')(username, api\_key);
var trace1 = {
x: x0,
type: "histogram"
};
var trace2 = {
x: x1,
type: "histogram"
};
var data = [trace1, trace2];
var layout = {barmode: "stack"};
var graphOptions = {layout: layout, filename: "stacked-histogram", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Horizontal Histogram
suite: histogram
---
var y = [];
for (var i = 0; i < 500; i ++) {
y[i] = Math.random();
}
require('plotly')(username, api\_key);
var data = [
{
y: y,
type: "histogram"
}
];
var graphOptions = {filename: "horizontal-histogram", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Histogram
suite: histogram
---
var x = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
}
require('plotly')(username, api\_key);
var data = [
{
x: x,
type: "histogram"
}
];
var graphOptions = {filename: "basic-histogram", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Colored and Styled Histograms
suite: histogram
---
var x0 = [];
var x1 = [];
for (var i = 0; i < 500; i ++) {
x0[i] = Math.random();
x1[i] = Math.random() + 1;
}
require('plotly')(username, api\_key);
var trace1 = {
x: x0,
histnorm: "count",
name: "control",
autobinx: false,
xbins: {
start: -3.2,
end: 2.8,
size: 0.2
},
marker: {
color: "fuchsia",
line: {
color: "grey",
width: 0
},
opacity: 0.75
},
type: "histogram"
};
var trace2 = {
x: x1,
name: "experimental",
autobinx: false,
xbins: {
start: -1.8,
end: 4.2,
size: 0.2
},
marker: {color: "rgb(255, 217, 102)"},
opacity: 0.75,
type: "histogram"
};
var data = [trace1, trace2];
var layout = {
title: "Sampled Results",
xaxis: {title: "Value"},
yaxis: {title: "Count"},
barmode: "overlay",
bargap: 0.25,
bargroupgap: 0.3
};
var graphOptions = {layout: layout, filename: "style-histogram", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Histograms
permalink: nodejs/histograms/
description: How to make a histogram in nodejs. Seven examples of colored, horizontal, and normal histogram bar charts.
thumbnail: thumbnail/histogram.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","histogram" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Overlaid Histogram
suite: histogram
---
var x0 = [];
var x1 = [];
for (var i = 0; i < 500; i ++) {
x0[i] = Math.random();
x1[i] = Math.random() + 1;
}
require('plotly')(username, api\_key);
var trace1 = {
x: x0,
opacity: 0.75,
type: "histogram"
};
var trace2 = {
x: x1,
opacity: 0.75,
type: "histogram"
};
var data = [trace1, trace2];
var layout = {barmode: "overlay"};
var graphOptions = {layout: layout, filename: "overlaid-histogram", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Public Graphs
suite: privacy
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 2, 4],
y: [0, 4, 2],
type: "scatter"
}
];
var graphOptions = {filename: "privacy-true", world\_readable: true, fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Public vs Private Graphs
permalink: nodejs/privacy/
description: How to set the privacy settings of plotly graphs in nodejs.
thumbnail: thumbnail/privacy.jpg
page\_type: example\_index
display\_as: file\_settings
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","privacy" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Private Graphs
suite: privacy
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 2, 4],
y: [0, 4, 2],
type: "scatter"
}
];
var graphOptions = {filename: "privacy-false", world\_readable: false, fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Multiple Axes
permalink: nodejs/multiple-axes/
description: How to make a graph with multiple axes in nodejs.
thumbnail: thumbnail/multiple-axes.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","multiple-axes" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Two Y-Axes
suite: multiple-axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [40, 50, 60],
name: "yaxis data",
type: "scatter"
};
var trace2 = {
x: [2, 3, 4],
y: [4, 5, 6],
name: "yaxis2 data",
yaxis: "y2",
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
title: "Double Y Axis Example",
yaxis: {title: "yaxis title"},
yaxis2: {
title: "yaxis2 title",
titlefont: {color: "rgb(148, 103, 189)"},
tickfont: {color: "rgb(148, 103, 189)"},
overlaying: "y",
side: "right"
}
};
var graphOptions = {layout: layout, filename: "multiple-axes-double", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Multiple Y-Axes
suite: multiple-axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
name: "yaxis1 data",
type: "scatter"
};
var trace2 = {
x: [2, 3, 4],
y: [40, 50, 60],
name: "yaxis2 data",
yaxis: "y2",
type: "scatter"
};
var trace3 = {
x: [4, 5, 6],
y: [40000, 50000, 60000],
name: "yaxis3 data",
yaxis: "y3",
type: "scatter"
};
var trace4 = {
x: [5, 6, 7],
y: [400000, 500000, 600000],
name: "yaxis4 data",
yaxis: "y4",
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: "multiple y-axes example",
width: 800,
xaxis: {domain: [0.3, 0.7]},
yaxis: {
title: "yaxis title",
titlefont: {color: "#1f77b4"},
tickfont: {color: "#1f77b4"}
},
yaxis2: {
title: "yaxis2 title",
titlefont: {color: "#ff7f0e"},
tickfont: {color: "#ff7f0e"},
anchor: "free",
overlaying: "y",
side: "left",
position: 0.15
},
yaxis3: {
title: "yaxis4 title",
titlefont: {color: "#d62728"},
tickfont: {color: "#d62728"},
anchor: "x",
overlaying: "y",
side: "right"
},
yaxis4: {
title: "yaxis5 title",
titlefont: {color: "#9467bd"},
tickfont: {color: "#9467bd"},
anchor: "free",
overlaying: "y",
side: "right",
position: 0.85
}
};
var graphOptions = {layout: layout, filename: "multiple-axes-multiple", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Contour Plot
suite: contour
---
var linspace = require('linspace');
var unpack = require('ndarray-unpack');
var zeros = require('zeros');
var fill = require('ndarray-fill');
var size = 100
var x = linspace(-2 \* Math.PI, 2 \* Math.PI, size)
var y = linspace(-2 \* Math.PI, 2 \* Math.PI, size)
var z = unpack(zeros([size,size]))
for (var i = 0; i < size; i++) {
for (var j = 0; j < size; j++) {
r2 = (x \* (i \* i) + y \* (j \* j))
z[i][j] = Math.sin(x \* i) \* Math.cos(y \* j) \* Math.sin(r2) / Math.log(r2+1)
}
}
require('plotly')(username, api\_key);
var data = [
{
z: z,
x: x,
y: y,
type: "contour"
}
];
var graphOptions = {filename: "simple-contour", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Contour Plots
permalink: nodejs/contour-plots/
description: How to make a contour plot in nodejs. Seven examples of contour plots of matrices with subplots, custom color-scales, and smoothing.
thumbnail: thumbnail/contour.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","contour" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 2D Histogram Contour Plot
with Histogram Subplots
suite: contour
---
var linspace = require('linspace');
var t = linspace(-1,1.2,2000);
var x = (Math.pow(t, 3)) + (0.3 \* (Math.random() \* 2000));
var y = (Math.pow(t, 6)) + (0.3 \* (Math.random() \* 2000));
require('plotly')(username, api\_key);
var trace1 = {
x: x,
y: y,
mode: "markers",
name: "points",
marker: {
color: "rgb(102,0,0)",
size: 2,
opacity: 0.4
},
type: "scatter"
};
var trace2 = {
x: x,
y: y,
name: "density",
ncontours: 20,
colorscale: "Hot",
reversescale: true,
showscale: false,
type: "histogram2dcontour"
};
var trace3 = {
x: x,
name: "x density",
marker: {color: "rgb(102,0,0)"},
yaxis: "y2",
type: "histogram"
};
var trace4 = {
y: y,
name: "y density",
marker: {color: "rgb(102,0,0)"},
xaxis: "x2",
type: "histogram"
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
showlegend: false,
autosize: false,
width: 600,
height: 550,
xaxis: {
domain: [0, 0.85],
showgrid: false,
zeroline: false
},
yaxis: {
domain: [0, 0.85],
showgrid: false,
zeroline: false
},
margin: {t: 50},
hovermode: "closest",
bargap: 0,
xaxis2: {
domain: [0.85, 1],
showgrid: false,
zeroline: false
},
yaxis2: {
domain: [0.85, 1],
showgrid: false,
zeroline: false
}
};
var graphOptions = {layout: layout, filename: "2dhistogram-contour-subplots", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: 3D Surface Plots
permalink: nodejs/3d-surface-plots/
description: How to make 3D surface plots in nodejs.
thumbnail: thumbnail/3d-surface.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","3d-surface" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Topographical 3D Surface Plot
suite: 3d-surface
---
require('plotly')(username, api\_key);
var data = [
{
z: [[27.80985, 49.61936, 83.08067, 116.6632, 130.414, 150.7206, 220.1871, 156.1536, 148.6416, 203.7845, 206.0386, 107.1618, 68.36975, 45.3359, 49.96142, 21.89279, 17.02552, 11.74317, 14.75226, 13.6671, 5.677561, 3.31234, 1.156517, -0.147662], [27.71966, 48.55022, 65.21374, 95.27666, 116.9964, 133.9056, 152.3412, 151.934, 160.1139, 179.5327, 147.6184, 170.3943, 121.8194, 52.58537, 33.08871, 38.40972, 44.24843, 69.5786, 4.019351, 3.050024, 3.039719, 2.996142, 2.967954, 1.999594], [30.4267, 33.47752, 44.80953, 62.47495, 77.43523, 104.2153, 102.7393, 137.0004, 186.0706, 219.3173, 181.7615, 120.9154, 143.1835, 82.40501, 48.47132, 74.71461, 60.0909, 7.073525, 6.089851, 6.53745, 6.666096, 7.306965, 5.73684, 3.625628], [16.66549, 30.1086, 39.96952, 44.12225, 59.57512, 77.56929, 106.8925, 166.5539, 175.2381, 185.2815, 154.5056, 83.0433, 62.61732, 62.33167, 60.55916, 55.92124, 15.17284, 8.248324, 36.68087, 61.93413, 20.26867, 68.58819, 46.49812, 0.2360095], [8.815617, 18.3516, 8.658275, 27.5859, 48.62691, 60.18013, 91.3286, 145.7109, 116.0653, 106.2662, 68.69447, 53.10596, 37.92797, 47.95942, 47.42691, 69.20731, 44.95468, 29.17197, 17.91674, 16.25515, 14.65559, 17.26048, 31.22245, 46.71704], [6.628881, 10.41339, 24.81939, 26.08952, 30.1605, 52.30802, 64.71007, 76.30823, 84.63686, 99.4324, 62.52132, 46.81647, 55.76606, 82.4099, 140.2647, 81.26501, 56.45756, 30.42164, 17.28782, 8.302431, 2.981626, 2.698536, 5.886086, 5.268358], [21.83975, 6.63927, 18.97085, 32.89204, 43.15014, 62.86014, 104.6657, 130.2294, 114.8494, 106.9873, 61.89647, 55.55682, 86.80986, 89.27802, 122.4221, 123.9698, 109.0952, 98.41956, 77.61374, 32.49031, 14.67344, 7.370775, 0.03711011, 0.6423392], [53.34303, 26.79797, 6.63927, 10.88787, 17.2044, 56.18116, 79.70141, 90.8453, 98.27675, 80.87243, 74.7931, 75.54661, 73.4373, 74.11694, 68.1749, 46.24076, 39.93857, 31.21653, 36.88335, 40.02525, 117.4297, 12.70328, 1.729771, 0], [25.66785, 63.05717, 22.1414, 17.074, 41.74483, 60.27227, 81.42432, 114.444, 102.3234, 101.7878, 111.031, 119.2309, 114.0777, 110.5296, 59.19355, 42.47175, 14.63598, 6.944074, 6.944075, 27.74936, 0, 0, 0.09449376, 0.07732264], [12.827, 69.20554, 46.76293, 13.96517, 33.88744, 61.82613, 84.74799, 121.122, 145.2741, 153.1797, 204.786, 227.9242, 236.3038, 228.3655, 79.34425, 25.93483, 6.944074, 6.944074, 6.944075, 7.553681, 0, 0, 0, 0], [0, 68.66396, 59.0435, 33.35762, 47.45282, 57.8355, 78.91689, 107.8275, 168.0053, 130.9597, 212.5541, 165.8122, 210.2429, 181.1713, 189.7617, 137.3378, 84.65395, 8.677168, 6.956576, 8.468093, 0, 0, 0, 0], [0, 95.17499, 80.03818, 59.89862, 39.58476, 50.28058, 63.81641, 80.61302, 66.37824, 198.7651, 244.3467, 294.2474, 264.3517, 176.4082, 60.21857, 77.41475, 53.16981, 56.16393, 6.949235, 7.531059, 3.780177, 0, 0, 0], [0, 134.9879, 130.3696, 96.86325, 75.70494, 58.86466, 57.20374, 55.18837, 78.128, 108.5582, 154.3774, 319.1686, 372.8826, 275.4655, 130.2632, 54.93822, 25.49719, 8.047439, 8.084393, 5.115252, 5.678269, 0, 0, 0], [0, 48.08919, 142.5558, 140.3777, 154.7261, 87.9361, 58.11092, 52.83869, 67.14822, 83.66798, 118.9242, 150.0681, 272.9709, 341.1366, 238.664, 190.2, 116.8943, 91.48672, 14.0157, 42.29277, 5.115252, 0, 0, 0], [0, 54.1941, 146.3839, 99.48143, 96.19411, 102.9473, 76.14089, 57.7844, 47.0402, 64.36799, 84.23767, 162.7181, 121.3275, 213.1646, 328.482, 285.4489, 283.8319, 212.815, 164.549, 92.29631, 7.244015, 1.167, 0, 0], [0, 6.919659, 195.1709, 132.5253, 135.2341, 89.85069, 89.45549, 60.29967, 50.33806, 39.17583, 59.06854, 74.52159, 84.93402, 187.1219, 123.9673, 103.7027, 128.986, 165.1283, 249.7054, 95.39966, 10.00284, 2.39255, 0, 0], [0, 21.73871, 123.1339, 176.7414, 158.2698, 137.235, 105.3089, 86.63255, 53.11591, 29.03865, 30.40539, 39.04902, 49.23405, 63.27853, 111.4215, 101.1956, 40.00962, 59.84565, 74.51253, 17.06316, 2.435141, 2.287471, -0.0003636982, 0], [0, 0, 62.04672, 136.3122, 201.7952, 168.1343, 95.2046, 58.90624, 46.94091, 49.27053, 37.10416, 17.97011, 30.93697, 33.39257, 44.03077, 55.64542, 78.22423, 14.42782, 9.954997, 7.768213, 13.0254, 21.73166, 2.156372, 0.5317867], [0, 0, 79.62993, 139.6978, 173.167, 192.8718, 196.3499, 144.6611, 106.5424, 57.16653, 41.16107, 32.12764, 13.8566, 10.91772, 12.07177, 22.38254, 24.72105, 6.803666, 4.200841, 16.46857, 15.70744, 33.96221, 7.575688, -0.04880907], [0, 0, 33.2664, 57.53643, 167.2241, 196.4833, 194.7966, 182.1884, 119.6961, 73.02113, 48.36549, 33.74652, 26.2379, 16.3578, 6.811293, 6.63927, 6.639271, 8.468093, 6.194273, 3.591233, 3.81486, 8.600739, 5.21889, 0], [0, 0, 29.77937, 54.97282, 144.7995, 207.4904, 165.3432, 171.4047, 174.9216, 100.2733, 61.46441, 50.19171, 26.08209, 17.18218, 8.468093, 6.63927, 6.334467, 6.334467, 5.666687, 4.272203, 0, 0, 0, 0], [0, 0, 31.409, 132.7418, 185.5796, 121.8299, 185.3841, 160.6566, 116.1478, 118.1078, 141.7946, 65.56351, 48.84066, 23.13864, 18.12932, 10.28531, 6.029663, 6.044627, 5.694764, 3.739085, 3.896037, 0, 0, 0], [0, 0, 19.58994, 42.30355, 96.26777, 187.1207, 179.6626, 221.3898, 154.2617, 142.1604, 148.5737, 67.17937, 40.69044, 39.74512, 26.10166, 14.48469, 8.65873, 3.896037, 3.571392, 3.896037, 3.896037, 3.896037, 1.077756, 0], [0.001229679, 3.008948, 5.909858, 33.50574, 104.3341, 152.2165, 198.1988, 191.841, 228.7349, 168.1041, 144.2759, 110.7436, 57.65214, 42.63504, 27.91891, 15.41052, 8.056102, 3.90283, 3.879774, 3.936718, 3.968634, 0.1236256, 3.985531, -0.1835741], [0, 5.626141, 7.676256, 63.16226, 45.99762, 79.56688, 227.311, 203.9287, 172.5618, 177.1462, 140.4554, 123.9905, 110.346, 65.12319, 34.31887, 24.5278, 9.561069, 3.334991, 5.590495, 5.487353, 5.909499, 5.868994, 5.833817, 3.568177]],
type: "surface"
}
];
var layout = {
title: "Mt Bruno Elevation",
autosize: false,
width: 500,
height: 500,
margin: {
l: 65,
r: 50,
b: 65,
t: 90
}
};
var graphOptions = {layout: layout, filename: "elevations-3d-surface", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Grouped Box Plot
suite: box
---
var x = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']
require('plotly')(username, api\_key);
var trace1 = {
y: [0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
x: x,
name: "kale",
marker: {color: "#3D9970"},
type: "box"
};
var trace2 = {
y: [0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
x: x,
name: "radishes",
marker: {color: "#FF4136"},
type: "box"
};
var trace3 = {
y: [0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
x: x,
name: "carrots",
marker: {color: "#FF851B"},
type: "box"
};
var data = [trace1, trace2, trace3];
var layout = {
yaxis: {
title: "normalized moisture",
zeroline: false
},
boxmode: "group"
};
var graphOptions = {layout: layout, filename: "box-grouped", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Box Plot
suite: box
---
for (var i = 0; i < 50; i ++) {
y0[i] = Math.random();
y1[i] = Math.random() + 1;
}
require('plotly')(username, api\_key);
var trace1 = {
y: y0,
type: "box"
};
var trace2 = {
y: y1,
type: "box"
};
var data = [trace1, trace2];
var graphOptions = {filename: "basic-box-plot", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Box Plots
permalink: nodejs/box-plots/
description: How to make a box plot in nodejs. Seven examples of box plots in nodejs that are grouped, colored, and display the underlying data distribution.
thumbnail: thumbnail/box.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","box" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Box Plot That Displays the Underlying Data
suite: box
---
require('plotly')(username, api\_key);
var data = [
{
y: [0, 1, 1, 2, 3, 5, 8, 13, 21],
boxpoints: "all",
jitter: 0.3,
pointpos: -1.8,
type: "box"
}
];
var graphOptions = {filename: "box-plot-jitter", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Inset Plots
permalink: nodejs/insets/
description: How to make an inset graph in nodejs.
thumbnail: thumbnail/insets.jpg
page\_type: example\_index
display\_as: basic
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","insets" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Simple Inset Graph
suite: insets
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [4, 3, 2],
type: "scatter"
};
var trace2 = {
x: [20, 30, 40],
y: [30, 40, 50],
xaxis: "x2",
yaxis: "y2",
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
yaxis2: {
domain: [0.6, 0.95],
anchor: "x2"
},
xaxis2: {
domain: [0.6, 0.95],
anchor: "y2"
}
};
var graphOptions = {layout: layout, filename: "simple-inset", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Adjusting Height, Width, and Margins
suite: sizing
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
}
];
var layout = {
autosize: false,
width: 500,
height: 500,
margin: {
l: 50,
r: 50,
b: 100,
t: 100,
pad: 4
},
paper\_bgcolor: "#7f7f7f",
plot\_bgcolor: "#c7c7c7"
};
var graphOptions = {layout: layout, filename: "size-margins", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Setting Graph Size
permalink: nodejs/setting-graph-size/
description: How to change the size of graphs in nodejs.
thumbnail: thumbnail/sizing.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","sizing" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Getting Started with Plotly
permalink: nodejs/getting-started/
description: Plotly's Node.js graphing library makes interactive, publication-quality graphs online. Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts and bubble charts.
---

# Getting started with Plotly for Nodejs

## Installation

To install Plotly's Node module, use **npm**.

```
npm install plotly
```

## Authentication

Fire up Node!

```
$ node
```

```
var plotly = require('plotly')("DemoAccount", "lr1c37zw81")
```

You'll need to replace `"DemoAccount"` and `"lr1c37zw81"` with your Plotly username and [API key](https://plotly.com/settings/api/).

[Find my API key.](https://plotly.com/settings/api/)

###### Special Instructions for [Chart Studio Enterprise](https://plotly.com/product/enterprise/) users

Your API key for account on the public cloud will be different than the API key in Chart Studio Enterprise. Visit <https://plotly.your-company.com/settings/api/> to find your Chart Studio Enterprise API key. Remember to replace "your-company.com" with the URL of your Chart Studio Enterprise server.

Instantiate your `plotly` object with the domain of your Chart Studio Enterprise server.

```
var plotly = require('plotly')({"username": "DemoAccount", "apiKey": "lr1c37zw81", "host": "plotly.your-company.com", "port": 443})
```

Remember to replace "your-company.com" with the URL of your Chart Studio Enterprise server. Questions? support@plot.ly

## Start plotting!

Copy and paste the following to create your first graph using the Plotly Node library! If all goes well, the URL for your graph will be printed in your console.

```

var data = [{x:[0,1,2], y:[3,2,1], type: 'bar'}];
var layout = {fileopt : "overwrite", filename : "simple-node-example"};

plotly.plot(data, layout, function (err, msg) {
	if (err) return console.log(err);
	console.log(msg);
});
```

[view examples](/nodejs/)
---
name: Get Requests
suite: get-requests
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4],
y: [16, 5, 11, 9],
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "get-requests-example", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Get Requests
permalink: nodejs/get-requests/
description: How to download plotly users's public graphs and data with nodejs.
thumbnail: thumbnail/get-requests.jpg
page\_type: example\_index
display\_as: get\_request
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","get-requests" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Colored and Styled Bar Chart
suite: bar
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
y: [219, 146, 112, 127, 124, 180, 236, 207, 236, 263, 350, 430, 474, 526, 488, 537, 500, 439],
name: "Rest of world",
marker: {color: "rgb(55, 83, 109)"},
type: "bar"
};
var trace2 = {
x: [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
y: [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270, 299, 340, 403, 549, 499],
name: "China",
marker: {color: "rgb(26, 118, 255)"},
type: "bar"
};
var data = [trace1, trace2];
var layout = {
title: "US Export of Plastic Scrap",
xaxis: {tickfont: {
size: 14,
color: "rgb(107, 107, 107)"
}},
yaxis: {
title: "USD (millions)",
titlefont: {
size: 16,
color: "rgb(107, 107, 107)"
},
tickfont: {
size: 14,
color: "rgb(107, 107, 107)"
}
},
legend: {
x: 0,
y: 1.0,
bgcolor: "rgba(255, 255, 255, 0)",
bordercolor: "rgba(255, 255, 255, 0)"
},
barmode: "group",
bargap: 0.15,
bargroupgap: 0.1
};
var graphOptions = {layout: layout, filename: "style-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Bar Chart with Hover Text
suite: bar
---
require('plotly')(username, api\_key);
var data = [
{
x: ["Liam", "Sophie", "Jacob", "Mia", "William", "Olivia"],
y: [8.0, 8.0, 12.0, 12.0, 13.0, 20.0],
text: ["4.17 below the mean", "4.17 below the mean", "0.17 below the mean", "0.17 below the mean", "0.83 above the mean", "7.83 above the mean"],
marker: {color: "rgb(142, 124, 195)"},
type: "bar"
}
];
var layout = {
title: "Number of graphs made this week",
font: {family: "Raleway, sans-serif"},
showlegend: false,
xaxis: {tickangle: -45},
yaxis: {
zeroline: false,
gridwidth: 2
},
bargap: 0.05
};
var graphOptions = {layout: layout, filename: "bar-with-hover-text", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Bar Charts
permalink: nodejs/bar-charts/
description: How to make a bar chart in nodejs. Seven examples of grouped, stacked, overlaid, and colored bar charts.
thumbnail: thumbnail/bar.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","bar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Customizing Individual Bar Colors
suite: bar
order: 10
---
require('plotly')(username, api\_key);
var data = [
{
x: [1, 2, 3, 4],
y: [5, 4, -3, 2],
marker: {color: ["#447adb", "#447adb", "#db5a44", "#447adb"]},
type: "bar"
}
];
var graphOptions = {filename: "bar-marker-array", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Stacked Bar Chart
suite: bar
---
require('plotly')(username, api\_key);
var trace1 = {
x: ["giraffes", "orangutans", "monkeys"],
y: [20, 14, 23],
name: "SF Zoo",
type: "bar"
};
var trace2 = {
x: ["giraffes", "orangutans", "monkeys"],
y: [12, 18, 29],
name: "LA Zoo",
type: "bar"
};
var data = [trace1, trace2];
var layout = {barmode: "stack"};
var graphOptions = {layout: layout, filename: "stacked-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Bar Chart
suite: bar
---
require('plotly')(username, api\_key);
var data = [
{
x: ["giraffes", "orangutans", "monkeys"],
y: [20, 14, 23],
type: "bar"
}
];
var graphOptions = {filename: "basic-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Grouped Bar Chart
suite: bar
---
require('plotly')(username, api\_key);
var trace1 = {
x: ["giraffes", "orangutans", "monkeys"],
y: [20, 14, 23],
name: "SF Zoo",
type: "bar"
};
var trace2 = {
x: ["giraffes", "orangutans", "monkeys"],
y: [12, 18, 29],
name: "LA Zoo",
type: "bar"
};
var data = [trace1, trace2];
var layout = {barmode: "group"};
var graphOptions = {layout: layout, filename: "grouped-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Horizontal Error Bars
suite: error-bar
---
require('plotly')(username, api\_key);
var data = [
{
x: [1, 2, 3, 4],
y: [2, 1, 3, 4],
error\_x: {
type: "percent",
value: 10
},
type: "scatter"
}
];
var graphOptions = {filename: "error-bar-horizontal", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Symmetric Error Bars
suite: error-bar
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 1, 2],
y: [6, 10, 2],
error\_y: {
type: "data",
array: [1, 2, 3],
visible: true
},
type: "scatter"
}
];
var graphOptions = {filename: "basic-error-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Bar Chart with Error Bars
suite: error-bar
---
require('plotly')(username, api\_key);
var trace1 = {
x: ["Trial 1", "Trial 2", "Trial 3"],
y: [3, 6, 4],
name: "Control",
error\_y: {
type: "data",
array: [1, 0.5, 1.5],
visible: true
},
type: "bar"
};
var trace2 = {
x: ["Trial 1", "Trial 2", "Trial 3"],
y: [4, 7, 3],
name: "Experimental",
error\_y: {
type: "data",
array: [0.5, 1, 2],
visible: true
},
type: "bar"
};
var data = [trace1, trace2];
var layout = {barmode: "group"};
var graphOptions = {layout: layout, filename: "error-bar-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Asymmetric Error Bars
suite: error-bar
---
require('plotly')(username, api\_key);
var data = [
{
x: [1, 2, 3, 4],
y: [2, 1, 3, 4],
error\_y: {
type: "data",
symmetric: false,
array: [0.1, 0.2, 0.1, 0.1],
arrayminus: [0.2, 0.4, 1, 0.2]
},
type: "scatter"
}
];
var graphOptions = {filename: "error-bar-asymmetric-array", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Error Bars
permalink: nodejs/error-bars/
description: How to add error bars to a line, scatter, or bar chart. Seven examples of symmetric, asymmetric, horizontal, and colored error bars.
thumbnail: thumbnail/error-bar.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","error-bar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Colored and Styled Error Bars
suite: error-bar
---
var linspace = require('linspace')
x\_theo = linspace(-4, 4, 100)
sincx = Math.sin(x\_theo) / x\_theo
var x = [-3.8, -3.03, -1.91, -1.46, -0.89, -0.24, -0.0, 0.41, 0.89, 1.01, 1.91, 2.28, 2.79, 3.56]
var y = [-0.02, 0.04, -0.01, -0.27, 0.36, 0.75, 1.03, 0.65, 0.28, 0.02, -0.11, 0.16, 0.04, -0.15]
require('plotly')(username, api\_key);
var trace1 = {
x: x\_theo,
y: sincx,
name: "sinc(x)",
type: "scatter"
};
var trace2 = {
x: x,
y: y,
mode: "markers",
name: "measured",
error\_y: {
type: "constant",
value: 0.1,
color: "#85144B",
thickness: 1.5,
width: 3,
opacity: 1
},
error\_x: {
type: "constant",
value: 0.2,
color: "#85144B",
thickness: 1.5,
width: 3,
opacity: 1
},
marker: {
color: "#85144B",
size: 8
},
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "error-bar-style", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Error Bars as a Percentage of the y-Value
suite: error-bar
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 1, 2],
y: [6, 10, 2],
error\_y: {
type: "percent",
value: 50,
visible: true
},
type: "scatter"
}
];
var graphOptions = {filename: "percent-error-bar", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Asymmetric Error Bars with a Constant Offset
suite: error-bar
---
require('plotly')(username, api\_key);
var data = [
{
x: [1, 2, 3, 4],
y: [2, 1, 3, 4],
error\_y: {
type: "percent",
symmetric: false,
value: 15,
valueminus: 25
},
type: "scatter"
}
];
var graphOptions = {filename: "error-bar-asymmetric-constant", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Global Font Properties
suite: font
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
}
];
var layout = {
title: "Global Font",
font: {
family: "Courier New, monospace",
size: 18,
color: "#7f7f7f"
}
};
var graphOptions = {layout: layout, filename: "global-font", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Text and Font Styling
permalink: nodejs/font/
description: How to edit and style the font of graphs in nodejs.
thumbnail: thumbnail/font.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","font" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Static Image Export
permalink: nodejs/static-image-export/
description: How to export plotly graphs as static images in nodejs. Plotly supports png, svg, jpg, and pdf image export.
thumbnail: thumbnail/static-image.jpg
page_type: example_index
display_as: get_request
---
<div class="content-box">
<p>These docs have moved!</p><br>

<p><a href="https://github.com/plotly/plotly-nodejs#plotlygetimagefigure-options-callback">Learn about image exporting Node.js on our GitHub docs.</a></p><br>
</div><br>

---
name: Logarithmic Axes
suite: log
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {
type: "log",
autorange: true
},
yaxis: {
type: "log",
autorange: true
}
};
var graphOptions = {layout: layout, filename: "plotly-log-axes", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Log Plots
permalink: nodejs/log-plot/
description: How to make a plot with logarithmic axes in nodejs.
thumbnail: thumbnail/log.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","log" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 3D Scatter Plot
suite: 3d-scatter
---
require('plotly')(username, api\_key);
var trace1 = {
x: [-0.858927762914, 0.759678101763, 1.6178351592, 1.87830282065, 0.809847170863, 0.268555760283, 2.30810416239, 0.282888011561, 1.75225768912, -0.0858584825427, -0.664926809221, -0.548288732801, 0.935236191463, -1.02421230779, 0.644847152488, 0.0793568349027, 0.376719868063, 0.462240513173, 0.973028103151, -0.114269985428, -0.033940830122, 0.811377010177, 0.173216762098, 1.13050378279, 0.553484661867, 0.440805181912, 0.148990837935, -0.493219257424, -0.40049507589, 0.624356936003, -1.34714271255, -1.33109047124, 0.580407752205, 1.31228189798, 1.16625104479, 0.372976659017, 0.33595979347, -0.791263889586, 2.95679346521, -1.44635853127, 0.802371733213, 2.69594639721, -1.80577115012, -0.585443782182, 1.74147234306, 0.0551660441537, 0.218995819792, 1.56944606413, -0.947713487167, 0.21531704968, 0.283274664607, -1.03433101051, 0.427567525355, -0.29651815918, 1.71666047058, -0.0124001672318, 1.25319441867, -0.94507428328, 3.09647680347, -0.287215190821, 1.45119951375, 1.69922212558, 2.69850672147, -0.0289175063451, 1.21716676273, 2.46646810578, -0.112577515009, 2.38520630018, -0.894226360843, 1.38400031789, -0.769002241532, 1.92561814496, -0.296718019513, -0.718227769059, 0.208753284183, 2.52782757368, 1.9361555668, -0.754003559785, 2.14063096306, 0.779847993597, 0.502973381133, 0.798184138778, -0.401231296439, -0.758368669985, 0.44767244853, -0.188431184199, 1.79497692012, -0.625306719407, -0.615724277639, -2.06735998972, 1.06474596869, -0.128866941481, -0.452517179795, 0.0200862867444, 0.421379325457, -1.0878312666, 3.09022738748, 0.0277330763081, -1.59553907708, 3.02447398417, 0.742938898095, -0.0669009525229, 1.11353510686, 0.349691325914, 1.27464565235, -0.849660878806, -0.718772836336, 1.4081636604, -0.753321894364, 2.51796096719, 0.623461242752, 2.47835521332, -1.53642964244, 0.159871420819, -0.395698796269, -1.11679091882, 0.448245168587, 1.55502024702, -0.343749743664, 0.724058499487, -0.686090692568, 1.32581077832, 1.25616394504, -0.484964890584, -0.460271614238, -0.841487231275, -1.36820594572, 0.90824794356, 0.67051351088, 0.0212121330424, -1.12267184074, 2.52453987516, 0.0849019587581, 1.7420758675, -1.0027007829, 1.9055764672, -2.14654088662, -1.52908707279, -0.640644116837, 1.67643856705, 2.25602889401, 1.83134219276, -1.72010278768, 2.74926371156, -1.74782046385, 2.00838277274, 2.77375902631, -0.809602500716, 0.444810361123, -0.862546878298, 1.9793213189, -0.0161110137557, -0.567182783683, -0.0148935369382, 1.29136015936, -0.447459511967, 2.01203302064, 3.65266094596, 3.51134603014, -2.60770981104, 2.24846069441, 0.966890489218, -0.880918847259, 1.56450901864, 3.23166864465, -1.18467635833, -1.64698877553, 1.0999706466, 1.37462800435, 0.0355155515869, 1.68461213782, 2.80665024521, 0.934728277386, 0.102742523087, -0.142481480764, -0.984400134993, 2.5408834026, -2.64514400656, 0.193597356785, -1.58222850849, 3.09908565915, 3.5367959438, 2.82880122941, 2.71306112901, 1.517531762, -1.60549123973, 2.06582826664, 0.415256545358, 0.802958397668, -1.83345209613, 2.89468274141, 1.08320823732, 1.10851585661, 2.35824916881, -0.0895465416277, 2.07564212248, -0.540300516929, -2.51315675561, 2.56087015306, -1.68477549995, 0.159617997414, -0.0096568387549, 2.38189315442, -1.77047179409, 0.823566144949, 2.19725973561, -2.30700971811, -2.68543507278, -2.09356427203, -1.62280421582, 3.5241757433, 0.982110745145, -1.44340169645, -3.1226208118, -1.79323527952, 2.37436121305, 1.41047281102, 3.94967038564, 0.890115902236, 1.29209752987, 0.157511695483, 2.03596315641, -0.239538147332, 0.667456763767, 1.46034222522, 1.42065240797, 2.40161812211, 2.81953536735, 3.1390491576, -0.809424460922, -0.613515342979, -2.37597124604, -0.102454450897, 1.10278080375, 1.35979036965, 1.43984057107, -1.32602471093, 0.232247238328, 2.22467629273, 1.32827158852, -0.592266211766, -2.2764609507, 0.377205738192, 0.353227718086, 1.93656584033, 1.9508653414, 1.38500252215, 2.73544615079, 1.1370189711, 1.87643818509, 0.935931377767, 0.147656457965, 0.707402783465, -2.27034360469, -0.21549529712, 1.84701270869, -1.59166018736, -0.0899279120141, -1.76780153178, 1.63174609695, -0.928495296123, 3.19960649446, 2.33011909541, 2.39706138327, 1.01785296718, 0.658242617297, 2.66337911939, -0.813082076212, -1.43347515326, -1.81743262746, -1.23249869238, 1.70358645138, 2.34830652544, -0.0312840792134, 0.556217873043, -2.09254676742, 2.20147446573, 2.26118757695, -0.13608553051, -1.17785812512, 3.00970271063, -2.38857976504, 1.60700925067, -0.31031752125, -0.0530433912159, -1.92633563006, -0.792793130711, 0.294658223896, -1.07807475309, 1.77597120332, 2.30471864914, 0.735157921792, 0.30693398648, 3.00091538111, -0.371353401071, -2.71001705707, -0.341155396452, 0.522613457871, -1.93085965936, 2.79478499215, -0.313871029869, 2.12051092648, 3.00141389588, -0.00535802781989, -2.0777556239, 0.717521153879, -1.96895226957, -0.123500384528, 3.82298949539, 2.64457625817, 0.851122568224, -0.433454261117, 1.32732171987, 2.92422971474, 1.60461821114, -1.57943427664, -0.471902204405, -1.71156258393, 3.66543091282, -0.79395254324, 2.77030702295, 3.92417977108, 0.178819511546, 0.627177838003, -0.107267457054, 1.03713811579, 0.852699587768, -0.710137602566, 2.59665240922, 3.51028489298, -0.0302576844334, -1.57247826785, -0.268406153014, -0.238958380149, 0.386329291232, 2.75650827998, 2.65374593439, 3.32308579008, 2.63394725262, -2.31611284957, 0.792368481101, 1.75250198315, -2.0863833566, -0.580824210252, -2.37313764374, 3.15809501972, 0.119166412194, -0.408202532592, -1.40792875754, 1.73369421215, 0.853135858155, 1.76013699958, -0.470156083617, 1.60540076601, 1.91131704998, 0.800832273894, 0.877989562347, 1.02142060122, 0.775024681003, -1.03816091377, -0.67240219194, -2.08830184156, 2.07126969944, 0.589118614708, -2.43246352324, -1.775012952, 0.338603801466, -1.36587825694, -1.01785435861, -0.251202362196, 0.240488465005, 3.37427125017, -0.427744032382, -0.0160438693411, -2.12360820093, -0.0136300160675, 1.6457583931, -0.398113568909, 2.53618579496, 1.99732502068, 3.03757893274, -1.542951805, 3.29032020554, 0.408597217183, -0.784512643074, 1.92727780511, 1.53237207726, -1.21123169572, -0.533099191238, -0.648573260417, -0.413723569224, 1.70961621052, -0.438637351355, 1.28189816388, -1.00815357379, -0.355421335745, 2.31287621579, 1.04410395208, 0.712592911641, -0.706727456723, -1.8960033809, 1.67320401337, 1.80477328126, -0.24666442478, -0.16108368822, -1.56370587204, 2.06107198416, -0.195931176216, 0.177288395826, -1.20729352235, 0.294135054063, 1.09730702538, 0.203291908383, -0.965609543176, 3.29553773891, -2.74479491047, -1.53148234693, 0.182945314599, 2.79105526804, 3.00847199565, 0.371686924352, -1.4676453197, -1.36196230158, -2.25640972442, -1.62081764515, 0.819163569299, -1.87813351684, 3.64231404007, -1.81342504306, -2.67452608479, -3.09528194535, -2.43224150927, 2.33231557534, 0.926829077971, -1.7157590476, -0.346085084905, -0.976704966679, 0.174122242602, -0.709571668723, -0.814946854616, -1.18937177368, 3.22661237692, 1.76487935387, 4.02168707708, 1.54253760561, 3.0684272825, 1.0766193676, 4.15039042142, -3.89394265607, -0.556788955049, 1.13104626799, -1.55159845843, -0.198247541327, -2.76365241834, -0.0437864059995, -1.1073471829, -2.22224941621, 2.18238487631, -1.88335356177, -1.44496819666, 1.15761562632, 0.601653653672, -1.52132522619, 3.72553746998, 3.34108341777, -1.76822827956, 2.77883375288, -1.83153667401, -1.99139499711, 1.97110727621, 3.61045236073, 1.78405333363, -3.07193793839, 3.59599391471, 2.86251718553, 0.756925211083, 3.43366242359, -0.713059647626, 3.34974067292, 1.06337642201, 0.0538352092257, -1.18727079658, -2.58573940196, 3.50750797235, -4.19551857748, 0.866834312384, 4.30363965594, 4.42541330197, 3.61456171231, -1.65607835843, 3.66914469514, -0.972301726054, 0.599171933545, 2.67894428534, 5.10664252733, -3.14997643882, 1.19941589947, -0.879386256104, -0.0259763360274, 4.09510806754, 3.43126239346, -1.18332293012, -3.11943368535, -0.643549187597, 0.123823429761, -2.77618764727, -2.08034348596, -1.12432451465, 0.799946742559, 0.638328163648, -1.29251792259, -2.0542306177, 3.22065702648, -2.46356134508, 3.37201979384, 2.50438240253, 3.97282056193, 2.71881280561, -2.9158864435, -3.28019303156, -3.10078035913, -0.734835442796, 0.959373739046, 1.1559574549, 2.39594583166, 3.13623943927, 3.37614503798, 2.75058031051, 1.50860950621, 1.46241227783, 3.45922400833, 4.72631615213, -3.43100652587, -1.72221955634, -0.975194108385, 4.20553757114, -2.62125819173, -1.13312733822, 1.88730868047, 1.6541632978, -2.59610704346, 1.15081366305, -1.03630719384, 3.45788622168, 0.639681868146, 2.82020884316, 2.37564446769, 3.27115765369, -1.26343773125, 1.45473962263, 0.00286176428154, 3.27535731623, -1.17140282966, 3.09924196837, 3.03267877809, 1.78511499261, -0.778420535471, -0.134379090833, 2.63877606224, 0.18277247683, -0.499556478565, 2.5813620685, 4.31823094167, 2.36684231859, 4.69734629954, 0.946046667237, 2.79465226142, 2.35736099073, 2.45848802124, 2.68120416047, 4.69362553102, 0.638104883716, 3.53346501409, -1.44606032139, -2.56104725937, 0.576801496142, 1.89699102685, -1.6347767405, -1.77764899257, -0.561879823945, 1.86177406036, 1.63059355365, 3.26898808078, 3.3389060153, -1.34368099274, -0.758128145199, -1.53955573605, -1.5992941923, 1.45428245865, 2.2232530871, 1.45384089708, -1.25036293191, 1.88168443914, 2.69946860476, -0.465826890784, 2.62221137577, 3.22855398135, 2.50436997995, 2.51680081341, 1.49805627454, 1.53685767869, -1.06190548994, 3.09158772759, 3.83825570337, 3.01739920313, 2.70321852027, -0.85718483251, 3.00647974554, -0.924208904843, 3.53032679291, 0.947653719512, 3.39073210706, -1.73332260474, -0.625987415303, 0.185971453854, 3.58225086672, 2.43555668298, 2.24681830569, 3.10745658206, -0.439852447281, 1.43443295631, -0.602383078451, 1.88437057044, 3.00661254036, 4.30151619719, 1.88411811149, 0.150312286689, -3.27525815778, 2.67269037181, -0.263319377466, -1.97676943299, 1.70079582215, 1.2141806404, 2.77435948268, -1.51565303988, 5.00882394354, 2.91914631481, 0.457616187688, -0.209673742902, 4.43503073188, 1.19247934425, -0.456937585971, -2.07779156963, 0.380014366574, -1.36371948682, 4.52062607666, -2.69784942812, -1.69672924589, 1.87215121045, 4.223311628, 0.410468836593, 3.79334797798, 3.24742241822, 4.01385774235, -1.90429254872, 1.42196218064, -0.0471062840955, 0.449089781812, -1.29162743202, 2.01299388237, -2.86555061708, 1.10082849539, 0.354190595237, 2.04126976047, -0.104602014704, 4.49224046065, 2.48638342595, 1.19547671213, 3.12986698547, 0.846866021451, -0.497774446696, 0.063062926305, -0.15960487312, 0.25714897901, 0.0292483892514, 3.09038076845, 3.51875485458, 0.327628239814, 4.7135527499, -2.57824908233, 1.73197959972, 2.68889806146, -2.86993925102, -2.97131945271, -1.24845796036, 2.74591831895, 1.93856886144, -0.046903689675, -2.5991560384, 0.386753042481, 2.90890220201, -3.597770169, -3.245774372, 3.14940672678, -2.14693412708, 1.87480014828, 2.20562206425, -2.43906562979, 4.73708106607, 0.0309644739696, 3.87143205026, 2.72726582774, 1.8514373677, 3.15180199391, 2.62604087016, -3.76009831969, -2.38328428959, -0.877221152294, -1.48383897363, 1.75965659589, 2.96591035733, 0.313303279724, -2.83574504618, 0.0800642694519, 3.89167665324, 1.3664003396, -1.71124623126, 3.56450068027, 2.4155653456, -1.43528702514, 3.22765930743, 2.38873811316, 2.02046011943, -1.19882933864, 2.6406229992, -3.2089185479, 2.95026663271, -3.63471156089, -0.649521388966, 1.6117139495, -2.72401626101, -1.96593960914, 2.95105213714, 3.64012858366, 1.54231069852, 3.73179413064, -3.34481308024, -2.22253695946, 1.99122616076, 0.353287297963, -2.79890068692, -1.57167851523, 3.07573913687, 3.4117374699, 0.610616324035, 2.83773059793, -2.19347305082, 0.397884857293, -0.974986607405, 3.24993538791, -0.940966176035, 4.80741215787, 2.82353674993, 4.71588788786, -3.12876280414, 1.43073266825, -0.203993415234, 0.28026234191, -1.55925520286, 4.9552108066, 0.352842398051, -2.49854848981, -0.132552008728, 3.34892003862, 3.05787364212, -1.63091690016, -0.184162785943, 2.68858103873, -1.01947817658, 1.0048399553, 5.22021824018, -0.39720547266, -1.06126498685, -1.9202336148, 0.811020545502, 3.20457894589, -1.33436117346, -1.98105017508, 2.15422964012, 0.451933250755, 4.34961179361, 3.26326396146, 1.17833104348, -3.51756161678, -0.288732549541, 0.893291484464, 3.30353990004, -2.5809991132, 4.09410011471, -1.98888457952, -4.05687907192, -1.18836640137, 1.305382615, 1.65696996364, 1.78966738959, 3.22097538395, 0.755757112515, -0.739925658487, -0.567695467429, 0.848485462153, 1.15101462962, -2.71239439449, 2.86664632354, 0.488249645374, 0.840652578165, -1.42297525428, -0.0755520122848, 5.17287437449, -0.553138434327, -2.64199082737, 0.180841391438, 2.4632414642, -0.232470420282, 4.97254523671, 0.0810415357898, -0.140018194457, 2.56562591725, 0.495424299718, 0.312675639707, 1.93012951594, -2.55568382821, 2.70514247648, -2.79877255855, 4.98854819708, 3.46584615796, -3.06454651661, -0.853701409499, -2.71091365291, -3.57037359194, 3.47088456285, 2.1418569755, -2.68047005472, 3.42043757672, -3.26604803727, 5.33485694131, -0.239895117086, 3.86668928799, 1.24405788081, 1.74723638513, 4.62206564375, -2.38010220025, 2.27356996649, -2.97287257056, -1.4089170725, 1.65998739322, -1.39009119576, 0.768328122511, -1.27493995859, 4.94251197134, 3.98512179771, -0.421039544483, -2.10169947094, 4.55426363574, -0.3367959076, -2.45387540477, 0.843639703699, 3.81233632447, -2.57883266647, -1.3074357814, -0.920415603475, 2.6887645862, -2.76330018616, -2.30186128816, -1.27577642285, -2.19398840759, -0.225242794663, -3.14661318937, 4.15105124753, 0.686238095301, -4.17498322472, -2.39059448319, 0.414929579683, 2.28813450043, 1.83083442469, 0.889450770708, 3.74095175878, -1.94875735935, -4.09874879026, -3.84327926312, 0.74483574938, 3.51170974605, -1.40472903196, 3.07073768303, 3.22055365466, 0.833381130627, 3.39980309861, -0.847013048474, 3.05119077118, -3.12787881198, -0.760331290229, 2.61407497301, -2.38893710234, -3.5566008536, 1.12853805186, -1.47864285073, -0.0767897548524, 4.39411971208, -1.68671668554, -2.66519872519, -2.91712822838, -3.96703065969, 0.488548858866, 2.1308958141, 4.40421079018, -2.54831394444, 2.23456494882, 0.334495725258, 3.99170719064, 0.376688898215, 3.05311987133, -2.261655463, 0.533432111175, -0.384993258895, 1.63706552778, -3.58766606769, -1.23545000999, -2.72899361933, 4.23120961538, -1.32779512678, 2.60724223257, -2.32247877958, 3.31602718913, 2.46547035899, 0.822486751233, -0.0912452696003, -1.14762193636, -2.03760232, -0.196450065178, -0.424021897756, 0.141686829758, -2.05886457452, 1.20232620207, 1.77289886522, 0.760238632869, -0.470403534897, 1.77288860806, -0.699140309353, 1.53081692396, -2.22262482935, 1.61991359828],
y: [0.121607854144, 1.67084933716, 0.671663712413, 0.985942302305, -0.115243084349, 1.33798679839, -0.179934882508, 0.540179686408, 0.21604728214, -0.0302080518868, 0.919135827055, -0.528565328027, 1.83941068702, 1.04539009448, -1.44498718643, 0.561038457617, 0.650872400394, 0.263067896694, -0.0170236540958, -1.08098614985, -1.35846617243, 0.448653432745, -1.21301578164, 0.941622525938, 1.18752171196, 1.07214906289, 0.219255727314, -0.239453747229, -0.988446275058, 0.133817727241, 1.65448647859, 1.27120897034, -1.08102680178, -0.419799996933, -0.447175179695, 0.118451435332, -0.0223066375921, -0.425602183962, -0.411493590312, -0.719385329248, 0.362414702244, 0.743830525207, 2.8060588424, -1.57681491722, 1.97829504919, -0.485791255905, -0.471516165045, -0.970200509502, 0.144654488986, -1.15546801186, -0.798790321471, 1.07185451408, -1.69763724423, -0.369829035766, -2.05203667702, -0.42144791923, 2.43864496915, -0.458928693116, 0.465013834345, 1.77172437663, -0.724872420252, 2.17648511143, -0.353001037496, 1.5056927257, 2.22417953478, 0.160718378447, 2.31296740201, -0.447060221904, -1.66314923766, 0.668404078716, 0.0834804524138, 0.134054278172, -1.64041151051, -0.0446653430143, -1.85302061002, -0.055267065248, 0.433094145689, 0.207978848661, -1.14878803813, -1.45781494301, -0.064439571961, -1.0163306583, 0.798775792381, 0.00880232461799, -0.211813436686, 1.82388983829, -1.16030310811, 0.810521891093, -2.16242603901, 1.1679034155, 1.9541641911, 0.652116107186, -0.834781733259, 0.415037109363, -0.778352628036, 2.44136516868, 0.657706277588, 1.62865475296, -0.238519154745, 0.151130784619, -1.68728669985, 1.97688496932, -1.47585838602, 0.860510349359, 0.896068671547, 0.920159889825, 1.89972094697, 2.56584041836, -0.688163345777, -0.178416173435, 0.177540044816, -1.83550919258, 0.884131037009, -1.1069093154, 2.49564687297, 2.41780844678, 1.6496380009, 0.0939622419912, 2.3674353785, -0.562816442402, -0.787860985582, 1.92558886265, 0.656021607091, -0.415843909164, -0.317129135628, 1.3631950381, -0.561539085395, 2.86731519479, 3.17567905078, -1.3687919662, -1.32323208155, 2.54590081887, 2.12704387311, 1.12044858175, 0.252462895574, 1.94890491532, 1.57490305238, -0.0473029127911, 1.77634018005, 0.128497826721, -1.88517818924, -0.717504553502, 1.28840309825, 0.383652831292, 2.25590690211, 0.93223429849, -0.0341076218033, -1.01054577672, 1.50987358635, 0.746585134349, 0.307968671762, 1.23058758593, 1.9692652804, 0.248744359861, -1.2084380369, -0.225550866237, -1.5861365356, 2.16296568286, 2.03894981964, -0.895558123918, 1.15146418484, 2.64278967201, 1.35264518502, 1.18194665116, 0.53094746942, 3.01937676225, 1.68529523835, 1.33819808265, -2.8331143038, -2.57705116854, 2.32021306219, 0.175279649202, -0.356185819119, -1.9591778066, 1.13065086752, -1.56935798452, 3.1670421582, 1.61896699201, 1.09263462668, 0.0482791434793, -0.350494810271, 0.0014084887222, -0.742278663661, -2.17862596787, -2.62161932028, 3.11618531322, 2.37950117147, -0.718568795178, -1.29239491705, 1.90269085083, 0.12419299627, 3.1817054745, -1.79084188798, -0.00462248910356, -0.292003601142, -2.33411285703, 1.8311289033, -0.659019026481, -3.06465418494, -1.72699833877, 0.623895997609, 0.964604682688, -1.17267297316, 1.36606191851, -2.5124610889, -2.24661973089, 0.103155493127, -0.706910194866, 0.919144647415, -1.32474679696, 1.33655407411, -1.80523805391, -1.88725081372, -0.924335768255, 2.79661974102, -3.21111800615, -1.88948492699, 0.304624750915, 3.71094541791, -2.00950950061, -0.569909561044, 1.15500957578, -1.79929518892, 2.48204111604, 2.26863592193, -0.973650233129, 1.952552287, -2.29577767969, 0.54210133198, 1.11547757976, -0.696655045387, 2.06145649187, -2.46119701793, 3.80634954725, -1.07600155641, 0.438317176631, -2.66662681909, 0.873893505871, 1.88148221713, -1.68666320243, -2.93082701082, -0.66587836813, -0.379505158541, 0.923318537067, 2.29127874359, 0.143183237746, 1.5905466156, -0.899888623163, 2.05130329338, -0.671698081452, -1.68016137097, -3.23663705689, 3.46482661893, -0.197924380248, 2.48635224049, -1.27706830948, -1.28252313085, -0.471692805744, 2.41892543964, 2.65313689305, 3.03822264522, 2.7242866612, -0.714929697407, 3.33362854335, -2.30934959692, -1.83310803594, 0.765825046604, 1.86259136352, 1.84340126199, 0.066928876837, 2.58835725059, 0.190521212875, 2.10942396499, 1.91229271706, 1.19828956083, 1.24679013862, 0.611546344321, 2.34548242529, 0.995190558349, 1.96577773161, -2.08974327291, 2.07238661862, 2.91018803325, 0.364974818825, -0.983223879366, 2.05418544356, 2.56109756947, -1.70757036807, 3.15973882953, -2.45912545626, -0.224478489789, -2.44498720845, -1.44215962978, 0.78959450184, 2.53080365101, -0.363200536383, -2.0753814119, -1.91070443665, 2.73339279506, 2.46060731393, 2.86090597158, -1.84630750687, 0.903615083582, -1.40826192436, 0.549334826511, -1.65220301956, -1.29777869193, -1.08696456287, 1.82185920613, 1.81559912519, 3.18556676071, 3.43458671581, 2.5690208932, -0.962265759914, 0.763622195497, -0.617644824792, -2.65494681174, 2.38536559688, -1.55543225673, 3.5992319811, -1.03227842968, 1.50274924648, -2.32315771578, 1.96034349421, -1.00897889333, -1.47073716306, -1.98275657497, 0.691212401727, 0.34270071436, -1.05852250263, 1.62763182045, -0.70047452051, -0.64995078965, 0.907541495228, -3.08961344428, -0.957046919508, -1.63436385841, 1.37542935641, 2.13160573026, 2.09713579492, -0.178963130461, 3.7808023883, -1.69045693671, -1.81839436406, -1.89257982843, -0.335618158888, 2.87002044082, 2.78471161827, -0.351428520244, -1.35791203113, -2.14537756089, -1.19683659192, -1.63746796568, 2.74364053422, 1.03484792337, 2.18180306044, 0.103485002054, 3.82422430167, 1.00929131385, 3.49727764311, 4.28613749522, -0.817613992786, -0.880418143716, 3.85273647076, -0.00618117695497, -1.1888154935, 1.73515143721, 3.34958074347, 1.1879464924, -1.71189363197, -2.54022218359, -0.13431048668, -1.52101048407, -1.58730504014, 1.24472758876, -0.338289617649, -0.874442018513, 2.07223932264, 1.72051207809, -2.12536681066, 0.295206108648, 0.293117689872, -1.06857498222, 2.19877611094, -1.81418769029, 0.285760393454, 3.27697504568, 0.666653546717, 2.66071291844, 0.695046743423, -0.789747986515, 0.547695081954, -0.639106617318, 1.66996189547, -0.629234432994, -0.23834034469, 2.15542769909, -2.53070914088, -2.02262128572, -2.57856825145, 1.41017653116, -0.773581576526, 1.22098816689, -1.58524778003, 2.73188138203, 0.831344514018, -0.584843587996, -1.29173408505, 3.49757369264, 2.10743762122, 0.602034298414, 0.314697478713, -0.400916910382, -2.70485284498, 0.439331098993, 0.807039541332, -1.39485511653, -0.524608002137, 3.03590359965, 0.0093547861141, -1.49087213401, -0.361708387287, 2.24556831163, 1.32734504569, 0.983899591459, -2.77267035972, -2.49144692929, -0.999979895567, -0.138972802474, -0.258032068016, 1.32169276629, 0.262406415489, 0.948879731237, -1.3906201365, -0.74762566112, -2.79167189741, -0.993087136886, -0.902882610722, 4.03671196038, 0.375339630687, 3.23270001679, 3.2220328974, -1.65049579195, 2.71718050756, -2.84561345561, 2.24437960675, 1.92110887802, -0.135949482463, 0.969329080061, 3.40310909301, 2.27056309586, 0.287019140639, -3.92371251739, -0.613027649653, 4.63530437357, -3.03691654758, 3.7290773576, 3.32652482933, 2.19424902473, 3.34983950668, 0.362817105536, 0.937644553495, 3.27851469419, -0.753358489457, -0.727707123599, -1.82244545634, 1.88706752142, 0.4973006872, -2.4282196345, -3.57722926778, -0.894645900311, 2.86251747702, 2.7669723099, 2.66070031333, 2.99494562263, 3.58284381583, -2.44132359243, -1.60823244437, 4.20987914726, -3.1306850209, -1.97107428152, -0.932311705628, 2.73009698728, 1.59870247997, 0.19311438639, -3.77549186608, 0.648456103525, 0.19512704998, -1.52111388192, 1.85768194125, 2.26564997362, 4.88431193817, -3.3106544245, 2.62459772853, 0.069296213103, -2.06085193189, 2.18708474125, -2.43226165837, 2.95059187962, 1.6460456297, 3.51819671076, 3.72943541849, 2.86285798827, 3.23625293425, -2.16838870657, 0.45327716894, 2.88747261513, -3.04184428594, -1.42037816925, 2.48466476347, 0.507623391179, -0.319005680045, -2.38903579485, 2.70985012877, -1.97937944782, 2.88348295059, 2.56273024991, 0.695070536066, 0.303954419046, -1.74464617628, 0.67091254462, 2.80163249281, -2.19841138132, 1.38679057717, -3.92173917478, -0.558198708566, 2.12103973008, 4.33330137606, 1.46791551249, -0.753515998053, -1.01264727217, 1.44487408365, -0.622023210952, 3.6554034387, -2.46987845989, 2.90565474881, 1.64405216979, -0.544825497445, 3.31155737483, 0.0169021173894, -0.276520606989, 0.846162518059, -3.34829191959, -0.628786779293, 1.95080928741, -1.57551180474, -2.05251867595, 1.67514739912, 2.58462562798, -2.0558097119, -1.64641872793, 2.87672578958, -1.77128152813, 2.43068052395, 1.22266020633, 3.87716255777, 2.64604125185, 4.87667907736, -0.504560787152, -4.24451984003, 1.08596790207, 1.4620580663, 0.0820969928967, -0.0275864508729, 2.74256756408, 1.31098950432, -3.38661928623, 3.04282516092, 3.15222031252, 0.938879155635, -0.6335720686, -0.621117028802, -0.525375647076, -0.558126656454, 2.09189005781, -2.62306311351, 4.54944655202, 2.57757848221, 0.683620641343, 3.77784520018, 2.44466027538, 3.85192842572, -1.20363077732, -0.031170467206, 2.91170643197, -1.5297903712, 0.47102647727, 3.0499989123, -0.64708758323, 3.55171960681, -1.46289714211, -2.25888931902, -0.298758088429, -0.872198140117, 3.79007745699, 3.18920633663, 3.19376269711, 1.02108062855, -2.45049413694, 4.04590997874, 2.85071526397, 2.76251046217, 1.03634488219, 1.57933287976, 3.73012130127, 2.46094137504, 2.25734240088, -0.831436705632, -0.729740367769, -0.927130321135, -4.22337915816, 3.88814647998, 2.29541764351, -0.388799340839, 2.84351797784, 3.64596708004, 1.45411725279, 0.729678778858, 3.91079356251, -3.00241658157, 3.95021606505, -3.34657532873, -2.51463115457, 3.15002744496, 0.45889369707, -0.525120024936, 4.7048517062, -1.4432624123, -0.148889600414, 2.85939190951, 4.85780195185, -4.17511071059, 3.38411400271, 1.1075676825, 3.26237689907, 0.878111925584, -1.41552344964, -3.08270987167, 4.27867965084, 0.410610098969, -2.39902329281, 3.19205750317, 1.32299783959, 3.45666991208, -1.83125735979, 0.099271997232, -0.806466305994, -0.766210518842, 4.77198806046, 1.30314573108, -3.48272099798, 1.5335374746, 0.289421719969, 0.804861901663, 2.00252924034, 3.13152099914, 4.83297593915, 1.44038424807, 3.30941865486, -3.87367098374, 2.70339219681, 2.22028008944, 4.22295753737, 0.534301786928, 1.37133154995, -1.2036954636, 0.483074819481, 4.28027976877, 0.572397285073, 4.58383664771, 3.35540744581, 1.79749541626, -1.4991794488, -3.09687473587, 0.807227312823, 1.5062322928, 2.40325240992, 1.14547800212, 0.0466001419489, 3.237473284, -2.06181068528, 0.0403678177779, -2.69559776458, -2.04781416022, 1.18762584977, -1.97106128261, -2.24423610216, 3.49291188911, -0.275531621896, 4.0838136761, 1.58879039841, -0.775837025422, -0.794811987219, -0.517636225882, 0.511060173337, 0.93516735872, -0.0990338703974, 1.19890835086, 1.41309766327, -3.97061024016, 0.0898869027245, -1.04147456174, -2.39853783716, 1.98072633203, -2.6897612745, 2.06860375824, 3.71613764059, -2.78091622317, -1.96246989454, 4.88462462942, -2.45747094755, -3.91528037882, 2.11465423656, -2.07248473641, -0.53221327981, 3.98671332582, 4.82734673233, 4.66633570953, -1.68118224522, -0.457808793946, 1.51059520262, -1.98686969621, -1.61383725104, 4.0353200723, 0.802342231662, -2.95394558654, -0.0449895867233, 0.459878001801, 3.66990855098, -3.08437410064, 1.02121946308, -2.19449096315, 2.51305522906, 0.707811391663, -1.35871775798, 4.54906223313, 1.20460936587, 4.07379796852, 1.7235968393, 1.56533250359, 2.18814303658, 2.45487961784, -0.575724606107, 2.96545054235, -3.67099884214, 2.51242739647, -3.03943805729, 4.26374450536, 2.52120581706, -0.446953220829, 2.74594656254, -1.08293970514, 1.63654780736, -0.809812659437, 1.84476846452, -2.79219306354, -3.26053483042, 3.47432677713, -1.2224782126, -1.0892799674, -2.491241097, 1.7183533287, -2.98126449713, -0.872857817996, 0.792367206197, 2.7369490873, 4.37658292646, 1.34983597988, 3.06321911481, 4.36159802641, 0.151298090907, -0.583547405996, 3.32520204194, 3.94157059584, -0.566033708164, 1.70987813843, 4.04046420835, 4.40178151817, 2.47645649564, 3.22617204062, 2.55300433663, -1.14876824354, 1.24099402005, -0.501838007371, -2.15117053508, 1.37046375286, -0.394539839471, 3.47078760836, 1.68510598522, 1.46665432482, -1.66759281879, 3.14813284502, -2.69651205193, 3.22185336291, 1.86009959765, -2.37130457724, -3.739422063, 3.34909140766, 3.73453462414, 2.21246314169, -2.3418258197, -2.49216835089, 3.59744160687, -0.218876979998, 1.05607698819, 1.90898929982, -1.06501287706, 1.73034273392, 3.17206464858, 0.548205011961, 3.53892331784, 2.96362034509, -1.49124343255, 1.41607917491, 1.54911376141, 3.00313909702, -2.31995443697, 4.071719803, 3.58259723555, 2.35198746539, 1.65145143655, -0.548535047384, -0.254091263446, -0.0720228196517, 1.29201223324, -0.0838480553573, 0.343210130505, -3.01255059507, -2.05562878556, -1.53259999404, -2.15692124072, 0.769769077393, 1.71456813051, 1.29163122718, 0.301343421628, 4.24309644164, 0.335769114692, -4.30616929733, 1.31560783864, 1.05766080757, -0.37508205115, 1.48606207225, -0.355299585784, -2.31251305215, 0.346650567467, 0.748478884534, 0.594598301046, -2.73527603644, -1.4407262667, -0.717418442303, -2.03042015581, 3.72959178971, -0.168629385404, 1.67695866427, -1.50951330707, -3.54411000166, 2.29796061702, -0.0814058504927, -1.37135620095, -0.671215916855, -1.34090093101, -0.493347300277, 1.05428488077, -0.400449287458, 3.68584786982, 0.77527866322, 2.54592679455, 0.743377350722, 4.83908723893, 1.15485643352, 2.82969262574, -3.16438123743, -2.61651584047, -3.39350598009, -2.16905660938, 2.48992274585, 3.15640932997, 2.13230359296, 0.693529521205, 3.94717131009, 0.6734715982, 0.0225067418109, -0.261518256972, 3.40041873479, 2.34424102281, 2.8342932616, 0.918540278944, 3.98005402422, -0.385692323103, -2.4602077064, -2.33847358675, 2.94436912602, -1.65625728757, 0.5925775848, -1.35320802106, 0.11954012745, -0.0289756364643, 3.72075823961, 0.376181733787, 3.02085783287, 2.30504581286, 0.40908892533, -3.25940588031, 2.54793312026, -0.914592624221, 3.0192954182, 5.33497496733, -0.351297413737, 4.12697161654, 0.898976282488, 2.25027996096, 2.50367000659, -0.538810085533, 3.50181395434, -0.193121531684, -3.38428133063, -2.93081554241, -1.88367363938, 4.80643294125, 0.215757649249, 0.634013225995, -0.635834474133, -1.46403780153, -3.0931203374, -3.74503199648, 1.23037569327, 3.11931414173, 0.705759216663, -3.45954184381, -2.46630377667, -3.41246174104, -2.46898758813, -1.78950443066, -1.80116629275, -0.870152865968, -0.353916491529, 2.83889679237, -0.828160399074, -0.722566038156, -3.13706894078],
z: [-0.0678156933388, 0.389506443363, 0.676541754404, 1.75657907672, -0.958695112654, 0.225931050084, -0.23357228432, -1.33222052754, 0.162127715405, -0.210695836441, 0.00243653681466, -0.801092913329, 0.0206282397949, 0.204366050782, 0.505718797501, 0.325802711625, -0.416340063844, 0.36065197589, 0.107801293861, 0.552783953522, 1.82133354725, -0.69883818517, -0.213115797791, 1.43330313383, -0.344003528037, 1.1156507032, 1.77593503521, 0.558619347352, 0.862122886939, 0.897810621164, 1.45440281373, -1.0706190343, 1.31692285243, -1.3261700212, 0.922215687168, 2.50946592048, -1.94369276491, 2.61258200886, -0.791526109635, 1.64217000504, -0.400760791538, -0.573741315769, -0.323618444674, -0.315321944337, 1.51073967987, -0.179071893477, 2.34244915564, 0.373867515259, 1.74822285426, 0.639409013862, 2.70923555876, -0.68348860724, 1.45698446097, 2.83914020175, 1.33604407133, 0.382758415808, 0.268927845133, 0.040472439349, 1.15819311468, -0.256698470962, -0.216776394446, 0.536207606273, 1.33042276241, 2.07028190105, -1.3907338399, 2.95329363383, -1.93994516023, -0.00397342728079, 0.886561343035, 1.18128852906, -1.26208589704, -1.44212442313, -1.80275003038, 1.08303283603, -0.856671487814, 0.49763381133, -1.1435822743, -1.76018384946, 0.969835721382, -0.0611391938563, -1.5751116183, 0.327935337024, 0.881562067938, 1.19007653035, -1.36859674662, 0.0550245739563, 1.42790584536, 1.83541192886, 0.356235763069, 2.215492038, 0.0197273411395, 1.50596577113, -1.11307083167, 2.14340450961, -2.15135041067, -0.575629455865, -0.580296232071, 1.09139450776, 0.910539344661, 0.849165190864, 0.712024525326, 1.74458727306, -0.376670143764, 2.12774441052, 1.25902628443, 1.96137215065, 1.59232737139, 2.46776383326, -0.470267944228, -0.0420247515189, -2.33860020594, 1.04898989032, 2.66131540691, 0.964508657078, 0.640364947829, 2.81671920669, 0.228965305651, 0.977810768387, 0.648937850805, 1.42379219483, 1.37063757285, -0.364044667508, -1.48289276143, 0.142711520334, 1.61852783266, 2.17866013132, 0.14603504759, -0.0631542222059, 0.519163280739, 0.241676404038, -1.23061560622, 1.39614063053, -0.717190093023, 1.97253826617, 1.02785413929, 0.403816927353, 1.10124799809, -0.682081764104, 1.28998559241, 1.82507474914, 0.0986393148958, -0.691923144587, 0.201204242022, -0.499332157783, 0.560136841975, -0.223643441699, -0.196720228032, -0.948232706486, -1.33285338983, -1.66157649284, -1.30311720441, -1.78366142227, 2.2026224712, 1.36783985749, 3.16245801452, -0.266965175783, 0.34347070342, 1.21182471624, -1.43987322431, 0.74817709599, -2.00939217668, 2.70419763669, 3.48207273145, 3.84477658672, 1.7063355625, 2.04972933748, 2.27978791307, 2.59221337832, 1.22829138233, 0.933221491179, 0.130104932987, -0.127068551273, -2.76199935898, -1.02100865006, -1.93048525627, -0.335444821641, 1.40217502013, 0.917588018304, 3.77446534821, -2.75029434993, 1.44667696708, 2.22531898977, -0.303234935883, -0.155944414371, 0.528021431169, 1.87200977173, 0.866548842736, -1.84801350652, 2.31613440949, 0.465953027775, -2.53929928222, 0.25916239168, 0.715408898367, -1.23047468594, -2.24942467666, 0.767909097148, 2.50946723049, 0.387129074288, 1.47997046012, -1.03768279411, -1.44197964433, 3.82185948617, -0.114533427767, 1.27446428588, 0.608939105049, 3.19097824554, 0.875760186089, 1.92629122812, 1.32966170988, 0.937874276181, -0.792447292472, -0.46977703339, 0.0686468886357, 0.408603609919, -0.658831793703, -0.734306432194, -1.75301813374, 0.266550336491, -0.27684900001, -0.191212276828, -2.34117882393, -2.15242766385, -1.54653797884, 3.84553905962, 2.08599671966, 3.00729547017, 3.5774590399, -0.19874079787, 0.697446528747, -1.16950236297, 3.21609077322, 2.53139212168, 1.45182298666, 0.995666407988, 3.0361944844, 2.74041919033, 0.756706819438, -2.211630423, -0.653313713137, -0.0304431803377, -0.794711004577, 0.375850548562, 3.63517279183, -1.34157767787, -1.44171229518, -1.5545707959, 2.56165728815, 1.6279936452, 1.85822954379, 0.408233853776, -0.646241390048, -0.0531126460193, -1.37075547457, 2.04966683661, 3.16181631327, 3.0700288637, -0.740254692607, 3.00649340558, -0.603787139091, 3.17211164435, 0.628077398657, 1.55675012643, 1.61526325835, 1.98964981009, 2.72778268587, 1.73312561777, -0.681740040163, 0.229635825173, 0.923434549033, -2.34405767419, -0.169212790524, 1.94306331913, 2.5981827883, 3.66001764357, -2.2716698752, -0.839082021301, -2.62328718215, 0.503850036422, 3.43782971029, -2.12132595082, 0.564199829748, -0.893512504445, -0.692312083565, 2.59788309822, -0.584187175611, -0.60567343255, 2.8269365135, 1.89429907029, 0.163702167057, 0.71122495196, 1.35877165059, 1.136846562, 3.37618315627, 2.19980280667, -0.666510703829, 0.711495958413, 2.39975911217, -0.965113354465, 2.22509506011, 0.0355714373887, -0.132299903473, -1.77896389972, -1.88011570566, -0.19932430691, 0.783817006614, 1.72971871031, 0.0811703405591, 1.5258468201, -0.750610793311, -0.598137776729, -2.29914603602, 2.43546216684, -1.52607050317, 1.74265955987, 2.52172370838, 1.25546693783, 1.7919417213, -0.147737107418, 0.795017782057, -1.13914687568, -0.630750762671, 0.784065882403, 3.08316080051, 2.58398206364, 2.35398670741, -2.64861868993, -1.86900216685, -2.4697218512, -0.715714019709, 0.364783445032, -1.95904925541, 1.42756871284, 2.95760269788, -1.93078537539, 0.764396537487, 0.307613048262, 1.32062201288, -0.366908672366, 0.866184736245, -1.96438902223, -2.87848586483, 0.162411450457, 1.92024908831, -0.503546545732, 1.93985297774, -0.799872824456, -2.16387068916, -1.8099835158, -0.973908378423, -2.63363147532, -1.22857241159, -1.89862731312, 0.2543086369, -0.342448177704, -1.7579361628, 3.61374222978, 3.20934544556, 1.07738043812, -2.51593400105, 0.849715266525, 0.773691227828, -1.50358425535, -0.918872554278, -0.742950398971, 0.898635887653, 0.089779915105, -2.93874966089, 2.0373550593, 1.54731132248, -0.477379498792, 2.10288829771, 3.02960439119, 2.8983977824, 1.21374030653, 2.75874236463, 3.03213840119, -0.235924139803, 0.740112349256, -0.559909142188, 0.576554737429, 3.5287858832, 3.24656497547, -2.17957052259, -2.99528808705, 1.20652069452, -1.23107805698, -1.06455780677, -0.849854041675, 2.5494122293, -1.82309660181, -0.410040361511, 3.67067068592, -2.48094429039, -1.11111926248, -0.456153228809, 4.2169195184, -1.49841773885, 0.303258482863, 2.70312704981, 0.513099531339, 1.15081315307, -1.57029023233, 2.90742250763, 0.547647451094, -0.361635918134, 3.36576249843, 3.39503287102, 1.11922190341, -0.679266134742, -0.735540482101, 2.92758679746, -1.89638366855, 2.72718629016, 1.04045913931, 3.85413170839, -0.695988964989, -0.616120716915, -1.47014732824, 1.40986003016, 3.26924568907, -0.668068810201, 1.75041668626, -1.4558189543, 1.426388034, -2.61424583843, -0.409513507358, -0.430722250168, -0.517725635541, -0.397573918277, -0.00962290113808, 0.113716658665, 0.47695688666, -1.56139756444, -1.18801954994, -0.159974702874, 2.23202469625, -0.565234704555, -1.83986067729, -1.39722131127, -3.36355399183, -0.853666826698, 1.3211401532, -2.78630034031, -0.191576557235, 1.30270578849, -2.292606358, 3.40593447726, 1.22944766403, 1.68663427483, -1.06920414503, -4.0787418978, 3.58512855486, -0.361994135068, -2.25103445576, 0.7090346251, -0.853629724549, -1.05932209419, 0.95966569225, -1.66359827085, 2.43184638388, -3.15651388923, 4.88404518615, 0.256060402219, 1.11140536922, -2.65604902335, 3.20490267618, 3.48608349544, -1.75898220162, -1.96526576117, 1.08666296042, -3.25385666521, -2.6649353445, 2.8403497235, 2.69822812483, 0.445111614904, 2.11334720218, -1.11935049459, 3.62719369087, 1.41957672975, 2.77653773711, 2.46873902969, -2.29018238168, -0.938910283863, -2.9528059016, -0.983535231245, 0.92856369087, -0.891434174232, -1.64265403957, 0.131046234934, 1.55404832104, -2.3966642404, 3.16492807319, 2.80650086797, -1.75511689333, 0.550110818643, -0.351897927821, 4.91139760073, 2.94557627659, 4.29881619846, 2.1798546456, -1.12074482885, 0.695984356295, 0.252140040788, -0.147796411712, -3.29142014699, -1.11599423885, 2.34804181151, 1.10057979133, 5.1698573206, 3.19467856587, 4.54174726053, -3.29275941503, 0.693572771345, 2.11677451125, 1.19675316213, 2.50118805401, 0.724413267091, 4.91309632562, -1.40844378954, 0.737967769075, 0.98971628016, -2.22197732269, 3.38564330407, -2.48568628218, 1.07776890924, 3.81129245878, -1.92535536545, -0.414378752117, 4.06862945548, 3.14840477363, -1.34670298676, 2.76503358348, 3.08969294223, 1.58537837381, -2.12787217577, 1.45580901885, -2.76777137014, -2.14432042275, 2.67211758719, 4.16160838747, 2.57581839534, -2.58478921489, 0.741684547766, 0.9265260623, 3.81211037065, 2.04485835276, -2.36166750512, -2.92654321698, 0.244067480484, 2.49289630176, -2.23469502526, -1.26794967346, -2.31874087616, -0.489189332123, -3.12278244032, -0.231309991614, 3.85016440071, 1.21997703435, 1.95774183455, 0.793867295126, -3.50181266692, -3.06337966582, -0.208592405006, 3.69901063099, 0.364567390026, -3.75492901778, -1.0782578202, 2.81893761314, -1.46902168402, -1.65329910422, 0.458563244374, -3.42630504818, -0.832421999939, 3.56438475706, 3.66121175267, 1.04687635294, 0.766670883713, -1.94435448279, -1.42978647352, -1.53051661165, -1.84750236353, 1.97808683295, 4.16510398021, -2.90233508396, 3.97149109334, -2.13346692849, -2.13225218685, 3.29346784744, 3.64322426981, -1.00384738453, -1.88819832204, -2.70990448732, -2.77132196861, 3.43857647861, 3.31409151471, -1.45525875596, 2.0387537371, 2.87501146153, -0.248412879141, 2.63717109356, 2.45741076987, 2.76667564531, 4.77854355311, -0.953295124543, 1.95999662526, 2.53491478988, -3.81129888078, 3.27007852498, -3.1373579252, 1.29143686609, 0.500105998165, -0.738646662736, 4.30320320594, -3.86034362752, 3.59800433084, -0.12878990184, -1.02212330339, 3.40582285312, 1.36055366858, 0.632663052286, -0.63530148592, -1.13374148102, 1.59133569185, 3.00780705181, 0.651028905627, 4.15143796366, -1.48298926567, 0.0274998498379, 3.63087237007, -2.84059147318, 1.33955057577, -0.406638844589, -0.942673560021, -1.98806039526, 2.00435142995, 0.127031315196, -0.222367298778, -1.04257886595, -1.68685072414, 1.86004210107, 2.88012144533, -1.17701791295, -0.308636809461, 2.82399478351, 3.86500259442, -0.810338108736, 2.04657447456, -2.98512566559, 2.42866076818, -0.64681089132, -1.98170132247, -1.5023214517, -0.117265452855, -2.29825931729, 2.64257303655, -2.97032688113, 0.367702903632, -3.92322048245, 1.90890479658, 0.295842577289, 0.850741411519, -2.82928014193, 4.04977450961, 4.61916844547, -2.8341564742, 1.07092131254, -2.59967817119, 3.21542970581, -1.70378102102, 0.224877332427, 2.04235000237, 3.77337325689, 3.62434238067, 2.3658679282, -2.7688728962, -3.54211347512, 0.490095323251, -3.47552416227, -0.351057583185, 1.90883248359, -1.42331201982, -2.60788184995, 2.29471084983, 1.32211303516, -2.11395372291, -2.29853399494, -2.6005640863, 4.80391020556, -2.79557478505, -3.17427129386, -1.84714725381, -0.930773666338, 3.48113115446, 2.40633762944, -1.65332582971, 4.26825781835, -4.11764015582, 3.37183411426, -1.17067931844, 0.0923384077709, -1.77457623598, 2.99204129675, 1.68429269678, 2.49902208634, -0.28098291337, -0.472530807231, 1.31753206309, 0.0461022457422, -1.83711761846, 0.358601273614, 0.157969792069, 0.176480645265, -1.05673513476, 4.9511645805, -0.956110502994, 1.04133933732, 0.302588075294, 0.812796146146, -1.55838893189, -3.00101234593, -2.39455895029, 2.57597329552, -0.775381658492, -1.57527679493, 4.05207961016, 0.966978167481, -3.68935641229, 1.55484165833, 0.220923990259, 2.28956403016, 1.90386388373, 0.801690564832, -0.585893585796, -1.79385180656, 3.66443735652, 1.16218829873, 2.44269115477, -2.22758151763, 4.07730217327, -2.08480562196, 1.75975786816, -2.15508466999, 4.27922363559, -0.891370291629, 1.01961573995, -0.260908234047, 0.23727626536, 3.33606371128, -1.54790096141, 2.24716541493, 2.79159177775, -0.537326460751, 2.79977605385, 2.300924339, -0.0688190214784, -1.51469927937, -0.00581979186487, 3.30258222833, 4.14396403724, -0.120127491124, -1.45240658954, -1.6250149094, 3.02864403684, 3.50739459552, -3.29618046498, 2.5766830547, 0.320088310221, 2.88736171176, 4.08913195333, 2.58441428481, -0.439159067499, 4.1202988017, -0.999061040992, 1.04645634397, -4.14401125164, 1.11861822186, -0.320911823099, -0.454970692787, -2.06390304949, -3.60874647617, -1.92614878022, 0.330535650132, 3.07912083262, 0.211157039346, -1.41342931641, -2.89625787816, -1.21525786458, -1.99747153404, 2.38360436056, 0.98205609407, 1.67274225202, -0.39990195144, -2.67968032769, 2.90670142297, -2.97961598054, 1.3044889912, -2.02943424058, -0.313559145855, 1.39248775661, 3.75910115991, 2.74300505009, -0.316905709912, 2.30854543722, -4.11147607523, 4.11632886847, -3.06300256075, -2.20772631296, 1.24823232639, 4.51241073786, 2.95343232452, -2.49630643622, -2.2685421005, -2.58021451251, 1.59380372801, 3.5292105216, -3.6173083118, 1.70101611228, -0.303491225293, 2.62472580737, 4.52966172351, 2.99228830383, -2.49158347751, 0.190044931805, -0.275816641634, 3.43959429525, -1.14827711796, -3.62372087059, 0.152618171367, -0.548151104933, 1.41571768555, 2.4933958796, 1.00044964613, 1.63021174362, 2.70359804861, -0.347120641663, 0.993176920453, -1.57389914727, -0.259243113497, -2.42973634349, 1.07991949312, 3.22849084768, 4.79391253333, -0.890487364611, -1.12515186206, -3.71565844563, -3.11985588709, 3.58828079249, -1.17268118935, 1.32300868673, 1.35019640098, -2.48083503646, -0.429201001545, 1.68670481678, 4.59399118678, -0.824209268306, -1.55083251834, 0.5821131488, 1.82611828149, 4.10067848225, -2.17981214711, 0.717290105335, 2.84911074615, 2.07257874259, 3.07903073602, 0.733379583945, -3.39208390435, -1.92330202743, -1.22015756342, -0.71579714095, 0.4783898886, -1.88490212717, 2.43051238936, 3.71275391038, -2.1516034475, 3.16763094386, 2.38833064049, 1.75873363671, -0.651733369863, 1.60182181616, 1.65836433095, -3.01917494956, -2.98520223755, 3.74937055452, 1.72324754898, 3.61748572706, -0.739380198947, 5.2889892628, -1.37373472211, 0.910703071009, 3.64575077912, 2.44670169077, 1.68628336141, -0.526644019543, 4.43082950583, -2.53600560649, -2.89093091186, 1.25656847427, -2.5852797674, 3.83238407373, -0.119083799795, 1.00842714551, -3.42892716665, -0.186721894202, -1.01354952677, -1.74741925166, 0.263215242639, -0.159380664148, 1.18729671398, -2.49717422548, 3.85517396759, 1.52686624775, -2.33850970147, -3.93132626921, 0.753572452518, 1.01159376025, -0.139109296068, -1.81887023101, 3.03398547237, 1.82549227782, 3.45051176157, 3.541168515, 4.80480012111, 2.2270564586, 1.51780461108, 0.0368393521912, -2.2385526132, 3.32179614832, -3.24655083596, -0.0803612163943, 0.457044073152, -0.252357206057, 1.28816071907, 2.6017475473, -2.51090601138, -3.3145348409, -2.90545270247, -2.50593272015, 4.68910517498, -1.82142524759, 2.90891255415],
mode: "markers",
marker: {
size: 12,
line: {
color: "rgba(217, 217, 217, 0.14)",
width: 0.5
},
opacity: 0.8
},
type: "scatter3d"
};
var trace2 = {
x: [-0.100387678599, -0.841098362432, -0.086900337279, -0.418153015989, -0.197122458852, 0.0391933774019, -0.759329967599, -1.29266640992, 0.950624526622, 1.52725553555, 2.25231901948, 1.84936962902, 0.833618714205, 2.42998331172, 1.73583322891, 3.19694965552, -0.909512478385, 0.983932265051, -0.992449424459, 2.349425425, -1.60550784046, 2.68216122416, 2.22665169157, -0.775707830008, 0.569030921894, 0.310849282625, 2.39935206131, -1.66045702411, 3.76747878057, 3.05333459172, -3.35932368186, 3.43730482552, -3.07611001807, -0.842850343527, 3.50008556345, 0.165085596719, -0.339561268287, -1.74747448536, 3.56148886503, 1.8353330132, -1.90428086596, -0.912688959871, -2.37825362991],
y: [0.14252201109, 0.745253687488, 1.16250599725, 2.47176489125, -1.69476239552, -0.48991323684, 1.84409425219, 0.367526589193, -0.328695718905, 2.14081057301, 2.03064486378, -0.904917704389, -0.736099553953, -0.479945186555, 1.05076717167, 2.31045246862, 3.56214860102, -1.24356092573, 2.81251569105, 0.0354567947856, -0.764543463049, -0.463534094967, 0.121969881263, 3.10372387334, -3.07803266701, 3.94722158567, -2.3010720086, 0.522405164718, 2.09399114056, -0.206807957036, -0.102937553009, 1.93741482093, 2.13939929808, 2.31731711195, 2.04266966673, -2.83044062307, -1.29617222855, -0.0602624529294, -0.288215534329, 3.93478999833, 0.185708369263, -0.495944639256, -0.147527715708],
z: [-0.0850216981743, 0.0772495602215, 0.822100957178, 0.234493023372, 1.32486987031, 1.35806542101, -0.737286816662, -0.563373179749, -0.0551875444142, -0.104727172455, 0.653748756692, 1.99993870003, 2.1181425229, 1.5259703198, -0.621228886025, 0.409865697587, 0.65584453111, 2.11519050918, 0.311775993159, 1.78321165695, 0.472856801961, 0.918408722859, 3.36357867891, 0.253121323865, 2.00494245448, 0.725818892026, -0.791414427718, 0.339800250917, 1.43633692227, -0.644759286391, 1.06252011487, -0.884604393579, 0.590838097803, -1.77517601605, 1.03386775027, -0.451081715245, 2.89900356475, 1.50485074307, -0.199970622936, 2.71850157406, -2.37896493905, -1.03295302469, 1.42318432732],
mode: "markers",
marker: {
color: "rgb(127, 127, 127)",
size: 12,
symbol: "circle",
line: {
color: "rgb(204, 204, 204)",
width: 1
},
opacity: 0.9
},
type: "scatter3d"
};
var data = [trace1, trace2];
var layout = {margin: {
l: 0,
r: 0,
b: 0,
t: 0
}};
var graphOptions = {layout: layout, filename: "simple-3d-scatter", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: 3D Scatter Plots
permalink: nodejs/3d-scatter-plots/
description: How to make 3D scatter plots in nodejs.
thumbnail: thumbnail/3d-scatter.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","3d-scatter" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Overlaid Area Chart
suite: area
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4],
y: [0, 2, 3, 5],
fill: "tozeroy",
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4],
y: [3, 5, 1, 7],
fill: "tonexty",
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "basic-area", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Filled Area Plots
permalink: nodejs/filled-area-plots/
description: How to make a filled area plot in nodejs. An area chart displays a solid color between the traces of a graph.
thumbnail: thumbnail/area.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","area" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Line and Scatter Plots
permalink: nodejs/line-and-scatter/
description: How to make line and scatter plots in nodejs. Seven examples of basic and colored line and scatter plots.
thumbnail: thumbnail/line-and-scatter.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","line\_and\_scatter" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Line Shape Options for Interpolation
suite: line\_and\_scatter
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4, 5],
y: [1, 3, 2, 3, 1],
mode: "lines+markers",
name: "'linear'",
line: {shape: "linear"},
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4, 5],
y: [6, 8, 7, 8, 6],
mode: "lines+markers",
name: "'spline'",
text: ["tweak line smoothness<br>with 'smoothing' in line object", "tweak line smoothness<br>with 'smoothing' in line object", "tweak line smoothness<br>with 'smoothing' in line object", "tweak line smoothness<br>with 'smoothing' in line object", "tweak line smoothness<br>with 'smoothing' in line object", "tweak line smoothness<br>with 'smoothing' in line object"],
line: {shape: "spline"},
type: "scatter"
};
var trace3 = {
x: [1, 2, 3, 4, 5],
y: [11, 13, 12, 13, 11],
mode: "lines+markers",
name: "'vhv'",
line: {shape: "vhv"},
type: "scatter"
};
var trace4 = {
x: [1, 2, 3, 4, 5],
y: [16, 18, 17, 18, 16],
mode: "lines+markers",
name: "'hvh'",
line: {shape: "hvh"},
type: "scatter"
};
var trace5 = {
x: [1, 2, 3, 4, 5],
y: [21, 23, 22, 23, 21],
mode: "lines+markers",
name: "'vh'",
line: {shape: "vh"},
type: "scatter"
};
var trace6 = {
x: [1, 2, 3, 4, 5],
y: [26, 28, 27, 28, 26],
mode: "lines+markers",
name: "'hv'",
line: {shape: "hv"},
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4, trace5, trace6];
var layout = {legend: {
y: 0.5,
traceorder: "reversed",
font: {size: 16},
yref: "paper"
}};
var graphOptions = {layout: layout, filename: "line-shapes", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Colored and Styled Scatter Plot
suite: line\_and\_scatter
---
require('plotly')(username, api\_key);
var trace1 = {
x: [52698, 43117],
y: [53, 31],
mode: "markers",
name: "North America",
text: ["United States", "Canada"],
marker: {
color: "rgb(164, 194, 244)",
size: 12,
line: {
color: "white",
width: 0.5
}
},
type: "scatter"
};
var trace2 = {
x: [39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046, 18007],
y: [33, 20, 13, 19, 27, 19, 49, 44, 38],
mode: "markers",
name: "Europe",
text: ["Germany", "Britain", "France", "Spain", "Italy", "Czech Rep.", "Greece", "Poland"],
marker: {
color: "rgb(255, 217, 102)",
size: 12,
line: {
color: "white",
width: 0.5
}
},
type: "scatter"
};
var trace3 = {
x: [42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
y: [23, 42, 54, 89, 14, 99, 93, 70],
mode: "markers",
name: "Asia/Pacific",
text: ["Australia", "Japan", "South Korea", "Malaysia", "China", "Indonesia", "Philippines", "India"],
marker: {
color: "rgb(234, 153, 153)",
size: 12,
line: {
color: "white",
width: 0.5
}
},
type: "scatter"
};
var trace4 = {
x: [19097, 18601, 15595, 13546, 12026, 7434, 5419],
y: [43, 47, 56, 80, 86, 93, 80],
mode: "markers",
name: "Latin America",
text: ["Chile", "Argentina", "Mexico", "Venezuela", "Venezuela", "El Salvador", "Bolivia"],
marker: {
color: "rgb(142, 124, 195)",
size: 12,
line: {
color: "white",
width: 0.5
}
},
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: "Quarter 1 Growth",
xaxis: {
title: "GDP per Capita",
showgrid: false,
zeroline: false
},
yaxis: {
title: "Percent",
showline: false
}
};
var graphOptions = {layout: layout, filename: "line-style", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Line Plot
suite: line\_and\_scatter
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4],
y: [16, 5, 11, 9],
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "basic-line", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Line and Scatter Plot
suite: line\_and\_scatter
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: "markers",
type: "scatter"
};
var trace2 = {
x: [2, 3, 4, 5],
y: [16, 5, 11, 9],
mode: "lines",
type: "scatter"
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: "lines+markers",
type: "scatter"
};
var data = [trace1, trace2, trace3];
var graphOptions = {filename: "line-scatter", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Embedding Graphs in HTML
permalink: nodejs/embedding-plotly-graphs-in-HTML/
description: How to embed plotly graphs with an iframe in HTML.
page\_type: example\_index
display\_as: get\_request
---

Plotly graphs can be embedded in any HTML page. This includes [Nodejs dashboards](http://moderndata.plot.ly/r-python-matlab-dashboards-graphs-with-d3-js-webgl/), [Wordpress sites](https://wordpress.org/plugins/wp-plotly/), blogs, and more.

For more on embedding Plotly graphs in HTML documents, [see our tutorial](https://plotly.com/how-to-embed-plotly-graphs-in-websites).
---
name: Polar Charts
permalink: nodejs/polar-chart/
description: How to graph polar charts in nodejs. Seven examples of polar line, polar scatter and polar area charts.
thumbnail: thumbnail/polar.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","polar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Polar Line Chart
suite: polar
---
require('plotly')(username, api\_key);
var trace1 = {
r: [1, 0.995, 0.978, 0.951, 0.914, 0.866, 0.809, 0.743, 0.669, 0.588, 0.5, 0.407, 0.309, 0.208, 0.105, 0, 0.105, 0.208, 0.309, 0.407, 0.5, 0.588, 0.669, 0.743, 0.809, 0.866, 0.914, 0.951, 0.978, 0.995, 1, 0.995, 0.978, 0.951, 0.914, 0.866, 0.809, 0.743, 0.669, 0.588, 0.5, 0.407, 0.309, 0.208, 0.105, 0, 0.105, 0.208, 0.309, 0.407, 0.5, 0.588, 0.669, 0.743, 0.809, 0.866, 0.914, 0.951, 0.978, 0.995, 1],
t: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360],
mode: "lines",
name: "Figure8",
marker: {
color: "none",
line: {color: "peru"}
},
type: "scatter"
};
var trace2 = {
r: [1, 0.997, 0.989, 0.976, 0.957, 0.933, 0.905, 0.872, 0.835, 0.794, 0.75, 0.703, 0.655, 0.604, 0.552, 0.5, 0.448, 0.396, 0.345, 0.297, 0.25, 0.206, 0.165, 0.128, 0.095, 0.067, 0.043, 0.024, 0.011, 0.003, 0, 0.003, 0.011, 0.024, 0.043, 0.067, 0.095, 0.128, 0.165, 0.206, 0.25, 0.297, 0.345, 0.396, 0.448, 0.5, 0.552, 0.604, 0.655, 0.703, 0.75, 0.794, 0.835, 0.872, 0.905, 0.933, 0.957, 0.976, 0.989, 0.997, 1],
t: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360],
mode: "lines",
name: "Cardioid",
marker: {
color: "none",
line: {color: "darkviolet"}
},
type: "scatter"
};
var trace3 = {
r: [1, 0.996, 0.984, 0.963, 0.935, 0.9, 0.857, 0.807, 0.752, 0.691, 0.625, 0.555, 0.482, 0.406, 0.328, 0.25, 0.172, 0.094, 0.018, 0.055, 0.125, 0.191, 0.252, 0.307, 0.357, 0.4, 0.435, 0.463, 0.484, 0.496, 0.5, 0.496, 0.484, 0.463, 0.435, 0.4, 0.357, 0.307, 0.252, 0.191, 0.125, 0.055, 0.018, 0.094, 0.172, 0.25, 0.328, 0.406, 0.482, 0.555, 0.625, 0.691, 0.752, 0.807, 0.857, 0.9, 0.935, 0.963, 0.984, 0.996, 1],
t: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360],
mode: "lines",
name: "Hypercardioid",
marker: {
color: "none",
line: {color: "deepskyblue"}
},
type: "scatter"
};
var trace4 = {
r: [1, 0.998, 0.993, 0.985, 0.974, 0.96, 0.943, 0.923, 0.901, 0.876, 0.85, 0.822, 0.793, 0.762, 0.731, 0.7, 0.669, 0.638, 0.607, 0.578, 0.55, 0.524, 0.499, 0.477, 0.457, 0.44, 0.426, 0.415, 0.407, 0.402, 0.4, 0.402, 0.407, 0.415, 0.426, 0.44, 0.457, 0.477, 0.499, 0.524, 0.55, 0.578, 0.607, 0.638, 0.669, 0.7, 0.731, 0.762, 0.793, 0.822, 0.85, 0.876, 0.901, 0.923, 0.943, 0.96, 0.974, 0.985, 0.993, 0.998, 1],
t: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360],
mode: "lines",
name: "Subcardioid",
marker: {
color: "none",
line: {color: "orangered"}
},
type: "scatter"
};
var trace5 = {
r: [1, 0.997, 0.986, 0.969, 0.946, 0.916, 0.88, 0.838, 0.792, 0.74, 0.685, 0.626, 0.565, 0.501, 0.436, 0.37, 0.304, 0.239, 0.175, 0.114, 0.055, 0, 0.052, 0.098, 0.14, 0.176, 0.206, 0.229, 0.246, 0.257, 0.26, 0.257, 0.246, 0.229, 0.206, 0.176, 0.14, 0.098, 0.052, 0, 0.055, 0.114, 0.175, 0.239, 0.304, 0.37, 0.436, 0.501, 0.565, 0.626, 0.685, 0.74, 0.792, 0.838, 0.88, 0.916, 0.946, 0.969, 0.986, 0.997, 1],
t: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354, 360],
mode: "lines",
name: "Supercardioid",
marker: {
color: "none",
line: {color: "green"}
},
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4, trace5];
var layout = {
title: "Mic Patterns",
font: {
family: "Arial, sans-serif;",
size: 12,
color: "#000"
},
showlegend: true,
width: 500,
height: 400,
margin: {
l: 40,
r: 40,
b: 20,
t: 40,
pad: 0
},
paper\_bgcolor: "rgb(255, 255, 255)",
plot\_bgcolor: "rgb(255, 255, 255)",
orientation: -90
};
var graphOptions = {layout: layout, filename: "polar-line", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Polar Area Chart
suite: polar
---
require('plotly')(username, api\_key);
var trace1 = {
r: [77.5, 72.5, 70.0, 45.0, 22.5, 42.5, 40.0, 62.5],
t: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "11-14 m/s",
marker: {color: "rgb(106,81,163)"},
type: "area"
};
var trace2 = {
r: [57.5, 50.0, 45.0, 35.0, 20.0, 22.5, 37.5, 55.0],
t: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "8-11 m/s",
marker: {color: "rgb(158,154,200)"},
type: "area"
};
var trace3 = {
r: [40.0, 30.0, 30.0, 35.0, 7.5, 7.5, 32.5, 40.0],
t: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "5-8 m/s",
marker: {color: "rgb(203,201,226)"},
type: "area"
};
var trace4 = {
r: [20.0, 7.5, 15.0, 22.5, 2.5, 2.5, 12.5, 22.5],
t: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "< 5 m/s",
marker: {color: "rgb(242,240,247)"},
type: "area"
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: "Wind Speed Distribution in Laurel, NE",
font: {size: 16},
legend: {font: {size: 16}},
radialaxis: {ticksuffix: "%"},
orientation: 270
};
var graphOptions = {layout: layout, filename: "polar-area-chart", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Polar Scatter Chart
suite: polar
---
require('plotly')(username, api\_key);
var trace1 = {
r: [6.80498578527, 3.38959601061, 5.38147211075, 8.05954021942, 5.31822922787, 2.98509993563, 1.96658700238, 6.76926540821, 4.07340189872, 6.50437182527, 7.556369819, 4.04745609407, 7.38666249607, 5.41362473698, 7.47071653116, 7.98211021694, 4.73781408009, 4.20645304293, 5.47860480459, 4.8245202807, 5.5996006099, 6.86679521708, 3.08567136626, 7.77181094323, 3.6877944351, 5.36035668519, 5.1404467393, 6.04544568093, 6.83392094019, 3.62076946254, 3.9894305834, 5.3118244995, 4.60821348028, 6.64058471615, 3.05518885448, 7.49256416375, 5.48507817779, 3.89779499662, 5.97624511403, 5.44706156091, 5.37703411681, 4.69080578773, 4.71164049118, 3.62991932939, 5.95766807637, 5.35712128439, 3.84923528282, 6.25050713632, 7.12224335715, 3.39940423384, 3.51055667227, 4.10099760366, 4.0963821002, 6.23358307481, 3.93948852677, 3.9254450774, 6.11813250146, 3.94045034629, 7.58301557326, 3.51320214534],
t: [-30.3529443619, -25.6114598545, -12.4252274527, 13.9613805187, -4.95093284067, -25.6922741909, 12.4687641616, -4.91376410703, -10.9673802876, 30.8141940549, 2.47495943114, 17.9755437524, 0.771130593362, 6.13748848563, -14.451963574, 28.1845341129, 12.538680066, -8.98323033713, 5.23128516476, -64.4890025358, 11.3574866818, 3.45407479151, 13.9243466131, -25.3640020468, -16.818006386, -10.2600510306, -13.2121341256, 2.5793388653, 8.71757496585, -10.6754987192, -2.92636601252, 25.1958807548, 40.5903293216, -9.12143363019, -24.2973623813, -3.17694450569, 10.8504984192, -31.3320597474, 4.84956746221, 15.0482769541, 3.29510469926, -6.19709187313, -8.77857413578, 29.5491741194, -5.13744879288, 23.0268604879, -6.63481657837, 2.75501499186, 21.7332501137, -24.8169949601, -7.83054706253, 28.3257962102, 12.3009774678, -21.56315724, -19.3355162838, 26.1464431708, -1.70607120268, 16.071723695, 2.05326630285, -5.09791161233],
mode: "markers",
name: "Trial 1",
marker: {
color: "rgb(27,158,119)",
size: 110,
line: {color: "white"},
opacity: 0.7
},
type: "scatter"
};
var trace2 = {
r: [3.48804392301, 2.91847857636, 4.20182735997, 8.22732460685, 4.77669042724, 3.04191230311, 4.78994771908, 5.66388078036, 3.85826239317, 8.26021288114, 6.86862448643, 5.74019759967, 6.59497928246, 5.69270377821, 5.33791657446, 9.28360418518, 5.76459089314, 4.02886455205, 5.66234474837, 0.422837231101, 6.20126646393, 6.43926538132, 5.09675851306, 4.63208190873, 3.42184613631, 4.36940470335, 4.02833441941, 5.80576719754, 6.84818992143, 3.80929551278, 4.38526818383, 6.98332684555, 7.39627318603, 5.21512500314, 3.08614877924, 6.33539449149, 6.09041471406, 2.4480560069, 5.94278402031, 6.37312988559, 5.45420534118, 4.39333761656, 4.20594467998, 6.15554228796, 5.11908717116, 6.86986083083, 4.10459986058, 5.95434812558, 8.09233287715, 2.96176970545, 3.97401218758, 6.37338412891, 5.41540914318, 3.87689091998, 3.26144694742, 6.1458085297, 5.50245198719, 5.57155329531, 6.85304926109, 4.14035507494],
t: [14.8066257809, 79.0063403726, 49.0220655413, 49.699083136, 54.1374910829, 86.4193210205, 96.9523919357, 41.4634882636, 67.1376916934, 68.0610394397, 42.6819303227, 76.3986566081, 42.1947934722, 59.5778889746, 27.5108667993, 60.7534448323, 68.3708327991, 65.7480281495, 58.5330083721, -176.744106458, 61.17401858, 47.451508589, 84.4266531858, 12.4793465505, 72.4808027618, 50.5788317578, 51.5602282402, 52.4378561813, 51.5868279921, 73.8729447773, 70.2170569279, 70.7142991543, 82.2343944264, 38.935390447, 84.7093666702, 38.1658284365, 61.7040536538, 70.1969562924, 54.4542925901, 64.3348949686, 58.2738931466, 60.4998223904, 59.155232539, 83.8656184676, 47.8734098973, 69.2826015659, 71.1899104287, 51.048396463, 59.4275824152, 78.5987369617, 75.7558645152, 79.9704837232, 73.8937802463, 31.7334111317, 68.084751177, 80.4110799786, 48.9242507089, 76.6502557554, 42.1828643629, 76.0333358945],
mode: "markers",
name: "Trial 2",
marker: {
color: "rgb(217,95,2)",
size: 110,
line: {color: "white"},
opacity: 0.7
},
type: "scatter"
};
var trace3 = {
r: [1.85587083503, 5.28696206204, 3.88601339194, 6.282863313, 4.45341484774, 5.68800805076, 7.33086428261, 3.82566059479, 4.98960417696, 7.89743146977, 4.65669311302, 6.66715369631, 4.43100628714, 5.34611325338, 2.47994569588, 8.11347734853, 6.08131168231, 4.96821689621, 5.24445392063, 5.42220788417, 5.79277461602, 4.78758059223, 6.78431863718, 1.10893690948, 5.13891110524, 4.04292965729, 4.02289202968, 4.82842879131, 5.41737837431, 5.37863521067, 5.42109717546, 7.12056197886, 8.3493085399, 3.41048558832, 5.62837847088, 3.91493697614, 5.76394026236, 4.7643741068, 5.0762362679, 6.1655581832, 5.10557651628, 4.76103637693, 4.59624954094, 7.50418841135, 4.10703141792, 6.92042229938, 5.34912894956, 4.79806571939, 7.0232515323, 5.28368096546, 5.56907115243, 7.38379490845, 6.26923321044, 2.65652964501, 4.8439843388, 7.24799236156, 4.37295939441, 6.57098108136, 4.60247924389, 5.67005205083],
t: [151.294255181, 147.188025028, 125.282157112, 87.0672979717, 119.627898357, 147.740824147, 139.564598145, 101.391497102, 134.56018428, 104.024444705, 89.3931429448, 123.1940314, 91.4743405152, 113.332373614, 96.1499255673, 93.2807345226, 118.215565226, 132.322937378, 112.941186391, -179.746233138, 110.303513559, 97.7508361661, 131.608089257, 115.496919231, 140.58118216, 123.396662119, 128.342009045, 107.608810398, 97.9046897875, 137.128447975, 130.431244912, 112.227084481, 118.630202246, 106.05822559, 146.908109706, 90.2773495582, 111.505282363, 151.089742536, 107.721394157, 111.300854997, 114.680277936, 126.569379493, 128.218952233, 125.354857195, 112.418068253, 111.797355679, 133.418052258, 105.184116842, 97.2310361206, 146.668036804, 136.239315201, 121.791844193, 123.911327971, 129.86224497, 141.34395085, 123.270967749, 108.458821723, 124.412377056, 89.0271107387, 134.876701145],
mode: "markers",
name: "Trial 3",
marker: {
color: "rgb(117,112,179)",
size: 110,
line: {color: "white"},
opacity: 0.7
},
type: "scatter"
};
var trace4 = {
r: [5.37247092432, 7.09635557204, 4.8838239032, 2.92013544124, 4.72396304568, 7.42369395093, 8.0909460754, 3.30684459137, 6.05082848252, 5.53023207444, 2.47230695264, 6.27567053686, 2.61589617379, 4.65353994458, 3.33544001388, 4.79588360487, 5.47271134648, 5.88193049095, 4.57158707205, 9.0398611698, 4.6429075999, 3.1727677358, 7.04424813882, 4.46633651411, 6.5573302898, 4.82084943725, 5.13191551521, 3.97001223705, 3.40632381283, 6.476722964, 6.01921850933, 5.66450153495, 7.15875852255, 3.60071266167, 7.32412716876, 2.55294615625, 4.72713386039, 6.97175520718, 4.07657836107, 4.94622340701, 4.64215544904, 5.36057486441, 5.39171906736, 7.0725243051, 4.10111157028, 5.48573262102, 6.19253528611, 3.76871139184, 4.29031138976, 7.06019536969, 6.53969184418, 6.67974440649, 6.0608253587, 4.78657404093, 6.41668652967, 6.70328133339, 3.88884781048, 6.30859108119, 2.4370447709, 6.5081863479],
t: [-140.203327641, -168.084245433, -166.285141329, 138.248866753, -174.424386436, -169.960482759, 176.991822687, -169.901416249, -172.641581594, 142.951668814, 172.415746367, 168.519359196, 177.822053694, 172.855190349, -146.014521701, 128.177293024, 169.167072781, -173.588573789, 173.726992705, -151.206104772, 166.260477163, 172.507566082, 173.949183904, -131.806840938, -170.635273831, -168.577085483, -166.765503421, 176.070487348, 162.297501498, -174.055746313, -178.060929857, 156.47126885, 155.239142145, -163.000526394, -170.116713265, -170.639272487, 167.383143694, -163.098817056, 172.880737006, 163.386007682, 176.182541977, -174.579680174, -172.335844882, 165.338025694, -172.525664261, 157.542877739, -175.881511093, 175.427643994, 142.069674723, -168.340734019, -175.805831123, 163.063745419, 171.720974997, -151.403904569, -168.27136909, 165.045327878, -177.315336665, 170.042412897, 173.59919661, -177.250656746],
mode: "markers",
name: "Trial 4",
marker: {
color: "rgb(231,41,138)",
size: 110,
line: {color: "white"},
opacity: 0.7
},
type: "scatter"
};
var trace5 = {
r: [7.93755787138, 7.30274649152, 5.92930222144, 2.40717871317, 5.27092188706, 7.40059612754, 6.81082033836, 4.96775903442, 6.19022937045, 2.15851865795, 4.00412589387, 4.77661732163, 4.23225045181, 4.30765487269, 6.20027517286, 0.727513848534, 4.37800680381, 6.00496493944, 4.34193170292, 10.2379829353, 3.8021588887, 3.96928117014, 5.75898014247, 7.67417906914, 6.69995353301, 5.73431038813, 6.0442759153, 4.31294306609, 3.37754528241, 6.36766672727, 5.73724418155, 3.39635147199, 4.21646748139, 5.46488501672, 7.31113557753, 4.74540076936, 3.91646853189, 7.60297299033, 4.12520482944, 3.67679494965, 4.55123578852, 5.60696053152, 5.79484425749, 5.03052815569, 5.10958624099, 3.40544020796, 6.02630612539, 4.22110926364, 1.90978293658, 7.25466939392, 6.26887587203, 4.56258056659, 4.91805796544, 6.83656096253, 6.78648654914, 4.75101433449, 4.71992634764, 4.92780521518, 4.05919058739, 6.12833898429],
t: [-101.833785776, -127.478391579, -112.244284997, -82.3259108712, -114.688855621, -130.537863362, -145.010264976, -98.7488450072, -124.441748821, -152.45411927, -89.2942365523, -139.832451718, -91.5435951844, -119.442163004, -92.4558385274, -129.659924316, -131.051235099, -123.852917454, -118.086739004, -121.979217138, -121.915029968, -99.3618475777, -141.467701997, -93.5662631891, -126.336901405, -112.834944178, -114.386479929, -109.796072327, -102.743264712, -128.246728907, -127.792092643, -142.473629745, -161.587294187, -99.9406107796, -130.163117326, -90.2288120096, -122.650491214, -123.267750572, -111.997308801, -127.528316806, -117.931295338, -120.391634245, -119.386871479, -149.674695492, -107.850517506, -138.989931341, -127.595470214, -107.32083544, -117.573807423, -127.481660968, -129.912033166, -148.495211671, -135.33164137, -104.421659276, -123.875440211, -146.816826618, -107.058485424, -138.902564873, -88.8968825195, -130.754467356],
mode: "markers",
name: "Trial 5",
marker: {
color: "rgb(102,166,30)",
size: 110,
line: {color: "white"},
opacity: 0.7
},
type: "scatter"
};
var trace6 = {
r: [8.46918052789, 5.82199756737, 6.14091832822, 5.83172428479, 5.54675447186, 5.6274877092, 3.94832897602, 6.49018461461, 5.32061824515, 3.24359304149, 6.44408533158, 3.36377810065, 6.46311681051, 4.73094492578, 7.79657841111, 4.57012782992, 3.926206816, 5.25434813987, 4.83841110661, 8.69452399898, 4.39953181822, 5.85648390518, 3.62157703921, 8.89491237311, 5.49454283608, 5.96898089085, 6.0478995736, 5.38467139672, 5.3812200182, 5.11157462274, 4.77056110506, 3.09833088263, 1.66508317194, 6.74025853333, 5.59449492888, 6.87963082567, 4.38279246628, 6.41084361649, 5.15420431777, 4.01515851866, 4.93914886826, 5.29829731449, 5.49041717695, 2.62375125938, 5.95358866167, 3.30147937192, 4.9548890011, 5.50005366961, 4.45051234955, 5.78662451335, 4.90683442406, 2.62996947345, 3.76970360805, 7.3967357155, 5.76448190196, 2.79458519588, 5.78203326982, 3.48535191762, 6.50065359862, 4.74864071013],
t: [-66.5358363273, -84.5144226769, -63.3397416996, -24.1468127442, -59.7012453226, -88.06537268, -98.4442045353, -49.1583968172, -73.636223312, -17.9238746786, -38.4123994546, -66.3403623779, -40.8888387392, -52.46063321, -52.6104625591, -7.03935105091, -57.2354586922, -71.642203502, -52.3453961691, -92.7830386735, -47.187163055, -41.9692084629, -82.1442282499, -59.4391656032, -79.1948225932, -62.2999085353, -65.5379040394, -48.9060554476, -37.748311038, -78.0533334583, -71.8731176631, -41.8910928259, -53.1154554855, -52.9976280973, -87.0843610179, -43.6119048384, -48.7979984056, -82.5668031571, -47.9099629957, -46.5704855853, -54.5004832176, -65.9007271268, -66.8733174636, -75.4808072521, -54.7776938669, -42.5983345914, -74.5081662691, -47.1102184434, -22.3568731833, -84.192986745, -78.5052847562, -65.0363717923, -66.5137336813, -63.5267765618, -77.8090785513, -68.5101797401, -51.2968693109, -68.3399130277, -38.6317330684, -77.8518485851],
mode: "markers",
name: "Trial 6",
marker: {
color: "rgb(230,171,2)",
size: 110,
line: {color: "white"},
opacity: 0.7
},
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4, trace5, trace6];
var layout = {
title: "Hobbs-Pearson Trials",
font: {size: 15},
plot\_bgcolor: "rgb(223, 223, 223)",
angularaxis: {tickcolor: "rgb(253,253,253)"}
};
var graphOptions = {layout: layout, filename: "polar-scatter", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Line Chart and a Bar Chart
suite: mixed
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5],
y: [1.5, 1, 1.3, 0.7, 0.8, 0.9],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5],
y: [1, 0.5, 0.7, -1.2, 0.3, 0.4],
type: "bar"
};
var data = [trace1, trace2];
var graphOptions = {filename: "bar-line", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: A Contour and Scatter Plot
of the Method of Steepest Descent
suite: mixed
---
require('plotly')(username, api\_key);
var trace1 = {
z: [[1.5, 1.23469387755, 1.01020408163, 0.826530612245, 0.683673469388, 0.581632653061, 0.520408163265, 0.5, 0.520408163265, 0.581632653061, 0.683673469388, 0.826530612245, 1.01020408163, 1.23469387755, 1.5], [1.36734693878, 1.10204081633, 0.877551020408, 0.69387755102, 0.551020408163, 0.448979591837, 0.387755102041, 0.367346938776, 0.387755102041, 0.448979591837, 0.551020408163, 0.69387755102, 0.877551020408, 1.10204081633, 1.36734693878], [1.25510204082, 0.989795918367, 0.765306122449, 0.581632653061, 0.438775510204, 0.336734693878, 0.275510204082, 0.255102040816, 0.275510204082, 0.336734693878, 0.438775510204, 0.581632653061, 0.765306122449, 0.989795918367, 1.25510204082], [1.16326530612, 0.897959183673, 0.673469387755, 0.489795918367, 0.34693877551, 0.244897959184, 0.183673469388, 0.163265306122, 0.183673469388, 0.244897959184, 0.34693877551, 0.489795918367, 0.673469387755, 0.897959183673, 1.16326530612], [1.09183673469, 0.826530612245, 0.602040816327, 0.418367346939, 0.275510204082, 0.173469387755, 0.112244897959, 0.0918367346939, 0.112244897959, 0.173469387755, 0.275510204082, 0.418367346939, 0.602040816327, 0.826530612245, 1.09183673469], [1.04081632653, 0.775510204082, 0.551020408163, 0.367346938776, 0.224489795918, 0.122448979592, 0.0612244897959, 0.0408163265306, 0.0612244897959, 0.122448979592, 0.224489795918, 0.367346938776, 0.551020408163, 0.775510204082, 1.04081632653], [1.01020408163, 0.744897959184, 0.520408163265, 0.336734693878, 0.19387755102, 0.0918367346939, 0.030612244898, 0.0102040816327, 0.030612244898, 0.0918367346939, 0.19387755102, 0.336734693878, 0.520408163265, 0.744897959184, 1.01020408163], [1.0, 0.734693877551, 0.510204081633, 0.326530612245, 0.183673469388, 0.0816326530612, 0.0204081632653, 0.0, 0.0204081632653, 0.0816326530612, 0.183673469388, 0.326530612245, 0.510204081633, 0.734693877551, 1.0], [1.01020408163, 0.744897959184, 0.520408163265, 0.336734693878, 0.19387755102, 0.0918367346939, 0.030612244898, 0.0102040816327, 0.030612244898, 0.0918367346939, 0.19387755102, 0.336734693878, 0.520408163265, 0.744897959184, 1.01020408163], [1.04081632653, 0.775510204082, 0.551020408163, 0.367346938776, 0.224489795918, 0.122448979592, 0.0612244897959, 0.0408163265306, 0.0612244897959, 0.122448979592, 0.224489795918, 0.367346938776, 0.551020408163, 0.775510204082, 1.04081632653], [1.09183673469, 0.826530612245, 0.602040816327, 0.418367346939, 0.275510204082, 0.173469387755, 0.112244897959, 0.0918367346939, 0.112244897959, 0.173469387755, 0.275510204082, 0.418367346939, 0.602040816327, 0.826530612245, 1.09183673469], [1.16326530612, 0.897959183673, 0.673469387755, 0.489795918367, 0.34693877551, 0.244897959184, 0.183673469388, 0.163265306122, 0.183673469388, 0.244897959184, 0.34693877551, 0.489795918367, 0.673469387755, 0.897959183673, 1.16326530612], [1.25510204082, 0.989795918367, 0.765306122449, 0.581632653061, 0.438775510204, 0.336734693878, 0.275510204082, 0.255102040816, 0.275510204082, 0.336734693878, 0.438775510204, 0.581632653061, 0.765306122449, 0.989795918367, 1.25510204082], [1.36734693878, 1.10204081633, 0.877551020408, 0.69387755102, 0.551020408163, 0.448979591837, 0.387755102041, 0.367346938776, 0.387755102041, 0.448979591837, 0.551020408163, 0.69387755102, 0.877551020408, 1.10204081633, 1.36734693878], [1.5, 1.23469387755, 1.01020408163, 0.826530612245, 0.683673469388, 0.581632653061, 0.520408163265, 0.5, 0.520408163265, 0.581632653061, 0.683673469388, 0.826530612245, 1.01020408163, 1.23469387755, 1.5]],
x: [-1.0, -0.857142857143, -0.714285714286, -0.571428571429, -0.428571428571, -0.285714285714, -0.142857142857, 0.0, 0.142857142857, 0.285714285714, 0.428571428571, 0.571428571429, 0.714285714286, 0.857142857143, 1.0],
y: [-1.0, -0.857142857143, -0.714285714286, -0.571428571429, -0.428571428571, -0.285714285714, -0.142857142857, 0.0, 0.142857142857, 0.285714285714, 0.428571428571, 0.571428571429, 0.714285714286, 0.857142857143, 1.0],
ncontours: 30,
showscale: false,
type: "contour"
};
var trace2 = {
x: [-0.8, -0.48, -0.288, -0.1728, -0.10368, -0.062208, -0.0373248, -0.02239488, -0.013436928, -0.0080621568, -0.00483729408, -0.002902376448, -0.0017414258688, -0.00104485552128, -0.000626913312768, -0.000376147987661],
y: [-0.9, -0.72, -0.576, -0.4608, -0.36864, -0.294912, -0.2359296, -0.18874368, -0.150994944, -0.1207959552, -0.09663676416, -0.077309411328, -0.0618475290624, -0.0494780232499, -0.0395824185999, -0.0316659348799],
mode: "markers+lines",
name: "steepest",
line: {color: "black"},
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "contour-scatter", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Multiple Chart Types
permalink: nodejs/graphing-multiple-chart-types/
description: How to design figures with multiple chart types in nodejs. An example of a contour plot with a scatter plot and a bar chart with a line chart.
thumbnail: thumbnail/mixed.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","mixed" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Legend Names
suite: legends
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
name: "Blue Trace",
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
name: "Orange Trace",
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "legend-labels", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Legends
permalink: nodejs/legend/
description: How to modify the legend in nodejs graphs. Seven examples of how to move, color, and hide the legend.
thumbnail: thumbnail/legends.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","legends" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Positioning the Legend Inside the Plot
suite: legends
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
showlegend: true,
legend: {
x: 1,
y: 1
}
};
var graphOptions = {layout: layout, filename: "legend-inside", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Hiding the Legend
suite: legends
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {showlegend: false};
var graphOptions = {layout: layout, filename: "legend-visibility", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Hiding Legend Entries
suite: legends
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2],
y: [1, 2, 3],
name: "First Trace",
showlegend: false,
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3],
y: [8, 4, 2, 0],
name: "Second Trace",
showlegend: true,
type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "show-legend", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Styling and Coloring the Legend
suite: legends
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {legend: {
x: 0,
y: 1,
traceorder: "normal",
font: {
family: "sans-serif",
size: 12,
color: "#000"
},
bgcolor: "#E2E2E2",
bordercolor: "#FFFFFF",
borderwidth: 2
}};
var graphOptions = {layout: layout, filename: "legend-style", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Positioning the Legend Outside the Plot
suite: legends
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
showlegend: true,
legend: {
x: 100,
y: 1
}
};
var graphOptions = {layout: layout, filename: "legend-outside", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Plotly Node.js Graphing Library
permalink: /nodejs/
description: Plotly's Nodejs graphing library makes interactive, publication-quality graphs online. Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts and bubble charts.
layout: langindex
redirect\_from: nodejs/reference/
---

# Plotly node.js Library

{{page.description}}

{% assign languagelist = site.posts | where:"page\_type","example\_index" | where:"language","nodejs" | sort: order %}
{% include posts/documentation\_eg.html %}
---
name: 3D Line Plots
permalink: nodejs/3d-line-plots/
description: How to make 3D line plots in nodejs.
thumbnail: thumbnail/3d-line.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","3d-line" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 3D Line Plot
3D Random Walk
suite: 3d-line
---
require('plotly')(username, api\_key);
var trace1 = {
x: [-0.014460360111, 0.420723053511, 0.471955637602, -1.5980850775, -1.1696928974, 0.62887815642, 1.64225480141, 1.84538844321, 2.39903055756, 2.74061873532, 2.98184534361, 3.63482281441, 3.51947216482, 3.24422002592, 1.97987531822, 2.49306912443, 1.98065348142, 2.49148828382, 1.8166301311, -0.418444162232, -1.91452615762, -1.26261858994, -0.702841491138, -2.53578213432, -2.96566072736, -5.06110427809, -7.00637040896, -6.9990237396, -8.80043516671, -8.71239917157, -10.4880913229, -14.0237638556, -14.3444267254, -12.0425575011, -10.8147720387, -9.77322085369, -7.8871343368, -10.1779694809, -7.7922357105, -4.06012871996, -3.25503609007, -2.98098865248, -1.1460800781, -4.7132235257, -5.96126803183, -6.08422139999, -2.67777205929, -4.22903304342, -4.01470370535, -5.4925628554, -3.41315115276, -4.09417736042, -5.92604468977, -7.0398214854, -4.54137742868, -4.48795563261, -3.70646317414, -4.33965125791, -4.76111378599, -3.34964004567, -2.79516815968, -0.985062514936, -1.19713635343, -3.14305435084, -4.26844060776, -3.35551475326, -2.97635400821, -3.11226810057, -5.00517291984, -4.45828762509, -2.92964495631, -3.0340518455, -2.63137123131, -0.5984251984, 1.46882692707, 1.91813591611, 0.931131009822, -0.198698414513, -3.10258584158, -5.10707707985, -5.53978453609, -5.87190440655, -6.15266139896, -6.09909315047, -3.56047669739, -3.55761346254, -1.23993200533, 0.474795919986, -1.02959575087, -1.24291855948, -1.31426952875, -2.32409070416, -2.74719528672, 0.285902173824, 3.46346174555, 5.55064318821, 7.93131324422, 7.99242651171, 8.5373199465, 11.0752351805, 10.3205319282, 11.7581891849, 13.4949527524, 14.402257039, 14.3341961315, 16.7118900516, 14.2627254109, 16.5382962436, 15.3067781388, 18.1656461106, 17.0995160962, 15.934693484, 12.360748197, 12.4371219166, 13.5501064722, 13.2089378056, 14.1279104195, 13.4566914737, 15.9390080651, 15.2023626211, 12.443013371, 11.6235738652, 12.3093408538, 13.413332176, 13.3378554542, 12.7324527487, 10.9583926979, 12.4770860368, 10.3856928769, 11.2769203911, 10.9252342885, 10.5648842903, 9.90341705159, 8.90109222607, 8.74410691403, 5.62013558101, 5.75894407649, 7.14620387683, 7.82192882076, 9.99752533649, 11.4669502774, 10.3036227351, 10.6353641791, 14.7873630054, 14.6815788314, 17.4222005324, 15.9305759257, 16.4283318184, 17.5594396448, 17.8371814833, 16.6537129297, 12.9698129546, 8.22890747877, 10.4446077726, 13.148096571, 16.5755720498, 17.0970366987, 18.4260467093, 17.8427544622, 16.153890924, 16.1188692931, 17.0701110598, 16.5592444246, 16.7801876574, 18.7058755511, 16.8994733969, 15.093160324, 17.6321434315, 13.7980907919, 10.9898205761, 11.30276208, 9.37855259325, 10.9117452673, 11.0812344068, 12.8525922512, 10.7657134117, 11.555475122, 8.96571434472, 5.60051748344, 6.89258971926, 6.41484884007, 5.87972395348, 8.33839027511, 10.9814037915, 11.6656886194, 9.902573022, 8.96599982974, 9.70357715902, 9.47267497888, 7.59562651098, 8.05171507272, 6.81324160259, 5.93272558092, 5.66885758889, 8.38838033493, 4.29354010421, 4.72704863187, 7.2565249243, 7.97067463359, 6.38361598112, 5.68639720468, 2.3657444534, 1.70934714165, 2.45720993286, 2.03355212971, -0.174752482635, -2.38494583162, -3.61461123073, -5.76496371563, -7.50254742778, -9.2956270284, -9.36776589712, -5.91491283109, -8.43918270326, -11.0162806727, -10.4725899139, -11.2769921424, -10.5641008534, -11.9928147849, -12.7483073835, -14.7672001844, -13.4777929449, -15.7901116746, -14.5569502867, -16.4933826324, -19.358021726, -18.9508511213, -18.0968256136, -16.0255273907, -19.0290483393, -19.3290168721, -18.4769531356, -19.225163488, -23.0562321371, -24.2830335385, -23.438117191, -23.6555178343, -20.2726489546, -19.455048731, -19.7863053144, -18.6545983156, -19.3574121043, -19.2048630105, -16.5631387925, -15.9213347995, -13.1730323144, -11.2452962616, -12.1456072698, -9.42917902507, -9.75066084596, -12.4902089244, -10.76325461, -10.2495453882, -10.0696692325, -7.83101325354, -9.68160249681, -11.2012611972, -9.37769680478, -11.3548260447, -9.56939528372, -7.55818751635, -7.94327560797, -4.51860599279, -5.96428843721, -7.43356147407, -5.53530146882, -5.1413890716, -5.9311125606, -7.23379839661, -4.92435468262, -6.20244740005, -7.56491772354, -6.43501630667, -7.36860703403, -9.544850133, -9.35905877848, -10.7724736225, -10.1929460888, -10.2769806516, -11.5945844717, -10.2076146177, -9.17566745132, -6.44234561378, -3.03685959579, 0.108979069684, 1.63292321945, -3.08231707893, -3.99824601089, -4.76766751779, -3.92895570577, -5.07233023067, -8.06734947554, -8.50264105061, -6.53794408326, -10.9236159279, -9.30379256484, -10.6467278331, -8.18200271162, -10.059796806, -13.0293717991, -9.35950632056, -9.4789239713, -8.54771091302, -6.87012462088, -8.06314781495, -6.81596908504, -3.64375134679, -2.73147927876, -0.969365998405, 0.046563582321, -1.98724358604, -2.29256165664, -4.43869105617, -3.44517225471, -5.05223966562, -5.70299749891, -4.72847971208, -5.37093764623, -8.65020440945, -10.6837253481, -10.1912707497, -8.08829638699, -7.35358781352, -10.5409366475, -9.59489645073, -11.125325334, -11.7185324629, -9.09013732852, -9.53073643867, -8.2904173021, -7.45330020383, -11.3149293215, -16.3884225385, -18.1348641881, -18.3769467479, -17.1871943902, -15.3328226006, -17.2201521411, -17.6087543443, -15.6965494364, -15.8888438242, -20.0427030899, -23.5741499961, -19.9267862136, -21.7932428801, -23.7805433321, -25.2903769751, -25.8224052919, -24.0756715863, -25.1160211799, -25.546393164, -26.5906593435, -28.3738626728, -27.212679408, -27.8648258452, -26.5382940526, -25.586916026, -23.9564109112, -24.8999843293, -24.5346644423, -25.2946855379, -27.0004062596, -26.6711396325, -25.7663475401, -23.6294743054, -22.2400241472, -23.4733888841, -22.0949183054, -23.7355531844, -23.9509775377, -21.3666238956, -21.0093678628, -22.5848073055, -23.0656215594, -23.2985810682, -24.9971474878, -25.6633129801, -23.0545809277, -22.4892842952, -22.0735508018, -20.7213650517, -17.2799752137, -18.7207128821, -17.1134175191, -17.3409263049, -16.8129416381, -15.0749359741, -15.8271086115, -14.8564727297, -15.8419171177, -16.001723019, -14.7008670014, -15.16605393, -16.5309096861, -17.1568547726, -15.8705096954, -15.0024494448, -15.7021808293, -12.2844657768, -10.5479018293, -7.4518005957, -10.5802392826, -10.4006493629, -11.6842892572, -13.5834689025, -13.0607161531, -12.4155448759, -11.4505012147, -10.3850909339, -11.2515723444, -9.55434784734, -7.43312830104, -2.16593821075, -4.08221762842, -3.73195393908, -1.32326575066, -3.36692537518, -0.991913066176, -3.42123571217, -1.02113081403, 2.74183254031, 4.60885625505, 5.1861551236, 7.94967179126, 7.23625922783, 11.4668733809, 12.9839283711, 13.6676413556, 12.7973009454, 13.1099156282, 12.09218766, 11.5220142187, 11.1301441484, 11.8974589099, 12.6259500047, 12.5506560285, 11.7623224739, 11.9614908808, 11.0550734881, 10.7542274336, 11.4893880995, 12.6656611233, 11.9535123108, 13.1726500228, 12.7314023273, 11.4541551565, 13.5044145125, 14.659728697, 11.3050455557, 14.062830264, 11.6768006716, 14.205718455, 13.2378021907, 13.4086026846, 14.4872875275, 12.9146726617, 12.4278865741, 13.2699726471, 13.326369081, 17.7321012457, 16.1246193103, 17.2657086042, 15.8107330738, 19.1422205396, 20.0189257722, 20.6044386727, 21.7737473969, 21.8620350915, 23.4052117833, 24.4199787578, 25.7428708104, 26.0596029916, 29.900994098, 30.8273076541, 29.2632766369, 33.977461361, 32.9119469068, 36.9031371045, 36.6210092539, 37.3810650386, 37.3800860511, 35.8506871095, 34.5116207281, 31.8895747896, 28.6998961332, 27.2500469629, 26.3289359688, 27.0121527705, 27.0073442404, 27.0392676401, 25.5561594425, 23.8864018552, 22.9447401451, 22.4172756724, 24.8788043801, 25.785845786, 28.6473894815, 26.7868658329, 27.5716168017, 26.4848733333, 26.5473856292, 25.0235839332, 22.9507844486, 22.3705473521, 23.0130013465, 24.5364341706, 26.1916301396, 28.1858461289, 30.1234486307, 32.5482323589, 31.2720236008, 34.5838642411, 35.644628907, 38.5257176675, 42.4925301959, 41.0921638938, 40.5893719849, 39.9537576988, 41.5217578144, 41.4516919132, 40.9703271571, 43.8515189499, 40.7185932407, 40.0531803268, 43.6235911876, 45.0562420092, 44.5143791877, 45.0235896159, 43.1257801982, 43.3970785006, 43.1575387646, 44.267676731, 43.2642346276, 42.2388280464, 45.4752424723, 43.6610022886, 44.6357649311, 45.8362684079, 42.7975292245, 43.2518617821, 41.4902799952, 43.5055420864, 42.3654159831, 44.9633016211, 46.8406823939, 47.8887328253, 47.9668184741, 48.9315527199, 52.0774477511, 50.4074982543, 49.3129414837, 53.6993364348, 54.1705941421, 54.5423200842, 56.7860194537, 57.1697614709, 56.1456841836, 57.7825365701, 54.5700332444, 54.2747855578, 55.0148321021, 56.3828996237, 56.4979510016, 55.5551435977, 58.6687455234, 59.7987737712, 59.490021811, 57.7925471809, 57.7848243747, 58.1126777348, 59.2771454495, 60.3714657896, 60.4654095288, 62.0979812011, 64.0445832126, 62.3265390894, 64.433462931, 66.0708752918, 66.8132448713, 64.919562555, 66.8318835583, 66.6807507547, 66.3618170889, 64.7141243477, 68.0190617941, 67.1748720444, 66.7790297365, 67.1344583348, 68.7205666699, 66.8746665317, 65.4228818483, 63.6824943346, 63.2110711395, 61.4630477416, 60.160529121, 60.0023262306, 61.308739689, 63.1511086518, 63.9968569346, 63.4103923724, 62.8785884775, 63.1801833899, 65.6496168924, 66.8742131604, 69.4065817654, 66.9407261063, 66.348872735, 67.8490003057, 66.3591373994, 61.5285102571, 60.0786185511, 55.6865152346, 55.4261810103, 59.3586831537, 58.5617655876, 59.3370454932, 59.8693996196, 58.4997380382, 61.3595077562, 60.6908718815, 56.0713399861, 58.9818262092, 56.6953229396, 55.9019733387, 56.7590598976, 57.0977619898, 54.7502581374, 56.4088301793, 56.3319197665, 56.5191730601, 57.7448195729, 57.1951254613, 57.4723658916, 60.7836321755, 59.5657474523, 63.3232262653, 63.2017233682, 65.0418743014, 61.8925706021, 63.8624216121, 64.4870835027, 66.3342804835, 70.5746462219, 69.5412971747, 66.1308154526, 65.072105087, 63.9830876463, 61.425255881, 60.7530095384, 61.3581366493, 60.3132497969, 60.7165011718, 60.2314953019, 61.1103637904, 62.4995182621, 63.6216438761, 64.5448830092, 63.7572127674, 63.8412024403, 63.2765181115, 63.6584882487, 65.9013307744, 64.8794091133, 62.3599178175, 59.0226125922, 60.7843513319, 62.556626775, 62.3464276, 62.6287127393, 62.7824361713, 61.9148039496, 59.6383012348, 59.1349526478, 57.6856738612, 58.3342304827, 57.2040584005, 55.9491561977, 56.8243075432, 55.0884209903, 56.8794368898, 55.285452174, 58.0693251387, 59.7783520447, 62.5440804306, 63.1427439828, 63.2173713084, 65.5492712044, 66.3009604696, 66.6940375158, 67.8726403748, 66.771771401, 69.8100758199, 70.4313785817, 69.6078541068, 68.1961598081, 69.5945761468, 69.7547279655, 71.737612621, 72.4832271444, 70.6844975053, 73.2479102143, 74.2757903207, 74.0251073728, 72.6113826391, 73.7521518798, 74.51406016, 74.9694116435, 72.2454743118, 71.1529155199, 72.087158784, 72.77217393, 71.778467844, 71.7533884196, 72.736839194, 72.9313807389, 72.3826989006, 75.869437254, 77.6021138202, 76.6294127673, 79.0019216484, 81.4762500799, 84.2385393944, 85.8238219283, 85.5760074495, 80.6270824484, 84.7759731016, 84.0918935393, 81.4937948004, 86.2164901735, 83.1733890063, 83.4503710474, 82.469403447, 80.4361206696, 79.2584155092, 80.0119982236, 78.9468764208, 79.171276713, 77.2525971309, 76.8162765189, 74.2080827849, 75.0750644022, 70.4276889275, 68.889748712, 68.2728662039, 71.2782704572, 69.4696507855, 69.5264757893, 68.8814630763, 68.5369706541, 67.6833912747, 68.7605061811, 71.1359403938, 70.6514105765, 68.1477343287, 67.0681859241, 67.0143174695, 67.3309641758, 68.051288646, 67.2024340697, 67.522050559, 67.7768475243, 65.9401471412, 66.1606463793, 66.9394316429, 68.3787264063, 70.1164009085, 71.5875038748, 69.4863500194, 69.503932177, 68.4593671173, 69.7260909554, 70.3114451756, 68.9902131352, 68.1104721958, 69.6990612438, 73.4661064448, 71.2599777213, 69.8595185982, 69.8563665114, 69.1884587717, 70.6731408565, 74.1189893226, 72.6613288594, 70.601515339, 67.5954381813, 64.8042814989, 64.368869946, 65.030008523, 65.0750925331, 65.2120176045, 67.0617269418, 69.5072301416, 70.0417127449, 73.219968293, 74.4577736319, 78.6334179825, 78.4998247775, 79.4984869678, 78.2933075197, 77.8802690836, 82.1025258923, 84.2673838315, 84.5024079994, 87.9125780504, 84.9027605109, 83.4489526179, 83.6203632289, 86.0516726291, 82.9342348231, 80.5382639536, 79.4315811918, 79.4709527024, 77.833266341, 72.9443818607, 71.8695966992, 75.0071259156, 72.3356105012, 74.8382695529, 73.9867068264, 74.1502448275, 73.3961146984, 74.6866475558, 76.1647130381, 81.3792454538, 83.0898140881, 83.5703481672, 83.3619488417, 79.8434495299, 79.9798284671, 78.7834261893, 80.2016337124, 80.0854233355, 79.5858995036, 82.9467070041, 81.0584297251, 82.3406042543, 82.3497075558, 82.02318963, 83.4218032879, 81.7436225133, 80.6308856437, 81.8953039976, 82.5536304317, 83.8170600513, 82.285337025, 83.445632418, 81.6442593082, 80.8701149169, 82.2632316989, 81.8132870898, 83.3743074098, 83.5245415036, 80.8755582912, 82.641331334, 84.2105682984, 84.5059549198, 82.8742303999, 83.4868755931, 87.0114564693, 85.0548085735, 84.6732648307, 85.3988840053, 86.398073196, 87.635826975, 85.125332009, 86.7850600206, 88.7834352317, 88.7121604182, 90.4957720327, 93.2530966351, 93.7006763997, 95.9122515356, 90.6071562219, 89.6360388581, 89.7689351168, 90.508488805, 90.8024094231, 91.3521511706, 90.8740843537, 90.6114494675, 90.378597497, 90.4905410862, 91.8700449357, 92.0920913333, 91.3769153169, 92.9084047541, 91.9801147605, 92.2725572176, 96.2282955953, 97.6011351014, 96.3048425226, 92.0017330229, 93.6998482244, 92.1516547087, 90.4886979463, 88.7565861076, 87.1598017971, 82.6225983227, 81.0225331869, 82.0096206011, 79.7153256246, 79.2710505653, 80.7829985936, 79.3561148892, 77.4492923931, 77.210016984, 77.5214035384, 77.9476673686, 80.5921028916, 80.4612388252, 79.9060554572, 80.1382417279, 80.9408844523, 80.3270430752, 81.9091714899, 83.4775154585, 82.4026664316, 79.5633067904, 80.5511571044, 80.0485082617, 83.8785852927, 84.0499914594, 82.1064077627, 82.6537411793, 83.8663351885, 80.5428108202, 82.8996714899, 85.6714275061, 86.7391232939, 84.7512994856, 84.7123969168, 81.1873842526, 80.2613181049, 81.3452681394, 80.8831808646, 82.1562199058, 83.6822931961, 85.2977827713, 85.3698398712, 82.9174494353, 80.7415153155, 82.9815591522, 83.7999967628, 85.932085419, 89.1889236698, 88.1228474501, 87.8773812519, 89.5473733898, 86.8021469904, 84.5604303088, 83.7426210713, 82.2049861386, 83.6368939144, 82.2237844715, 81.8154448647, 81.3624534674, 82.867351418, 84.3284800652, 81.3763481066, 82.9182259427, 80.672995694, 80.297248479, 84.7274219803, 85.6342701532, 82.6644946146, 83.9627659672, 83.9236946689, 83.9318005501, 85.3685800687, 86.0838994658, 86.5992794351, 86.1049833089, 86.75811886, 86.7870200065, 87.8954686811, 87.8070648794, 90.0322693794, 87.4410457048, 86.1615654814, 83.9933370833, 86.9096744723, 86.4147198163, 86.4025383343, 88.4553477356, 87.6466679167, 88.3482345117, 86.0620340473, 84.6692035945, 84.6585094628, 82.8138595718, 82.6674980887, 83.341210921, 81.8268587004, 81.8221647291, 81.1626053843, 81.0605562215, 81.4263206798, 83.2503682057, 83.7745917531, 83.4576028874, 83.2552141865],
y: [-0.700740641367, -4.22733500259, -3.34519351254, -5.24047112859, -4.32950676893, -1.73642938603, -2.3381318465, -1.30013798663, -2.34259102965, -4.7097973579, -4.23048596248, -4.10616597806, -1.13721249399, 1.74712441174, 1.80643215496, -0.124705468256, 0.102956881674, 2.64455174559, 7.09865480876, 7.73096240707, 5.28471390777, 5.51769873795, 7.12683622781, 4.50019074477, 2.52413981475, 3.64347006815, 3.61278891617, 6.51152605854, 5.48328245565, 5.40856991004, 8.64836165268, 5.91334066238, 7.16087183589, 3.81874739194, 5.91445517137, 2.73910572933, 3.4407373475, 1.95976785907, 1.56912431386, 1.82004530701, 2.30859612784, 4.71190833401, 4.96312665689, 3.87900776269, 3.6593098265, 1.45670185071, 3.88182449209, 5.39948443233, 3.96718200593, 1.9488183581, 3.9479819188, 7.83451461542, 8.56589803804, 7.7310518376, 8.31775522172, 9.97283206773, 13.2463670971, 10.9945336731, 12.2495484244, 14.0415730809, 16.6293019839, 15.0291460903, 13.0824559956, 10.5367290223, 9.64205800185, 11.0593758696, 10.7153014807, 11.6048402682, 13.2993655519, 14.269770172, 11.8779394773, 10.2044199848, 11.9941296665, 11.6086286077, 10.8771148302, 12.1471584567, 13.7470205419, 13.1859361609, 9.99738017586, 10.8165553423, 13.316755317, 13.7152634092, 12.2107000853, 15.0443797447, 14.6645775769, 12.6720842816, 12.2765703434, 11.5865592883, 15.0386241033, 14.8086388877, 14.38172374, 15.972652947, 11.9502172712, 14.8274167915, 13.8000108549, 12.5763980744, 13.0507246596, 12.8988381066, 11.3192324574, 11.4972312402, 13.2576588091, 11.7783077974, 11.8074163343, 11.1902078172, 9.8321075529, 10.4190490585, 12.1367497976, 10.7340548561, 9.4353144921, 9.84572680661, 11.8166301711, 13.1902267237, 16.531929775, 14.5160183021, 13.2067683804, 16.0587565885, 16.6589947384, 17.775075397, 16.7175319908, 15.8155358994, 15.2291513455, 18.1548696074, 18.8402892211, 19.5398583822, 21.3314002847, 23.7686875282, 20.5097221456, 19.963715331, 19.0940279119, 23.7959290405, 23.731710376, 23.8037280612, 22.168392284, 25.4801344554, 25.1081602361, 23.5406661947, 24.0235635704, 24.4342082776, 24.5569892583, 26.4305318007, 25.4583993882, 25.5850406421, 27.5063348569, 27.1283228702, 27.6272503917, 28.7066009336, 25.2119681238, 21.6129141224, 21.6667734971, 20.2669203931, 20.8963156826, 21.6112416379, 21.0532124933, 21.0271501084, 23.5926488619, 23.7113539633, 20.5972953923, 22.193048598, 22.5631229594, 22.3670798207, 22.7059183118, 19.5075149221, 19.5547584336, 20.9416508807, 23.1327764914, 25.8377240693, 27.4547762178, 29.824991361, 29.2119719658, 30.0751029748, 28.8911085742, 30.3106725789, 30.9537801787, 30.6979288799, 33.6101241413, 34.7156933038, 32.6152141304, 29.9390499933, 28.8718605516, 28.4642004692, 31.0870109898, 30.8146949434, 31.7952399659, 26.6652408612, 27.733688094, 32.4214525586, 31.5027043162, 30.381276834, 30.3311599706, 30.5754512353, 29.4973907107, 31.4015561745, 32.4306783155, 31.8700452621, 30.0377180911, 27.775609339, 26.6830458681, 29.4868611888, 27.850203162, 27.6808277266, 27.949305082, 28.0050732116, 28.3579290815, 27.1917571537, 26.1306135526, 27.9902039763, 26.1612151859, 29.0764431829, 31.621314499, 31.5604653763, 33.6175696154, 34.8852254255, 32.8592301026, 35.5803975575, 33.6883478249, 33.7598123075, 31.4246185388, 32.2457728668, 32.0553366374, 32.1852216477, 33.7094450635, 37.3336470163, 37.5001204632, 36.217875068, 34.4166574493, 35.7019209552, 33.0631107621, 36.7830479701, 34.3503104018, 32.4182960734, 33.0874837273, 31.6697229812, 31.5067589649, 33.5265854996, 33.260232581, 31.9815176406, 34.6105557252, 34.3388886128, 34.0368793254, 33.6522919004, 37.6217247333, 38.1669514235, 40.4074781547, 38.3615992404, 36.1629611723, 35.9671510871, 38.1361290612, 35.8922649915, 38.1512572094, 36.5074675872, 34.4116714257, 31.111860568, 32.5383729834, 35.2397798857, 35.9621849496, 37.5523842005, 39.0982258029, 36.2376156354, 33.5426655784, 33.4427675666, 32.1796879463, 30.8483901618, 28.9933318391, 29.0362960255, 29.083610239, 29.4490072648, 32.1292923777, 31.8902730065, 29.3961270134, 31.9836195384, 31.6268345271, 30.1327992644, 29.2216379993, 29.6910120974, 29.675504607, 31.0756789149, 32.0882607374, 35.0711908, 36.2767191403, 33.9766510411, 32.0225494181, 34.4973538692, 34.5773374195, 37.4277541103, 35.504596674, 35.9273889243, 36.5458670633, 36.0655211794, 35.0428648999, 37.0379878754, 35.0061792353, 34.7827095055, 35.760669295, 36.0640632276, 38.4837054196, 36.2773643104, 36.1001789797, 36.0073696909, 37.3077181, 38.5705229883, 37.4042295093, 37.4460198924, 35.2902469539, 35.601462242, 34.2983513601, 34.8451171091, 35.4879083312, 35.7167921169, 36.490065193, 36.8182577334, 40.4488942714, 41.9675069345, 40.4959269289, 38.5710510681, 39.1212421814, 40.3298431263, 40.0574197111, 40.1668906257, 38.9630904754, 42.9121381512, 43.8760216992, 47.8844760906, 49.672509939, 48.1353811579, 50.7479445394, 54.4067440874, 55.3450281215, 52.1811636149, 48.8631989788, 50.5817919321, 52.8849774277, 53.4643860136, 51.6473538987, 48.9965418284, 46.2631850528, 45.3368321015, 48.2830767987, 48.227357545, 49.516915907, 49.2653158104, 47.6360181359, 50.1431325636, 51.1987588188, 48.9833528519, 51.7966301722, 49.8599379486, 50.5195405746, 49.4937293472, 46.6827494083, 43.1872880239, 41.6743498113, 39.7400824276, 39.7163473301, 39.3089980528, 39.7604110371, 39.7244365155, 39.5095813604, 42.381926836, 40.9419824164, 37.7290971952, 39.2191189819, 40.2914154466, 38.6446692128, 40.0703253249, 38.5069541771, 36.7938469257, 34.3614107684, 35.9538803102, 35.500839439, 34.3653931908, 32.8158290408, 29.2222936842, 30.7686890105, 28.4040666168, 28.5312536795, 26.1965284108, 22.4664646236, 21.3013679647, 19.9829463221, 17.5881209976, 19.6186456516, 17.666502843, 20.3321325922, 19.6052143049, 21.1606141981, 21.226544152, 22.1047296409, 19.8847370899, 17.6545975117, 20.4855890392, 20.7811131318, 23.9645490672, 23.9022683678, 22.076111249, 22.1327357741, 21.5358094603, 20.5454301939, 20.8815304134, 19.5545852842, 18.9487489556, 19.9804235995, 20.9552664912, 20.9991734474, 23.0159732477, 19.645716366, 18.7469848157, 22.773372402, 21.6180201526, 16.5619591882, 16.0826932042, 15.9095629564, 15.4177152362, 17.1511852596, 16.7861675454, 14.6804803501, 17.5389058006, 18.9998899394, 16.3309567446, 16.7445589308, 17.8108075583, 18.0530705829, 18.3260094143, 17.6218193885, 17.628553479, 17.5990205773, 19.9746041709, 19.9943389266, 19.260144183, 20.4791083201, 18.9969208525, 19.4108668078, 18.4259319455, 14.7542145805, 13.9133361325, 15.0420822945, 15.6969235741, 15.1917155805, 14.5554948706, 14.1340096552, 14.2588080213, 15.8725326603, 15.7762382525, 16.3447980848, 14.5692199212, 16.5449929368, 18.233346642, 16.2822191871, 17.1302810015, 16.180456143, 17.6190658156, 17.0400574771, 17.0901759052, 20.1365140701, 20.0968112049, 20.1638651692, 18.5973309814, 18.3838546297, 18.8788272297, 17.5883413035, 17.6763630617, 18.8841176922, 16.4960327806, 20.2475159766, 17.9811059961, 19.0199083998, 20.9844282471, 20.4532805028, 22.451920476, 26.8731608968, 25.5172148275, 28.2824425852, 32.1307085325, 31.2733341042, 34.296973307, 32.7665124741, 30.7742970573, 29.3627066827, 33.8068234405, 33.6282257154, 35.1264609407, 34.0133957295, 36.207499146, 35.8304873756, 33.2039114864, 35.5103705367, 36.840122754, 36.2922703013, 38.407097006, 37.3893274262, 37.5890915846, 36.3775631146, 34.5262331866, 31.7814694834, 26.8532069525, 25.4313270347, 25.3925322804, 30.201410772, 28.5309914324, 30.6139417189, 32.7009242984, 31.7929754749, 31.6160635543, 33.0725106145, 35.6071433922, 37.2381371048, 39.7718933248, 40.6215854061, 43.5802635305, 46.8671846643, 44.7361812229, 44.9218496807, 42.5555334128, 38.9724393267, 38.3208281754, 38.3228697221, 34.1742511636, 36.3028928898, 36.8538353131, 35.0982488485, 34.6325983125, 35.4730294559, 36.4374616557, 36.7406967586, 37.253370556, 35.0144023181, 34.7703415116, 32.3564340407, 31.319200939, 27.8411907354, 30.1206135734, 32.165068159, 33.200585906, 36.3110337077, 38.3523053131, 41.0245234881, 44.0176399777, 48.1018712827, 48.6413481561, 46.3792118443, 48.720885009, 48.1651024841, 46.9311889525, 49.2704955987, 48.7819561313, 52.2185796397, 51.8831607765, 55.2371552195, 55.9413926763, 53.6517496057, 54.4772953217, 54.2748921377, 51.848752617, 51.3608680751, 52.4865507734, 52.7636179337, 52.1726890096, 55.3672096376, 56.0972976478, 54.4637483461, 53.6133703098, 53.1712985541, 54.0265425641, 55.7634565489, 54.5096769969, 55.8926032539, 58.0694995448, 56.0534469645, 54.9102995782, 55.8481369293, 55.9720353986, 57.1619054552, 57.8337308384, 57.261471799, 54.5651324505, 54.8487785441, 53.3555991929, 53.8467519794, 51.81255424, 53.3303021639, 53.9344080818, 52.8830548737, 52.69287293, 51.744189314, 50.7609764404, 49.7335987815, 49.6569398989, 49.6938423712, 48.6514842993, 48.8778956164, 45.9099100841, 46.5975962591, 47.9418625841, 46.7127570376, 46.0396229346, 46.670646749, 50.4428817305, 53.094488002, 57.1518572862, 54.2922383885, 52.1426976397, 51.1399077416, 49.8859092241, 51.3027303967, 51.4069892835, 54.2460519984, 52.7325361079, 53.1686555354, 57.5415858633, 58.0711760017, 60.2641434129, 59.5190444897, 60.6810033156, 58.6183119592, 59.9264633604, 61.3128284876, 58.7140573568, 59.3065514253, 60.4961468039, 58.2816946134, 58.5064439032, 59.585595486, 62.8181050404, 60.8438065681, 59.905363601, 61.458224663, 62.6463256602, 64.3433756259, 64.7761315044, 65.9823533761, 67.9171601341, 64.528432919, 64.1376257686, 65.7718805393, 65.3221164152, 65.3230211651, 63.3273775829, 65.0911693371, 65.126061715, 62.7102452675, 60.847373958, 61.4991410393, 62.432284537, 62.1398030232, 60.8136911433, 60.2559561398, 59.0151333726, 59.8615606151, 56.396068951, 56.8863654071, 58.8782086435, 58.2483313497, 55.6489213181, 55.7191011049, 50.9012183084, 50.8439548996, 49.8376594489, 49.4873065723, 48.4471858245, 50.5612103333, 51.5151020609, 52.9467558619, 54.6413888108, 54.0813529211, 54.5480233494, 56.0669110967, 58.1829640752, 59.6616610095, 60.1568237094, 59.2945429911, 60.5660700305, 57.4948310868, 61.293441506, 60.2266959515, 59.3574992038, 58.1270997967, 55.4882036932, 56.9587217291, 58.3641382398, 55.2394997046, 58.1812156491, 60.7135183312, 63.6496432431, 62.3672861501, 63.9529979124, 67.0465929116, 66.6977751528, 68.5222314146, 68.7038354795, 67.0455156956, 68.4271912486, 69.3039685181, 73.0303791664, 72.0227502463, 72.7424528094, 74.7226267021, 78.2809707848, 78.0702074907, 77.3926222174, 78.5477133283, 77.2777665593, 77.7758244404, 77.7198051373, 82.0069690036, 81.9654877981, 81.4670173169, 81.859762936, 82.1404788566, 81.5444729019, 80.5662916968, 82.2062620166, 81.8018008036, 82.1231001906, 80.3520169868, 80.7056042369, 80.7908196452, 80.3123859573, 81.7481281556, 80.5166896617, 80.1535777549, 83.6768136477, 80.6828687483, 82.7557975977, 83.3451475631, 83.2705088883, 82.1674892945, 80.6846709471, 79.9601986432, 81.0161075769, 82.0119798897, 80.0582990579, 81.0563236049, 81.8780614569, 82.9730408312, 82.4736935282, 85.1259021459, 84.9951099718, 86.3350015799, 89.0801788625, 91.1618770961, 92.0245812291, 94.9099153677, 93.8119943765, 93.6088503301, 95.8466004165, 99.8482695865, 100.38147662, 101.917547766, 102.047441065, 100.220468206, 100.623967374, 100.388544515, 102.958306608, 103.205290748, 105.00650426, 105.014336077, 105.410987873, 105.775481044, 107.763394618, 107.678309938, 106.943756839, 108.619593916, 108.763371838, 109.75021844, 110.650073292, 110.574149081, 108.873326265, 109.323247052, 106.088962552, 104.070390529, 105.777122704, 108.108730226, 111.25955063, 113.636501082, 113.716543809, 111.310604446, 107.444630975, 106.66884291, 105.449898824, 103.875445848, 100.161488187, 98.8995295179, 100.328992852, 98.9014877286, 98.382443123, 97.7004225982, 97.902597891, 95.2516621866, 95.0091319337, 98.4128875076, 98.6493974041, 100.200722685, 97.4620362515, 100.497215393, 100.164009774, 100.668133029, 100.831253785, 99.4347053374, 97.4694190789, 94.4923714117, 93.6346465981, 97.1940586901, 99.2745506798, 100.259419403, 100.381714307, 102.318822862, 104.923174657, 105.262017439, 104.89535123, 102.724932504, 106.885434515, 107.296568113, 109.677372477, 110.244997574, 112.972280061, 113.770689702, 112.447973781, 111.929817938, 109.683851439, 109.729777899, 107.543621393, 107.720007956, 108.383666809, 109.884759957, 109.451061005, 107.119968211, 110.880869888, 109.671317908, 111.685571, 112.068129699, 112.238443359, 110.373235439, 107.13981872, 108.460255422, 107.852363793, 107.962763192, 105.434793208, 104.31450059, 105.659450933, 105.209314833, 101.225949442, 101.38626022, 101.72557437, 99.9749693299, 98.4249757103, 97.0726429857, 98.0850669196, 99.4273482715, 96.7433242896, 95.5238646249, 94.1215445115, 95.2690448375, 94.1455902179, 94.5973552822, 91.4508210957, 91.2633566343, 90.1397536743, 90.4380280046, 88.7336234702, 87.7229250192, 88.5849568842, 89.1040602154, 89.4868187862, 87.5479588909, 85.5565688084, 83.8967949143, 80.3271561616, 81.5367721746, 82.0298796131, 82.9367820762, 82.3484956442, 87.0882571274, 87.664675965, 88.6844548417, 88.7573432478, 89.0599003612, 89.4110912413, 87.9541540988, 86.4281991775, 89.5501094016, 89.6336680743, 90.6144708375, 92.7357008268, 94.668797149, 95.4885615438, 94.8313569272, 91.7990584827, 91.9975438029, 94.3027038624, 93.6946814421, 95.4648550995, 96.4435168654, 97.6794207989, 96.6941401676, 96.6412968985, 97.1394201533, 101.778969087, 100.575470447, 102.247049226, 97.6661633661, 98.0712180542, 94.9227695074, 94.6177145991, 94.2624268664, 94.2742431827, 94.6822975593, 98.1888671577, 96.4703330933, 94.7959354647, 97.0898539043, 98.0912343676, 98.4246615228, 98.6251339784, 99.1031270327, 101.237821491, 100.539437022, 101.143722621, 103.171131881, 102.642090109, 99.9188358045, 103.427464292, 102.194604795, 100.241009447, 97.8488669343, 97.7099690515, 95.4514887557, 93.4573210777, 95.0153902399, 95.0912622925, 96.8290883409, 97.0865910729, 98.4342438514, 99.0261941878, 98.0914537679, 96.4118630687, 96.2441449337, 96.7250885356, 97.8263633513, 102.078578894, 102.358153173, 101.260322329, 100.253639556, 100.09962594, 96.4704670312, 93.3844772478, 93.4465866379, 91.9877303052, 95.1081306581, 96.2118417964, 97.8692485043, 95.6187344165, 94.5624422428, 92.6951390502, 94.7674810825, 93.8314145597, 92.7782697925, 93.3318849959, 92.1822359831, 92.5449501278, 91.4621320935, 89.1184249619, 87.6884074041, 87.5479230861, 88.6184233703, 89.8936065288, 88.3976997364, 87.6289445027, 88.1619767514, 86.9260956198, 86.8496457434, 86.8352328661, 89.4041620719, 88.8870714697, 87.2628431943, 83.4868902306, 82.0681940604, 81.9235987646, 79.9072468464, 79.720871665, 80.7452985326, 80.5317605669, 81.6294487468, 81.0016427656, 79.7308619627, 77.7413311474, 79.5356548694, 75.2984617463, 72.8950525578, 73.8448490243, 73.0749368338, 73.6608636764, 70.3327246889, 72.4464412351, 70.2435433491, 67.5560806982, 67.0133581711, 69.5200988351, 70.5016600707, 69.6441177446, 68.8142210831, 70.9338888156, 67.84331135],
z: [0.713269550396, 3.19989768759, 2.02094286338, 1.45725589225, 1.93178506708, 3.23754362484, 2.04875525218, 1.00363955037, 0.771680134326, 0.00691708381888, 3.55666549609, 2.44753828196, 1.48826210338, 0.0999109695063, -1.14687251901, -1.21445888783, -1.00480412256, -1.97440757655, -1.23499961889, -1.69669684773, -0.988885854872, -1.59555126119, -0.312675881678, 2.67532785528, 3.92165027448, 2.62491380141, 0.85598786084, 5.22107232943, 3.5803933126, 5.13314363408, 2.21903359476, 0.867223229493, -0.518242319647, 0.138830094799, -0.49954374139, -0.174657197986, 0.147878824163, -4.69552982799, -4.76751220426, -5.804678139, -7.48643511518, -10.3492563905, -10.3591279793, -12.1147394286, -7.90367244626, -7.54127853612, -6.71069413119, -5.75530389604, -1.8708701384, -5.10942735863, -8.25912759122, -10.5337511964, -10.0357789753, -9.8496440121, -11.2138471683, -15.4573033007, -13.8442838687, -8.70659473805, -8.65768703664, -8.31426281804, -8.80678748261, -6.6723947917, -5.32251038624, -5.53399414317, -4.72308586345, -5.38207765052, -4.82574354079, -4.22750397174, -4.1913553824, -4.11530359287, -1.88065127535, -3.25813061764, -2.68079142455, -5.73846850461, -6.25766226449, -5.27287879584, -5.83022819224, -9.7523486679, -10.655260046, -10.6978227758, -9.50962461241, -8.55621314931, -3.76801644878, -1.9663402358, 0.947329951028, 1.80033921638, 1.65884445548, -0.206453454474, -1.15656816957, -0.127119521404, 3.68083404601, 4.27517350297, 4.36985278452, 4.32211697988, 5.94482376604, 4.53273319531, 1.52643064338, 0.724481602507, 1.45517069142, 4.89485477104, 5.00138463331, 3.96111090606, 3.58542328677, 3.70573218177, 3.19419231967, 2.13712605435, 2.50640332232, 0.413840711954, 2.22886925206, 0.763870201385, -2.5609733026, -7.5784209863, -5.26465619958, -2.94828839321, -2.37049955149, -0.959761415914, -2.97962609776, -4.3981967322, -3.82341510085, -2.9720818881, -3.93629758922, -2.72678614432, -0.23003225245, 1.41519637836, 3.84856210323, 3.00807429418, 3.57498648763, 8.58248844568, 8.46314598803, 5.55684469647, 6.94086194369, 6.9696042331, 8.07135462329, 7.6304370719, 6.7410037468, 10.2364274883, 11.7000633563, 13.800419933, 14.6765894465, 14.8376962647, 12.7777108103, 11.5679983039, 10.5394261365, 7.07132794116, 9.99815927645, 11.5806555404, 11.0164178068, 9.38763092673, 11.1464261716, 10.8090268125, 10.544651166, 9.04725949009, 7.22452136056, 4.83546785506, 2.0493551028, 4.91449638834, 3.70568663165, 2.48664076917, 3.23705070523, 4.17989486795, 4.94352545035, 2.74957599894, -0.187298332964, -1.52034374481, -0.277351314571, -0.730969790781, 0.181592561899, 1.26718923435, 2.11047622649, -0.4680433463, 1.6699973559, 1.32825465995, 3.65600751881, 5.06320577525, 3.95894438083, 4.203074258, 3.74410584532, 2.67322728425, 3.28739857075, 6.13020601354, 3.80759401456, 4.07257858973, 3.4644934163, 1.84378987031, 4.01781175589, 6.37943399807, 2.5645352514, 5.84851211517, 3.42526236917, 2.12260023092, 1.6663363351, -0.882079207579, -2.57893467664, -3.93112043647, -1.56259271311, -1.00321628212, 0.82271132315, 0.751929074731, 1.59043257482, 2.47601258223, 4.50442769674, 6.9090139977, 6.80305969966, 5.61523249955, 2.07077935274, 2.80365842211, 3.25910541966, 2.21891608077, 2.25061246132, 2.10253382266, 0.679058961503, 4.1078180614, 5.08327417141, 4.1715868863, 6.49035301027, 8.81717389811, 9.65295171185, 11.7413900888, 12.4694390462, 10.1708971989, 10.6328717526, 11.8096683783, 12.5324329675, 12.8749708945, 14.767510312, 15.7941786456, 13.49474075, 10.9523743062, 10.4653979732, 10.9920317453, 12.8632200357, 11.5972194352, 12.5447377974, 13.2314694127, 12.1423078095, 12.069869477, 11.2610155595, 10.925455942, 11.9135263625, 10.2475844688, 10.2915713153, 11.4243727731, 10.421509891, 11.0079559014, 9.66035380852, 11.8155837338, 13.1360278384, 12.7131093517, 12.9228963308, 11.7966534001, 10.3859667433, 10.4019480113, 7.95063915364, 7.00094224343, 5.74773591975, 4.67295734229, 2.06424946654, 4.81329818708, 0.646795720654, -3.35188356428, -5.51998129483, -2.92439245453, -3.76244817089, -3.49855531392, -6.35764865927, -6.80689454102, -6.99911714322, -9.8684589115, -8.19920310081, -7.68682145988, -6.35248843418, -7.26305105742, -9.10108633147, -8.59483382342, -12.0381620972, -11.9587079619, -11.4411964886, -10.642450255, -9.91205834528, -9.25895957812, -7.61678696869, -7.87660238986, -9.49599163067, -9.02421149231, -11.7456497375, -12.9757865697, -12.1588124456, -11.7562283492, -12.5991033754, -11.0999787627, -9.14310727559, -10.8583183184, -11.8833602681, -12.8622138726, -11.8276251436, -11.6316289742, -12.0040703296, -12.4008468121, -12.9867350358, -15.0451859796, -14.1015022046, -13.6352786602, -16.880729323, -14.900701897, -13.3569371791, -10.9477537798, -8.45734086096, -8.27880463945, -6.87492914976, -7.55875594537, -9.55207495034, -10.4339227365, -9.62012496325, -11.1733725299, -12.644444318, -10.5311910742, -11.1973868629, -14.9094648831, -16.261409877, -15.3520033359, -16.7598734174, -17.2636840603, -16.4840886338, -17.0932339147, -16.8917199109, -14.4290393082, -13.5244058745, -14.3440049638, -12.2600550694, -11.5969503055, -14.6470260131, -15.2741635175, -15.6721187161, -13.3055590738, -15.3904415696, -12.3574476932, -10.685457986, -11.2966460728, -9.62261519658, -8.47492130882, -5.80165090805, -3.33912027846, -5.09033404978, -3.68150869308, -5.19181057272, -5.19951885623, -3.70914038985, -2.51539689952, -1.31587120788, -3.90830166654, -6.98877073124, -2.97017586397, -2.86172606688, -4.47417583171, -3.80632192775, -4.9344509623, -0.200198681497, 0.0889976276957, -0.933755338377, -1.33353992062, -1.8826490949, -0.982796259247, -0.826254658206, 2.75094042299, 2.77422461965, 2.36530511586, 0.226501273168, -0.208431566681, -2.59292615592, -5.67622103495, -3.65563620875, -5.4477849094, -5.31910590745, -4.283190924, -3.04107835034, -6.55561692597, -5.49409614565, -7.76297785468, -9.63658747074, -6.81822094932, -6.71223763875, -5.87066954612, -4.43462393922, -6.1701934028, -8.10704049023, -10.4122590491, -10.916085077, -9.5940567305, -9.5271157924, -11.4463756019, -8.81053174861, -8.32935851819, -6.31845287813, -7.21479985279, -6.98025579371, -6.94840908232, -3.15454982627, -3.30177796654, -1.9103696236, 0.213182084653, 0.475927705225, -1.18666457573, -0.482301374729, -1.26442607202, 0.700239477619, 1.19435685413, 5.20118671483, 4.65882364808, 4.52360208992, 4.07110059213, 3.63006789844, 1.74900866652, 1.59125588223, 0.193316607773, 2.48270107238, 0.400294607514, -1.12957411824, 2.42267786219, 3.37274722875, 4.47239911538, 3.62523403273, 2.03621798777, 2.52928129894, 5.39328954028, 3.69136627397, 3.44056967851, 4.96248138165, 3.83596368976, 4.52780077038, 5.20632598181, 5.86602674995, 5.10886432216, 3.58225773547, 4.79916435913, 5.55357349352, 3.28475180641, 2.67203790654, 3.6270763513, 0.816567212407, 3.53427223855, 5.69963648989, 3.37719726454, 3.35803762036, 5.95436109291, 5.49397883214, 5.80083364762, 5.56074562536, 8.4882622107, 8.8185294387, 10.8165481369, 12.1434923804, 10.7075654074, 12.2310410022, 10.7339790926, 9.21025536685, 7.21359490637, 5.80499483128, 5.88206342648, 5.10625291008, 6.06243528461, 6.37554128386, 6.53088891753, 6.6698144435, 7.91177632069, 8.22832670615, 11.5373794345, 9.67516906974, 8.20182487825, 6.36700639347, 9.06671974178, 8.07236683758, 9.06004520384, 10.3601293578, 8.71463547168, 8.97215201215, 6.96131647867, 9.52357352979, 8.47477953132, 9.61930763473, 11.7756909471, 10.6747161121, 10.1850840264, 8.84362348876, 9.13999649752, 10.606978891, 11.875143946, 14.6336001366, 15.6577969406, 18.2954635878, 17.8613722492, 19.0799749585, 18.52345455, 18.5857530942, 19.3244108645, 19.125371287, 16.5142636914, 17.4044823781, 16.8941314286, 15.8871661014, 16.4022481931, 18.8121941146, 19.0956759185, 19.4871485442, 18.2676527338, 15.394784, 18.0345232426, 19.9493062328, 20.4500691547, 24.7676448749, 25.6537552008, 27.5740945867, 28.9678387152, 32.3122006252, 35.1119981266, 36.7719417091, 35.7964035582, 40.1717331232, 41.5164199192, 42.6587859902, 41.2292102645, 40.6463007976, 38.0689557218, 39.1505560171, 39.1398722879, 40.4150802194, 39.7853588503, 39.523874304, 42.2925604942, 41.0286954515, 42.9709141816, 40.9298257713, 39.5103483764, 38.6032818023, 39.0365701011, 42.2270941138, 42.1128579196, 42.7915383244, 39.0273357984, 37.0214739816, 38.4868497458, 40.0145368084, 36.8813944262, 38.0858265135, 38.9782587783, 39.33361195, 40.296978473, 43.049003813, 39.7825746669, 36.9585111755, 36.551943306, 37.2076088228, 35.137265469, 35.1688752061, 33.2931256866, 33.2561919039, 30.5296547211, 29.251183458, 28.7427584713, 27.3209843907, 25.2573282875, 24.7499132754, 21.3804466672, 20.89906222, 21.2391446035, 19.3651603829, 21.8135158062, 22.6425453802, 22.6741822992, 20.4548587288, 19.5967905354, 19.4601918202, 20.4212730647, 22.664429813, 22.2953815827, 22.0391053371, 21.155645216, 22.4143276119, 24.6575277815, 24.6817632793, 24.0469357478, 26.2624170708, 25.593176527, 25.7495770929, 26.8212649802, 24.5388137249, 25.0548028894, 26.1152799903, 24.7513083321, 26.4900657906, 26.0529825448, 26.5903782122, 26.9672068127, 29.0417432386, 29.0203326799, 32.9059625545, 30.4891162117, 28.6887673781, 29.8137979581, 30.8150101253, 32.8010488021, 32.6159940638, 33.5284119917, 34.8061029457, 39.9409709265, 39.3223382703, 38.5645692684, 37.9065737429, 39.3737501674, 41.2617859803, 39.9615428417, 43.5630447026, 41.7880690606, 39.4576723583, 36.3868808961, 37.5269278777, 36.5550306563, 38.7130955756, 39.1925839887, 40.1399106425, 43.8500083793, 42.4031961978, 41.9342669845, 40.4913721211, 39.7067612408, 42.8780983464, 40.8536194989, 44.8467849487, 42.890981587, 41.8438796533, 42.3152223186, 42.1265346438, 43.2471941834, 40.0581710945, 38.229647538, 38.6101991932, 39.531519313, 38.9362977088, 37.6229388898, 38.7731571703, 38.7690565562, 39.3689265252, 40.4106729791, 38.1299461913, 36.7191011934, 38.5328727117, 37.3344437747, 38.7607607187, 38.6690425337, 39.5009492381, 38.8527468824, 37.5988897963, 38.687708733, 36.6461808795, 37.1952407127, 38.5584868481, 38.3957699316, 38.8712492025, 39.8437916754, 43.4157819151, 45.6057828512, 43.2263389326, 41.3247708862, 47.1887651314, 46.5358512606, 45.3113980493, 46.1478980877, 45.5275835846, 45.2026070436, 45.9086307313, 49.8751901838, 49.2895048818, 47.1203475773, 47.2134462516, 47.1756486414, 44.7022889886, 45.6341837229, 46.6977574971, 46.8491395337, 47.9068355181, 47.6420218142, 50.0659318338, 51.5337359414, 54.2470118003, 57.2843610148, 58.8557934117, 59.1548948816, 57.6987585546, 59.6647666826, 61.696611815, 61.7855317909, 58.4077099439, 58.7273238979, 61.1893839957, 63.3406345208, 62.3763505902, 60.7423176929, 60.1630605956, 60.2812494258, 55.7139570528, 55.4843059296, 55.1774510303, 55.0636487688, 54.9897366828, 56.22481901, 56.4042139159, 57.2585056336, 55.9534884023, 54.7470661145, 52.6276907415, 58.4145760804, 55.5946757494, 59.2585477265, 60.4173602135, 59.5846780446, 57.01185203, 57.2044359706, 58.342268091, 58.2622327087, 58.7911452297, 57.0763250037, 56.402307219, 55.18369845, 56.395356364, 53.187925031, 53.7239837083, 53.9908028138, 55.0380952722, 58.6926924708, 57.1012040455, 58.4867905575, 56.1186476536, 56.1380322397, 55.3159646232, 55.3793559149, 53.4573207205, 55.6444397851, 59.307215817, 61.4572960539, 61.6007878665, 61.829723274, 59.3891421548, 59.3766218289, 57.9167130951, 61.3195052318, 63.6612715744, 62.2801779906, 60.8872208648, 57.3367266126, 60.0785614508, 59.3370116863, 57.2757945746, 55.7925029563, 56.739095355, 55.6730556249, 55.7364402264, 54.3722111991, 53.3966311607, 54.3299589023, 55.3445486878, 56.0235003903, 55.2508681132, 57.1042603956, 57.121357502, 59.7251111529, 57.6441302248, 59.2864557131, 60.9068398833, 58.5766464142, 61.1930117791, 59.3478852611, 59.6430909482, 60.5590331409, 60.84790285, 62.0767633724, 64.1918269848, 63.6041103962, 62.5897579145, 61.3299851472, 62.0140192138, 61.9904302416, 64.1240924369, 62.7529107333, 62.3179353428, 59.5046708812, 60.3308115724, 63.0742583444, 61.577165446, 58.5598815692, 59.5026152735, 61.3861986322, 62.6030969169, 62.8438151827, 63.2530614308, 61.5189327827, 61.9486848251, 63.9593434248, 65.7921360954, 64.1126464295, 63.042932372, 60.2788864189, 62.3068053519, 60.2317075145, 60.134691736, 59.6158855845, 58.2365162823, 58.7170102233, 61.6821711316, 60.0797360912, 58.3855633684, 57.584495768, 56.5296788425, 58.9917739952, 56.9870506019, 55.2225155501, 57.2403902269, 60.4621891448, 63.6896961747, 63.9764784443, 65.9590951853, 65.9330522956, 67.286111666, 66.6134925397, 64.2385855352, 61.2107600209, 61.2981902051, 60.7258231851, 59.7909468649, 58.4181601587, 57.7458933944, 56.9379483758, 56.5706071946, 53.9439672935, 51.0013289993, 50.3151424517, 53.4208408009, 52.0094855561, 49.222106317, 47.536834088, 49.1528124536, 49.3913621937, 48.3047260082, 50.8802036857, 52.4884096869, 52.0624913169, 53.0710466165, 51.8488766156, 51.4531846165, 49.7977973943, 53.04690192, 54.7407953632, 53.1115107583, 53.9885389315, 54.2575427145, 52.1460192045, 54.3366581739, 53.768845917, 51.7881595992, 51.3044439541, 51.1485601654, 53.9855243741, 51.4489496803, 49.4336391028, 46.9310048728, 48.7060273792, 48.5880581444, 50.3040532872, 50.9623812631, 52.0017001645, 55.6853165159, 54.1833804907, 53.4494554708, 53.5287673885, 53.5983638406, 54.1678916892, 56.5141903687, 55.0945477136, 58.3584310866, 58.8386143369, 58.086407718, 60.2950285803, 60.014820724, 59.8970534778, 62.0281285099, 61.1735476402, 61.7526577574, 58.018917262, 57.9745324863, 55.2835380032, 54.2946879644, 56.1355265281, 54.8099322345, 53.0105830475, 54.7278344056, 55.9831115304, 55.2735463457, 57.1914012586, 58.8962228947, 57.4155077229, 54.8726206957, 51.9970710354, 52.2393665908, 53.913954457, 57.1308191998, 54.8946986007, 56.6064241107, 56.2233365691, 55.1277650295, 54.2189513325, 55.0629061151, 57.0946910938, 58.2242655496, 56.7289827334, 55.3593785476, 57.3368758028, 58.4084706288, 60.9386777573, 62.4318632296, 62.7095203773, 61.7071974165, 65.9444889019, 67.3209149805, 69.6394598929, 68.465179891, 68.1797446041, 69.367021933, 69.6575424188, 68.0308225294, 69.4027142912, 67.7494019689, 67.9445253646, 67.2008688818, 66.1396054365, 65.9497500969, 67.689043774, 66.4012801458, 66.7425947917, 68.8011729243, 70.3186862104, 72.0695518943, 72.5598688086, 70.782776507, 68.3626705363, 66.1899252547, 67.5676297696, 64.2025577075, 64.8975299399, 62.8567780902, 63.3652600597, 66.6040409843, 64.6287026704, 64.3937457222, 61.798068437, 64.9856091736, 64.558238466, 62.169491675, 63.3155737088, 65.3175722301, 65.8233780405, 66.3773025314, 65.7390712973, 67.9727535534, 69.0420780297, 67.3509700096, 70.9099895868, 67.6959441338, 67.5456634589, 67.5164125252, 66.5738097089, 63.2891002008, 64.1493657769, 64.0586956647, 68.0431056145, 69.3085584556, 68.952602073, 67.146687709, 63.9733912367, 66.8097397535, 68.8802971479, 65.7781268843, 66.8877863534, 66.9545773496, 65.7410622014, 66.2756396853, 67.919725035, 69.1150213107, 69.5127577953, 71.232098292, 71.1480488125, 70.7791003228, 68.8595291973, 68.1562064509, 68.1669622299, 69.1857881491, 69.6571478572, 69.0046503539, 68.6605037401, 66.7753046122, 70.910972287, 74.2199609783, 73.6220263671, 71.8683048803],
mode: "lines",
marker: {
color: "#1f77b4",
size: 12,
symbol: "circle",
line: {
color: "rgb(0,0,0)",
width: 0
}
},
line: {
color: "#1f77b4",
width: 1
},
type: "scatter3d"
};
var trace2 = {
x: [-0.587622718547, -1.03238066514, -0.955447830169, 0.730583372109, 2.93339711726, 4.25361817374, 6.16445038897, 5.27068858708, 4.47131226492, 4.03026160482, 1.49942947544, 2.07997672475, 1.96242415343, 3.67579561534, 3.55998947092, -0.0292525095442, 1.10060876568, 1.22674953221, 3.23155133388, 4.06278986602, 0.583984909082, -0.255810951498, 0.297155422706, -0.999877068743, -1.80319855082, -2.84385754084, -1.82804187703, -1.72620444216, -3.36680611139, -3.75402800638, -5.06720225572, -2.76907488882, -1.49864373537, -1.85871255959, -1.67045620891, -2.9135767863, -2.10622197943, -1.28698047925, -0.393536146303, -2.48258508757, -1.44852803531, -2.39750494465, -2.79833237449, -2.65359401943, 1.00441765535, -0.256225306779, 2.94477768753, 5.41748317161, 3.92015130451, 5.03226377818, 5.40107346635, 5.08430409522, 6.85559588016, 6.41869904681, 5.88064507699, 4.21587975022, 2.54715689123, -0.821870465229, -1.47018982461, -0.12087057773, 1.64462530766, 2.87511491317, 2.95604458735, 1.58568574301, 1.54247932965, 1.72598288802, 3.39962210486, 3.35230054426, 4.86902351439, 6.34668614717, 4.90300530343, 8.59459352322, 7.84827451496, 9.94802455465, 10.2421260338, 10.0172310032, 8.16382364176, 7.3965285262, 9.09484827436, 12.8261855265, 14.8207888353, 11.9666279632, 11.1126019876, 12.1661262137, 9.4809756594, 9.87576125269, 7.40245216782, 5.55428547624, 5.06644437466, 7.09240986166, 7.02205321571, 9.58939931102, 9.75288852468, 8.48563164529, 9.22046555064, 14.2820381388, 13.6638717278, 13.6878062434, 10.375743606, 6.71888430012, 7.02074769754, 10.5986910484, 13.1088946792, 11.5838152399, 11.6776928561, 11.5163293874, 12.4442048178, 12.5026988512, 13.3387267958, 13.6974567083, 15.3344308336, 13.386736946, 13.4294541386, 12.8731013019, 13.4152813912, 13.995101175, 14.6400255305, 12.8330868292, 12.3799479948, 12.7841551705, 14.0710102751, 13.0243179534, 8.64109930023, 8.65233277461, 8.08490069917, 8.69474665607, 8.87335820073, 9.85420780044, 12.0114210513, 11.4072708709, 10.4701888165, 9.94581157526, 10.3882747154, 10.2170612701, 9.70089655219, 11.998066402, 10.5055195024, 10.7326634111, 9.44787989326, 6.04415127228, 3.10128556497, -0.546395923211, 1.30899991741, -1.21224440501, -0.581429826656, 1.40087100764, 1.20165802769, 2.3674063337, 0.511398584763, 3.3981841416, 1.49025172893, -1.07777123809, 1.89459800154, -0.186046025795, -3.22524016254, -2.24377619692, -3.56150784222, -4.07188138498, -1.61573631653, -0.184873004833, -1.82367212261, -2.89528354382, -3.2618625201, -2.58024194554, -4.79118773274, -7.35337503261, -6.19158404983, -4.85993871107, -1.71581639541, -1.84201348822, -4.5703620122, -5.65654789835, -5.27587250519, -4.49315099559, -7.07301044973, -6.75188737258, -7.39505819032, -7.572050175, -9.21679336654, -9.19717062305, -9.02367232806, -8.74689832633, -8.97272456416, -9.08111296777, -8.31566852489, -4.97349019083, -3.01322633465, -3.84834530652, -5.6217183145, -5.66607232119, -6.07895607903, -5.69057911815, -4.84345378563, -5.58975734813, -4.56322115049, -8.87977342407, -10.0749344049, -10.1059647126, -10.9559095128, -13.5906640393, -13.4273256186, -14.3463540899, -11.9677397611, -13.378202929, -13.8342765829, -15.2664906251, -13.9575140176, -15.3767531651, -13.9289609977, -16.8102601455, -17.6253025356, -13.2754598826, -10.3313213229, -9.62813009656, -7.35317558547, -8.00436789974, -10.422544791, -8.30867717168, -10.3560424194, -9.77662674151, -9.10940320698, -5.49392332131, -3.40602887849, -5.23890220533, -4.15612829178, -4.03418266545, -4.53460226297, -6.14137534661, -2.85449805455, -4.67165547557, -3.51608304801, -3.13549037719, -1.63970888167, -2.39458425942, -1.71098604418, -4.16798911529, -7.05666316414, -5.34298796292, -2.85808149816, -3.6925412174, -3.14821183432, -1.8748325103, -0.975788203441, -4.85318146413, -4.70027525844, -5.72058812156, -7.24735021155, -9.52701902916, -12.6967063177, -13.1112031903, -12.354516099, -14.460469141, -12.8035905694, -15.0676144531, -18.3085950866, -18.5501384459, -17.8807182936, -21.1436264144, -20.1036820567, -18.1825393587, -18.6382612213, -16.8660702054, -17.7622966523, -16.0928160063, -17.5775220144, -16.644331587, -15.5598848788, -17.0149562151, -16.541464819, -12.6743744782, -12.5563061213, -13.7573513682, -15.4657813201, -15.3732455095, -18.9331144174, -19.8721782792, -19.3991666152, -19.5363453204, -16.229101065, -18.0865420111, -19.1267424254, -18.4124682252, -19.3834780886, -16.5916766983, -14.1914348036, -11.2812550661, -9.39340127101, -8.78001811585, -10.2240693388, -9.34028823798, -8.00361232204, -7.97600733677, -5.31338653365, -6.11847375757, -11.5057905115, -10.514788302, -8.54512511674, -7.74118402546, -6.09997061368, -6.09791452526, -6.84372107447, -7.80551202768, -11.2547104883, -9.95274827428, -8.41940479756, -5.71379798981, -6.41351534673, -4.58962260541, -2.44515127859, -0.157736534829, -2.5401131128, -2.47182765521, -1.14800500146, -0.165235358031, 0.130112217811, -3.05777276873, -3.91346723166, -4.63213023461, -4.54966309264, -3.80591965896, -4.19980214728, -5.00665834216, -6.35696429648, -6.58178094695, -4.80485709508, -4.57245337415, -4.23369023079, -3.88629626758, -6.07458902192, -6.07059792076, -4.1737707974, -4.62037911066, -6.44782883125, -3.29176697872, -4.02341377982, -0.456146991099, -0.296736250934, -1.11227791612, -2.43009067908, -3.52887935721, -4.87669614678, -5.88875611265, -6.62153923734, -8.3185208786, -5.77650673006, -5.75414931597, -0.763441755773, 0.564831703064, 1.56455991074, -0.72199005731, -1.50695644913, -1.526202932, 0.142948662793, -1.32097027158, -2.01961093398, -1.82091811613, -3.35308617816, -1.94792546138, -4.79265271337, -5.58668995594, -5.78627344005, -5.19488768171, -6.32611169365, -8.82983241894, -8.05247287015, -7.63881162383, -7.57442325109, -8.47896901323, -12.360689317, -15.3523775652, -15.84600334, -17.0290668767, -14.1271527356, -14.3581184151, -12.6711165243, -13.5497100505, -15.4601925413, -15.303086348, -15.2601794563, -15.2622794698, -15.2776967646, -14.5830184143, -17.621942029, -21.5233450816, -23.0709536505, -22.1385466535, -23.7663457764, -26.7283587348, -30.5693109396, -32.8394278254, -34.6568288935, -35.4665020597, -36.219339803, -35.4559638065, -38.876321972, -37.4148280781, -37.0369221286, -36.9484454939, -35.7674792365, -35.9962606802, -35.2865387096, -35.992282725, -36.8283972904, -36.7539983157, -37.484651773, -37.1535547898, -34.8441992184, -33.0983166184, -33.2236666287, -32.2114811437, -33.9660935008, -35.612130296, -32.6826364993, -31.9746784789, -29.3118926835, -30.5946233944, -29.2734790496, -27.1346349278, -26.3343891869, -25.313497375, -25.6030099848, -22.4792551307, -21.053451582, -23.7479473809, -19.5174758009, -19.5408618242, -20.6861631195, -15.366730356, -11.9385905439, -10.6894112563, -11.9486026855, -11.8275930509, -12.1969552535, -12.5017088846, -12.2679217736, -12.299170856, -10.2110224673, -9.74409607506, -11.0049525074, -12.3734641264, -13.1616093854, -10.1660194249, -10.8807849923, -9.56197617938, -9.55400915145, -7.64065140716, -9.11697211292, -7.48628059768, -8.61850324773, -8.886397177, -6.24694662061, -5.6933534581, -7.72847997762, -6.95520044112, -6.07879928568, -6.10094104985, -7.79796921808, -8.4631122144, -7.32729456285, -11.4172073097, -10.0951877952, -10.769674176, -8.06754805743, -6.8607897044, -9.59524775892, -9.3156032026, -8.30339485389, -9.57911601618, -7.27898657262, -8.61909606823, -6.30846538648, -8.64262998582, -8.32695788841, -7.42968999793, -5.74324540366, -3.68817707211, -2.69291843094, -0.811221097969, -2.15341905393, -1.85170509184, -4.64501957245, -3.21637412565, -0.175249310808, 2.15471454201, 3.16356388458, 4.25744843432, 4.08701168486, 3.2316408036, 0.355365802289, -1.19367137758, 0.495914026624, 0.619221841606, -0.440792651152, -0.476326276378, 4.7575817149, 3.62257509308, 3.75750006557, 4.15250919689, 1.15503678061, 2.41435315678, 4.26292034921, 6.07265307514, 6.07839558446, 5.99812707965, 6.90209286943, 5.67494361869, 6.85128286211, 6.41846157754, 6.49406329999, 7.57353256115, 5.43260560935, 8.82046491564, 5.53073293314, 4.89746766715, 5.18743519293, 4.45916979397, 6.03721501341, 7.32116851845, 6.78402538034, 5.28844206915, 8.86375024071, 5.01334483161, 4.8177864524, -0.624567563057, -2.2131014095, -5.04263759526, -5.33924855082, -4.18595385606, -4.80711377919, -5.04175823103, -3.3235833772, -4.70973406808, -2.74104271954, -5.06905761737, -6.03066071057, -5.26553808048, -7.69942953389, -4.17328371821, -5.39126521031, -3.74126695861, -4.10109640674, -3.48206302891, -4.05887558309, -6.6711338665, -5.64849318114, -3.03901862368, 0.964895830215, 1.65299790667, 4.04051631548, 2.33672887238, 4.94606025626, 5.14324311345, 2.16099316368, 2.12616115692, 1.85592707007, 5.8354402007, 6.34330667783, 4.75649172874, 3.01962291635, 3.9694649547, 4.73320026406, 6.93977140981, 7.31496682675, 6.85398119316, 7.40518613701, 5.90688005233, 3.34795522108, 4.83708426544, 2.16617674033, 1.34080726403, 1.26778279532, 0.770494957491, -0.233376296616, -1.36082969601, -2.53218815471, -2.45349313754, -1.08927383818, -0.175501376977, 0.73150387348, 2.37604993943, 4.37752429846, 6.13485933208, 5.62388303864, 8.57104887937, 7.91145841388, 6.18106840829, 9.68604617438, 8.41940578493, 8.38563048652, 10.4491341343, 11.5247709787, 11.3696590381, 13.5956921832, 12.510517484, 12.0721400804, 11.1748934578, 12.6889473837, 9.45581225995, 9.74654821983, 8.57466836923, 7.9930651921, 6.21473116067, 9.14949470981, 9.51456663807, 9.09771672154, 9.47060081843, 7.56147806874, 7.89933395634, 5.93650396174, 7.20490576117, 4.73084584453, 7.60602042541, 8.08323118627, 12.5546006796, 14.4172819467, 12.0788626548, 15.5127509623, 15.9289690387, 13.8897009795, 14.7335017208, 12.5950097815, 10.0620404734, 10.1829723872, 9.60032732437, 9.33170102908, 10.5350583611, 9.97227405553, 9.35865533194, 10.7041343158, 8.99714673794, 6.61644361114, 6.85028117966, 5.05761549905, 3.3252007666, 2.81808296187, 3.58882384798, 7.18453525072, 3.80606305014, 3.7570525163, 6.19632462795, 3.21536122605, 4.91521056178, 4.87363464931, 2.38417466349, 1.69355785584, 0.320581525031, -0.261878961621, -2.14806946803, -0.190761750026, -0.0104743823582, -1.30078517746, -1.63642918919, -0.949279347323, -1.33117011502, -0.0862019939102, 1.3843919289, 2.81649802245, 4.29312846502, 2.88068447068, 2.3624646852, -2.01760898371, 1.13063990688, 2.67065179364, 4.88225442245, 4.07322305986, 4.00336580009, 2.97894233712, 3.19269440481, 2.55974592204, 2.05103242493, 2.99281643613, 4.77391675654, 4.27909650521, 4.7975516475, 5.96693574432, 5.00454954553, 3.86569976627, 5.08607379712, 6.89646349216, 5.38799166178, 6.3609805219, 10.1373979169, 9.22827990788, 8.37898537432, 8.79560732401, 10.1922901708, 8.38554077297, 10.0279807928, 9.65719026814, 10.0618905059, 7.53584670308, 7.20577355804, 5.66910202379, 5.8072433784, 7.3986541924, 5.96489025714, 4.54266969739, 4.5268520306, 2.76483641141, 5.59381968996, 5.7632645058, 7.82157415967, 8.91361817209, 11.5680974679, 10.465772765, 14.3977670138, 14.1878989393, 15.8657371114, 17.403760018, 15.2818342517, 15.9148400502, 14.3663020743, 14.2038073517, 13.4352572144, 15.8603512639, 16.7102459986, 15.9234741699, 18.4105207305, 20.0544437011, 18.7712566269, 17.0265053173, 13.5041462184, 14.3562145869, 14.8071478462, 11.2023484691, 11.2303303037, 13.1165233001, 16.3808437636, 16.5707139775, 15.2966790554, 16.7947581555, 14.1852464456, 12.8622078699, 11.7352147152, 10.6176419391, 8.53563942309, 7.21836810421, 6.70800165946, 6.48842304844, 7.11910261846, 4.02244317921, 1.75396913011, -0.12985291456, 1.97340351665, 2.23921947111, 2.27476080473, 2.20716784128, 2.46500117472, 2.19002723064, 1.00825347172, 2.89346764817, 2.34200992877, 2.90391059757, 3.18832246592, 6.66605696703, 8.20531041504, 6.59013002324, 8.89040051354, 9.97807531418, 10.5588697932, 15.1206682904, 16.5158365219, 16.290774491, 16.6566396816, 17.2959520341, 18.7961433242, 19.6648926179, 18.3395659472, 18.8410104879, 16.3919160473, 18.8733434872, 16.2995805921, 14.3254190885, 11.2607881049, 10.2676635964, 11.6778373641, 12.7697508212, 11.7448932461, 10.559855338, 9.42549000203, 7.2195471576, 11.0939199884, 9.40150301371, 11.4129710967, 9.5769691667, 9.08885404098, 7.66973844883, 8.62085097154, 8.6774711041, 9.29977466863, 9.52833119515, 8.53703839563, 12.0827157671, 9.23054081039, 6.19270144188, 7.04487376465, 6.8752449567, 7.35530886682, 9.04808314751, 10.4900082037, 13.4151725783, 13.2563656954, 14.9931869238, 11.1543404591, 12.8615545847, 11.0768501825, 13.8070680177, 13.1482275388, 11.3369487963, 14.7420652971, 15.1449216183, 15.4532819597, 13.8116831555, 14.0326462239, 14.6250351888, 15.9938183505, 16.0783171095, 16.8976263333, 17.3912413016, 21.1183352593, 21.3653372964, 23.5102814603, 24.8337793941, 23.6979679831, 26.0077630111, 23.5790513828, 22.191914898, 21.265067148, 20.3969849312, 19.316483068, 20.1838897693, 19.9555379172, 19.3178922402, 17.9857253016, 19.172939364, 20.6579882984, 20.14985553, 22.8704139129, 25.7259540552, 26.3312980887, 27.2021062673, 27.0797163172, 29.3864221151, 28.1472225025, 29.0284770764, 29.0840553784, 29.3509411325, 29.3278079082, 28.7158598529, 26.9097266649, 25.5213735559, 24.6735530245, 24.52128381, 25.4553149501, 23.3899235642, 24.4285307302, 26.1888469628, 28.6737977446, 27.668190657, 26.7694846344, 28.2171451071, 25.0394270128, 24.2427151, 23.0268131234, 24.3632373373, 28.1616360661, 28.1811077312, 30.001719258, 31.5104865014, 29.8207787661, 28.5431441404, 28.5599715053, 29.8834907119, 26.4282336417, 27.924839793, 29.3803318688, 30.975003224, 29.3667545352, 31.7382541234, 31.0306808614, 29.7549997483, 26.437619405, 26.6676740453, 27.5584596587, 26.8090049107, 25.2013494694, 25.5994590549, 26.2781342142, 25.156911776, 25.8864658654, 26.5001187657, 26.7682768265, 24.0680723242, 26.3581082267, 28.3759974086, 26.3571311351, 24.8836229061, 24.1942019842, 25.0405714918, 26.4344757564, 22.8640938676, 20.9652364153, 22.961569134, 20.6011148444, 19.3089923931, 18.3435520902, 18.647451788, 19.2829707748, 15.393051431, 13.4297305421, 13.6553556869, 12.4935065563, 10.9408639711, 12.393430513, 9.56983891574, 7.01805452191, 7.8915948617, 8.5047800199, 9.73730575231, 9.14001309692, 8.55028228328, 5.8400379338, 8.00342308836, 9.32868436714, 9.46237269952, 6.73599995904, 9.52393510073, 8.1535137279, 8.92334037879, 9.28893097486, 7.2723246035, 4.23999509784, 3.74313714697, 1.68513665067, 1.05146826795, 4.56302618765, 5.39751815881, 3.41276813847, 4.6272066743, 2.8765233073, 1.63205154353, 1.07855042025, -0.404553879129, 1.34538650974, 2.28308666732, 2.35038401011, 1.24618014858, 2.3542346423, 3.19810771172, 3.58174812069, 4.45431039112, 2.28386873392, 3.89338119358, 2.97426075015, 2.00730022231, 3.26298190084, 3.13728763879, 0.467766417577, 0.0959793654297, -1.49813544286, 1.97030055717, -1.17517052292, -0.730399671856, -2.32637831183, -2.45042589121, -5.88908815052, -6.45387975786, -2.01100524268, -2.52541501613, -0.584418357044, 0.484651768388, 4.95383998637, 4.29110262373, 1.82997779472, 3.62798476261, 2.70815934561, 5.92750983133, 6.32014713218, 10.0427710312, 8.57418652572, 6.13007921883, 7.30410191425, 6.09951099905, 8.83502612707, 7.84329099165, 9.42853550561, 9.66671922245, 12.080822031, 11.6324624949, 7.98788455546, 6.64079989096, 6.46228552094, 9.10775878785, 10.0311000074, 10.4379822881, 8.78764710938, 10.7592644039, 13.8103663351, 13.9162187345, 12.6579494789, 14.5954789162],
y: [0.277992933649, -0.426548360652, -3.33327472981, -2.83388599166, -1.07204928915, -4.11682750529, -4.18179184992, -4.45210951393, -6.04272826232, -10.9173322109, -8.44475668069, -9.98224666218, -10.9864509939, -11.1367895139, -8.34505714401, -7.3733941904, -6.96239443014, -10.0858972497, -9.69905917401, -9.83831278124, -8.91073254762, -8.55813827287, -10.2818828078, -8.73434433612, -5.75600711417, -6.11680238588, -9.68211473606, -9.82968990632, -8.07034284665, -10.8279128846, -11.9669972335, -8.50669694387, -8.07058306606, -8.73887967311, -9.91144133336, -9.04553096748, -9.61800248883, -7.69649987961, -5.94363142463, -8.6189664572, -12.0134439998, -15.0739028608, -16.332781991, -13.4234152737, -15.8849980413, -14.8372656872, -17.4089491368, -17.4321215795, -18.1829485851, -15.2292324489, -17.6049794748, -15.4047631724, -12.7746440025, -15.0776175485, -13.0598173042, -15.9692914179, -18.9809123743, -20.236432359, -19.7144827567, -19.4211747268, -22.6383146731, -19.6687421755, -22.1106161766, -23.3836755293, -22.8833506138, -27.1132978085, -24.953279407, -23.0705179117, -23.1547466291, -21.4380411334, -20.1561431993, -16.32912709, -14.319654764, -16.1822778635, -16.0129841595, -12.6261571296, -12.6964330746, -15.2038876029, -16.2324914691, -16.5299920234, -17.8691382632, -18.161943325, -17.8753867622, -16.6218202681, -19.8441640518, -20.1022162633, -19.8034885712, -17.3579651975, -17.4212140387, -19.1199067516, -20.2502291742, -18.7410348568, -21.0427338931, -19.1550540794, -19.3400295076, -20.7160511279, -21.9513342605, -24.5419895015, -27.8659639985, -27.9892825396, -27.7988714764, -25.7189580526, -26.668417305, -24.1955921389, -26.8108105131, -25.4643558794, -27.4143962581, -28.0749143452, -28.3019575316, -27.394571469, -28.3120660188, -30.3855504475, -34.085968785, -32.7550343265, -33.6509692201, -33.0581745319, -30.903320933, -29.1125213501, -31.2031860145, -31.0853866059, -29.7931274542, -31.4913821288, -30.4010277394, -29.4523821331, -31.115187663, -29.6000581846, -28.3295482957, -27.5592738345, -25.0034149063, -23.2520009623, -23.8146258675, -26.8701243196, -26.005657159, -26.4354618722, -25.2978693506, -23.5809710929, -22.8053494465, -23.5004865062, -24.6448053694, -21.5183301865, -20.7906421199, -22.0361896695, -20.8746767647, -21.0182483015, -19.8837615999, -22.8262006854, -24.6853664249, -25.0402534059, -27.4004904638, -28.6668027489, -27.7413082009, -27.6227854134, -29.073497947, -33.2314409816, -30.3318521795, -33.0982091203, -36.5661676674, -38.1554030356, -37.9062521976, -38.2693352845, -39.1109184448, -37.0493471071, -36.7692700289, -34.9475295552, -35.9674383532, -36.5778881992, -37.5122598028, -36.6070801443, -35.8053226832, -34.566036577, -34.5460632432, -32.0586131144, -33.859834062, -33.2394817465, -33.6413899465, -36.2436131787, -37.5733641889, -38.7235997579, -40.2690540837, -39.0036517737, -38.7679647972, -37.1017743119, -35.3110854417, -36.1314478833, -36.8432587837, -37.6053065542, -38.4859378892, -38.1327073312, -37.1383434517, -36.3093149002, -35.1590544895, -42.0693941263, -40.9696116162, -43.1038244593, -43.7861780583, -45.9047806532, -47.5282918605, -50.3781151719, -47.0242373635, -45.2474787152, -46.8937996138, -45.2164706558, -45.7353855719, -47.0656500413, -46.1844883177, -47.1451492722, -49.3713264197, -49.7802064693, -49.4286039286, -47.5828412554, -45.4563006049, -47.7801875929, -50.9682015807, -50.9332036058, -49.8610718442, -47.8096413889, -47.8597853824, -47.9408609451, -43.0625995502, -45.4748419613, -46.3615845772, -46.4709412721, -46.7375372297, -46.6391487923, -50.4106750875, -50.9261177031, -49.5604486214, -49.2874739476, -49.1019038444, -48.6638732682, -46.9688090376, -45.4997542975, -46.6017993229, -46.051787436, -42.9805726614, -42.421368503, -40.6331648674, -39.7085768732, -37.6550357662, -40.461722089, -40.3822956688, -39.9465439579, -36.7884630463, -36.4522176923, -36.6642090608, -37.5621078539, -34.2869213954, -30.8685899537, -33.9252135408, -33.0258165267, -31.2760981432, -32.0993702116, -36.2036884868, -36.1155651651, -40.1015591978, -39.9888714239, -40.2223281789, -42.7239484969, -39.8860227444, -41.8306522813, -42.3117443075, -45.3477718803, -43.7327822401, -44.6126082556, -44.5448642256, -44.2455343523, -45.2967947517, -43.7535546018, -46.6878720166, -44.1684739897, -43.8194883795, -40.6222044637, -40.6340085453, -39.3868838335, -40.7297168455, -44.0111919798, -46.6728465759, -46.4781237397, -43.3759721353, -43.3832779728, -41.8536372001, -42.0916992413, -42.379433144, -43.7805893502, -44.3146850576, -43.1747370359, -44.8670337073, -45.3590452202, -46.3546316928, -45.8199443763, -47.3604253245, -48.2553975225, -47.560141193, -49.5036613653, -51.2428881686, -51.3021252344, -50.1454876939, -50.5275697169, -50.2370399763, -49.7508183705, -47.991614682, -49.3508773332, -48.090387142, -47.0778186706, -45.5864263612, -44.6271240949, -46.0989128278, -43.3134118773, -43.84390366, -45.6229942367, -43.0450823305, -47.8315431968, -42.7188344659, -43.1630988612, -45.5114984984, -45.9805296747, -45.1991838046, -41.9480853443, -42.7566734777, -40.9756146918, -42.6372847341, -41.0603780498, -40.1604500015, -41.1331559156, -43.7537664006, -42.3168365829, -40.5933541578, -41.3566988111, -40.0502423255, -37.4511275242, -38.1054831839, -36.9361330328, -37.3298160971, -33.4187081389, -30.558221148, -30.2990733558, -29.1349260025, -29.7280651484, -30.1738139452, -30.7310211626, -29.9688944984, -31.0718485226, -29.2969481057, -30.502375716, -29.9755221507, -28.6245996037, -31.1520392109, -33.2443087815, -33.2633424659, -33.4702616445, -32.2566683213, -33.0697204092, -31.3554568046, -29.7281899549, -26.7537615685, -29.9311260621, -31.7602229635, -29.5160595878, -27.3990479993, -27.5039735368, -29.1204913825, -30.0962943017, -28.5849850478, -28.7916966415, -30.8341216171, -27.2215796419, -25.1416188834, -23.6117863864, -22.6299813145, -23.8151775177, -22.1012386033, -22.3598710977, -25.1051045327, -24.3333921679, -22.7562455346, -23.3035887808, -23.4550183039, -24.9047594564, -25.5316445865, -23.2587640093, -23.9668017797, -23.1178251342, -21.3112611969, -18.3302634481, -15.7386702831, -15.2440260079, -16.1086559272, -16.0782081432, -16.3413024453, -15.3682367563, -14.9783090437, -18.163761023, -17.6934403746, -15.7571629895, -17.3670716762, -18.1631639802, -20.6886706647, -23.2067701319, -20.5314534507, -19.305705723, -20.3965955515, -21.0966980213, -21.9955108942, -21.0613571637, -19.4293839011, -18.9480476305, -23.8842133619, -25.8882913894, -24.853908524, -26.4389724003, -23.7094594441, -24.1795191918, -20.6449444215, -25.0967240874, -21.9527394067, -23.866291876, -26.6402249938, -27.005218177, -24.8288474553, -23.4976023555, -23.30232567, -24.3659039992, -23.2698523385, -23.7157262864, -23.6450605643, -23.400018254, -23.5487321392, -23.4168231787, -22.7062672403, -20.4304642927, -21.2334030016, -19.6853775481, -20.3700711734, -23.0871941478, -24.1446353104, -25.4031759026, -23.4245157611, -25.3991966751, -25.4292695078, -25.4008030702, -26.4055242475, -27.3934805529, -27.502503585, -28.811599379, -30.1627959839, -29.7428357216, -27.5205912565, -22.5594276816, -23.7768639098, -23.9323159871, -26.630975483, -21.804000689, -19.7784480084, -22.6720968203, -21.7531369261, -24.1683935654, -23.8008178784, -20.9538516808, -20.6709596615, -20.9922760339, -21.3733256128, -21.5726571486, -22.4171793632, -20.9433863001, -20.7097604739, -20.2008146074, -20.6404065631, -19.8338614398, -19.7005401409, -20.9992075502, -16.9931949842, -16.1047115205, -18.0711208408, -19.7088316779, -19.6657209063, -20.2530265987, -20.837218629, -22.6319886357, -23.6058683202, -23.8211079657, -24.3213938019, -22.5562496182, -18.3198047759, -17.0776304637, -16.4200213459, -15.6217606993, -18.9556991542, -19.2159575424, -18.7705513916, -20.4932419871, -19.8949332138, -19.742226496, -21.5811535792, -24.4381305635, -25.7045057497, -24.3478173931, -23.9972593967, -25.0853874529, -23.2072476013, -23.370356789, -24.7930427333, -24.9149670177, -25.592077396, -25.7678438652, -24.4599631305, -24.4789827949, -27.0473648959, -23.1314134732, -24.1192850617, -24.2697170594, -24.682270372, -26.3714223313, -28.9963249609, -28.8727502967, -29.132649234, -27.1994355611, -27.398261512, -27.3548529881, -25.5491705793, -24.4543509964, -24.770560897, -27.1406687351, -26.7786023629, -26.9515450437, -26.3602594594, -27.0780604116, -27.7844659747, -24.774806751, -24.6383705947, -26.750532996, -25.6790278335, -24.6436270735, -20.9564251952, -21.3235856896, -19.2017706665, -19.0945890502, -20.4035535871, -21.6454714912, -19.5638504856, -21.0176280246, -20.3520146786, -20.1761818343, -17.9876623932, -17.9989996374, -19.8592978129, -18.3306455702, -17.13544312, -16.9566655679, -19.6432822509, -19.729346535, -19.3611553263, -18.8530081538, -17.7109363586, -15.3592508679, -16.0578751503, -14.9389584555, -13.226361236, -12.0745226454, -9.74029432358, -9.73674257829, -8.77337250411, -5.82082454039, -7.07851791022, -10.0900860759, -9.34336773514, -8.87007888953, -6.93938702325, -9.30374727633, -6.22644539959, -2.84963634726, -1.63091237203, 1.15895792139, -0.140883672669, 1.68220351588, 3.28843914461, 3.85387311714, 4.28564250081, 8.04115381897, 7.90300957946, 7.70604146433, 7.10518776351, 10.2125930892, 8.59206282251, 5.85699903394, 6.64572021669, 4.57486066116, 6.43682191136, 6.9715252758, 5.31821766985, 4.82245503732, 3.78801481303, 3.90456256646, 2.23612585467, 4.0986225393, 1.82654710509, -0.661504127386, 0.670910598631, 2.45737253165, 5.05535113607, 5.974326582, 5.88383410252, 9.36457687391, 6.96866712052, 6.22439098019, 5.84353049452, 6.09010463816, 5.28401735614, 3.87564029345, 3.7704991349, 3.0678700936, 0.970516843068, 1.49380243233, 2.52051447694, 0.583971959133, -0.440355559553, 3.20047058896, 4.45970013189, 4.22626861431, 5.61398155093, 5.4763215808, 5.31482234537, 6.52031281807, 4.32207449638, 2.88508638774, 0.818939700869, -1.5518524976, 2.97765112631, 1.62345404386, 2.92614116825, 1.26958222481, 0.884130896766, -1.10699198704, -1.66046286622, -3.66220137425, 0.0550736987221, 2.28863776616, 0.722453874388, 2.89700890835, 2.44468410965, 2.48482440769, 1.25882112807, 0.678002169046, 1.36713189402, 0.199537401497, 0.718218901267, 2.59817288918, 4.44523999801, 5.30361474913, 3.67843585839, 6.56210557773, 6.65444435262, 8.12448513406, 5.35076671274, 3.01008913655, 3.10415711031, 5.24567801563, 5.73458279238, 7.35453727424, 10.0887520002, 11.7038693686, 10.2211941143, 10.1330908799, 8.78628733933, 8.40897813042, 7.96741204425, 3.81039189649, 2.28394498352, 3.80922711081, 5.10033714632, 8.89613076055, 9.18685412039, 9.88545289574, 10.067556167, 8.5286184704, 10.8250811614, 9.21823413131, 7.55490352057, 5.57983040882, 5.28855912023, 8.42833101023, 5.68937916182, 5.05650214775, 5.46535618699, 7.11823604828, 6.79272866043, 5.75393961228, 6.45874354071, 6.97847758579, 6.1524662991, 6.31114227436, 7.79423742085, 6.22711437579, 6.59340550621, 6.63482636833, 5.6861707667, 3.90061102969, 4.91778736406, 8.00458687301, 8.98288710471, 9.53877057175, 8.65996217326, 6.7318138724, 6.17204322576, 8.09515647502, 8.21886177631, 8.90370598032, 10.5862458317, 9.84006420822, 14.6497824735, 16.1265761028, 14.5634793433, 11.8220622664, 10.1400666482, 9.19151333252, 8.42955431702, 7.38265314439, 8.64458594487, 7.80610177354, 6.54051146393, 4.52499893349, 2.08500288547, 5.99886271284, 2.96016000432, 4.13710519849, 3.8043789621, 1.99299122456, 1.46314095033, 2.93882832894, 1.49004920016, 0.476364941288, -0.741762113444, -1.46591287165, -1.35374453298, -1.84426417484, 0.399574181799, -0.0384260038311, -0.785164594909, -0.841588921067, -2.09838868499, 0.676670503702, 1.87719578624, 2.41403974535, 2.49920542414, 5.77877223273, 4.77441912944, 1.85488501597, 3.43888138157, 2.23273857399, 5.10514890823, 1.97570678117, 1.94262722999, 1.98188493069, 4.27170133232, 6.11149357536, 5.9014286271, 4.24482481922, 4.17263556859, 4.53839516921, 3.95971045797, 2.5960160566, 1.29455326957, 2.05978492559, 0.180486737195, -3.95319207358, -4.58038468738, -3.6205778294, -5.8227441474, -11.6308385485, -11.9407357884, -14.0684271666, -13.9340695681, -13.5762987816, -14.0392061898, -14.3737397178, -15.4061092794, -15.0721834978, -12.7313269076, -13.8867698367, -13.6874274623, -14.4205118401, -15.9881561098, -16.7535940776, -15.0170271432, -14.3644835867, -14.6517736094, -17.373759489, -18.3470249739, -21.0306324527, -21.9357277902, -22.1295296203, -25.1482249465, -26.9797357278, -27.8090543411, -29.0843698669, -29.3634428484, -31.6670671478, -29.2235323616, -31.2593149334, -31.0265157441, -34.0918485783, -32.3151517829, -31.3749911926, -29.6136748425, -28.8709717552, -26.5484691553, -25.9818720961, -27.7745878933, -29.5042749503, -30.1765666666, -29.7128125183, -27.587879205, -29.7364411353, -32.204085035, -29.869805823, -32.0820259772, -31.9204546955, -32.9100718122, -30.6906947598, -29.6327900974, -34.6239694626, -34.2846871966, -36.3548076205, -37.4086755948, -39.2081844297, -38.7419220124, -36.673599457, -32.6421799799, -31.1641592537, -34.3005495012, -32.0312724363, -30.5034753006, -30.5635206199, -31.4974123094, -31.4334469323, -32.878924448, -28.4587323758, -28.0970920978, -25.7142478007, -26.9828018072, -25.6042182527, -25.9202064819, -24.6926653477, -27.3310685222, -29.5919172012, -27.4265745377, -29.4557641895, -28.4516920544, -25.4999514743, -25.5310868578, -20.9876757699, -24.1296474716, -23.3997125844, -21.2685383653, -21.2091721072, -19.8047425476, -21.2956540682, -21.2628166465, -21.2168551711, -21.9334614285, -23.3956236264, -24.7431154058, -23.4171544243, -21.4775683151, -20.4583221021, -21.3219261928, -22.4414651673, -22.0002757988, -21.0644828019, -20.1537986092, -18.7750901194, -15.6183884423, -17.3692874139, -16.3772911147, -13.5751102765, -17.099029361, -19.862370757, -20.936749715, -21.31155576, -19.1949163998, -16.0551280695, -18.9148244013, -21.3204109061, -22.1184259034, -26.1544782193, -26.8051450189, -27.8481000756, -30.8348099035, -31.2125214317, -30.2126113496, -30.8419711704, -32.4502484974, -32.7541756605, -34.2955253436, -37.1002900888, -37.4019915959, -35.9329161454, -36.3620217121, -35.5005247309, -36.2010080591, -35.8661666813, -41.5905394347, -40.8467607144, -38.0812848416, -39.4427652155, -39.1299314942, -37.1496613623, -34.9686391874, -33.7667549057, -32.979040438, -31.4457316057, -35.8508454292, -36.2004404068, -40.866975857, -41.7852717472, -44.0863542007, -44.7960848652, -44.6505169208, -40.6327137221, -40.2951264126, -39.7222584991, -36.7097352915, -40.3613042505, -41.9677024383, -44.6294279674, -44.2365250373, -44.4038709397, -44.9179398778, -43.6864069462, -41.2584608768, -42.9919052884, -40.3348647317, -40.7608940881, -44.366543627, -44.355405057, -45.9412835032, -41.9519761908, -43.3977789544, -45.0845109232, -46.6785829299, -50.67270829, -50.8796515979, -48.6068119787, -51.4954413525, -49.8611134564, -54.0404571519, -56.6052965887, -54.4089466393, -51.936210785, -52.1712162415, -49.3980794574, -49.5780442897, -49.7083853594, -50.0086230389, -53.150475046, -54.1328174984, -51.0141848777, -50.387038848, -49.34390607, -49.498202854, -48.4400818352, -49.5103968225, -48.9124171878, -47.6117277507, -48.6410391872, -48.5331563415, -48.835701848, -48.8489706733, -48.7133296807, -50.5262313803, -47.933690495, -45.7329752432, -41.9828313149, -42.7208343888, -40.8651694736, -37.1250809562, -42.3835819278, -41.0511782746, -44.0597345413, -42.0473900435, -40.2938663523, -40.3409215424, -44.1046323219, -44.0637388006, -45.7292323337, -47.9856532427, -46.2224866416, -50.2746760332, -51.2156612867, -50.5610929478, -54.247302019, -51.4834083954, -49.2812690285, -48.4563570043, -49.1428330473, -47.3631942998, -46.8824626252, -45.5502079351, -42.1794275239, -38.7266044151, -40.0544750795, -44.4296416466],
z: [-0.759881220645, -5.40429290197, -7.12660610955, -10.2886735655, -11.5012062505, -13.0858438208, -11.7202444772, -8.50247816131, -8.02821031479, -7.41209846217, -6.26831949247, -6.45870852842, -8.13122913464, -6.30754902855, -6.54749119421, -7.26990482893, -5.14144549274, -5.51207416768, -4.39925367038, -4.50173491545, -4.2759669067, -1.54682923346, -1.43517539548, -1.20271277786, 1.23060070007, 2.32265509018, -1.23608555421, 0.640706099942, -0.950344448851, -2.96952321322, -3.07630821548, -1.74201730381, -1.36251197359, 1.07740821931, -0.508534210601, -0.688997641361, -3.15755034188, -4.33833086821, -8.2563234128, -12.8910011058, -16.6627268279, -15.8064375887, -13.8430122478, -12.0974271601, -12.211365824, -12.1170005215, -10.107803556, -6.70853258294, -9.59386544458, -8.5831985326, -8.78981880888, -6.39457763724, -6.56602581666, -8.51306955061, -7.50998261532, -4.88734355455, -5.28150105773, -5.10355743906, -3.85106180213, -1.92380780462, -1.78662268047, -0.940701670047, -1.14901020898, -1.06038827716, 0.276085567896, 1.66030102571, 2.72243124598, -1.04010769383, -2.89646238066, -2.08215649508, -1.66673926228, -2.47743406283, -0.977962713926, -1.22333272887, 2.86705402552, 1.40660438621, 2.98045131601, 1.89101882008, 2.40367733569, 2.20248772631, 0.330520429255, 3.36118309249, 4.90287957618, 7.9317976682, 6.5555653371, 6.37427742033, 5.34426999408, 4.65652540203, 3.29087310203, 1.77360818718, 1.14513384529, 1.81507097286, 2.6373463424, 6.68095576307, 6.13922112462, 7.11940859157, 5.00430741348, 5.02553802953, 3.63985425901, 5.34798908244, 4.82239421183, 5.87224308925, 9.49887815617, 10.7760797343, 5.66775229527, 7.77081146222, 10.2781936027, 10.5458752284, 10.8844388563, 11.0402205162, 11.049917247, 11.4909849163, 10.314096627, 10.8364605095, 8.96581331256, 9.4280196166, 7.51524554384, 6.74966461487, 6.90586314967, 6.74342383015, 8.83345670765, 8.43192939185, 8.73846332746, 6.37838366692, 5.32349512868, 4.89691941318, 4.99683189307, 7.05422188867, 7.47993259892, 7.66867557673, 10.0392102219, 11.4311036295, 8.46172597692, 11.0569312529, 11.0073235388, 9.67968557731, 11.7783278772, 13.5878512141, 14.711199337, 14.7523724556, 17.2644394552, 18.0016315662, 18.6352039704, 18.5061505443, 20.1240581401, 19.8618582909, 19.9841826312, 18.9081841015, 19.1722746958, 17.0307168546, 16.103542817, 18.0413277328, 16.4510040051, 19.7812719424, 22.7340613429, 23.2500187421, 24.1765183475, 24.6336857452, 24.228894593, 25.9299068071, 23.9547503886, 23.8333827489, 25.7103002994, 27.5694974426, 26.2221003245, 26.0928747444, 26.3753162859, 25.3385489471, 25.3131401019, 23.5421321244, 21.6193396246, 22.0824038379, 25.2808396625, 30.4165335131, 29.2808509276, 32.5974648565, 35.6869851098, 37.0218861908, 37.5560789922, 37.6413091663, 38.378573334, 39.7087106962, 41.2637766421, 41.0492971522, 42.8058213266, 45.3313921517, 44.6989221679, 47.8248326108, 46.3044916613, 47.9994046061, 50.3785521908, 49.921002473, 51.8585341447, 50.8104430501, 48.832059118, 47.4729075774, 47.1920733699, 49.620472404, 50.0514039375, 50.3891825185, 51.4246865941, 53.1865579013, 53.9742241066, 54.8113526404, 54.1962738145, 54.409051824, 54.4978349236, 55.1537290666, 52.2434136799, 53.6913765295, 54.9792818882, 56.0858105601, 57.6681108505, 57.4448039576, 57.6400366108, 55.9865635209, 55.2309521465, 56.2710033321, 56.484274491, 57.5911025374, 56.8279630881, 56.5089496041, 55.345377578, 57.6407974753, 54.8205047246, 55.4695241087, 53.5399987778, 52.5112810158, 49.3350747079, 45.2893100181, 43.4066796665, 44.5240181725, 48.5439369495, 49.4592550947, 46.6887363445, 44.4829426524, 46.2564023008, 48.4762093333, 47.0901602707, 49.0500848138, 49.4352292035, 47.6749413654, 45.0158465498, 45.0526713599, 44.8903758946, 46.7779403366, 50.0715223404, 51.4567423269, 54.413770784, 56.4615407369, 54.674168105, 54.7343242723, 52.6285308934, 51.1188248591, 50.0524256094, 51.5399958913, 51.5410681996, 51.493649325, 49.5810470711, 51.0828077773, 49.172837634, 49.8095649926, 51.5554559551, 53.1612275721, 54.1318750629, 51.6581509082, 51.2243459712, 47.5083114249, 46.6266141855, 49.1686716846, 48.254946282, 50.4018586057, 51.7976945483, 51.0055596242, 45.7454921747, 44.179207227, 46.7755017849, 48.6538545858, 50.0021883325, 48.1006048253, 49.6203813643, 51.573772729, 54.1832560359, 52.4796123359, 53.1793086477, 56.127607698, 53.2896666488, 52.5102371977, 51.2916253732, 50.8750790852, 50.771670663, 53.6475692081, 51.9972080007, 49.3281677732, 48.3947944417, 51.1440793082, 49.7815280583, 48.8316367291, 50.7909132053, 48.7576323169, 47.0496207193, 48.5960951333, 47.2290335783, 47.9282769609, 50.0049480612, 49.3984720225, 50.3945611388, 51.5675997396, 51.7306739049, 48.3523195717, 47.6854472495, 47.4464367049, 45.7759329459, 46.8444150246, 47.6144295263, 46.7953631481, 46.3622728428, 47.6111540694, 45.4323723489, 43.166072214, 41.7084756334, 42.2363088802, 40.6908987033, 42.776693816, 42.3391381948, 42.4917974541, 42.8039818545, 46.0866140211, 46.3395327707, 45.9503058685, 44.1097040398, 44.9247753912, 43.601067036, 40.9388982459, 41.1309168488, 38.1619162191, 40.2824704419, 39.3296083902, 40.6410047504, 43.099796534, 42.2393472484, 42.3712029202, 39.3868785486, 37.1044897197, 37.769984911, 41.6961261219, 41.2920596426, 40.1106911516, 37.9427008462, 38.2668639865, 36.8978341135, 38.3840820437, 38.3161738614, 38.6948395987, 38.8517206197, 40.9122596654, 40.8410420606, 37.0610066791, 39.0981371633, 39.819850185, 37.6877351263, 40.4131970169, 40.6047199527, 40.6775388726, 40.2388499533, 39.2854304948, 40.8460990384, 42.6805036882, 44.1714679081, 45.3649230051, 45.248043348, 46.4067825273, 44.9437525621, 39.9625268025, 40.726951649, 39.7641087623, 42.4714700977, 43.5913161253, 43.7328206427, 45.388253538, 41.8721760691, 44.7363909461, 45.667523673, 46.0226450025, 46.4094407534, 45.9531165887, 42.9773517728, 43.2320469197, 43.2236981527, 42.9150888578, 42.0698513134, 45.4541094339, 48.2322576884, 48.015615753, 48.4828841395, 44.5669500394, 44.7318425089, 45.0286220705, 45.153005827, 46.2451937634, 46.0673057622, 44.2993808926, 46.1937999668, 50.8155642515, 50.7660465196, 49.9763261227, 50.9197529472, 53.3859030399, 57.3463588467, 58.3701644263, 60.0945200422, 58.0456785184, 55.7564834791, 56.1161493922, 55.5035687982, 57.8089917134, 56.9411931813, 58.4853230214, 57.9868027849, 57.4098633223, 59.0766928439, 58.2049430829, 58.7335613826, 58.6716527278, 58.8342895423, 58.7411294568, 59.6865524804, 59.8793831266, 59.9224635821, 59.4186414562, 60.3946320876, 62.6260533725, 62.3629056875, 63.8167790895, 62.0050103546, 59.50295813, 60.1788276, 62.4608830705, 64.1039573185, 65.3229125334, 65.1101093555, 64.7697107454, 67.7662983054, 68.5789513898, 68.8045257001, 67.3120840528, 69.5404569458, 70.2779574683, 68.775082891, 66.2516071002, 64.9880041032, 63.6071905145, 62.8078000131, 63.7414341467, 62.1485155736, 60.8513993031, 58.8546020996, 59.7154747972, 60.8415472833, 62.1491227001, 63.2514304563, 64.8082342999, 66.0601497319, 63.4898928798, 64.8167500746, 69.1592319171, 72.2974905243, 69.8816363093, 67.2894450542, 63.9975636531, 65.1396578397, 64.2235705358, 61.9222915625, 64.0046200806, 62.7061020711, 62.9075254659, 62.6706522782, 63.8986769462, 64.3662442424, 65.6346552038, 67.5181158376, 67.55212866, 68.1959583825, 69.1177244159, 68.1514970882, 65.2556128392, 67.5997964685, 64.7594976854, 62.5960540389, 62.6017204247, 63.9125577635, 66.5960069341, 63.7303986788, 64.7141996392, 64.1786784504, 65.8480540976, 66.7746491051, 66.8517894323, 67.0029145952, 65.3358555907, 64.0227239199, 67.2707535513, 70.0569431296, 66.5886429911, 65.5925938088, 66.075359374, 67.4744305208, 67.2152556877, 67.101694285, 67.6813761535, 70.1243762521, 69.4094080381, 68.9790432943, 69.5721166951, 69.5072212685, 68.7823597765, 70.2493164537, 71.0758622214, 72.3712411329, 72.5939372218, 72.3865475341, 71.8234621147, 72.9645732622, 74.2753793245, 73.3101772865, 69.5799413598, 71.2115050515, 70.3922484973, 70.7048964309, 71.274027869, 68.6542978736, 68.5186220737, 68.6318032856, 68.0950331462, 69.9385898136, 71.6666465374, 71.3787935227, 71.1423041646, 69.6399390218, 69.7479949336, 69.9154678512, 69.3662501147, 69.6971428248, 66.3320651005, 67.3283470686, 65.3354628389, 64.2124917203, 65.66985323, 68.8971821063, 68.8084459443, 68.9453960075, 68.282192448, 69.9078235084, 71.2269461382, 70.2591117076, 69.2842358312, 69.3902937768, 70.8769762957, 71.7489141127, 68.3792946595, 68.1676012572, 67.34591267, 69.5919981636, 69.6257583326, 70.5690230257, 67.6840528605, 71.0817704129, 70.2247278192, 67.9171810178, 67.8374544396, 68.6356657166, 67.6870063402, 68.6210141651, 69.7369901363, 70.6847902102, 69.2200236535, 69.432835118, 72.5914720521, 72.1735065279, 72.8398975157, 72.8957616672, 73.5014402353, 69.2111150165, 68.9538056386, 68.4826628874, 69.1765258504, 68.1313120266, 68.4364289054, 68.7902816322, 69.9056682986, 66.5831594944, 63.4965112718, 62.2312218206, 62.0531303035, 67.5931740329, 67.1392287247, 67.6986599813, 67.1999262468, 65.2217050935, 63.0902181804, 62.395368695, 57.0789425253, 57.8702948234, 57.6894843978, 55.4987001634, 55.4828246345, 54.1327536924, 54.0526085253, 53.3203268027, 50.982367741, 54.2276307045, 52.7621629529, 57.2758322595, 56.4688000272, 54.4837388238, 54.2629744768, 54.4040920283, 55.4426327809, 57.1578923213, 53.9899743304, 55.5666869911, 57.0323618329, 59.5971433573, 60.6010850145, 63.7932859459, 63.9697089653, 60.5189599836, 63.050354105, 63.7128985099, 60.927124528, 61.6225054445, 64.4750646853, 61.8802685441, 63.4978299129, 62.7820729287, 63.2717811248, 61.8469890184, 62.463529559, 60.8556577723, 57.9992756498, 55.1037269688, 56.996124009, 57.2058010929, 56.8677302322, 55.4869936363, 57.1190029818, 55.4795797533, 58.0322390504, 58.7534103992, 57.6708546467, 58.248669724, 55.8871814532, 56.288219043, 57.7759594795, 59.6041503247, 60.5239383954, 65.8878957307, 67.1760474176, 66.1689784489, 63.9686904476, 62.5916053624, 62.4766576492, 59.4723843184, 60.8570947877, 57.9075007359, 56.9167185193, 56.9791464683, 57.1439289275, 57.8401080312, 59.0547669118, 59.4119769986, 61.8402719205, 61.3676731557, 62.1005141787, 62.5359164147, 62.1530884571, 62.1247509104, 59.9964201312, 60.0070233479, 60.5080845442, 58.8721831283, 61.5320785909, 61.2413638281, 62.3175435222, 64.365148407, 64.5822351087, 65.1644769455, 65.6198581809, 69.1891072018, 71.677493743, 70.7659219886, 70.8919122493, 68.2519238359, 67.7190179299, 67.1303149619, 70.9113747701, 68.5466072779, 68.622436651, 69.9513752054, 69.7077916241, 70.0586526394, 70.4540974387, 72.6789808384, 72.2708218137, 73.3262365673, 71.579732639, 75.0419051005, 73.1013732743, 73.5423522732, 71.4130022544, 71.0229260018, 67.4663742541, 69.9713919815, 69.0849866069, 69.7844220502, 70.2513571578, 70.5120123683, 71.2025183403, 69.0980626464, 68.291950608, 66.4907995795, 66.3131279269, 65.9155871936, 67.7049521919, 69.1766288891, 67.6058212973, 66.961785912, 69.1332473989, 68.5870480822, 67.2393373814, 65.9241944639, 65.5695781151, 64.813136775, 63.9467649411, 61.6563107782, 62.7919153044, 62.0343710617, 62.2198014924, 61.2828427726, 61.0516050179, 61.6765699783, 59.758606214, 61.9154929674, 64.9509409437, 66.1373924216, 67.1231051798, 66.3301824315, 66.7753308206, 67.904294002, 67.0538300999, 64.8093312496, 63.9910922061, 64.8602586294, 66.2652892821, 64.0131648065, 66.60198661, 69.3673092917, 68.1487733138, 66.2695796145, 64.249854758, 62.9901384078, 64.1266807259, 64.5335614627, 66.7507501269, 65.5801996572, 67.3167269234, 68.5133144768, 70.0383823845, 68.1503202547, 63.6751625266, 65.4858757498, 66.3887763471, 63.2468335534, 65.216278084, 65.8094726439, 65.4121526106, 65.1641220938, 65.9736253224, 64.6874539224, 64.7156555894, 63.0787406452, 62.2399607162, 64.550357768, 62.791634021, 63.4789911009, 65.7996125643, 64.5330412008, 61.4462801987, 61.9214518336, 61.900508045, 59.6969581209, 60.2386757774, 58.8274221645, 58.203465503, 58.0079130772, 55.6541749859, 53.0869174752, 53.1199027285, 55.2535376528, 55.1001791778, 53.9564280888, 53.9934116714, 55.792305903, 55.7403459445, 57.1870450144, 59.9342579866, 59.2072284529, 56.5831966248, 59.5458237545, 58.4003369115, 57.6597597473, 55.8652321432, 53.0433335572, 53.0250886773, 55.7277151103, 58.7451962395, 58.3677419756, 61.0191213468, 63.8695561506, 63.0738900027, 63.9769636866, 63.6562018644, 62.0715315521, 58.494890868, 55.9938808335, 53.1111064645, 54.1092985679, 55.892301027, 52.8697573781, 52.1937966495, 56.4318201462, 58.8973881205, 61.0172458863, 64.106162407, 62.908136742, 60.913026058, 59.6284041864, 63.8549043854, 61.4191907909, 60.3763021782, 58.4436027905, 57.6809881506, 53.6703361862, 55.5761263819, 54.9609698674, 55.5986525157, 52.7940413115, 55.6119372275, 56.0161769172, 58.1408019949, 60.8064283385, 58.1656376282, 56.5396477621, 58.5785714024, 57.6129181757, 56.5310641687, 59.0627862805, 59.219715033, 60.1745854511, 60.1612652578, 57.6901963087, 57.4899218633, 55.9275155374, 55.7155183878, 55.9828556456, 56.5976910807, 58.3044784297, 57.9396351824, 58.3766497848, 59.3425770472, 60.9729920013, 57.7561366057, 59.3282784055, 59.5950857927, 59.7039746984, 56.4962776386, 55.3646416372, 54.8022647676, 53.0681068406, 56.5861628281, 57.8275650645, 58.1005416934, 57.8466921153, 56.4794824704, 53.6358887203, 52.9403763165, 56.8738134847, 56.7117912556, 56.0346912327, 54.7610138098, 55.305041198, 57.2316913548, 60.7548200034, 62.1150677331, 62.6448236841, 65.6445632967, 61.1795037896, 59.2304742336, 59.3763913287, 55.8686920789, 57.0276456622, 58.3281577401, 56.9913854244, 59.0861139377, 62.5751965195, 61.9111418607, 60.9959186537, 59.8568447507, 59.8766670463, 59.0678247142, 55.0383404999, 51.9433936971, 54.3876837926, 52.745007874, 53.1073926661, 51.8183773914, 48.1822666469, 48.5108276526, 47.3516510626, 48.8276485774, 48.0774202261, 48.2743703996, 47.1838732579, 48.1866513798, 44.3249005597, 47.0982552072, 46.7000802872, 46.9799563066, 43.5259830169, 45.5614446133, 47.0373546889, 47.3887987295, 49.7802368495, 47.138434139, 46.0271852127, 44.6223155107, 45.8298806641, 44.3962582315, 45.6573840975, 46.9786838557, 48.1691715642, 47.7628283084, 45.5337353538, 47.8989432625, 50.2364458915, 48.1519390003, 49.5586673138, 51.9468376859, 51.2493329879, 55.5846142149, 54.744839578, 57.1085282438, 59.0327235916, 59.7948752179, 62.1739248628, 60.3774103081, 58.1561797748, 59.0422024137, 56.9916059937, 55.1525742719, 56.1370270412, 58.8852235739, 61.0040270922, 63.1014481925, 63.2549801714, 65.7577912212, 66.32351834, 66.9005768715, 68.1065482151, 66.6505357211, 64.1593048117, 66.7033627772, 66.3114430992, 67.200532816, 70.4436703819, 72.0368903495, 72.5036377658, 75.6288472254, 72.1993774869, 69.636863179, 66.7681700586, 66.3572946847, 65.1839054172, 64.7743915255, 64.0625587101, 65.4112233218, 66.1527301318, 64.36036027, 62.4829610963, 60.4367010541, 60.8447103468, 62.2110568367, 59.8236138947, 60.219759601, 60.6789589793, 62.5938753092, 64.0676922944, 63.6052451473, 64.5407500158, 67.0748389218, 66.6448755464],
mode: "lines",
marker: {
color: "#9467bd",
size: 12,
symbol: "circle",
line: {
color: "rgb(0,0,0)",
width: 0
}
},
line: {
color: "rgb(44, 160, 44)",
width: 1
},
type: "scatter3d"
};
var trace3 = {
x: [-0.366643784486, 1.46867702426, 1.49158152793, 2.69868615756, 2.65684108853, -1.50957669136, 1.30595070728, -0.482437634496, -3.33494755811, -2.03052334978, -3.2489509072, -1.82107984366, 1.16735399512, -0.541809555384, 2.13362928294, 1.85078669989, -1.61152692388, -5.24367285709, -4.92871177652, -5.92248589648, -6.72666383117, -7.29213255796, -8.18775147365, -10.9510888283, -8.45828696371, -8.82239435447, -8.51672841826, -8.96535928602, -10.6644057716, -10.5610915446, -12.5530047964, -10.2194806858, -9.42740314954, -8.72313056016, -9.15681370159, -7.59962325783, -4.12379323734, -4.12953511436, -4.37564038952, -1.58418118344, -1.89849776714, -3.82344139126, -2.29862634246, -3.08997672547, -2.55486367629, -6.01211696522, -2.24381363707, -2.33947162562, -2.28682453842, -1.3247819837, -2.93449768138, -2.18757398723, -2.65080704246, -1.28430187459, -1.39534524977, -5.57930047785, -4.658780558, -5.10798381288, -2.30724245525, 0.28857891365, -2.40315215358, -1.83600198743, -4.33967047929, -4.45365282598, -0.672407929082, -3.76492223278, -5.34948629226, -6.94685544808, -8.8852887949, -11.6805027579, -14.7357385002, -13.1697805369, -12.8538582165, -14.6455296023, -15.0110936059, -20.1460707277, -20.357463296, -22.4939400519, -24.987824741, -26.3624471081, -26.8015192705, -24.2905643583, -23.8739929036, -21.5149997688, -24.3238470129, -24.0081427291, -24.3319673627, -27.2049254996, -27.8652475116, -27.9149221267, -27.1719296278, -26.599869403, -28.0800486325, -29.9276840445, -28.3518306466, -28.981996937, -32.4100781152, -35.8027849546, -34.5274354147, -31.5671446406, -31.3734658358, -32.1551613736, -30.6839070731, -28.9915128473, -31.1327047076, -30.7418154508, -29.1070064367, -28.9334094512, -28.134411581, -29.1188577361, -29.9900494659, -28.709484251, -30.7346601744, -28.5082698595, -26.0953552689, -24.9115309444, -24.0308599264, -23.5605432643, -24.1759170874, -25.2134107148, -26.4126634324, -27.9188902939, -28.5249719142, -28.7812351191, -26.484712937, -26.1979670542, -23.980429257, -23.7962896723, -23.1655177045, -20.2574012244, -21.3390237755, -24.7509331328, -21.5292712983, -22.6559872054, -20.3460488964, -18.9842569895, -18.7711584121, -18.1147145775, -15.5762995186, -15.5725877822, -15.9007572871, -17.7374449736, -15.9751097954, -15.8026675369, -16.8349091687, -18.8012656432, -19.9340332548, -17.2784719959, -19.7634231867, -20.8639893581, -21.3179824372, -22.9670634313, -22.3419076791, -23.6683657946, -23.1574848842, -23.8386402341, -23.6543578457, -23.3155526621, -22.7607626994, -20.7747429464, -23.4934278782, -24.9861065372, -30.0693622949, -31.0110103801, -31.6706545887, -32.0625477093, -35.2865258687, -32.7792978241, -28.3717083845, -31.6020573651, -29.7417597687, -23.8276442048, -22.6902576238, -24.7577752755, -23.9485295934, -23.9123108429, -23.6261495351, -25.6560530843, -23.1505042447, -22.6998537145, -20.745655149, -17.6384590018, -18.8804995907, -21.0121882317, -21.7675698925, -20.0519515057, -20.2013658902, -19.3238132573, -17.3037196134, -15.5730122913, -15.4870169849, -17.7881644347, -17.304896315, -17.0549580558, -19.8973477035, -20.1697195875, -18.3167381729, -19.7911589085, -17.3283492961, -15.0647625201, -13.4959207418, -17.693924031, -17.5407764747, -13.5133070518, -12.740725088, -17.5244739167, -21.7656154174, -22.1230633938, -22.1964242284, -20.6117046991, -20.2622260721, -19.5155425503, -16.9552149265, -19.0397121653, -17.7835612392, -18.7075714754, -19.5378291737, -17.132708198, -16.0820537025, -18.4068035914, -18.914648562, -18.3117563478, -15.9499444978, -16.4969595804, -14.842906784, -11.9254817311, -10.4457178503, -6.60981510621, -6.63460324855, -6.85061945233, -4.72496425216, -7.31208836293, -8.95895619947, -8.46413795895, -10.7287359214, -12.2695615426, -12.3956088356, -12.0038029113, -12.1456064319, -10.5335113622, -10.424416554, -9.79745915591, -7.32334423097, -7.61038019839, -6.88852317524, -8.92463452219, -8.10860242713, -11.204712281, -9.76871895885, -9.72908595672, -8.72051661019, -8.25205350141, -7.77531849911, -8.09757338188, -7.3692497151, -8.29924358678, -8.04645048302, -5.49419507923, -6.50325269739, -6.45770386365, -7.89777076221, -8.73324138251, -8.13003474547, -6.52790108923, -2.58550835392, -2.62407327302, -3.10148241772, -6.88409156851, -8.17742447671, -8.41023701112, -9.72769239585, -11.569066554, -12.060674678, -15.7535757118, -16.9922788692, -18.973300845, -18.4677011826, -18.7587883248, -19.9261566994, -20.6220390337, -22.4199274348, -22.2697296435, -22.4347373481, -20.90059989, -21.8505608747, -23.9247739697, -23.3895571845, -25.1943530151, -23.9872862053, -24.7648604278, -26.9200056074, -29.0190775214, -26.8276927435, -24.0033202019, -24.6266672768, -21.6248179282, -24.2656757685, -25.4178438176, -24.3869705805, -23.1800502796, -22.0245445594, -21.2896366659, -21.2474106837, -23.2983388058, -21.4838546557, -24.378013278, -24.4581297647, -24.5051443538, -26.9379125203, -26.6579909944, -26.2697654886, -25.8955675197, -25.1441909941, -21.6352353058, -19.2494097263, -20.1275297005, -22.3666861882, -27.0212828343, -29.1960781436, -31.1531852901, -31.0138057468, -29.2358446608, -26.1546741276, -27.9645146478, -26.1703984667, -26.884220139, -26.8198259922, -31.1873182735, -29.3758844384, -27.4718326794, -28.3657426213, -28.2584445026, -30.0939403991, -30.1017043126, -30.4623967613, -32.4739088474, -34.8389030162, -33.2171355251, -32.0262846762, -33.3050916916, -36.4861970118, -37.8041311065, -37.4390198443, -37.2590876446, -34.2291445311, -33.4656557683, -31.3113843349, -29.1165584131, -26.7758744075, -25.0567265479, -22.4536252952, -18.0531332753, -14.3967233433, -15.2599003482, -14.9055524342, -15.4371104998, -13.5942941143, -16.3992955725, -14.8588899275, -16.9228426798, -14.6843749176, -11.4663515834, -10.7039944441, -9.10560794319, -7.64477432292, -4.72317577332, -1.90421845985, 2.45228684262, 3.00203904874, 1.96978689769, 1.1216273452, 1.67986661735, 4.01599968444, 4.35599406922, 3.04742479143, 3.00138927525, 2.10604153587, 0.998420822484, 1.52404939847, -0.0261456240821, 0.34026760782, -0.924324128052, -4.02759116262, -2.51294170499, -2.88453356065, -1.27835777069, -1.38821734424, 3.79945016382, 4.75820577049, 6.89368018984, 8.18526251216, 8.97648460094, 9.59091463766, 10.2927369639, 10.2837777866, 9.61430734394, 10.4353774413, 12.7512749615, 12.3743389497, 11.8455385422, 12.5163937088, 14.742405326, 13.1886594251, 10.8062430886, 10.0375498938, 8.62557338555, 8.77338440444, 11.0640780305, 13.3107981335, 14.6055138903, 13.0366132602, 15.3046379318, 14.3037941916, 16.365239605, 11.4794511046, 11.3182282972, 11.9957108268, 10.3014191915, 12.205833407, 10.6544724225, 9.64997691904, 8.6042264869, 5.86013871474, 6.18251843556, 6.02113554871, 5.53977599568, 4.47252883676, 3.98156839214, 3.03670768773, 2.83642092697, 3.00469325201, 0.673674312298, 1.03917289776, -1.70470862106, -0.62394320436, -1.50402877218, -1.76542624865, -3.18851693857, -4.89431915275, -1.85398947519, -1.00648376787, -1.23570689208, -4.72730159014, -9.89452737282, -8.31260219374, -6.21076247838, -3.79497542873, -4.08574645223, -4.46474450992, -1.23774425398, 0.0728087754921, -1.52555047701, 0.504548364394, 0.118099507283, 2.48450674518, 3.00343664576, 4.01799358498, 1.76029687825, 1.56075945499, 0.853753948553, 1.82217187239, 1.93143698333, 0.921659719638, 1.92177534161, 7.3055515881, 5.992613025, 6.22728471476, 6.43394681002, 6.95597591231, 7.38374854372, 9.20789351254, 7.37503540685, 8.29248749342, 9.10476836589, 9.78394700564, 9.44209329531, 9.40130029354, 9.27629112648, 7.70186170567, 6.90525719534, 4.91901463652, 5.26440316527, 6.63874926302, 7.71761488687, 5.17571416134, 2.50783377864, 2.79089205199, 3.13165717374, 3.20933804478, 4.71950238768, 4.23849009164, 6.43201129991, 8.3113964651, 8.31848343637, 8.49760462319, 9.80692550924, 9.86699365355, 11.2758121122, 10.6251190333, 6.92151482605, 6.79683348664, 6.97415926266, 6.14221431105, 5.80529991984, 5.12512067403, 4.65345463049, 3.82353692673, 3.9804902107, 1.88462538744, 3.25328285244, 4.77382860551, 5.74080403531, 4.92508243798, 2.56042251019, 3.71944684571, 3.78051397584, 2.0430903416, 2.15795691183, 0.291762185712, 3.52374951601, 4.30544860807, 5.32609775223, 5.59120789549, 4.91279436161, 2.32684593282, 1.89977310688, 0.742332159466, -0.832658482627, -3.94327494172, -2.03020626992, -0.669787851115, 1.60625823427, -2.54413970368, -2.09581024568, -3.58069890878, -3.68803611024, -2.17626868634, -3.63114327625, -3.7283132995, -6.59451051682, -5.05844983544, -7.4438833729, -9.06708655271, -6.90817670007, -5.16108678359, -6.08739192071, -6.65923272885, -8.69807385276, -10.4758519649, -11.072101651, -11.0535552957, -11.5337452076, -12.9689297013, -14.368159507, -11.9518208039, -16.2407486135, -16.5282819204, -13.6515453555, -15.6532286531, -16.7236733267, -18.1181926963, -21.1086526333, -20.9417786355, -16.6648856019, -18.4141191099, -20.267709101, -19.1518253458, -19.1829406954, -18.3257229923, -18.6995014286, -16.6970721773, -17.487927734, -18.6411556051, -18.7430472358, -21.5618109473, -25.342545572, -25.3322867981, -23.6676828693, -26.2125682423, -24.3568279342, -25.9551094069, -28.604834798, -27.7145972065, -26.834686091, -24.3980169045, -23.9709406904, -22.4891898851, -21.6879116143, -21.6232476837, -22.6742447003, -22.9069852132, -21.9452472038, -21.936284556, -24.159636215, -26.3588155021, -24.1701416294, -23.7056805362, -23.0202679132, -23.881099187, -22.9383517026, -22.0606960054, -21.9661970534, -18.7535773131, -19.2111287125, -21.0406044555, -22.6104672678, -20.2357836582, -19.8192948846, -20.9152788691, -21.6971620702, -23.0788554895, -22.4525149634, -22.2851968041, -24.481290699, -26.8201567477, -24.1833388924, -20.7955767584, -23.4572873969, -25.1211317554, -26.6984555333, -25.765536365, -24.5026273876, -25.5635879106, -25.4824663204, -26.3184440134, -25.8971483727, -24.7982749102, -26.0548456574, -25.6494040279, -26.8543840128, -26.0803314072, -25.3026671555, -27.0032079217, -28.4928307793, -26.2754005457, -27.327044396, -27.2005691332, -27.8615998138, -31.1062003122, -29.3000903901, -29.9592123295, -28.0507925399, -26.2085780831, -26.5640050221, -26.7594632668, -24.0206980114, -27.8327151453, -25.1565085512, -28.1653814006, -29.6318972729, -26.5049278758, -26.049848531, -23.5397588636, -26.302451247, -26.0227503142, -27.0868800498, -26.0835263421, -24.0585392253, -24.6006611807, -24.1883705409, -21.2179181461, -21.3481707071, -19.9113221184, -17.9226359925, -15.2139231214, -12.1356803662, -11.7356811551, -11.5775681238, -10.2863799712, -6.63224084232, -9.12042317266, -8.36498985555, -10.5894053787, -10.5484092662, -9.10315361592, -10.0893831404, -9.08555960204, -9.62350423105, -11.7989723626, -12.4088760548, -15.0646627236, -15.3667724219, -14.2909359537, -15.4684853722, -15.6434100178, -14.0686774002, -12.1052861983, -15.0185792886, -20.4815414528, -22.6524902046, -23.1181011134, -23.3670164399, -21.2004730547, -23.5011266614, -23.3280811234, -25.9029218124, -26.6202085581, -27.1029581211, -27.293531518, -30.2543906474, -33.6450443644, -30.9759863796, -31.6905210162, -33.2407485012, -33.9645437437, -32.23912975, -34.0023555403, -35.3005486297, -36.4027248905, -37.2012573461, -36.7054795669, -36.8952523523, -39.5634727012, -38.1906670091, -39.005880058, -41.4538947557, -37.058914879, -34.836179725, -34.2489821138, -36.1454917813, -34.3243904934, -34.0677757882, -35.8663057181, -33.6708442305, -34.3973684987, -32.4036345639, -33.3620832634, -36.616901647, -36.5608793405, -34.2619766989, -34.2902620311, -32.9951681104, -34.6885181431, -34.6352631181, -35.0009612729, -36.0927721468, -36.8784330952, -38.6321547877, -36.579885199, -36.6499877238, -36.368595471, -36.1135344717, -35.1353918656, -34.9431840205, -34.6318361912, -34.5467580487, -32.5309783741, -33.3758110977, -32.3210267913, -30.175437773, -32.2077764803, -34.2808610654, -31.7481039145, -28.9916360415, -27.6099888958, -24.2811738499, -25.1843854082, -23.8533996286, -25.4548163674, -26.628605721, -27.8367021315, -25.4478818986, -26.6671868935, -25.469096662, -26.0512184174, -25.9687901692, -26.6465822982, -26.5962966918, -26.1687600439, -25.2889381792, -23.4945148856, -23.7685376412, -24.4856451453, -23.4511324158, -20.8466837554, -19.9776064971, -20.3909214642, -15.6121020203, -17.3268549884, -21.7236714669, -24.1658705219, -24.5377163533, -24.6813015338, -23.9072062307, -21.1248773551, -20.5674768504, -23.79430845, -25.3359490511, -23.0201182456, -26.7943351798, -29.0657729409, -27.3833839525, -25.5135545713, -22.1115892236, -22.7808905766, -20.7417456175, -23.7519425093, -24.8599718734, -21.8415313139, -20.794866198, -24.8978459546, -27.2343254275, -28.9072523555, -28.6864411808, -28.9467802957, -24.5504632533, -25.9350945267, -25.8905262535, -26.3624603876, -26.6383655121, -27.5764373637, -28.0094904615, -29.3698003256, -30.5332717529, -30.0115299712, -28.0874068332, -26.5737245081, -24.4460373848, -22.721571244, -24.3966736389, -21.1548161197, -23.1463615083, -22.5707045425, -25.676695077, -27.4615297882, -24.2123600797, -26.7738071354, -26.4579049881, -25.1441899987, -27.2259047044, -24.1893184392, -25.3771406766, -23.7218124378, -23.3115223025, -22.4684634545, -22.7751804876, -24.0083777532, -23.0561331581, -23.6465196519, -24.2145796853, -27.6642841033, -26.7384451225, -23.0039566935, -24.1699058537, -23.8225121795, -26.0270313524, -23.33299358, -24.0385574029, -24.9655413154, -24.4937729508, -24.3389816651, -21.9914986033, -21.5771839475, -21.7164781309, -20.136802143, -23.2910446995, -21.8127060543, -21.0600711324, -20.9628181981, -21.2820565045, -23.386346177, -23.5495042906, -24.7867075585, -24.7081398184, -25.9530598353, -26.3773094309, -27.1262759003, -26.7831797394, -25.3095008886, -24.4923123903, -23.8757190745, -22.9909315182, -22.5696793567, -21.7704049237, -23.3096546121, -24.4874485304, -24.1970833798, -22.9251012501, -22.121588331, -22.4694004136, -21.5904542137, -24.7531384114, -28.4414695355, -27.1709056435, -25.0759190002, -24.3366737269, -23.5765518903, -21.4682687413, -20.8445257715, -19.0537043759, -19.8970143685, -20.1007013021, -19.1392482053, -20.8994782621, -19.9091640122, -20.7655389722, -21.7040980328, -24.0989514804, -24.2707363604, -24.3230447034, -23.8078637864, -22.4188101853, -19.6263399446, -19.8942499842, -19.2895760649, -19.110250189, -19.8167714222, -17.3060470956, -18.1720120052, -19.4083390027, -20.1444454973, -22.4531136573, -22.661485435, -25.8353640861, -22.5694073388, -22.3488278317, -22.3619113075, -23.6981883417, -25.2005526721, -28.1295650928, -25.7682464418, -23.967975652, -21.406730382, -20.1651048624, -21.4508809036, -20.4526036206, -25.4238337046, -25.7854581106, -25.8845704531, -26.7910525198, -25.2119807989, -23.0334760807, -24.3796174924, -23.9060667761, -24.3747332413, -24.9933681139, -24.720025189, -26.2399111676, -25.6558190537, -24.2955500518, -21.7462531844, -18.6413789045, -17.4086956888, -13.5653030323, -11.6946101532, -13.4181825587, -13.5929249635, -15.3782927252, -13.1533864481, -11.9299823028, -12.1460769524, -12.1285316306, -14.2052328441, -18.033127626, -15.5011727926, -13.9966654634, -15.3746056794, -14.156370293, -15.5259174568, -15.2031933958, -13.7620032201, -12.220368085, -13.2979473017, -14.2194242682, -11.8079981256, -14.2880060415, -13.9214307835, -13.1163351545, -12.7385310896, -14.4683388134, -14.2538765474, -16.0918797723, -12.2416199805, -13.8670404248, -12.5029395551, -7.85917370595, -5.21528704447, -3.29127488249, -4.35811436631, -4.53100613142, -3.81615216123, -0.926092308265, 0.588968662044, -2.102079912, -0.0902340794677, -1.11939473098, -2.04236019162, -4.60673062606, -5.78645920074, -7.13868671068, -7.98178701057, -6.2221733934, -6.95719066838, -4.97130962272, -2.78408636852, -2.41006328279, -1.623988036, -2.66355312453, -0.610204662192, 1.31513403543, -0.755575043695],
y: [0.671891657472, -0.287102130342, 2.09425411112, -0.0432503304168, 0.0191379024233, -2.69654293548, -5.47165918656, -8.07273136573, -10.0788257514, -13.6017277544, -14.2446889414, -14.2938323123, -15.3087415068, -13.3753876652, -7.97473157311, -8.69026090791, -8.25755728227, -9.36409388741, -7.85035629921, -8.64308275085, -11.6475291944, -11.1701623873, -11.5098191362, -8.27593215087, -6.22185470927, -7.57504356678, -5.33235908583, -5.55092640664, -5.14357046472, -6.212619012, -4.96216724759, -4.50013002344, -0.593154764069, 1.64400686382, 1.3172020084, 0.246269562504, -3.57181950601, -5.70455267069, -5.01992524693, -7.52149605266, -4.10063348149, -4.61974788286, -8.13154431163, -9.57393278678, -9.07212080472, -9.83048764252, -7.86508425598, -10.152585207, -7.14527832581, -5.4229210356, -4.26160048454, -6.51613771293, -6.33380777398, -6.69794447027, -10.8672399573, -8.49195227829, -6.99808721962, -6.65006847341, -6.82287090098, -4.44917244446, -4.31944457221, 0.0196531167493, -0.610352238005, -0.386094619618, 2.69420164586, 0.474108444816, 2.35312851493, -0.991091178891, -1.34002929985, -2.31605424409, -3.4305621409, -1.99292430541, -2.43005111711, -6.78646867437, -6.03947971825, -3.82347934534, -3.23441904895, -5.51372280671, -7.10239206183, -7.94410479661, -7.34057311707, -5.7177770785, -5.03315172791, -5.95736256828, -8.68976505023, -8.91878531964, -8.70044256949, -6.70556439412, -8.36377170901, -11.2713722532, -11.2132257606, -11.1486555255, -11.0059122711, -10.5320670417, -9.95431700485, -7.41543318956, -9.80529130725, -8.25209244278, -6.72761505269, -8.40177626742, -7.07827944716, -8.48020943969, -9.5481636461, -7.30677203995, -9.15515518627, -8.39859103145, -8.68039298739, -10.3740435569, -12.5000204881, -11.0441338644, -11.0267352594, -15.3826914652, -15.3399446269, -15.6375767241, -16.8767692673, -15.4933615426, -15.03462752, -14.0330621237, -15.6856229791, -17.8748456549, -18.0246120542, -21.4271543807, -22.8385072718, -23.7272424496, -24.8213958913, -23.4221157031, -21.8653184355, -22.5458904737, -24.9524747861, -25.0563457785, -25.8908356884, -26.3151304148, -23.9948165804, -22.2879781292, -21.5013571167, -22.3325898079, -24.2701035919, -22.5106367771, -22.8614075781, -25.091409284, -25.6697603564, -24.7504173753, -22.7681621294, -22.5117444702, -22.5455649705, -23.9186371021, -25.6521813374, -25.3279602323, -25.4907594507, -27.1956254267, -27.7436112287, -29.7458971467, -31.0282003305, -32.4301137422, -31.9992026925, -33.7966054984, -34.3694402973, -30.9618059408, -31.5566338417, -31.9120937683, -32.2060066232, -29.1365651346, -28.9380056329, -28.4816202259, -32.1020335297, -32.2437132042, -33.0409194937, -30.6786530977, -32.5640008167, -32.8808564811, -32.6512963944, -32.0260645011, -30.2370252525, -31.0482690701, -31.4057203906, -30.588924007, -31.2357385566, -30.865120862, -31.0246048436, -29.8672611539, -26.4896292467, -28.4724883975, -29.5391623364, -30.2153088308, -31.5209733355, -30.5407813654, -29.4224101222, -28.9528381806, -29.7992758757, -30.0450970224, -28.4923812397, -30.7451265347, -28.3118177908, -28.2739004753, -29.9505037313, -29.2307476662, -31.0042215404, -33.1469160387, -38.6881519983, -35.8379104429, -37.4464891367, -36.63680263, -38.0385529454, -35.8734153803, -33.7656940094, -33.1434510996, -32.2479520454, -30.9216939163, -29.9971973656, -29.1979986232, -28.8056070314, -31.207577107, -30.6031758602, -27.5853351108, -28.7995287528, -29.2220195126, -29.2045713213, -28.2232127714, -29.450861518, -31.8657549493, -31.7403880144, -33.198466827, -30.6495893316, -33.1901600196, -32.4141491138, -32.7179821567, -31.5067667307, -31.9148701888, -31.1953757907, -30.1443894907, -31.2289106482, -29.2745210109, -31.9614328295, -32.7780694554, -30.2737320611, -28.7583921589, -29.0818042848, -29.3477202888, -26.9006693547, -25.9048813981, -26.1092378607, -26.4480851564, -23.6860400734, -21.2620980241, -21.3070898281, -19.9508501185, -19.7604207359, -17.4327730342, -16.9307886826, -16.3123340797, -17.925338908, -14.6182717257, -15.4724393879, -15.1823382344, -14.7491347329, -14.6633784188, -13.0967195805, -12.5346460667, -14.5415298576, -14.2885145695, -14.6036543717, -14.0197145062, -15.1693475144, -13.8019936702, -16.1951298899, -16.6599144736, -20.8128063772, -20.2405933931, -21.7984863186, -20.0650424935, -19.5673373163, -22.3955619672, -19.7553812447, -21.8239148887, -19.5800248341, -21.6238527772, -22.5721220148, -23.441768856, -23.2269456016, -25.075389456, -28.9801759048, -29.0404206653, -29.1048955202, -32.5780978027, -34.8538036663, -37.4180425726, -36.4376879884, -34.7191901095, -34.196407841, -35.3834499948, -31.83633847, -30.9895448897, -30.0242012857, -30.225543474, -31.4190910267, -33.9522450557, -31.4390978834, -32.1093556885, -32.5902281054, -27.9002693775, -28.084001354, -24.8820341392, -23.5635732261, -24.0407801643, -23.9803434779, -24.598796829, -25.1259755416, -24.5645693265, -26.0001086914, -27.370910868, -27.4887208233, -26.751624886, -26.9545427146, -25.0148469692, -23.2246221102, -22.5531070225, -23.807242893, -24.8339106375, -22.5276696963, -21.3671311534, -22.8534929599, -23.0996998919, -24.23468526, -21.9029121658, -19.9443628471, -18.1197160854, -19.4085769983, -18.486989232, -16.6495560511, -15.0962456643, -16.6013421366, -15.3377220586, -14.3813600008, -13.3280625331, -13.9262154604, -18.7449533519, -16.0203635164, -18.1145404479, -17.9210260158, -19.9409142025, -17.476872232, -17.792142885, -16.8700093193, -16.0022250624, -14.5499062938, -12.3550080239, -12.5318352141, -14.3236083768, -15.3666856466, -14.9085493481, -14.8118491125, -13.3101505216, -13.8847874898, -14.8670677014, -12.3624013755, -12.4622348181, -16.9952024766, -15.717891801, -14.8992075571, -15.7502189436, -14.366539096, -10.2185449952, -12.1521196663, -13.7561515014, -10.1412687481, -8.60637015888, -8.11883785379, -7.7052009615, -7.29466408899, -4.63328461814, -7.1361081287, -8.34949875023, -7.23260998427, -8.29191382455, -7.88971777649, -6.34279104277, -7.49873370776, -7.70619899468, -9.16096718023, -9.95720147114, -8.62688861485, -13.1322431664, -11.6120975623, -11.7132021963, -10.9134239692, -12.7479727573, -13.7416013511, -11.3691821939, -12.6880490137, -8.71572042068, -9.61892540624, -9.38631586307, -9.13128191852, -5.70498286888, -3.9493767315, -4.76809524596, -4.3863764489, -4.27723128634, -4.52879365873, -3.64404379069, -3.48058222756, -1.88007794957, -2.92513430843, -5.63016023458, -2.90852732974, -2.02551919388, -1.54360880806, -3.57665326957, -4.34914114227, -3.32870868591, -0.219084787424, 1.36557544252, 2.24673014628, -1.07442653076, -3.10621933767, -0.960768215919, -3.57794071297, -4.20250067385, -3.11511094665, -2.62378167864, -2.53675186064, -5.11134150661, -5.19769745843, -4.96631353666, -6.73776355606, -7.26387812243, -4.42461984876, -5.04450946013, -1.58845515147, 1.90471522135, 2.60355306132, -0.279824535976, -3.27696365165, -5.20288051495, -3.04920033615, -7.98911362798, -6.23970814517, -6.95332472533, -8.32270413025, -9.4001633076, -11.918302112, -8.32993459451, -6.73148593329, -8.50054811946, -9.08525483019, -8.89099127399, -5.99723236861, -7.99125187017, -7.60776628482, -9.82706914401, -6.95357727161, -3.33845425523, -4.18443130778, -4.42381132355, -0.683673799381, 2.36526783265, 3.79302838549, 3.33088069479, 5.62340610062, 8.58707156183, 6.47372059826, 10.8869508094, 10.8738583391, 13.1268817281, 13.1711071083, 14.8649970248, 15.5206367016, 13.6889326509, 14.7145303194, 14.9931760494, 13.186783327, 12.0848381418, 12.5564181077, 15.8605887338, 14.6976119674, 12.8782837222, 13.474880652, 15.5594193978, 13.4082037663, 10.5447936462, 7.70771969603, 8.88877776247, 8.16832053285, 10.5907956397, 8.92920530467, 11.9587056021, 12.3183866136, 11.6222811299, 11.9832302802, 9.49164191742, 13.6929045555, 13.7174482828, 15.3731387834, 14.681115245, 13.3193033351, 11.3104798564, 10.5669030044, 12.8475449294, 14.4152162182, 15.6749708323, 15.1383358074, 17.0203923645, 17.316660471, 17.54699374, 13.6435372124, 12.8547109713, 15.4915766964, 14.9176747617, 15.8576179519, 13.7360455408, 11.8380892585, 13.0478116202, 14.5784093297, 15.9060361282, 13.1933312553, 16.5210905939, 16.8673123854, 19.5895371967, 19.8849798564, 21.0886887284, 21.7856804274, 20.9125626111, 22.5983377723, 20.0529289768, 18.5984223048, 15.4290881665, 19.4184506831, 23.2386291384, 19.8587903643, 19.9089983229, 20.7265957734, 21.9164490183, 22.1589557078, 20.8943227804, 21.8945654439, 22.5219894327, 20.2613681134, 19.8100108899, 22.5853638926, 21.7002265463, 22.0381079784, 19.9421101201, 20.4766480824, 18.2815422923, 20.6221197792, 17.5729376619, 18.1358187228, 18.7981603205, 20.2026018393, 19.1027779485, 19.0755440265, 22.444493282, 19.6025603699, 19.7542457849, 17.3958653189, 14.4660324783, 12.1026609432, 12.0385229118, 9.82508052837, 9.93292563357, 9.63904258545, 9.40418730684, 12.0868137316, 11.6926026945, 8.99017776787, 9.56022217179, 11.0437325403, 9.3525368411, 7.74714652456, 7.38702150493, 9.28675009086, 9.53325077046, 11.4315134067, 9.28784028749, 9.32249585325, 11.0553484157, 8.48390294724, 7.66670918662, 7.78941306977, 8.6335691464, 7.32788496712, 7.0385336911, 7.21590001592, 9.90334102369, 9.14853824136, 8.58847813058, 6.06443883318, 5.67035622506, 4.01737644663, 4.01734420148, 5.77591643223, 2.01809299994, 2.02917027271, -1.24383005348, -4.35687282059, -2.45763439489, -4.3827722976, -4.49542986034, -8.68822365759, -10.5363433329, -10.3784622661, -7.05863025128, -7.62729937306, -5.567894296, -7.93637658461, -9.27963905117, -10.395537369, -12.481008087, -12.4333587803, -13.7462699811, -12.6118370969, -12.0619882414, -8.75658203557, -6.9763127744, -8.1286836121, -9.16743459482, -7.39819422645, -9.29154547991, -7.96578210809, -6.51764785937, -4.9051828192, -5.68898579493, -6.34985781173, -7.82319377724, -7.75901956071, -9.66192939745, -7.60755934199, -5.42963689518, -6.62921423218, -6.72297232435, -5.73391065107, -4.6498802835, -4.90081665571, -8.809764316, -9.1843493561, -8.81918123244, -9.6255943484, -12.7042835758, -9.17346578116, -8.13744305638, -9.55126791212, -9.33007216686, -11.2262943, -11.6825644231, -16.7878469762, -16.7735400559, -15.9044721462, -14.0842575027, -17.7436558981, -18.9193850012, -18.5454315207, -19.4135643779, -19.6445298207, -21.7051384631, -21.5956034781, -22.0621496057, -22.6494537593, -23.8912764002, -23.1103026949, -24.2391296943, -20.8377464639, -23.028112822, -20.6338334023, -21.4871949212, -19.8162718216, -18.1644899987, -22.0958824103, -22.0270431073, -18.5785721611, -19.3413930134, -20.3206085022, -22.8213222399, -24.2740687768, -24.4591725023, -22.5457072375, -21.1891411901, -24.4399290042, -24.8889222782, -24.2637772359, -24.2438621274, -22.3264155569, -21.2607262813, -21.2130753453, -20.1054233476, -19.6595640861, -18.7362882921, -19.8013009088, -18.1705232927, -18.0754342422, -18.3280354158, -21.0623793983, -23.6920698279, -25.9248679033, -27.004285847, -28.9273211209, -29.1006104525, -28.358715956, -27.12455194, -27.0511444423, -24.8138935884, -24.3905126096, -23.6848501526, -26.2169247063, -28.6045492546, -29.2577360178, -29.1536263289, -28.0383786218, -27.029748175, -24.9696193103, -22.7766533183, -21.6447515725, -21.6817465916, -23.9931224375, -25.9951655224, -27.9944442166, -30.6972909977, -33.401890242, -29.5426274018, -28.8606929306, -27.4916960608, -25.9187155767, -30.0717858184, -27.7698134092, -28.3159857595, -28.466839622, -27.7034034449, -25.1517512904, -25.4580566238, -24.8680173929, -21.3800797372, -20.558581984, -17.0346198543, -19.3092480519, -21.2170286695, -23.0257165241, -21.5186960686, -22.2539845966, -22.0291179181, -23.7404379996, -21.5389131304, -22.4053686362, -23.5937280916, -26.7966568492, -30.5254177897, -26.8985062059, -27.3035811104, -27.5980258296, -27.5794521979, -29.9131709233, -27.0386555708, -28.3622006077, -28.0324084416, -30.0699487113, -30.0934051684, -27.5671295794, -27.0316851006, -27.6475645866, -30.0559602708, -29.8179785685, -33.4825669284, -33.1258340016, -35.0203211268, -35.7915306812, -33.4079355001, -34.8380810798, -34.2221581819, -33.6432853094, -34.2752772357, -34.504671027, -35.8107275649, -37.5089671208, -36.3165680857, -30.1343073683, -30.3557724307, -30.7216616779, -31.621614748, -33.7754787494, -33.1021068968, -35.8390607071, -35.9167837427, -37.5072488338, -38.982010576, -39.3728895287, -38.5927699464, -37.7292360991, -37.0041612648, -39.686573556, -40.8485499107, -41.0307401559, -45.0731212603, -48.1725985766, -48.9621325344, -49.7342553809, -46.2316371662, -48.6209005576, -46.0821121491, -45.9939839419, -46.9487134027, -45.6628396082, -42.2483303164, -38.9453640197, -40.2014889463, -43.9883446121, -44.0836134914, -45.6510170542, -43.2385651473, -45.4781859231, -46.7345339235, -47.853514964, -50.571680577, -52.7903489804, -54.3635691402, -54.9839145482, -54.4739432208, -54.0405642888, -52.8180192286, -54.5412805453, -52.5911438836, -50.8700755608, -51.2990077434, -52.1340195714, -50.7329796818, -51.0952473476, -54.7765691674, -54.5081607195, -51.0607100849, -50.1021485495, -51.037897962, -50.2251185013, -50.6173840477, -48.2249002318, -49.7331848442, -50.3259876082, -53.0280632817, -55.8114178822, -55.9838706563, -52.0663465982, -54.8819989108, -54.8536633015, -52.0227853168, -49.7152078133, -49.8556885209, -51.0353925676, -50.2726794516, -50.5114670021, -51.3474396901, -51.5528467438, -53.3963445238, -52.378406578, -52.4021739403, -50.735987164, -52.7026908119, -52.4930007209, -50.6563605909, -52.0612733217, -51.5570275101, -52.2640132716, -49.6597232359, -48.5667661722, -48.6066113151, -46.4298840263, -46.3144849068, -46.7820082094, -49.1387641487, -49.3157533858, -46.3714523054, -46.6528801479, -47.2431142508, -47.5770553079, -45.0742431441, -46.3311906176, -45.6903153677, -45.6610486313, -41.4725432372, -44.0868119246, -44.0869245532, -44.5302515362, -45.0032739163, -44.9181163709, -45.5908258498, -44.8191127189, -43.8936545108, -44.3296799545, -44.5154986091, -47.2976760074, -47.0453861423, -42.727990522, -42.3023348169, -43.7037655716, -42.3303017105, -42.7572521515, -40.6855189431, -40.9868472206, -44.6729657222, -46.6892026115, -42.5354395605, -42.5707064128, -42.9350230532, -42.4671143658, -41.60720328, -42.8968217411, -41.1911764681, -41.118394706, -40.0152281441, -39.4736702715, -39.3229852027, -37.6629231439, -36.7403462994, -37.0371424763, -40.0039382024, -39.242144328, -38.9292201268, -39.5602867314, -39.9762126838, -38.0653086469, -40.7139157473, -40.0722486547, -38.225750777, -40.600523988, -39.9100873526, -42.4073320174, -44.3047242871, -43.0137527999, -41.3145600393, -45.3788973547, -45.6292073891, -45.6218441646, -44.9627548997, -47.2211590199, -46.7738409224, -49.0616395896, -46.5364968799, -45.7100964764, -44.9534977445, -44.1569948034, -42.2191732772, -40.5324026957, -40.0377290303, -43.1254209088, -45.256628335, -48.333972176, -45.9688539994, -45.7797210684, -43.9456404075, -44.9067438812, -46.1215467713, -44.0308631183, -42.3316779398, -44.3880561434, -45.7564356243, -46.4252130322, -41.707227763, -40.3322626153, -39.4322069472, -37.1367300397, -37.4481609443, -35.9626784214, -36.8375112843, -37.6282914863, -36.1459851739, -38.8918901699, -37.1982636822, -35.8371385418, -36.8407883854, -36.6707639783, -34.22491151, -30.9825111051, -31.3972302642, -29.8381277291, -31.509122265, -27.8723714909, -26.670798014, -23.47216587, -24.0341922219, -23.5867565854, -25.8967584065, -25.5352030366, -24.840261983, -25.943444038, -28.4288145722, -30.0474230701, -27.8354350988, -26.7414696481, -26.6785445437, -28.0693851824, -31.4744589667, -31.4492622572, -33.4749320966, -30.9912177828, -30.3791491865, -31.1142561378, -31.0383397074, -30.7479996191, -29.9717102477, -26.7488931189, -26.9394236787, -28.0323025149, -30.0431302538, -32.2490689382, -30.172571921, -30.9906509656],
z: [-0.643532389175, 1.19440732254, 1.75749718595, -2.08620121257, -3.18393375978, -0.299016207313, 2.64310326227, 2.99111979343, 1.89365407911, 1.85674092968, 0.831097146388, 3.03323250024, 3.02216871173, -0.411437954273, -1.01992224552, -1.85381836367, 1.15482277771, 1.38542071157, -2.7386667156, -6.83226810791, -7.05667136473, -6.88946652346, -9.99828566365, -11.743944794, -11.2879927277, -12.9983010242, -13.5447238575, -10.4930183403, -12.683939164, -10.9783030896, -14.4482022228, -15.248921874, -12.184607962, -10.6262075993, -13.0155758893, -11.9417921191, -13.5224239079, -13.9994597214, -10.1474153836, -11.036154833, -11.3791358395, -9.97457866829, -7.50440544216, -7.48620381739, -6.19370619639, -5.09679388392, -5.18731852317, -5.3551380982, -5.49235851559, -1.54025717009, -1.17360106201, -0.273944212854, -0.682135541354, 0.0308321648382, -0.292478238931, -0.451374869211, -2.1615001662, -5.99370002989, -4.40365146088, -5.31370847772, -3.4264630306, -2.41998315948, -3.21494260782, -2.81592420496, 0.377911612456, 0.927275457514, 1.61759586102, 2.00400820851, 4.38994324236, 5.2843651449, 4.33425608678, 1.46273433905, 1.25768447966, -0.595681205917, 3.47738795473, 3.89560027128, 3.46687420809, 2.84949510439, 3.81156086396, 1.17928703065, 0.508131846098, -1.83877692483, -0.852097132303, -1.86067833297, -2.60358705551, -2.44386147458, -2.31196383671, -4.42164805569, -4.15868601005, -3.93324154433, -5.65856267491, -7.15775320869, -7.97654489314, -7.50237583472, -8.20148145284, -11.9098551171, -10.9318421515, -10.6220961677, -12.0114808196, -12.8553718111, -11.1617140627, -13.6243777377, -11.2236529007, -10.7099851786, -9.11486075577, -8.36022121174, -5.57761555723, -8.55871299477, -11.2141205107, -13.0935460792, -13.0154263716, -11.2152919754, -13.0441525491, -12.8984537744, -12.373315313, -9.53736244925, -7.30993040725, -9.79305983207, -8.11158312728, -6.79117600586, -8.37564977767, -12.7420695918, -12.8535393802, -13.6493586574, -14.9355357181, -16.1167703444, -13.1498528248, -13.4968256622, -13.3758715516, -14.5475300222, -16.7690882776, -18.5249065841, -21.2349978623, -21.6598807891, -24.7874153361, -25.2354510854, -25.5583728867, -26.716313344, -24.6348935498, -23.9964847331, -25.0627199548, -25.4996220204, -23.0199316532, -22.46029955, -23.1373591753, -24.8567424756, -21.5779023833, -21.6922524932, -19.9220155391, -18.9757881888, -19.9043745828, -20.2450014476, -21.0731368154, -21.0410847062, -22.489521948, -22.3682856762, -22.6194234643, -19.5779697099, -17.4180435072, -19.1769659106, -17.1731745235, -16.7274149275, -18.7366223834, -18.6128109768, -18.9447941176, -19.5379520145, -21.3079887275, -22.1004314599, -18.065952868, -17.3152166903, -18.3820706904, -18.8158190303, -17.3555560008, -15.53230266, -17.2398537253, -14.5045677261, -18.2526256422, -17.1090613829, -16.9089947121, -14.2974126237, -16.3046911495, -18.1140440628, -14.1217034457, -13.5354967641, -13.3389231082, -12.6092557139, -11.1893154121, -13.3404733503, -15.0560178043, -12.2817277924, -14.0025997334, -15.8447548176, -14.0664978973, -15.1352927342, -13.8131382632, -11.284188221, -13.2907201026, -12.7021393784, -9.90470964932, -11.1826978486, -12.6745119218, -12.4185706903, -9.97775817499, -9.75270899917, -9.85109830016, -8.81728344441, -8.59662900249, -8.7135434008, -7.8640540401, -7.26185976418, -5.96307465538, -6.73256201874, -8.14545270362, -6.0768699888, -11.5806723447, -12.8809662266, -13.5411080064, -13.6076927665, -12.8297158577, -14.3222471579, -13.8128000302, -15.8625843126, -15.6582015408, -15.505903666, -14.3048723884, -12.817781594, -13.303545923, -14.2455379115, -14.9205598204, -13.7596994925, -14.1575372578, -17.4261671417, -17.1134007469, -14.1336037003, -15.1201608449, -14.8260259366, -16.4256568031, -15.1188205753, -11.9924087981, -14.7227262839, -15.8915932186, -16.2801909418, -15.1936178556, -15.5840106996, -15.9869742518, -15.6766003176, -13.3691540082, -12.7213015002, -10.441617793, -11.0166583377, -12.2452925933, -8.89194886077, -7.541458783, -9.57893835674, -10.9191299774, -9.75216491547, -10.3640715899, -6.60849980632, -2.41485689369, -1.13693673144, -2.66594013123, 0.061724843493, -0.8142451905, -0.716711878336, 1.52662066365, 0.256507217238, 0.655780962832, -2.46410598979, -3.24947218911, -3.74867198142, -3.9760573515, -3.55588821179, -4.79735954425, -4.58655777215, -3.51684319073, -2.89358760766, -0.26989918674, 0.202059442688, 2.68402890397, 0.391588381035, 1.03366757046, -0.409976795928, -2.84022551979, -5.68058302109, -4.86647994855, -7.65765812235, -8.32359271277, -10.4571115529, -11.8670913193, -12.4266242822, -11.0269165507, -11.4199452869, -11.4234565218, -9.61651353791, -10.0310479322, -11.2826809958, -12.4385061783, -13.7593935958, -14.0300708525, -13.5389132951, -12.1852871889, -12.6605858047, -12.7028250667, -14.0509500115, -11.0138296969, -11.2333127382, -8.98999814391, -5.61735664647, -3.61084656276, -3.25503726263, -5.24387708885, -3.28960908022, -4.37335020891, -2.8212120805, -3.15119595976, -3.67889641519, -3.98036857091, -4.92894221632, -3.8090796889, -1.59389344879, -1.56029848361, -3.74277935936, -2.75880822876, -1.99006016983, -4.65920008487, -7.28070075525, -7.11125856405, -9.41889956194, -9.32413428501, -8.528566737, -9.53468037596, -9.23958776523, -7.57784712847, -7.20913067442, -7.14157941774, -4.95154110382, -3.16816748676, -4.42072580513, -5.86914322451, -7.42378011682, -7.00107147338, -6.55444997303, -5.96009495848, -5.83331939799, -6.67539458654, -2.67420630948, -4.45367476787, -1.85127342256, -3.23599014275, -5.64625545598, -4.8767824486, -4.14510132274, -2.56560829194, -3.52978574266, -3.07250186543, -2.96646846799, -0.064529135035, -1.18745213443, 0.557008094672, 2.68586692642, 3.71616419867, 2.35028499991, -0.828629064553, 0.895361146727, 0.555133171775, 0.577970347182, -0.0961985025767, 0.697743103243, -0.237014198389, 0.659373479809, -0.403638760079, 0.212943317239, 0.387974167935, -0.195637617068, -0.368542953084, 1.78216549073, 1.09732029497, 2.41581069008, 5.5396673313, 5.81531413559, 5.69994220951, 7.13428871174, 5.81774026487, 7.90010223271, 7.61129035235, 4.30435828219, 2.68600452468, 2.86045197888, 4.28460855665, 1.78067070891, -1.50617075751, -3.05359007194, -3.27217161828, -4.04262579805, -3.23666120538, -0.996977244805, -0.968387175574, -2.62155712904, -5.17430247273, -7.46606981153, -7.14194630635, -4.85256137062, -6.06001061722, -8.96560166763, -6.24575943584, -4.33933587236, -5.54261577465, -5.55069024227, -3.64398706164, -3.80649376283, -3.78871109106, -4.25145841401, -6.00155130496, -6.61945978286, -5.90443024798, -9.56145143297, -10.5263990293, -10.9529552921, -8.58251061707, -9.05186810701, -10.8691540839, -11.6109190969, -12.8076447277, -12.3159963904, -8.40275745934, -8.71877223988, -8.76630119073, -11.0777652146, -13.8030414977, -12.5841091472, -12.6580004161, -11.6199536518, -14.2131838647, -12.7926124158, -14.9706206323, -14.6125007932, -14.6039417842, -14.2328021104, -15.3853067152, -15.2935961788, -17.3582747239, -17.0906708156, -14.9998344792, -15.4893482927, -13.2470749617, -12.4809656875, -9.71691283491, -10.1597789593, -11.0751562774, -10.359120595, -12.6413386376, -10.7831034863, -11.109193118, -13.7302722812, -12.1340332775, -12.8873748282, -11.6505857786, -11.6455459421, -12.9836447327, -10.7426493947, -6.34620778824, -7.63243163806, -7.28147018552, -7.37419189125, -7.86680673359, -5.92332305125, -3.93854971753, -1.75672235446, -1.99129170903, -2.81292055449, -2.901420476, -0.915424327489, -0.013889661105, 2.53991411835, 3.70818530044, 2.15782624804, 3.403566207, 4.38155567639, 3.99440284919, 2.24249650671, 2.24987219796, 3.20409972654, 2.39870834909, 1.84056504318, 0.242967391902, -1.85731728868, -0.876352218192, 0.320597355843, 1.37831511731, 5.28210740136, 7.50556011874, 8.47344932491, 10.0074381809, 9.83437901498, 7.06225365553, 9.17621835042, 7.03089709174, 5.80924763581, 4.48944911727, 3.27891223077, 3.40125641697, 3.20339954341, 2.07633438109, -0.0468899376899, -2.83445842058, -2.76473326237, -0.963673340661, -0.800120426944, -2.14086282397, -4.93298382642, -5.4672303452, -7.73104952885, -10.7902582636, -6.71510767, -4.67066236883, -4.24182645375, -5.90907649472, -3.02098653264, -3.61710309888, -3.66553896972, -3.26944868887, -3.63600677856, -4.90235856453, -7.12112907498, -10.1051231127, -10.8942925541, -13.7268035793, -16.7589521246, -14.9779756873, -19.4911586204, -19.120186343, -18.9769786621, -18.4107185228, -18.3788871681, -17.558426636, -13.2867184481, -11.3740066735, -10.6219614259, -13.5950443478, -16.0155994821, -16.188953707, -16.8798915385, -16.9156508878, -13.9397573567, -14.9839547336, -18.5835224461, -17.2112088613, -17.9821075424, -14.9940690494, -12.1180995381, -11.2610810019, -14.8455254748, -15.5896889367, -16.9256067407, -17.1555050746, -15.9982480818, -15.4412336272, -18.1831141612, -20.3212092614, -19.3725426167, -21.5407768503, -19.9654846984, -19.1376564095, -18.494201686, -19.2791616247, -17.5488640674, -15.6258095637, -15.8177374473, -14.9712098334, -15.0513550782, -12.4106010023, -10.7657839096, -6.40534640781, -4.52306734519, -1.08434458019, 0.754999648791, -0.204599363248, 1.5707485628, -0.76075250842, -1.1362433844, 1.49226687195, 1.68345179106, 0.730264300645, 1.60044262256, 0.0386290227906, -0.407806180975, 3.19848681022, 1.20262835165, 0.017329064763, -1.62453004241, -2.86030890188, -0.780619233914, -0.795526854223, -2.68802318703, -1.68675009397, -0.450084425415, 1.03350736583, -0.0948882098553, 1.0402792092, 1.67811904034, 2.17504658591, 3.13657006763, 2.25284563484, 0.113135957663, 1.39525633369, 0.925602363615, -0.389184736959, 1.55767165251, 2.08702160474, 2.27189285595, 1.24036082985, 2.59193750943, 2.59586839935, 4.194359209, 5.74590490081, 5.3787251149, 5.60439210243, 4.64968256013, 5.19052487302, 2.44495615527, 4.11910254213, 3.54939456307, 5.35023671946, 4.67748713547, 5.4341264524, 10.7862329775, 10.4663175509, 9.92141503812, 8.07717178024, 9.15395485553, 10.8287607562, 9.37616203578, 7.22847786575, 4.32692310766, 5.40816382749, 6.79015746836, 7.38829777454, 5.96033965979, 5.96374243659, 7.41642749893, 7.05081628985, 7.66693728274, 8.79813023764, 6.42084367919, 6.61579150381, 4.74781932843, 1.46249087301, -1.43455517441, -3.73572174729, -2.48483348177, -3.60990592337, -4.07351341169, -2.33308970381, -2.69135987962, -1.16494898501, -0.887523130986, 0.883563290011, 3.02767280288, 2.9584189162, 2.37540822219, 5.46058591636, 7.76314086786, 9.77203739721, 11.6488972161, 13.4724217907, 12.5273757272, 11.751684738, 12.7470050373, 13.7054343457, 14.5990810879, 13.2564224701, 12.8932997111, 14.5330945838, 16.9305027101, 19.2137888082, 16.3896947344, 14.9794256544, 14.8145556655, 15.287908149, 13.5179483154, 12.5024184908, 13.7786431116, 13.9011712733, 10.5734168581, 8.53481071817, 8.98582675391, 8.85370328153, 10.6937725136, 10.3574473342, 9.36123298751, 10.9211073907, 12.5772483929, 11.7953005038, 11.9136223011, 12.3884656776, 12.213734291, 14.5579896464, 14.5237731242, 13.9944813907, 13.1383816166, 12.0863997231, 11.7624451432, 12.6170922826, 10.6155431406, 8.65389883222, 9.55741457679, 8.71344481854, 8.50852075015, 7.81622625196, 5.86623950207, 7.50855341489, 5.15427346954, 6.50591966113, 8.73036308032, 7.80677059894, 8.56341522301, 5.28641069554, 5.88947826358, 7.74077364087, 9.24352670985, 9.62533926537, 7.95717683266, 6.67111875375, 7.73068471728, 8.77898885207, 9.82150939849, 14.8575484391, 14.8476866376, 12.200094485, 12.8356914375, 10.8568493124, 11.7846166337, 9.52460784168, 8.83268434423, 7.0719467532, 8.27072947667, 10.096028261, 9.49218318504, 5.16989588002, 5.32864998243, 7.68433208748, 8.50619471683, 7.92014978839, 6.40558923181, 5.11325631428, 5.13624175805, 5.26738437259, 3.26603104603, 4.50024983012, 6.97861354396, 7.04637274832, 6.23979539371, 8.36984597078, 8.72192815548, 11.8118509419, 10.7901153775, 9.70771564264, 12.2351390304, 14.1161704053, 14.3358447828, 15.38291936, 13.8100339868, 12.1142369207, 12.973439028, 13.7486717038, 12.3422880985, 11.8317453325, 12.337999585, 18.2080018125, 18.7214101806, 18.4526107697, 17.4741969481, 14.9696181584, 13.9223803612, 16.4392281794, 17.3598555025, 18.8982823741, 16.4711110785, 14.67257486, 18.2618635993, 15.9713921073, 16.3625975727, 16.8607281962, 18.2682393788, 16.1890028687, 13.5338995687, 12.4074020327, 11.5924572047, 13.3735168603, 11.078624657, 8.30997775995, 9.72276976519, 10.7273438327, 8.9284062342, 8.55341176645, 8.89126643065, 10.2424572556, 11.796078924, 10.6898984529, 11.4324981518, 14.928028256, 14.1818122312, 13.8632987039, 13.8362014176, 9.49648745369, 9.6144278068, 11.4613787024, 13.4148537604, 14.4093894939, 15.9384466775, 13.5485792747, 9.58134508281, 12.2711419273, 13.8828734013, 15.7238083042, 15.5149543387, 15.1285807057, 13.8713637465, 12.4668838177, 13.4405950675, 14.9964461035, 17.0072591315, 15.2016427813, 16.8930298739, 19.7600855662, 20.4875790013, 22.0652351542, 22.2079501018, 23.0010306263, 22.455937449, 22.1196680043, 24.131972917, 25.3471094639, 25.8997089724, 27.822942983, 28.9115095605, 24.9134410637, 24.6386387979, 24.1438325104, 24.6963109758, 22.4495740232, 21.2520916036, 23.0725994046, 23.0279169039, 21.0310895911, 20.1069461694, 20.2291856319, 21.0066305271, 22.6133308649, 22.1115279586, 25.5945002958, 29.1879075196, 29.524963945, 32.2896565322, 35.7196248967, 37.3020941126, 38.5821285257, 38.6898449205, 37.2065214351, 39.2367412855, 39.4452598743, 38.2212882947, 39.5502300614, 42.5559933139, 42.9539143665, 43.7926371345, 45.4201296926, 47.6967076437, 47.1133953813, 44.9545905187, 43.8848478947, 42.118818593, 41.0648297327, 41.4282723717, 41.6628996613, 41.2447314464, 39.8550697388, 43.1221728418, 42.6323315834, 40.4708114997, 41.3530681512, 42.0042657548, 44.9057874586, 43.0246201162, 39.0724130196, 39.1192955854, 40.3876917273, 39.9896043037, 40.5334614197, 44.0677916814, 42.5404493398, 41.5157418362, 42.9720123886, 42.0101429323, 42.0251973022, 40.9912666152, 41.6710854963, 42.6860207783, 42.6569186828, 37.5948946284, 36.1834427448, 32.3797459285, 34.8851774351, 34.2129089073, 31.4897427724, 30.148872718, 28.756038061, 27.4767575369, 26.484588824, 24.6492468214, 23.1356501408, 21.1021130629, 22.2889189538, 22.4420331887, 20.8049215931, 21.3898465584, 20.4462811112, 20.7536039087, 20.4148845188, 21.5026829729, 20.1938571488, 17.911969182, 17.6898052512, 20.3262183803, 18.681715743, 18.2414891726, 17.1595355112, 18.4397390366, 18.5010986949, 18.9833738897, 18.625406738, 18.7982533665, 20.2503449557, 20.1900966548, 21.8976506151, 25.7934435849, 28.2355872182, 28.2002020894, 29.113769401, 27.552608069, 25.2348136536, 23.6257865382, 23.9998005245, 27.3138897325, 28.8215659123, 28.6575233266, 31.8506528324, 32.2904144469, 33.017176677, 33.2015565407, 33.9983817028, 35.8675916704, 34.2320351264, 36.8212410606, 39.9344034319, 41.7200077028, 38.8664408964, 38.7134984731, 39.5903152485, 41.4591197685, 42.3424428763, 43.5828395706, 44.1184365119, 42.2642567129, 42.5427873472, 46.1680747417, 44.2698615787, 44.5578944604, 43.324457299, 45.423992088, 43.4429080117, 43.6538433918, 45.1691220294, 44.184581566, 43.5669893999, 45.3169565082, 46.3694388336, 46.4300899337, 46.0670626609, 47.9620349559, 47.4896761901, 47.4978054808, 48.2131269266, 46.8691154607, 47.6124281376, 44.9034535816, 46.5869577459, 46.2961840453, 46.1876627781, 48.2060455481, 47.2958350986, 47.4665692347, 48.5085511364, 46.5414015166, 44.3624913898, 41.9459538589, 40.2530699506, 43.021844556, 44.5968004235, 45.5261375662, 45.350759082],
mode: "lines",
marker: {
color: "#bcbd22",
size: 12,
symbol: "circle",
line: {
color: "rgb(0,0,0)",
width: 0
}
},
line: {
color: "#bcbd22",
width: 1
},
type: "scatter3d"
};
var data = [trace1, trace2, trace3];
var layout = {
autosize: false,
width: 500,
height: 500,
margin: {
l: 0,
r: 0,
b: 0,
t: 65
}
};
var graphOptions = {layout: layout, filename: "random-walk", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Styling Axes Labels
suite: labels
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
name: "Name of Trace 1",
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [1, 0, 3, 2, 5, 4, 7, 6, 8],
name: "Name of Trace 2",
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
title: "Plot Title",
xaxis: {
title: "x Axis",
titlefont: {
family: "Courier New, monospace",
size: 18,
color: "#7f7f7f"
}
},
yaxis: {
title: "y Axis",
titlefont: {
family: "Courier New, monospace",
size: 18,
color: "#7f7f7f"
}
}
};
var graphOptions = {layout: layout, filename: "styling-names", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Setting the Title, Legend Entries, and Axis Titles
permalink: nodejs/figure-labels/
description: How to set the title, legend-entries, and axis-titles in nodejs.
thumbnail: thumbnail/labels.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","labels" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Picnic Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Picnic",
type: "heatmap"
}
];
var layout = {title: "Picnic"};
var graphOptions = {layout: layout, filename: "Picnic-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Earth Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Earth",
type: "heatmap"
}
];
var layout = {title: "Earth"};
var graphOptions = {layout: layout, filename: "Earth-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Blackbody Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Blackbody",
type: "heatmap"
}
];
var layout = {title: "Blackbody"};
var graphOptions = {layout: layout, filename: "Blackbody-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Greens Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Greens",
type: "heatmap"
}
];
var layout = {title: "Greens"};
var graphOptions = {layout: layout, filename: "Greens-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Bluered Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Bluered",
type: "heatmap"
}
];
var layout = {title: "Bluered"};
var graphOptions = {layout: layout, filename: "Bluered-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Portland Heatmap
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Portland",
type: "heatmap"
}
];
var layout = {title: "Portland"};
var graphOptions = {layout: layout, filename: "Portland-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Heatmap with Categorical Axis Labels
suite: heatmap
---
require('plotly')(username, api\_key);
var data = [
{
z: [[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
x: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
y: ["Morning", "Afternoon", "Evening"],
type: "heatmap"
}
];
var graphOptions = {filename: "labelled-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Electric Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Electric",
type: "heatmap"
}
];
var layout = {title: "Electric"};
var graphOptions = {layout: layout, filename: "Electric-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Hot Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Hot",
type: "heatmap"
}
];
var layout = {title: "Hot"};
var graphOptions = {layout: layout, filename: "Hot-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Jet Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Jet",
type: "heatmap"
}
];
var layout = {title: "Jet"};
var graphOptions = {layout: layout, filename: "Jet-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Greys Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "Greys",
type: "heatmap"
}
];
var layout = {title: "Greys"};
var graphOptions = {layout: layout, filename: "Greys-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: RdBu Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "RdBu",
type: "heatmap"
}
];
var layout = {title: "RdBu"};
var graphOptions = {layout: layout, filename: "RdBu-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Basic Heatmap
suite: heatmap
---
require('plotly')(username, api\_key);
var data = [
{
z: [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
type: "heatmap"
}
];
var graphOptions = {filename: "basic-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Custom Colorscale
suite: heatmap
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: [["0.0", "rgb(165,0,38)"], ["0.111111111111", "rgb(215,48,39)"], ["0.222222222222", "rgb(244,109,67)"], ["0.333333333333", "rgb(253,174,97)"], ["0.444444444444", "rgb(254,224,144)"], ["0.555555555556", "rgb(224,243,248)"], ["0.666666666667", "rgb(171,217,233)"], ["0.777777777778", "rgb(116,173,209)"], ["0.888888888889", "rgb(69,117,180)"], ["1.0", "rgb(49,54,149)"]],
type: "heatmap"
}
];
var graphOptions = {filename: "custom-colorscale", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: YlGnBu Colorscale
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "YlGnBu",
type: "heatmap"
}
];
var layout = {title: "YlGnBu"};
var graphOptions = {layout: layout, filename: "YlGnBu-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: YlOrRd Heatmap
suite: heatmap
order: 16
---
require('plotly')(username, api\_key);
var data = [
{
z: [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56], [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57], [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60], [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61], [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63], [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64], [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65], [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66], [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67], [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70], [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71], [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72], [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73], [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76], [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77], [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78], [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81], [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82], [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83], [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84], [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85], [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87], [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91], [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92], [44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93], [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94], [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95], [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96], [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98], [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]],
colorscale: "YlOrRd",
type: "heatmap"
}
];
var layout = {title: "YlOrRd"};
var graphOptions = {layout: layout, filename: "YlOrRd-heatmap", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Heatmaps
permalink: nodejs/heatmaps/
description: How to make a heatmap in nodejs with a matrix. Seven examples of colored and labeled heatmaps with custom colorscales.
thumbnail: thumbnail/heatmap.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","heatmap" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: LaTeX Typesetting
suite: latex
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4],
y: [1, 4, 9, 16],
name: "$\alpha\_{1c} = 352 \pm 11 \text{ km s}^{-1}$",
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4],
y: [0.5, 2, 4.5, 8],
name: "$\beta\_{1c} = 25 \pm 11 \text{ km s}^{-1}$",
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {title: "$\sqrt{(n\_\text{c}(t|{T\_\text{early}}))}$"},
yaxis: {title: "$d, r \text{ (solar radius)}$"}
};
var graphOptions = {layout: layout, filename: "latex", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: LaTeX
permalink: nodejs/LaTeX/
description: How to add LaTeX to nodejs graphs.
thumbnail: thumbnail/latex.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","latex" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Reversed Axes
suite: axes
---
require('plotly')(username, api\_key);
var data = [
{
x: [1, 2],
y: [1, 2],
type: "scatter"
}
];
var layout = {xaxis: {autorange: "reversed"}};
var graphOptions = {layout: layout, filename: "axes-reversed", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Styling and Coloring Axes and the Zero-Line
suite: axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {
showgrid: true,
zeroline: true,
showline: true,
mirror: "ticks",
gridcolor: "#bdbdbd",
gridwidth: 2,
zerolinecolor: "#969696",
zerolinewidth: 4,
linecolor: "#636363",
linewidth: 6
},
yaxis: {
showgrid: true,
zeroline: true,
showline: true,
mirror: "ticks",
gridcolor: "#bdbdbd",
gridwidth: 2,
zerolinecolor: "#969696",
zerolinewidth: 4,
linecolor: "#636363",
linewidth: 6
}
};
var graphOptions = {layout: layout, filename: "axes-lines", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Setting the Range of Axes Manually
suite: axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {range: [2, 5]},
yaxis: {range: [2, 5]}
};
var graphOptions = {layout: layout, filename: "axes-range-manual", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Axes
permalink: nodejs/axes/
description: How to adjust axes properties in nodejs. Seven examples of linear and logarithmic axes, axes titles, and styling and coloring axes and grid lines.
thumbnail: thumbnail/axes.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","axes" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: `nonnegative`, `tozero`, and `normal` Rangemode
suite: axes
---
require('plotly')(username, api\_key);
var data = [
{
x: [2, 4, 6],
y: [-3, 0, 3],
type: "scatter"
}
];
var layout = {
showlegend: false,
xaxis: {
rangemode: "tozero",
autorange: true
},
yaxis: {
rangemode: "nonnegative",
autorange: true
}
};
var graphOptions = {layout: layout, filename: "axes-range-mode", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Toggling Axes Lines, Ticks, Labels, and Autorange
suite: axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {
autorange: true,
showgrid: false,
zeroline: false,
showline: false,
autotick: true,
ticks: "",
showticklabels: false
},
yaxis: {
autorange: true,
showgrid: false,
zeroline: false,
showline: false,
autotick: true,
ticks: "",
showticklabels: false
}
};
var graphOptions = {layout: layout, filename: "axes-booleans", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Set and Style Axes Title Labels and Ticks
suite: axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {
title: "AXIS TITLE",
titlefont: {
family: "Arial, sans-serif",
size: 18,
color: "lightgrey"
},
showticklabels: true,
tickangle: 45,
tickfont: {
family: "Old Standard TT, serif",
size: 14,
color: "black"
},
exponentformat: "e",
showexponent: "All"
},
yaxis: {
title: "AXIS TITLE",
titlefont: {
family: "Arial, sans-serif",
size: 18,
color: "lightgrey"
},
showticklabels: true,
tickangle: 45,
tickfont: {
family: "Old Standard TT, serif",
size: 14,
color: "black"
},
exponentformat: "e",
showexponent: "All"
}
};
var graphOptions = {layout: layout, filename: "axes-labels", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Tick Placement, Color, and Style
suite: axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {
autotick: false,
ticks: "outside",
tick0: 0,
dtick: 0.25,
ticklen: 8,
tickwidth: 4,
tickcolor: "#000"
},
yaxis: {
autotick: false,
ticks: "outside",
tick0: 0,
dtick: 0.25,
ticklen: 8,
tickwidth: 4,
tickcolor: "#000"
}
};
var graphOptions = {layout: layout, filename: "axes-ticks", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Logarithmic Axes
suite: axes
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {
type: "log",
autorange: true
},
yaxis: {
type: "log",
autorange: true
}
};
var graphOptions = {layout: layout, filename: "axes-range-type", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Date Strings
suite: time-series
---
require('plotly')(username, api\_key);
var data = [
{
x: ["2013-10-04 22:23:00", "2013-11-04 22:23:00", "2013-12-04 22:23:00"],
y: [1, 3, 6],
type: "scatter"
}
];
var graphOptions = {filename: "date-axes", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Time Series
permalink: nodejs/time-series/
description: How to plot date and time in nodejs. An example of a time-series plot.
thumbnail: thumbnail/time-series.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","time-series" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Adding Hover Text to Data in Line and Scatter Plots
suite: annotations
---
require('plotly')(username, api\_key);
var data = [
{
x: [0, 1, 2],
y: [1, 3, 2],
mode: "markers",
text: ["Text A", "Text B", "Text C"],
type: "scatter"
}
];
var layout = {title: "Hover over the points to see the text"};
var graphOptions = {layout: layout, filename: "hover-chart-basic", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Multiple Annotations
suite: annotations
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 3, 2, 4, 3, 4, 6, 5],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 5, 1, 2, 2, 3, 4, 2],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
annotations: [
{
x: 2,
y: 5,
xref: "x",
yref: "y",
text: "Annotation Text",
showarrow: true,
arrowhead: 7,
ax: 0,
ay: -40
},
{
x: 4,
y: 4,
xref: "x",
yref: "y",
text: "Annotation Text 2",
showarrow: true,
arrowhead: 7,
ax: 0,
ay: -40
}
]
};
var graphOptions = {layout: layout, filename: "multiple-annotation", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Simple Annotation
suite: annotations
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 3, 2, 4, 3, 4, 6, 5],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 5, 1, 2, 2, 3, 4, 2],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
annotations: [
{
x: 2,
y: 5,
xref: "x",
yref: "y",
text: "Annotation Text",
showarrow: true,
arrowhead: 7,
ax: 0,
ay: -40
}
]
};
var graphOptions = {layout: layout, filename: "simple-annotation", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Custom Text Color and Styling
suite: annotations
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2],
y: [1, 1, 1],
mode: "lines+markers+text",
name: "Lines, Markers and Text",
text: ["Text A", "Text B", "Text C"],
textposition: "top right",
textfont: {
family: "sans serif",
size: 18,
color: "#1f77b4"
},
type: "scatter"
};
var trace2 = {
x: [0, 1, 2],
y: [2, 2, 2],
mode: "lines+markers+text",
name: "Lines and Text",
text: ["Text G", "Text H", "Text I"],
textposition: "bottom",
textfont: {
family: "sans serif",
size: 18,
color: "#ff7f0e"
},
type: "scatter"
};
var data = [trace1, trace2];
var layout = {showlegend: false};
var graphOptions = {layout: layout, filename: "text-chart-styling", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Styling and Coloring Annotations
suite: annotations
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 3, 2, 4, 3, 4, 6, 5],
type: "scatter"
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 5, 1, 2, 2, 3, 4, 2],
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
annotations: [
{
x: 2,
y: 5,
xref: "x",
yref: "y",
text: "max=5",
showarrow: true,
font: {
family: "Courier New, monospace",
size: 16,
color: "#ffffff"
},
align: "center",
arrowhead: 2,
arrowsize: 1,
arrowwidth: 2,
arrowcolor: "#636363",
ax: 20,
ay: -30,
bordercolor: "#c7c7c7",
borderwidth: 2,
borderpad: 4,
bgcolor: "#ff7f0e",
opacity: 0.8
}
]
};
var graphOptions = {layout: layout, filename: "style-annotation", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Adding Text to Data in Line and Scatter Plots
suite: annotations
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2],
y: [1, 1, 1],
mode: "lines+markers+text",
name: "Lines, Markers and Text",
text: ["Text A", "Text B", "Text C"],
textposition: "top",
type: "scatter"
};
var trace2 = {
x: [0, 1, 2],
y: [2, 2, 2],
mode: "markers+text",
name: "Markers and Text",
text: ["Text D", "Text E", "Text F"],
textposition: "bottom",
type: "scatter"
};
var trace3 = {
x: [0, 1, 2],
y: [3, 3, 3],
mode: "lines+text",
name: "Lines and Text",
text: ["Text G", "Text H", "Text I"],
textposition: "bottom",
type: "scatter"
};
var data = [trace1, trace2, trace3];
var layout = {showlegend: false};
var graphOptions = {layout: layout, filename: "text-chart-basic", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Text and Annotations
permalink: nodejs/text-and-annotations/
description: How to add text labels and annotations to plots in nodejs.
thumbnail: thumbnail/annotations.jpg
page\_type: example\_index
display\_as: layout\_opt
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","annotations" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 2D Histogram of a Bivariate Normal Distribution
suite: histogram2d
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
require('plotly')(username, api\_key);
var data = [
{
x: x,
y: y,
type: "histogram2d"
}
];
var graphOptions = {filename: "2d-histogram", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: 2D Histogram Overlaid with a Scatter Chart
suite: histogram2d
---
var x0 = [];
var y0 = [];
var x1 = [];
var y1 = [];
for (var i = 0; i < 500; i ++) {
x0[i] = Math.random() / 5 \* 0.5;
y0[i] = Math.random() / 5 \* 0.5;
}
for (var i = 0; i < 50; i ++) {
x1[i] = Math.random();
y1[i] = Math.random() + 1;
}
var x = [x0, x1]
var y = [y0, y1]
require('plotly')(username, api\_key);
var trace1 = {
x: x0,
y: y0,
mode: "markers",
marker: {
symbol: "circle",
opacity: 0.7
},
type: "scatter"
};
var trace2 = {
x: x1,
y: y1,
mode: "markers",
marker: {
symbol: "square",
opacity: 0.7
},
type: "scatter"
};
var trace3 = {
x: x,
y: y,
type: "histogram2d"
};
var data = [trace1, trace2, trace3];
var graphOptions = {filename: "2d-histogram-scatter", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: 2D Histogram Binning and Styling Options
suite: histogram2d
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
require('plotly')(username, api\_key);
var data = [
{
x: x,
y: y,
histnorm: "probability",
autobinx: false,
xbins: {
start: -3,
end: 3,
size: 0.1
},
autobiny: false,
ybins: {
start: -2.5,
end: 4,
size: 0.1
},
colorscale: [["0", "rgb(12,51,131)"], ["0.25", "rgb(10,136,186)"], ["0.5", "rgb(242,211,56)"], ["0.75", "rgb(242,143,56)"], ["1", "rgb(217,30,30)"]],
type: "histogram2d"
}
];
var graphOptions = {filename: "2d-histogram-options", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: 2D Histograms
permalink: nodejs/2D-Histogram/
description: How to make a 2D histogram in nodejs. A 2D histogram is a visualization of a bivariate distribution.
thumbnail: thumbnail/histogram2d.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","histogram2d" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Bubble Charts
permalink: nodejs/bubble-charts/
description: How to make a bubble chart in nodejs. Examples of scatter charts whose markers have variable color, size, and symbols.
thumbnail: thumbnail/bubble.jpg
page\_type: example\_index
display\_as: chart\_type
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","bubble" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Marker Size, Color, and Symbol as an Array
suite: bubble
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 11, 12, 13],
mode: "markers",
marker: {
color: ["hsl(0,100,40)", "hsl(33,100,40)", "hsl(66,100,40)", "hsl(99,100,40)"],
size: [12, 22, 32, 42],
opacity: [0.6, 0.7, 0.8, 0.9]
},
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4],
y: [11, 12, 13, 14],
mode: "markers",
marker: {
color: "rgb(31, 119, 180)",
size: 18,
symbol: ["circle", "square", "diamond", "cross"]
},
type: "scatter"
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 13, 14, 15],
mode: "markers",
marker: {
size: 18,
line: {
color: ["rgb(120,120,120)", "rgb(120,120,120)", "red", "rgb(120,120,120)"],
width: [2, 2, 6, 2]
}
},
type: "scatter"
};
var data = [trace1, trace2, trace3];
var layout = {showlegend: false};
var graphOptions = {layout: layout, filename: "bubblechart", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Subplots with Shared Axes
suite: subplots
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [2, 3, 4],
type: "scatter"
};
var trace2 = {
x: [20, 30, 40],
y: [5, 5, 5],
xaxis: "x2",
yaxis: "y",
type: "scatter"
};
var trace3 = {
x: [2, 3, 4],
y: [600, 700, 800],
xaxis: "x",
yaxis: "y3",
type: "scatter"
};
var trace4 = {
x: [4000, 5000, 6000],
y: [7000, 8000, 9000],
xaxis: "x4",
yaxis: "y4",
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
xaxis: {domain: [0, 0.45]},
yaxis: {domain: [0, 0.45]},
xaxis4: {
domain: [0.55, 1],
anchor: "y4"
},
xaxis2: {domain: [0.55, 1]},
yaxis3: {domain: [0.55, 1]},
yaxis4: {
domain: [0.55, 1],
anchor: "x4"
}
};
var graphOptions = {layout: layout, filename: "shared-axes-subplots", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Stacked Subplots with a Shared X-Axis
suite: subplots
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2],
y: [10, 11, 12],
type: "scatter"
};
var trace2 = {
x: [2, 3, 4],
y: [100, 110, 120],
yaxis: "y2",
type: "scatter"
};
var trace3 = {
x: [3, 4, 5],
y: [1000, 1100, 1200],
yaxis: "y3",
type: "scatter"
};
var data = [trace1, trace2, trace3];
var layout = {
yaxis: {domain: [0, 0.33]},
legend: {traceorder: "reversed"},
yaxis2: {domain: [0.33, 0.66]},
yaxis3: {domain: [0.66, 1]}
};
var graphOptions = {layout: layout, filename: "stacked-coupled-subplots", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Simple Subplot
suite: subplots
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: "scatter"
};
var trace2 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: "x2",
yaxis: "y2",
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {domain: [0, 0.45]},
yaxis2: {anchor: "x2"},
xaxis2: {domain: [0.55, 1]}
};
var graphOptions = {layout: layout, filename: "simple-subplot", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Multiple Subplots
suite: subplots
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: "scatter"
};
var trace2 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: "x2",
yaxis: "y2",
type: "scatter"
};
var trace3 = {
x: [300, 400, 500],
y: [600, 700, 800],
xaxis: "x3",
yaxis: "y3",
type: "scatter"
};
var trace4 = {
x: [4000, 5000, 6000],
y: [7000, 8000, 9000],
xaxis: "x4",
yaxis: "y4",
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
xaxis: {domain: [0, 0.45]},
yaxis: {domain: [0, 0.45]},
xaxis4: {
domain: [0.55, 1],
anchor: "y4"
},
xaxis3: {
domain: [0, 0.45],
anchor: "y3"
},
xaxis2: {domain: [0.55, 1]},
yaxis2: {
domain: [0, 0.45],
anchor: "x2"
},
yaxis3: {domain: [0.55, 1]},
yaxis4: {
domain: [0.55, 1],
anchor: "x4"
}
};
var graphOptions = {layout: layout, filename: "multiple-subplots", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Custom Sized Subplot
suite: subplots
---
require('plotly')(username, api\_key);
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: "scatter"
};
var trace2 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: "x2",
yaxis: "y2",
type: "scatter"
};
var data = [trace1, trace2];
var layout = {
xaxis: {domain: [0, 0.7]},
yaxis2: {anchor: "x2"},
xaxis2: {domain: [0.8, 1]}
};
var graphOptions = {layout: layout, filename: "custom-size-subplot", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Subplots
permalink: nodejs/subplots/
description: How to make subplots in nodejs. Seven examples of stacked, custom-sized, and gridded subplots.
thumbnail: thumbnail/subplots.jpg
page\_type: example\_index
display\_as: basic
---
{% assign examples = site.posts | where:"language","nodejs" | where:"suite","subplots" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Stacked Subplots
suite: subplots
---
require('plotly')(username, api\_key);
var trace1 = {
x: [0, 1, 2],
y: [10, 11, 12],
type: "scatter"
};
var trace2 = {
x: [2, 3, 4],
y: [100, 110, 120],
xaxis: "x2",
yaxis: "y2",
type: "scatter"
};
var trace3 = {
x: [3, 4, 5],
y: [1000, 1100, 1200],
xaxis: "x3",
yaxis: "y3",
type: "scatter"
};
var data = [trace1, trace2, trace3];
var layout = {
yaxis: {domain: [0, 0.266]},
legend: {traceorder: "reversed"},
xaxis3: {anchor: "y3"},
xaxis2: {anchor: "y2"},
yaxis2: {domain: [0.366, 0.633]},
yaxis3: {domain: [0.733, 1]}
};
var graphOptions = {layout: layout, filename: "stacked-subplots", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
console.log(msg);
});
---
name: Object Constancy
suite: animations
markdown\_content: |
For scatter traces, you may wish to retain a marker's identity as it is updated. If you include an array of string ids with the trace, the marker identity will be retained. By shuffling the ids, the example below shuffles the markers each time the button is pressed.
---
function shuffleInPlace(array) {
for (var i = array.length - 1; i > 0; i--) {
var j = Math.floor(Math.random() \* (i + 1));
var temp = array[i];
array[i] = array[j];
array[j] = temp;
}
}
var ids = ['1', '2', '3', '4', '5', '6'];
Plotly.newPlot('myDiv', [{
x: [1, 0.5, -0.5, -1, -0.5, 0.5],
y: [0, 0.866, 0.866, 0, -0.866, -0.866],
marker:{size:14,
color:['#631357', '#880E4F', '#AD1457',
'#F06292', '#F48FB1']},
ids: ids,
mode: 'markers'
}], {
xaxis: {range: [-3, 3]},
yaxis: {range: [-2, 2]}
});
function animateShuffle() {
shuffleInPlace(ids);
Plotly.animate('myDiv', [{
data: [{ids: ids}]
}]);
}
---
name: Animating Many Frames Quickly
suite: animations
markdown\_content: |
By default and to ensure any properties that cannot be animated are applied to the plot, a full redraw occurs after each transition. This is generally desirable, but hurts performance when you wish to animate frames as quickly as possible. The example below performs a live simulation of the Lorenz attractor and greatly improves the performance by eliminating the redraw with `redraw: false`.
---
var n = 100;
var x = [], y = [], z = [];
var dt = 0.015;
for (i = 0; i < n; i++) {
x[i] = Math.random() \* 2 - 1;
y[i] = Math.random() \* 2 - 1;
z[i] = 30 + Math.random() \* 10;
}
Plotly.newPlot('myDiv', [{
x: x,
y: z,
mode: 'markers'
}], {
xaxis: {range: [-40, 40]},
yaxis: {range: [0, 60]}
})
function compute () {
var s = 10, b = 8/3, r = 28;
var dx, dy, dz;
var xh, yh, zh;
for (var i = 0; i < n; i++) {
dx = s \* (y[i] - x[i]);
dy = x[i] \* (r - z[i]) - y[i];
dz = x[i] \* y[i] - b \* z[i];
xh = x[i] + dx \* dt \* 0.5;
yh = y[i] + dy \* dt \* 0.5;
zh = z[i] + dz \* dt \* 0.5;
dx = s \* (yh - xh);
dy = xh \* (r - zh) - yh;
dz = xh \* yh - b \* zh;
x[i] += dx \* dt;
y[i] += dy \* dt;
z[i] += dz \* dt;
}
}
function update () {
compute();
Plotly.animate('myDiv', {
data: [{x: x, y: z}]
}, {
transition: {
duration: 0
},
frame: {
duration: 0,
redraw: false
}
});
requestAnimationFrame(update);
}
requestAnimationFrame(update);
---
name: Animating Sequences of Frames
suite: animations
markdown\_content: |
The above examples have used one frame at a time. Whether passing objects as frames or referring to frames by name, you may pass multiple frames together in an array. If `null` or `undefined` is passed as the second argument (i.e. `Plotly.animate('myDiv')`), then all defined frames will be animated in sequence.
The third argument of `Plotly.animate` contains animation options. The transition duration defines the amount of time spent interpolating a trace from one state to another (currently limited to scatter traces), while the frame duration defines the total time spent in that state, including time spent transitioning. The example below has two frames, each with their own transition and frame timing.
---
Plotly.newPlot('myDiv', [{
x: [0, 0],
y: [-1, 1],
}], {
xaxis: {range: [-Math.PI, Math.PI]},
yaxis: {range: [-1.3, 1.3]}
}).then(function () {
Plotly.addFrames('myDiv', [
{
data: [{x: [1, -1], y: [0, 0]}],
name: 'frame1'
}, {
data: [{x: [0, 0], y: [-1, 1]}],
name: 'frame2'
}
]);
})
function startAnimation() {
Plotly.animate('myDiv', ['frame1', 'frame2'], {
frame: [
{duration: 1500},
{duration: 500},
],
transition: [
{duration: 800, easing: 'elastic-in'},
{duration: 100, easing: 'cubic-in'},
],
mode: 'afterall'
})
}
---
name: Animating with a Slider
suite: animations
markdown\_content: |
See [Adding Sliders to Animations](https://plotly.com/javascript/gapminder-example/).
---
---
name: Frame Groups and Animation Modes
suite: animations
markdown\_content: |
The following example combines many of these concepts to draw a glass filling with water.
The first row of buttons animates a different set of predefined frames by changing the second argument of `Plotly.animate`. Passing `null` or `undefined` animates all defined frames in sequence, while passing an array of strings (here, the frames in reverse) animates a specific sequence of frames. By passing a plain string (here, `lower` or `upper`), it filters the animated frames to those with a `group` property equal to that name. The stop button is accomplished by interrupting the current animation with an empty list of frames, therefore simply stopping the animation at the end of the current frame.
The second row of buttons animates all frames with different animation modes. The `mode` option defines whether an animation either interrupts or follows the current animation. `immediate` mode discards all queued frames and begins a new sequence immediately. The `next` mode is very similar but doesn't begin the new animation until the \*end\* of the current frame. Finally, `afterall` queues the new frames so that the new animation begins only after all previous animations have completed.
---
var i, j, t, x, y, name;
var frames = [];
var nFrames = 10;
var n = 80;
var reverseFrames = [];
for (i = 0; i < nFrames; i++) {
var fill = 0.1 + 0.9 \* i / (nFrames - 1);
x = [-1];
y = [0];
// A wave across the top:
for (j = 0; j < n; j++) {
t = j / (n - 1);
x.push(-1 - fill + (2 + 2 \* fill) \* t);
y.push(fill + 0.05 \* Math.sin(t \* Math.PI \* 2 \* i));
}
// Close the loop to draw the water:
x.push(1, -1);
y.push(0, 0);
// Choose a name:
name = 'frame' + i;
// Store it in an array so we can animate in reverse order:
reverseFrames.unshift(name);
// Create the frame:
frames.push({
name: name,
data: [{x: x, y: y}],
group: i < nFrames / 2 ? 'lower' : 'upper'
})
}
Plotly.newPlot('myDiv', [{
// Set up the initial water:
x: frames[0].data[0].x,
y: frames[0].data[0].y,
mode: 'lines',
fill: 'toself',
showlegend: false,
line: {simplify: false}
}, {
// Draw a glass:
x: [-1, 1, 2.1, -2.1, -1],
y: [0, 0, 1.1, 1.1, 0],
mode: 'lines',
fill: 'toself',
showlegend: false,
fillcolor: 'rgba(0, 0, 0, 0.1)',
line: {color: 'rgba(100,100,100,0.2)'}
}], {
xaxis: {range: [-3, 3]},
yaxis: {range: [-0.1, 1.5]}
}).then(function() {
// Add the frames so we can animate them:
Plotly.addFrames('myDiv', frames);
});
// Stop the animation by animating to an empty set of frames:
function stopAnimation () {
Plotly.animate('myDiv', [], {mode: 'next'});
}
function startAnimation (groupOrFrames, mode) {
Plotly.animate('myDiv', groupOrFrames, {
transition: {
duration: 500,
easing: 'linear'
},
frame: {
duration: 500,
redraw: false,
},
mode: mode
});
}
---
name: Defining Named Frames with `Plotly.addFrames`
suite: animations
markdown\_content: |
The above examples pass the data itself through the `Plotly.animate` command. You may instead predefine named frames through the `Plotly.addFrames` command. Then, instead of passing frames through `Plotly.animate`, you may simply refer to a frame by name.
Similar to traces, frames are assigned a serial index as they are added. Frames may be updated by passing an array of frame indices. For example, the command to update the frame with index 2 would be `Plotly.addFrames('myDiv', [{...}], [2])`. Frames can be similarly deleted with, for example, `Plotly.deleteFrames('myDiv', [2])`.
The following example uses frames together with an `updatemenu` for interactive transitions.
---
var frames = [
{name: 'sine', data: [{x: [], y: []}]},
{name: 'cosine', data: [{x: [], y: []}]},
{name: 'circle', data: [{x: [], y: []}]},
];
var n = 100;
for (var i = 0; i < n; i++) {
var t = i / (n - 1) \* 2 - 1;
// A sine wave:
frames[0].data[0].x[i] = t \* Math.PI;
frames[0].data[0].y[i] = Math.sin(t \* Math.PI);
// A cosine wave:
frames[1].data[0].x[i] = t \* Math.PI;
frames[1].data[0].y[i] = Math.cos(t \* Math.PI);
// A circle:
frames[2].data[0].x[i] = Math.sin(t \* Math.PI);
frames[2].data[0].y[i] = Math.cos(t \* Math.PI);
}
Plotly.newPlot('myDiv', [{
x: frames[0].data[0].x,
y: frames[0].data[0].y,
line: {simplify: false},
}], {
xaxis: {range: [-Math.PI, Math.PI]},
yaxis: {range: [-1.2, 1.2]},
updatemenus: [{
buttons: [
{method: 'animate', args: [['sine']], label: 'sine'},
{method: 'animate', args: [['cosine']], label: 'cosine'},
{method: 'animate', args: [['circle']], label: 'circle'}
]
}]
}).then(function() {
Plotly.addFrames('myDiv', frames);
});
---
name: Animating the Layout
suite: animations
markdown\_content: |
The example below transitions to a new axis range each time the button is pressed. A present limitation of the animate API is that only one of either data or layout may be smoothly transitioned at a time. If both are provided, the data will be updated instantaneously after the layout is transitioned.
---
var n = 500;
var x = [], y = [];
for (var i = 0; i < n; i++) {
x[i] = i / (n - 1);
y[i] = x[i] + 0.2 \* (Math.random() - 0.5);
}
Plotly.newPlot('myDiv', [{
x: x,
y: y,
mode: 'markers'
}], {
xaxis: {range: [0, 1]},
yaxis: {range: [0, 1]}
});
function zoom() {
var min = 0.45 \* Math.random();
var max = 0.55 + 0.45 \* Math.random();
Plotly.animate('myDiv', {
layout: {
xaxis: {range: [min, max]},
yaxis: {range: [min, max]}
}
}, {
transition: {
duration: 500,
easing: 'cubic-in-out'
}
})
}
---
name: Animating the Data
suite: animations
markdown\_content: |
The animate command lets you add dynamic behavior to Plotly graphs in a number of different ways. At its core, `Plotly.animate` transitions traces to a new state or sequence of states. When you tell Plotly to animate, it merges the properties you've supplied into the current state of the plot. Therefore to animate a trace, \*you must first plot the trace you wish to animate\*.
The example below transitions to new y-values each time the button is pressed. Since the transition animation occurs within a frame, `frame.duration` must be set at least as long as `transition.duration`. Note that to prevent artifacts while animating, the default line simplification algorithm is explicitly disabled. Currently, only scatter traces may be smoothly transitioned from one state to the next. Other traces are compatible with frames and animations but will be updated instantaneously.
---
Plotly.newPlot('myDiv', [{
x: [1, 2, 3],
y: [0, 0.5, 1],
line: {simplify: false},
}]);
function randomize() {
Plotly.animate('myDiv', {
data: [{y: [Math.random(), Math.random(), Math.random()]}],
traces: [0],
layout: {}
}, {
transition: {
duration: 500,
easing: 'cubic-in-out'
},
frame: {
duration: 500
}
})
}
---
name: Animating with a Slider
suite: adding-sliders
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv', function (err, data) {
// Create a lookup table to sort and regroup the columns of data,
// first by year, then by continent:
var lookup = {};
function getData(year, continent) {
var byYear, trace;
if (!(byYear = lookup[year])) {;
byYear = lookup[year] = {};
}
// If a container for this year + continent doesn't exist yet,
// then create one:
if (!(trace = byYear[continent])) {
trace = byYear[continent] = {
x: [],
y: [],
id: [],
text: [],
marker: {size: []}
};
}
return trace;
}
// Go through each row, get the right trace, and append the data:
for (var i = 0; i < data.length; i++) {
var datum = data[i];
var trace = getData(datum.year, datum.continent);
trace.text.push(datum.country);
trace.id.push(datum.country);
trace.x.push(datum.lifeExp);
trace.y.push(datum.gdpPercap);
trace.marker.size.push(datum.pop);
}
// Get the group names:
var years = Object.keys(lookup);
// In this case, every year includes every continent, so we
// can just infer the continents from the \*first\* year:
var firstYear = lookup[years[0]];
var continents = Object.keys(firstYear);
// Create the main traces, one for each continent:
var traces = [];
for (i = 0; i < continents.length; i++) {
var data = firstYear[continents[i]];
// One small note. We're creating a single trace here, to which
// the frames will pass data for the different years. It's
// subtle, but to avoid data reference problems, we'll slice
// the arrays to ensure we never write any new data into our
// lookup table:
traces.push({
name: continents[i],
x: data.x.slice(),
y: data.y.slice(),
id: data.id.slice(),
text: data.text.slice(),
mode: 'markers',
marker: {
size: data.marker.size.slice(),
sizemode: 'area',
sizeref: 200000
}
});
}
// Create a frame for each year. Frames are effectively just
// traces, except they don't need to contain the \*full\* trace
// definition (for example, appearance). The frames just need
// the parts the traces that change (here, the data).
var frames = [];
for (i = 0; i < years.length; i++) {
frames.push({
name: years[i],
data: continents.map(function (continent) {
return getData(years[i], continent);
})
})
}
// Now create slider steps, one for each frame. The slider
// executes a plotly.js API command (here, Plotly.animate).
// In this example, we'll animate to one of the named frames
// created in the above loop.
var sliderSteps = [];
for (i = 0; i < years.length; i++) {
sliderSteps.push({
method: 'animate',
label: years[i],
args: [[years[i]], {
mode: 'immediate',
transition: {duration: 300},
frame: {duration: 300, redraw: false},
}]
});
}
var layout = {
xaxis: {
title: {text: 'Life Expectancy'},
range: [30, 85]
},
yaxis: {
title: {text: 'GDP per Capita'},
type: 'log'
},
hovermode: 'closest',
// We'll use updatemenus (whose functionality includes menus as
// well as buttons) to create a play button and a pause button.
// The play button works by passing `null`, which indicates that
// Plotly should animate all frames. The pause button works by
// passing `[null]`, which indicates we'd like to interrupt any
// currently running animations with a new list of frames. Here
// The new list of frames is empty, so it halts the animation.
updatemenus: [{
x: 0,
y: 0,
yanchor: 'top',
xanchor: 'left',
showactive: false,
direction: 'left',
type: 'buttons',
pad: {t: 87, r: 10},
buttons: [{
method: 'animate',
args: [null, {
mode: 'immediate',
fromcurrent: true,
transition: {duration: 300},
frame: {duration: 500, redraw: false}
}],
label: 'Play'
}, {
method: 'animate',
args: [[null], {
mode: 'immediate',
transition: {duration: 0},
frame: {duration: 0, redraw: false}
}],
label: 'Pause'
}]
}],
// Finally, add the slider and use `pad` to position it
// nicely next to the buttons.
sliders: [{
pad: {l: 130, t: 55},
currentvalue: {
visible: true,
prefix: 'Year:',
xanchor: 'right',
font: {size: 20, color: '#666'}
},
steps: sliderSteps
}]
};
// Create the plot:
Plotly.newPlot('myDiv', {
data: traces,
layout: layout,
frames: frames,
});
});
---
name: Animations
permalink: javascript/animations/
description: How to animate charts in JavaScript with the animate API.
thumbnail: thumbnail/animations.gif
page\_type: example\_index
display\_as: animations
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","animations" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Multiple Trace Filled-Area
suite: filled-area-animations
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var frames = []
var x = unpack(rows, 'Date')
var y = unpack(rows, 'AAPL.High')
var x2 = unpack(rows, 'Date')
var y2 = unpack(rows, 'AAPL.Low')
var n = 100;
for (var i = 0; i < n; i++) {
frames[i] = {data: [{x: [], y: []}, {x: [], y: []}]}
frames[i].data[1].x = x.slice(0, i+1);
frames[i].data[1].y = y.slice(0, i+1);
frames[i].data[0].x = x2.slice(0, i+1);
frames[i].data[0].y = y2.slice(0, i+1);
}
var trace2 = {
type: "scatter",
mode: "lines",
name: 'AAPL High',
fill: 'tonexty',
x: frames[5].data[1].x,
y: frames[5].data[1].y,
line: {color: 'grey'}
}
var trace1 = {
type: "scatter",
mode: "lines",
name: 'AAPL Low',
x: frames[5].data[0].x,
y: frames[5].data[0].y,
line: {color: 'lightgrey'}
}
var data = [trace1,trace2];
var layout = {
title: {
text: 'Multiple Trace Filled-Area Animation'
},
xaxis: {
range: [frames[99].data[0].x[0], frames[99].data[0].x[99]],
showgrid: false
},
yaxis: {
range: [120, 140],
showgrid: false
},
legend: {
orientation: 'h',
x: 0.5,
y: 1.2,
xanchor: 'center'
},
updatemenus: [{
x: 0.5,
y: 0,
yanchor: "top",
xanchor: "center",
showactive: false,
direction: "left",
type: "buttons",
pad: {"t": 87, "r": 10},
buttons: [{
method: "animate",
args: [null, {
fromcurrent: true,
transition: {
duration: 0,
},
frame: {
duration: 40,
redraw: false
}
}],
label: "Play"
}, {
method: "animate",
args: [
[null],
{
mode: "immediate",
transition: {
duration: 0
},
frame: {
duration: 0,
redraw: false
}
}
],
label: "Pause"
}]
}]
};
Plotly.newPlot('myDiv', data, layout).then(function() {
Plotly.addFrames('myDiv', frames);
});
})
---
name: Filled-Area-Animation
suite: filled-area-animations
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/2014\_apple\_stock.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var frames = []
var x = unpack(rows, 'AAPL\_x')
var y = unpack(rows, 'AAPL\_y')
var n = 100;
for (var i = 0; i < n; i++) {
frames[i] = {data: [{x: [], y: []}]}
frames[i].data[0].x = x.slice(0, i+1);
frames[i].data[0].y = y.slice(0, i+1);
}
Plotly.newPlot('myDiv', [{
x: frames[1].data[0].x,
y: frames[1].data[0].y,
fill: 'tozeroy',
type: 'scatter',
mode: 'lines',
line: {color: 'green'}
}], {
title: {
text: "Filled-Area Animation"
},
xaxis: {
type: 'date',
range: [
frames[99].data[0].x[0],
frames[99].data[0].x[99]
]
},
yaxis: {
range: [
0,
90
]
},
updatemenus: [{
x: 0.1,
y: 0,
yanchor: "top",
xanchor: "right",
showactive: false,
direction: "left",
type: "buttons",
pad: {"t": 87, "r": 10},
buttons: [{
method: "animate",
args: [null, {
fromcurrent: true,
transition: {
duration: 0,
},
frame: {
duration: 40,
redraw: false
}
}],
label: "Play"
}, {
method: "animate",
args: [
[null],
{
mode: "immediate",
transition: {
duration: 0
},
frame: {
duration: 0,
redraw: false
}
}
],
label: "Pause"
}]
}]
}).then(function() {
Plotly.addFrames('myDiv', frames);
});
})
---
name: Map Animation
permalink: javascript/map-animations/
description: How to make an animated map with Plotly JS
thumbnail: thumbnail/map-animation.gif
page\_type: example\_index
display\_as: animations
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","map-animations" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Map Animations
suite: map-animations
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder\_with\_codes.csv", function(err, rows){
function filter\_and\_unpack(rows, key, year) {
return rows.filter(row => row['year'] == year).map(row => row[key])
}
var frames = []
var slider\_steps = []
var n = 11;
var num = 1952;
for (var i = 0; i <= n; i++) {
var z = filter\_and\_unpack(rows, 'lifeExp', num)
var locations = filter\_and\_unpack(rows, 'iso\_alpha', num)
frames[i] = {data: [{z: z, locations: locations, text: locations}], name: num}
slider\_steps.push ({
label: num.toString(),
method: "animate",
args: [[num], {
mode: "immediate",
transition: {duration: 300},
frame: {duration: 300}
}
]
})
num = num + 5
}
var data = [{
type: 'choropleth',
locationmode: 'world',
locations: frames[0].data[0].locations,
z: frames[0].data[0].z,
text: frames[0].data[0].locations,
zauto: false,
zmin: 30,
zmax: 90
}];
var layout = {
title: {
text: 'World Life Expectency
1952 - 2007'
},
geo:{
scope: 'world',
countrycolor: 'rgb(255, 255, 255)',
showland: true,
landcolor: 'rgb(217, 217, 217)',
showlakes: true,
lakecolor: 'rgb(255, 255, 255)',
subunitcolor: 'rgb(255, 255, 255)',
lonaxis: {},
lataxis: {}
},
updatemenus: [{
x: 0.1,
y: 0,
yanchor: "top",
xanchor: "right",
showactive: false,
direction: "left",
type: "buttons",
pad: {"t": 87, "r": 10},
buttons: [{
method: "animate",
args: [null, {
fromcurrent: true,
transition: {
duration: 200,
},
frame: {
duration: 500
}
}],
label: "Play"
}, {
method: "animate",
args: [
[null],
{
mode: "immediate",
transition: {
duration: 0
},
frame: {
duration: 0
}
}
],
label: "Pause"
}]
}],
sliders: [{
active: 0,
steps: slider\_steps,
x: 0.1,
len: 0.9,
xanchor: "left",
y: 0,
yanchor: "top",
pad: {t: 50, b: 10},
currentvalue: {
visible: true,
prefix: "Year:",
xanchor: "right",
font: {
size: 20,
color: "#666"
}
},
transition: {
duration: 300,
easing: "cubic-in-out"
}
}]
};
Plotly.newPlot('myDiv', data, layout).then(function() {
Plotly.addFrames('myDiv', frames);
});
})
---
name: Stacked Histograms
suite: histogram
---
var x1 = [];
var x2 = [];
for (var i = 0; i < 500; i ++) {
x1[i] = Math.random();
x2[i] = Math.random();
}
var trace1 = {
x: x1,
type: "histogram",
};
var trace2 = {
x: x2,
type: "histogram",
};
var data = [trace1, trace2];
var layout = {barmode: "stack"};
Plotly.newPlot('myDiv', data, layout);
---
name: Normalized Histogram
suite: histogram
---
var x = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
}
var data = [
{
x: x,
type: 'histogram',
histnorm: 'probability',
marker: {
color: 'rgb(255,255,100)',
},
}
];
Plotly.newPlot('myDiv', data);
---
name: Specify Binning Function
suite: histogram
order: 10
---
var x = ["Apples","Apples","Apples","Oranges", "Bananas"]
var y = ["5","10","3","10","5"]
var data = [
{
histfunc: "count",
y: y,
x: x,
type: "histogram",
name: "count"
},
{
histfunc: "sum",
y: y,
x: x,
type: "histogram",
name: "sum"
}
]
Plotly.newPlot('myDiv', data)
---
name: Cumulative Histogram
suite: histogram
---
var x = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
}
var trace = {
x: x,
type: 'histogram',
cumulative: {enabled: true}
};
var data = [trace];
Plotly.newPlot('myDiv', data);
---
name: Horizontal Histogram
suite: histogram
---
var y = [];
for (var i = 0; i < 500; i ++) {
y[i] = Math.random();
}
var data = [
{
y: y,
type: 'histogram',
marker: {
color: 'pink',
},
}
];
Plotly.newPlot('myDiv', data);
---
name: Basic Histogram
suite: histogram
---
var x = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
}
var trace = {
x: x,
type: 'histogram',
};
var data = [trace];
Plotly.newPlot('myDiv', data);
---
name: Colored and Styled Histograms
suite: histogram
---
var x1 = [];
var x2 = [];
var y1 = [];
var y2 = [];
for (var i = 1; i < 500; i++)
{
k = Math.random();
x1.push(k\*5);
x2.push(k\*10);
y1.push(k);
y2.push(k\*2);
}
var trace1 = {
x: x1,
y: y1,
name: 'control',
autobinx: false,
histnorm: "count",
marker: {
color: "rgba(255, 100, 102, 0.7)",
line: {
color: "rgba(255, 100, 102, 1)",
width: 1
}
},
opacity: 0.5,
type: "histogram",
xbins: {
end: 2.8,
size: 0.06,
start: .5
}
};
var trace2 = {
x: x2,
y: y2,
autobinx: false,
marker: {
color: "rgba(100, 200, 102, 0.7)",
line: {
color: "rgba(100, 200, 102, 1)",
width: 1
}
},
name: "experimental",
opacity: 0.75,
type: "histogram",
xbins: {
end: 4,
size: 0.06,
start: -3.2
}
};
var data = [trace1, trace2];
var layout = {
bargap: 0.05,
bargroupgap: 0.2,
barmode: "overlay",
title: {
text: "Sampled Results"
},
xaxis: {
title: {
text: "Value"
}
},
yaxis: {
title: {
text: "Count"
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based histogram in JavaScript. Seven examples of
colored, horizontal, and normal histogram bar charts.
display\_as: statistical
name: Histograms
page\_type: example\_index
permalink: javascript/histograms/
plottype: histogram
redirect\_from: javascript-graphing-library/histograms/
thumbnail: thumbnail/histogram.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","histogram" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Overlaid Histogram
suite: histogram
---
var x1 = [];
var x2 = [];
for (var i = 1; i < 500; i++)
{
k = Math.random();
x1.push(Math.random() + 1);
x2.push(Math.random() + 1.1);
}
var trace1 = {
x: x1,
type: "histogram",
opacity: 0.5,
marker: {
color: 'green',
},
};
var trace2 = {
x: x2,
type: "histogram",
opacity: 0.6,
marker: {
color: 'red',
},
};
var data = [trace1, trace2];
var layout = {barmode: "overlay"};
Plotly.newPlot('myDiv', data, layout);
---
name: Colored Box Plot
suite: box
---
var trace1 = {
y: [1, 2, 3, 4, 4, 4, 8, 9, 10],
type: 'box',
name: 'Sample A',
marker:{
color: 'rgb(214,12,140)'
}
};
var trace2 = {
y: [2, 3, 3, 3, 3, 5, 6, 6, 7],
type: 'box',
name: 'Sample B',
marker:{
color: 'rgb(0,128,128)'
}
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Colored Box Plot'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Box Plot Styling Mean and Standard Deviation
suite: box
---
var trace1 = {
y: [2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51, 0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19],
type: 'box',
name: 'Only Mean',
marker: {
color: 'rgb(8,81,156)'
},
boxmean: true
};
var trace2 = {
y: [2.37, 2.16, 4.82, 1.73, 1.04, 0.23, 1.32, 2.91, 0.11, 4.51, 0.51, 3.75, 1.35, 2.98, 4.50, 0.18, 4.66, 1.30, 2.06, 1.19],
type: 'box',
name: 'Mean and Standard Deviation',
marker: {
color: 'rgb(10,140,208)'
},
boxmean: 'sd'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Box Plot Styling Mean and Standard Deviation'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Grouped Box Plot
suite: box
---
var x = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']
var trace1 = {
y: [0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
x: x,
name: 'kale',
marker: {color: '#3D9970'},
type: 'box'
};
var trace2 = {
y: [0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
x: x,
name: 'radishes',
marker: {color: '#FF4136'},
type: 'box'
};
var trace3 = {
y: [0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
x: x,
name: 'carrots',
marker: {color: '#FF851B'},
type: 'box'
};
var data = [trace1, trace2, trace3];
var layout = {
yaxis: {
title: {
text: 'normalized moisture'
},
zeroline: false
},
boxmode: 'group'
};
Plotly.newPlot('myDiv', data, layout);
---
name: Basic Box Plot
suite: box
---
var y0 = [];
var y1 = [];
for (var i = 0; i < 50; i ++) {
y0[i] = Math.random();
y1[i] = Math.random() + 1;
}
var trace1 = {
y: y0,
type: 'box'
};
var trace2 = {
y: y1,
type: 'box'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
name: Box Plot Styling Outliers
suite: box
---
var trace1 = {
y: [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
type: 'box',
name: 'All Points',
jitter: 0.3,
pointpos: -1.8,
marker: {
color: 'rgb(7,40,89)'
},
boxpoints: 'all'
};
var trace2 = {
y: [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
type: 'box',
name: 'Only Wiskers',
marker: {
color: 'rgb(9,56,125)'
},
boxpoints: false
};
var trace3 = {
y: [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
type: 'box',
name: 'Suspected Outlier',
marker: {
color: 'rgb(8,81,156)',
outliercolor: 'rgba(219, 64, 82, 0.6)',
line: {
outliercolor: 'rgba(219, 64, 82, 1.0)',
outlierwidth: 2
}
},
boxpoints: 'suspectedoutliers'
};
var trace4 = {
y: [0.75, 5.25, 5.5, 6, 6.2, 6.6, 6.80, 7.0, 7.2, 7.5, 7.5, 7.75, 8.15, 8.15, 8.65, 8.93, 9.2, 9.5, 10, 10.25, 11.5, 12, 16, 20.90, 22.3, 23.25],
type: 'box',
name: 'Wiskers and Outliers',
marker: {
color: 'rgb(107,174,214)'
},
boxpoints: 'Outliers'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'Box Plot Styling Outliers'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Rainbow Box Plot
suite: box
order: 12
---
function linspace(a,b,n) {
return d3.range(n).map(function(i){return a+i\*(b-a)/(n-1);});
}
var boxNumber = 30;
var boxColor = [];
var allColors = linspace(0, 360, boxNumber);
var data = [];
var yValues = [];
//Colors
for( var i = 0; i < boxNumber; i++ ){
var result = 'hsl('+ allColors[i] +',50%'+',50%)';
boxColor.push(result);
}
function getRandomArbitrary(min, max) {
return Math.random() \* (max - min) + min;
};
//Create Y Values
for( var i = 0; i < boxNumber; i++ ){
var ySingleArray = [];
for( var j = 0; j < 10; j++ ){
var randomNum = getRandomArbitrary(0, 1);
var yIndValue = 3.5\*Math.sin(Math.PI \* i/boxNumber) + i/boxNumber+(1.5+0.5\*Math.cos(Math.PI\*i/boxNumber))\*randomNum;
ySingleArray.push(yIndValue);
}
yValues.push(ySingleArray);
}
//Create Traces
for( var i = 0; i < boxNumber; i++ ){
var result = {
y: yValues[i],
type:'box',
marker:{
color: boxColor[i]
}
};
data.push(result);
};
//Format the layout
var layout = {
xaxis: {
showgrid: false,
zeroline: false,
tickangle: 60,
showticklabels: false
},
yaxis: {
zeroline: false,
gridcolor: 'white'
},
paper\_bgcolor: 'rgb(233,233,233)',
plot\_bgcolor: 'rgb(233,233,233)',
showlegend:false
};
Plotly.newPlot('myDiv', data, layout);
---
name: Fully Styled Box Plot
suite: box
order: 10
---
var xData = ['Carmelo
Anthony', 'Dwyane
Wade',
'Deron
Williams', 'Brook
Lopez',
'Damian
Lillard', 'David
West',
'Blake
Griffin', 'David
Lee',
'Demar
Derozan'];
function getrandom(num , mul) {
var value = [ ];
for ( i = 0; i <= num; i++ ) {
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var yData = [
getrandom(30 ,10),
getrandom(30, 20),
getrandom(30, 25),
getrandom(30, 40),
getrandom(30, 45),
getrandom(30, 30),
getrandom(30, 20),
getrandom(30, 15),
getrandom(30, 43),
];
var colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)', 'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)', 'rgba(255, 140, 184, 0.5)', 'rgba(79, 90, 117, 0.5)', 'rgba(222, 223, 0, 0.5)'];
var data = [];
for ( var i = 0; i < xData.length; i ++ ) {
var result = {
type: 'box',
y: yData[i],
name: xData[i],
boxpoints: 'all',
jitter: 0.5,
whiskerwidth: 0.2,
fillcolor: 'cls',
marker: {
size: 2
},
line: {
width: 1
}
};
data.push(result);
};
layout = {
title: {
text: 'Points Scored by the Top 9 Scoring NBA Players in 2012'
},
yaxis: {
autorange: true,
showgrid: true,
zeroline: true,
dtick: 5,
gridcolor: 'rgb(255, 255, 255)',
gridwidth: 1,
zerolinecolor: 'rgb(255, 255, 255)',
zerolinewidth: 2
},
margin: {
l: 40,
r: 30,
b: 80,
t: 100
},
paper\_bgcolor: 'rgb(243, 243, 243)',
plot\_bgcolor: 'rgb(243, 243, 243)',
showlegend: false
};
Plotly.newPlot('myDiv', data, layout);
---
name: Grouped Horizontal Box Plot
suite: box
---
var y = ['day 1', 'day 1', 'day 1', 'day 1', 'day 1', 'day 1',
'day 2', 'day 2', 'day 2', 'day 2', 'day 2', 'day 2']
var trace1 = {
x: [0.2, 0.2, 0.6, 1.0, 0.5, 0.4, 0.2, 0.7, 0.9, 0.1, 0.5, 0.3],
y: y,
name: 'kale',
marker: {color: '#3D9970'},
type: 'box',
boxmean: false,
orientation: 'h'
};
var trace2 = {
x: [0.6, 0.7, 0.3, 0.6, 0.0, 0.5, 0.7, 0.9, 0.5, 0.8, 0.7, 0.2],
y: y,
name: 'radishes',
marker: {color: '#FF4136'},
type: 'box',
boxmean: false,
orientation: 'h'
};
var trace3 = {
x: [0.1, 0.3, 0.1, 0.9, 0.6, 0.6, 0.9, 1.0, 0.3, 0.6, 0.8, 0.5],
y: y,
name: 'carrots',
marker: {color: '#FF851B'},
type: 'box',
boxmean: false,
orientation: 'h'
};
var data = [trace1, trace2, trace3];
var layout = {
title: {
text: 'Grouped Horizontal Box Plot'
},
xaxis: {
title: {
text: 'normalized moisture'
},
zeroline: false
},
boxmode: 'group'
};
Plotly.newPlot('myDiv', data, layout);
---
name: Horizontal Box Plot
suite: box
---
var trace1 = {
x: [1, 2, 3, 4, 4, 4, 8, 9, 10],
type: 'box',
name: 'Set 1'
};
var trace2 = {
x: [2, 3, 3, 3, 3, 5, 6, 6, 7],
type: 'box',
name: 'Set 2'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Horizontal Box Plot'
},
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based box plot in javascript. Seven examples of box
plots in javascript that are grouped, colored, and display the underlying data distribution.
display\_as: statistical
name: Box Plots
page\_type: example\_index
permalink: javascript/box-plots/
redirect\_from: javascript-graphing-library/box-plots/
thumbnail: thumbnail/box.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","box" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Box Plot That Displays the Underlying Data
suite: box
---
var data = [
{
y: [0, 1, 1, 2, 3, 5, 8, 13, 21],
boxpoints: 'all',
jitter: 0.3,
pointpos: -1.8,
type: 'box'
}
];
Plotly.newPlot('myDiv', data);
---
description: How to make a D3.js-based SPC Control Charts in javascript.
display\_as: statistical
name: SPC Control Charts
permalink: javascript/spc-control-charts/
thumbnail: thumbnail/SPC.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","SPC" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: SPC Control Chart & Distribution
suite: SPC
description:
---
var Data = {
type: 'scatter',
x: [1,2,3,4,5,6,7,8,9],
y: [4,2,-1,4,-5,-7,0,3,8],
mode: 'lines+markers',
name: 'Data',
showlegend: true,
hoverinfo: 'all',
line: {
color: 'blue',
width: 2
},
marker: {
color: 'blue',
size: 8,
symbol: 'circle'
}
}
var Viol = {
type: 'scatter',
x: [6,9],
y: [-7,8],
mode: 'markers',
name: 'Violation',
showlegend: true,
marker: {
color: 'rgb(255,65,54)',
line: {width: 3},
opacity: 0.5,
size: 12,
symbol: 'circle-open'
}
}
var CL = {
type: 'scatter',
x: [0.5, 10, null, 0.5, 10],
y: [-5, -5, null, 5, 5],
mode: 'lines',
name: 'LCL/UCL',
showlegend: true,
line: {
color: 'red',
width: 2,
dash: 'dash'
}
}
var Centre = {
type: 'scatter',
x: [0.5, 10],
y: [0, 0],
mode: 'lines',
name: 'Centre',
showlegend: true,
line: {
color: 'grey',
width: 2
}
}
var histo = {
type: 'histogram',
x: [1,2,3,4,5,6,7,8,9],
y: [4,2,-1,4,-5,-7,0,3,8],
name: 'Distribution',
orientation: 'h',
marker: {
color: 'blue',
line: {
color: 'white',
width: 1
}
},
xaxis: 'x2',
yaxis: 'y2'
}
var data = [Data,Viol,CL,Centre,histo]
// layout
var layout = {
title: {
text: 'Basic SPC Chart'
},
xaxis: {
domain: [0, 0.7], // 0 to 70% of width
zeroline: false
},
yaxis: {
range: [-10,10],
zeroline: false
},
xaxis2: {
domain: [0.8, 1] // 70 to 100% of width
},
yaxis2: {
anchor: 'x2',
showticklabels: false
}
}
Plotly.newPlot('myDiv', data,layout);
---
name: Basic SPC Control Chart
suite: SPC
description:
---
var Data = {
type: 'scatter',
x: [1,2,3,4,5,6,7,8,9],
y: [4,2,-1,4,-5,-7,0,3,8],
mode: 'lines+markers',
name: 'Data',
showlegend: true,
hoverinfo: 'all',
line: {
color: 'blue',
width: 2
},
marker: {
color: 'blue',
size: 8,
symbol: 'circle'
}
}
var Viol = {
type: 'scatter',
x: [6,9],
y: [-7,8],
mode: 'markers',
name: 'Violation',
showlegend: true,
marker: {
color: 'rgb(255,65,54)',
line: {width: 3},
opacity: 0.5,
size: 12,
symbol: 'circle-open'
}
}
var CL = {
type: 'scatter',
x: [0.5, 10, null, 0.5, 10],
y: [-5, -5, null, 5, 5],
mode: 'lines',
name: 'LCL/UCL',
showlegend: true,
line: {
color: 'red',
width: 2,
dash: 'dash'
}
}
var Centre = {
type: 'scatter',
x: [0.5, 10],
y: [0, 0],
mode: 'lines',
name: 'Centre',
showlegend: true,
line: {
color: 'grey',
width: 2
}
}
var data = [Data,Viol,CL,Centre]
var layout = {
title: {
text: 'Basic SPC Chart'
},
xaxis: {
zeroline: false
},
yaxis: {
range: [-10,10],
zeroline: false
}
}
Plotly.newPlot('myDiv', data,layout);
---
description: How to add D3.js-based continuous error bars to a line, scatter, or bar
chart.
display\_as: statistical
name: Continuous Error Bars
page\_type: example\_index
permalink: javascript/continuous-error-bars/
thumbnail: thumbnail/error-cont.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","continuous-error-bar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Asymmetric Error Bars with a Constant Offset
suite: continuous-error-bar
---
function random\_date(start, end, mul)
{
return new Date(start.getTime() + mul \* (end.getTime() - start.getTime()));
}
function date\_list(y1,m1,d1,y2,m2,d2,count)
{
var a =[];
for(i=0;iNotice the hover text!"
},
yaxis: {
title: {
text: "Wind speed (m/s)"
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Filled Lines
suite: continuous-error-bar
---
var trace1 = {
x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
y: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
fill: "tozerox",
fillcolor: "rgba(0,100,80,0.2)",
line: {color: "transparent"},
name: "Fair",
showlegend: false,
type: "scatter"
};
var trace2 = {
x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
y: [5.5, 3, 5.5, 8, 6, 3, 8, 5, 6, 5.5, 4.75, 5, 4, 7, 2, 4, 7, 4.4, 2, 4.5],
fill: "tozerox",
fillcolor: "rgba(0,176,246,0.2)",
line: {color: "transparent"},
name: "Premium",
showlegend: false,
type: "scatter"
};
var trace3 = {
x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
y: [11, 9, 7, 5, 3, 1, 3, 5, 3, 1, -1, 1, 3, 1, -0.5, 1, 3, 5, 7, 9],
fill: "tozerox",
fillcolor: "rgba(231,107,243,0.2)",
line: {color: "transparent"},
name: "Ideal",
showlegend: false,
type: "scatter"
};
var trace4 = {
x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
y: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
line: {color: "rgb(0,100,80)"},
mode: "lines",
name: "Fair",
type: "scatter"
};
var trace5 = {
x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
y: [5, 2.5, 5, 7.5, 5, 2.5, 7.5, 4.5, 5.5, 5],
line: {color: "rgb(0,176,246)"},
mode: "lines",
name: "Premium",
type: "scatter"
};
var trace6 = {
x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
y: [10, 8, 6, 4, 2, 0, 2, 4, 2, 0],
line: {color: "rgb(231,107,243)"},
mode: "lines",
name: "Ideal",
type: "scatter"
};
var data = [trace1, trace2, trace3, trace4, trace5, trace6];
var layout = {
paper\_bgcolor: "rgb(255,255,255)",
plot\_bgcolor: "rgb(229,229,229)",
xaxis: {
gridcolor: "rgb(255,255,255)",
range: [1, 10],
showgrid: true,
showline: false,
showticklabels: true,
tickcolor: "rgb(127,127,127)",
ticks: "outside",
zeroline: false
},
yaxis: {
gridcolor: "rgb(255,255,255)",
showgrid: true,
showline: false,
showticklabels: true,
tickcolor: "rgb(127,127,127)",
ticks: "outside",
zeroline: false
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Horizontal Error Bars
suite: error-bar
---
var data = [
{
x: [1, 2, 3, 4],
y: [2, 1, 3, 4],
error\_x: {
type: 'percent',
value: 10
},
type: 'scatter'
}
];
Plotly.newPlot('myDiv', data);
---
name: Basic Symmetric Error Bars
suite: error-bar
---
var data = [
{
x: [0, 1, 2],
y: [6, 10, 2],
error\_y: {
type: 'data',
array: [1, 2, 3],
visible: true
},
type: 'scatter'
}
];
Plotly.newPlot('myDiv', data);
---
name: Bar Chart with Error Bars
suite: error-bar
---
var trace1 = {
x: ['Trial 1', 'Trial 2', 'Trial 3'],
y: [3, 6, 4],
name: 'Control',
error\_y: {
type: 'data',
array: [1, 0.5, 1.5],
visible: true
},
type: 'bar'
};
var trace2 = {
x: ['Trial 1', 'Trial 2', 'Trial 3'],
y: [4, 7, 3],
name: 'Experimental',
error\_y: {
type: 'data',
array: [0.5, 1, 2],
visible: true
},
type: 'bar'
};
var data = [trace1, trace2];
var layout = {barmode: 'group'};
Plotly.newPlot('myDiv', data, layout);
---
name: Asymmetric Error Bars
suite: error-bar
---
var data = [
{
x: [1, 2, 3, 4],
y: [2, 1, 3, 4],
error\_y: {
type: 'data',
symmetric: false,
array: [0.1, 0.2, 0.1, 0.1],
arrayminus: [0.2, 0.4, 1, 0.2]
},
type: 'scatter'
}
];
Plotly.newPlot('myDiv', data);
---
description: How to add error bars to a D3.js-based line, scatter, or bar chart. Seven
examples of symmetric, asymmetric, horizontal, and colored error bars.
display\_as: statistical
name: Error Bars
page\_type: example\_index
permalink: javascript/error-bars/
redirect\_from: javascript-graphing-library/error-bars/
thumbnail: thumbnail/error-bar.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","error-bar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Colored and Styled Error Bars
suite: error-bar
---
function linspace(a,b,n) {
return d3.range(n).map(function(i){return a+i\*(b-a)/(n-1);});
}
x\_theo = linspace(-4, 4, 100)
sincx = Math.sin(x\_theo) / x\_theo
var x = [-3.8, -3.03, -1.91, -1.46, -0.89, -0.24, -0.0, 0.41, 0.89, 1.01, 1.91, 2.28, 2.79, 3.56]
var y = [-0.02, 0.04, -0.01, -0.27, 0.36, 0.75, 1.03, 0.65, 0.28, 0.02, -0.11, 0.16, 0.04, -0.15]
var trace1 = {
x: x\_theo,
y: sincx,
name: 'sinc(x)',
type: 'scatter'
};
var trace2 = {
x: x,
y: y,
mode: 'markers',
name: 'measured',
error\_y: {
type: 'constant',
value: 0.1,
color: '#85144B',
thickness: 1.5,
width: 3,
},
error\_x: {
type: 'constant',
value: 0.2,
color: '#85144B',
thickness: 1.5,
width: 3,
},
marker: {
color: '#85144B',
size: 8
},
type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data, {}, {showSendToCloud: true});
---
name: Error Bars as a Percentage of the y-Value
suite: error-bar
---
var data = [
{
x: [0, 1, 2],
y: [6, 10, 2],
error\_y: {
type: 'percent',
value: 50,
visible: true
},
type: 'scatter'
}
];
Plotly.newPlot('myDiv', data);
---
name: Asymmetric Error Bars with a Constant Offset
suite: error-bar
---
var data = [
{
x: [1, 2, 3, 4],
y: [2, 1, 3, 4],
error\_y: {
type: 'percent',
symmetric: false,
value: 15,
valueminus: 25
},
type: 'scatter'
}
];
Plotly.newPlot('myDiv', data);
---
name: Splom of Iris Dataset
suite: splom
markdown\_content: |
The Iris dataset contains four data variables, sepal length, sepal width, petal length petal width, for 150 iris flowers. The flowers are labeled as Iris-setosa, Iris-versicolor, Iris-virginica.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key.replace('.',' ')]; });
}
colors = []
for (i=0; i < unpack(rows, 'class').length; i++) {
if (unpack(rows, 'class')[i] == "Iris-setosa") {
colors.push(0)
} else if (unpack(rows, 'class')[i] == "Iris-versicolor") {
colors.push(0.5)
} else if (unpack(rows, 'class')[i] == "Iris-virginica") {
colors.push(1)
}
}
var pl\_colorscale=[
[0.0, '#19d3f3'],
[0.333, '#19d3f3'],
[0.333, '#e763fa'],
[0.666, '#e763fa'],
[0.666, '#636efa'],
[1, '#636efa']
]
var axis = () => ({
showline:false,
zeroline:false,
gridcolor:'#ffff',
ticklen:4
})
var data = [{
type: 'splom',
dimensions: [
{label:'sepal length', values:unpack(rows,'sepal length')},
{label:'sepal width', values:unpack(rows,'sepal width')},
{label:'petal length', values:unpack(rows,'petal length')},
{label:'petal width', values:unpack(rows,'petal width')}
],
text: unpack(rows, 'class'),
marker: {
color: colors,
colorscale:pl\_colorscale,
size: 7,
line: {
color: 'white',
width: 0.5
}
}
}]
var layout = {
title: {
text: 'Iris Data set'
},
height: 800,
width: 800,
autosize: false,
hovermode:'closest',
dragmode:'select',
plot\_bgcolor:'rgba(240,240,240, 0.95)',
xaxis:axis(),
yaxis:axis(),
xaxis2:axis(),
xaxis3:axis(),
xaxis4:axis(),
yaxis2:axis(),
yaxis3:axis(),
yaxis4:axis()
}
Plotly.react('myDiv', data, layout)
});
---
description: How to make D3.js-based splom in Plotly.js.
display\_as: statistical
name: Splom
order: 10
permalink: javascript/splom/
thumbnail: thumbnail/splom\_image.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","splom" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Splom of Diabetes Dataset
suite: splom
markdown\_content: |
Diabetes dataset is downloaded from [kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database/data). It is used to predict the onset of diabetes based on 8 diagnostic measures. The diabetes file contains the diagnostic measures for 768 patients, that are labeled as non-diabetic (Outcome=0), respectively diabetic (Outcome=1). The splom associated to the 8 variables can illustrate the strength of the relationship between pairs of measures for diabetic/nondiabetic patients.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
text = []
for (i=0; i < unpack(rows, 'Outcome').length; i++) {
if (unpack(rows, 'Outcome')[i] == "0") {
text.push("Diabetic")
} else {
text.push("Non-Diabetic")
}
}
var pl\_colorscale=[
[0.0, '#119dff'],
[0.5, '#119dff'],
[0.5, '#ef553b'],
[1, '#ef553b']
]
var axis = () => ({
showline:false,
zeroline:false,
gridcolor:'#ffff',
ticklen:2,
tickfont:{size:10},
title:{font:{size:12}}
})
var data = [{
type: 'splom',
dimensions: [
{label:'Pregnancies', values:unpack(rows, 'Pregnancies')},
{label:'Glucose', values:unpack(rows, 'Glucose')},
{label:'BloodPressure', values:unpack(rows, 'BloodPressure')},
{label:'SkinThickness', values:unpack(rows, 'SkinThickness')},
{label:'Insulin', values:unpack(rows, 'Insulin')},
{label:'BMI', values:unpack(rows, 'BMI')},
{label:'DiabPedigreeFun', values:unpack(rows, 'DiabetesPedigreeFunction')},
{label:'Age', values:unpack(rows, 'Age')}
],
text:text,
marker: {
color: unpack(rows, 'Outcome'),
colorscale:pl\_colorscale,
size: 5,
line: {
color: 'white',
width: 0.5
}
}
}]
var layout = {
title: {
text: "Scatterplot Matrix (SPLOM) for Diabetes Dataset
Data source: [[1]](https://www.kaggle.com/uciml/pima-indians-diabetes-database/data)"
},
height: 1000,
width: 1000,
autosize: false,
hovermode:'closest',
dragmode:'select',
plot\_bgcolor:'rgba(240,240,240, 0.95)',
xaxis:axis(),
yaxis:axis(),
xaxis2:axis(),
xaxis3:axis(),
xaxis4:axis(),
xaxis5:axis(),
xaxis6:axis(),
xaxis7:axis(),
xaxis8:axis(),
yaxis2:axis(),
yaxis3:axis(),
yaxis4:axis(),
yaxis5:axis(),
yaxis6:axis(),
yaxis7:axis(),
yaxis8:axis()
}
Plotly.react('myDiv', data, layout);
});
---
description: How to make a D3.js-based 2d density plot in JavaScript. Examples of
density plots with kernel density estimations, custom color-scales, and smoothing.
display\_as: statistical
name: 2d Density Plots
page\_type: example\_index
permalink: javascript/2d-density-plots/
redirect\_from: javascript-graphing-library/2d-density-plots/
thumbnail: thumbnail/2d-density-plot.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite", "2d-density-plot" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 2D Histogram Contour Plot
with Histogram Subplots
suite: 2d-density-plot
---
// from http://bl.ocks.org/mbostock/4349187
// Sample from a normal distribution with mean 0, stddev 1.
function normal() {
var x = 0,
y = 0,
rds, c;
do {
x = Math.random() \* 2 - 1;
y = Math.random() \* 2 - 1;
rds = x \* x + y \* y;
} while (rds == 0 || rds > 1);
c = Math.sqrt(-2 \* Math.log(rds) / rds); // Box-Muller transform
return x \* c; // throw away extra sample y \* c
}
var N = 2000,
a = -1,
b = 1.2;
var step = (b - a) / (N - 1);
var t = new Array(N), x = new Array(N), y = new Array(N);
for(var i = 0; i < N; i++){
t[i] = a + step \* i;
x[i] = (Math.pow(t[i], 3)) + (0.3 \* normal() );
y[i] = (Math.pow(t[i], 6)) + (0.3 \* normal() );
}
var trace1 = {
x: x,
y: y,
mode: 'markers',
name: 'points',
marker: {
color: 'rgb(102,0,0)',
size: 2,
opacity: 0.4
},
type: 'scatter'
};
var trace2 = {
x: x,
y: y,
name: 'density',
ncontours: 20,
colorscale: 'Hot',
reversescale: true,
showscale: false,
type: 'histogram2dcontour'
};
var trace3 = {
x: x,
name: 'x density',
marker: {color: 'rgb(102,0,0)'},
yaxis: 'y2',
type: 'histogram'
};
var trace4 = {
y: y,
name: 'y density',
marker: {color: 'rgb(102,0,0)'},
xaxis: 'x2',
type: 'histogram'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
showlegend: false,
autosize: false,
width: 600,
height: 550,
margin: {t: 50},
hovermode: 'closest',
bargap: 0,
xaxis: {
domain: [0, 0.85],
showgrid: false,
zeroline: false
},
yaxis: {
domain: [0, 0.85],
showgrid: false,
zeroline: false
},
xaxis2: {
domain: [0.85, 1],
showgrid: false,
zeroline: false
},
yaxis2: {
domain: [0.85, 1],
showgrid: false,
zeroline: false
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: 2D Histogram Contour Plot with Slider Control
suite: 2d-density-plot
order: 17
height: 800
---
Add slider controls to 2d-density-plot plots with the [postMessage API](https://github.com/plotly/postMessage-API).
See the [code on JSFiddle](https://jsfiddle.net/plotlygraphs/y9sdy76h/4/).
Watch [the 5 second video](https://raw.githubusercontent.com/plotly/documentation/gh-pages/all_static/images/flight_conflicts.gif) of how it works.
---
permalink: javascript/statistical-charts/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make statistical charts such as boxplots and histograms.
name: Statistical Charts
layout: langindex
display\_as: statistical
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Statistical Charts

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","statistical" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
name: Basic 2D Histogram Contour
suite: hist2dcontour
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
var data = [
{
x: x,
y: y,
type: 'histogram2dcontour'
}
];
Plotly.newPlot('myDiv', data);
---
name: 2D Histogram Contour Colorscale
suite: hist2dcontour
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
var data = [
{
x: x,
y: y,
colorscale: 'Blues',
type: 'histogram2dcontour'
}
];
Plotly.newPlot('myDiv', data);
---
description: How to make D3.js-based 2D Histogram Contour plots in Plotly.js.
display\_as: statistical
name: 2D Histogram Contour
order: 11
permalink: javascript/2d-histogram-contour/
thumbnail: thumbnail/hist2dcontour.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","hist2dcontour" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Styled 2D Histogram Contour
suite: hist2dcontour
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
var data = [
{
x: x,
y: y,
colorscale: 'Blues',
type: 'histogram2dcontour',
contours: {
showlabels: true,
labelfont: {
family: 'Raleway',
color: 'white'
}
},
hoverlabel: {
bgcolor: 'white',
bordercolor: 'black',
font: {
family: 'Raleway',
color: 'black'
}
}
}
];
Plotly.newPlot('myDiv', data);
---
name: 2D Histogram of a Bivariate Normal Distribution
suite: histogram2d
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
var data = [
{
x: x,
y: y,
type: 'histogram2d'
}
];
Plotly.newPlot('myDiv', data);
---
name: 2D Histogram Overlaid with a Scatter Chart
suite: histogram2d
---
var x0 = [];
var y0 = [];
var x1 = [];
var y1 = [];
var x2 = [];
var y2 = [];
for (var i = 0; i < 500; i ++)
{
x0[i] = Math.random() + 1;
y0[i] = Math.random() + 1.5;
}
for (var i = 0; i < 100; i ++)
{
x1[i] = Math.random();
y1[i] = Math.random() + 1;
}
for (var i = 0; i < 500; i ++)
{
x2[i] = Math.random()\*2;
y2[i] = Math.random()\*3;
}
var trace1 = {
x: x0,
y: y0,
mode: 'markers',
marker: {
symbol: 'circle',
opacity: 0.7,
color:'rgb(200,111,200)',
},
type: 'scatter',
};
var trace2 = {
x: x1,
y: y1,
mode: 'markers',
marker: {
symbol: 'square',
opacity: 0.7,
color:'cyan',
},
type: 'scatter'
};
var trace3 = {
x: x2,
y: y2,
type: 'histogram2d',
colorscale : [['0' , 'rgb(0,225,100)'],['1', 'rgb(100,0,200)']],
};
var data = [trace1, trace2, trace3];
Plotly.newPlot('myDiv', data);
---
name: 2D Histogram Binning and Styling Options
suite: histogram2d
---
var x = [];
var y = [];
for (var i = 0; i < 500; i ++) {
x[i] = Math.random();
y[i] = Math.random() + 1;
}
var data = [
{
x: x,
y: y,
histnorm: 'probability',
autobinx: false,
xbins: {
start: -3,
end: 3,
size: 0.1
},
autobiny: false,
ybins: {
start: -2.5,
end: 4,
size: 0.1
},
colorscale: [['0', 'rgb(12,51,131)'], ['0.25', 'rgb(10,136,186)'], ['0.5', 'rgb(242,211,56)'], ['0.75', 'rgb(242,143,56)'], ['1', 'rgb(217,30,30)']],
type: 'histogram2d'
}
];
Plotly.newPlot('myDiv', data);
---
description: How to make a D3.js-based 2D histogram in javascript. A 2D histogram
is a visualization of a bivariate distribution.
display\_as: statistical
name: 2D Histograms
permalink: javascript/2D-Histogram/
redirect\_from: javascript-graphing-library/2D-Histogram/
thumbnail: thumbnail/histogram2d.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","histogram2d" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Grouped Violin Plot
suite: violin
---
// need to fix data
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/violin\_data.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'violin',
x: unpack(rows, 'day'),
y: unpack(rows, 'total\_bill'),
legendgroup: 'M',
scalegroup: 'M',
name: 'M',
box: {
visible: true
},
line: {
color: 'blue',
},
meanline: {
visible: true
}
}, {
type: 'violin',
x: unpack(rows, 'day'),
y: unpack(rows, 'total\_bill'),
legendgroup: 'F',
scalegroup: 'F',
name: 'F',
box: {
visible: true
},
line: {
color: 'pink',
},
meanline: {
visible: true
}
}]
var layout = {
title: {
text: "Grouped Violin Plot"
},
yaxis: {
zeroline: false
},
violinmode: 'group'
}
Plotly.newPlot('myDiv', data, layout);
});
---
name: Advanced Violin Plot
suite: violin
width: 700
---
var trace1 = {
text: "sample length: 32",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "F",
scalegroup: "F",
points: "all",
pointpos: 1,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#bebada"
},
symbol: "line-ns"
},
showlegend: false,
side: "positive",
type: "violin",
name: "F",
span: [
0
],
line: {
color: "#bebada"
},
y0: "Thursday",
x: [
10.07,
34.83,
10.65,
12.43,
24.08,
13.42,
12.48,
29.8,
14.52,
11.38,
20.27,
11.17,
12.26,
18.26,
8.51,
10.33,
14.15,
13.16,
17.47,
27.05,
16.43,
8.35,
18.64,
11.87,
19.81,
43.11,
13.0,
12.74,
13.0,
16.4,
16.47,
18.78
],
orientation: "h"
}
var trace2 = {
text: "sample length: 30",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "M",
scalegroup: "M",
points: "all",
pointpos: -0.6,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#8dd3c7"
},
symbol: "line-ns"
},
showlegend: false,
side: "negative",
type: "violin",
name: "M",
span: [
0
],
line: {
color: "#8dd3c7"
},
y0: "Thursday",
x: [
27.2,
22.76,
17.29,
19.44,
16.66,
32.68,
15.98,
13.03,
18.28,
24.71,
21.16,
11.69,
14.26,
15.95,
8.52,
22.82,
19.08,
16.0,
34.3,
41.19,
9.78,
7.51,
28.44,
15.48,
16.58,
7.56,
10.34,
13.51,
18.71,
20.53
],
orientation: "h"
}
var trace3 = {
text: "sample length: 9",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "F",
scalegroup: "F",
points: "all",
pointpos: 0.4,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#bebada"
},
symbol: "line-ns"
},
showlegend: false,
side: "positive",
type: "violin",
name: "F",
span: [
0
],
line: {
color: "#bebada"
},
y0: "Friday",
x: [
5.75,
16.32,
22.75,
11.35,
15.38,
13.42,
15.98,
16.27,
10.09
],
orientation: "h"
}
var trace4= {
text: "sample length: 10",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "M",
scalegroup: "M",
points: "all",
pointpos: -0.3,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#8dd3c7"
},
symbol: "line-ns"
},
showlegend: false,
side: "negative",
type: "violin",
name: "M",
span: [
0
],
line: {
color: "#8dd3c7"
},
y0: "Friday",
x: [
28.97,
22.49,
40.17,
27.28,
12.03,
21.01,
12.46,
12.16,
8.58,
13.42
],
orientation: "h"
}
var trace5 = {
text: "sample length: 28",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "F",
scalegroup: "F",
points: "all",
pointpos: 0.55,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#bebada"
},
symbol: "line-ns"
},
showlegend: true,
side: "positive",
type: "violin",
name: "F",
span: [
0
],
line: {
color: "#bebada"
},
y0: "Saturday",
x: [
20.29,
15.77,
19.65,
15.06,
20.69,
16.93,
26.41,
16.45,
3.07,
17.07,
26.86,
25.28,
14.73,
44.3,
22.42,
20.92,
14.31,
7.25,
10.59,
10.63,
12.76,
13.27,
28.17,
12.9,
30.14,
22.12,
35.83,
27.18
],
orientation: "h"
}
var trace4 = {
text: "sample length: 59",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "M",
scalegroup: "M",
points: "all",
pointpos: -1.1,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#8dd3c7"
},
symbol: "line-ns"
},
showlegend: true,
side: "negative",
type: "violin",
name: "M",
span: [
0
],
line: {
color: "#8dd3c7"
},
y0: "Saturday",
x: [
20.65,
17.92,
39.42,
19.82,
17.81,
13.37,
12.69,
21.7,
9.55,
18.35,
17.78,
24.06,
16.31,
18.69,
31.27,
16.04,
38.01,
11.24,
48.27,
20.29,
13.81,
11.02,
18.29,
17.59,
20.08,
20.23,
15.01,
12.02,
10.51,
17.92,
15.36,
20.49,
25.21,
18.24,
14.0,
50.81,
15.81,
26.59,
38.73,
24.27,
30.06,
25.89,
48.33,
28.15,
11.59,
7.74,
20.45,
13.28,
24.01,
15.69,
11.61,
10.77,
15.53,
10.07,
12.6,
32.83,
29.03,
22.67,
17.82
],
orientation: "h"
}
var trace6 = {
text: "sample length: 18",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "F",
scalegroup: "F",
points: "all",
pointpos: 0.45,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#bebada"
},
symbol: "line-ns"
},
showlegend: false,
side: "positive",
type: "violin",
name: "F",
span: [
0
],
line: {
color: "#bebada"
},
y0: "Sunday",
x: [
16.99,
24.59,
35.26,
14.83,
10.33,
16.97,
10.29,
34.81,
25.71,
17.31,
29.85,
25.0,
13.39,
16.21,
17.51,
9.6,
20.9,
18.15
],
orientation: "h"
}
var trace7 = {
text: "sample length: 58",
hoveron: "points+kde",
meanline: {
visible: true
},
legendgroup: "M",
scalegroup: "M",
points: "all",
pointpos: -0.9,
box: {
visible: true
},
jitter: 0,
scalemode: "count",
marker: {
line: {
width: 2,
color: "#8dd3c7"
},
symbol: "line-ns"
},
showlegend: false,
side: "negative",
type: "violin",
name: "M",
span: [
0
],
line: {
color: "#8dd3c7"
},
y0: "Sunday",
x: [
10.34,
21.01,
23.68,
25.29,
8.77,
26.88,
15.04,
14.78,
10.27,
15.42,
18.43,
21.58,
16.29,
17.46,
13.94,
9.68,
30.4,
18.29,
22.23,
32.4,
28.55,
18.04,
12.54,
9.94,
25.56,
19.49,
38.07,
23.95,
29.93,
14.07,
13.13,
17.26,
24.55,
19.77,
48.17,
16.49,
21.5,
12.66,
13.81,
24.52,
20.76,
31.71,
7.25,
31.85,
16.82,
32.9,
17.89,
14.48,
34.63,
34.65,
23.33,
45.35,
23.17,
40.55,
20.69,
30.46,
23.1,
15.69
],
orientation: "h"
}
var data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7]
var layout = {
hovermode: "closest",
width: 400,
yaxis: {
showgrid: true
},
title: {
text: "Total bill distribution
*scaled by number of bills per gender"
},
legend: {
tracegroupgap: 0
},
violingap: 0,
violingroupgap: 0,
violinmode: "overlay",
height: 700
}
Plotly.newPlot("myDiv", data, layout)*
---
name: Basic Violin Plot
suite: violin
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/violin\_data.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'violin',
y: unpack(rows, 'total\_bill'),
points: 'none',
box: {
visible: true
},
boxpoints: false,
line: {
color: 'black'
},
fillcolor: '#8dd3c7',
opacity: 0.6,
meanline: {
visible: true
},
x0: "Total Bill"
}]
var layout = {
title: {
text: ""
},
yaxis: {
zeroline: false
}
}
Plotly.newPlot('myDiv', data, layout);
});
---
name: Split Violin Plot
suite: violin
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/violin\_data.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'violin',
x: unpack(rows, 'day'),
y: unpack(rows, 'total\_bill'),
legendgroup: 'Yes',
scalegroup: 'Yes',
name: 'Yes',
side: 'negative',
box: {
visible: true
},
line: {
color: 'blue',
width: 2
},
meanline: {
visible: true
}
}, {
type: 'violin',
x: unpack(rows, 'day'),
y: unpack(rows, 'total\_bill'),
legendgroup: 'No',
scalegroup: 'No',
name: 'No',
side: 'positive',
box: {
visible: true
},
line: {
color: 'green',
width: 2
},
meanline: {
visible: true
}
}]
var layout = {
title: {
text: "Split Violin Plot"
},
yaxis: {
zeroline: false
},
violingap: 0,
violingroupgap: 0,
violinmode: "overlay",
}
Plotly.newPlot('myDiv', data, layout);
});
---
name: Horizontal Violin Plot
suite: violin
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/violin\_data.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'violin',
x: unpack(rows, 'total\_bill'),
points: 'none',
box: {
visible: true
},
boxpoints: false,
line: {
color: 'black'
},
fillcolor: '#8dd3c7',
opacity: 0.6,
meanline: {
visible: true
},
y0: "Total Bill"
}]
var layout = {
title: {
text: "Basic Horizontal Violin Plot"
},
xaxis: {
zeroline: false
}
}
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make D3.js-based violin plots in Plotly.js.
display\_as: statistical
name: Violin Plot
permalink: javascript/violin/
thumbnail: thumbnail/violin.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","violin" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Mutli-Color Parallel Categories Diagram
suite: parcats
markdown\_content: |
The color of the ribbons can be specified with the `line.color` property. Similar to other trace types, this
property may be set to an array of numbers, which are then mapped to colors according to the the colorscale
specified in the `line.colorscale` property.
Here is an example of visualizing the survival rate of passengers in the titanic dataset, where the ribbons are
colored based on survival outcome.
By setting the `hoveron` property to `'color'` and the `hoverinfo` property to `'count+probability'` the tooltips
now display count and probability information for each color (outcome) per category.
By setting the `arrangement` property to `'freeform'` it is now possible to drag categories horizontally to
reorder dimensions as well as vertically to reorder categories within the dimension.
---
var gd = document.getElementById('myDiv');
d3.csv(
"https://raw.githubusercontent.com/plotly/datasets/master/titanic.csv",
function(titanicData) {
var classDim = {
values: titanicData.map(function(row) {return row['Pclass']}),
categoryorder: 'category ascending',
label: "Class"
};
var genderDim = {
values: titanicData.map(function(row) {return row['Sex']}),
label: "Gender"
};
var survivalDim = {
values: titanicData.map(function(row) {return row['Survived']}),
label: "Outcome",
categoryarray: [0, 1],
ticktext: ['perished', 'survived'],
};
var color = survivalDim.values;
var colorscale = [[0, 'lightsteelblue'], [1, 'mediumseagreen']];
// Build Traces
var traces = [
{type: 'parcats',
dimensions: [classDim, genderDim, survivalDim],
line: {color: color,
colorscale: colorscale},
hoveron: 'color',
hoverinfo: 'count+probability',
labelfont: {size: 14},
arrangement: 'freeform'
}
];
var layout = {width: 600};
// Make plot
Plotly.newPlot('myDiv', traces, layout);
});
---
name: Basic Parallel Categories Diagram
suite: parcats
markdown\_content: |
The parallel categories diagram is a visualization of multi-dimensional categorical data sets. Each variable in
the data set is represented by a column of rectangles, where each rectangle corresponds to a discrete value
taken on by that variable. The relative heights of the rectangles reflect the relative frequency of occurrence of
the corresponding value.
Combinations of category rectangles across dimensions are connected by ribbons, where the height of the ribbon
corresponds to the relative frequency of occurrence of the combination of categories in the data set.
In this example, we visualize the hair color, eye color, and sex of a sample of 8 people. Hovering over a
category rectangle displays a tooltip with the number of people with that single trait. Hovering over a ribbon
in the diagram displays a tooltip with the number of people with a particular combination of the three
traits connected by the ribbon.
The dimension labels can be dragged horizontally to reorder the dimensions and the category rectangles can be
dragged vertically to reorder the categories within a dimension.
---
var trace1 = {
type: 'parcats',
dimensions: [
{label: 'Hair',
values: ['Black', 'Black', 'Black', 'Brown',
'Brown', 'Brown', 'Red', 'Brown']},
{label: 'Eye',
values: ['Brown', 'Brown', 'Brown', 'Brown',
'Brown', 'Blue', 'Blue', 'Blue']},
{label: 'Sex',
values: ['Female', 'Female', 'Female', 'Male',
'Female', 'Male', 'Male', 'Male']}]
};
var data = [ trace1 ];
var layout = {width: 600};
Plotly.newPlot('myDiv', data, layout);
---
name: Parallel Categories Linked Brushing
suite: parcats
markdown\_content: |
This example demonstrates how the `plotly\_selected` and `plotly\_click` events can be used to implement linked
brushing between 3 categorical dimensions displayed with a `parcats` trace and 2 continuous dimensions displayed
with a `scatter` trace.
This example also sets the `line.shape` property to `hspline` to cause the ribbons to curve between categories.
---
var gd = document.getElementById("myDiv");
var categoricalDimensionLabels = [
'body-style',
'drive-wheels',
'fuel-type'
];
d3.csv(
'https://raw.githubusercontent.com/plotly/datasets/master/imports-85.csv',
function(carsData) {
// Preprocess Data
var mpg = carsData.map(function(row) { return row['highway-mpg'] });
var horsepower = carsData.map(function(row) { return row['horsepower'] });
var categoricalDimensions = categoricalDimensionLabels.map(
function(dimLabel) {
// Extract column
var values = carsData.map(function(row) {
return row[dimLabel]
});
return {
values: values,
label: dimLabel
};
});
// Colors
var color = new Int8Array(carsData.length);
var colorscale = [[0, 'gray'], [1, 'firebrick']];
// Layout
var layout = {
width: 600,
height: 800,
xaxis: {title: {text: 'Horsepower'}},
yaxis: {domain: [0.6, 1], title: {text: 'MPG'}},
dragmode: 'lasso',
hovermode: 'closest'
};
// Build Traces
var traces = [
{type: 'scatter',
x: horsepower,
y: mpg,
marker: {color: 'gray'},
mode: 'markers',
selected: {'marker': {'color': 'firebrick'}},
unselected: {'marker': {'opacity': 0.3}}
},
{type: 'parcats',
domain: {y: [0, 0.4]},
dimensions:categoricalDimensions,
line: {
colorscale: colorscale,
cmin: 0,
cmax: 1,
color: color,
shape: 'hspline'},
labelfont: {size: 14}
}
];
// Make plot
Plotly.newPlot('myDiv', traces, layout);
// Update color on selection and click
var update\_color = function(points\_data) {
var new\_color = new Int8Array(carsData.length);
var selection = []
for(var i = 0; i < points\_data.points.length; i++) {
new\_color[points\_data.points[i].pointNumber] = 1;
selection.push(points\_data.points[i].pointNumber);
}
// Update selected points in scatter plot
Plotly.restyle('myDiv', {'selectedpoints': [selection]}, 0)
// Update color of selected paths in parallel categories diagram
Plotly.restyle('myDiv', {'line.color': [new\_color]}, 1)
};
gd.on('plotly\_selected', update\_color);
gd.on('plotly\_click', update\_color);
});
---
description: How to make parallel categories diagrams in JavaScript
display\_as: statistical
name: Parallel Categories Diagram
permalink: javascript/parallel-categories-diagram/
thumbnail: thumbnail/parcats.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","parcats" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Parallel Categories with Multi-Color Linked Brushing
suite: parcats
markdown\_content: |
This example extends the previous example to support brushing with multiple colors. The radio buttons above may
be used to select the active color, and this color will be applied when points are selected in the `scatter`
trace and when categories or ribbons are clicked in the `parcats` trace.
---
var gd = document.getElementById('myDiv');
var categoricalDimensionLabels = [
'body-style',
'drive-wheels',
'fuel-type'
];
d3.csv(
'https://raw.githubusercontent.com/plotly/datasets/master/imports-85.csv',
function(carsData) {
// Preprocess Data
var mpg = carsData.map(function(row) { return row['highway-mpg'] });
var horsepower = carsData.map(function(row) { return row['horsepower'] });
var categoricalDimensions = categoricalDimensionLabels.map(
function(dimLabel) {
// Extract column
var values = carsData.map(function(row) {
return row[dimLabel]
});
return {
values: values,
label: dimLabel
};
}
);
// Colors
var color = new Int8Array(carsData.length);
var colorscale = [[0, 'gray'], [0.33, 'gray'],
[0.33, 'firebrick'], [0.66, 'firebrick'],
[0.66, 'blue'], [1.0, 'blue']];
// Layout
var layout = {
width: 600,
height: 800,
xaxis: {title: {text: 'Horsepower'}},
yaxis: {domain: [0.6, 1], title: {text: 'MPG'}},
dragmode: 'lasso',
hovermode: 'closest'
};
// Build Traces
var traces = [
{type: 'scatter',
x: horsepower,
y: mpg,
marker: {color: color,
colorscale: colorscale,
cmin: -0.5,
cmax: 2.5,
showscale: true,
colorbar: {tickvals: [0, 1, 2],
ticktext: ['None', 'Red', 'Blue']}},
mode: 'markers',
},
{type: 'parcats',
domain: {y: [0, 0.4]},
dimensions:categoricalDimensions,
line: {
colorscale: colorscale,
cmin: -0.5,
cmax: 2.5,
color: color,
shape: 'hspline'},
labelfont: {size: 14}
}
];
// Make plot
Plotly.newPlot('myDiv', traces, layout);
// Update color on selection and click
var update\_color = function(points\_data) {
var new\_color = color;
var color\_value = document.querySelector('input[name="rate"]:checked').value;
console.log(color\_value);
var selection = []
for(var i = 0; i < points\_data.points.length; i++) {
new\_color[points\_data.points[i].pointNumber] = color\_value;
selection.push(points\_data.points[i].pointNumber);
}
// Update selected points in scatter plot
Plotly.restyle'myDiv', {'marker.color': [new\_color]}, 0)
// Update color of selected paths in parallel categories diagram
Plotly.restyle'myDiv',
{'line.color': [new\_color]}, 1)
};
gd.on('plotly\_selected', update\_color);
gd.on('plotly\_click', update\_color);
});
---
name: Basic Parallel Categories Diagram with Counts
suite: parcats
markdown\_content: |
If the frequency of occurrence for each combination of attributes is known in advance, this can be specified using
the `counts` property
---
var trace1 = {
type: 'parcats',
dimensions: [
{label: 'Hair',
values: ['Black', 'Brown', 'Brown', 'Brown', 'Red']},
{label: 'Eye',
values: ['Brown', 'Brown', 'Brown', 'Blue', 'Blue']},
{label: 'Sex',
values: ['Female', 'Male', 'Female', 'Male', 'Male']}],
counts: [6, 10, 40, 23, 7]
};
var data = [ trace1 ];
var layout = {width: 600};
Plotly.newPlot('myDiv', data, layout);
---
name: Plotly JavaScript Graphing Library
permalink: /javascript/
description: A free open source interactive javascript graphing library. Plotly.js is built on d3.js and webgl and supports over 20 types of interactive charts.
layout: langindex
display\_as: false
redirect\_from: /javascript-graphing-library/
---

# Plotly JavaScript Open Source Graphing Library

Built on top of [d3.js](https://d3js.org/) and [stack.gl](https://github.com/stackgl), Plotly.js is a high-level, declarative charting library. plotly.js ships with over 40 chart types, including 3D charts, statistical graphs, and SVG maps.

plotly.js is [free and open source](/javascript/is-plotly-free) and you can [view the source, report issues or contribute on GitHub](https://github.com/plotly/plotly.js).

{% include layouts/dashplug.html %}

Read more about plotly.js features

Sophisticated chart types

`plotly.js` abstracts the types of statistical and scientific charts that you would find in packages like matplotlib, ggplot2, or MATLAB.

[![]({{site.imgurl}}images/turbulence-simulation.jpg)](https://plotly.com/~mdtusz/72.embed)

```
d3.json('https://plotly.com/~DanielCarrera/13.json', function(figure){
                  var trace = {
                    x: figure.data[0].x, y: figure.data[0].y, z: figure.data[0].z,
                    type: 'contour', autocolorscale: false,
                    colorscale: [[0,"rgb(  0,  0,  0)"],[0.3,"rgb(230,  0,  0)"],[0.6,"rgb(255,210,  0)"],[1,"rgb(255,255,255)"]],
                    reversescale: true, zmax: 2.5, zmin: -2.5
                  };
                  var layout = {
                    title: {
                      text: 'turbulence simulation'
                  },
                    xaxis: {
                      title: {
                          text: 'radial direction'
                      },
                      showline: true,
                      mirror: 'allticks',
                      ticks: 'inside'
                    },
                    yaxis: {
                        title: {
                            text: 'vertical direction'
                        },
                        showline: true,
                        mirror: 'allticks',
                        ticks: 'inside'
                    },
                    margin: {l: 40, b: 40, t: 60},
                    annotations: [{
                      showarrow: false,
                      text: 'Credit: Daniel Carrera',
                      x: 0, y: 0, xref: 'paper', yref: 'paper'
                    }]
                  }
                  Plotly.newPlot(document.getElementById('contour-plot'), [trace], layout, {showLink: false});
                });
```

Fully customizable

`plotly.js` charts are described declaratively as JSON objects. Every aspect of the charts, such as colors, grid lines, and the legend, has a corresponding set of JSON attributes.

[view all of the available attributes](https://plotly.com/javascript/reference)

```
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv', function(rows){
                    var trace = {
                      type: 'scatter',                    // set the chart type
                      mode: 'lines',                      // connect points with lines
                      x: rows.map(function(row){          // set the x-data
                        return row['Time'];
                      }),
                      y: rows.map(function(row){          // set the x-data
                        return row['10 Min Sampled Avg'];
                      }),
                      line: {                             // set the width of the line.
                        width: 1
                      },
                      error_y: {
                        array: rows.map(function(row){    // set the height of the error bars
                          return row['10 Min Std Dev'];
                        }),
                        thickness: 0.5,                   // set the thickness of the error bars
                        width: 0
                      }
                    };

                    var layout = {
                      yaxis: {
                        title: {
                          text: "Wind Speed"
                        }
                      },       // set the y axis title
                      xaxis: {
                        showgrid: false,                  // remove the x-axis grid lines
                        tickformat: "%B, %Y"              // customize the date format to "month, day"
                      },
                      margin: {                           // update the left, bottom, right, top margin
                        l: 40, b: 10, r: 10, t: 20
                      }
                    };

                    Plotly.newPlot(document.getElementById('wind-speed'), [trace], layout, {showLink: false});
                });
```

High performance

Most plotly graphs are drawn with SVG. This offers great compatibility across browsers and publication-quality vector image export. Unfortunately, there are inherent performance limitations with the number of SVG elements that you can draw in the DOM.

`plotly.js` uses [stack.gl](http://stack.gl) for high performance 2D and 3D charting.

[![]({{site.imgurl}}images/hue-value-vs.jpg)](https://plotly.com/~chris/17389.embed)

This chart was drawn with the `plotly.js` chart type `scattergl`. `scattergl` charts render an order of magnitude faster than their SVG counterparts.

[![]({{site.imgurl}}images/surface-plot.jpg)](https://plotly.com/~chriddyp/1780.embed)

All 3D charts in `plotly.js` are rendered with WebGL, leveraging the power of the GPU for fast interactivity.
[view the interactive version](https://plotly.com/~chris/17389.embed)

Universal

By abstracting charts to a declarative JSON structure, `plotly.js` is used as a browser-based charting library for [Python](https://plotly.com/python/), [R](https://plotly.com/r/), [MATLAB](https://plotly.com/matlab/).

{% assign languagelist = site.posts | where:"language","plotly\_js" | sort: "order" %}
{% include posts/mainlang\_documentation\_eg.html %}
---
name: Extend Traces & Relayout
suite: streaming
---
function rand() {
return Math.random();
}
var time = new Date();
var data = [{
x: [time],
y: [rand],
mode: 'lines',
line: {color: '#80CAF6'}
}]
Plotly.newPlot('myDiv', data);
var cnt = 0;
var interval = setInterval(function() {
var time = new Date();
var update = {
x: [[time]],
y: [[rand()]]
}
var olderTime = time.setMinutes(time.getMinutes() - 1);
var futureTime = time.setMinutes(time.getMinutes() + 1);
var minuteView = {
xaxis: {
type: 'date',
range: [olderTime,futureTime]
}
};
Plotly.relayout('myDiv', minuteView);
Plotly.extendTraces('myDiv', update, [0])
if(++cnt === 100) clearInterval(interval);
}, 1000);
---
name: Basic Streaming
suite: streaming
---
function rand() {
return Math.random();
}
Plotly.newPlot('myDiv', [{
y: [1,2,3].map(rand),
mode: 'lines',
line: {color: '#80CAF6'}
}]);
var cnt = 0;
var interval = setInterval(function() {
Plotly.extendTraces('myDiv', {
y: [[rand()]]
}, [0])
if(++cnt === 100) clearInterval(interval);
}, 300);
---
name: Multiple Traces
suite: streaming
---
function rand() {
return Math.random();
}
Plotly.newPlot('myDiv', [{
y: [1,2,3].map(rand),
mode: 'lines',
line: {color: '#80CAF6'}
}, {
y: [1,2,3].map(rand),
mode: 'lines',
line: {color: '#DF56F1'}
}]);
var cnt = 0;
var interval = setInterval(function() {
Plotly.extendTraces('myDiv', {
y: [[rand()], [rand()]]
}, [0, 1])
if(++cnt === 100) clearInterval(interval);
}, 300);
---
name: Streaming with Timestamp
suite: streaming
---
function rand() {
return Math.random();
}
var time = new Date();
var data = [{
x: [time],
y: [rand()],
mode: 'lines',
line: {color: '#80CAF6'}
}]
Plotly.newPlot('myDiv', data);
var cnt = 0;
var interval = setInterval(function() {
var time = new Date();
var update = {
x: [[time]],
y: [[rand()]]
}
Plotly.extendTraces('myDiv', update, [0])
if(++cnt === 100) clearInterval(interval);
}, 1000);
---
name: Streaming
permalink: javascript/streaming/
description: How to create D3.js-based streaming plots in Plotly.js.
thumbnail: thumbnail/streaming-thumb-square.gif
page\_type: example\_index
display\_as: streaming
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","streaming" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 30 Points Using Update
suite: streaming
---
var arrayLength = 30
var newArray = []
for(var i = 0; i < arrayLength; i++) {
var y = Math.round(Math.random()\*10) + 1
newArray[i] = y
}
Plotly.newPlot('myDiv', [{
y: newArray,
mode: 'lines',
line: {color: '#80CAF6'}
}]);
var cnt = 0;
var interval = setInterval(function() {
var y = Math.round(Math.random()\*10) + 1
newArray = newArray.concat(y)
newArray.splice(0, 1)
var data\_update = {
y: [newArray]
};
Plotly.update('myDiv', data\_update)
if(++cnt === 100) clearInterval(interval);
}, 1000);
---
name: Streaming Subplots
suite: streaming
---
function rand() {
return Math.random();
}
var time = new Date();
var trace1 = {
x: [],
y: [],
mode: 'lines',
line: {
color: '#80CAF6',
shape: 'spline'
}
}
var trace2 = {
x: [],
y: [],
xaxis: 'x2',
yaxis: 'y2',
mode: 'lines',
line: {color: '#DF56F1'}
};
var layout = {
xaxis: {
type: 'date',
domain: [0, 1],
showticklabels: false
},
yaxis: {domain: [0.6,1]},
xaxis2: {
type: 'date',
anchor: 'y2',
domain: [0, 1]
},
yaxis2: {
anchor: 'x2',
domain: [0, 0.4]},
}
var data = [trace1,trace2];
Plotly.newPlot('myDiv', data, layout);
var cnt = 0;
var interval = setInterval(function() {
var time = new Date();
var update = {
x: [[time], [time]],
y: [[rand()], [rand()]]
}
Plotly.extendTraces('myDiv', update, [0,1])
if(++cnt === 100) clearInterval(interval);
}, 1000);
---
name: Button Events
permalink: javascript/custom-buttons/
description: How to bind callback functions to custom buttons in D3.js-based JavaScript charts.
thumbnail: thumbnail/custom-buttons.jpg
page\_type: example\_index
display\_as: controls
redirect\_from: javascript-graphing-library/custom-buttons/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","button-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Update Button
suite: button-events
markdown\_content: |
The `update` method should be used when modifying the data and layout sections of the graph.
This example demonstrates how to update which traces are displayed while simulaneously updating
layout attributes such as the chart title and annotations.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
const arrAvg = arr => arr.reduce((a,b) => a + b, 0) / arr.length
var button\_layer\_2\_height = 1.2
var high = unpack(rows, 'AAPL.High').map(x => parseFloat(x))
var low = unpack(rows, 'AAPL.Low').map(x => parseFloat(x))
var date = unpack(rows, 'Date')
var high\_ave = arrAvg(high)
var high\_max = Math.max(...high)
var low\_ave = arrAvg(low)
var low\_min = Math.min(...low)
var data = [{
x: date,
y: high,
mode: 'lines',
name: 'High',
marker: {color: '#33CFA5'}
},
{
x: date,
y: date.map(a => high\_ave),
mode: 'lines',
name: 'Low Average',
line: {color: '#33CFA5', dash: 'dash'},
visible: false
},
{
x: date,
y: low,
name: 'Low',
mode: 'lines',
marker: {color: '#F06A6A'}
},
{
x: date,
y: date.map(a => low\_ave),
mode: 'lines',
name: 'High Average',
visible: false,
line: {color: '#F06A6A', dash: 'dash'}
},
]
var high\_annotations = [
{
text: 'High Average:
' + high\_ave.toFixed(2),
x: '2016-03-01',
y: high\_ave,
yref: 'y', xref: 'x',
ay: -40, ax: 0
},
{
text: 'High Max:
' + high\_max.toFixed(2),
x: date[high.indexOf(high\_max)],
y: high\_max,
yref: 'y', xref: 'x',
ay: -40, ax: 0
},
]
var low\_annotations = [{
text: 'Low Average:
' + low\_ave.toFixed(2),
x: '2015-05-01',
y: low\_ave,
yref: 'y', xref: 'x',
ay: 40, ax: 0
},
{
text: 'Low Min:
' + low\_min.toFixed(2),
x: date[low.indexOf(low\_min)],
y: low\_min,
yref: 'y', xref: 'x',
ay: 40, ax: 0
}
]
var updatemenus=[
{
buttons: [
{
args: [{'visible': [true, true, false, false]},
{'title': 'Yahoo High',
'annotations': high\_annotations}],
label: 'High',
method: 'update'
},
{
args: [{'visible': [false, false, true, true,]},
{'title': 'Yahoo Low',
'annotations': low\_annotations}],
label: 'Low',
method: 'update'
},
{
args: [{'visible': [true, true, true, true,]},
{'title': 'Yahoo',
'annotations': [...low\_annotations, ...high\_annotations]}],
label: 'Both',
method: 'update'
},
{
args: [{'visible': [true, false, true, false,]},
{'title': 'Yahoo',
'annotations': []}],
label: 'Reset',
method: 'update'
},
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.1,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top'
},
]
var layout = {
title: {
text: 'Yahoo'
},
updatemenus: updatemenus,
showlegend: false
}
Plotly.newPlot("myDiv", data, layout);
});
---
name: Animate Button
suite: button-events
markdown\_content: |
Refer to our animation docs: [https://plotly.com/javascript/#animations](https://plotly.com/javascript/#animations) for examples on how to use the animate method with Plotly buttons.
---
---
name: Style the Buttons
suite: button-events
markdown\_content: |
When adding buttons to Plotly charts, users have the option of styling the color, font, padding,
and position of the buttons. The example below demonstrates how to apply different styling options.
See all updatemenus styling attributes here: [https://plotly.com/javascript/reference/layout/#layout-updatemenus](https://plotly.com/javascript/reference/layout/updatemenus/).
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/api\_docs/mt\_bruno\_elevation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var button\_layer\_1\_height = 1.12
var button\_layer\_2\_height = 1.0
var annotation\_offset = 0.04
var z\_data=[ ]
for(i=0;i<24;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type:'surface',
colorscale:'Viridis'
}]
var updatemenus=[
{
buttons: [
{
args: ['type', 'surface'],
label: '3D Surface',
method: 'restyle'
},
{
args: ['type', 'heatmap'],
label:'Heatmap',
method:'restyle'
},
{
args: ['type', 'contour'],
label:'Contour',
method:'restyle'
}
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.15,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top',
font: {color: '#5072a8'}
},
{
buttons: [
{
args: ['reversescale', true],
label: 'Reverse',
method: 'restyle'
},
{
args: ['reversescale', false],
label:'Undo Reverse',
method:'restyle'
}
],
direction: 'down',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'dropdown',
x: 0.56,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top',
active: 1,
font: {color: '#5072a8'}
},
{
buttons: [
{
args: [{'contours.showlines':false, 'type':'contour'}],
label: 'Hide lines',
method: 'restyle'
},
{
args: [{'contours.showlines':true, 'type':'contour'}],
label:'Show lines',
method:'restyle'
}
],
direction: 'down',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'dropdown',
x: 0.78,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top',
font: {color: '#5072a8'}
},
{
buttons: [
{
args: ['colorscale', 'Viridis'],
label: 'Viridis',
method: 'restyle'
},
{
args: ['colorscale', 'Electric'],
label:'Electric',
method:'restyle'
},
{
args: ['colorscale', 'Earth'],
label:'Earth',
method:'restyle'
},
{
args: ['colorscale', 'Hot'],
label:'Hot',
method:'restyle'
},
{
args: ['colorscale', 'Jet'],
label:'Jet',
method:'restyle'
},
{
args: ['colorscale', 'Portland'],
label:'Portland',
method:'restyle'
},
{
args: ['colorscale', 'Rainbow'],
label:'Rainbow',
method:'restyle'
},
{
args: ['colorscale', 'Blackbody'],
label:'Blackbody',
method:'restyle'
},
{
args: ['colorscale', 'Cividis'],
label:'Cividis',
method:'restyle'
}
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.15,
xanchor: 'left',
y: button\_layer\_1\_height,
yanchor: 'top',
active: 1,
bgcolor: '#aaaaaa',
bordercolor: '#FFFFFF'
},
]
var annotations = [
{
text: 'Trace type:',
x: 0,
y: button\_layer\_2\_height - annotation\_offset,
yref: 'paper',
align: 'left',
showarrow: false
},
{
text: 'Colorscale:',
x: 0,
y: button\_layer\_1\_height - annotation\_offset,
yref: 'paper',
align: 'left',
showarrow: false
},
]
var layout = {
paper\_bgcolor: 'black',
margin: {t: 0, b: 0, l: 0, r: 0},
updatemenus: updatemenus,
annotations: annotations,
scene: {
bgcolor: 'black',
aspectratio: {x: 1, y: 1, z: 0.7},
aspectmode: 'manual'
}
}
Plotly.newPlot("myDiv", data, layout);
});
---
name: Restyle Button Single Attribute
suite: button-events
markdown\_content: |
The `restyle` method should be used when modifying the data and data attributes of the graph
This example demonstrates how to update a single data attribute: chart type with the `restyle` method.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/api\_docs/mt\_bruno\_elevation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data=[ ]
for(i=0;i<24;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type:'surface',
colorscale:'Viridis'
}]
var updatemenus=[
{
buttons: [
{
args: ['type', 'surface'],
label: '3D Surface',
method: 'restyle'
},
{
args: ['type', 'heatmap'],
label:'Heatmap',
method:'restyle'
}
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.1,
xanchor: 'left',
y: 1.1,
yanchor: 'top'
}
]
var annotations = [
{
text: 'Trace type:',
x: 0,
y: 1.085,
yref: 'paper',
align: 'left',
showarrow: false
}
]
var layout = {
width: 800,
height: 900,
autosize: false,
margin: {t: 0, b: 0, l: 0, r: 0},
updatemenus: updatemenus,
annotations: annotations,
scene: {
xaxis:{
gridcolor: 'rgb(255, 255, 255)',
zerolinecolor: 'rgb(255, 255, 255)',
showbackground: true,
backgroundcolor:'rgb(230, 230,230)'
},
yaxis: {
gridcolor: 'rgb(255, 255, 255)',
zerolinecolor: 'rgb(255, 255, 255)',
showbackground: true,
backgroundcolor: 'rgb(230, 230, 230)'
},
zaxis: {
gridcolor: 'rgb(255, 255, 255)',
zerolinecolor: 'rgb(255, 255, 255)',
showbackground: true,
backgroundcolor: 'rgb(230, 230,230)'
},
aspectratio: {x: 1, y: 1, z: 0.7},
aspectmode: 'manual'
}
}
Plotly.newPlot("myDiv", data, layout);
});
---
name: Relayout Button
suite: button-events
markdown\_content: |
The `relayout` method should be used when modifying the layout attributes of the graph.
\*\*Update One Layout Attribute\*\*
This example demonstrates how to update a layout attribute: chart type with the `relayout` method.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/normal-clusters.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return parseFloat(row[key]); });
}
var button\_layer\_height = 1.2
var x0 = unpack(rows,'x0')
var x1 = unpack(rows,'x1')
var x2 = unpack(rows,'x2')
var y0 = unpack(rows,'y0')
var y1 = unpack(rows,'y1')
var y2 = unpack(rows,'y2')
var data = [{
x: x0,
y: y0,
mode: 'markers',
marker: {color: '#835AF1'}
},
{
x: x1,
y: y1,
mode: 'markers',
marker: {color: '#7FA6EE'}
},
{
x: x2,
y: y2,
mode: 'markers',
marker: {color: '#B8F7D4'}
},
]
var cluster0 = {type: 'circle',
xref: 'x', yref: 'y',
x0: Math.min(...x0), y0: Math.min(...y0),
x1: Math.max(...x0), y1: Math.max(...y0),
opacity: 0.25,
line: {color: '#835AF1'},
fillcolor: '#835AF1'}
var cluster1 = {type: 'circle',
xref: 'x', yref: 'y',
x0: Math.min(...x1), y0: Math.min(...y1),
x1: Math.max(...x1), y1: Math.max(...y1),
opacity: 0.25,
line: {color: '#7FA6EE'},
fillcolor: '#7FA6EE'}
var cluster2 = {type: 'circle',
xref: 'x', yref: 'y',
x0: Math.min(...x2), y0: Math.min(...y2),
x1: Math.max(...x2), y1: Math.max(...y2),
opacity: 0.25,
line: {color: '#B8F7D4'},
fillcolor: '#B8F7D4'}
var updatemenus=[
{
buttons: [
{
args: ['shapes', []],
label: 'None',
method: 'relayout'
},
{
args: ['shapes', [cluster0]],
label: 'Cluster 0',
method: 'relayout'
},
{
args: ['shapes', [cluster1]],
label: 'Cluster 1',
method: 'relayout'
},
{
args: ['shapes', [cluster2]],
label: 'Cluster 2',
method: 'relayout'
},
{
args: ['shapes', [cluster0, cluster1, cluster2]],
label: 'All',
method: 'relayout'
},
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.1,
xanchor: 'left',
y: button\_layer\_height,
yanchor: 'top'
},
]
var layout = {
updatemenus: updatemenus,
showlegend: false
}
Plotly.newPlot("myDiv", data, layout);
});
---
name: Restyle Button Multiple Attributes
suite: button-events
markdown\_content: |
This example demonstrates how to use a restyle button to update single attributes by passing a two element array
to a button's `args` attribute or update multiple attributes at the same time by passing an array containing an object.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/api\_docs/mt\_bruno\_elevation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var button\_layer\_1\_height = 1.12
var button\_layer\_2\_height = 1.0
var annotation\_offset = 0.04
var z\_data=[ ]
for(i=0;i<24;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type:'surface',
colorscale:'Viridis'
}]
var updatemenus=[
{
buttons: [
{
args: ['type', 'surface'],
label: '3D Surface',
method: 'restyle'
},
{
args: ['type', 'heatmap'],
label:'Heatmap',
method:'restyle'
},
{
args: ['type', 'contour'],
label:'Contour',
method:'restyle'
}
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.15,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top'
},
{
buttons: [
{
args: ['reversescale', true],
label: 'Reverse',
method: 'restyle'
},
{
args: ['reversescale', false],
label:'Undo Reverse',
method:'restyle'
}
],
direction: 'down',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'dropdown',
x: 0.56,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top'
},
{
buttons: [
{
args: [{'contours.showlines':false, 'type':'contour'}],
label: 'Hide lines',
method: 'restyle'
},
{
args: [{'contours.showlines':true, 'type':'contour'}],
label:'Show lines',
method:'restyle'
}
],
direction: 'down',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'dropdown',
x: 0.78,
xanchor: 'left',
y: button\_layer\_2\_height,
yanchor: 'top'
},
{
buttons: [
{
args: ['colorscale', 'Viridis'],
label: 'Viridis',
method: 'restyle'
},
{
args: ['colorscale', 'Electric'],
label:'Electric',
method:'restyle'
},
{
args: ['colorscale', 'Earth'],
label:'Earth',
method:'restyle'
},
{
args: ['colorscale', 'Hot'],
label:'Hot',
method:'restyle'
},
{
args: ['colorscale', 'Jet'],
label:'Jet',
method:'restyle'
},
{
args: ['colorscale', 'Portland'],
label:'Portland',
method:'restyle'
},
{
args: ['colorscale', 'Rainbow'],
label:'Rainbow',
method:'restyle'
},
{
args: ['colorscale', 'Blackbody'],
label:'Blackbody',
method:'restyle'
},
{
args: ['colorscale', 'Cividis'],
label:'Cividis',
method:'restyle'
}
],
direction: 'left',
pad: {'r': 10, 't': 10},
showactive: true,
type: 'buttons',
x: 0.15,
xanchor: 'left',
y: button\_layer\_1\_height,
yanchor: 'top'
},
]
var annotations = [
{
text: 'Trace type:',
x: 0,
y: button\_layer\_2\_height - annotation\_offset,
yref: 'paper',
align: 'left',
showarrow: false
},
{
text: 'Colorscale:',
x: 0,
y: button\_layer\_1\_height - annotation\_offset,
yref: 'paper',
align: 'left',
showarrow: false
},
]
var layout = {
margin: {t: 0, b: 0, l: 0, r: 0},
updatemenus: updatemenus,
annotations: annotations,
scene: {
xaxis:{
gridcolor: 'rgb(255, 255, 255)',
zerolinecolor: 'rgb(255, 255, 255)',
showbackground: true,
backgroundcolor:'rgb(230, 230,230)'
},
yaxis: {
gridcolor: 'rgb(255, 255, 255)',
zerolinecolor: 'rgb(255, 255, 255)',
showbackground: true,
backgroundcolor: 'rgb(230, 230, 230)'
},
zaxis: {
gridcolor: 'rgb(255, 255, 255)',
zerolinecolor: 'rgb(255, 255, 255)',
showbackground: true,
backgroundcolor: 'rgb(230, 230,230)'
},
aspectratio: {x: 1, y: 1, z: 0.7},
aspectmode: 'manual'
}
}
Plotly.newPlot("myDiv", data, layout);
});
---
name: Bind dropdown events to Plotly.js charts
suite: dropdowns-events
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var allCountryNames = unpack(rows, 'country'),
allYear = unpack(rows, 'year'),
allGdp = unpack(rows, 'gdpPercap'),
listofCountries = [],
currentCountry,
currentGdp = [],
currentYear = [];
for (var i = 0; i < allCountryNames.length; i++ ){
if (listofCountries.indexOf(allCountryNames[i]) === -1 ){
listofCountries.push(allCountryNames[i]);
}
}
function getCountryData(chosenCountry) {
currentGdp = [];
currentYear = [];
for (var i = 0 ; i < allCountryNames.length ; i++){
if ( allCountryNames[i] === chosenCountry ) {
currentGdp.push(allGdp[i]);
currentYear.push(allYear[i]);
}
}
};
// Default Country Data
setBubblePlot('Afghanistan');
function setBubblePlot(chosenCountry) {
getCountryData(chosenCountry);
var trace1 = {
x: currentYear,
y: currentGdp,
mode: 'lines+markers',
marker: {
size: 12,
opacity: 0.5
}
};
var data = [trace1];
var layout = {
title: {text: 'Line and Scatter Plot'},
height: 400,
width: 480
};
Plotly.newPlot('myDiv', data, layout);
};
var innerContainer = document.querySelector('[data-num="0"'),
plotEl = innerContainer.querySelector('.plot'),
countrySelector = innerContainer.querySelector('.countrydata');
function assignOptions(textArray, selector) {
for (var i = 0; i < textArray.length; i++) {
var currentOption = document.createElement('option');
currentOption.text = textArray[i];
selector.appendChild(currentOption);
}
}
assignOptions(listofCountries, countrySelector);
function updateCountry(){
setBubblePlot(countrySelector.value);
}
countrySelector.addEventListener('change', updateCountry, false);
});
---
name: Dropdown Events
permalink: javascript/dropdowns/
description: Use Plotly to create custom dropdowns in D3.js-based JavaScript charts.
thumbnail: thumbnail/dropdown.jpg
page\_type: example\_index
display\_as: controls
redirect\_from: javascript-graphing-library/high-dimension-data/
redirect\_from: javascript/high-dimension-data/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","dropdowns-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add Two Dropdown Menus to a Chart with Plotly.js
suite: dropdowns-events
---
function makeTrace(i) {
return {
y: Array.apply(null, Array(10)).map(() => Math.random()),
line: {
shape: 'spline' ,
color: 'red'
},
visible: i === 0,
name: 'Data set ' + i,
};
}
Plotly.newPlot('myDiv', [0, 1, 2, 3].map(makeTrace), {
updatemenus: [{
y: 0.8,
yanchor: 'top',
buttons: [{
method: 'restyle',
args: ['line.color', 'red'],
label: 'red'
}, {
method: 'restyle',
args: ['line.color', 'blue'],
label: 'blue'
}, {
method: 'restyle',
args: ['line.color', 'green'],
label: 'green'
}]
}, {
y: 1,
yanchor: 'top',
buttons: [{
method: 'restyle',
args: ['visible', [true, false, false, false]],
label: 'Data set 0'
}, {
method: 'restyle',
args: ['visible', [false, true, false, false]],
label: 'Data set 1'
}, {
method: 'restyle',
args: ['visible', [false, false, true, false]],
label: 'Data set 2'
}, {
method: 'restyle',
args: ['visible', [false, false, false, true]],
label: 'Data set 3'
}]
}],
});
---
name: Lasso Selection
permalink: javascript/lasso-selection/
description: How to bind callback functions to lasso selection in JavaScript D3.js-based charts.
thumbnail: thumbnail/lasso.jpg
page\_type: example\_index
display\_as: controls
redirect\_from: javascript-graphing-library/lasso-selection/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","lasso-selection" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Lasso Selection
suite: lasso-selection
---
var graphDiv = document.getElementById('myDiv');
var N = 1000;
var color1 = '#7b3294';
var color1Light = '#c2a5cf';
var colorX = '#ffa7b5';
var colorY = '#fdae61';
function randomArray() {
var out = new Array(N);
for(var i = 0; i < N; i++) {
out[i] = Math.random();
}
return out;
}
var x = randomArray();
var y = randomArray();
Plotly.newPlot(graphDiv, [{
type: 'scatter',
mode: 'markers',
x: x,
y: y,
xaxis: 'x',
yaxis: 'y',
name: 'random data',
marker: {color: color1, size: 10}
}, {
type: 'histogram',
x: x,
xaxis: 'x2',
yaxis: 'y2',
name: 'x coord dist.',
marker: {color: colorX}
}, {
type: 'histogram',
x: y,
xaxis: 'x3',
yaxis: 'y3',
name: 'y coord dist.',
marker: {color: colorY}
}], {
title: {
text: 'Lasso around the scatter points to see sub-distributions'
},
dragmode: 'lasso',
xaxis: {
zeroline: false,
},
yaxis: {
domain: [0.55, 1],
},
xaxis2: {
domain: [0, 0.45],
anchor: 'y2',
},
yaxis2: {
domain: [0, 0.45],
anchor: 'x2'
},
xaxis3: {
domain: [0.55, 1],
anchor: 'y3'
},
yaxis3: {
domain: [0, 0.45],
anchor: 'x3'
}
});
graphDiv.on('plotly\_selected', function(eventData) {
var x = [];
var y = [];
var colors = [];
for(var i = 0; i < N; i++) colors.push(color1Light);
console.log(eventData.points)
eventData.points.forEach(function(pt) {
x.push(pt.x);
y.push(pt.y);
colors[pt.pointNumber] = color1;
});
Plotly.restyle(graphDiv, {
x: [x, y],
xbins: {}
}, [1, 2]);
Plotly.restyle(graphDiv, 'marker.color', [colors], [0]);
});
---
permalink: javascript/controls/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make controls in charts.
name: Add Custom Controls
layout: langindex
language: plotly_js
display_as: controls
thumbnail: thumbnail/mixed.jpg
page_type: example_index
---


<header class="--welcome">
	<div class="--welcome-body">
		<!--div.--wrap-inner-->
		<div class="--title">

			<div class="--body">
				<h1>Add Custom Controls</h1>
				<p>{{page.description}}</p>
				{% include layouts/dashplug.html %}
			</div>
		</div>
	</div>
</header>

		{% assign languagelist = site.posts | where:"language","plotly_js" | where:"display_as","controls" | where: "layout","base" | sort: "order" %}
        {% include posts/documentation_eg.html %}

---
name: Bind Components to the Appearance of a Plot
suite: slider-components-events
---
Plotly.newPlot('myDiv', [{
x: [1, 2, 3],
y: [2, 1, 3]
}], {
sliders: [{
pad: {t: 30},
len: 0.5,
x: 0.5,
currentvalue: {
xanchor: 'right',
prefix: 'color: ',
font: {
color: '#888',
size: 20
}
},
// If all of a component's commands affect a single attribute, the component
// will be bound to the plot and will automatically update to reflect changes.
steps: [{
label: 'red',
method: 'restyle',
args: ['line.color', 'red']
}, {
label: 'green',
method: 'restyle',
args: ['line.color', 'green']
}, {
label: 'blue',
method: 'restyle',
args: ['line.color', 'blue']
}]
}],
updatemenus: [{
pad: {t: 60, r: 30},
type: 'buttons',
xanchor: 'left',
yanchor: 'top',
x: 00,
y: 0,
direction: 'right',
buttons: [{
label: 'red',
method: 'restyle',
args: ['line.color', 'red']
}, {
label: 'green',
method: 'restyle',
args: ['line.color', 'green']
}, {
label: 'blue',
method: 'restyle',
args: ['line.color', 'blue']
}]
}]
});
---
name: Adding Sliders to Animations
permalink: javascript/gapminder-example/
description: How to make the classic Gapminder Animation using sliders and buttons in Plotly JS
thumbnail: thumbnail/gapminder\_animation.gif
page\_type: example\_index
display\_as: animations
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","adding-sliders" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Slider
suite: slider-components-events
---
Plotly.newPlot('myDiv', [{
x: [1, 2, 3],
y: [2, 1, 3]
}], {
sliders: [{
pad: {t: 30},
currentvalue: {
xanchor: 'right',
prefix: 'color: ',
font: {
color: '#888',
size: 20
}
},
steps: [{
label: 'red',
method: 'restyle',
args: ['line.color', 'red']
}, {
label: 'green',
method: 'restyle',
args: ['line.color', 'green']
}, {
label: 'blue',
method: 'restyle',
args: ['line.color', 'blue']
}]
}]
});
---
name: Slider Events
permalink: javascript/sliders/
description: Use Plotly to create custom sliders in D3.js-based JavaScript charts.
thumbnail: thumbnail/slider-component.jpg
page\_type: example\_index
display\_as: controls
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","slider-components-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add a Play Button to Control a Slider
suite: slider-components-events
---
Plotly.newPlot('myDiv', {
data: [{
x: [1, 2, 3],
y: [2, 1, 3],
line: {
color: 'red',
simplify: false,
}
}],
layout: {
sliders: [{
pad: {t: 30},
x: 0.05,
len: 0.95,
currentvalue: {
xanchor: 'right',
prefix: 'color: ',
font: {
color: '#888',
size: 20
}
},
transition: {duration: 500},
// By default, animate commands are bound to the most recently animated frame:
steps: [{
label: 'red',
method: 'animate',
args: [['red'], {
mode: 'immediate',
frame: {redraw: false, duration: 500},
transition: {duration: 500}
}]
}, {
label: 'green',
method: 'animate',
args: [['green'], {
mode: 'immediate',
frame: {redraw: false, duration: 500},
transition: {duration: 500}
}]
}, {
label: 'blue',
method: 'animate',
args: [['blue'], {
mode: 'immediate',
frame: {redraw: false, duration: 500},
transition: {duration: 500}
}]
}]
}],
updatemenus: [{
type: 'buttons',
showactive: false,
x: 0.05,
y: 0,
xanchor: 'right',
yanchor: 'top',
pad: {t: 60, r: 20},
buttons: [{
label: 'Play',
method: 'animate',
args: [null, {
fromcurrent: true,
frame: {redraw: false, duration: 1000},
transition: {duration: 500}
}]
}]
}]
},
// The slider itself does not contain any notion of timing, so animating a slider
// must be accomplished through a sequence of frames. Here we'll change the color
// and the data of a single trace:
frames: [{
name: 'red',
data: [{
y: [2, 1, 3],
'line.color': 'red'
}]
}, {
name: 'green',
data: [{
y: [3, 2, 1],
'line.color': 'green'}]
}, {
name: 'blue',
data: [{
y: [1, 3, 2],
'line.color': 'blue'}]
}]
});
---
name: Basic Range Slider on Time Series
suite: range-slider
---
var rawDataURL = 'https://raw.githubusercontent.com/plotly/datasets/master/2016-weather-data-seattle.csv';
var xField = 'Date';
var yField = 'Mean\_TemperatureC';
var selectorOptions = {
buttons: [{
step: 'month',
stepmode: 'backward',
count: 1,
label: '1m'
}, {
step: 'month',
stepmode: 'backward',
count: 6,
label: '6m'
}, {
step: 'year',
stepmode: 'todate',
count: 1,
label: 'YTD'
}, {
step: 'year',
stepmode: 'backward',
count: 1,
label: '1y'
}, {
step: 'all',
}],
};
d3.csv(rawDataURL, function(err, rawData) {
if(err) throw err;
var data = prepData(rawData);
var layout = {
title: {
text: 'Time series with range slider and selectors'
},
xaxis: {
rangeselector: selectorOptions,
rangeslider: {}
},
yaxis: {
fixedrange: true
}
};
Plotly.newPlot('myDiv', data, layout);
});
function prepData(rawData) {
var x = [];
var y = [];
rawData.forEach(function(datum, i) {
x.push(new Date(datum[xField]));
y.push(datum[yField]);
});
return [{
mode: 'lines',
x: x,
y: y
}];
}
---
name: Range Slider and Selector
permalink: javascript/range-slider/
description: How to add range sliders to a D3.js-based line or scatter chart. Examples of Range Sliders
thumbnail: thumbnail/sliders.jpg
page\_type: example\_index
display\_as: controls
redirect\_from: javascript-graphing-library/range-slider/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","range-slider" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
description: How to export graphs as static images in JavaScript. The Plotly JavaScript
  graphing library supports `.jpg`, `.png`, and `.svg` as formats for static image
  export.
display_as: file_settings
language: plotly_js
name: Static Image Export
order: 25
page_type: u-guide
permalink: javascript/static-image-export/
thumbnail: thumbnail/png-export.png
---

You can save graphs created with `plotly.js` to static images and view them in your browser. Consider the following example:

    var img_jpg= d3.select('#jpg-export');

    // Plotting the Graph

    var trace={x:[3,9,8,10,4,6,5],y:[5,7,6,7,8,9,8],type:"scatter"};
    var trace1={x:[3,4,1,6,8,9,5],y:[4,2,5,2,1,7,3],type:"scatter"};
    var data = [trace,trace1];
    var layout = {title : "Simple JavaScript Graph"};
    Plotly.newPlot(
      'plotly_div',
       data,
       layout)

    // static image in jpg format

    .then(
        function(gd)
         {
          Plotly.toImage(gd,{height:300,width:300})
             .then(
                 function(url)
             {
                 img_jpg.attr("src", url);
             }
             )
        });
To view this image in your page include following HTML tag:

    <img id="jpg-export"></img>

Height and width of the image can be adjusted by specifying the same in `toImage` call:

    Plotly.toImage(
    gd,{
      format:'jpeg',
      height:desired_height,
      width:desired_width,
    });

You can also save the image using different formats.

# Formats Supported

The common image formats: 'PNG', 'JPG/JPEG' are supported. In addition, formats like 'EPS', 'SVG' and 'PDF' are also available for user with a Personal or Professional subscription. You can get more details on our [pricing page] (https://plotly.com/products/cloud/)

**Note:** It is important to note that any figures containing WebGL traces (i.e. of type scattergl, heatmapgl, contourgl, scatter3d, surface, mesh3d, scatterpolargl, cone, streamtube, splom, or parcoords) that are exported in a vector format like SVG, EPS or PDF will include encapsulated rasters instead of vectors for some parts of the image.

## Saving as PNG ##
      img_png.attr("src", url);
      Plotly.toImage(gd,{format:'png',height:400,width:400});

## Saving as SVG ##
    img_svg.attr("src", url);
    Plotly.toImage(gd,{format:'svg',height:800,width:800});

---
name: Customize Hover for Spikelines
suite: 3d-hover
markdown\_content: |
By default, Plotly's 3D plots display lines called "spikelines" while hovering over a point.
These lines project from the hover point to each of the three axes' normal planes and
then extend from those projection data points to the planes' wall boundaries.
---
function getrandom(num , mul)
{
var value = [ ];
for(i=0;i<=num;i++)
{
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var data=[
{
opacity:0.4,
type: 'scatter3d',
x: getrandom(50 , -75),
y: getrandom(50 , -75),
z: getrandom(50 , -75),
},
];
var layout = {
scene:{
xaxis: {
spikecolor: '#1fe5bd',
spikesides: false,
spikethickness: 6
},
yaxis: {
spikecolor: '#1fe5bd',
spikesides: false,
spikethickness: 6
},
zaxis: {
spikecolor: '#1fe5bd',
spikethickness: 6
}
},
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to customize hover options for 3d charts.
display\_as: file\_settings
name: 3D Hover Options
order: 13
page\_type: u-guide
permalink: javascript/3d-hover/
thumbnail: thumbnail/subplots.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-hover" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Customize Hover for Surface Contours
suite: 3d-hover
markdown\_content: |
In addition to spikelines, Plotly 3D Surface plots also display surface contours on hover by default.
These are customized by styling the [`contours`](https://plotly.com/javascript/reference/surface/#surface-contours)
attribute in the surface trace.
---
x = [10,20,30,40]
y = [0,1,2,3]
z = [
[2,2,2,3],
[1,1,1,1],
[1,1,0,0],
[0,0,0,0]
];
var data=[
{
opacity:0.9,
type: 'surface',
x:x, y:y, z:z,
contours: {
x: {
highlight: true,
highlightcolor: "#41a7b3"
},
y: { highlight: false },
z: { highlight: false}
}
},
];
var layout = {
scene:{
xaxis: { showspikes: false },
yaxis: { showspikes: false },
zaxis: { showspikes: false }
},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Plotting CSV Data from Ajax Call
suite: ajax
---
function makeplot() {
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/2014\_apple\_stock.csv", function(data){ processData(data) } );
};
function processData(allRows) {
console.log(allRows);
var x = [], y = [], standard\_deviation = [];
for (var i=0; i<allRows.length; i++) {
row = allRows[i];
x.push( row['AAPL\_x'] );
y.push( row['AAPL\_y'] );
}
console.log( 'X',x, 'Y',y, 'SD',standard\_deviation );
makePlotly( x, y, standard\_deviation );
}
function makePlotly( x, y, standard\_deviation ){
var plotDiv = document.getElementById("plot");
var traces = [{
x: x,
y: y
}];
Plotly.newPlot('myDiv', traces, {
title: {
text: 'Plotting CSV data from AJAX call'
}
});
};
makeplot();
---
name: Read CSV Data from an Ajax Call
permalink: javascript/ajax-call/
description: How to make Ajax calls in javascript for Plotlyjs.
thumbnail: thumbnail/line-plots.jpg
page\_type: example\_index
display\_as: tutorials
redirect\_from: javascript-graphing-library/ajax-call/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","ajax" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
description: How to use colorway to set default trace colors in JavaScript with Plotly.
display\_as: file\_settings
name: Colorway
page\_type: u-guide
permalink: javascript/colorway/
thumbnail: thumbnail/colorway.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","colorway" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Set Default Trace Colors with colorway
suite: colorway
---
function linspace(a,b,n) {
return d3.range(n).map(function(i){return a+i\*(b-a)/(n-1);});
}
const parabolaGen = (a, b) =>
x => x\*x\*a + b;
var as = linspace(1, 3, 7);
var bs = linspace(2, 14, 7);
var x = linspace(-1, 3, 50);
var data = [];
for (i=0; i< as.length; i++ ){
data.push({
type: "scatter",
mode: "lines",
x: x,
y: x.map(parabolaGen(as[i],bs[i]))
})
}
var layout = {
colorway : ['#f3cec9', '#e7a4b6', '#cd7eaf', '#a262a9', '#6f4d96', '#3d3b72', '#182844']
};
Plotly.newPlot('myDiv', data, layout);
---
name: Add a Logo
suite: images
---
var data = [
{
x: ["-35.3", "-15.9", "-15.8", "-15.6", "-11.1", "-9.6", "-9.2", "-3.5", "-1.9", "-0.9", "1.0", "1.4", "1.7", "2.0", "2.8", "6.2", "8.1", "8.5", "8.5", "8.6", "11.4", "12.5", "13.3", "13.7", "14.4", "17.5", "17.7", "18.9", "25.1", "28.9", "41.4"],
y: ["Designers, musicians, artists, etc.", "Secretaries and administrative assistants", "Waiters and servers", "Archivists, curators, and librarians", "Sales and related", "Childcare workers, home car workers, etc.", "Food preparation occupations", "Janitors, maids, etc.", "Healthcare technicians, assistants. and aides", "Counselors, social and religious workers", "Physical, life and social scientists", "Construction", "Factory assembly workers", "Machinists, repairmen, etc.", "Media and communications workers", "Teachers", "Mechanics, repairmen, etc.", "Financial analysts and advisers", "Farming, fishing and forestry workers", "Truck drivers, heavy equipment operator, etc.", "Accountants and auditors", "Human resources, management analysts, etc.", "Managers", "Lawyers and judges", "Engineers, architects and surveyors", "Nurses", "Legal support workers", "Computer programmers and system admin.", "Police officers and firefighters", "Chief executives", "Doctors, dentists and surgeons"],
marker: {
color: "rgb(253, 240, 54)",
line: {
color: "rgb(0, 0, 0)",
width: 2
}
},
name: "y",
orientation: "h",
type: "bar",
}
];
var layout = {
autosize: false,
bargap: 0.15,
bargroupgap: 0.1,
barmode: "stack",
height: 800,
hovermode: "x",
images: [
{
x: 1,
y: 1.05,
sizex: 0.2,
sizey: 0.2,
source: "https://raw.githubusercontent.com/cldougl/plot\_images/add\_r\_img/vox.png",
xanchor: "right",
xref: "paper",
yanchor: "bottom",
yref: "paper"
}
],
margin: {
r: 20,
t: 125,
b: 75,
l: 300
},
title: {
text: "Moving Up, Moving Down
*Percentile change in income between childhood and adulthood*"
},
width: 700,
xaxis: {
tickmode: "linear",
dtick: 10,
gridcolor: "rgba(102, 102, 102, 0.4)",
linecolor: "#000",
linewidth: 1,
mirror: true,
nticks: 0,
showticklabels: true,
tick0: 0,
tickwidth: 1,
title: {
text: "*Change in percentile*"
},
},
yaxis: {
anchor: "x",
tickmode: "linear",
gridcolor: "rgba(102, 102, 102, 0.4)",
gridwidth: 1,
linecolor: "#000",
linewidth: 1,
mirror: true,
showgrid: false,
showline: true,
showticklabels: true,
tick0: 0,
type: "category",
zeroline: false
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to add images to charts as background images or logos.
display\_as: file\_settings
name: Images
page\_type: u-guide
permalink: javascript/images/
redirect\_from: javascript-graphing-library/images/
thumbnail: thumbnail/images.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","images" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add Multiple Images
suite: images
---
Plotly.newPlot('myDiv', [{
x: [1, 2, 3],
y: [1, 2, 3]
}], {
images: [
{
"source": "https://images.plot.ly/language-icons/api-home/python-logo.png",
"xref": "paper",
"yref": "paper",
"x": 0,
"y": 1,
"sizex": 0.2,
"sizey": 0.2,
"xanchor": "right",
"yanchor": "bottom"
},
{
"source": "https://images.plot.ly/language-icons/api-home/js-logo.png",
"xref": "x",
"yref": "y",
"x": 1.5,
"y": 2,
"sizex": 1,
"sizey": 1,
"xanchor": "right",
"yanchor": "bottom"
},
{
"source": "https://images.plot.ly/language-icons/api-home/r-logo.png",
"xref": "x",
"yref": "y",
"x": 1,
"y": 3,
"sizex": 2,
"sizey": 2,
"sizing": "stretch",
"opacity": 0.4,
"layer": "below"
},
{
"source": "https://images.plot.ly/language-icons/api-home/matlab-logo.png",
"xref": "x",
"yref": "paper",
"x": 3,
"y": 0,
"sizex": 0.5,
"sizey": 1,
"opacity": 1,
"xanchor": "right",
"yanchor": "middle"
},
]
})
---
name: Add Named Container Array Items
suite: layout\_template
markdown\_content: |
Container array items in a template with a `name` attribute will be added to any plot using that template.
We can use this feature to create a template that adds watermarks to our chart by including named image items in `images`.
The example below also shows how to make one of these images invisible using the `templateitemname` attribute
if you don't want it to display for this specific chart.
---
var baseLayout = {
title: {
text: 'Watermark Template'
},
// items with a `name` attribute in template.images will be added to any
// plot using this template
images: [{
name: 'watermark\_1',
source: "https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/benzene.png",
xref: "paper",
yref: "paper",
x: 0.40,
y: 0.9,
sizex: 0.7,
sizey: 0.7,
opacity: 0.1,
layer: "below"
},
{
name: 'watermark\_2',
source: "https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/naphthalene.png",
xref: "paper",
yref: "paper",
x: .75,
y: 0.3,
sizex: 0.25,
sizey: 0.25,
sizing: "stretch",
opacity: 0.2,
layer: "below"
}],
showlegend: false
};
var template = {data: {}, layout: baseLayout};
var data = [{
x: [0, 1, 2, 3, 4, 5],
y: [2, 4, 3, 0, 5, 6],
}];
var layoutUsingTemplate = {
template: template,
images: [
{
// set the second watermark in the template to be invisible
templateitemname: 'watermark\_2',
visible: false
}
]
};
Plotly.newPlot("myDiv", data, layoutUsingTemplate);
---
name: The Layout Template Attribute
suite: layout\_template
markdown\_content: |
The `template` attribute of `layout` allows a Plotly chart to take it's style and formatting from a `template`
object. `template`s can be generated using [Plotly.makeTemplate](https://plotly.com/javascript/plotlyjs-function-reference/#plotlymaketemplate)
or manually. `annotaions`, `updatemenus`, `images`, `shapes` and other container array objects in the Plotly `layout`
are specially handled by the template machinery to provide more flexibility when using these container arrays
in plots derived from these templates.
For more information see [https://plotly.com/javascript/reference/layout/#layout-template](https://plotly.com/javascript/reference/layout/#layout-template).
---
---
name: Matching Named Template Container Items
suite: layout\_template
markdown\_content: |
A container item in your new plot with the attribute `templateitemname` matching one of the named
container items in the template will inherit attributes from item with the corresponding name.
If an item in the plot using the template has the `templateitemname` attribute but there is no
corresponding template container item by the same name, it will be marked as invisible in your new plot.
---
var x = [0, 1, 2, 3, 4, 5];
var y = [2, 4, 3, 0, 5, 6];
var baseData = [{
mode: 'lines',
error\_y: {visible: true, width: 0},
line: {color: 'teal'}
}];
var baseLayout = {
title: {
text: 'Template Title'
},
annotations: [{
text: 'First point',
name:'first',
yref: 'y', xref: 'x',
ay: 40, ax: 30,
font: {size: 16}
}],
showlegend: false
};
// use Plotly.makeTemplate to generate the template object
var template = Plotly.makeTemplate({data: baseData, layout: baseLayout});
var data = [{
x: x,
y: y,
}];
var annotations = [
// plotly will look for an annotation with `name` matching `templateitemname`
// and use insert that annotation into the new plot.
{
templateitemname:'first',
x: x[0],
y: y[0],
},
{
templateitemname: 'fourth', //since there is no template item with this name,
//this annotation will be set to invisible.
text: 'Fourth point',
x: x[3],
y: y[3],
showarrow: true,
yref: 'y', xref: 'x',
}
];
var layoutWithTemplate = {template: template, annotations: annotations};
Plotly.newPlot("myDiv", data, layoutWithTemplate);
---
name: Creating Default Item Values
suite: layout\_template
markdown\_content: |
Add an attribute called `annotationdefaults` to your template to set a default annotation object. Each
item in the plot using the template without a `templateitemname` attribute will have the default applied
to it. `annotationdefaults` can be manually added to a template or, if makeTemplate is used, the first un-named
item in annotations will be used as the default.
Note, this behaviour works for all container array objects. E.g for `images`, you would create `imagedefaults` in
your layout containing the default image item.
---
var x = [0, 1, 2, 3, 4, 5];
var y = [2, 4, 3, 0, 5, 6];
var baseData = [{
mode: 'lines',
error\_y: {visible: true, width: 0},
line: {color: 'teal'}
}];
var baseLayout = {
// Plotly.makeTemplate will use the first annotation without a `name` attribute
// in the annotations array as the annotationdefaults for the template.
annotations: [
{
text: 'DEFAULT ANNOTATION',
x: 0.1,
y: 1.1,
yref: 'paper', xref: 'paper',
showarrow: false,
font: {color:'teal', size: 14}
}
],
showlegend: false
};
// use Plotly.makeTemplate to generate the template object
var template = Plotly.makeTemplate({data: baseData, layout: baseLayout});
var data = [{
x: x,
y: y
}];
var annotations = [
{}, // An empty annotation object will copy annotationdefaults
{
text: 'Third point',
x: x[2],
y: y[2],
showarrow: true,
yref: 'y', xref: 'x',
font: {size: 20} // since there is no font.color attribute for this object,
// it will use the annotationdefaults' color
}
];
var layoutWithTemplate = {template: template, annotations: annotations};
Plotly.newPlot("myDiv", data, layoutWithTemplate);
---
description: Plotly's template attribute and how to use it with Container arrays.
display\_as: file\_settings
name: Layout Template Examples
order: 19
page\_type: u-guide
permalink: javascript/layout-template/
thumbnail: thumbnail/plotly-express.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","layout\_template" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Adjusting Height, Width, and Margins
suite: sizing
---
var data = [
{
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
}
];
var layout = {
autosize: false,
width: 500,
height: 500,
margin: {
l: 50,
r: 50,
b: 100,
t: 100,
pad: 4
},
paper\_bgcolor: '#7f7f7f',
plot\_bgcolor: '#c7c7c7'
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to change the size of D3.js-based graphs in javascript.
display\_as: file\_settings
name: Setting Graph Size
order: 21
page\_type: u-guide
permalink: javascript/setting-graph-size/
redirect\_from: javascript-graphing-library/setting-graph-size/
thumbnail: thumbnail/multiple-axes.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","sizing" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Automatically Adjust Margins
suite: sizing
markdown\_content: |
Set `automargin=true` ([reference](https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-automargin)) and Plotly will automatically increase the margin size to prevent ticklabels from being cut off or overlapping with axis titles.
---
var data = [
{
x: ['Apples', 'Oranges', 'Watermelon', 'Pears'],
y: [3, 2, 1, 4],
type: 'bar'
}
];
var layout = {
autosize: false,
width: 500,
height: 500,
yaxis: {
title: {
text: 'Y-axis Title',
font: { size: 30 }
},
ticktext: ['long label','Very long label','3','label'],
tickvals: [1, 2, 3, 4],
tickmode: 'array',
automargin: true,
},
paper\_bgcolor: '#7f7f7f',
plot\_bgcolor: '#c7c7c7'
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to edit and style the font of D3.js-based graphs in javascript.
display\_as: file\_settings
name: Text and Font Styling
page\_type: u-guide
permalink: javascript/font/
redirect\_from: javascript-graphing-library/font/
thumbnail: thumbnail/hover-text.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","font" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Global Font Properties
suite: font
---
var data = [
{
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
}
];
var layout = {
title: {
text: 'Global Font'
},
font: {
family: 'Courier New, monospace',
size: 18,
color: '#7f7f7f'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Customize Text Template
suite: texttemplate
markdown\_content: |
The following example uses [textfont](https://plotly.com/javascript/reference/scatterternary/#scatterternary-textfont) to customize the added text.
---
var data = [{
type: "scatterternary",
a: [3, 2, 5],
b: [2, 5, 2],
c: [5, 2, 2],
mode: "markers+text",
text: ["A", "B", "C"],
texttemplate: "%{text}
(%{a:.2f}, %{b:.2f}, %{c:.2f})",
textposition: "bottom center",
textfont:{'family': "Times", 'size': [18, 21, 20], 'color': ["IndianRed", "MediumPurple", "DarkOrange"]}
}];
Plotly.newPlot("myDiv", data)
---
description: How to use D3.js-based text template in Plotly.js.
display\_as: file\_settings
has\_thumbnail: true
name: Text Template
order: 24
page\_type: u-guide
permalink: javascript/texttemplate/
thumbnail: thumbnail/texttemplate.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","texttemplate" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add Text Template in Pie Chart
suite: texttemplate
markdown\_content: |
To show an arbitrary text in your chart you can use [texttemplate](https://plotly.com/javascript/reference/pie/#pie-texttemplate), which is a template string used for rendering the information, and will override [textinfo](https://plotly.com/javascript/reference/treemap/#treemap-textinfo).
---
var data = [{
type: "pie",
values: [2, 5, 3, 2.5],
labels: ["R", "Python", "Java Script", "Matlab"],
texttemplate: "%{label}: %{value} (%{percent})",
textposition: "inside"
}];
Plotly.newPlot("myDiv", data)
---
name: Set Date in Text Template
suite: texttemplate
markdown\_content: |
The following example displays how to show date by setting [axis.type](https://plotly.com/javascript/reference/layout/yaxis/#layout-yaxis-type) in [funnel charts](https://plotly.com/javascript/funnel-charts/).
---
var data = [{
type: 'funnel',
name: 'Montreal',
orientation: "h",
y: ["2018-01-01", "2018-07-01", "2019-01-01", "2020-01-01"],
x: [100, 60, 40, 20],
textposition: "inside",
texttemplate: "%{label}"
},{
type: "funnel",
name: 'Vancouver',
orientation: "h",
y: ["2018-01-01", "2018-07-01", "2019-01-01", "2020-01-01"],
x: [90, 70, 50, 10],
textposition: "inside",
textinfo: "label"}]
var layout = {yaxis: {type: 'date'}}
Plotly.newPlot("myDiv", data, layout)
---
description: How to create figures with responsive/fluid layouts in JavaScript.
display\_as: file\_settings
name: Responsive / Fluid Layouts
page\_type: example\_index
permalink: javascript/responsive-fluid-layout/
redirect\_from: javascript-graphing-library/responsive-fluid-layout/
thumbnail: thumbnail/fluid-layout.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","responsive-fluid-layout" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Responsive Plots
suite: responsive-fluid-layout
markdown\_content: |
If you set the `responsive` attribute equal to `true` (using the `config` object), then your figures will be automatically resized when the browser window size changes. This is an especially useful feature for charts which are going to viewed on mobile devices!
---
var trace1 = {
type: 'bar',
x: [1, 2, 3, 4],
y: [5, 10, 2, 8],
marker: {
color: '#C8A2C8',
line: {
width: 2.5
}
}
};
var data = [ trace1 ];
var layout = {
title: {
text: 'Responsive to window\'s size!'
},
font: {size: 18}
};
var config = {responsive: true}
Plotly.newPlot('myDiv', data, layout, config );
---
name: Display Edit in Chart Studio Modebar Button
suite: configuration
order: 7.1
---
var data = [{
values: [19, 26, 55],
labels: ['Residential', 'Non-Residential', 'Utility'],
type: 'pie'
}];
var layout = {
title: {
text: 'Show Edit in Chart Studio Modebar Button'
}
};
var config = {
showEditInChartStudio: true,
plotlyServerURL: "https://chart-studio.plotly.com"
};
Plotly.newPlot('myDiv', data, layout, config);
---
name: Making a Static Chart
suite: configuration
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6],
y: [1, 9, 4, 7, 5, 2, 4],
mode: 'markers',
marker: {
size: [20, 40, 25, 10, 60, 90, 30],
}
};
var data = [trace1];
var layout = {
title: {
text: 'Create a Static Chart'
},
showlegend: false
};
Plotly.newPlot('myDiv', data, layout, {staticPlot: true});
---
description: How to set the configuration options for figures in JavaScript.
display\_as: file\_settings
name: Configuration Options
page\_type: example\_index
permalink: javascript/configuration-options/
thumbnail: thumbnail/modebar-icons.png
---
The plotly.js `config` argument sets properties like the mode bar buttons and the interactivity in the chart.
It's the last argument in `Plotly.newPlot` calls.

View the full list of configuration options in the
[plotly.js source code on GitHub](https://github.com/plotly/plotly.js/blob/master/src/plot_api/plot_config.js#L22-L86).

{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","configuration" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add Buttons to ModeBar
suite: configuration
order: 5.7
markdown\_content: |
The following example shows how to add a button to your modebar, either by using one of the [Plotly icons](https://github.com/plotly/plotly.js/blob/master/src/fonts/ploticon.js) or an [arbitrary icon](https://fontawesome.com/icons?d=gallery&m=free) with a custom behaviour.
---
var icon1 = {
'width': 500,
'height': 600,
'path': 'M224 512c35.32 0 63.97-28.65 63.97-64H160.03c0 35.35 28.65 64 63.97 64zm215.39-149.71c-19.32-20.76-55.47-51.99-55.47-154.29 0-77.7-54.48-139.9-127.94-155.16V32c0-17.67-14.32-32-31.98-32s-31.98 14.33-31.98 32v20.84C118.56 68.1 64.08 130.3 64.08 208c0 102.3-36.15 133.53-55.47 154.29-6 6.45-8.66 14.16-8.61 21.71.11 16.4 12.98 32 32.1 32h383.8c19.12 0 32-15.6 32.1-32 .05-7.55-2.61-15.27-8.61-21.71z'
}
var colors = ['green', 'red', 'blue']
var data = [{
mode: 'lines',
y: [2, 1, 2],
line: {color: colors[0], width: 3, shape: 'spline'}
}]
var layout = {
title: {
text: 'add mode bar button with custom icon'
}
}
var config = {
displayModeBar: true,
modeBarButtonsToAdd: [
{
name: 'color toggler',
icon: icon1,
click: function(gd) {
var newColor = colors[Math.floor(3 \* Math.random())]
Plotly.restyle(gd, 'line.color', newColor)
}},
{
name: 'button1',
icon: Plotly.Icons.pencil,
direction: 'up',
click: function(gd) {alert('button1')
}}],
modeBarButtonsToRemove: ['pan2d','select2d','lasso2d','resetScale2d','zoomOut2d']}
Plotly.newPlot('myDiv', data, layout, config)
---
name: Customize The `Edit Chart` Link Text
suite: configuration
---
var data = [{
z: [[0, 1, 2, 3, 4, 5, 6],
[1, 9, 4, 7, 5, 2, 4],
[2, 4, 2, 1, 6, 9, 3]],
type: 'heatmap'}]
var layout = {
title: {
text: 'Customize The Edit Chart Link Text'
}
};
var config = {
showLink: true,
plotlyServerURL: "https://chart-studio.plotly.com",
linkText: 'This text is custom!'
};
Plotly.newPlot('myDiv', data, layout, config)
---
name: Hide the Plotly Logo on the Modebar
suite: configuration
---
var trace1 = {
x:['trees', 'flowers', 'hedges'],
y: [90, 130, 40],
type: 'bar'
};
var data = [trace1];
var layout = {
title: {
text: 'Hide the Plotly Logo on the Modebar'
},
showlegend: false
};
Plotly.newPlot('myDiv', data, layout, {displaylogo: false});
---
name: Force The Modebar to Always Be Visible
suite: configuration
markdown\_content: |
When users hover over a figure generated with `plotly.js`, a `modebar` appears in the top-right of the figure. This presents users with several options for interacting with the figure.
By default, the `modebar` is only visible while the user is hovering over the chart. If you would like the `modebar` to always be visible regardless of whether or not the user is currently hovering over the figure, set the `displayModeBar` attribute in the `config` of your figure to `true`.
---
var data = [{
y:['Marc', 'Henrietta', 'Jean', 'Claude', 'Jeffrey', 'Jonathan', 'Jennifer', 'Zacharias'],
x: [90, 40, 60, 80, 75, 92, 87, 73],
type: 'bar',
orientation: 'h'}]
var layout = {
title: {
text: 'Always Display the Modebar'
},
showlegend: false
}
Plotly.newPlot('myDiv', data, layout, {displayModeBar: true})
---
name: Editable Mode
suite: configuration
markdown\_content: |
In editable mode, users can edit the chart title, axis labels and trace names in the legend.
---
var trace1 = {
x: [0, 1, 2, 3, 4],
y: [1, 5, 3, 7, 5],
mode: 'lines+markers',
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3, 4, 5],
y: [4, 0, 4, 6, 8],
mode: 'lines+markers',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Click Here
to Edit Chart Title'
}
};
Plotly.newPlot('myDiv', data, layout, {editable: true});
---
name: Never Display The Modebar
suite: configuration
markdown\_content: |
When users hover over a figure generated with `plotly.js`, a `modebar` appears in the top-right of the figure. This presents users with several options for interacting with the figure.
By default, the `modebar` is only visible while the user is hovering over the chart. If you would like the `modebar` to never be visible, then set the `displayModeBar` attribute in the `config` of your figure to `false`.
---
var trace1 = {
x:['Zebras', 'Lions', 'Pelicans'],
y: [90, 40, 60],
type: 'bar',
name: 'New York Zoo'
};
var trace2 = {
x:['Zebras', 'Lions', 'Pelicans'],
y: [10, 80, 45],
type: 'bar',
name: 'San Francisco Zoo'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Hide the Modebar'
},
showlegend: true
};
Plotly.newPlot('myDiv', data, layout, {displayModeBar: false});
---
name: Customize Download Plot Options
suite: configuration
order: 3.1
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6],
y: [1, 9, 4, 7, 5, 2, 4],
mode: 'markers',
marker: {
size: [20, 40, 25, 10, 60, 90, 30],
}
};
var data = [trace1];
var layout = {
title: {
text: 'Download Chart as SVG instead of PNG'
},
showlegend: false
};
var config = {
toImageButtonOptions: {
format: 'svg', // one of png, svg, jpeg, webp
filename: 'custom\_image',
height: 500,
width: 700,
scale: 1 // Multiply title/legend/axis/canvas sizes by this factor
}
};
Plotly.newPlot('myDiv', data, layout, config);
---
name: Remove ModeBar Buttons
suite: configuration
order: 5.5
markdown\_content: |
To delete buttons from the modebar, pass an array of strings containing the names of the buttons you want to remove to the `modeBarButtonsToRemove` attribute in the figure's configuration object. Note that different chart types have different default modebars. The following is a list of all the modebar buttons and the chart types they are associated with:

* -'2D', `zoom2d`, `pan2d`, `select2d`, `lasso2d`, `zoomIn2d`, `zoomOut2d`, `autoScale2d`, `resetScale2d`
* -'3D', `zoom3d`, `pan3d`, `orbitRotation`, `tableRotation`, `handleDrag3d`, `resetCameraDefault3d`, `resetCameraLastSave3d`, `hoverClosest3d`
* -'Cartesian', `hoverClosestCartesian`, `hoverCompareCartesian`
* -'Geo', `zoomInGeo`, `zoomOutGeo`, `resetGeo`, `hoverClosestGeo`
* -'Other', `hoverClosestGl2d`, `hoverClosestPie`, `toggleHover`, `resetViews`, `toImage`, `sendDataToCloud`, `toggleSpikelines`, `resetViewMapbox`

---
var data = [{
x:['trees', 'flowers', 'hedges'],
y: [90, 130, 40],
type: 'bar'}]
var layout = {
title: {
text: 'Remove Modebar Buttons'
},
showlegend: false
}
Plotly.newPlot('myDiv', data, layout, {modeBarButtonsToRemove: ['toImage']})
---
name: Making a Responsive Chart
suite: configuration
order: 10
---
var trace1 = {
type: 'bar',
x: [1, 2, 3, 4],
y: [5, 10, 2, 8],
marker: {
color: '#C8A2C8',
line: {
width: 2.5
}
}
};
var data = [ trace1 ];
var layout = {
title: {
text: 'Responsive to window size!'
},
font: {size: 18}
};
Plotly.newPlot('myDiv', data, layout, {responsive: true});
---
name: Change the Default Locale
suite: configuration
order: 7.5
markdown\_content: |
Load and register a non-default locale by adding ``
to your HTML after the plotly.js tag and then reference the locale in the `config`. For Example, the codepen example below has
`` in its HTML. For more information and a list of available locales, see
[https://github.com/plotly/plotly.js/blob/master/dist/README.md#to-include-localization](https://github.com/plotly/plotly.js/blob/master/dist/README.md#to-include-localization)
---
var trace1 = {
type: "scatter",
mode: "lines",
x: ['2018-01-01', '2018-08-31'],
y: [10, 5],
line: {color: '#17BECF'}
};
var trace2 = {
type: "scatter",
mode: "lines",
x: ['2018-01-01', '2018-08-31'],
y: [3,7],
line: {color: '#7F7F7F'}
};
var data = [trace1,trace2];
var layout = {
title: {
text: 'Custom Locale'
}
};
var config = {locale: 'fr'};
Plotly.newPlot('myDiv', data, layout, config);
---
name: Double Click Delay
suite: configuration
order: 11
markdown\_content: |
Sets the maximum delay between two consecutive clicks to be interpreted as a double-click in ms. This is the time interval between first mousedown, and' second mouseup. The default timing is 300 ms (less than half a second).
This setting propagates to all on-subplot double clicks, (except for geo, map, and mapbox).
---
var data = [{
type: "bar",
y: [3, 5, 3, 2],
x: ["2019-09-02", "2019-10-10", "2019-11-12", "2019-12-22"]
}];
var layout = {xaxis: {type: 'date'}};
var config = {doubleClickDelay: 1000}
Plotly.newPlot("myDiv", data, layout, config)
---
name: Display the `Edit Chart` Link
suite: configuration
markdown\_content: |
Note: `showLink` now defaults to false.
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6],
y: [1, 9, 4, 7, 5, 2, 4],
mode: 'lines+markers',
type: 'scatter'
};
var data = [trace1];
var layout = {
title: {
text: 'Display the Edit Chart Link'
}
};
var config = {
showLink: true,
plotlyServerURL: "https://chart-studio.plotly.com"
};
Plotly.newPlot('myDiv', data, layout, config);
---
name: Scroll and Zoom
suite: configuration
---
// mousewheel or two-finger scroll zooms the plot
var trace1 = {
x:['2020-10-04', '2021-11-04', '2023-12-04'],
y: [90, 40, 60],
type: 'scatter'
};
var data = [trace1];
var layout = {
title: {
text: 'Scroll and Zoom'
},
showlegend: false
};
Plotly.newPlot('myDiv', data, layout, {scrollZoom: true});
---
name: Basic Example
suite: horizontal\_legend
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: 'scatter',
name:'Plot 1'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: 'scatter',
name:'Plot 2'
};
var trace3 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 5, 3, 10, 5.33, 2.24, 4.4, 5.1, 7.2],
type: 'scatter',
name:'Plot 3'
};
var data = [trace1, trace2, trace3];
var layout = {
showlegend: true,
legend: {"orientation": "h"}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based horizontal legend plot in JavaScript.
display\_as: file\_settings
name: Horizontal Legends
order: 16
page\_type: u-guide
permalink: javascript/horizontal-legend/
redirect\_from: javascript-graphing-library/horizontal-legends/
thumbnail: thumbnail/images.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","horizontal\_legend" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Tickmode - Linear (Date)
suite: tick-formatting
---
var x = ['2000-01', '2000-02', '2000-03', '2000-04', '2000-05', '2000-06', '2000-07', '2000-08', '2000-09', '2000-10', '2000-11', '2000-12', '2001-01'];
var y = [-36.5, -26.6, -43.6, -52.3, -71.5, -81.4, -80.5, -82.2, -76, -67.3, -46.1, -35, -40];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
xaxis: {
tickmode: "linear", // If "linear", the placement of the ticks is determined by a starting position `tick0` and a tick step `dtick`
tick0: '1999-12-15',
dtick: 30 \* 24 \* 60 \* 60 \* 1000 // milliseconds
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Using Exponentformat
suite: tick-formatting
order: 3.0
---
var x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
var y = [68000, 52000, 60000, 20000, 95000, 40000, 60000, 79000, 74000, 42000, 20000, 90000];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
yaxis: {
showexponent: 'all',
exponentformat: 'e'
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Using Tickformat (Date)
suite: tick-formatting
order: 2.5
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function (err, rows) {
function unpack(rows, key) {
return rows.map(function (row) {
return row[key];
});
}
var trace1 = {
type: "scatter",
mode: "lines",
name: 'AAPL High',
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.High'),
line: {
color: '#17BECF'
}
}
var trace2 = {
type: "scatter",
mode: "lines",
name: 'AAPL Low',
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.Low'),
line: {
color: '#7F7F7F'
}
}
var data = [trace1, trace2];
var layout = {
title: {text: 'Time series with custom tickformat'},
xaxis: {
tickformat: '%d %B (%a)\n %Y' // For more time formatting types, see: https://github.com/d3/d3-time-format/blob/master/README.md
}
};
Plotly.newPlot('myDiv', data, layout);
})
---
description: How to format axes ticks in D3.js-based JavaScript charts.
display\_as: file\_settings
name: Formatting Ticks
order: 22
page\_type: u-guide
permalink: javascript/tick-formatting/
thumbnail: thumbnail/hover.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","tick-formatting" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Tickmode - Linear
suite: tick-formatting
order: 0.5
---
var x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
var y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
xaxis: {
tickmode: "linear", // If "linear", the placement of the ticks is determined by a starting position `tick0` and a tick step `dtick`
tick0: 0.5,
dtick: 0.75
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Layout Attributes with respect to Formatting Ticks
suite: tick-formatting
---
{
xaxis: {
/\* show/hide tick labels (defaults to true) \*/
showticklabels: boolean,
/\* Set the tick mode for the axis "auto" or "linear" or "array" \*/
tickmode: 'auto',
/\* Set the placement of the first tick\*/
tick0: '',
/\* Set the step in-between ticks\*/
dtick: '',
/\* Specifies the maximum number of ticks \*/
nticks: 0,
/\* Set the values at which ticks on this axis appear \*/
tickvals: [ /\* \*/ ],
/\* Set the text displayed at the ticks position via tickvals \*/
ticktext: [ /\* \*/ ],
/\* Set the source reference for tickvals \*/
tickvalssrc: '',
/\* Set the source reference for ticktext \*/
tickvtextsrc: '',
/\* Set the tick label formatting rule using d3 formatting mini-languages \*/
tickformat: '',
/\* Set the tickformat per zoom level \*/
tickformatstops: {
enabled: true,
/\* Set the range of the dtick values which describe the zoom level, it is possible to omit "min" or "max" value by passing "null" \*/
dtickrange: ["min", "max"],
/\* dtickformat for described zoom level, the same as "tickformat" \*/
value: string,
},
/\* Set the ticks to display with a prefix: "all" or "first" or "last" or "none" \*/
showtickprefix: 'all',
tickprefix: string,
/\* Set the ticks to display with a suffix: "all" or "first" or "last" or "none" \*/
showticksuffix: 'all',
ticksuffix: string,
/\* Determines a formatting rule for the tick exponents: "none" or "e" or "E" or "power" or "SI" or "B" \*/
exponentformat: 'B',
}
/\* similarly for yaxis \*/
}
---
name: Using Tickformat
suite: tick-formatting
order: 2.0
---
var x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
var y = [0.18, 0.38, 0.56, 0.46, 0.59, 0.4, 0.78, 0.77, 0.74, 0.42, 0.45, 0.39];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
yaxis: {
tickformat: '%' // For more formatting types, see: https://github.com/d3/d3-format/blob/master/README.md#locale\_format
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Tickmode - Array
suite: tick-formatting
order: 1.5
---
var x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];
var y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
xaxis: {
tickmode: "array", // If "array", the placement of the ticks is set via `tickvals` and the tick text is `ticktext`.
tickvals: [1, 3, 5, 7, 9, 11],
ticktext: ['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Include Locale Config
suite: tick-formatting
order: 4.0
---
var x = ['2013-02-04', '2013-04-05', '2013-06-06', '2013-08-07', '2013-10-02'];
var y = [1, 4, 3, 6, 2];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
xaxis: {
tickformat: '%a %e %b \n %Y'
}
}
Plotly.newPlot('myDiv', data, layout, {
locale: 'fr' // For more info, see: https://github.com/plotly/plotly.js/blob/master/dist/README.md#to-include-localization and https://github.com/plotly/plotly.js/tree/master/dist
});
---
name: Tickformatstops to customize for different zoom levels
suite: tick-formatting
order: 2.75
---
var gd = document.getElementById('myDiv');
var x = ["2005-01", "2005-02", "2005-03", "2005-04", "2005-05", "2005-06", "2005-07"];
var y = [-20, 10, -5, 0, 5, -10, 20];
var data = [{
x: x,
y: y,
type: 'scatter'
}];
var layout = {
xaxis: {
tickformatstops: [{
"dtickrange": [null, 1000],
"value": "%H:%M:%S.%L ms"
},
{
"dtickrange": [1000, 60000],
"value": "%H:%M:%S s"
},
{
"dtickrange": [60000, 3600000],
"value": "%H:%M m"
},
{
"dtickrange": [3600000, 86400000],
"value": "%H:%M h"
},
{
"dtickrange": [86400000, 604800000],
"value": "%e. %b d"
},
{
"dtickrange": [604800000, "M1"],
"value": "%e. %b w"
},
{
"dtickrange": ["M1", "M12"],
"value": "%b '%y M"
},
{
"dtickrange": ["M12", null],
"value": "%Y Y"
}
]
}
};
Plotly.newPlot("myDiv", data, layout);
---
permalink: javascript/plotly-fundamentals/
redirect\_from: javascript/modularizing-monolithic-javascript-projects/
description: Plotly.js makes interactive, publication-quality graphs online. Tutorials and tips about fundamental features of Plotly JS
name: Fundamentals
layout: langindex
display\_as: file\_settings
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Fundamentals

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","file\_settings" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
markdown\_content: 'Adding a `uirevision` attribute and then keeping it the same during
the next call to Plotly.react ensures that user
interactions persist.
'
name: Persist User Changes
suite: uirevision
---
const rand = () => Math.random();
var x = [1, 2, 3, 4, 5];
const new\_data = (trace) => Object.assign(trace, {y: x.map(rand)});
// add random data to three line traces
var data = [
{mode:'lines', line: {color: "#b55400"}},
{mode: 'lines', line: {color: "#393e46"}},
{mode: 'lines', line: {color: "#222831"}}
].map(new\_data);
var layout = {
title: {text: 'User Zoom Persists
When uirevision Unchanged'},
uirevision:'true',
xaxis: {autorange: true},
yaxis: {autorange: true}
};
Plotly.react('myDiv', data, layout);
var myPlot = document.getElementById('myDiv');
var cnt = 0;
var interval = setInterval(function() {
data = data.map(new\_data);
// user interaction will mutate layout and set autorange to false
// so we need to reset it to true
layout.xaxis.autorange = true;
layout.yaxis.autorange = true;
// not changing uirevision will ensure that user interactions are unchanged
// layout.uirevision = rand();
Plotly.react('myDiv', data, layout);
if(cnt === 100) clearInterval(interval);
}, 2500);
---
description: Persist user interactions using uirevision with Plotly.react or Dash.
display\_as: file\_settings
name: uirevision in Plotly.react
page\_type: example\_index
permalink: javascript/uirevision/
thumbnail: thumbnail/uirevision.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","uirevision" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
markdown\_content: 'Changing the `uirevision` attribute during a Plotly.react call
will reset previous user interactions in the updated plot.
'
name: Reset User Changes
suite: uirevision
---
const rand = () => Math.random();
var x = [1, 2, 3, 4, 5];
const new\_data = (trace) => Object.assign(trace, {y: x.map(rand)});
// add random data to three line traces
var data = [
{mode:'lines', line: {color: "#b55400"}},
{mode: 'lines', line: {color: "#393e46"}},
{mode: 'lines', line: {color: "#222831"}}
].map(new\_data);
var layout = {
title: {text: 'User Zoom Resets
When uirevision Changes'},
uirevision:'true',
xaxis: {autorange: true},
yaxis: {autorange: true}
};
Plotly.react('myDiv', data, layout);
var myPlot = document.getElementById('myDiv');
var cnt = 0;
var interval = setInterval(function() {
data = data.map(new\_data);
// user interaction will mutate layout and set autorange to false
// so we need to reset it to true
layout.xaxis.autorange = true;
layout.yaxis.autorange = true;
// a new random number should ensure that uirevision will be different
// and so the graph will autorange after the Plotly.react
layout.uirevision = rand();
Plotly.react('myDiv', data, layout);
if(cnt === 100) clearInterval(interval);
}, 2500);
---
description: How to modify the legend in D3.js-based javascript graphs. Seven examples
of how to move, color, and hide the legend.
display\_as: file\_settings
name: Legends
order: 20
page\_type: u-guide
permalink: javascript/legend/
redirect\_from: javascript-graphing-library/legend/
thumbnail: thumbnail/legends.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","legends" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Legend Names
suite: legends
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
name: 'Blue Trace',
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
name: 'Orange Trace',
type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
name: Positioning the Legend Inside the Plot
suite: legends
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
showlegend: true,
legend: {
x: 1,
xanchor: 'right',
y: 1
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Changing the orientation of Legend
suite: legends
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {showlegend: true,
legend: {"orientation": "h"}};
Plotly.newPlot('myDiv', data, layout);
---
name: Grouped Legend
suite: legends
order: 10
---
var trace1 = {
x: [1, 2, 3],
y: [2, 1, 3],
legendgroup: 'group',
marker: {color: 'rgb(164, 194, 244)'},
mode: 'markers',
name: 'first legend group',
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3],
y: [2, 2, 2],
legendgroup: 'group',
line: {color: 'rgb(164, 194, 244)'},
mode: 'lines',
name: 'first legend group - average',
type: 'scatter'
};
var trace3 = {
x: [1, 2, 3],
y: [4, 9, 2],
legendgroup: 'group2',
marker: {color: 'rgb(142, 124, 195)'},
mode: 'markers',
name: 'second legend group',
type: 'scatter'
};
var trace4 = {
x: [1, 2, 3],
y: [5, 5, 5],
legendgroup: 'group2',
line: {color: 'rgb(142, 124, 195)'},
mode: 'lines',
name: 'second legend group - average',
type: 'scatter'
};
data = [trace1, trace2, trace3, trace4];
Plotly.newPlot('myDiv', data);
---
name: Subplot Grouped Legend
suite: legends
order: 11
---
var trace1 = {
x: ['a'],
y: [2],
legendgroup: 'a',
marker: {
color: 'rgba(102,194,165,1)',
line: {color: 'transparent'}
},
name: 'a',
type: 'bar',
xaxis: 'x',
yaxis: 'y'
};
var trace2 = {
x: ['b'],
y: [3],
legendgroup: 'b',
marker: {
color: 'rgba(252,141,98,1)',
line: {color: 'transparent'}
},
name: 'b',
type: 'bar',
xaxis: 'x',
yaxis: 'y'
};
var trace3 = {
x: ['c'],
y: [2],
legendgroup: 'c',
marker: {
color: 'rgba(141,160,203,1)',
line: {color: 'transparent'}
},
name: 'c',
type: 'bar',
xaxis: 'x',
yaxis: 'y'
};
var trace4 = {
x: ['a'],
y: [4],
legendgroup: 'a',
marker: {
color: 'rgba(102,194,165,1)',
line: {color: 'transparent'}
},
name: 'a',
showlegend: false,
type: 'bar',
xaxis: 'x2',
yaxis: 'y2'
};
var trace5 = {
x: ['b'],
y: [2],
legendgroup: 'b',
marker: {
color: 'rgba(252,141,98,1)',
line: {color: 'transparent'}
},
name: 'b',
showlegend: false,
type: 'bar',
xaxis: 'x2',
yaxis: 'y2'
};
var trace6 = {
x: ['c'],
y: [4],
legendgroup: 'c',
marker: {
color: 'rgba(141,160,203,1)',
line: {color: 'transparent'}
},
name: 'c',
showlegend: false,
type: 'bar',
xaxis: 'x2',
yaxis: 'y2'
};
var data = [trace1, trace2, trace3, trace4, trace5, trace6];
var layout = {
hovermode: 'closest',
margin: {
r: 10,
t: 25,
b: 40,
l: 60
},
showlegend: true,
xaxis: {
anchor: 'y',
categoryorder: 'array',
domain: [0, 1],
type: 'category',
showgrid: false,
showticklabels: false
},
xaxis2: {
anchor: 'y2',
categoryorder: 'array',
domain: [0, 1],
type: 'category',
showgrid: false
},
yaxis: {
anchor: 'x',
domain: [0.52, 1],
showgrid: false
},
yaxis2: {
anchor: 'x2',
domain: [0, 0.48],
showgrid: false
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Hiding the Legend
suite: legends
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {showlegend: false};
Plotly.newPlot('myDiv', data, layout);
---
name: Hiding Legend Entries
suite: legends
---
var trace1 = {
x: [0, 1, 2],
y: [1, 2, 3],
name: 'First Trace',
showlegend: false,
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3],
y: [8, 4, 2, 0],
name: 'Second Trace',
showlegend: true,
type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
name: Styling and Coloring the Legend
suite: legends
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {legend: {
x: 0,
y: 1,
traceorder: 'normal',
font: {
family: 'sans-serif',
size: 12,
color: '#000'
},
bgcolor: '#E2E2E2',
bordercolor: '#FFFFFF',
borderwidth: 2
}};
Plotly.newPlot('myDiv', data, layout);
---
name: Positioning the Legend Outside the Plot
suite: legends
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 3, 6, 4, 5, 2, 3, 5, 4],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 7, 8, 3, 6, 3, 3, 4],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
showlegend: true,
legend: {
x: 1,
y: 0.5
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Picnic Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Picnic',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'Picnic'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Earth Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Earth',
type: 'heatmap'
}];
Plotly.newPlot('myDiv', data);
});
---
name: Blackbody Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Blackbody',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'Blackbody'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Colorscale for Contour Plot
suite: colorscales
order: 20
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: 'Jet'
}
];
var layout = {
title: {
text: 'Colorscale for Contour Plot'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Greens Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Greens',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'Greens'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Bluered Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Bluered',
type: 'heatmap'
}];
Plotly.newPlot('myDiv', data);
});
---
description: How to set colorscales and heatmap colorscales in D3.js-based JavaScript
charts in Plotly.js. Divergent, sequential, and qualitative colorscales.
display\_as: file\_settings
name: Colorscales
page\_type: u-guide
permalink: javascript/colorscales/
redirect\_from: javascript-graphing-library/heatmap-and-contour-colorscales/
thumbnail: thumbnail/heatmap\_colorscale.jpg
---
{% assign examples = site.posts | where:'language','plotly\_js' | where:'suite','colorscales' | sort: 'order' %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Portland Heatmap
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Portland',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'Portland'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Electric Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Electric',
type: 'heatmap'
}];
Plotly.newPlot('myDiv', data);
});
---
name: Hot Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Hot',
type: 'heatmap'
}];
Plotly.newPlot('myDiv', data);
});
---
name: Jet Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Jet',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'Jet'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Custom Colorscale for Contour Plot
suite: colorscales
order: 21
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: [[0, 'rgb(166,206,227)'], [0.25, 'rgb(31,120,180)'], [0.45, 'rgb(178,223,138)'], [0.65, 'rgb(51,160,44)'], [0.85, 'rgb(251,154,153)'], [1, 'rgb(227,26,28)']]
}
];
var layout = {
title: {
text: 'Custom Contour Plot Colorscale'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Greys Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'Greys',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'Greys'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Custom Discretized Heatmap Colorscale
suite: colorscales
order: 22
---
var data = [
{
z: [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]],
colorscale: [
// Let first 10% (0.1) of the values have color rgb(0, 0, 0)
[0, 'rgb(0, 0, 0)'],
[0.1, 'rgb(0, 0, 0)'],
// Let values between 10-20% of the min and max of z
// have color rgb(20, 20, 20)
[0.1, 'rgb(20, 20, 20)'],
[0.2, 'rgb(20, 20, 20)'],
// Values between 20-30% of the min and max of z
//have color rgb(40, 40, 40)
[0.2, 'rgb(40, 40, 40)'],
[0.3, 'rgb(40, 40, 40)'],
[0.3, 'rgb(60, 60, 60)'],
[0.4, 'rgb(60, 60, 60)'],
[0.4, 'rgb(80, 80, 80)'],
[0.5, 'rgb(80, 80, 80)'],
[0.5, 'rgb(100, 100, 100)'],
[0.6, 'rgb(100, 100, 100)'],
[0.6, 'rgb(120, 120, 120)'],
[0.7, 'rgb(120, 120, 120)'],
[0.7, 'rgb(140, 140, 140)'],
[0.8, 'rgb(140, 140, 140)'],
[0.8, 'rgb(160, 160, 160)'],
[0.9, 'rgb(160, 160, 160)'],
[0.9, 'rgb(180, 180, 180)'],
[1.0, 'rgb(180, 180, 180)']
],
type: 'heatmap',
colorbar:{
tickmode: 'linear',
tick0: 0,
dtick: 1
}
}
];
var layout = {
title: {
text: 'CUSTOM DISCRETIZED HEATMAP COLORSCALE'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: RdBu Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'RdBu',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'RdBu'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Custom Colorscale
suite: colorscales
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: [
['0.0', 'rgb(165,0,38)'],
['0.111111111111', 'rgb(215,48,39)'],
['0.222222222222', 'rgb(244,109,67)'],
['0.333333333333', 'rgb(253,174,97)'],
['0.444444444444', 'rgb(254,224,144)'],
['0.555555555556', 'rgb(224,243,248)'],
['0.666666666667', 'rgb(171,217,233)'],
['0.777777777778', 'rgb(116,173,209)'],
['0.888888888889', 'rgb(69,117,180)'],
['1.0', 'rgb(49,54,149)']
],
type: 'heatmap'
}];
Plotly.newPlot('myDiv', data);
});
---
name: YlGnBu Colorscale
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'YlGnBu',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'YlGnBu'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: YlOrRd Heatmap
suite: colorscales
order: 16
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/custom\_heatmap\_colorscale.json', function(figure) {
var data = [{
z: figure.z,
colorscale: 'YlOrRd',
type: 'heatmap'
}
];
var layout = {
title: {
text: 'YlOrRd'
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Installation
suite: react
---
$ npm install react-plotly.js plotly.js
---
name: Quick Start
suite: react
markdown\_content: |
The easiest way to use this component is to import and pass data to a plot component:
---
import React from 'react';
import Plot from 'react-plotly.js';
class App extends React.Component {
render() {
return (
);
}
}
---
name: Advanced Usage
suite: react
markdown\_content: |
For information on more advanced usage patterns such as [State Management](https://github.com/plotly/react-plotly.js#state-management) or [Customizing the plotly.js bundle](https://github.com/plotly/react-plotly.js#customizing-the-plotlyjs-bundle) please see the [ReadMe for react-plotly.js](https://github.com/plotly/react-plotly.js/blob/master/README.md).
---
---
name: Plotly.js Chart Types and Attributes
suite: react
markdown\_content: |
Click here for more information about [Plotly Chart Types](https://plotly.com/javascript/) and [Attributes](https://plotly.com/javascript/reference/).
---
---
description: How to use the Plotly.js React component.
display\_as: file\_settings
name: React Plotly.js
page\_type: example\_index
permalink: javascript/react/
thumbnail: thumbnail/react.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","react" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Introduction
suite: react
markdown\_content: |
Use [react-plotly.js](https://github.com/plotly/react-plotly.js) to embed D3 charts in your [React](https://reactjs.org/)-powered web application. This React component takes the chart type, data, and styling as [Plotly JSON](https://help.plot.ly/json-chart-schema/) in its data and layout props, then draws the chart using Plotly.js. See below about how to get started with react-plotly.js.
---
---
name: Props and Events
suite: react
markdown\_content: |
More information about [Props](https://github.com/plotly/react-plotly.js/#basic-props) and [Event Handlers](https://github.com/plotly/react-plotly.js/#event-handler-props) can be found in the [ReadMe for react-plotly.js](https://github.com/plotly/react-plotly.js/blob/master/README.md).
---
---
name: Styling Names
suite: labels
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
name: 'Name of Trace 1',
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [1, 0, 3, 2, 5, 4, 7, 6, 8],
name: 'Name of Trace 2',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
title: {
text:'Plot Title',
font: {
family: 'Courier New, monospace',
size: 24
},
xref: 'paper',
x: 0.05,
},
xaxis: {
title: {
text: 'x Axis',
font: {
family: 'Courier New, monospace',
size: 18,
color: '#7f7f7f'
}
},
},
yaxis: {
title: {
text: 'y Axis',
font: {
family: 'Courier New, monospace',
size: 18,
color: '#7f7f7f'
}
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Setting Title Automargin
suite: labels
markdown\_content: |
Set `automargin` to `true` to allow the title to push the figure margins.
With `yref` set to `paper`, `automargin` expands the margins to make the title visible,
but doesn't push outside the container. With `yref` set to `container`, `automargin`
expands the margins, but doesn't overlap with the plot area, tick labels, and axis titles.
---
var trace1 = {
x: [1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007],
y: [69.39,
70.26,
71.24,
71.52,
71.89,
72.22,
73.84,
74.32,
76.33,
77.55,
79.11,
80.204
],
type: 'scatter'
};
var trace2 = {
x: [1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007],
y: [69.12,
70.33,
70.93,
71.1,
71.93,
73.49,
74.74,
76.32,
77.56,
78.83,
80.37,
81.235
],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Population',
font: {
family: 'Courier New, monospace',
size: 70
},
yref: 'paper',
automargin: true,
},
showlegend: false
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to set the title, legend-entries, and axis-titles in javascript D3.js-based
charts.
display\_as: file\_settings
name: Setting the Title, Legend Entries, and Axis Titles
order: 18
page\_type: u-guide
permalink: javascript/figure-labels/
redirect\_from: javascript-graphing-library/figure-labels/
thumbnail: thumbnail/figure-labels.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","labels" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
description: How to add LaTeX to javascript D3.js-based graphs.
display\_as: file\_settings
name: LaTeX
order: 10
page\_type: u-guide
permalink: javascript/LaTeX/
redirect\_from: javascript-graphing-library/LaTeX/
thumbnail: thumbnail/venn.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","latex" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: LaTeX Typesetting
suite: latex
---
// remember to load MathJax.js?config=TeX-MML-AM\_CHTML
var trace1 = {
x: [1, 2, 3, 4],
y: [1, 4, 9, 16],
name: '$\\alpha\_{1c} = 352 \\pm 11 \\text{ km s}^{-1}$',
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3, 4],
y: [0.5, 2, 4.5, 8],
name: '$\\beta\_{1c} = 25 \\pm 11 \\text{ km s}^{-1}$',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {
title: {
text: '$\\sqrt{(n\_\\text{c}(t|{T\_\\text{early}}))}$'
}
},
yaxis: {
title: {
text: '$d, r \\text{ (solar radius)}$'
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Adding Hover Text to Data in Line and Scatter Plots
suite: hover
---
var data = [
{
x: [0, .5, 1, 1.5, 2],
y: [1, 3, 2, 4, 2],
mode: 'markers',
marker: {size:16},
text: ['Text A', 'Text B', 'Text C', 'Text D', 'Text E'],
type: 'scatter'
}
];
var layout = {
title: {
text: 'Hover over the points to see the text'
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to add hover text and format hover values in D3.js-based javascript
charts.
display\_as: file\_settings
name: Hover Text and Formatting
order: 17
page\_type: u-guide
permalink: javascript/hover-text-and-formatting/
redirect\_from: javascript-graphing-library/hover-text-and-formatting/
thumbnail: thumbnail/hover-text.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","hover" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Rounding X and Y Hover Values
suite: hover
---
// Round x and y hover values by setting hoverformat in layout.xaxis and/or layout.yaxis
// using D3 number formatting ( https://github.com/mbostock/d3/wiki/Formatting )
var N = 40,
x = d3.range(N).map( d3.random.normal() ),
y1 = d3.range(N).map( d3.random.normal() ),
y2 = d3.range(N).map( d3.random.normal() ),
data = [{ x:x, y:y1, type:'scatter', mode:'markers',
marker:{color:'rgba(200, 50, 100, .7)', size:16},
hoverinfo:"x+y"
},
{ x:x, y:y2, type:'scatter', mode:'markers',
marker:{color:'rgba(10, 180, 180, .8)', size:16},
hoverinfo:"x+y"}];
layout = {
hovermode: 'closest',
title: {
text: 'Formatting X & Y Hover Values'
},
xaxis: {
zeroline: false,
hoverformat: '.2f',
title: {
text: 'Rounded: 2 values after the decimal point on hover'
}
},
yaxis: {
zeroline: false,
hoverformat: '.2r',
title: {
text: 'Rounded: 2 significant values on hover'
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Roughness
suite: 3d-surface-lighting
---
d3.csv('https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/sin\_saddle.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data = [];
for(i=0;i<100;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface',
colorscale:'Viridis',
lighting: {roughness: 0.9}
},
{
z: z\_data,
type: 'surface',
scene: 'scene2',
colorscale:'Viridis',
lighting: {roughness: 0.2}
}
];
var layout = {
title: {
text: 'Roughness'
},
grid: {
rows: 1,
columns: 2,
pattern: 'independent',
},
scene:{
aspectmode:'cube',
domain:{row:0, column:0}
},
scene2:{
aspectmode:'cube',
domain:{row:0, column:1}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to customize lighting for 3D surface charts.
display\_as: file\_settings
name: 3D Surface Lighting
order: 14
page\_type: u-guide
permalink: javascript/3d-surface-lighting/
thumbnail: thumbnail/3d-surface.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-surface-lighting" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Fresnel
suite: 3d-surface-lighting
---
d3.csv('https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/sin\_saddle.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data = [];
for(i=0;i<100;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface',
colorscale:'Viridis',
lighting: {fresnel: 0.1}
},
{
z: z\_data,
type: 'surface',
scene: 'scene2',
colorscale:'Viridis',
lighting: {fresnel: 5}
}
];
var layout = {
title: {
text: 'Fresnel'
},
grid: {
rows: 1,
columns: 2,
pattern: 'independent',
},
scene:{
aspectmode:'cube',
domain:{row:0, column:0}
},
scene2:{
aspectmode:'cube',
domain:{row:0, column:1}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Ambient Lighting
suite: 3d-surface-lighting
---
d3.csv('https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/sin\_saddle.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data = [ ];
for(i=0;i<100;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface',
colorscale: 'Viridis',
lighting: {ambient: 0.9}
},
{
z: z\_data,
type: 'surface',
scene: 'scene2',
colorscale:'Viridis',
lighting: {ambient: 0.2}
}
];
var layout = {
title: {
text: 'Ambient Lighting'
},
grid: {
rows: 1,
columns: 2,
pattern: 'independent',
},
scene:{
aspectmode:'cube',
domain:{row:0, column:0}
},
scene2:{
aspectmode:'cube',
domain:{row:0, column:1}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Specular
suite: 3d-surface-lighting
---
d3.csv('https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/sin\_saddle.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data = [];
for(i=0;i<100;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface',
colorscale:'Viridis',
lighting: {specular: 0.1}
},
{
z: z\_data,
type: 'surface',
scene: 'scene2',
colorscale:'Viridis',
lighting: {specular: 2}
}
];
var layout = {
title: {
text: 'Specular Reflection'
},
grid: {
rows: 1,
columns: 2,
pattern: 'independent',
},
scene:{
aspectmode:'cube',
domain:{row:0, column:0}
},
scene2:{
aspectmode:'cube',
domain:{row:0, column:1}
},
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Reference
suite: 3d-surface-lighting
order: 10
markdown\_content: |
See [https://plotly.com/javascript/reference/surface/#surface-lighting](https://plotly.com/javascript/reference/surface/#surface-lighting) for more information!
---
---
name: Diffuse
suite: 3d-surface-lighting
---
d3.csv('https://raw.githubusercontent.com/michaelbabyn/plot\_data/master/sin\_saddle.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data = []
for(i=0;i<100;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface',
colorscale:'Viridis',
lighting: {diffuse: 0.9}
},
{
z: z\_data,
type: 'surface',
scene: 'scene2',
colorscale:'Viridis',
lighting: {diffuse: 0.1}
}
];
var layout = {
title: {
text: 'Diffuse Reflection'
},
grid: {
rows: 1,
columns: 2,
pattern: 'independent',
},
scene:{
aspectmode:'cube',
domain:{row:0, column:0}
},
scene2:{
aspectmode:'cube',
domain:{row:0, column:1}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Plotly.js
permalink: javascript/eula/
description: End User License Agreement for Plotly.js and other Plotly products
layout: langindex
redirect\_from: javascript-graphing-library/eula/
---

## Plotly EULA

Please read the full Plotly.js [End User License Agreement](http://bit.ly/1HWyooe) before using, downloading, or purchasing the software.

##### Free use of  "Basic Charts"

* The Plotly.js Basic Charts module is free for unlimited use if all links and references to Plotly remain visible and unmodified.
* All Restricted and Permitted Uses below and the full EULA apply.

##### Permitted Uses

* Plotly.js can be used with an unlimited number of SaaS projects, web applications, intranets, and websites.
* Each person who directly or indirectly creates an application or user interface containing Plotly.js is considered a developer.
* Source editing is allowed

##### Restricted Uses

* Plotly.js distribution with your desktop software or hardware requires an OEM license. Please contact sales@plot.ly
* Plotly.js use with IPython notebook, RStudio, MATLAB, or another desktop analytics IDE requires a Plotly Desktop license.
* Plotly.js integration with Spotfire, Cognos, Qlikview, or Tableau products requires an additional support plan and license for viewers. Please contact sales@plot.ly

{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","Plotly.js" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Reversed Axes
suite: axes
---
var data = [
{
x: [1, 2],
y: [1, 2],
type: 'scatter'
}
];
var layout = {xaxis: {autorange: 'reversed'}};
Plotly.newPlot('myDiv', data, layout);
---
name: Fixed-Ratio Axes
suite: axes
---
var trace0 = {
x: [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
y: [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
}
var trace1 = {
x: [0,1,2,3],
y: [1,2,4,8],
yaxis:"y2"
}
var trace2 = {
x: [1,10,100,10,1],
y: [0,1,2,3,4],
xaxis: "x2",
yaxis:"y3",
}
var trace3 = {
x: [1,100,30,80,1],
y: [1,1.5,2,2.5,3],
xaxis:"x2",
yaxis:"y4"
}
var data = [trace0,trace1,trace2,trace3]
var layout = {
width: 800,
height: 500,
title: {
text: "fixed-ratio axes"
},
xaxis: {
nticks: 10,
domain: [0, 0.45],
title: {
text: "shared X axis"
}
},
yaxis: {
scaleanchor: "x",
domain: [0, 0.45],
title: {
text: "1:1"
}
},
yaxis2: {
scaleanchor: "x",
scaleratio: 0.2,
domain: [0.55, 1],
title: {
text: "1:5"
}
},
xaxis2: {
type: "log",
domain: [0.55, 1],
anchor: "y3",
title: {
text: "unconstrained log X"
}
},
yaxis3: {
domain: [0, 0.45],
anchor: "x2",
title: {
text: "Scale matches ->"
}
},
yaxis4: {
scaleanchor: "y3",
domain: [0.55, 1],
anchor: "x2",
title: {
text: "Scale matches <-"
}
},
showlegend: false
}
Plotly.newPlot('myDiv', data, layout)
---
name: Reversed Axes with Range ( Min/Max ) Specified
suite: axes
---
var data = [
{
x: [0.0, 0.1, 0.2, 0.3, 0.4, 0.51, 0.61, 0.71, 0.81, 0.91, 1.01, 1.11, 1.21, 1.31, 1.41, 1.52, 1.62, 1.72, 1.82, 1.92, 2.02, 2.12, 2.22, 2.32, 2.42, 2.53, 2.63, 2.73, 2.83, 2.93, 3.03, 3.13, 3.23, 3.33, 3.43, 3.54, 3.64, 3.74, 3.84, 3.94, 4.04, 4.14, 4.24, 4.34, 4.44, 4.55, 4.65, 4.75, 4.85, 4.95, 5.05, 5.15, 5.25, 5.35, 5.45, 5.56, 5.66, 5.76, 5.86, 5.96, 6.06, 6.16, 6.26, 6.36, 6.46, 6.57, 6.67, 6.77, 6.87, 6.97, 7.07, 7.17, 7.27, 7.37, 7.47, 7.58, 7.68, 7.78, 7.88, 7.98, 8.08, 8.18, 8.28, 8.38, 8.48, 8.59, 8.69, 8.79, 8.89, 8.99, 9.09, 9.19, 9.29, 9.39, 9.49, 9.6, 9.7, 9.8, 9.9, 10.0],
y: [63, 65, 78, 92, 12, 50, 17, 31, 1, 25, 76, 66, 83, 38, 95, 23, 20, 88, 31, 26, 39, 74, 11, 84, 7, 13, 30, 85, 80, 47, 12, 89, 12, 35, 99, 78, 77, 56, 26, 13, 96, 55, 19, 88, 31, 1, 42, 39, 99, 62, 68, 61, 45, 44, 10, 25, 89, 82, 28, 2, 24, 1, 32, 16, 29, 40, 55, 75, 20, 41, 67, 33, 92, 14, 16, 22, 86, 55, 37, 42, 42, 85, 60, 11, 54, 3, 34, 29, 59, 28, 25, 67, 90, 10, 29, 16, 51, 17, 2, 34],
mode: "markers"
}
];
var layout = {
title: {
text: "Reversed Axis with Min/Max"
},
xaxis: {
range: [10, 0]
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Styling and Coloring Axes and the Zero-Line
suite: axes
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {
showgrid: true,
zeroline: true,
showline: true,
mirror: 'ticks',
gridcolor: '#bdbdbd',
gridwidth: 2,
zerolinecolor: '#969696',
zerolinewidth: 4,
linecolor: '#636363',
linewidth: 6
},
yaxis: {
showgrid: true,
zeroline: true,
showline: true,
mirror: 'ticks',
gridcolor: '#bdbdbd',
gridwidth: 2,
zerolinecolor: '#969696',
zerolinewidth: 4,
linecolor: '#636363',
linewidth: 6
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Setting the Range of Axes Manually
suite: axes
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {range: [2, 5]},
yaxis: {range: [2, 5]}
};
Plotly.newPlot('myDiv', data, layout);
---
name: `nonnegative`, `tozero`, and `normal` Rangemode
suite: axes
---
var data = [
{
x: [2, 4, 6],
y: [-3, 0, 3],
type: 'scatter'
}
];
var layout = {
showlegend: false,
xaxis: {
rangemode: 'tozero',
autorange: true
},
yaxis: {
rangemode: 'nonnegative',
autorange: true
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Categorical Axes
suite: axes
---
var trace1 = {
x: ['A12', 'BC2', 109, '12F', 215, 304],
y: [1, 6, 3, 5, 1, 4],
mode: 'markers',
type: 'bar',
name: 'Team A',
text: ['Apples', 'Pears', 'Peaches', 'Bananas', 'Pineapples', 'Cherries'],
};
var data = [ trace1 ];
var layout = {
xaxis: {
type: 'category',
title: {
text: 'Product Code'
}
},
yaxis: {
range: [0, 7],
title: {
text: 'Number of Items in Stock'
}
},
title: {text: 'Inventory'}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Specifying Label Aliases
suite: axes
order: 10
markdown\_content: |
This example uses `labelalias` to update the text displayed for the x-axis values.
---
var trace1 = {
x: ['UK', 'US', 'Germany', 'France'],
y: [8, 3, 10, 3],
type: 'bar',
};
var data = [trace1];
var layout = {
xaxis: {
labelalias: {
UK: '🇬🇧 United Kingdom',
US: '🇺🇸 United States',
Germany: '🇩🇪 Germany',
France: '🇫🇷 France'}
},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Set Axis Title Position
suite: axes
order: 3.5
markdown\_content: |
This example sets `standoff` attribute to cartesian axes to determine the distance between the tick labels and the axis title.
Note that the axis title position is always constrained within the margins, so the actual standoff distance is always less than the set or default value.
By setting standoff and turning [automargin](https://plotly.com/javascript/setting-graph-size/#automatically-adjust-margins) on, plotly.js will push the margins to fit the axis title at given standoff distance.
---
var data = [{
mode: "lines+markers",
x:["December", "January", "February"],
y:[4,1,3]
}]
var layout = {
margin: {t:0,r:0,b:0,l:20},
xaxis: {
automargin: true,
tickangle: 90,
title: {
text: "Month",
standoff: 20
}},
yaxis: {
automargin: true,
tickangle: 90,
title: {
text: "Temperature",
standoff: 40
}}}
Plotly.newPlot('myDiv', data, layout)
---
name: Multi-Category Axes
suite: axes
order: 7.4
---
var trace1 = {
x: [
['SF Zoo','SF Zoo','SF Zoo'],
['giraffes', 'orangutans', 'monkeys']
],
y: [20, 14, 23],
name: 'SF Zoo',
type: 'bar'
};
var trace2 = {
x: [
['LA Zoo','LA Zoo','LA Zoo'],
['giraffes', 'orangutans', 'monkeys']
],
y: [12, 18, 29],
name: 'LA Zoo',
type: 'bar'
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
xaxis: {
tickson: "boundaries",
ticklen: 15,
showdividers: true,
dividercolor: 'grey',
dividerwidth: 2
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Toggling Axes Lines, Ticks, Labels, and Autorange
suite: axes
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {
autorange: true,
showgrid: false,
zeroline: false,
showline: false,
autotick: true,
ticks: '',
showticklabels: false
},
yaxis: {
autorange: true,
showgrid: false,
zeroline: false,
showline: false,
autotick: true,
ticks: '',
showticklabels: false
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Set and Style Axes Title Labels and Ticks
suite: axes
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var x = unpack(rows, 'Date')
var y = unpack(rows, 'AAPL.Volume')
var trace = {
type: "scatter",
mode: "lines",
name: 'AAPL Volume',
x: x,
y: y,
line: {color: 'grey'}
}
var data = [trace];
var layout = {
title: {text: 'Volume of Apple Shares Traded'},
xaxis: {
title: {
text: 'AXIS TITLE',
font: {
family: 'Arial, sans-serif',
size: 18,
color: 'lightgrey'
}
},
showticklabels: true,
tickangle: 'auto',
tickfont: {
family: 'Old Standard TT, serif',
size: 14,
color: 'black'
},
exponentformat: 'e',
showexponent: 'all'
},
yaxis: {
title: {
text: 'AXIS TITLE',
font: {
family: 'Arial, sans-serif',
size: 18,
color: 'lightgrey'
}
},
showticklabels: true,
tickangle: 45,
tickfont: {
family: 'Old Standard TT, serif',
size: 14,
color: 'black'
},
exponentformat: 'e',
showexponent: 'all'
}
};
Plotly.newPlot('myDiv', data, layout);
})
---
description: How to adjust axes properties in D3.js-based javascript charts. Seven
examples of linear and logarithmic axes, axes titles, and styling and coloring axes
and grid lines.
display\_as: file\_settings
name: Axes
order: 15
page\_type: u-guide
permalink: javascript/axes/
redirect\_from: javascript-graphing-library/axes/
thumbnail: thumbnail/axes.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","axes" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Tick Placement, Color, and Style
suite: axes
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {
tickmode: 'linear',
ticks: 'outside',
tick0: 0,
dtick: 0.25,
ticklen: 8,
tickwidth: 4,
tickcolor: '#000'
},
yaxis: {
tickmode: 'linear',
ticks: 'outside',
tick0: 0,
dtick: 0.25,
ticklen: 8,
tickwidth: 4,
tickcolor: '#000'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Logarithmic Axes
suite: axes
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {
type: 'log',
autorange: true
},
yaxis: {
type: 'log',
autorange: true
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Enumerated Ticks with Tickvals and Ticktext
suite: axes
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row)
{ return row[key]; });}
var trace1 = {
x:unpack(rows, 'Date'),
y: unpack(rows, 'IBM'),
mode: 'markers',
marker: {
size: 7,
line: {
width: 0.5},
opacity: 0.8},
type: 'scatter'
};
var layout = {
title: {
text: 'IBM Stock Data: Jan 2007 - Mar 2016'
},
xaxis: {
tickvals: ['2007-01-01', '2007-09-01', '2008-01-01', '2008-09-01', '2009-01-01', '2010-01-01', '2011-01-01', '2011-02-14', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01'],
ticktext: ['2007', 'Financial Crisis Starts', '2008', 'Financial Crisis Ends', '2009', '2010', '2011', 'IBM wins Jeopardy!', '2012', '2013', '2014', '2015', '2016']
}
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
});
---
name: Using Dates on the X-Axis
suite: axes
---
var trace1 = {
x: ['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04', '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08', '2000-01-09', '2000-01-10', '2000-01-11', '2000-01-12', '2000-01-13', '2000-01-14', '2000-01-15', '2000-01-16', '2000-01-17', '2000-01-18', '2000-01-19', '2000-01-20', '2000-01-21', '2000-01-22', '2000-01-23', '2000-01-24', '2000-01-25', '2000-01-26', '2000-01-27', '2000-01-28', '2000-01-29', '2000-01-30', '2000-01-31'],
y: [4.3, 8.2, 4.1, 5.6, -3, -0.2, 0.3, 0.4, 4.1, 5, 4.6, -0.2, -8.5, -9.1, -2.7, -2.7, -17, -11.3, -5.5, -6.5, -16.9, -12, -6.1, -6.6, -7.9, -10.8, -14.8, -11, -4.4, -1.3, -1.1],
mode: 'lines',
type: 'scatter',
name: '2000'
};
var data = [ trace1 ];
var layout = {
xaxis: {
type: 'date',
title: {
text: 'January Weather'
}
},
yaxis: {
title: {
text: 'Daily Mean Temperature'
}
},
title: {
text: '2000 Toronto January Weather'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Use Base64-Encoded Typed Arrays
suite: axes
order: 11
markdown\_content: |
Plotly.js 2.28.0 and later supports using base64-encoded typed arrays. To use a base64-encoded typed array, pass an object with the keys `bdata` (a base64-encoded string or the ArrayBuffer of an integer or float typed array) and `dtype` (the data type of the array, where the supported types are `float64`, `float32`, `int32`, `uint32`, `int16`, `uint16`, `int8`, `uint8`, and `uint8c`). You can also specify `shape` for multidimensional arrays. For example, `'4,10'` would be a 2D array with 4 rows and 10 columns.
---
var x = 'VVVVVVVV1b8AAAAAAAAAAFVVVVVVVdU/'
var y = 'q6qqPquqqr4='
var z = 'AABkAMgALAGQAfQB'
var trace1 = {
x: {
bdata: x,
dtype: 'f8'
},
y: {
bdata: y,
dtype: 'f4'
},
z: {
bdata: z,
dtype: 'u2',
shape: '2,3'
},
type: 'surface'
};
var data = [trace1];
Plotly.newPlot('myDiv', data);
---
name: Fully Opaque
suite: marker-style
markdown\_content: |
Fully opaque, the default setting, is useful for non-overlapping markers. When many points overlap it can be hard to observe density.
---
var x = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var y = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var data = [{
x: x,
y: y,
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
size: 20,
line: {
color: 'rgb(231, 99, 250)',
width: 2
}
},
showlegend: false
}, {
x: [2,2],
y: [4.25,4.75],
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
size: 60,
line: {
color: 'rgb(231, 99, 250)',
width: 6
}
},
showlegend: false
}]
Plotly.newPlot('myDiv', data)
---
description: How to style markers in JavaScript.
display\_as: file\_settings
name: Styling Markers
order: 11
page\_type: u-guide
permalink: javascript/marker-style/
thumbnail: thumbnail/marker-style.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","marker-style" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Trace Opacity
suite: marker-style
markdown\_content: |
Setting opacity outside the marker will set the opacity of the trace. Thus, it will allow greater visbility of additional traces but like fully opaque it is hard to distinguish density.
---
var x = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var y = Array.from({length: 500}, () => Math.random()\*(4.5-3)+3);
var x2 = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var y2 = Array.from({length: 500}, () => Math.random()\*(6-4.5)+4.5);
var data = [{
x: x,
y: y,
type: 'scatter',
mode: 'markers',
opacity: 0.5,
marker: {
color: 'rgb(17, 157, 255)',
size: 20,
line: {
color: 'rgb(231, 99, 250)',
width: 2
}
},
name: 'Opacity 0.5'
}, {
x: x2,
y: y2,
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
size: 20,
line: {
color: 'rgb(231, 99, 250)',
width: 2
}
},
name: 'Opacity 1.0'
}, {
x: [2,2],
y: [4.25,4.75],
type: 'scatter',
mode: 'markers',
opacity: 0.5,
marker: {
color: 'rgb(17, 157, 255)',
size: 60,
line: {
color: 'rgb(231, 99, 250)',
width: 6
}
},
showlegend: false
}]
Plotly.newPlot('myDiv', data)
---
name: Add Marker Border
suite: marker-style
markdown\_content: |
In order to make markers distinct, you can add a border to the markers. This can be achieved by adding the line dict to the marker dict. For example, `marker:{..., line: {...}}`.
---
var x = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var y = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var data = [{
x: x,
y: y,
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
size: 20,
line: {
color: 'rgb(231, 99, 250)',
width: 2
}
},
showlegend: false
}, {
x: [2],
y: [4.5],
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
size: 60,
line: {
color: 'rgb(231, 99, 250)',
width: 6
}
},
showlegend: false
}]
Plotly.newPlot('myDiv', data)
---
name: Color Opacity
suite: marker-style
markdown\_content: |
To maximise visibility of each point, set the color opacity by using alpha: `marker:{color: 'rgba(0,0,0,0.5)'}`. Here, the marker line will remain opaque.
---
var x = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var y = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var data = [{
x: x,
y: y,
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgba(17, 157, 255,0.5)',
size: 20,
line: {
color: 'rgb(231, 99, 250)',
width: 2
}
},
showlegend: false
}, {
x: [2,2],
y: [4.25,4.75],
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgba(17, 157, 255,0.5)',
size: 60,
line: {
color: 'rgb(231, 99, 250)',
width: 6
}
},
showlegend: false
}]
Plotly.newPlot('myDiv', data)
---
name: Marker Opacity
suite: marker-style
markdown\_content: |
To maximise visibility of density, it is recommended to set the opacity inside the marker `marker:{opacity:0.5}`. If multiple traces exist with high density, consider using marker opacity in conjunction with trace opacity.
---
var x = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var y = Array.from({length: 500}, () => Math.random()\*(6-3)+3);
var data = [{
x: x,
y: y,
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
opacity: 0.5,
size: 20,
line: {
color: 'rgb(231, 99, 250)',
width: 2
}
},
showlegend: false
}, {
x: [2,2],
y: [4.25,4.75],
type: 'scatter',
mode: 'markers',
marker: {
color: 'rgb(17, 157, 255)',
opacity: 0.5,
size: 60,
line: {
color: 'rgb(231, 99, 250)',
width: 6
}
},
showlegend: false
}]
Plotly.newPlot('myDiv', data)
---
name: Paper Referenced Annotations
suite: annotations
---
Plotly.newPlot('myDiv', [{
x: [1,2,3],
y: [2,1,2]
}], {
annotations: [{
xref: 'paper',
yref: 'paper',
x: 0,
xanchor: 'right',
y: 1,
yanchor: 'bottom',
text: 'X axis label',
showarrow: false
}, {
xref: 'paper',
yref: 'paper',
x: 1,
xanchor: 'left',
y: 0,
yanchor: 'top',
text: 'Y axis label',
showarrow: false
}]
})
---
name: Multiple Annotations
suite: annotations
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 3, 2, 4, 3, 4, 6, 5],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 5, 1, 2, 2, 3, 4, 2],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
annotations: [
{
x: 2,
y: 5,
xref: 'x',
yref: 'y',
text: 'Annotation Text',
showarrow: true,
arrowhead: 7,
ax: 0,
ay: -40
},
{
x: 4,
y: 4,
xref: 'x',
yref: 'y',
text: 'Annotation Text 2',
showarrow: true,
arrowhead: 7,
ax: 0,
ay: -40
}
]
};
Plotly.newPlot('myDiv', data, layout);
---
name: Simple Annotation
suite: annotations
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 3, 2, 4, 3, 4, 6, 5],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 5, 1, 2, 2, 3, 4, 2],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
annotations: [
{
x: 2,
y: 5,
xref: 'x',
yref: 'y',
text: 'Annotation Text',
showarrow: true,
arrowhead: 7,
ax: 0,
ay: -40
}
]
};
Plotly.newPlot('myDiv', data, layout);
---
name: 3D Annotations
suite: annotations
order: 4.75
---
var data = [{
type: "scatter3d",
x: ["2017-01-01", "2017-02-10", "2017-03-20"],
y: ["A", "B", "C"],
z: [1, 1e3, 1e5]
}]
var layout = {
scene: {
camera: {
eye: {x: 2.1, y: 0.1, z: 0.9}
},
xaxis: {
title: {
text: ""
}
},
yaxis: {
title: {
text: ""
}
},
zaxis: {
type: "log",
title: {
text: ""
}
},
annotations: [{
showarrow: false,
x: "2017-01-01",
y: "A",
z: 0,
text: "Point 1",
font: {
color: "black",
size: 12
},
xanchor: "left",
xshift: 10,
opacity: 0.7
}, {
x: "2017-02-10",
y: "B",
z: 4,
text: "Point 2",
textangle: 0,
ax: 0,
ay: -75,
font: {
color: "black",
size: 12
},
arrowcolor: "black",
arrowsize: 3,
arrowwidth: 1,
arrowhead: 1
}, {
x: "2017-03-20",
y: "C",
z: 5,
ax: 50,
ay: 0,
text: "Point 3",
arrowhead: 1,
xanchor: "left",
yanchor: "bottom"
}]
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Custom Text Color and Styling
suite: annotations
---
var trace1 = {
x: [0, 1, 2],
y: [1, 1, 1],
mode: 'lines+markers+text',
name: 'Lines, Markers and Text',
text: ['Text A', 'Text B', 'Text C'],
textposition: 'top right',
textfont: {
family: 'sans serif',
size: 18,
color: '#1f77b4'
},
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2],
y: [2, 2, 2],
mode: 'lines+markers+text',
name: 'Lines and Text',
text: ['Text G', 'Text H', 'Text I'],
textposition: 'bottom',
textfont: {
family: 'sans serif',
size: 18,
color: '#ff7f0e'
},
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {showlegend: false};
Plotly.newPlot('myDiv', data, layout);
---
name: WebGL Text and Annotations
suite: annotations
---
var n = 250;
var t = 12;
var x = [];
var y = [];
var z = [];
var text = [];
var arr = ["A","T","G", "C"];
for (var j = 0; j < t; j++){
ztemp = [];
for (var i = 0; i < n; i++) {
x.push(i);
y.push(j);
ztemp.push(Math.floor(Math.random() \* 10));
text.push(arr[Math.floor(Math.random() \* 4)])
}
z.push(ztemp)
}
var steps = [];
for (var e = 0; e < n-30; e++){
steps.push({
label: e,
value: e,
method: 'relayout',
args: ['xaxis', {range: [-0.5 + e, 30.5 + e]}]
})
}
data1 = {
x: x,
y: y,
mode: "text",
text: text,
type: "scattergl",
textfont: {
size: 20
}
}
data2 = {
z: z,
type: "heatmap"
}
sliders = [{
active: 0,
steps: steps
}]
layout = {
sliders: sliders,
xaxis: {
range: [-0.5, 30.5],
showline: false,
zeroline: false,
showgrid: false
},
yaxis: {
showline: false,
zeroline: false,
showgrid: false
}
}
data = [data1, data2]
Plotly.newPlot('myDiv', {data:data,
layout:layout});
---
name: Styling and Coloring Annotations
suite: annotations
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 3, 2, 4, 3, 4, 6, 5],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 4, 5, 1, 2, 2, 3, 4, 2],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
showlegend: false,
annotations: [
{
x: 2,
y: 5,
xref: 'x',
yref: 'y',
text: 'max=5',
showarrow: true,
font: {
family: 'Courier New, monospace',
size: 16,
color: '#ffffff'
},
align: 'center',
arrowhead: 2,
arrowsize: 1,
arrowwidth: 2,
arrowcolor: '#636363',
ax: 20,
ay: -30,
bordercolor: '#c7c7c7',
borderwidth: 2,
borderpad: 4,
bgcolor: '#ff7f0e',
opacity: 0.8
}
]
};
Plotly.newPlot('myDiv', data, layout);
---
name: Subplot Annotations
suite: annotations
order: 4.5
---
var trace0 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: 'scatter'
};
var trace1 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: 'x2',
yaxis: 'y2',
type: 'scatter'
};
var data = [trace0, trace1];
var layout = {
title: {
text: 'Subplot Annotations'
},
xaxis: {domain: [0, 0.45]},
yaxis2: {anchor: 'x2'},
xaxis2: {domain: [0.55, 1]},
annotations: [
{
x: 2,
y: 5,
xref: 'x',
yref: 'y',
text: 'Annotation A',
showarrow: true,
arrowhead: 3,
ax: -30,
ay: -40
},
{
x: 30,
y: 60,
xref: 'x2',
yref: 'y2',
text: 'Annotation B',
showarrow: true,
arrowhead: 2,
ax: -25,
ay: -40
}
]
};
Plotly.newPlot('myDiv', data, layout);
---
name: Adding Text to Data in Line and Scatter Plots
suite: annotations
---
var trace1 = {
x: [0, 1, 2],
y: [1, 1, 1],
mode: 'lines+markers+text',
name: 'Lines, Markers and Text',
text: ['Text A', 'Text B', 'Text C'],
textposition: 'top',
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2],
y: [2, 2, 2],
mode: 'markers+text',
name: 'Markers and Text',
text: ['Text D', 'Text E', 'Text F'],
textposition: 'bottom',
type: 'scatter'
};
var trace3 = {
x: [0, 1, 2],
y: [3, 3, 3],
mode: 'lines+text',
name: 'Lines and Text',
text: ['Text G', 'Text H', 'Text I'],
textposition: 'bottom',
type: 'scatter'
};
var data = [trace1, trace2, trace3];
var layout = {showlegend: false};
Plotly.newPlot('myDiv', data, layout);
---
name: Styling and Formatting Annotations
suite: annotations
---
var myPlot = document.getElementById('myDiv'),
N = 12,
x = d3.range(N).map( d3.random.normal(3) ),
y1 = d3.range(N).map( d3.random.normal(4) ),
y2 = d3.range(N).map( d3.random.normal(4) ),
y3 = d3.range(N).map( d3.random.normal(4) ),
months = ['Jan', 'Feb', 'Mar',
'Apr', 'May', 'June',
'July', 'Aug', 'Sept',
'Oct', 'Nov', 'Dec'],
data = [{ x:x, y:y1,
type:'scatter', mode:'markers',
name:'2014', text: months,
marker:{color:'rgba(200, 50, 100, .7)',
size:16}
},
{ x:x, y:y2,
type:'scatter', mode:'markers',
name:'2015', text:months,
marker:{color:'rgba(120, 20, 130, .7)',
size:16}
},
{ x:x, y:y3,
type:'scatter', mode:'markers',
name: '2016', text:months,
marker:{color:'rgba(10, 180, 180, .8)',
size:16}}];
layout = {
hovermode:'closest',
title: {text: '**Formatting Annotations**
 click on a point to plot an annotation'},
xaxis: {
zeroline: false,
title: {
text: 'Value A'
}
},
yaxis: {
zeroline: false,
title: {
text: 'Value B'
}
}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click',
function(data){
var point = data.points[0],
newAnnotation = {
x: point.xaxis.d2l(point.x),
y: point.yaxis.d2l(point.y),
arrowhead: 6,
ax: 0,
ay: -80,
bgcolor: 'rgba(255, 255, 255, 0.9)',
arrowcolor: point.fullData.marker.color,
font: {size:12},
bordercolor: point.fullData.marker.color,
borderwidth: 3,
borderpad: 4,
text: '*Series Identification*' +
'**Year** '+(point.data.name) + '
' +
'*Point Identification*
' +
'**Month** '+ (months[point.pointNumber]) +
'
*Point Values*
' +
'**A** '+(point.x).toPrecision(4) +
'
**B** '+(point.y).toPrecision(4)
},
divid = document.getElementById('myDiv'),
newIndex = (divid.layout.annotations || []).length;
console.log(point.pointNumber)
// delete instead if clicked twice
if(newIndex) {
var foundCopy = false;
divid.layout.annotations.forEach(function(ann, sameIndex) {
if(ann.text === newAnnotation.text ) {
Plotly.relayout('myDiv', 'annotations[' + sameIndex + ']', 'remove');
foundCopy = true;
}
});
if(foundCopy) return;
}
Plotly.relayout('myDiv', 'annotations[' + newIndex + ']', newAnnotation);
})
.on('plotly\_clickannotation', function(event, data) {
Plotly.relayout('myDiv', 'annotations[' + data.index + ']', 'remove');
});
---
name: Annotations with Log Axes
suite: annotations
order: 3.5
markdown\_content: |
If the `x` or `y` positions of an annotation reference a log axis, you need to provide that position as a `log10` value when adding the annotation. In this example, the `yaxis` is a log axis so we pass the `log10` value of `1000` to the annotation's `y` position.
---
var dates = [
"2024-01-01",
"2024-01-02",
"2024-01-03",
"2024-01-04",
"2024-01-05",
"2024-01-06",
];
var y\_values = [1, 30, 70, 100, 1000, 10000000];
var trace1 = {
x: dates,
y: y\_values,
mode: 'lines+markers',
type: 'scatter'
};
var layout = {
yaxis: {
type: 'log',
},
annotations: [
{
x: '2024-01-05',
y: Math.log10(1000),
text: 'Log axis annotation',
showarrow: true,
xanchor: 'right',
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
description: How to add text labels and annotations to D3.js-based plots in javascript.
display\_as: file\_settings
name: Text and Annotations
order: 26
page\_type: example\_index
permalink: javascript/text-and-annotations/
redirect\_from: javascript-graphing-library/text-and-annotations/
thumbnail: thumbnail/text-and-annotations.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","annotations" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Highlighting Clusters of Scatter Points with Circle Shapes
suite: shape
---
function normal\_array( mean, stddev, size ){
var arr = new Array(size), i;
// from http://bl.ocks.org/nrabinowitz/2034281
var generator = (function() {
return d3.random.normal(mean, stddev);
}());
for( i=0; i< arr.length; i++ ){
arr[i] = generator();
}
return arr;
}
var x0 = normal\_array(2, 0.45, 300);
var y0 = normal\_array(2, 0.45, 300);
var x1 = normal\_array(6, 0.4, 200);
var y1 = normal\_array(6, 0.4, 200)
var x2 = normal\_array(4, 0.3, 200);
var y2 = normal\_array(4, 0.3, 200);
console.log(x0);
var data = [
{
x: x0,
y: y0,
mode: 'markers'
}, {
x: x1,
y: y1,
mode: 'markers'
}, {
x: x2,
y: y2,
mode: 'markers'
}, {
x: x1,
y: y0,
mode: 'markers'
}
];
var layout = {
shapes: [
{
type: 'circle',
xref: 'x',
yref: 'y',
x0: d3.min(x0),
y0: d3.min(y0),
x1: d3.max(x0),
y1: d3.max(y0),
opacity: 0.2,
fillcolor: 'blue',
line: {
color: 'blue'
}
},
{
type: 'circle',
xref: 'x',
yref: 'y',
x0: d3.min(x1),
y0: d3.min(y1),
x1: d3.max(x1),
y1: d3.max(y1),
opacity: 0.2,
fillcolor: 'orange',
line: {
color: 'orange'
}
},
{
type: 'circle',
xref: 'x',
yref: 'y',
x0: d3.min(x2),
y0: d3.min(y2),
x1: d3.max(x2),
y1: d3.max(y2),
opacity: 0.2,
fillcolor: 'green',
line: {
color: 'green'
}
},
{
type: 'circle',
xref: 'x',
yref: 'y',
x0: d3.min(x1),
y0: d3.min(y0),
x1: d3.max(x1),
y1: d3.max(y0),
opacity: 0.2,
fillcolor: 'red',
line: {
color: 'red'
}
}
],
height: 400,
width: 480,
showlegend: false
}
Plotly.newPlot('myDiv', data, layout);
---
name: Lines Positioned Relative to the Plot and to the Axis
suite: shape
---
var trace1 = {
x: [2, 6],
y: [1, 1],
text: ['Line positioned relative to the plot', 'Line positioned relative to the axes'],
mode: 'text'
};
var layout = {
title: {
text: 'Lines Positioned Relative to the Plot & to the Axes'
},
xaxis: {
range: [0, 8]
},
yaxis: {
range: [0, 2]
},
width: 500,
height: 500,
shapes: [
//Line reference to the axes
{
type: 'line',
xref: 'x',
yref: 'y',
x0: 4,
y0: 0,
x1: 8,
y1: 1,
line: {
color: 'rgb(55, 128, 191)',
width: 3
}
},
//Line reference to the plot
{
type: 'line',
xref: 'paper',
yref: 'paper',
x0: 0,
y0: 0,
x1: 0.5,
y1: 0.5,
line: {
color: 'rgb(50, 171, 96)',
width: 3
}
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Rectangle Positioned Relative to the Plot and to the Axes
suite: shape
---
var trace1 = {
x: [1.5, 3],
y: [2.5, 2.5],
text: ['Rectangle reference to the plot', 'Rectangle reference to the axes'],
mode: 'text'
};
var layout = {
title: {
text: 'Rectangles Positioned Relative to the Plot and to the Axes'
},
xaxis: {
range: [0, 4],
showgrid: false
},
yaxis: {
range: [0, 4]
},
width: 800,
height: 600,
shapes: [
//Rectangle reference to the axes
{
type: 'rect',
xref: 'x',
yref: 'y',
x0: 2.5,
y0: 0,
x1: 3.5,
y1: 2,
line: {
color: 'rgb(55, 128, 191)',
width: 3
},
fillcolor: 'rgba(55, 128, 191, 0.6)'
},
//Rectangle reference to the Plot
{
type: 'rect',
xref: 'paper',
yref: 'paper',
x0: 0.25,
y0: 0,
x1: 0.5,
y1: 0.5,
line: {
color: 'rgb(50, 171, 96)',
width: 3
},
fillcolor: 'rgba(50, 171, 96, 0.6)'
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Highlighting Time Series Regions with Rectangle Shapes
suite: shape
---
var data = [
{
x: ['2015-02-01', '2015-02-02', '2015-02-03', '2015-02-04', '2015-02-05',
'2015-02-06', '2015-02-07', '2015-02-08', '2015-02-09', '2015-02-10',
'2015-02-11', '2015-02-12', '2015-02-13', '2015-02-14', '2015-02-15',
'2015-02-16', '2015-02-17', '2015-02-18', '2015-02-19', '2015-02-20',
'2015-02-21', '2015-02-22', '2015-02-23', '2015-02-24', '2015-02-25',
'2015-02-26', '2015-02-27', '2015-02-28'],
y: [-14, -17, -8, -4, -7, -10, -12, -14, -12, -7, -11, -7, -18, -14, -14,
-16, -13, -7, -8, -14, -8, -3, -9, -9, -4, -13, -9, -6],
mode: 'line',
name: 'temperature'
}
];
var layout = {
// to highlight the timestamp we use shapes and create a rectangular
shapes: [
// 1st highlight during Feb 4 - Feb 6
{
type: 'rect',
// x-reference is assigned to the x-values
xref: 'x',
// y-reference is assigned to the plot paper [0,1]
yref: 'paper',
x0: '2015-02-04',
y0: 0,
x1: '2015-02-06',
y1: 1,
fillcolor: '#d3d3d3',
opacity: 0.2,
line: {
width: 0
}
},
// 2nd highlight during Feb 20 - Feb 23
{
type: 'rect',
xref: 'x',
yref: 'paper',
x0: '2015-02-20',
y0: 0,
x1: '2015-02-22',
y1: 1,
fillcolor: '#d3d3d3',
opacity: 0.2,
line: {
width: 0
}
}
],
height: 500,
width: 500
}
Plotly.newPlot('myDiv', data, layout);
---
name: Rectangle Positioned Relative to the Axes
suite: shape
---
var trace1 = {
x: [1.5, 4.5],
y: [0.75, 0.75],
text: ['Unfilled Rectangle', 'Filled Rectangle'],
mode: 'text'
};
var layout = {
title: {
text: 'Rectangle Positioned Relative to the Axes'
},
xaxis: {
range: [0, 7],
showgrid: false
},
yaxis: {
range: [0, 3.5]
},
width: 500,
height: 500,
shapes: [
//Unfilled Rectangle
{
type: 'rect',
x0: 1,
y0: 1,
x1: 2,
y1: 3,
line: {
color: 'rgba(128, 0, 128, 1)'
}
},
//Filled Rectangle
{
type: 'rect',
x0: 3,
y0: 1,
x1: 6,
y1: 2,
line: {
color: 'rgba(128, 0, 128, 1)',
width: 2
},
fillcolor: 'rgba(128, 0, 128, 0.7)'
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Venn Diagram with Circle Shapes
suite: shape
---
var trace1 = {
x: [1, 1.75, 2.5],
y: [1, 1, 1],
type: 'scatter',
mode: 'text',
text: ['A', 'A+B', 'B'],
textfont: {
color: 'black',
size: 18,
family: 'Arial'
}
};
var layout = {
title: {
text: 'Venn Diagram with Circle Shapes'
},
xaxis: {
showticklabels: false,
tickmode: 'linear',
showgrid: false,
zeroline: false
},
yaxis: {
showticklabels: false,
tickmode: 'linear',
showgrid: false,
zeroline: false
},
shapes: [{
opacity: 0.3,
xref: 'x',
yref: 'y',
fillcolor: 'blue',
x0: 0,
y0: 0,
x1: 2,
y1: 2,
type: 'circle',
line: {
color: 'blue'
}
}, {
opacity: 0.3,
xref: 'x',
yref: 'y',
fillcolor: 'gray',
x0: 1.5,
y0: 0,
x1: 3.5,
y1: 2,
type: 'circle',
line: {
color: 'gray'
}
}],
margin: {
l: 20,
r: 20,
b: 100
},
height: 500,
width: 500
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Basic Arbitrary SVG Paths
suite: shape
---
var trace1 = {
x: [2, 1, 8, 8],
y: [0.25, 9, 2, 6],
text: ['filled triangle', 'filled Polygon', 'Quadratic Bezier Curves', 'Cubic Bezier Curves'],
mode: 'text'
};
var layout = {
title: {
text: 'Basic Arbitrary SVG Paths'
},
xaxis: {
range: [0, 9],
zeroline: false
},
yaxis: {
range: [0, 11],
showgrid: false
},
width: 500,
height: 500,
shapes: [
//Quadratic Bezier Curves
{
type: 'path',
path: 'M 4,4 Q 6,0 8,4',
line: {
color: 'rgb(93, 164, 214)'
}
},
//Cubic Bezier Curves
{
type: 'path',
path: 'M 1,4 C 2,8 6,4 8,8',
line: {
color: 'rgb(207, 114, 255)'
}
},
//Filled Triangle
{
type: 'path',
path: 'M 1 1 L 1 3 L 4 1 Z',
fillcolor: 'rgba(44, 160, 101, 0.5)',
line: {
color: 'rgb(44, 160, 101)'
}
},
//Filled Polygon
{
type: 'path',
path: ' M 3,7 L2,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z',
fillcolor: 'rgba(255, 140, 184, 0.5)',
line: {
color: 'rgb(255, 140, 184)'
}
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Adding Labels to Shapes
suite: shape
order: 11
markdown\_content: |
This example adds a `label` to a rectangle and a line on the graph,
sets a `font` `size` and `color` on the rectangle, and positions its label
'top center' using `textposition`. On the line, we specify a `yanchor` of "top"
to anchor the top of the label to its `textposition`.
You can also draw new shapes on the graph and each new shape automatically
gets a text label.
---
var data = [
{
x: [
'2015-02-01', '2015-02-02', '2015-02-03', '2015-02-04', '2015-02-05',
'2015-02-06', '2015-02-07', '2015-02-08', '2015-02-09', '2015-02-10',
'2015-02-11', '2015-02-12', '2015-02-13', '2015-02-14', '2015-02-15',
'2015-02-16', '2015-02-17', '2015-02-18', '2015-02-19', '2015-02-20',
'2015-02-21', '2015-02-22', '2015-02-23', '2015-02-24', '2015-02-25',
'2015-02-26', '2015-02-27', '2015-02-28',
],
y: [
14, 17, 8, 4, 7, 10, 12, 14, 12, 11, 10, 9, 18, 14, 14, 16, 13, 8, 8,
7, 7, 3, 9, 9, 4, 13, 9, 6,
],
mode: 'line',
},
];
var layout = {
title: {text: 'Product price changes and revenue growth'},
xaxis: { title: {text: 'Date' }},
yaxis: { title: {text: 'Revenue Growth' }},
dragmode: 'drawline',
shapes: [
{
type: 'rect',
xref: 'x',
yref: 'paper',
x0: '2015-02-02',
y0: 0,
x1: '2015-02-08',
y1: 1,
fillcolor: '#d3d3d3',
opacity: 0.2,
editable: true,
line: {
width: 0,
},
label: {
text: 'Price drop',
font: { size: 10, color: 'green' },
textposition: 'top center',
},
},
{
type: 'line',
x0: '2015-02-01',
y0: 8,
x1: '2015-02-28',
y1: 8,
fillcolor: '#d3d3d3',
opacity: 0.2,
editable: true,
label: {
text: 'January average',
yanchor: 'top',
},
},
],
newshape: { label: { text: 'New shape text' } },
height: 500,
width: 500,
};
var config = { 'modeBarButtonsToAdd': [
'drawline',
'drawopenpath',
'drawclosedpath',
'drawcircle',
'drawrect',
'eraseshape'
]
};
Plotly.newPlot('myDiv', data, layout, config);
---
description: How to make arbitrary D3.js-based SVG shapes in JavaScript. Examples
of lines, circle, rectangle, and path.
display\_as: file\_settings
name: Shapes
order: 23
page\_type: u-guide
permalink: javascript/shapes/
redirect\_from: javascript-graphing-library/shapes/
thumbnail: thumbnail/shape.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","shape" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Vertical and Horizontal Lines Positioned Relative to the Axes
suite: shape
---
var trace1 = {
x: [2, 3.5, 6],
y: [1, 1.5, 1],
text: ['Vertical Line', 'Horizontal Dashed Line', 'Diagonal dotted Line'],
mode: 'text'
};
var layout = {
title: {
text: 'Vertical and Horizontal Lines Positioned Relative to the Axes'
},
xaxis: {
range: [0, 7]
},
yaxis: {
range: [0, 2.5]
},
width: 500,
height: 500,
shapes: [
//line vertical
{
type: 'line',
x0: 1,
y0: 0,
x1: 1,
y1: 2,
line: {
color: 'rgb(55, 128, 191)',
width: 3
}
},
//Line Horizontal
{
type: 'line',
x0: 2,
y0: 2,
x1: 5,
y1: 2,
line: {
color: 'rgb(50, 171, 96)',
width: 4,
dash: 'dashdot'
}
},
//Line Diagonal
{
type: 'line',
x0: 4,
y0: 0,
x1: 6,
y1: 2,
line: {
color: 'rgb(128, 0, 128)',
width: 4,
dash: 'dot'
}
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Circle
suite: shape
---
var trace1 = {
x: [1.5, 3.5],
y: [0.75, 2.5],
text: ['Unfilled Circle', 'Filled Circle'],
mode: 'text'
};
var layout = {
title: {
text: 'Circles'
},
xaxis: {
range: [0, 4.5],
zeroline: false
},
yaxis: {
range: [0, 4.5]
},
width: 500,
height: 500,
shapes: [
// Unfilled Circle
{
type: 'circle',
xref: 'x',
yref: 'y',
x0: 1,
y0: 1,
x1: 3,
y1: 3,
line: {
color: 'rgba(50, 171, 96, 1)'
}
},
// Filled Circle
{
type: 'circle',
xref: 'x',
yref: 'y',
fillcolor: 'rgba(50, 171, 96, 0.7)',
x0: 3,
y0: 3,
x1: 4,
y1: 4,
line: {
color: 'rgba(50, 171, 96, 1)'
}
}
]
};
var data = [trace1];
Plotly.newPlot('myDiv', data, layout);
---
name: Creating Tangent Lines with Shapes
suite: shape
order: 10
---
function linspace(a,b,n) {
return d3.range(n).map(function(i){return a+i\*(b-a)/(n-1);});
}
var xValues = linspace(1, 3, 200);
var yValues = [];
for ( var i = 0 ; i < xValues.length ; i++ ) {
var result = xValues[i] \* Math.sin(Math.pow(xValues[i], 2)) + 1;
yValues.push(result);
};
var trace1 = {
x: xValues,
y: yValues,
type: 'scatter'
};
var data = [trace1];
var layout = {
title: {
text: 'Rectangles Positioned Relative to the Plot and to the Axes'
},
shapes: [{
type: 'line',
x0: 1,
y0: 2.30756,
x1: 1.75,
y1: 2.30756,
opacity: 0.7,
line: {
color: 'red',
width: 2.5
}
}, {
type: 'line',
x0: 2.5,
y0: 3.80796,
x1: 3.05,
y1: 3.80796,
opacity: 0.7,
line: {
color: 'red',
width: 2.5
}
}, {
type: 'line',
x0: 1.90,
y0: -1.1827,
x1: 2.50,
y1: -1.1827,
opacity: 0.7,
line: {
color: 'red',
width: 2.5
}
}],
height: 500,
width: 500
};
Plotly.newPlot('myDiv', data, layout);
---
description: Learn about the changes in Plotly.js version 3.
display_as: file_settings
language: plotly_js
name: Version 3 Changes
order: 27
page_type: u-guide
permalink: javascript/version-3-changes/
redirect_from: javascript/pointcloud/
thumbnail: thumbnail/pointcloud.jpg
---
This page outlines the changes in Plotly.js version 3 and cases where you may need to update your charts.

## Removed Features

Plotly.js 3 removes the following features that were deprecated in previous versions.

### `annotation.ref` Attribute

`annotation.ref` has been removed. Use `annotation.xref` and `annotation.yref` instead.

Here's an example using `annotation.ref`, followed by teh same example rewritte to use `annotation.xref` and `annotation.yref`:

```js
...
var layout = {
    title: "Try panning or zooming!",
    annotations: [{
        text: "Absolutely-positioned annotation",
        ref: "paper",
        x: 0.3,
        y: 0.3,
        showarrow: false
    }]
};
...
```

```js
...
var layout = {
    title: "Try panning or zooming!",
    annotations: [{
        text: "Absolutely-positioned annotation",
        xref: "paper",
        yref: "paper",
        x: 0.3,
        y: 0.3,
        showarrow: false
    }]
};
...
```

### `autotick` Attribute

The `autotick` attribute has been removed. Use `tickmode: 'auto'` instead of `autotick: true` and `tickmode: 'linear'` instead of `autotick: false`.

### `bardir` Attribute on Bar Charts

The `bardir` attribute for setting the bar direction on bar charts has been removed. Use `orientation` instead.

Here's an example using `bardir` to make the bars horizontal, followed by the same example rewritten to use `orientation`:

```js
var data = [{
    type: 'bar',
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    bardir: 'h',
}];

var layout = {
    title: 'Bar Chart with Horizontal Bars',
    xaxis: {
        title: 'X Axis'
    },
    yaxis: {
        title: 'Y Axis'
    }
};


Plotly.newPlot('bar-chart', data, layout);
```

```js
var data = [{
    type: 'bar',
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    orientation: 'h',
}];

var layout = {
    title: 'Bar Chart with Horizontal Bars',
    xaxis: {
        title: 'X Axis'
    },
    yaxis: {
        title: 'Y Axis'
    }
};


Plotly.newPlot('bar-chart', data, layout);
```

### `layout.scene.cameraposition` Attribute for 3D Plots

The `layout.scene.cameraposition` attribute on 3D plots has been removed. Use `layout.scene.camera` instead.

If you are using `cameraposition`, you'll need to update it for it work with the `camera` attribute. Here's an example of converting a `cameraposition` to `camera`. This example uses [gl-mat4](https://www.npmjs.com/package/gl-mat4#fromquatoutmat4-qquat4).

```js
var m4FromQuat = require('gl-mat4/fromQuat');

// Original cameraposition
var cameraposition = <cameraposition>;

var rotation = cameraposition[0];
var center = cameraposition[1];
var radius = cameraposition[2];
var mat = m4FromQuat([], rotation);
var eye = [];

for(j = 0; j < 3; ++j) {
    eye[j] = center[j] + radius * mat[2 + 4 * j];
}

// New camera
var camera = {
    eye: {x: eye[0], y: eye[1], z: eye[2]},
    center: {x: center[0], y: center[1], z: center[2]},
    up: {x: 0, y: 0, z: 1}
};
```

### `heatmapgl` Trace

`heatmapgl` has been removed. Use `heatmap` instead.

```
var data = [
  {
    z: [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
    type: 'heatmapgl'
  }
];

Plotly.newPlot('myDiv', data);
```

```
var data = [
  {
    z: [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
    type: 'heatmap'
  }
];

Plotly.newPlot('myDiv', data);
```

### `opacity` Attribute on Error Bars

The `opacity` attribute on error bars has been removed. Use the alpha channel of the `color` attribute instead.

Here's an example that was previously in the Plotly.js docs, and which uses `opacity`, followed by the same example rewritten to use the alpha channel on a `rgba` color value.

```
  error_y: {
    type: 'constant',
    value: 0.1,
    color: '#85144B',
    thickness: 1.5,
    width: 3,
    opacity: 0.5
  }

```

```
  error_y: {
    type: 'constant',
    value: 0.1,
    color: 'rgba(133, 20, 75, 0.5)',
    thickness: 1.5,
    width: 3,
  }

```

### jQuery Events

Support for using jQuery events has been removed. Use [Plotly.js events](/javascript/plotlyjs-events/) instead.

### `pointcloud` Trace

`pointcloud` has been removed. Use `scattergl` instead.

Here's an example that was previously in the Plotly.js docs and which uses `pointcloud`, followed by the same example rewritten to use `scattergl`:

```js
var myPlot = document.getElementById('myDiv');

var xy = new Float32Array([1,2,3,4,5,6,0,4]);


data = [{ xy: xy,  type: 'pointcloud' }];

layout = { };


Plotly.newPlot('myDiv', data, layout);
```

```js
var myPlot = document.getElementById('myDiv');

var xy = new Float32Array([1,2,3,4,5,6,0,4]);

var x = [];
var y = [];
for (var i = 0; i < xy.length; i += 2) {
    x.push(xy[i]);
    y.push(xy[i + 1]);
}

var data = [{
    x: x,
    y: y,
    mode: 'markers',
    type: 'scattergl',
    marker: {
        size: 10,
        color: 'blue',
        opacity: 0.8
    }
}];
var layout = {
    title: 'Point Cloud',
    xaxis: { title: 'X Axis' },
    yaxis: { title: 'Y Axis' }
};

Plotly.newPlot('myDiv', data, layout);
```

### `plot3dPixelRatio` for WebGL Image Export

The `plot3dPixelRatio` option on `config` for setting the pixel ration during WebGL image export has been removed. Use `plotGlPixelRatio` instead.


## `title` Attribute as a String

The `title` attribute can no longer be set as a string. Use `title.text` instead. Here's an example of how to set the title using `title.text`:

```js
var data = [
  {
    x: [1, 2, 3, 4, 5],
    y: [1, 2, 4, 8, 16]
  }
];

var layout = {
  title: { text: "My chart title" },
  xaxis: {
    title: {
      text: "x-axis title"
    }
  },
  yaxis: { title: { text: "y-axis title" } }
};

Plotly.newPlot("myDiv", data, layout);
```

### `titlefont`,`titleposition`, `titleside`, and `titleoffset` Attributes

The `titlefont`,`titleposition`, `titleside`, and `titleoffset` attributes are removed. Replace them with `title.font`, `title.position`, `title.side`, and `title.offset`.

Here's an example that uses `titlefont`, followed by the same example rewritten to use `title.font`:

```js
var data = [{
    type: 'bar',
    x: ['A', 'B', 'C', 'D'],
    y: [10, 15, 13, 17]
}];

var layout = {
    title: {
        text: 'Chart Title',
    },
    titlefont: {
        size: 40
    }
};

Plotly.newPlot('chart', data, layout);
```

```js
var data = [{
    type: 'bar',
    x: ['A', 'B', 'C', 'D'],
    y: [10, 15, 13, 17]
}];

var layout = {
    title: {
        text: 'Chart Title',
        font: {
            size: 40
        }
    },
};

Plotly.newPlot('chart', data, layout);
```

### Transforms

Transforms have been removed.

### `zauto`, `zmin`, and `zmax` from Surface Trace

The `zauto`, `zmin`, and `zmax` attributes have been removed on surface traces. Use `cauto`, `cmin`, and `cmax` instead.

```JavaScript
var data = [{
    z: [
        [1, 20, 30, 50],
        [20, 1, 60, 80],
        [30, 60, 1, 100],
        [50, 80, 100, 1]
    ],
    type: 'surface',
    zauto: false,
    zmin: 0,
    zmax: 100
}];
```

```JavaScript
var data = [{
    z: [
        [1, 20, 30, 50],
        [20, 1, 60, 80],
        [30, 60, 1, 100],
        [50, 80, 100, 1]
    ],
    type: 'surface',
    cauto: false,
    cmin: 0,
    cmax: 100
}];
```

---
description: How to format axes for 3d charts.
display\_as: file\_settings
name: 3D Axes
order: 12
page\_type: u-guide
permalink: javascript/3d-axes/
redirect\_from: javascript-graphing-library/3d-axes/
thumbnail: thumbnail/theming-and-templates.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-axes" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Range of Axes
suite: 3d-axes
---
function getrandom(num , mul)
{
var value = [ ];
for(i=0;i<=num;i++)
{
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var data=[
{
opacity:0.4,
type: 'scatter3d',
x: getrandom(50 , -75),
y: getrandom(50 , -75),
z: getrandom(50 , -75),
},
{
opacity:0.5,
type: 'scatter3d',
x: getrandom(50 , -75),
y: getrandom(50 , 75),
z: getrandom(50 , 75),
},
{
opacity:0.5,
type: 'scatter3d',
x: getrandom(50 , 100),
y: getrandom(50 , 100),
z: getrandom(50 , 100),
}
];
var layout = {
scene:{
aspectmode: "manual",
aspectratio: {
x: 1, y: 0.7, z: 1,
},
xaxis: {
nticks: 9,
range: [-200, 100],
},
yaxis: {
nticks: 7,
range: [-100, 100],
},
zaxis: {
nticks: 10,
range: [-150, 100],
}},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Ticks Formatting
suite: 3d-axes
---
function getrandom(num , mul)
{
var value = [ ];
for(i=0;i<=num;i++)
{
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var data=[
{
opacity:0.4,
type: 'scatter3d',
x: getrandom(50 , -75),
y: getrandom(50 , -75),
z: getrandom(50 , -75),
},
];
var layout = {
scene:{
xaxis: {
ticktext:['H20','C02','O2'],
tickvals:[-30, -45, -65, -10]
},
yaxis: {
nticks: 5,
tickfont:
{
color:'green',
family:'Old Standard TT, serif',
size: 14
},
ticksuffix:'$'
},
zaxis: {
ticks: 'outside',
tick0: 0,
tickwidth: 4}},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Camera Controls
suite: 3d-axes
---
function getrandom(num , mul)
{
var value = [ ];
for(i=0;i<=num;i++)
{
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var data = [
{
x: getrandom(20, 4),
y: getrandom(20, 3),
z: getrandom(20, 5),
opacity:0.5,
mode: "markers",
type: "scatter3d",
scene: "scene1",
name: "Lower the view point"
},
{
x:getrandom(20, 4),
y:getrandom(20, 3),
z:getrandom(20, 5),
opacity:0.5,
mode: "markers",
type: "scatter3d",
scene: "scene2",
name: "x-z plane"
},
{
x:getrandom(20, 4),
y:getrandom(20, 3),
z:getrandom(20, 5),
opacity:0.5,
mode: "markers",
type: "scatter3d",
scene: "scene3",
name: "y-z plane"
},
{
x:getrandom(10, 4),
y:getrandom(10, 3),
z:getrandom(10, 5),
opacity:0.5,
mode: "markers",
type: "scatter3d",
scene: "scene4",
name: "View from above"
},
{
x:getrandom(20, 4),
y:getrandom(20, 3),
z:getrandom(20, 5),
opacity:0.5,
mode: "markers",
type: "scatter3d",
scene: "scene5",
name: "Zooming in"
},
];
var layout = {
scene1: {
domain: {
x: [0.00, 0.33],
y: [0.5, 1]
},
camera: {
center: {
x: 0, y: 0, z: 0 },
eye: {
x: 2, y: 2, z: 0.1 },
up: {
x: 0, y: 0, z: 1 }
},},
scene2: {
domain: {
x: [0.33, 0.66],
y: [0.5, 1.0]
},
camera: {
center: {
x: 0, y: 0, z: 0},
eye: {
x:0.1, y:2.5, z:0.1},
up: {
x: 0, y: 0, z: 1}
},},
scene3: {
domain: {
x: [0.66, 0.99],
y: [0.5, 1]
},
camera: {
center: {
x: 0, y: 0, z: 0},
eye: {
x:2.5, y:0.1, z:0.1},
up: {
x: 0, y: 0, z: 1}
},},
scene4: {
domain: {
x: [0.15, 0.5],
y: [-0.25, 0.4]
},
camera: {
center: {
x: 0, y: 0, z: 0},
eye: {
x:0.1, y:0.1, z:2.5},
up: {
x: 0, y: 0, z: 1}
},},
scene5: {
domain: {
x: [0.62, 0.7],
y: [-0.2, 0.4]
},
camera: {
center: {
x: 0, y: 0, z: 0},
eye: {
x:0.1, y:0.1, z:1},
up: {
x: 0, y: 0, z: 1}
},},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Axes Background Color
suite: 3d-axes
---
function getrandom(num , mul)
{
var value = [ ];
for(i=0;i<=num;i++)
{
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var data=[
{
opacity:0.4,type: 'scatter3d',
x: getrandom(50 , 75),
y: getrandom(50 , 75),
z: getrandom(50 , 75),
mode:'markers'
},
{
opacity: 0.5,
type: 'scatter3d',
x: getrandom(75 , 75),
y: getrandom(75 , 75),
z: getrandom(75 , 75),
mode:'markers'
},
{
opacity: 0.5,
type: 'scatter3d',
x: getrandom(75 , 100),
y: getrandom(75 , 100),
z: getrandom(75 , 100),
mode:'markers'
}
];
var layout = {
scene:{
xaxis: {
backgroundcolor: "rgb(200, 200, 230)",
gridcolor: "rgb(255, 255, 255)",
showbackground: true,
zerolinecolor: "rgb(255, 255, 255)",
},
yaxis: {
backgroundcolor: "rgb(230, 200,230)",
gridcolor: "rgb(255, 255, 255)",
showbackground: true,
zerolinecolor: "rgb(255, 255, 255)"
},
zaxis: {
backgroundcolor: "rgb(230, 230,200)",
gridcolor: "rgb(255, 255, 255)",
showbackground: true,
zerolinecolor: "rgb(255, 255, 255)"
}}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Fixed Ratio Axes
suite: 3d-axes
order: 1.1
---
function getrandom(num , mul)
{
var value = [ ]
var i;
for(i=0;i<=num;i++)
{
rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var i;
traces = [];
names = ['cube', 'data', 'auto', 'manual'];
for (i=1; i<5; i++){
traces.push({
x: getrandom(20, 4),
y: getrandom(20, 3),
z: getrandom(20, 5),
opacity:0.5,
mode: "markers",
type: "mesh3d",
scene: "scene" + i,
name: names[i-1]
}
)
}
var layout = {
scene:{
aspectmode:'cube',
domain:{row:0, column:0}
},
scene2:{
aspectmode:'data',
domain:{row:1, column:0}
},
scene3:{
aspectmode:'auto',
domain:{row:0, column:1}
},
scene4:{
aspectmode:'manual',
aspectratio: {x:1, y:1, z:2},
domain: {row:1, column:1}
},
grid:{
pattern: 'independent',
rows:2,
columns:2
},
};
Plotly.newPlot('myDiv', traces, layout);
---
name: Set Axes Title
suite: 3d-axes
---
function getrandom(num , mul) {
var value = [ ];
for(i=0;i<=num;i++)
{
var rand = Math.random() \* mul;
value.push(rand);
}
return value;}
var trace1 = {
type:'mesh3d',
x: getrandom(1000,200), y: getrandom(1000,300), z: getrandom(1000,150),
color: 'lightblue',};
var trace2 = {
type:'mesh3d',
x: getrandom(1000,200), y: getrandom(1000,300), z: getrandom(1000,150),
color: 'pink'};
var layout = {
scene: {
xaxis: {
title: {
text: 'X AXIS TITLE'
}
},
yaxis: {
title: {
text: 'Y AXIS TITLE'
}
},
zaxis: {
title: {
text: 'Z AXIS TITLE'
}
}
},
autosize: false,
width: 550,
height: 500,
margin: {
l: 0,
r: 0,
b: 50,
t: 50,
pad: 4
},
}
Plotly.newPlot('myDiv', [trace1,trace2], layout);
---
name: Basic Contour Plot
suite: contour
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5.0, 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour'
}
];
var layout = {
title: {
text: 'Basic Contour Plot'
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Smoothing Contour Lines
suite: contour
---
var data = [ {
z: [[2, 4, 7, 12, 13, 14, 15, 16],
[3, 1, 6, 11, 12, 13, 16, 17],
[4, 2, 7, 7, 11, 14, 17, 18],
[5, 3, 8, 8, 13, 15, 18, 19],
[7, 4, 10, 9, 16, 18, 20, 19],
[9, 10, 5, 27, 23, 21, 21, 21],
[11, 14, 17, 26, 25, 24, 23, 22]],
type: 'contour',
line:{
smoothing: 0
},
xaxis: 'x1',
yaxis: 'y1'
},
{
z: [[2, 4, 7, 12, 13, 14, 15, 16],
[3, 1, 6, 11, 12, 13, 16, 17],
[4, 2, 7, 7, 11, 14, 17, 18],
[5, 3, 8, 8, 13, 15, 18, 19],
[7, 4, 10, 9, 16, 18, 20, 19],
[9, 10, 5, 27, 23, 21, 21, 21],
[11, 14, 17, 26, 25, 24, 23, 22]],
type: 'contour',
line:{
smoothing: 0.85
},
xaxis: 'x2',
yaxis: 'y2'
}];
var layout = {
title: {
text: 'Smoothing Contour Lines'
},
xaxis: {domain: [0, 0.45],
anchor: 'y1'},
yaxis: {domain: [0, 1],
anchor: 'x1'},
xaxis2: {domain: [0.55, 1],
anchor: 'y2'},
yaxis2: {domain: [0, 1],
anchor: 'x2'}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Color Bar Title
suite: contour
order: 11
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorbar:{
title: {
text: 'Color Bar Title',
side: 'right',
font: {
size: 14,
family: 'Arial, sans-serif'
}
}
}
}];
var layout = {
title: {
text: 'Colorbar with a Title'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Smooth Contour Coloring
suite: contour
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
contours: {
coloring: 'heatmap'
}
}];
var layout = {
title: {
text: 'Smooth Contour Coloring'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Setting X and Y Coordinates in a Contour Plot
suite: contour
---
var data = [{
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
x: [-9, -6, -5 , -3, -1],
y: [0, 1, 4, 5, 7],
type: 'contour'
}];
var layout = {
title: {
text: 'Setting the X and Y Coordinates in a Contour Plot'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Simple Contour Plot
suite: contour
---
var size = 100, x = new Array(size), y = new Array(size), z = new Array(size), i, j;
for(var i = 0; i < size; i++) {
x[i] = y[i] = -2 \* Math.PI + 4 \* Math.PI \* i / size;
z[i] = new Array(size);
}
for(var i = 0; i < size; i++) {
for(j = 0; j < size; j++) {
var r2 = x[i]\*x[i] + y[j]\*y[j];
z[i][j] = Math.sin(x[i]) \* Math.cos(y[j]) \* Math.sin(r2) / Math.log(r2+1);
}
}
var data = [ {
z: z,
x: x,
y: y,
type: 'contour'
}
];
Plotly.newPlot('myDiv', data);
---
name: Colorscale for Contour Plot
suite: contour
---
var data = [{
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: 'Jet',
}];
var layout = {
title: {
text: 'Colorscale for Contour Plot'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Connect the Gaps between Null Values in the Z Matrix
suite: contour
---
var trace1 = {
z: [[null, null, null, 12, 13, 14, 15, 16],
[null, 1, null, 11, null, null, null, 17],
[null, 2, 6, 7, null, null, null, 18],
[null, 3, null, 8, null, null, null, 19],
[5, 4, 10, 9, null, null, null, 20],
[null, null, null, 27, null, null, null, 21],
[null, null, null, 26, 25, 24, 23, 22]],
type: 'contour',
showscale: false,
xaxis: 'x1',
yaxis: 'y1'
};
var trace2 = {
z: [[null, null, null, 12, 13, 14, 15, 16],
[null, 1, null, 11, null, null, null, 17],
[null, 2, 6, 7, null, null, null, 18],
[null, 3, null, 8, null, null, null, 19],
[5, 4, 10, 9, null, null, null, 20],
[null, null, null, 27, null, null, null, 21],
[null, null, null, 26, 25, 24, 23, 22]],
connectgaps: true,
type: 'contour',
showscale: false,
xaxis: 'x2',
yaxis: 'y2'
};
var trace3 = {
z: [[null, null, null, 12, 13, 14, 15, 16],
[null, 1, null, 11, null, null, null, 17],
[null, 2, 6, 7, null, null, null, 18],
[null, 3, null, 8, null, null, null, 19],
[5, 4, 10, 9, null, null, null, 20],
[null, null, null, 27, null, null, null, 21],
[null, null, null, 26, 25, 24, 23, 22]],
zsmooth: 'best',
type: 'heatmap',
showscale: false,
xaxis: 'x3',
yaxis: 'y3'
};
var trace4 = {
z: [[null, null, null, 12, 13, 14, 15, 16],
[null, 1, null, 11, null, null, null, 17],
[null, 2, 6, 7, null, null, null, 18],
[null, 3, null, 8, null, null, null, 19],
[5, 4, 10, 9, null, null, null, 20],
[null, null, null, 27, null, null, null, 21],
[null, null, null, 26, 25, 24, 23, 22]],
zsmooth: 'best',
type: 'heatmap',
showscale: false,
connectgaps: true,
xaxis: 'x4',
yaxis: 'y4'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'Connect the Gaps Between Null Values in the Z Matrix'
},
xaxis: {domain: [0, 0.45],
anchor: 'y1'},
yaxis: {domain: [0.55, 1],
anchor: 'x1'},
xaxis2: {domain: [0.55, 1],
anchor: 'y2'},
yaxis2: {domain: [0.55, 1],
anchor: 'x2'},
xaxis3: {domain: [0, 0.45],
anchor: 'y3'},
yaxis3: {domain: [0, 0.45],
anchor: 'x3'},
xaxis4: {domain: [0.55, 1],
anchor: 'y4'},
yaxis4: {domain: [0, 0.45],
anchor: 'x4'}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based contour plot in javascript. Examples of contour
plots of matrices with subplots, custom color-scales, and smoothing.
display\_as: scientific
name: Contour Plots
page\_type: example\_index
permalink: javascript/contour-plots/
redirect\_from: javascript-graphing-library/contour-plots/
thumbnail: thumbnail/contour.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","contour" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Color Bar Size
suite: contour
order: 12
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorbar:{
thickness: 75,
thicknessmode: 'pixels',
len: 0.9,
lenmode: 'fraction',
outlinewidth: 0
}
}];
var layout = {
title: {
text: 'Colorbar Size for Contour Plots'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Contour Line Labels
suite: contour
order: 9.5
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5.0, 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
contours: {
coloring: 'heatmap',
showlabels: true,
labelfont: {
family: 'Raleway',
size: 12,
color: 'white',
}
}
}];
var layout = {
title: {
text: 'Contour with Labels'
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Contour Lines
suite: contour
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: 'Jet',
contours:{
coloring: 'lines'
}
}];
var layout = {
title: {
text: 'Contour Lines'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Customizing Size and Range of a Contour Plot's Contours
suite: contour
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: 'Jet',
autocontour: false,
contours: {
start: 0,
end: 8,
size: 2
}
}];
var layout = {
title: {
text: 'Customizing Size and Range of Contours'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Custom Colorscale for Contour Plot
suite: contour
order: 10
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: [[0, 'rgb(166,206,227)'], [0.25, 'rgb(31,120,180)'], [0.45, 'rgb(178,223,138)'], [0.65, 'rgb(51,160,44)'], [0.85, 'rgb(251,154,153)'], [1, 'rgb(227,26,28)']]
}
];
var layout = {
title: {
text: 'Custom Contour Plot Colorscale'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Styling Color Bar Ticks for Contour Plots
suite: contour
order: 13
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorbar:{
ticks: 'outside',
dtick: 1,
tickwidth: 2,
ticklen: 10,
tickcolor: 'grey',
showticklabels: true,
tickfont: {
size: 15
},
xpad: 50
}
}];
var layout = {
title: {
text: 'Styling Color Bar Ticks for Contour Plots'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Customizing Spacing Between X and Y Ticks
suite: contour
---
var data = [ {
z: [[10, 10.625, 12.5, 15.625, 20],
[5.625, 6.25, 8.125, 11.25, 15.625],
[2.5, 3.125, 5., 8.125, 12.5],
[0.625, 1.25, 3.125, 6.25, 10.625],
[0, 0.625, 2.5, 5.625, 10]],
type: 'contour',
colorscale: 'Jet',
dx: 10,
x0: 5,
dy: 10,
y0: 10
}];
var layout = {
title: {
text: 'Customizing Spacing Between X and Y Axis Ticks'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Add Multiple Carpet Scatter Traces
suite: scattercarpet
description:
---
var trace1 = {
type: "carpet",
a: [0.1, 0.2, 0.3],
b: [1, 2, 3],
y: [
[1, 2.2, 3],
[1.5, 2.7, 3.5],
[1.7, 2.9, 3.7]
],
cheaterslope: 1,
aaxis: {
title: {
text: "a"
},
tickmode: "linear",
dtick: 0.05,
minorgridcount: 9
},
baxis: {
title: {
text: "b"
},
tickmode: "linear",
dtick: 0.5,
minorgridcount: 9
}
}
var trace2 = {
type: "scattercarpet",
name: "b = 1.5",
a: [0.05, 0.15, 0.25, 0.35],
b: [1.5, 1.5, 1.5, 1.5]
}
var trace3 = {
type: "scattercarpet",
name: "b = 2",
a: [0.05, 0.15, 0.25, 0.35],
b: [2, 2, 2, 2]
}
var trace4 = {
type: "scattercarpet",
name: "b = 2.5",
a: [0.05, 0.15, 0.25, 0.35],
b: [2.5, 2.5, 2.5, 2.5]
}
var trace5 = {
type: "scattercarpet",
name: "a = 0.15",
a: [0.15, 0.15, 0.15, 0.15],
b: [0.5, 1.5, 2.5, 3.5],
line: {
smoothing: 1,
shape: "spline"
}
}
var trace6 = {
type: "scattercarpet",
name: "a = 0.2",
a: [0.2, 0.2, 0.2, 0.2],
b: [0.5, 1.5, 2.5, 3.5],
line: {
smoothing: 1,
shape: "spline"
},
marker: {
size: [10, 20, 30, 40],
color: ["#000", "#f00", "#ff0", "#fff"]
}
}
var trace7 = {
type: "scattercarpet",
name: "a = 0.25",
a: [0.25, 0.25, 0.25, 0.25],
b: [0.5, 1.5, 2.5, 3.5],
line: {
smoothing: 1,
shape: "spline"
}
}
var data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7]
var layout = {
title: {
text: "scattercarpet extrapolation, clipping, and smoothing"
},
hovermode: "closest"
}
Plotly.newPlot('myDiv', data, layout)
---
description: How to make D3.js-based carpet scatter plots in Plotly.js.
display\_as: scientific
name: Carpet Scatter Plot
order: 10
permalink: javascript/carpet-scatter/
thumbnail: thumbnail/scattercarpet.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","scattercarpet" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add Carpet Scatter Trace
suite: scattercarpet
description:
---
var trace1 = {
type: 'carpet',
a: [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6].map(a => a \* 1e-6),
b: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3].map(b => b \* 1e6),
y: [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
aaxis: {
tickprefix: 'a = ',
ticksuffix: 'm',
smoothing: 1,
minorgridcount: 9,
},
baxis: {
tickprefix: 'b = ',
ticksuffix: 'Pa',
smoothing: 1,
minorgridcount: 9,
}
}
var trace2 = {
type: 'scattercarpet',
a: [4, 4.5, 5, 6].map(a => a \* 1e-6),
b: [1.5, 2.5, 1.5, 2.5].map(b => b \* 1e6),
line: {shape: 'spline', smoothing: 1}
}
var data = [trace1,trace2]
Plotly.newPlot('myDiv', data)
---
name: Basic Carpet Plot
suite: scattercarpet
description:
---
var trace1 = {
type: 'carpet',
a: [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6].map(a => a \* 1e-6),
b: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3].map(b => b \* 1e6),
y: [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
aaxis: {
tickprefix: 'a = ',
ticksuffix: 'm',
smoothing: 1,
minorgridcount: 9,
},
baxis: {
tickprefix: 'b = ',
ticksuffix: 'Pa',
smoothing: 1,
minorgridcount: 9,
}
}
var data = [trace1]
Plotly.newPlot('myDiv', data)
---
description: How to make a plot with D3.js-based logarithmic axes in javascript.
display\_as: scientific
name: Log Plots
page\_type: example\_index
permalink: javascript/log-plot/
redirect\_from: javascript-graphing-library/log-plot/
thumbnail: thumbnail/log.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","log" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Logarithmic Axes
suite: log
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {
type: 'log',
autorange: true
},
yaxis: {
type: 'log',
autorange: true
}
};
Plotly.newPlot('myDiv', data, layout);
---
permalink: javascript/scientific-charts/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make scientific graphs such as heatmaps and contour plots.
name: Scientific Charts
layout: langindex
display\_as: scientific
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Scientific Charts

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","scientific" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
description: How to make D3.js-based carpet contour plots in Plotly.js.
display\_as: scientific
name: Carpet Contour Plot
order: 11
permalink: javascript/carpet-contour/
thumbnail: thumbnail/contourcarpet.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","contourcarpet" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Add Multiple Traces
suite: contourcarpet
description:
---
function Get(url){
var Httpreq = new XMLHttpRequest();
Httpreq.open("GET",url,false);
Httpreq.send(null);
return Httpreq.responseText;
}
var json\_obj = JSON.parse(Get("https://raw.githubusercontent.com/bcdunbar/datasets/master/airfoil\_data.json"));
var trace1 = {
a: json\_obj[0].a,
b: json\_obj[0].b,
baxis: {
startline: false,
endline: false,
showticklabels: "none",
smoothing: 0,
showgrid: false
},
x: json\_obj[0].x,
y: json\_obj[0].y,
type: "carpet",
aaxis:{
startlinewidth: 2,
startline: true,
showticklabels: "none",
endline: true,
showgrid: false,
endlinewidth: 2,
smoothing: 0
}
}
var trace2 = {
autocolorscale: false,
zmax: 1,
name: "Pressure",
colorscale: "Viridis",
zmin: -8,
colorbar: {
y: 0,
yanchor: "bottom",
title: {side:
'right'
},
len: 0.75,
title: {
text: "Pressure coefficient, cp"
},
},
contours: {
start: -1,
size: 0.025,
end: 1.000,
showlines: false
},
line: {
smoothing: 0
},
z: json\_obj[1].z,
type: "contourcarpet",
autocontour: false,
zauto: false
}
var trace3 = {
opacity: 0.300,
showlegend: true,
name: "Streamlines",
autocontour: true,
ncontours: 50,
contours: {
coloring: "none"
},
line: {
color: "white",
width: 1
},
z: json\_obj[2].z,
type: "contourcarpet"
}
var trace4 = {
showlegend: true,
name: "Pressure
contours",
autocontour: false,
z: json\_obj[3].z,
type: "contourcarpet",
line: {
color: "rgba(0, 0, 0, 0.5)",
smoothing: 1
},
contours: {
size: 0.250,
start: -4,
coloring: "none",
end: 1.000,
showlines: true
}
}
var trace5 = {
legendgroup: "g1",
name: "Surface
pressure",
mode: "lines",
hoverinfo: "skip",
x: json\_obj[4].x,
y: json\_obj[4].y,
line: {
color: "rgba(255, 0, 0, 0.5)",
width: 1,
shape: "spline",
smoothing: 1
},
fill: "toself",
type: "scatter",
fillcolor: "rgba(255, 0, 0, 0.2)"
}
var trace6 = {
showlegend: false,
legendgroup: "g1",
mode: "lines",
hoverinfo: "skip",
x: json\_obj[5].x,
y: json\_obj[5].y,
line: {
color: "rgba(255, 0, 0, 0.3)",
width: 1
},
type: "scatter"
}
var trace7 = {
showlegend: false,
legendgroup: "g1",
name: "cp",
text: json\_obj[6].text,
mode: "lines",
hoverinfo: "text",
x: json\_obj[6].x,
y: json\_obj[6].y,
line: {
color: "rgba(255, 0, 0, 0.2)",
width: 0
},
type: "scatter"
}
data = [trace1,trace2,trace3,trace4,trace5,trace6,trace7]
var layout = {
yaxis: {
zeroline: false,
range: [-1.800,1.800],
showgrid: false
},
dragmode: "pan",
height: 700,
xaxis: {
zeroline: false,
scaleratio: 1,
scaleanchor: "y",
range: [-3.800,3.800],
showgrid: false
},
title: {
text: "Flow over a Karman-Trefftz airfoil"
},
hovermode: "closest",
margin: {
r: 60,
b: 40,
l: 40,
t: 80
},
width: 900
}
Plotly.newPlot('myDiv', data, layout);
---
name: Basic Carpet Plot
suite: contourcarpet
description:
---
var trace1 = {
type: 'carpet',
a: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
b: [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
x: [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
y: [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
aaxis: {
tickprefix: "a = ",
smoothing: 0,
minorgridcount: 9,
type: 'linear'
},
baxis: {
tickprefix: "b = ",
smoothing: 0,
minorgridcount: 9,
type: 'linear'
}
}
var layout = {
title: {
text: "Cheater plot with 1d input"
},
margin: {
t: 40, r: 30, b: 30, l: 30
},
yaxis: {
range: [0.388,4.361]
},
xaxis: {
range: [0.667,5.932]
}
}
var data = [trace1]
Plotly.newPlot('myDiv', data, layout)
---
name: Add Contours
suite: contourcarpet
description:
---
var trace1 = {
type: 'contourcarpet',
a: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
b: [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
z: [1, 1.96, 2.56, 3.0625, 4, 5.0625, 1, 7.5625, 9, 12.25, 15.21, 14.0625],
autocontour: false,
contours: {
start: 1,
end: 14,
size: 1
},
line: {
width: 2,
smoothing: 0
},
colorbar: {
len: 0.4,
y: 0.25
}
}
var trace2 = {
type: 'carpet',
a: [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
b: [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
x: [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
y: [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
aaxis: {
tickprefix: "a = ",
smoothing: 0,
minorgridcount: 9,
type: 'linear'
},
baxis: {
tickprefix: "b = ",
smoothing: 0,
minorgridcount: 9,
type: 'linear'
}
}
var layout = {
title: {
text: "Cheater plot with 1d input"
},
margin: {
t: 40, r: 30, b: 30, l: 30
},
yaxis: {
range: [0.388,4.361]
},
xaxis: {
range: [0.667,5.932]
}
}
var data = [trace1,trace2]
Plotly.newPlot('myDiv', data, layout)
---
description: How to make D3.js-based parallel coordinates plots in Plotly.js.
display\_as: scientific
name: Parallel Coordinates Plot
page\_type: example\_index
permalink: javascript/parallel-coordinates-plot/
thumbnail: thumbnail/parcoords.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","parcoords" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Adding Dimensions
suite: parcoords
description:
markdown\_content: |
Parallel coordinates are richly interactive by default. Drag the lines along the axes to filter regions and drag the axis names across the plot to rearrange variables: ![IPython terminal](https://s3-us-west-1.amazonaws.com/plotly-tutorials/plotly-documentation/images/js\_parcoords\_ex1.gif)
---
var trace = {
type: 'parcoords',
line: {
color: 'blue'
},
dimensions: [{
range: [1, 5],
constraintrange: [1, 2],
label: 'A',
values: [1,4]
}, {
range: [1,5],
label: 'B',
values: [3,1.5],
tickvals: [1.5,3,4.5]
}, {
range: [1, 5],
label: 'C',
values: [2,4],
tickvals: [1,2,4,5],
ticktext: ['text 1','text 2','text 4','text 5']
}, {
range: [1, 5],
label: 'D',
values: [4,2]
}]
};
var data = [trace]
Plotly.newPlot('myDiv', data);
---
name: Basic Parallel Coordinates Plot
suite: parcoords
description:
---
d3.csv('https://raw.githubusercontent.com/bcdunbar/datasets/master/iris.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var data = [{
type: 'parcoords',
pad: [80,80,80,80],
line: {
color: unpack(rows, 'species\_id'),
colorscale: [[0, 'red'], [0.5, 'green'], [1, 'blue']]
},
dimensions: [{
range: [2, 4.5],
label: 'sepal\_width',
values: unpack(rows, 'sepal\_width')
}, {
constraintrange: [5, 6],
range: [4,8],
label: 'sepal\_length',
values: unpack(rows, 'sepal\_length')
}, {
label: 'petal\_width',
range: [0, 2.5],
values: unpack(rows, 'petal\_width')
}, {
label: 'petal\_length',
range: [1, 7],
values: unpack(rows, 'petal\_length')
}]
}];
var layout = {
width: 800
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Advanced Parallel Coordinates Plot
suite: parcoords
description:
---
d3.csv('https://raw.githubusercontent.com/bcdunbar/datasets/master/parcoords\_data.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var data = [{
type: 'parcoords',
line: {
showscale: true,
reversescale: true,
colorscale: 'Jet',
cmin: -4000,
cmax: -100,
color: unpack(rows, 'colorVal')
},
dimensions: [{
constraintrange: [100000, 150000],
range: [32000, 227900],
label: 'Block height',
values: unpack(rows, 'blockHeight')
}, {
range: [0, 700000],
label: 'Block width',
values: unpack(rows, 'blockWidth')
}, {
label: 'Cylinder material',
tickvals: [0, 0.5, 1, 2, 3],
ticktext: ['A', 'AB', 'B', 'Y', 'Z'],
values: unpack(rows, 'cycMaterial')
}, {
label: 'Block material',
tickvals: [0, 1, 2, 3],
range: [-1, 4],
values: unpack(rows, 'blockMaterial')
}, {
range: [134, 3154],
label: 'Total weight',
visible: true,
values: unpack(rows, 'totalWeight')
}, {
range: [9, 19984],
label: 'Assembly penalty weight',
values: unpack(rows, 'assemblyPW')
}, {
range: [49000, 568000],
label: 'Height st width',
values: unpack(rows, 'HstW')
}, {
range: [-28000, 196430],
label: 'Min height width',
values: unpack(rows, 'minHW')
}, {
range: [98453, 501789],
label: 'Min width diameter',
values: unpack(rows, 'minWD')
}, {
range: [1417, 107154],
label: 'RF block',
values: unpack(rows, 'rfBlock')
}]
}];
Plotly.newPlot('myDiv', data);
});
---
name: Annotated Parallel Coordinates Plot
suite: parcoords
order: 2.5
description:
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-id.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var data = [{
type: 'parcoords',
pad: [80,80,80,80],
line: {
color: unpack(rows, 'species\_id'),
colorscale: [[0, 'red'], [0.5, 'green'], [1, 'blue']]
},
dimensions: [{
range: [2, 4.5],
label: 'sepal\_width',
values: unpack(rows, 'sepal\_width')
}, {
constraintrange: [5, 6],
range: [4,8],
label: 'sepal\_length',
values: unpack(rows, 'sepal\_length')
}, {
label: 'petal\_width',
range: [0, 2.5],
values: unpack(rows, 'petal\_width')
}, {
label: 'petal\_length',
range: [1, 7],
values: unpack(rows, 'petal\_length')
}]
}];
var layout = {
width: 800,
annotations: [
{showarrow: false,
text: 'Higher sepal width',
x: 0, y: 1, xref: 'paper', yref: 'paper'},
{showarrow: false,
text: 'Lower petal width and length',
x: 0.9, y: .25, xref: 'paper', yref: 'paper'
}]
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to graph D3.js-based wind rose charts in plotly.js .
display\_as: scientific
name: Wind Rose Charts
permalink: javascript/wind-rose-charts/
redirect\_from: javascript-graphing-library/wind-rose-charts/
thumbnail: thumbnail/wind-rose.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","wind-rose" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Wind Rose Chart
suite: wind-rose
order: 17
---
var data = [{
r: [77.5, 72.5, 70.0, 45.0, 22.5, 42.5, 40.0, 62.5],
theta: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "11-14 m/s",
marker: {color: "rgb(106,81,163)"},
type: "barpolar"
}, {
r: [57.5, 50.0, 45.0, 35.0, 20.0, 22.5, 37.5, 55.0],
theta: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "8-11 m/s",
marker: {color: "rgb(158,154,200)"},
type: "barpolar"
}, {
r: [40.0, 30.0, 30.0, 35.0, 7.5, 7.5, 32.5, 40.0],
theta: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "5-8 m/s",
marker: {color: "rgb(203,201,226)"},
type: "barpolar"
}, {
r: [20.0, 7.5, 15.0, 22.5, 2.5, 2.5, 12.5, 22.5],
theta: ["North", "N-E", "East", "S-E", "South", "S-W", "West", "N-W"],
name: "< 5 m/s",
marker: {color: "rgb(242,240,247)"},
type: "barpolar"
}]
var layout = {
title: {
text: "Wind Speed Distribution in Laurel, NE"
},
font: {size: 16},
legend: {font: {size: 16}},
polar: {
barmode: "overlay",
bargap: 0,
radialaxis: {ticksuffix: "%", angle: 45, dtick: 20},
angularaxis: {direction: "clockwise"}
}
}
Plotly.newPlot("myDiv", data, layout)
---
name: Annotated Heatmap
suite: heatmap
arrangement: horizontals
---
var xValues = ['A', 'B', 'C', 'D', 'E'];
var yValues = ['W', 'X', 'Y', 'Z'];
var zValues = [
[0.00, 0.00, 0.75, 0.75, 0.00],
[0.00, 0.00, 0.75, 0.75, 0.00],
[0.75, 0.75, 0.75, 0.75, 0.75],
[0.00, 0.00, 0.00, 0.75, 0.00]
];
var colorscaleValue = [
[0, '#3D9970'],
[1, '#001f3f']
];
var data = [{
x: xValues,
y: yValues,
z: zValues,
type: 'heatmap',
colorscale: colorscaleValue,
showscale: false
}];
var layout = {
title: {
text: 'Annotated Heatmap'
},
annotations: [],
xaxis: {
ticks: '',
side: 'top'
},
yaxis: {
ticks: '',
ticksuffix: ' ',
width: 700,
height: 700,
autosize: false
}
};
for ( var i = 0; i < yValues.length; i++ ) {
for ( var j = 0; j < xValues.length; j++ ) {
var currentValue = zValues[i][j];
if (currentValue != 0.0) {
var textColor = 'white';
}else{
var textColor = 'black';
}
var result = {
xref: 'x1',
yref: 'y1',
x: xValues[j],
y: yValues[i],
text: zValues[i][j],
font: {
family: 'Arial',
size: 12,
color: 'rgb(50, 171, 96)'
},
showarrow: false,
font: {
color: textColor
}
};
layout.annotations.push(result);
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Heatmap with Categorical Axis Labels
suite: heatmap
markdown\_content: |
In this example we also show how to ignore [hovertext](https://plotly.com/javascript/hover-text-and-formatting/) when we have missing values in the data by setting the [hoverongaps](https://plotly.com/javascript/reference/heatmap/#heatmap-hoverongaps) to False.
---
var data = [
{
z: [[1, null, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
y: ['Morning', 'Afternoon', 'Evening'],
type: 'heatmap',
hoverongaps: false
}
];
Plotly.newPlot('myDiv', data);
---
description: How to make a D3.js-based heatmap in javascript with a matrix. Seven
examples of colored and labeled heatmaps with custom colorscales.
display\_as: scientific
name: Heatmaps
page\_type: example\_index
permalink: javascript/heatmaps/
redirect\_from:
- javascript-graphing-library/heatmaps/
- javascript-graphing-library/heatmap-webgl/
- javascript/heatmap-webgl/
thumbnail: thumbnail/heatmap.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","heatmap" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Heatmap
suite: heatmap
---
var data = [
{
z: [[1, 20, 30], [20, 1, 60], [30, 60, 1]],
type: 'heatmap'
}
];
Plotly.newPlot('myDiv', data);
---
name: Heatmap with Unequal Block Sizes
suite: heatmap
---
function linspace(a,b,n) {
return d3.range(n).map(function(i){return a+i\*(b-a)/(n-1);});
}
//number of spiral loops
var nspiral = 2;
// angle
var th = linspace(((-Math.PI) / 13), (2 \* Math.PI \* nspiral), 1000);
//Empty Value Containers
var xValues = [];
var yValues = [];
var yShift = [];
var finalX = [];
var finalY = [];
//spiral
for(var i = 0; i < th.length; i++){
var a = 1.120529;
var b = 0.306349;
var r = a \* Math.exp((-b) \* th[i]);
var xResult = (r \* Math.cos(th[i]));
var yResult = (r \* Math.sin(th[i]));
xValues.push(xResult);
yValues.push(yResult);
}
function getMaxOfArray(numArray) {
return Math.max.apply(null, numArray);
};
function getMinOfArray(numArray) {
return Math.min.apply(null, numArray);
};
//Shift spiral north so that it is centered
var yShift = (1.6 - (getMaxOfArray(yValues) - getMinOfArray(yValues))) / 2;
var spiralTrace = {
x: xValues.map(function(xi) { return -(xi) + xValues[0]; }),
y: yValues.map(function(yi) { return yi - yValues[0] + yShift; }),
type: 'scatter',
line: {
color: 'white',
width: 3
}
};
//Build the rectangles as a heatmap and specify the edges of the heatmap squares
var phi = (1 + Math.sqrt(5)) / 2;
var xe = [0, 1, (1 + (1 / Math.pow(phi,4))), 1 + (1 / Math.pow(phi,3)), phi];
var ye = [0, (1 / Math.pow(phi,3)), (1 / Math.pow(phi,3)) + (1 / Math.pow(phi,4)), (1 / Math.pow(phi,2)), 1];
var zValues = [
[13, 3, 3, 5],
[13, 2, 1, 5],
[13, 10, 11, 12],
[13, 8, 8, 8]
];
var hm = {
x: xe,
y: ye.map(function(yi) { return yi + yShift; }),
z: zValues,
type: 'heatmap',
colorscale: 'Viridis'
};
var axisTemplate = {
range: [0, 1.6],
autorange: false,
showgrid: false,
zeroline: false,
linecolor: 'black',
showticklabels: false,
ticks: ''
};
var data = [spiralTrace, hm];
var layout = {
title: {
text: 'Heatmap with Unequal Block Sizes'
},
margin: {
t: 200,
r: 200,
b: 200,
l: 200
},
xaxis: axisTemplate,
yaxis: axisTemplate,
showlegend: false,
width: 700,
height: 700,
autosize: false
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make D3.js-based radar charts in Plotly.js.
display\_as: scientific
name: Radar Charts
permalink: javascript/radar-chart/
thumbnail: thumbnail/radar.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","radar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Radar Chart
suite: radar
---
data = [{
type: 'scatterpolar',
r: [39, 28, 8, 7, 28, 39],
theta: ['A','B','C', 'D', 'E', 'A'],
fill: 'toself'
}]
layout = {
polar: {
radialaxis: {
visible: true,
range: [0, 50]
}
},
showlegend: false
}
Plotly.newPlot("myDiv", data, layout)
---
name: Multiple Trace Radar Chart
suite: radar
---
data = [
{
type: 'scatterpolar',
r: [39, 28, 8, 7, 28, 39],
theta: ['A','B','C', 'D', 'E', 'A'],
fill: 'toself',
name: 'Group A'
},
{
type: 'scatterpolar',
r: [1.5, 10, 39, 31, 15, 1.5],
theta: ['A','B','C', 'D', 'E', 'A'],
fill: 'toself',
name: 'Group B'
}
]
layout = {
polar: {
radialaxis: {
visible: true,
range: [0, 50]
}
}
}
Plotly.newPlot("myDiv", data, layout)
---
description: How to make D3.js-based carpet plots in Plotly.js.
display\_as: scientific
name: Carpet Plot
permalink: javascript/carpet-plot/
redirect\_from: javascript/carpet-plots/
thumbnail: thumbnail/carpet.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","carpet" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Set X and Y Coordinates
suite: carpet
description:
---
var data = {
type: 'carpet',
y: [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10]
}
var data = [data]
Plotly.newPlot('myDiv', data);
---
name: Style A and B axis
suite: carpet
description:
---
var trace1 = {
type: "carpet",
a: [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
b: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
y: [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
aaxis: {
tickprefix: 'a = ',
ticksuffix: 'm',
smoothing: 1,
minorgridcount: 9,
minorgridcolor: 'white',
gridcolor: 'white',
color: 'white'
},
baxis: {
tickprefix: 'b = ',
ticksuffix: 'pa',
smoothing: 1,
minorgridcount: 9,
minorgridcolor: 'white',
gridcolor: 'white',
color: 'white'
}
}
var layout = {
plot\_bgcolor: 'black',
paper\_bgcolor: 'black'
}
Plotly.newPlot('myDiv', [trace1], layout)
---
name: Add A and B axis
suite: carpet
description:
---
var data = {
type: 'carpet',
a: [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
b: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
y: [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
aaxis: {
tickprefix: 'a = ',
ticksuffix: 'm',
smoothing: 1,
minorgridcount: 9
},
baxis: {
tickprefix: 'b = ',
ticksuffix: 'Pa',
smoothing: 1,
minorgridcount: 9
}
}
var data = [data]
Plotly.newPlot('myDiv', data);
---
name: Add Parameter Values
suite: carpet
description:
---
var data = {
type: 'carpet',
a: [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
b: [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
y: [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10]
}
var data = [data]
Plotly.newPlot('myDiv', data);
---
name: Add Points and Contours
suite: carpet
description: To add points and lines see [Carpet Scatter Plots](https://plotly.com/javascript/carpet-scatter) or to add contours see [Carpet Contour Plots](https://plotly.com/javascript/carpet-contour)
---
---
name: Categorical Polar Chart
suite: scatterpolar
---
var data = [
{
type: "scatterpolar",
name: "angular categories",
r: [5, 4, 2, 4, 5],
theta: ["a", "b", "c", "d", "a"],
fill: "toself"
},
{
type: "scatterpolar",
name: "radial categories",
r: ["a", "b", "c", "d", "b", "f", "a"],
theta: [1, 4, 2, 1.5, 1.5, 6, 5],
thetaunit: "radians",
fill: "toself",
subplot: "polar2"
},
{
type: "scatterpolar",
name: "angular categories (w/ categoryarray)",
r: [5, 4, 2, 4, 5],
theta: ["a", "b", "c", "d", "a"],
fill: "toself",
subplot: "polar3"
},
{
type: "scatterpolar",
name: "radial categories (w/ category descending)",
r: ["a", "b", "c", "d", "b", "f", "a", "a"],
theta: [45, 90, 180, 200, 300, 15, 20, 45],
fill: "toself",
subplot: "polar4"
},
{
type: "scatterpolar",
name: "angular categories (w/ extra category)",
r: [5, 4, 2, 4, 5, 5],
theta: ["b", "c", "d", "e", "a", "b"],
fill: "toself"
}
]
var layout = {
polar: {
domain: {
x: [0, 0.46],
y: [0.56, 1]
},
radialaxis: {
angle: 45
},
angularaxis: {
direction: "clockwise",
period: 6
}
},
polar2: {
domain: {
x: [0, 0.46],
y: [0, 0.44]
},
radialaxis: {
angle: 180,
tickangle: -180
}
},
polar3: {
domain: {
x: [0.54, 1],
y: [0.56, 1]
},
sector: [150, 400],
radialaxis: {
angle: -45
},
angularaxis: {
categoryarray: ["d", "a", "c", "b"]
}
},
polar4: {
domain: {
x: [0.54, 1],
y: [0, 0.44]
},
radialaxis: {
categoryorder: "category descending"
},
angularaxis: {
thetaunit: "radians",
dtick: 0.3141592653589793
}
}
}
Plotly.newPlot('myDiv', data, layout)
---
name: Webgl Polar Chart
suite: scatterpolar
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/hobbs-pearson-trials.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [
{
type: "scatterpolargl",
r: unpack(rows, 'trial\_1\_r'),
theta: unpack(rows, 'trial\_1\_theta'),
mode: "markers",
name: "Trial 1",
marker: {
color: "rgb(27,158,119)",
size: 15,
line: {
color: "white"
},
opacity: 0.7
},
cliponaxis: false
},
{
type: "scatterpolargl",
r: unpack(rows, "trial\_2\_r"),
theta: unpack(rows, "trial\_2\_theta"),
mode: "markers",
name: "Trial 2",
marker: {
color: "rgb(217,95,2)",
size: 20,
line: {
color: "white"
},
"opacity": 0.7
},
"cliponaxis": false
},
{
type: "scatterpolargl",
r: unpack(rows, "trial\_3\_r"),
theta: unpack(rows, "trial\_3\_theta"),
mode: "markers",
name: "Trial 3",
marker: {
color: "rgb(117,112,179)",
size: 12,
line: {
color: "white"
},
opacity: 0.7
},
cliponaxis: false
},
{
type: "scatterpolargl",
r: unpack(rows, "trial\_4\_r"),
theta: unpack(rows, "trial\_4\_theta"),
mode: "markers",
name: "Trial 4",
marker: {
color: "rgb(231,41,138)",
size: 22,
line: {
color: "white"
},
opacity: 0.7
},
cliponaxis: false
},
{
type: "scatterpolargl",
r: unpack(rows, "trial\_5\_r"),
theta: unpack(rows, "trial\_5\_theta"),
mode: "markers",
name: "Trial 5",
marker: {
color: "rgb(102,166,30)",
size: 19,
line: {
color: "white"
},
opacity: 0.7
},
cliponaxis: false
},
{
type: "scatterpolargl",
r: unpack(rows, "trial\_6\_r"),
theta: unpack(rows, "trial\_6\_theta"),
mode: "markers",
name: "Trial 6",
marker: {
color: "rgb(230,171,2)",
size: 10,
line: {
color: "white"
},
opacity: 0.7
},
cliponaxis: false
}
]
var layout = {
title: {
text: "Hobbs-Pearson Trials"
},
font: {
size: 15
},
showlegend: false,
polar: {
bgcolor: "rgb(223, 223, 223)",
angularaxis: {
tickwidth: 2,
linewidth: 3,
layer: "below traces"
},
radialaxis: {
side: "counterclockwise",
showline: true,
linewidth: 2,
tickwidth: 2,
gridcolor: "white",
gridwidth: 2
}
},
paper\_bgcolor: "rgb(223, 223, 223)",
}
Plotly.newPlot('myDiv', data, layout);
})
---
name: Polar Chart Directions
suite: scatterpolar
---
var data = [
{
type: "scatterpolar",
mode: "lines+markers",
r: [1,2,3,4,5],
theta: [0,90,180,360,0],
line: {
color: "#ff66ab"
},
marker: {
color: "#8090c7",
symbol: "square",
size: 8
},
subplot: "polar"
},
{
type: "scatterpolar",
mode: "lines+markers",
r: [1,2,3,4,5],
theta: [0,90,180,360,0],
line: {
color: "#ff66ab"
},
marker: {
color: "#8090c7",
symbol: "square",
size: 8
},
subplot: "polar2"
}
]
var layout = {
showlegend: false,
polar: {
domain: {
x: [0,0.4],
y: [0,1]
},
radialaxis: {
tickfont: {
size: 8
}
},
angularaxis: {
tickfont: {
size: 8
},
rotation: 90,
direction: "counterclockwise"
}
},
polar2: {
domain: {
x: [0.6,1],
y: [0,1]
},
radialaxis: {
tickfont: {
size: 8
}
},
angularaxis: {
tickfont: {
size: 8
},
direction: "clockwise"
}
}
}
Plotly.newPlot('myDiv', data, layout)
---
name: Polar Chart Subplots
suite: scatterpolar
---
var data = [{
type: "scatterpolargl",
r: [1, 2, 3],
theta: [50, 100, 200],
marker: {symbol: "square"}
}, {
type: "scatterpolargl",
r: [1, 2, 3],
theta: [1, 2, 3],
thetaunit: "radians"
}, {
type: "scatterpolargl",
r: ["a", "b", "c", "b"],
theta: ["D", "C", "B", "A"],
subplot: "polar2"
}, {
type: "scatterpolargl",
r: [50, 300, 900],
theta: [0, 90, 180],
subplot: "polar3"
}, {
type: "scatterpolargl",
mode: "lines",
r: [3, 3, 4, 3],
theta: [0, 45, 90, 270],
fill: "toself",
subplot: "polar4"
}]
var layout = {
polar: {
domain: {
x: [0, 0.46],
y: [0.56, 1]
},
radialaxis: {
range: [1, 4]
},
angularaxis: {
thetaunit: "radians"
}
},
polar2: {
domain: {
x: [0, 0.46],
y: [0, 0.42]
}
},
polar3: {
domain: {
x: [0.54, 1],
y: [0.56, 1]
},
radialaxis: {
type: "log",
tickangle: 45
},
sector: [0, 180]
},
polar4: {
domain: {
x: [0.54, 1],
y: [0, 0.44]
},
radialaxis: {
visible: false,
range: [0, 6]
}
},
showlegend: false
}
Plotly.newPlot('myDiv', data, layout);
---
name: Line Polar Plot
suite: scatterpolar
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/polar\_dataset.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var trace1 = {
r: unpack(rows, 'x1'),
theta: unpack(rows, 'y'),
mode: 'lines',
name: 'Figure8',
line: {color: 'peru'},
type: 'scatterpolar'
};
var trace2 = {
r: unpack(rows, 'x2'),
theta: unpack(rows, 'y'),
mode: 'lines',
name: 'Cardioid',
line: {color: 'darkviolet'},
type: 'scatterpolar'
};
var trace3 = {
r: unpack(rows, 'x3'),
theta: unpack(rows, 'y'),
mode: 'lines',
name: 'Hypercardioid',
line: {color: 'deepskyblue'},
type: 'scatterpolar'
};
var trace4 = {
r: unpack(rows, 'x4'),
theta: unpack(rows, 'y'),
mode: 'lines',
name: 'Subcardioid',
line: {color: 'orangered'},
type: 'scatterpolar'
};
var trace5 = {
r: unpack(rows, 'x5'),
theta: unpack(rows, 'y'),
mode: 'lines',
name: 'Supercardioid',
marker: {
color: 'none',
line: {color: 'green'}
},
type: 'scatterpolar'
};
var data = [trace1, trace2, trace3, trace4, trace5];
var layout = {
title: {
text: 'Mic Patterns'
},
font: {
family: 'Arial, sans-serif;',
size: 12,
color: '#000'
},
showlegend: true,
orientation: -90
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make D3.js-based polar charts in Plotly.js.
display\_as: scientific
name: Polar Charts
order: 12
permalink: javascript/polar-chart/
redirect\_from:
- javascript/legacy-polar-chart/
- javascript-graphing-library/polar-chart/
thumbnail: thumbnail/polar.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","scatterpolar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Area Polar Chart
suite: scatterpolar
---
data = [
{
type: "scatterpolar",
mode: "lines",
r: [0, 1.5, 1.5, 0, 2.5, 2.5, 0],
theta: [0, 10, 25, 0, 205, 215, 0],
fill: "toself",
fillcolor: '#709BFF',
line: {
color: 'black'
}
},
{
type: "scatterpolar",
mode: "lines",
r: [0, 3.5, 3.5, 0],
theta: [0, 55, 75, 0],
fill: "toself",
fillcolor: '#E4FF87',
line: {
color: 'black'
}
},
{
type: "scatterpolar",
mode: "lines",
r: [0, 4.5, 4.5, 0, 4.5, 4.5, 0],
theta: [0, 100, 120, 0, 305, 320, 0],
fill: "toself",
fillcolor: '#FFAA70',
line: {
color: 'black'
}
},
{
type: "scatterpolar",
mode: "lines",
r: [0, 4, 4, 0],
theta: [0, 165, 195, 0],
fill: "toself",
fillcolor: '#FFDF70',
line: {
color: 'black'
}
},
{
type: "scatterpolar",
mode: "lines",
r: [0, 3, 3, 0],
theta: [0, 262.5, 277.5, 0],
fill: "toself",
fillcolor: '#B6FFB4',
line: {
color: 'black'
}
}
]
layout = {
polar: {
radialaxis: {
visible: true,
range: [0, 5]
}
},
showlegend: false
}
Plotly.newPlot('myDiv', data, layout)
---
name: Polar Chart Sector
suite: scatterpolar
---
var data = [
{
type: "scatterpolar",
mode: "lines+markers",
r: [1,2,3,4,5],
theta: [0,90,180,360,0],
line: {
color: "#ff66ab"
},
marker: {
color: "#8090c7",
symbol: "square",
size: 8
},
subplot: "polar"
},
{
type: "scatterpolar",
mode: "lines+markers",
r: [1,2,3,4,5],
theta: [0,90,180,360,0],
line: {
color: "#ff66ab"
},
marker: {
color: "#8090c7",
symbol: "square",
size: 8
},
subplot: "polar2"
}
]
var layout = {
showlegend: false,
polar: {
sector: [145,215],
domain: {
x: [0,0.4],
y: [0,1]
},
radialaxis: {
tickfont: {
size: 8
}
},
angularaxis: {
tickfont: {
size: 8
}
}
},
polar2: {
domain: {
x: [0.6,1],
y: [0,1]
},
radialaxis: {
tickfont: {
size: 8
}
},
angularaxis: {
tickfont: {
size: 8
}
}
}
}
Plotly.newPlot('myDiv', data, layout)
---
name: Basic Ternary Plot with Markers
suite: ternary-plot
description: Inspired from Tom Pearson's [block](http://bl.ocks.org/tomgp/7674234)
---
var rawData = [
{journalist:75,developer:25,designer:0,label:'point 1'},
{journalist:70,developer:10,designer:20,label:'point 2'},
{journalist:75,developer:20,designer:5,label:'point 3'},
{journalist:5,developer:60,designer:35,label:'point 4'},
{journalist:10,developer:80,designer:10,label:'point 5'},
{journalist:10,developer:90,designer:0,label:'point 6'},
{journalist:20,developer:70,designer:10,label:'point 7'},
{journalist:10,developer:20,designer:70,label:'point 8'},
{journalist:15,developer:5,designer:80,label:'point 9'},
{journalist:10,developer:10,designer:80,label:'point 10'},
{journalist:20,developer:10,designer:70,label:'point 11'},
];
Plotly.newPlot('myDiv', [{
type: 'scatterternary',
mode: 'markers',
a: rawData.map(function(d) { return d.journalist; }),
b: rawData.map(function(d) { return d.developer; }),
c: rawData.map(function(d) { return d.designer; }),
text: rawData.map(function(d) { return d.label; }),
marker: {
symbol: 100,
color: '#DB7365',
size: 14,
line: { width: 2 }
},
}], {
ternary: {
sum: 100,
aaxis: makeAxis('Journalist', 0),
baxis: makeAxis('
Developer', 45),
caxis: makeAxis('
Designer', -45),
bgcolor: '#fff1e0'
},
annotations: [{
showarrow: false,
text: 'Replica of Tom Pearson\'s [block](http://bl.ocks.org/tomgp/7674234)',
x: 1.0,
y: 1.3,
font: { size: 15 }
}],
paper\_bgcolor: '#fff1e0',
});
function makeAxis(title, tickangle) {
return {
title: {
text: title,
font: {
size: 20
}
},
tickangle: tickangle,
tickfont: {
size: 15
},
tickcolor: 'rgba(0,0,0,0)',
ticklen: 5,
showline: true,
showgrid: true
};
}
---
name: Soil Types Ternary Plot
suite: ternary-plot
description: Inspired from Daven Quinn's [block](http://bl.ocks.org/davenquinn/988167471993bc2ece29)
---
var url = 'https://gist.githubusercontent.com/davenquinn/988167471993bc2ece29/raw/f38d9cb3dd86e315e237fde5d65e185c39c931c2/data.json';
d3.json(url, function(err, rawData) {
if(err) throw err;
plot(rawData);
});
function plot(rawData) {
var data = Object.keys(rawData).map(function(k) {
var pts = rawData[k];
return {
type: 'scatterternary',
mode: 'lines',
name: k,
a: pts.map(function(d) { return d.clay }),
b: pts.map(function(d) { return d.sand }),
c: pts.map(function(d) { return d.silt }),
line: { color: '#c00' }
};
});
var layout = {
ternary: {
sum: 100,
aaxis: makeAxis('Clay'),
baxis: makeAxis('Sand'),
caxis: makeAxis('Silt')
},
showlegend: false,
width: 700,
annotations: [{
showarrow: false,
text: 'Replica of Daven Quinn\'s [block](http://bl.ocks.org/davenquinn/988167471993bc2ece29)',
x: 0.15,
y: 1.1
}]
};
Plotly.newPlot('myDiv', data, layout);
}
function makeAxis(title) {
return {
title: {
text: title
},
ticksuffix: '%',
min: 0.01,
linewidth: 2,
ticks: 'outside',
ticklen: 8,
showgrid: true,
};
}
---
description: How to create D3.js-based ternary plots. Examples of Ternary Plots with
plotly.
display\_as: scientific
name: Ternary Plots
page\_type: example\_index
permalink: javascript/ternary-plots/
redirect\_from: javascript/ternary-plot/
thumbnail: thumbnail/ternary-plot.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","ternary-plot" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Filled Ternary Plot
suite: ternary-contour
description: Inspired from Daven Quinn's [block](http://bl.ocks.org/davenquinn/988167471993bc2ece29)
---
var url = 'https://gist.githubusercontent.com/davenquinn/988167471993bc2ece29/raw/f38d9cb3dd86e315e237fde5d65e185c39c931c2/data.json';
var colors = ['#8dd3c7','#ffffb3','#bebada','#fb8072','#80b1d3','#fdb462','#b3de69','#fccde5','#d9d9d9','#bc80bd','#ccebc5','#ffed6f'];
d3.json(url, function(err, rawData) {
if(err) throw err;
plot(rawData);
});
function plot(rawData) {
var data = Object.keys(rawData).map(function(k, i) {
var pts = rawData[k];
pts = pts.concat(pts[0]);
return {
type: 'scatterternary',
mode: 'lines',
name: k,
a: pts.map(function(d) { return d.clay }),
b: pts.map(function(d) { return d.sand }),
c: pts.map(function(d) { return d.silt }),
line: { color: '#444' },
fill: 'toself',
fillcolor: colors[i],
hoveron:'fills+points'
};
});
var layout = {
ternary: {
sum: 100,
aaxis: makeAxis('Clay'),
baxis: makeAxis('Sand'),
caxis: makeAxis('Silt')
},
showlegend: false,
width: 700,
annotations: [{
showarrow: false,
text: 'Soil Types Fill Plot',
x: 0.15,
y: 1.1
}]
};
Plotly.newPlot('myDiv', data, layout);
}
function makeAxis(title) {
return {
title: {
text: title
},
ticksuffix: '%',
min: 0.01,
linewidth: 2,
ticks: 'outside',
ticklen: 8,
showgrid: true,
};
}
---
description: How to create D3.js-based ternary contour plots. Examples of Ternary
Contour Plots with plotly.
display\_as: scientific
name: Ternary Contour Plots
permalink: javascript/ternary-contour/
thumbnail: thumbnail/ternary-contour.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","ternary-contour" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Function Reference
permalink: /javascript/plotlyjs-function-reference/
description: Plotly.js function reference. How to create, update, and modify graphs drawn with Plotly's JavaScript Graphing Library.
redirect\_from: /javascript-graphing-library/plotlyjs-function-reference
---

#### [Common parameters](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#common-parameters)

`graphDiv`
:   The functions documented here all create or modify a plot that is drawn into a `<div>` element on the page, commonly referred to as `graphDiv` or `plotDiv`. The first argument to each function on this page is a reference to this element, and it can be either a DOM node, i.e. the output of `document.getElementById()`, or a string, in which case it will be treated as the `id` of the `div`. A note on sizing: You can either supply height and width in the `layout` object (see below), or give the `<div>` a height and width in CSS.

`data`
:   The data to be plotted is described in an array usually called `data`, whose elements are trace objects of various types (e.g. `scatter`, `bar` etc) as documented [in the Full Reference](%7B%7B%20BASE_URL%20%7D%7D/javascript/reference).

`layout`
:   The layout of the plot – non-data-related visual attributes such as the title, annotations etc – is described in an object usually called `layout`, as documented [in/ the Full Reference](%7B%7B%20BASE_URL%20%7D%7D/javascript/reference/layout).

`config`
:   High-level configuration options for the plot, such as the scroll/zoom/hover behaviour, is described in an object usually called `config`, as [documented here](%7B%7B%20BASE_URL%20%7D%7D/javascript/configuration-options). The difference between `config` and `layout` is that `layout` relates to the content of the plot, whereas `config` relates to the context in which the plot is being shown.

`frames`
:   Animation frames are described in an object usually called `frames` as per the [example here](%7B%7B%20BASE_URL%20%7D%7D/javascript/gapminder-example/).
    They can contain `data` and `layout` objects, which define any changes to be animated, and a `traces`
    object that defines which traces to animate. Additionally, frames containing `name` and/or `group`
    attributes can be referenced by [Plotly.animate](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyanimate)
    after they are added by [Plotly.addFrames](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyaddframes)

#### [Plotly.newPlot](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlynewplot)

Draws a new plot in an `<div>` element, *overwriting any existing plot*. To update an existing plot in a `<div>`, it is much more efficient to use [`Plotly.react`](#plotlyreact) than to overwrite it.

Signature

`Plotly.newPlot(graphDiv, data, layout, config)`
:   `graphDiv`
    :   DOM node or string id of a DOM node

    `data`
    :   array of objects, see [documentation](%7B%7B%20BASE_URL%20%7D%7D/javascript/reference)
        (defaults to `[]`)

    `layout`
    :   object, see [documentation](%7B%7B%20BASE_URL%20%7D%7D/javascript/reference/layout)/
        (defaults to `{}`)

    `config`
    :   object, see [documentation](%7B%7B%20BASE_URL%20%7D%7D/javascript/configuration-options)
        (defaults to `{}`)

`Plotly.newPlot(graphDiv, obj)`
:   `graphDiv`
    :   DOM node or string id of a DOM node

    `obj` : single object with keys for `data`, `layout`, `config` and `frames`, see above for contents (defaults to `{data: [], layout: {}, config: {}, frames: []}`)

After plotting, the `data` or `layout` can always be retrieved from the `<div>` element in which the plot was drawn:

```

var graphDiv = document.getElementById('id_of_the_div')

var data = [{
  x: [1999, 2000, 2001, 2002],
  y: [10, 15, 13, 17],
  type: 'scatter'
}];

var layout = {
  title: {
    text: 'Sales Growth'
  },
  xaxis: {
    title: {
      text: 'Year'
    },
    showgrid: false,
    zeroline: false
  },
  yaxis: {
    title: {
      text: 'Percent'
    },
    showline: false
  }
};
Plotly.newPlot(graphDiv, data, layout);

...
var dataRetrievedLater = graphDiv.data;
var layoutRetrievedLater = graphDiv.layout;

```

#### [Plotly.react](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyreact)

`Plotly.react` has the same signature as [`Plotly.newPlot`](#plotlynewplot) above, and can be used in its place to create a plot, but when called again on the same `<div>` will update it far more efficiently than [`Plotly.newPlot`](#plotlynewplot), which would destroy and recreate the plot. `Plotly.react` is as fast as `Plotly.restyle`/`Plotly.relayout` documented below.

Important Note: In order to use this method to plot new items in arrays under `data` such as `x` or `marker.color` etc, these items must either have been added immutably (i.e. the identity of the parent array must have changed) or the value of [`layout.datarevision`](%7B%7B%20BASE_URL%20%7D%7D/javascript/reference/layout/#layout-datarevision) must have changed.

#### [Plotly.restyle](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyrestyle)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

An efficient means of changing attributes in the `data` array in an existing plot. When restyling, you may choose to have the specified changes affect as many traces as desired. The update is given as a single object and the traces that are affected are given as a list of traces indices. Note, leaving the trace indices unspecified assumes that you want to restyle **all** the traces.

Signature

`Plotly.restyle(graphDiv, update [, traceIndices])`
:   `graphDiv`
    :   DOM node or string id of a DOM node

    `update`
    :   object, see below for examples
        (defaults to `{}`)

    `traceIndices`
    :   array of integer indices into existing value of `data`
        (optional, default behaviour is to apply to all traces)

```

// restyle a single trace using attribute strings
var update = {
    opacity: 0.4,
    'marker.color': 'red'
};
Plotly.restyle(graphDiv, update, 0);

// restyle all traces using attribute strings
var update = {
    opacity: 0.4,
    'marker.color': 'red'
};
Plotly.restyle(graphDiv, update);

// restyle two traces using attribute strings
var update = {
    opacity: 0.4,
    'marker.color': 'red'
};
Plotly.restyle(graphDiv, update, [1, 2]);

```

See the Pen [Plotly.restyle](http://codepen.io/plotly/pen/meaKYw/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

The above examples have applied values across single or multiple traces. However, you can also specify **arrays** of values to apply to traces **in turn**.

```

// restyle the first trace's marker color 'red' and the second's 'green'
var update = {
    'marker.color': ['red', 'green']
};
Plotly.restyle(graphDiv, update, [0, 1])

// alternate between red and green for all traces (note omission of traces)
var update = {
    'marker.color': ['red', 'green']
};
Plotly.restyle(graphDiv, update)

```

See the Pen [Plotly.restyle Traces in Turn](http://codepen.io/plotly/pen/NGeBGL/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

In restyle, arrays are assumed to be used in conjunction with the trace indices provided. Therefore, to apply an array **as a value**, you need to wrap it in an additional array. For example:

```

// update the color attribute of the first trace so that the markers within the same trace
// have different colors
var update = {
    'marker.color': [['red', 'green']]
}
Plotly.restyle(graphDiv, update, [0])

// update two traces with new z data
var update = {z: [[[1,2,3], [2,1,2], [1,1,1]], [[0,1,1], [0,2,1], [3,2,1]]]};
Plotly.restyle(graphDiv, update, [1, 2])

```

See the Pen [Plotly.restyle Arrays](http://codepen.io/plotly/pen/wKRxJE/)  by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

The term **attribute strings** is used above to mean **flattened** (e.g., `{marker: {color: 'red'}}` vs. `{'marker.color': red}`). When you pass an attribute string to restyle inside the update object, it’s assumed to mean **update only this attribute**. Therefore, if you wish to replace and entire sub-object, you may simply specify **one less level of nesting**.

```

// replace the entire marker object with the one provided
var update = {
    marker: {color: 'red'}
};
Plotly.restyle(graphDiv, update, [0])

```

See the Pen [Plotly.restyle Attribute strings](http://codepen.io/plotly/pen/LpMBOy/)  by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

Finally, you may wish to selectively reset or ignore certain properties when restyling. This may be useful when specifying multiple properties for multiple traces so that you can carefully target what is and is not affected. In general `null` resets a property to the default while `undefined` applies no change to the current state.

```

// Set the first trace's line to red, the second to the default, and ignore the third
Plotly.restyle(graphDiv, {
  'line.color': ['red', null, undefined]
}, [0, 1, 2])

```

See the Pen [null vs. undefined in Plotly.restyle](http://codepen.io/plotly/pen/XMWRqj/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.relayout](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyrelayout)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

An efficient means of updating the `layout` object of an existing plot. The call signature and arguments for relayout are similar (but simpler) to restyle. Because there are no indices to deal with, arrays need not be wrapped. Also, no argument specifying applicable trace indices is passed in.

Signature

`Plotly.relayout(graphDiv, update)`
:   `graphDiv`
    :   DOM node or string id of a DOM node

    `update`
    :   object, see below for examples
        (defaults to `{}`)

```

// update only values within nested objects
var update = {
    title: {text: 'some new title'}, // updates the title
    'xaxis.range': [0, 5],   // updates the xaxis range
    'yaxis.range[1]': 15     // updates the end of the yaxis range
};
Plotly.relayout(graphDiv, update)

```

See the Pen [Plotly.relayout](http://codepen.io/plotly/pen/meajqx/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.update](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyupdate)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

An efficient means of updating both the `data` array and `layout` object in an existing plot, basically a combination of `Plotly.restyle` and `Plotly.relayout`.

Signature

`Plotly.update(graphDiv, data_update, layout_update, [, traceIndices])`
:   `graphDiv`
    :   DOM node or string id of a DOM node

    `data_update`
    :   object, see `Plotly.restyle` above
        (defaults to `{}`)

    `layout_update`
    :   object, see `Plotly.relayout` above
        (defaults to `{}`)

    `traceIndices`
    :   array of integer indices into existing value of `data`, see `Plotly.restyle` above
        (optional, default behaviour is to apply to all traces)

```

//update the layout and all the traces
var layout_update = {
    title: {text: 'some new title'}, // updates the title
};
var data_update = {
    'marker.color': 'red'
};
Plotly.update(graphDiv, data_update, layout_update)

//update the layout and a single trace
var layout_update = {
    title: {text: 'some new title'}, // updates the title
};
var data_update = {
    'marker.color': 'red'
};
Plotly.update(graphDiv, data_update, layout_update,0)

//update the layout and two specific traces
var layout_update = {
    title: {text: 'some new title'}, // updates the title
};
var data_update = {
    'marker.color': 'red'
};
Plotly.update(graphDiv, data_update, layout_update, [0,2])

```

See the Pen [Plotly.update](http://codepen.io/plotly/pen/PKGrem/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.validate](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyvalidate)

`Plotly.validate` allows users to validate their input `data` array and `layout` object. This can be done on the `data` array and `layout` object passed into `Plotly.newPlot` or on an updated `graphDiv` with `Plotly.validate(graphDiv.data, graphDiv.layout)`.

Signature

`Plotly.validate(data, layout)`
:   `data`
    :   array of objects

        `layout`
        :   object

```

var data = [{
  type: 'bar',
  y: [2, 1, 3, 2],
  orientation: 'horizontal'
}];

var out = Plotly.validate(data, layout);
console.log(out[0].msg)
// "In data trace 0, key orientation is set to an invalid value (horizontal)"

```

#### [Plotly.makeTemplate](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlymaketemplate)

`Plotly.makeTemplate` copies the style information from a figure. It does this by returning a `template` object which can be passed to the `layout.template` attribute of another figure.

Signature

`Plotly.makeTemplate(figure)`
:   `figure` or `DOM Node`
    :   where `figure` is a plot object, with `{data, layout}` members. If a DOM node is used
        it must be a div element already containing a plot.

```

var figure = {
  data: [{
    type: 'bar',
    marker: {color: 'red'},
    y: [2, 1, 3, 2],
  }],
  layout:{
    title: {
      text: 'Quarterly Earnings'
    }
  }
};

var template = Plotly.makeTemplate(figure);

var newData = [{
  type:'bar',
  y:[3,2,5,8]
}]

var layout = {template:template}

Plotly.newPlot(graphDiv,newData,layout)

```

#### [Plotly.validateTemplate](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyvalidatetemplate)

`Plotly.validateTemplate` allows users to Test for consistency between the given figure and a template,
either already included in the figure or given separately. Note that not every issue identified here is necessarily
a problem, it depends on what you're using the template for.

Signature

`Plotly.validateTemplate(figure, template)`
:   `figure` or `DOM Node`
    :   where `figure` is a plot object, with `{data, layout}` members.

        `template`
        :   the template, with its own `{data, layout}`, to test.
            If omitted, we will look for a template already attached as
            the plot's `layout.template` attribute.

```

var out = Plotly.validateTemplate(figure, template);
console.log(out[0].msg)
// "The template has 1 traces of type bar but there are none in the data."

```

#### [Plotly.addTraces](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyaddtraces)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

This allows you to add **new** traces to an existing `graphDiv` at any location in its [data array](#retrieving-data-layout). Every `graphDiv` object has a `data` component which is an array of JSON blobs that each describe one trace. The full list of trace types can be found [in the Full Reference](%7B%7B%20BASE_URL%20%7D%7D/javascript/reference/).

```

// add a single trace to an existing graphDiv
Plotly.addTraces(graphDiv, {y: [2,1,2]});

// add two traces
Plotly.addTraces(graphDiv, [{y: [2,1,2]}, {y: [4, 5, 7]}]);

// add a trace at the beginning of the data array
Plotly.addTraces(graphDiv, {y: [1, 5, 7]}, 0);

```

See the Pen [Plotly.addtraces](http://codepen.io/plotly/pen/xwmJvL/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.deleteTraces](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlydeletetraces)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

This allows you to remove traces from an existing `graphDiv` by specifying the indices of the traces to be removed.

```

// remove the first trace
Plotly.deleteTraces(graphDiv, 0);

// remove the last two traces
Plotly.deleteTraces(graphDiv, [-2, -1]);

```

See the Pen [Plotly.deleteTraces](http://codepen.io/plotly/pen/meaGRo/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.moveTraces](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlymovetraces)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

This allows you to reorder traces in an existing `graphDiv`. This will change the ordering of the layering and the legend.
All traces defined in `graphDiv` are ordered in an array. They are drawn one by one from first to last. Each time a new layer or trace is drawn to the canvas the new trace is drawn directly over the current canvas, replacing the colors of the traces and background. This algorithm to image stacking/drawing is known as the [Painter's Algorithm](https://www.youtube.com/watch?v=oMgOR3PxmDU). As its name implies the Painter's Algorithm is typically the manner in which a painter paints a landscape, starting from objects with the most perspective depth and progressively moving forward and layering over the background objects.

```

// move the first trace (at index 0) the the end of the data array
Plotly.moveTraces(graphDiv, 0);

// move selected traces (at indices [0, 3, 5]) to the end of the data array
Plotly.moveTraces(graphDiv, [0, 3, 5]);

// move last trace (at index -1) to the beginning of the data array (index 0)
Plotly.moveTraces(graphDiv, -1, 0);

// move selected traces (at indices [1, 4, 5]) to new indices [0, 3, 2]
Plotly.moveTraces(graphDiv, [1, 4, 5], [0, 3, 2]);

```

See the Pen [Plotly.moveTraces](http://codepen.io/plotly/pen/LpMJyB/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.extendTraces](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyextendtraces)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

This allows you to add data to traces in an existing `graphDiv`.

```

// extend one trace
Plotly.extendTraces(graphDiv, {y: [[rand()]]}, [0])

// extend multiple traces
Plotly.extendTraces(graphDiv, {y: [[rand()], [rand()]]}, [0, 1])

// extend multiple traces up to a maximum of 10 points per trace
Plotly.extendTraces(graphDiv, {y: [[rand()], [rand()]]}, [0, 1], 10)

```

See the Pen [Plotly.extendTraces](http://codepen.io/plotly/pen/apaoOw/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.prependTraces](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyprependtraces)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

This allows you to prepend data to an existing trace `graphDiv`.

```

// prepend one trace
Plotly.prependTraces(graphDiv, {y: [[rand()]]}, [0])

// prepend multiple traces
Plotly.prependTraces(graphDiv, {y: [[rand()], [rand()]]}, [0, 1])

// prepend multiple traces up to a maximum of 10 points per trace
Plotly.prependTraces(graphDiv, {y: [[rand()], [rand()]]}, [0, 1], 10)

```

#### [Plotly.addFrames](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyaddframes)

*This function has comparable performance to [`Plotly.react`](#plotlyreact) and is faster than redrawing the whole plot with [`Plotly.newPlot`](#plotlynewplot).*

This allows you to add animation frames to a `graphDiv`. The `group` or `name` attribute of a frame can
be used by [Plotly.animate](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyanimate) in place of a frame object (or array of
frame objects).
See [example here](%7B%7B%20BASE_URL%20%7D%7D/javascript/gapminder-example/).

#### [Plotly.animate](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyanimate)

Add dynamic behaviour to plotly graphs with `Plotly.animate`.

Signature

`Plotly.animate(graphDiv, frameOrGroupNameOrFrameList, animationAttributes)`
:   `graphDiv`
    :   DOM node or string id of a DOM node

    `frameOrGroupNameOrFrameList`
    :   A frame to be animated or an array of frames to be animated in sequence. Frames added by
        [Plotly.addFrames](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlyaddframes) which have a
        `group` attribute, can be animated by passing their group name here.
        Similarly, you can reference frames by an array of strings of frame `name` values.

    `animationAttributes`
    :   An object, see [documentation](%7B%7B%20BASE_URL%20%7D%7D/javascript/animations) for examples.

```

Plotly.newPlot('graph', [{
  x: [1, 2, 3],
  y: [0, 0.5, 1],
  line: {simplify: false},
}]);

function randomize() {
  Plotly.animate('graph', {
    data: [{y: [Math.random(), Math.random(), Math.random()]}],
    traces: [0],
    layout: {}
  }, {
    transition: {
      duration: 500,
      easing: 'cubic-in-out'
    },
	  frame: {
		  duration: 500
	  }
  })
}

```

See the Pen [Plotly.animate](http://codepen.io/plotly/pen/ZpWPpj/) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.purge](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlypurge)

Using `purge` will clear the div, and remove any Plotly plots that have been placed in it.

```

// purge will be used on the div that you wish clear of Plotly plots
Plotly.purge(graphDiv);

```

See the Pen [Plotly.purge](http://codepen.io/plotly/pen/xOVpeb) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.toImage](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlytoimage)

`toImage` will generate a promise to an image of the plot in data URL format.

```

// Plotly.toImage will turn the plot in the given div into a data URL string
// toImage takes the div as the first argument and an object specifying image properties as the other
Plotly.toImage(graphDiv, {format: 'png', width: 800, height: 600}).then(function(dataUrl) {
    // use the dataUrl
})

```

See the Pen [Plotly.toImage](http://codepen.io/plotly/pen/mEPxyQ) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Plotly.downloadImage](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#plotlydownloadimage)

`downloadImage` will trigger a request to download the image of a Plotly plot.

```

// downloadImage will accept the div as the first argument and an object specifying image properties as the other
Plotly.downloadImage(graphDiv, {format: 'png', width: 800, height: 600, filename: 'newplot'});

```

See the Pen [Plotly.toImage](http://codepen.io/plotly/pen/jrqzar) by plotly ([@plotly](http://codepen.io/plotly)) on [CodePen](http://codepen.io).

#### [Using events](%7B%7B%20BASE_URL%20%7D%7D/javascript/plotlyjs-function-reference/#using-events)

Plots emit events prefixed with `plotly_` when clicked or hovered over, and event handlers can be bound to events using the `on` method that is exposed by the plot div object. For more information and examples of how to use Plotly events see: <https://plotly.com/javascript/plotlyjs-events/>.
---
name: Customizing the Figure with Shapes and Annotations
suite: ohlc
---
var trace1 = {
x: ['2017-01-17', '2017-01-18', '2017-01-19', '2017-01-20', '2017-01-23', '2017-01-24', '2017-01-25', '2017-01-26', '2017-01-27', '2017-01-30', '2017-01-31', '2017-02-01', '2017-02-02', '2017-02-03', '2017-02-06', '2017-02-07', '2017-02-08', '2017-02-09', '2017-02-10'],
close: [120, 119.989998, 119.779999, 120, 120.080002, 119.970001, 121.879997, 121.940002, 121.949997, 121.629997, 121.349998, 128.75, 128.529999, 129.080002, 130.289993, 131.529999, 132.039993, 132.419998, 132.119995],
decreasing: {line: {color: '#7F7F7F'}},
high: [120.239998, 120.5, 120.089996, 120.449997, 120.809998, 120.099998, 122.099998, 122.440002, 122.349998, 121.629997, 121.389999, 130.490005, 129.389999, 129.190002, 130.5, 132.089996, 132.220001, 132.449997, 132.940002],
increasing: {line: {color: '#17BECF'}},
line: {color: 'rgba(31,119,180,1)'},
low: [118.220001, 119.709999, 119.370003, 119.730003, 119.769997, 119.5, 120.279999, 121.599998, 121.599998, 120.660004, 120.620003, 127.010002,
127.779999, 128.160004, 128.899994, 130.449997, 131.220001, 131.119995, 132.050003],
open: [118.339996, 120, 119.400002, 120.449997, 120, 119.550003, 120.419998, 121.669998, 122.139999, 120.93, 121.150002, 127.029999, 127.980003, 128.309998, 129.130005, 130.539993, 131.350006, 131.649994, 132.460007],
type: 'ohlc',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace1];
var layout = {
dragmode: 'zoom',
margin: {
r: 10,
t: 25,
b: 40,
l: 60
},
showlegend: false,
xaxis: {
autorange: true,
rangeslider: {range: ['2017-01-17 12:00', '2017-02-10 12:00']},
title: {
text: 'Date'
},
type: 'date'
},
yaxis: {
autorange: true,
type: 'linear'
},
annotations: [
{
x: '2017-01-31',
y: 0.9,
xref: 'x',
yref: 'paper',
text: 'largest movement',
font: {color: 'magenta'},
showarrow: true,
xanchor: 'right',
ax: -20,
ay: 0
}
],
shapes: [
{
type: 'rect',
xref: 'x',
yref: 'paper',
x0: '2017-01-31',
y0: 0,
x1: '2017-02-01',
y1: 1,
fillcolor: '#d3d3d3',
opacity: 0.2,
line: {
width: 0
}
}
]
};
Plotly.newPlot('myDiv', data, layout);
---
name: OHLC Chart without Rangeslider
suite: ohlc
order: 1.5
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var trace = {
x: unpack(rows, 'Date'),
close: unpack(rows, 'AAPL.Close'),
high: unpack(rows, 'AAPL.High'),
low: unpack(rows, 'AAPL.Low'),
open: unpack(rows, 'AAPL.Open'),
// cutomise colors
increasing: {line: {color: 'black'}},
decreasing: {line: {color: 'red'}},
type: 'ohlc',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace];
var layout = {
dragmode: 'zoom',
showlegend: false,
xaxis: {
rangeslider: {
visible: false
}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Simple OHLC Chart
suite: ohlc
---
var trace1 = {
x: ['2017-01-17', '2017-01-18', '2017-01-19', '2017-01-20', '2017-01-23', '2017-01-24', '2017-01-25', '2017-01-26', '2017-01-27', '2017-01-30', '2017-01-31', '2017-02-01', '2017-02-02', '2017-02-03', '2017-02-06', '2017-02-07', '2017-02-08', '2017-02-09', '2017-02-10'],
close: [120, 119.989998, 119.779999, 120, 120.080002, 119.970001, 121.879997, 121.940002, 121.949997, 121.629997, 121.349998, 128.75, 128.529999, 129.080002, 130.289993, 131.529999, 132.039993, 132.419998, 132.119995],
decreasing: {line: {color: '#7F7F7F'}},
high: [120.239998, 120.5, 120.089996, 120.449997, 120.809998, 120.099998, 122.099998, 122.440002, 122.349998, 121.629997, 121.389999, 130.490005, 129.389999, 129.190002, 130.5, 132.089996, 132.220001, 132.449997, 132.940002],
increasing: {line: {color: '#17BECF'}},
line: {color: 'rgba(31,119,180,1)'},
low: [118.220001, 119.709999, 119.370003, 119.730003, 119.769997, 119.5, 120.279999, 121.599998, 121.599998, 120.660004, 120.620003, 127.010002, 127.779999, 128.160004, 128.899994, 130.449997, 131.220001, 131.119995, 132.050003],
open: [118.339996, 120, 119.400002, 120.449997, 120, 119.550003, 120.419998, 121.669998, 122.139999, 120.93, 121.150002, 127.029999, 127.980003, 128.309998, 129.130005, 130.539993, 131.350006, 131.649994, 132.460007],
type: 'ohlc',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace1];
var layout = {
dragmode: 'zoom',
margin: {
r: 10,
t: 25,
b: 40,
l: 60
},
showlegend: false,
xaxis: {
autorange: true,
rangeslider: {range: ['2017-01-17 12:00', '2017-02-10 12:00']},
title: {
text: 'Date'
},
type: 'date'
},
yaxis: {
autorange: true,
type: 'linear'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Customise OHLC Chart Colors
suite: ohlc
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var trace = {
x: unpack(rows, 'Date'),
close: unpack(rows, 'AAPL.Close'),
high: unpack(rows, 'AAPL.High'),
low: unpack(rows, 'AAPL.Low'),
open: unpack(rows, 'AAPL.Open'),
// cutomise colors
increasing: {line: {color: 'black'}},
decreasing: {line: {color: 'red'}},
type: 'ohlc',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace];
var layout = {
dragmode: 'zoom',
showlegend: false,
xaxis: {
autorange: true,
title: {
text: 'Date'
},
},
yaxis: {
autorange: true,
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Add Rangeselector
suite: ohlc
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var trace = {
x: unpack(rows, 'Date'),
close: unpack(rows, 'AAPL.Close'),
high: unpack(rows, 'AAPL.High'),
low: unpack(rows, 'AAPL.Low'),
open: unpack(rows, 'AAPL.Open'),
// cutomise colors
increasing: {line: {color: 'black'}},
decreasing: {line: {color: 'red'}},
type: 'ohlc',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace];
var layout = {
dragmode: 'zoom',
showlegend: false,
xaxis: {
autorange: true,
title: {
text: 'Date'
},
rangeselector: {
x: 0,
y: 1.2,
xanchor: 'left',
font: {size:8},
buttons: [{
step: 'month',
stepmode: 'backward',
count: 1,
label: '1 month'
}, {
step: 'month',
stepmode: 'backward',
count: 6,
label: '6 months'
}, {
step: 'all',
label: 'All dates'
}]
}
},
yaxis: {
autorange: true,
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to graph D3.js-based OHLC charts in javascript. Examples of OHCL
charts.
display\_as: financial
name: OHLC Charts
permalink: javascript/ohlc-charts/
thumbnail: thumbnail/ohlc.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","ohlc" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Horizontal Waterfall Chart
suite: waterfall
---
var gd = document.getElementById('myDiv');
var data = [
{
name: "2018",
type: "waterfall",
orientation: "h",
measure: [
"relative",
"relative",
"relative",
"relative",
"total",
"relative",
"relative",
"relative",
"relative",
"total",
"relative",
"relative",
"total",
"relative",
"total"
],
y: [
"Sales",
"Consulting",
"Maintenance",
"Other revenue",
"Net revenue",
"Purchases",
"Material expenses",
"Personnel expenses",
"Other expenses",
"Operating profit",
"Investment income",
"Financial income",
"Profit before tax",
"Income tax (15%)",
"Profit after tax"
],
x: [
375,
128,
78,
27,
null,
-327,
-12,
-78,
-12,
null,
32,
89,
null,
-45,
null
],
connector: {
mode: "between",
line: {
width: 4,
color: "rgb(0, 0, 0)",
dash: 0
}
}
}
];
var layout = {title: {
text: "Profit and loss statement 2018
waterfall chart displaying positive and negative"
},
yaxis: {
type: "category",
autorange: "reversed"
},
xaxis: {
type: "linear"
},
margin: { l: 150 },
showlegend: true
}
Plotly.newPlot('myDiv', data, layout);
---
name: Style Waterfall Chart
suite: waterfall
---
var gd = document.getElementById('myDiv');
var data = [
{
type: "waterfall",
x: [
["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total" ]
],
measure: ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
y: [10, 20, 30, -10, null, 10, 20, -40, null],
base: 300,
decreasing: { marker: { color: "Maroon" , line:{color : "red", width :2}}},
increasing: { marker: { color: "Teal"} },
totals: { marker: { color: "deep sky blue", line:{color:'blue',width:3}} }
}];
var layout = {title: {
text: "Profit and loss statement"
},
waterfallgap : 0.3,
xaxis: {
title: { text: ""},
tickfont: {size: 15},
ticks: "outside"
}
}
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based waterfall chart in javascript.
display\_as: financial
name: Waterfall Charts
page\_type: example\_index
permalink: javascript/waterfall-charts/
thumbnail: thumbnail/waterfall-charts.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","waterfall" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Waterfall Chart
suite: waterfall
---
var data = [
{
name: "2018",
type: "waterfall",
orientation: "v",
measure: [
"relative",
"relative",
"total",
"relative",
"relative",
"total"
],
x: [
"Sales",
"Consulting",
"Net revenue",
"Purchases",
"Other expenses",
"Profit before tax"
],
textposition: "outside",
text: [
"+60",
"+80",
"",
"-40",
"-20",
"Total"
],
y: [
60,
80,
0,
-40,
-20,
0
],
connector: {
line: {
color: "rgb(63, 63, 63)"
}
},
}
];
layout = {
title: {
text: "Profit and loss statement 2018"
},
xaxis: {
type: "category"
},
yaxis: {
type: "linear"
},
autosize: true,
showlegend: true
};
Plotly.newPlot('myDiv', data, layout);
---
name: Multi Category Waterfall Chart
suite: waterfall
---
var gd = document.getElementById('myDiv');
var data = [
{
type: "waterfall",
x: [
["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total" ]
],
measure: ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
y: [1, 2, 3, -1, null, 1, 2, -4, null],
base: 1000
},
{
type: "waterfall",
x: [
["2016", "2017", "2017", "2017", "2017", "2018", "2018", "2018", "2018"],
["initial", "q1", "q2", "q3", "total", "q1", "q2", "q3", "total" ]
],
measure: ["absolute", "relative", "relative", "relative", "total", "relative", "relative", "relative", "total"],
y: [1.1, 2.2, 3.3, -1.1, null, 1.1, 2.2, -4.4, null],
base: 1000
}
];
var layout = {
waterfallgroupgap : 0.5,
xaxis: {
title: {
text: "MULTI-CATEGORY",
},
tickfont: {size: 16},
ticks: "outside"
}
}
Plotly.newPlot('myDiv', data, layout);
---
name: Overview
suite: indicator
markdown\_content: |
In this tutorial we introduce a new trace named "Indicator". The purpose of "indicator" is to visualize a single value specified by the "value" attribute.
Three distinct visual elements are available to represent that value: number, delta and gauge. Any combination of them can be specified via the "mode" attribute.
Top-level attributes are:

1. value: the value to visualize
2. mode: which visual elements to draw
3. align: how to align number and delta (left, center, right)
4. domain: the extent of the figure

Then we can configure the 3 different visual elements via their respective container:

1. number is simply a representation of the number in text. It has attributes:- valueformat: to format the number
   - prefix: a string before the number
   - suffix: a string after the number
   - font.(family|size): to control the font

"delta" simply displays the difference between the value with respect to a reference. It has attributes:

1. reference: the number to compare the value with
2. relative: whether that difference is absolute or relative
3. valueformat: to format the delta
4. (increasing|decreasing).color: color to be used for positive or decreasing delta
5. (increasing|decreasing).symbol: symbol displayed on the left of the delta
6. font.(family|size): to control the font
7. position: position relative to `number` (either top, left, bottom, right)

Finally, we can have a simple title for the indicator via `title` with 'text' attribute which is a string, and 'align' which can be set to left, center, and right.
There are two gauge types: [angular](https://plotly.com/javascript/gauge-charts/) and [bullet](https://plotly.com/javascript/bullet-charts/). Here is a combination of both shapes (angular, bullet), and different modes (guage, delta, and value):
---
var data = [
{
type: "indicator",
value: 200,
delta: { reference: 160 },
gauge: { axis: { visible: false, range: [0, 250] } },
domain: { row: 0, column: 0 }
},
{
type: "indicator",
value: 120,
gauge: {
shape: "bullet",
axis: {
visible: false,
range: [-200, 200]
}
},
domain: { x: [0.1, 0.5], y: [0.15, 0.35] }
},
{
type: "indicator",
mode: "number+delta",
value: 300,
domain: { row: 0, column: 1 }
},
{ type: "indicator", mode: "delta", value: 40, domain: { row: 1, column: 1 } }
];
var layout = {
width: 600,
height: 400,
margin: { t: 25, b: 25, l: 25, r: 25 },
grid: { rows: 2, columns: 2, pattern: "independent" },
template: {
data: {
indicator: [
{
title: { text: "Speed" },
mode: "number+delta+gauge",
delta: { reference: 90 }
}
]
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: A Single Angular Gauge Chart
suite: indicator
markdown\_content: |
---
var data = [
{
domain: { x: [0, 1], y: [0, 1] },
value: 450,
title: { text: "Speed" },
type: "indicator",
mode: "gauge+number",
delta: { reference: 400 },
gauge: { axis: { range: [null, 500] } }
}
];
var layout = { width: 600, height: 400 };
Plotly.newPlot('myDiv', data, layout);
---
name:
suite: indicator
markdown\_content: |
It's possible to display several numbers
---
var data = [
{
type: "indicator",
mode: "number+delta",
value: 200,
domain: { x: [0, 0.5], y: [0, 0.5] },
delta: { reference: 400, relative: true, position: "top" }
},
{
type: "indicator",
mode: "number+delta",
value: 350,
delta: { reference: 400, relative: true },
domain: { x: [0, 0.5], y: [0.5, 1] }
},
{
type: "indicator",
mode: "number+delta",
value: 450,
title: {
text:
"Accounts
Subtitle
Subsubtitle"
},
delta: { reference: 400, relative: true },
domain: { x: [0.6, 1], y: [0, 1] }
}
];
var layout = {
width: 600,
height: 400,
margin: { t: 25, r: 25, l: 25, b: 25 }
};
Plotly.newPlot('myDiv', data, layout);
---
name: Bullet Gauge
suite: indicator
markdown\_content: |
The equivalent of above "angular gauge":
---
var data = [
{
type: "indicator",
mode: "number+gauge+delta",
gauge: { shape: "bullet" },
delta: { reference: 300 },
value: 220,
domain: { x: [0, 1], y: [0, 1] },
title: { text: "Profit" }
}
];
var layout = { width: 600, height: 250 };
Plotly.newPlot('myDiv', data, layout);
---
name: Showing Information above Your Chart
suite: indicator
markdown\_content: |
Another interesting feature is that indicator trace sits above the other traces (even the 3d ones). This way, it can be easily used as an overlay as demonstrated below:
---
var data = [
{
type: "indicator",
mode: "number+delta",
value: 492,
delta: { reference: 512, valueformat: ".0f" },
domain: { y: [0, 1], x: [0.25, 0.75] },
title: { text: "Users online" }
},
{
y: [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]
}
];
var layout = { width: 600, height: 450, xaxis: { range: [0, 62] } };
Plotly.newPlot('myDiv', data, layout);
---
name: Data Cards / Big Numbers
suite: indicator
order: 4.1
markdown\_content: |
Data card helps to display more contextual information about the data. Sometimes one number is all you want to see in a report, such as total sales, annual revenue, etc. This example shows how to visualize these big numbers:
---
var data = [
{
type: "indicator",
mode: "number+delta",
value: 400,
number: { prefix: "$" },
delta: { position: "top", reference: 320 },
domain: { x: [0, 1], y: [0, 1] }
}
];
var layout = {
paper\_bgcolor: "lightgray",
width: 600,
height: 200,
margin: { t: 0, b: 0, l: 0, r: 0 }
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based gauge chart in javascript.
display\_as: financial
name: Indicators
page\_type: example\_index
permalink: javascript/indicator/
thumbnail: thumbnail/indicator.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","indicator" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Bullet Charts
suite: bullet-charts
markdown\_content: |
Stephen Few's Bullet Chart was invented to replace dashboard [gauges](https://plotly.com/javascript/gauge-charts/) and meters, combining both types of charts into simple bar charts with qualitative bars (steps), quantitative bar (bar) and performance line (threshold); all into one simple layout.
Steps typically are broken into several values, which are defined with an array. The bar represent the actual value that a particular variable reached, and the threshold usually indicate a goal point relative to the value achieved by the bar. See [indicator page](https://plotly.com/javascript/gauge-charts/) for more detail.
---
var data = [
{
type: "indicator",
mode: "number+gauge+delta",
gauge: { shape: "bullet" },
delta: { reference: 300 },
value: 220,
domain: { x: [0, 1], y: [0, 1] },
title: { text: "Profit" }
}
];
var layout = { width: 600, height: 250 };
Plotly.newPlot('myDiv', data, layout);
---
name: Add Steps, and Threshold
suite: bullet-charts
markdown\_content: |
Below is the same example using "steps" attribute, which is shown as shading, and "threshold" to determine boundaries that visually alert you if the value cross a defined threshold.
---
var data = [
{
type: "indicator",
mode: "number+gauge+delta",
value: 220,
domain: { x: [0, 1], y: [0, 1] },
title: {
text: "**Profit**"
},
delta: { reference: 200 },
gauge: {
shape: "bullet",
axis: { range: [null, 300] },
threshold: {
line: { color: "red", width: 2 },
thickness: 0.75,
value: 280
},
steps: [
{ range: [0, 150], color: "lightgray" },
{ range: [150, 250], color: "gray" }
]
}
}
];
var layout = { width: 600, height: 250 };
var config = { responsive: true };
Plotly.newPlot('myDiv', data, layout, config);
---
name: Custom Bullet Chart
suite: bullet-charts
markdown\_content: |
The following example shows how to customize your charts. For more information about all possible options check our [reference page](https://plotly.com/javascript/reference/indicator/).
---
var data = [
{
type: "indicator",
mode: "number+gauge+delta",
value: 220,
domain: { x: [0, 1], y: [0, 1] },
delta: { reference: 280, position: "top" },
title: {
text:
"**Profit**
U.S. $",
font: { size: 14 }
},
gauge: {
shape: "bullet",
axis: { range: [null, 300] },
threshold: {
line: { color: "red", width: 2, gradient: { yanchor: "vertical" } },
thickness: 0.75,
value: 270
},
bgcolor: "white",
steps: [{ range: [0, 150], color: "cyan" }],
bar: { color: "darkblue" }
}
}
];
var layout = { width: 400, height: 230 };
var config = { responsive: true };
Plotly.newPlot('myDiv', data, layout, config);
---
description: How to make a D3.js-based bullet chart in javascript.
display\_as: financial
name: Bullet Charts
permalink: javascript/bullet-charts/
redirect\_from: javascript-graphing-library/bullet-charts
thumbnail: thumbnail/bullet.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","bullet-charts" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Multi Bullet
suite: bullet-charts
markdown\_content: |
Bullet charts can be stacked for comparing several values at once as illustrated below:
---
var data = [
{
type: "indicator",
mode: "number+gauge+delta",
value: 180,
delta: { reference: 200 },
domain: { x: [0.25, 1], y: [0.08, 0.25] },
title: { text: "Revenue" },
gauge: {
shape: "bullet",
axis: { range: [null, 300] },
threshold: {
line: { color: "black", width: 2 },
thickness: 0.75,
value: 170
},
steps: [
{ range: [0, 150], color: "gray" },
{
range: [150, 250],
color: "lightgray"
}
],
bar: { color: "black" }
}
},
{
type: "indicator",
mode: "number+gauge+delta",
value: 35,
delta: { reference: 200 },
domain: { x: [0.25, 1], y: [0.4, 0.6] },
title: { text: "Profit" },
gauge: {
shape: "bullet",
axis: { range: [null, 100] },
threshold: {
line: { color: "black", width: 2 },
thickness: 0.75,
value: 50
},
steps: [
{ range: [0, 25], color: "gray" },
{ range: [25, 75], color: "lightgray" }
],
bar: { color: "black" }
}
},
{
type: "indicator",
mode: "number+gauge+delta",
value: 220,
delta: { reference: 200 },
domain: { x: [0.25, 1], y: [0.7, 0.9] },
title: { text: "Satisfaction" },
gauge: {
shape: "bullet",
axis: { range: [null, 300] },
threshold: {
line: { color: "black", width: 2 },
thickness: 0.75,
value: 210
},
steps: [
{ range: [0, 150], color: "gray" },
{ range: [150, 250], color: "lightgray" }
],
bar: { color: "black" }
}
}
];
var layout = {
width: 600, height: 250,
margin: { t: 10, r: 25, l: 25, b: 10 }
};
Plotly.newPlot('myDiv', data, layout);
---
name: Funnelarea Plot
suite: funnel
---
var gd = document.getElementById('myDiv');
var data = [{type: 'funnelarea', values: [5, 4, 3, 2, 1], text: ["The 1st", "The 2nd", "The 3rd", "The 4th", "The 5th"],
marker: {colors: ["59D4E8", "DDB6C6", "A696C8", "67EACA", "94D2E6"],
line: {color: ["3E4E88", "606470", "3E4E88", "606470", "3E4E88"], width: [2, 1, 5, 0, 3]}},
textfont: {family: "Old Standard TT", size: 13, color: "black"}, opacity: 0.65}];
var layout = {margin: {l: 200 , r: 200}, funnelmode: "stack", showlegend: 'True'}
Plotly.newPlot('myDiv', data, layout);
---
name: Stacked Funnel
suite: funnel
---
var gd = document.getElementById('myDiv');
var data = [{type: 'funnel', name: 'Montreal',
y: ["Website visit", "Downloads", "Potential customers", "Requested price"],
x: [120, 60, 30, 20],
textinfo: "value+percent initial"},
{
type: 'funnel',name: 'Toronto',
y: ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"],
x: [100, 60, 40, 30, 20], textposition: "inside", textinfo: "value+percent previous"},
{
type: 'funnel',name: 'Vancouver',
y: ["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent", "closed deals"],
x: [90, 70, 50, 30, 10, 5], textposition: "outside", textinfo: "value+percent total"}];
var layout = {margin: {l: 130, r: 0}, width: 600, funnelmode: "stack", showlegend: 'true'}
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based funnel chart in javascript.
display\_as: financial
name: Funnel and Funnelarea Charts
page\_type: example\_index
permalink: javascript/funnel-charts/
thumbnail: thumbnail/funnel.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","funnel" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Funnel Plot
suite: funnel
---
var gd = document.getElementById('myDiv');
var data = [{type: 'funnel', y: ["Website visit", "Downloads", "Potential customers", "Invoice sent", "Closed delas"], x: [13873, 10533, 5443, 2703, 908], hoverinfo: 'x+percent previous+percent initial'}];
var layout = {margin: {l: 150}, width:600, height: 500}
Plotly.newPlot('myDiv', data, layout);
---
name: Setting Marker Size and Color
suite: funnel
---
var gd = document.getElementById('myDiv');
var data = [{type: 'funnel',
y: ["Sales person A", "Sales person B", "Sales person C", "Sales person D", "Sales person E"],
x: [1200, 909.4, 600.6, 300, 80], textposition: "inside", textinfo: "value+percent initial",
hoverinfo: 'percent total+x', opacity: 0.65, marker: {color: ["59D4E8", "DDB6C6", "A696C8", "67EACA", "94D2E6"],
line: {"width": [4, 2, 2, 3, 1, 1], color: ["3E4E88", "606470", "3E4E88", "606470", "3E4E88"]}},
connector: {line: {color: "royalblue", dash: "dot", width: 3}}}];
var layout = {margin: {l: 100}, width: 600, height: 500}
Plotly.newPlot('myDiv', data, layout);
---
name: Multi Funnelarea
suite: funnel
---
var gd = document.getElementById('myDiv');
var data = [{type: 'funnelarea', scalegroup: "first", values: [500, 450, 340, 230, 220, 110],
textinfo: "value", title: {position: "top center", text: "Sales for Sale Person A in U.S."},
domain: {x: [0, 0.5], y: [0, 0.5]}},
{
type: 'funnelarea', scalegroup: "first", values: [600, 500, 400, 300, 200, 100], textinfo: "value",
title: {position: "top center", text: "Sales of Sale Person B in Canada"},
domain: {x: [0, 0.5], y: [0.55, 1]}},
{
type:'funnelarea', scalegroup: "second", values: [510, 480, 440, 330, 220, 100], textinfo: "value",
title: {position: "top left", text: "Sales of Sale Person A in Canada"},
domain: {x: [0.55, 1], y: [0, 0.5]}},
{
type: 'funnelarea', scalegroup: "second", values: [360, 250, 240, 130, 120, 60],
textinfo: "value", title: {position: "top left", text: "Sales of Sale Person B in U.S."},
domain: {x: [0.55, 1], y: [0.55, 1]}}];
var layout = {width: 600,shapes: [
{x0: 0, x1: 0.5, y0: 0, y1: 0.5},
{x0: 0, x1: 0.5, y0: 0.55, y1: 1},
{x0: 0.55, x1: 1, y0: 0, y1: 0.5},
{x0: 0.55, x1: 1, y0: 0.55, y1: 1}]}
Plotly.newPlot('myDiv', data, layout);
---
name: Candlestick Chart without Rangeslider
suite: candlestick
order: 1.5
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var trace = {
x: unpack(rows, 'Date'),
close: unpack(rows, 'AAPL.Close'),
high: unpack(rows, 'AAPL.High'),
low: unpack(rows, 'AAPL.Low'),
open: unpack(rows, 'AAPL.Open'),
// cutomise colors
increasing: {line: {color: 'black'}},
decreasing: {line: {color: 'red'}},
type: 'candlestick',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace];
var layout = {
dragmode: 'zoom',
showlegend: false,
xaxis: {
rangeslider: {
visible: false
}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Customizing Candlestick Chart Colors
suite: candlestick
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var trace = {
x: unpack(rows, 'Date'),
close: unpack(rows, 'AAPL.Close'),
high: unpack(rows, 'AAPL.High'),
low: unpack(rows, 'AAPL.Low'),
open: unpack(rows, 'AAPL.Open'),
// cutomise colors
increasing: {line: {color: 'black'}},
decreasing: {line: {color: 'red'}},
type: 'candlestick',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace];
var layout = {
dragmode: 'zoom',
showlegend: false,
xaxis: {
title: {
text: 'Date'
},
range: ['2016-06-01 12:00', '2017-01-01 12:00']
},
yaxis: {
autorange: true,
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Simple Candlestick Chart
suite: candlestick
---
var trace1 = {
x: ['2017-01-04', '2017-01-05', '2017-01-06', '2017-01-09', '2017-01-10', '2017-01-11', '2017-01-12', '2017-01-13', '2017-01-17', '2017-01-18', '2017-01-19', '2017-01-20', '2017-01-23', '2017-01-24', '2017-01-25', '2017-01-26', '2017-01-27', '2017-01-30', '2017-01-31', '2017-02-01', '2017-02-02', '2017-02-03', '2017-02-06', '2017-02-07', '2017-02-08', '2017-02-09', '2017-02-10', '2017-02-13', '2017-02-14', '2017-02-15'],
close: [116.019997, 116.610001, 117.910004, 118.989998, 119.110001, 119.75, 119.25, 119.040001, 120, 119.989998, 119.779999, 120, 120.080002, 119.970001, 121.879997, 121.940002, 121.949997, 121.629997, 121.349998, 128.75, 128.529999, 129.080002, 130.289993, 131.529999, 132.039993, 132.419998, 132.119995, 133.289993, 135.020004, 135.509995],
decreasing: {line: {color: '#7F7F7F'}},
high: [116.510002, 116.860001, 118.160004, 119.43, 119.379997, 119.93, 119.300003, 119.620003, 120.239998, 120.5, 120.089996, 120.449997, 120.809998, 120.099998, 122.099998, 122.440002, 122.349998, 121.629997, 121.389999, 130.490005, 129.389999, 129.190002, 130.5, 132.089996, 132.220001, 132.449997, 132.940002, 133.820007, 135.089996, 136.270004],
increasing: {line: {color: '#17BECF'}},
line: {color: 'rgba(31,119,180,1)'},
low: [115.75, 115.809998, 116.470001, 117.940002, 118.300003, 118.599998, 118.209999, 118.809998, 118.220001, 119.709999, 119.370003, 119.730003, 119.769997, 119.5, 120.279999, 121.599998, 121.599998, 120.660004, 120.620003, 127.010002, 127.779999, 128.160004, 128.899994, 130.449997, 131.220001, 131.119995, 132.050003, 132.75, 133.25, 134.619995],
open: [115.849998, 115.919998, 116.779999, 117.949997, 118.769997, 118.739998, 118.900002, 119.110001, 118.339996, 120, 119.400002, 120.449997, 120, 119.550003, 120.419998, 121.669998, 122.139999, 120.93, 121.150002, 127.029999, 127.980003, 128.309998, 129.130005, 130.539993, 131.350006, 131.649994, 132.460007, 133.080002, 133.470001, 135.520004],
type: 'candlestick',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace1];
var layout = {
dragmode: 'zoom',
margin: {
r: 10,
t: 25,
b: 40,
l: 60
},
showlegend: false,
xaxis: {
autorange: true,
domain: [0, 1],
range: ['2017-01-03 12:00', '2017-02-15 12:00'],
rangeslider: {range: ['2017-01-03 12:00', '2017-02-15 12:00']},
title: {
text: 'Date'
},
type: 'date'
},
yaxis: {
autorange: true,
domain: [0, 1],
range: [114.609999778, 137.410004222],
type: 'linear'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Add Rangeselector
suite: candlestick
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var trace = {
x: unpack(rows, 'Date'),
close: unpack(rows, 'AAPL.Close'),
high: unpack(rows, 'AAPL.High'),
low: unpack(rows, 'AAPL.Low'),
open: unpack(rows, 'AAPL.Open'),
// cutomise colors
increasing: {line: {color: 'black'}},
decreasing: {line: {color: 'red'}},
type: 'candlestick',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace];
var layout = {
dragmode: 'zoom',
showlegend: false,
xaxis: {
autorange: true,
title: {
text: 'Date'
},
rangeselector: {
x: 0,
y: 1.2,
xanchor: 'left',
font: {size:8},
buttons: [{
step: 'month',
stepmode: 'backward',
count: 1,
label: '1 month'
}, {
step: 'month',
stepmode: 'backward',
count: 6,
label: '6 months'
}, {
step: 'all',
label: 'All dates'
}]
}
},
yaxis: {
autorange: true,
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Customise Candlestick Chart with Shapes and Annotations
suite: candlestick
---
var trace1 = {
x: ['2017-01-17', '2017-01-18', '2017-01-19', '2017-01-20', '2017-01-23', '2017-01-24', '2017-01-25', '2017-01-26', '2017-01-27', '2017-01-30', '2017-01-31', '2017-02-01', '2017-02-02', '2017-02-03', '2017-02-06', '2017-02-07', '2017-02-08', '2017-02-09', '2017-02-10'],
close: [120, 119.989998, 119.779999, 120, 120.080002, 119.970001, 121.879997, 121.940002, 121.949997, 121.629997, 121.349998, 128.75, 128.529999, 129.080002, 130.289993, 131.529999, 132.039993, 132.419998, 132.119995],
decreasing: {line: {color: '#7F7F7F'}},
high: [120.239998, 120.5, 120.089996, 120.449997, 120.809998, 120.099998, 122.099998, 122.440002, 122.349998, 121.629997, 121.389999, 130.490005, 129.389999, 129.190002, 130.5, 132.089996, 132.220001, 132.449997, 132.940002],
increasing: {line: {color: '#17BECF'}},
line: {color: 'rgba(31,119,180,1)'},
low: [118.220001, 119.709999, 119.370003, 119.730003, 119.769997, 119.5, 120.279999, 121.599998, 121.599998, 120.660004, 120.620003, 127.010002, 127.779999, 128.160004, 128.899994, 130.449997, 131.220001, 131.119995, 132.050003],
open: [118.339996, 120, 119.400002, 120.449997, 120, 119.550003, 120.419998, 121.669998, 122.139999, 120.93, 121.150002, 127.029999, 127.980003, 128.309998, 129.130005, 130.539993, 131.350006, 131.649994, 132.460007],
type: 'candlestick',
xaxis: 'x',
yaxis: 'y'
};
var data = [trace1];
var layout = {
dragmode: 'zoom',
margin: {
r: 10,
t: 25,
b: 40,
l: 60
},
showlegend: false,
xaxis: {
autorange: true,
rangeslider: {range: ['2017-01-17 12:00', '2017-02-10 12:00']},
title: {
text: 'Date'
},
type: 'date'
},
yaxis: {
autorange: true,
type: 'linear'
},
annotations: [
{
x: '2017-01-31',
y: 0.9,
xref: 'x',
yref: 'paper',
text: 'largest movement',
font: {color: 'magenta'},
showarrow: true,
xanchor: 'right',
ax: -20,
ay: 0
}
],
shapes: [
{
type: 'rect',
xref: 'x',
yref: 'paper',
x0: '2017-01-31',
y0: 0,
x1: '2017-02-01',
y1: 1,
fillcolor: '#d3d3d3',
opacity: 0.2,
line: {
width: 0
}
}
]
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to graph D3.js-based candlestick charts in javascript. Examples of
candlestick charts.
display\_as: financial
name: Candlestick Charts
page\_type: example\_index
permalink: javascript/candlestick-charts/
thumbnail: thumbnail/candlestick.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","candlestick" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
permalink: javascript/financial-charts/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make financial charts.
name: Financial Charts
layout: langindex
display\_as: financial
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Financial Charts

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","financial" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
name: Manually Set Range
suite: time-series
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var trace1 = {
type: "scatter",
mode: "lines",
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.High'),
line: {color: '#17BECF'}
}
var trace2 = {
type: "scatter",
mode: "lines",
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.Low'),
line: {color: '#7F7F7F'}
}
var data = [trace1,trace2];
var layout = {
title: {
text: 'Custom Range'
},
xaxis: {
range: ['2016-07-01', '2016-12-31'],
type: 'date'
},
yaxis: {
autorange: true,
range: [86.8700008333, 138.870004167],
type: 'linear'
}
};
Plotly.newPlot('myDiv', data, layout);
})
---
description: How to plot D3.js-based date and time in Plotly.js. An example of a time-series
plot.
display\_as: financial
name: Time Series
page\_type: example\_index
permalink: javascript/time-series/
redirect\_from: javascript-graphing-library/time-series/
thumbnail: thumbnail/time-series.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","time-series" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Date Strings
suite: time-series
---
var data = [
{
x: ['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
y: [1, 3, 6],
type: 'scatter'
}
];
Plotly.newPlot('myDiv', data);
---
name: Time Series with Rangeslider
suite: time-series
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var trace1 = {
type: "scatter",
mode: "lines",
name: 'AAPL High',
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.High'),
line: {color: '#17BECF'}
}
var trace2 = {
type: "scatter",
mode: "lines",
name: 'AAPL Low',
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.Low'),
line: {color: '#7F7F7F'}
}
var data = [trace1,trace2];
var layout = {
title: {text: 'Time Series with Rangeslider'},
xaxis: {
autorange: true,
range: ['2015-02-17', '2017-02-16'],
rangeselector: {buttons: [
{
count: 1,
label: '1m',
step: 'month',
stepmode: 'backward'
},
{
count: 6,
label: '6m',
step: 'month',
stepmode: 'backward'
},
{step: 'all'}
]},
rangeslider: {range: ['2015-02-17', '2017-02-16']},
type: 'date'
},
yaxis: {
autorange: true,
range: [86.8700008333, 138.870004167],
type: 'linear'
}
};
Plotly.newPlot('myDiv', data, layout);
})
---
name: Basic Time Series
suite: time-series
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var trace1 = {
type: "scatter",
mode: "lines",
name: 'AAPL High',
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.High'),
line: {color: '#17BECF'}
}
var trace2 = {
type: "scatter",
mode: "lines",
name: 'AAPL Low',
x: unpack(rows, 'Date'),
y: unpack(rows, 'AAPL.Low'),
line: {color: '#7F7F7F'}
}
var data = [trace1,trace2];
var layout = {
title: {
text: 'Date'
},
};
Plotly.newPlot('myDiv', data, layout);
})
---
name: Basic Gauge
suite: gauge-charts
markdown\_content: |
A radial gauge chart has a circular arc, which displays a single value to estimate progress toward a goal.
The bar shows the target value, and the shading represents the progress toward that goal. Gauge charts, known as
speedometer charts as well. This chart type is usually used to illustrate key business indicators.
The example below displays a basic gauge chart with default attributes. For more information about different added attributes check [indicator](https://plotly.com/javascript/indicator/) tutorial.
---
var data = [
{
domain: { x: [0, 1], y: [0, 1] },
value: 270,
title: { text: "Speed" },
type: "indicator",
mode: "gauge+number"
}
];
var layout = { width: 600, height: 500, margin: { t: 0, b: 0 } };
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based gauge chart in javascript.
display\_as: financial
name: Gauge Charts
permalink: javascript/gauge-charts/
redirect\_from: javascript-graphing-library/gauge-charts
thumbnail: thumbnail/gauge.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","gauge-charts" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Custom Gauge Chart
suite: gauge-charts
markdown\_content: |
The following example shows how to style your gauge charts. For more information about all possible options check our [reference page](https://plotly.com/javascript/reference/indicator/).
---
var data = [
{
type: "indicator",
mode: "gauge+number+delta",
value: 420,
title: { text: "Speed", font: { size: 24 } },
delta: { reference: 400, increasing: { color: "RebeccaPurple" } },
gauge: {
axis: { range: [null, 500], tickwidth: 1, tickcolor: "darkblue" },
bar: { color: "darkblue" },
bgcolor: "white",
borderwidth: 2,
bordercolor: "gray",
steps: [
{ range: [0, 250], color: "cyan" },
{ range: [250, 400], color: "royalblue" }
],
threshold: {
line: { color: "red", width: 4 },
thickness: 0.75,
value: 490
}
}
}
];
var layout = {
width: 500,
height: 400,
margin: { t: 25, r: 25, l: 25, b: 25 },
paper\_bgcolor: "lavender",
font: { color: "darkblue", family: "Arial" }
};
Plotly.newPlot('myDiv', data, layout);
---
name: Add Steps, Threshold, and Delta
suite: gauge-charts
markdown\_content: |
The following examples include "steps" attribute shown as shading inside the radial arc, "delta" which is the
difference of the value and goal (reference - value), and "threshold" to determine boundaries that visually alert you if the value cross a defined threshold.
---
var data = [
{
domain: { x: [0, 1], y: [0, 1] },
value: 450,
title: { text: "Speed" },
type: "indicator",
mode: "gauge+number+delta",
delta: { reference: 380 },
gauge: {
axis: { range: [null, 500] },
steps: [
{ range: [0, 250], color: "lightgray" },
{ range: [250, 400], color: "gray" }
],
threshold: {
line: { color: "red", width: 4 },
thickness: 0.75,
value: 490
}
}
}
];
var layout = { width: 600, height: 450, margin: { t: 0, b: 0 } };
Plotly.newPlot('myDiv', data, layout);
---
name: Remove Trace
suite: remove-trace
---
function plotGraph(){
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
type: 'scatter',
line: {
color: 'rgb(55, 128, 191)',
}
};
var trace2 = {
x: [1, 2, 3, 4],
y: [16, 5, 11, 9],
type: 'scatter',
line: {
color: 'rgb(255,140,0)',
}
};
var layout = {
title: {text: 'Click Buttons to Delete Traces'},
showlegend:false
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data, layout);
}
function deleteTrace(divId){
Plotly.deleteTraces('myDiv', 0);
};
---
name: Remove Trace from Plot
permalink: javascript/remove-trace/
description: How to remove a trace from a plot in JavaScript with D3.js.
thumbnail: thumbnail/remove-trace.jpg
page\_type: example\_index
display\_as: reference
redirect\_from: javascript-graphing-library/remove-trace/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","remove-trace" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Binding to Zoom Events
suite: zoom-events
---
var graphDiv = document.getElementById('myDiv');
var N = 40,
x = d3.range(N),
y = d3.range(N).map( d3.random.normal() ),
data = [ { x:x, y:y } ];
layout = { title: {text: 'Click-drag to zoom' }};
Plotly.newPlot(graphDiv, data, layout);
graphDiv.on('plotly\_relayout',
function(eventdata){
alert( 'ZOOM!' + '\n\n' +
'Event data:' + '\n' +
JSON.stringify(eventdata) + '\n\n' +
'x-axis start:' + eventdata['xaxis.range[0]'] + '\n' +
'x-axis end:' + eventdata['xaxis.range[1]'] );
});
---
name: Zoom Events
permalink: javascript/zoom-events/
description: How to bind callback functions to zoom events in D3.js-based JavaScript charts.
thumbnail: thumbnail/zoom.jpg
page\_type: example\_index
display\_as: chart\_events
redirect\_from: javascript-graphing-library/zoom-events/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","zoom-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Hover Event Data
suite: hover-events
---
{
points: [{
curveNumber: 2, // index in data of the trace associated with the selected point
pointNumber: 2, // index of the selected point
x: 5, // x value
y: 600, // y value
data: {/\* \*/}, // ref to the trace as sent to Plotly.newPlot associated with the selected point
fullData: {/\* \*/}, // ref to the trace including all the defaults
xaxis: {/\* \*/}, // ref to x-axis object (i.e layout.xaxis) associated with the selected point
yaxis: {/\* \*/} // ref to y-axis object " "
}, {
/\* similarly for other selected points \*/
}]
}
---
name: Coupled Hover Events
suite: hover-events
---
var myPlot = document.getElementById('myDiv'),
N = 12,
x1 = d3.range(N).map( d3.random.normal() ),
x2 = d3.range(N).map( d3.random.normal() ),
x3 = d3.range(N).map( d3.random.normal() ),
y1 = d3.range(N).map( d3.random.normal() ),
y2 = d3.range(N).map( d3.random.normal() ),
y3 = d3.range(N).map( d3.random.normal() ),
months = ['January', 'February', 'March', 'April',
'May', 'June', 'July', 'August',
'September', 'October', 'November', 'December']
data = [{ x: x1, y: y1, text: months, type: 'scatter', name: '2014', hoverinfo: 'text+x+y',
mode: 'markers', marker: {color: 'rgba(200, 50, 100, .7)', size: 16}
},
{ x: x2, y: y2, text: months, type: 'scatter', name: '2015', hoverinfo: 'text+x+y',
mode: 'markers', marker: {color: 'rgba(120, 20, 130, .7)', size: 16}
},
{ x: x3, y: y3, text: months, type: 'scatter', name: '2016', hoverinfo: 'text+x+y',
mode: 'markers', marker: {color: 'rgba(10, 180, 180, .8)', size: 16}
}];
layout = {
hovermode:'closest',
title: {text: 'Display Hover Info for Related Points'},
xaxis:{zeroline:false, hoverformat: '.2r'},
yaxis:{zeroline:false, hoverformat: '.2r'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_hover', function (eventdata){
var points = eventdata.points[0],
pointNum = points.pointNumber;
Plotly.Fx.hover('myDiv',[
{ curveNumber:0, pointNumber:pointNum },
{ curveNumber:1, pointNumber:pointNum },
{ curveNumber:2, pointNumber:pointNum },
]);
});
---
name: Capturing Hover Events: Data
suite: hover-events
---
var myPlot = document.getElementById('myDiv'),
hoverInfo = document.getElementById('hoverinfo'),
N = 16,
x = d3.range(N),
y1 = d3.range(N).map( d3.random.normal() ),
y2 = d3.range(N).map( d3.random.normal() ),
data = [ { x:x, y:y1, type:'scatter', name:'Trial 1',
mode:'markers', marker:{size:16} },
{ x:x, y:y2, type:'scatter', name:'Trial 2',
mode:'markers', marker:{size:16} } ];
layout = {
hovermode:'closest',
title: {text: 'Hover on Points'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_hover', function(data){
var infotext = data.points.map(function(d){
return (d.data.name+': x= '+d.x+', y= '+d.y.toPrecision(3));
});
hoverInfo.innerHTML = infotext.join('
');
})
.on('plotly\_unhover', function(data){
hoverInfo.innerHTML = '';
});
---
name: Hover Events
permalink: javascript/hover-events/
description: How to bind callback functions to hover events in D3.js-based JavaScript charts.
thumbnail: thumbnail/hover.jpg
page\_type: example\_index
display\_as: chart\_events
redirect\_from: javascript-graphing-library/hover-events/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","hover-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Capturing Hover Events: Pixels
suite: hover-events
order: 1.5
---
var myPlot = document.getElementById('myDiv'),
hoverInfo = document.getElementById('hoverinfo'),
N = 16,
x = d3.range(N),
y1 = d3.range(N).map(d3.random.normal()),
y2 = d3.range(N).map(d3.random.normal()),
data = [{x:x, y:y1, type:'scatter', name:'Trial 1',
mode:'markers', marker:{size:16}},
{x:x, y:y2, type:'scatter', name:'Trial 2',
mode:'markers', marker:{size:16}}],
layout = {hovermode:'closest',
title: {text: 'Hover on Points to see
Pixel Coordinates'}};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_hover', function(data){
var xaxis = data.points[0].xaxis,
yaxis = data.points[0].yaxis;
var infotext = data.points.map(function(d){
return ('width: '+xaxis.l2p(d.x)+', height: '+yaxis.l2p(d.y));
});
hoverInfo.innerHTML = infotext.join('
---
name: Combined Click and Hover Events
suite: hover-events
height: 600
---
This is a more complex example that uses both hover, and click events to display traces. Take a look in the codepen javascript!
---
name: Triggering Hover Events
suite: hover-events
---
var myPlot = document.getElementById('myDiv'),
hoverButton = document.getElementById('hoverbutton'),
N = 16,
x = d3.range(N),
y1 = d3.range(N).map( d3.random.normal() ),
y2 = d3.range(N).map( d3.random.normal() ),
data = [ { x:x, y:y1, type:'scatter', name:'Trial 1',
mode:'markers', marker:{size:16} },
{ x:x, y:y2, type:'scatter', name:'Trial 2',
mode:'markers', marker:{size:16} } ];
layout = {
hovermode:'closest',
title: {text: 'Click "Go" button to trigger hover'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_beforehover',function(){
return false;
});
hoverButton.addEventListener('click', function(){
var curve1 = Math.floor(Math.random()\*2),
curve2 = Math.floor(Math.random()\*2),
point1 = Math.floor(Math.random()\*14),
point2 = Math.floor(Math.random()\*14);
Plotly.Fx.hover('myDiv',[
{curveNumber:curve1, pointNumber:point1},
{curveNumber:curve2, pointNumber:point2}
]);
});
---
name: Disabling Zoom Events for X Axis
suite: unbind-zoom-events
---
function makeplot() {
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/2014\_apple\_stock.csv", function(data){ processData(data) } );
};
function processData(allRows) {
console.log(allRows);
var x = [], y = [], standard\_deviation = [];
for (var i=0; i < allRows.length; i++) {
row = allRows[i];
x.push( row['AAPL\_x'] );
y.push( row['AAPL\_y'] );
}
console.log( 'X',x, 'Y',y, 'SD',standard\_deviation );
makePlotly( x, y, standard\_deviation );
}
function makePlotly( x, y, standard\_deviation ){
var plotDiv = document.getElementById("myDiv");
var traces = [{
x: x,
y: y
}];
var layout = {
title: {
text: 'Plotting CSV data from AJAX call'
},
xaxis: {
fixedrange: true
}
};
Plotly.newPlot('myDiv', traces, layout);
};
makeplot();
---
name: Disabling Zoom Events for X and Y Axis
suite: unbind-zoom-events
---
function makeplot() {
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/2014\_apple\_stock.csv", function(data){ processData(data) } );
};
function processData(allRows) {
var x = [], y = [], standard\_deviation = [];
for (var i=0; i < allRows.length; i++) {
row = allRows[i];
x.push( row['AAPL\_x'] );
y.push( row['AAPL\_y'] );
}
makePlotly( x, y, standard\_deviation );
}
function makePlotly( x, y, standard\_deviation ){
var plotDiv = document.getElementById("myDiv");
var traces = [{
x: x,
y: y
}];
var layout = {
title: {
text: 'Plotting CSV data from AJAX call'
},
yaxis: {fixedrange: true},
xaxis: {fixedrange: true}
};
Plotly.newPlot('myDiv', traces, layout);
};
makeplot();
---
name: Disable Zoom Events
permalink: javascript/disable-zoom/
description: How to disable zoom events in JavaScript charts.
thumbnail: thumbnail/zoom.jpg
page\_type: example\_index
display\_as: chart\_events
order: 4.75
redirect\_from: javascript-graphing-library/disable-zoom/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","unbind-zoom-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
permalink: javascript/chart-events/
name: More Chart Events
description: Plotly.js makes interactive, publication-quality graphs online. Examples of binding callbacks to Plotly chart interactions.
layout: langindex
display\_as: chart\_events
thumbnail: thumbnail/mixed.jpg
page\_type: example\_index
---

# Plotly.js Chart Events

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","chart\_events" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
name: Hovertemplate
suite: hover
---
var data = [
{
type: 'scatter',
mode: 'lines+markers',
x: [1,2,3,4,5],
y: [2.02825,1.63728,6.83839,4.8485,4.73463],
hovertemplate: '*Price*: $%{y:.2f}' +
'
**X**: %{x}
' +
'**%{text}**',
text: ["Text A", "Text B", "Text C", "Text D", "Text E"],
showlegend: false
},
{
x: [1,2,3,4,5],
y: [3.02825,2.63728,4.83839,3.8485,1.73463],
hovertemplate: 'Price: %{y:$.2f}',
showlegend: false
}
];
var layout = {
title: {
text: "Set hover text with hovertemplate"
},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Create annotation on click event
suite: click-events
---
var myPlot = document.getElementById('myDiv'),
N = 100,
x = d3.range(N),
y1 = d3.range(N).map( d3.random.normal() ),
y2 = d3.range(N).map( d3.random.normal(-2) ),
y3 = d3.range(N).map( d3.random.normal(2) ),
trace1 = { x:x, y:y1, type:'scatter', mode:'lines', name:'Jeff' },
trace2 = { x:x, y:y2, type:'scatter', mode:'lines', name:'Terren' },
trace3 = { x:x, y:y3, type:'scatter', mode:'lines', name:'Arthur' },
data = [ trace1, trace2, trace3 ],
layout = {
hovermode:'closest',
title: {text: 'Click on Points to add an Annotation on it'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click', function(data){
var pts = '';
for(var i=0; i < data.points.length; i++){
annotate\_text = 'x = '+data.points[i].x +
'y = '+data.points[i].y.toPrecision(4);
annotation = {
text: annotate\_text,
x: data.points[i].x,
y: parseFloat(data.points[i].y.toPrecision(4))
}
annotations = self.layout.annotations || [];
annotations.push(annotation);
Plotly.relayout('myDiv',{annotations: annotations})
}
});
---
name: Click Events
permalink: javascript/click-events/
description: How to bind callback functions to click events in D3.js-based JavaScript charts.
thumbnail: thumbnail/click.jpg
page\_type: example\_index
display\_as: chart\_events
redirect\_from: javascript-graphing-library/click-events/
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","click-events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Click Event Data
suite: click-events
---
{
points: [{
curveNumber: 2, // index in data of the trace associated with the selected point
pointNumber: 2, // index of the selected point
x: 5, // x value
y: 600, // y value
data: {/\* \*/}, // ref to the trace as sent to Plotly.newPlot associated with the selected point
fullData: {/\* \*/}, // ref to the trace including all the defaults
xaxis: {/\* \*/}, // ref to x-axis object (i.e layout.xaxis) associated with the selected point
yaxis: {/\* \*/} // ref to y-axis object " "
}, {
/\* similarly for other selected points \*/
}]
}
---
name: Binding to Click Events
suite: click-events
---
var myPlot = document.getElementById('myDiv'),
N = 16,
x = d3.range(N),
y = d3.range(N).map( d3.random.normal() ),
data = [ { x:x, y:y, type:'scatter',
mode:'markers', marker:{size:16} } ],
layout = {
hovermode:'closest',
title: {text: 'Click on Points'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click', function(data){
var pts = '';
for(var i=0; i < data.points.length; i++){
pts = 'x = '+data.points[i].x +'\ny = '+
data.points[i].y.toPrecision(4) + '\n\n';
}
alert('Closest point clicked:\n\n'+pts);
});
---
name: Webgl Context Lost Event
suite: events
order: 10.1
markdown\_content: |
Plotly graphs which use WebGL receive a "WebGL context" from the browser which gives them access to gpu resources.
A program may lose its WebGL context if the browser is overloaded with them and is forced to shut one down.
The event handler: `plotly\_webglcontextlost`, can be used to trigger an event after a graph loses it's WebGL context.
---
---
name: Legend Click Events
suite: events
order: 4.1
markdown\_content: |
`plotly\_legendclick` and `plotly\_legenddoubleclick` allow customization of the plotly legend. The default behaviour of `plotly\_legendclick` is to hide a trace and the default behavior of `plotly\_legenddoubleclick` is to select one trace and hide all the others.
We can add to the default behaviour by creating a new `plotly\_legendclick` event with a function of our choice. We can also disable the default behaviour by creating a function that returns `false`. In the example below, we do both in order to create a `plotly\_legendclick` event which changes the marker color back to black instead of erasing the trace.
---
var myPlot = document.getElementById('myDiv'),
x = [1, 2, 3, 4, 5, 6],
y = [1, 2, 3, 2, 3, 4],
y2 = [1, 4, 7, 6, 1, 5],
colors = [['#5C636E','#5C636E','#5C636E','#5C636E','#5C636E','#5C636E'],
['#393e46','#393e46','#393e46','#393e46','#393e46','#393e46']],
data = [{x:x, y:y, type:'scatter',
mode:'line', line:{ color:'#5C636E'},marker:{size:16, color:colors[0]}},
{x:x, y:y2, type:'scatter',
mode:'line',line:{ color:'#393e46'}, marker:{size:16, color:colors[1]}}],
layout = {
showlegend: true,
hovermode:'closest',
title: {text: 'Click on a Point to Change Color
Click on a Trace in the Legend to Change Back One Trace Only'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click', function(data){
var pn='',
tn='',
colors=[];
for(var i=0; i < data.points.length; i++){
pn = data.points[i].pointNumber;
tn = data.points[i].curveNumber;
colors = data.points[i].data.marker.color;
};
colors[pn] = '#C54C82';
var update = {'marker':{color: colors, size:16}};
Plotly.restyle('myDiv', update,[tn]);
});
myPlot.on('plotly\_legendclick', function(data){
var trColors = [['#5C636E','#5C636E','#5C636E','#5C636E','#5C636E','#5C636E'],
['#393e46','#393e46','#393e46','#393e46','#393e46','#393e46']];
var update = {'marker':{color: trColors[data.curveNumber], size:16}};
Plotly.restyle('myDiv', update,[data.curveNumber]);
return false;
});
---
name: Event Data
suite: events
markdown\_content: |
Many Plotly events emit event data when the event is triggered. Event data is information about the data point related to the event (i.e. the point clicked).
The following events emit event data: [`plotly\_click`](), [`plotly\_hover`](), [`plotly\_unhover`](), [`plotly\_selecting`](), and [`plotly\_selected`]().

Event data differs depending on the type of plot the user is interacting with. The event data structure for Cartesian (2D) plots, 3D plots, and maps can be found below, along with examples of each event.
---
// Cartesian
{
points: [{
curveNumber: 1, // index in data of the trace associated with the selected point
pointNumber: 1, // index of the selected point
x: 1, // x value
y: 1, // y value
data: {/\* \*/}, // ref to the trace as sent to Plotly.newPlot associated with the selected point
fullData: {/\* \*/}, // ref to the trace including all of the default attributes
xaxis: {/\* \*/}, // ref to x-axis object (i.e layout.xaxis) associated with the selected point
yaxis: {/\* \*/} // ref to y-axis object " "
}, {
/\* similarly for other selected points \*/
}]
}
// Cartesian Histograms
{
points: [{
curveNumber: 1, // index in data of the trace associated with the selected point
pointNumbers: [1, 5, 28, 33, 41, ...], // Array of indices of the points aggregated into selected bin
x: 1, // x value
y: 45, // y value
data: {/\* \*/}, // ref to the trace as sent to Plotly.newPlot associated with the selected point
fullData: {/\* \*/}, // ref to the trace including all of the default attributes
xaxis: {/\* \*/}, // ref to x-axis object (i.e layout.xaxis) associated with the selected point
yaxis: {/\* \*/} // ref to y-axis object " "
}, {
/\* similarly for other selected points \*/
}]
}
// 3D
{
points: [{
curveNumber: 2, // index in data of the trace associated with the selected point
pointNumber: 2, // index of the selected point
x: 5, // x value
y: 600, // y value
z: 12, // z value
data: {/\* \*/}, // ref to the trace as sent to Plotly.newPlot associated with the selected point
fullData: {/\* \*/}, // ref to the trace including all of the default attributes
xaxis: {/\* \*/}, // ref to x-axis object (i.e layout.xaxis) associated with the selected point
yaxis: {/\* \*/} // ref to y-axis object " "
zaxis: {/\* \*/} // ref to z-axis object " "
}, {
/\* similarly for other selected points \*/
}]
}
// Maps
{
points: [{
curveNumber: 2, // index in data of the trace associated with the selected point
pointNumber: 2, // index of the selected point
lat: 50, // latitude value
lon: -12, // longitude value
data: {/\* \*/}, // ref to the trace as sent to Plotly.newPlot associated with the selected point
fullData: {/\* \*/}, // ref to the trace including all of the default attributes
location: //
}, {
/\* similarly for other selected points \*/
}]
}
---
name: Additional Events
suite: events
order: 10
markdown\_content: |
The following Plotly events do not emit additional data or update information: [`plotly\_webglcontextlost`](#webgl-context-lost-event), [`plotly\_afterplot`](#afterplot-event), [`plotly\_autosize`](), [`plotly\_deselect`](), [`plotly\_doubleclick`](#double-click-event), [`plotly\_redraw`](), and [`plotly\_animated`](). These event handlers can be used to notify or trigger an additional event with the following syntax:
---
function eventTriggeredHandler() {
/\* add your event triggered handler here \*/
}
myDiv.on('plotly\_event', eventTriggeredHandler);
---
name: Simple Event Example
suite: events
markdown\_content: |
Here's a simple example using a Plotly event. Click on a point on the chart below to see an alert triggered by the `plotly\_click` event.
---
var myPlot = document.getElementById('myDiv'),
x = [1, 2, 3, 4, 5],
y = [10, 20, 30, 20, 10],
data = [{x:x, y:y, type:'scatter',
mode:'markers', marker:{size:20}
}],
layout = {hovermode:'closest',
title: {text: 'Click on Points'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click', function(){
alert('You clicked this Plotly chart!');
});
---
name: Hover Event
suite: events
markdown\_content: |
Here's a simple example of using the data returned from the `plotly\_hover` and `plotly\_unhover` events to restyle the graph. After creating a plot, we can change the color of the point hovered on by updating the `marker.color` array at the index of the point we hovered on then using `Plotly.restyle()` to apply the update. Then we can use `plotly\_unhover` to change the `marker.color` back to the original color. For more examples of using `plotly\_hover` events, see: https://plotly.com/javascript/hover-events/
---
var myPlot = document.getElementById('myDiv'),
x = [1, 2, 3, 4, 5, 6, 7],
y = [1, 2, 3, 2, 3, 4, 3],
colors =['#00000','#00000','#00000',
'#00000','#00000','#00000',
'#00000'],
data = [{x:x, y:y,
type:'scatter',
mode:'markers', marker:{size:16, color:colors}}],
layout = {
hovermode:'closest',
title: {text: 'Hover on a Point
to Change Color'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_hover', function(data){
var pn='',
tn='',
colors=[];
for(var i=0; i < data.points.length; i++){
pn = data.points[i].pointNumber;
tn = data.points[i].curveNumber;
colors = data.points[i].data.marker.color;
};
colors[pn] = '#C54C82';
var update = {'marker':{color: colors, size:16}};
Plotly.restyle('myDiv', update, [tn]);
});
myPlot.on('plotly\_unhover', function(data){
var pn='',
tn='',
colors=[];
for(var i=0; i < data.points.length; i++){
pn = data.points[i].pointNumber;
tn = data.points[i].curveNumber;
colors = data.points[i].data.marker.color;
};
colors[pn] = '#00000';
var update = {'marker':{color: colors, size:16}};
Plotly.restyle('myDiv', update, [tn]);
});
---
name: Double Click Event
suite: events
order: 10.3
markdown\_content: |
In addition to `plotly\_click`, `plotly\_doubleclick` can be used as an event handle in Plotly charts as well. You may already be familiar with `plotly\_doubleclick` if you regularly use Plotly's zoom and pan functionality, double clicking on the graph will restore the axes ranges after zooming into a specific area. Unlike `plotly\_click`, a `plotly\_doubleclick` is registered upon clicking anywhere on the graph (not just data points), therefore, `plotly\_doubleclick` does not return data. In the following example, we'll build off of our `plotly\_click` example, and reset the color of our data points upon double clicking anywhere on the graph.
---
var myPlot = document.getElementById('myDiv'),
x = [1, 2, 3, 4, 5, 6],
y = [1, 2, 3, 2, 3, 4],
colors = ['#00000','#00000','#00000',
'#00000','#00000','#00000'],
data = [{x:x, y:y, type:'scatter',
mode:'markers', marker:{size:16, color:colors}}],
layout = {
hovermode:'closest',
title: {text: 'Click on a Point to Change Color
Double Click (anywhere) to Change it Back'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click', function(data){
var pn='',
tn='',
colors=[];
for(var i=0; i < data.points.length; i++){
pn = data.points[i].pointNumber;
tn = data.points[i].curveNumber;
colors = data.points[i].data.marker.color;
};
colors[pn] = '#C54C82';
var update = {'marker':{color: colors, size:16}};
Plotly.restyle('myDiv', update, [tn]);
});
myPlot.on('plotly\_doubleclick', function(data){
var orgColors = ['#00000','#00000','#00000',
'#00000','#00000','#00000'];
var update = {'marker':{color: orgColors, size:16}};
Plotly.restyle('myDiv', update);
});
---
name: Click Event
suite: events
markdown\_content: |
Here's a simple example of using the data returned from the `plotly\_click` event to restyle the graph. After creating a plot, we can change the color of the point clicked on by updating the `marker.color` array at the index of the point we clicked on then using `Plotly.restyle()` to apply the update. For more examples of using `plotly\_click` events, see: [https://plotly.com/javascript/click-events/]()
---
var myPlot = document.getElementById('myDiv'),
x = [1, 2, 3, 4, 5, 6],
y = [1, 2, 3, 2, 3, 4],
colors = ['#00000','#00000','#00000',
'#00000','#00000','#00000'],
data = [{x:x, y:y, type:'scatter',
mode:'markers', marker:{size:16, color:colors}}],
layout = {
hovermode:'closest',
title: {text: 'Click on a Point to Change Color
Double Click (anywhere) to Change it Back'}
};
Plotly.newPlot('myDiv', data, layout);
myPlot.on('plotly\_click', function(data){
var pn='',
tn='',
colors=[];
for(var i=0; i < data.points.length; i++){
pn = data.points[i].pointNumber;
tn = data.points[i].curveNumber;
colors = data.points[i].data.marker.color;
};
colors[pn] = '#C54C82';
var update = {'marker':{color: colors, size:16}};
Plotly.restyle('myDiv', update, [tn]);
});
---
name: Update Data
suite: events
markdown\_content: |
The following Plotly events emit update information when the event is triggered: [`plotly\_restyle`]() and [`plotly\_relayout`]().
The update emitted with `plotly\_restyle` is similar across plot types and includes an array containing an object of the newly updated
attributes and an array of the trace numbers that were updated.
For Cartesian (2D) plots, `plotly\_relayout` emits only the xaxis and yaxis ranges which were directly changed by the triggering event.
For 3D plots, [`layout.scene.camera`](https://plotly.com/javascript/reference/layout/scene/#layout-scene-camera) data is similarly emitted.
See the full structures below:
---
// plotly\_restyle update
[
{update}, // update object -- attribute updated: new value
[0] // array of traces updated
]
// plotly\_relayout update: Cartesian
//// Upon resizing plot:
{
xaxis.range[0]: , // new value if xaxis.range[0] was updated
xaxis.range[1]: ,
yaxis.range[0]: , // new value if yaxis.range[0] was updated
yaxis.range[1]:
}
//// Upon autosizing plot:
{
xaxis.autorange: true,
yaxis.autorange: true
}
// plotly\_relayout update: 3D
// a subset of the following data will be emitted depending on
// which attributes were changed by the triggering event.
{
scene: {
center: { // https://plotly.com/javascript/reference/layout/scene/#layout-scene-camera-center
x: 0,
y: 0,
z: 0
}
},
{
eye: { // https://plotly.com/javascript/reference/layout/scene/#layout-scene-camera-eye
x: 1.25,
y: 1.25,
z: 1.25
}
}.
{
up: { // https://plotly.com/javascript/reference/layout/scene/#layout-scene-camera-up
x: 0,
y: 0,
z: 1
}
}
}
---
name: Select Event
suite: events
markdown\_content: |
Here's a simple example using the data returned from the `plotly\_selected` event. `plotly\_selected` returns event data for all points selected simultaneously. After creating a scatter plot with random data and two histograms that display the x and y distributions of that random data, we can select points by clicking and dragging on the plot. Upon `plotly\_selected` the histograms will update to display the distribution of the x and y values of the selected points. The color of the scatter plot will be updated as well to highlight the selected points. For more examples of using `plotly\_selected` and `plotly\_selecting` events, see: https://plotly.com/javascript/lasso-selection/
---
var graphDiv = document.getElementById('myDiv');
var N = 1000;
var color1 = '#7b3294';
var color1Light = '#c2a5cf';
var colorX = '#ffa7b5';
var colorY = '#fdae61';
function randomArray() {
var out = new Array(N);
for(var i = 0; i < N; i++) {
out[i] = Math.random();
}
return out;
}
var x = randomArray();
var y = randomArray();
Plotly.newPlot(graphDiv, [{
type: 'scatter',
mode: 'markers',
x: x,
y: y,
xaxis: 'x',
yaxis: 'y',
name: 'random data',
marker: {color: color1, size: 10}
}, {
type: 'histogram',
x: x,
xaxis: 'x2',
yaxis: 'y2',
name: 'x coord dist.',
marker: {color: colorX}
}, {
type: 'histogram',
x: y,
xaxis: 'x3',
yaxis: 'y3',
name: 'y coord dist.',
marker: {color: colorY}
}], {
title: {
text: 'Lasso around the scatter points to see sub-distributions'
},
dragmode: 'lasso',
xaxis: {
zeroline: false,
},
yaxis: {
domain: [0.55, 1],
},
xaxis2: {
domain: [0, 0.45],
anchor: 'y2',
},
yaxis2: {
domain: [0, 0.45],
anchor: 'x2'
},
xaxis3: {
domain: [0.55, 1],
anchor: 'y3'
},
yaxis3: {
domain: [0, 0.45],
anchor: 'x3'
}
});
graphDiv.on('plotly\_selected', function(eventData) {
var x = [];
var y = [];
var colors = [];
for(var i = 0; i < N; i++) colors.push(color1Light);
eventData.points.forEach(function(pt) {
x.push(pt.x);
y.push(pt.y);
colors[pt.pointNumber] = color1;
});
Plotly.restyle(graphDiv, {
x: [x, y],
xbins: {}
}, [1, 2]);
Plotly.restyle(graphDiv, 'marker.color', [colors], [0]);
});
---
name: Using Plotly.js Events
suite: events
markdown\_content: |
Plotly graphs emit events prefixed with plotly\_ (i.e. `'plotly\_click'`, `'plotly\_hover'`, `'plotly\_relayout'`) when interacted with (clicked, hovered, zoomed). Event handlers can be bound to events using the `.on` method that is exposed by the plot div object.
In addition to the event handler, some events emit additional information about the point(s) or plot interacted with. The following documentation organizes Plotly events based on the accessible information emitted with the event: [event data](), [update data](), or [no additional data](). The following page provides a description and example of each Plotly event as well as the structure of the data or update returned with the event.
---
myDiv.on('plotly\_event', function(){
// do something;
});
---
name: Event Handlers
permalink: javascript/plotlyjs-events/
description: Definitions and examples of how to use Plotly.js event handlers to add additional interactive capabilities to Plotly charts.
page\_type: example\_index
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","events" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Afterplot Event
suite: events
order: 10.2
markdown\_content: |
The event handler: `plotly\_afterplot`, can be used to trigger an event each time a chart is plotted. This also includes re-plotting after the restyling or relayout of a plot.
Users also have the option of adding a post-plot handler to the plot call with the following syntax: `Plotly.newPlot('myDiv', data, layout, config).then(postPlotHandler);`
The simple example below logs a console message each time the chart is plotted. Zoom or pan on the graph below to trigger the `plotly\_afterplot` handler.
---
var myPlot = document.getElementById('myDiv'),
N = 20,
x = d3.range(N),
y = d3.range(N).map( d3.random.normal() ),
data = [{x:x, y:y, type:'scatter',
mode:'markers', marker:{size:14}}
];
Plotly.newPlot('myDiv', data);
myPlot.on('plotly\_afterplot', function(){
console.log('done plotting');
});
---
name: Overview
suite: filled-area-on-map
markdown\_content: |
There are three different ways to show a filled area in a tile-based map.

1. Use a [scattermap](https://plotly.com/javascript/reference/scattermap/) trace and set `fill` attribute to 'toself'
2. Use a map layout (i.e. by minimally using an empty Scattermap trace) and add a GeoJSON layer
3. Use the [Choroplethmap](https://plotly.com/javascript/map-county-choropleth/) trace type

###### Filled `Scattermap` Trace

The following example uses `Scattermap` and sets `fill = 'toself'`.
---
var data = [
{
type: "scattermap",
fill: "toself",
lon: [-74, -70, -70, -74],
lat: [47, 47, 45, 45],
marker: { size: 10, color: "orange" }
}
];
var layout = {
map: {
style: "stamen-terrain",
center: { lon: -73, lat: 46 },
zoom: 5
},
showlegend: false,
height: 450,
width: 600
};
Plotly.newPlot("myDiv", data, layout);
---
name: Multiple Filled Areas with a Scattermap trace
suite: filled-area-on-map
markdown\_content: |
The following example shows how to use `null` in your data to draw multiple filled areas. Such gaps in trace data are unconnected by default, but this can be controlled via the [connectgaps](https://plotly.com/javascript/reference/scattermap/#scattermap-connectgaps) attribute.
---
var data = [{
type: "scattermap",
mode: "lines",
fill: "toself",
lon: [-10, -10, 8, 8, -10, null, 30, 30, 50, 50, 30, null, 100, 100, 80, 80, 100],
lat: [30, 6, 6, 30, 30, null, 20, 30, 30, 20, 20, null, 40, 50, 50, 40, 40]
}]
var layout = {
map: {style: "stamen-terrain", center: {lon: 40, lat: 20}, 'zoom': 1.5},
showlegend: false,
width:700, height: 700}
Plotly.newPlot("myDiv", data, layout)
---
description: How to make an area on Map using a D3.js-based scattermap.
display\_as: maps
has\_thumbnail: true
name: Filled Area on Tile Maps
order: 10
page\_type: u-guide
permalink: javascript/filled-area-on-map/
redirect\_from: javascript/filled-area-on-mapbox/
thumbnail: thumbnail/area.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","filled-area-on-map" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: GeoJSON Layers
suite: filled-area-on-map
markdown\_content: |
This example shows an area below [water layer](https://plotly.com/javascript/reference/choroplethmap/#choroplethmap-below), and sets geojson object of type feature and geometries of type [MultiPolygon](https://plotly.com/javascript/reference/choroplethmap/#choroplethmap-geojson).
---
var data = [{
type: "scattermap", mode: "markers",
lon: [-73.605], lat: [45.51],
marker: { size: 20, color: ["cyan"] }
}];
var layout = {
map: {
style: "dark",
center: { lon: -73.6, lat: 45.515},
zoom: 12, layers: [{
source: {
type: "FeatureCollection",
features: [{
type: "Feature",
geometry: {
type: "MultiPolygon",
coordinates: [[[
[-73.606352888, 45.507489991], [-73.606133883, 45.50687600],
[-73.605905904, 45.506773980], [-73.603533905, 45.505698946],
[-73.602475870, 45.506856969], [-73.600031904, 45.505696003],
[-73.599379992, 45.505389066], [-73.599119902, 45.505632008],
[-73.598896977, 45.505514039], [-73.598783894, 45.505617001],
[-73.591308727, 45.516246185], [-73.591380782, 45.516280145],
[-73.596778656, 45.518690062], [-73.602796770, 45.521348046],
[-73.612239983, 45.525564037], [-73.612422919, 45.525642061],
[-73.617229085, 45.527751983], [-73.617279234, 45.527774160],
[-73.617304713, 45.527741334], [-73.617492052, 45.527498362],
[-73.617533258, 45.527512253], [-73.618074188, 45.526759105],
[-73.618271651, 45.526500673], [-73.618446320, 45.526287943],
[-73.618968507, 45.525698560], [-73.619388002, 45.525216750],
[-73.619532966, 45.525064183], [-73.619686662, 45.524889290],
[-73.619787038, 45.524770086], [-73.619925742, 45.524584939],
[-73.619954486, 45.524557690], [-73.620122362, 45.524377961],
[-73.620201713, 45.524298907], [-73.620775593, 45.523650879]
]]]
}
}]
},
type: "fill", below: "water", color: "teal"
}]
},
height: 450, width: 700
};
Plotly.newPlot("myDiv", data, layout);
---
name: Lines on an Orthographic Map
suite: lines-on-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/globe\_contours.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [];
var scl =['rgb(213,62,79)','rgb(244,109,67)','rgb(253,174,97)','rgb(254,224,139)','rgb(255,255,191)','rgb(230,245,152)','rgb(171,221,164)','rgb(102,194,165)','rgb(50,136,189)'];
var allLats = [];
var allLons = [];
for ( var i = 0 ; i < scl.length; i++){
var latHead = 'lat-'+i;
var lonHead = 'lon-'+i;
var lat = unpack(rows, latHead);
var lon = unpack(rows, lonHead);
allLats.push(lat);
allLons.push(lon);
}
for ( var i = 0 ; i < scl.length; i++) {
var current = {
type:'scattergeo',
lon: allLons[i],
lat: allLats[i],
mode: 'lines',
line: {
width: 2,
color: scl[i]
}
}
data.push(current);
};
var layout = {
geo: {
projection: {
type: 'orthographic',
rotation: {
lon: -100,
lat: 40
},
},
showocean: true,
oceancolor: 'rgb(0, 255, 255)',
showland: true,
landcolor: 'rgb(230, 145, 56)',
showlakes: true,
lakecolor: 'rgb(0, 255, 255)',
showcountries: true,
lonaxis: {
showgrid: true,
gridcolor: 'rgb(102, 102, 102)'
},
lataxis: {
showgrid: true,
gridcolor: 'rgb(102, 102, 102)'
}
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
description: How to draw D3.js-based lines, great circles, and contours on maps in
JavaScript. Lines on maps can show distance between geographic points or be contour
lines (isolines, isopleths, or isarithms).
display\_as: maps
name: Lines on Maps
page\_type: example\_index
permalink: javascript/lines-on-maps/
redirect\_from: javascript-graphing-library/lines-on-maps/
thumbnail: thumbnail/flight-paths.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","lines-on-maps" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: US Flight Paths Map
suite: lines-on-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/c34aaa0b1b3cddad335173cb7bc0181897201ee6/2011\_february\_aa\_flight\_paths.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });}
function getMaxOfArray(numArray) {
return Math.max.apply(null, numArray);
}
var data = [];
var count = unpack(rows, 'cnt');
var startLongitude = unpack(rows, 'start\_lon');
var endLongitude = unpack(rows, 'end\_lon');
var startLat = unpack(rows, 'start\_lat');
var endLat = unpack(rows, 'end\_lat');
for ( var i = 0 ; i < count.length; i++ ) {
var opacityValue = count[i]/getMaxOfArray(count);
var result = {
type: 'scattergeo',
locationmode: 'USA-states',
lon: [ startLongitude[i] , endLongitude[i] ],
lat: [ startLat[i] , endLat[i] ],
mode: 'lines',
line: {
width: 1,
color: 'red'
},
opacity: opacityValue
};
data.push(result);
};
var layout = {
title: {text: 'Feb. 2011 American Airline flight paths'},
showlegend: false,
geo:{
scope: 'north america',
projection: {
type: 'azimuthal equal area'
},
showland: true,
landcolor: 'rgb(243,243,243)',
countrycolor: 'rgb(204,204,204)'
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: London to NYC Great Circle
suite: lines-on-maps
---
var data = [{
type: 'scattergeo',
lat: [ 40.7127, 51.5072 ],
lon: [ -74.0059, 0.1275 ],
mode: 'lines',
line:{
width: 2,
color: 'blue'
}
}];
var layout = {
title: {text: 'London to NYC Great Circle'},
showlegend: false,
geo: {
resolution: 50,
showland: true,
showlakes: true,
landcolor: 'rgb(204, 204, 204)',
countrycolor: 'rgb(204, 204, 204)',
lakecolor: 'rgb(255, 255, 255)',
projection: {
type: 'equirectangular'
},
coastlinewidth: 2,
lataxis: {
range: [ 20, 60 ],
showgrid: true,
tickmode: 'linear',
dtick: 10
},
lonaxis:{
range: [-100, 20],
showgrid: true,
tickmode: 'linear',
dtick: 20
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Dark tile
suite: tile-county-choropleth
markdown\_content: |
This example uses [zmin and zmax](https://plotly.com/javascript/reference/choroplethmap/#choroplethmap-zmin) to define the lower bound and upper bound of the color domain. If these attributes are not set, Plotly [determines the color domain](https://plotly.com/javascript/reference/heatmap/#heatmap-zauto) based on the input data.
---
var data = [{
type: "choroplethmap", name: "US states", geojson: "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json", locations: [ "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY" ],
z: [ 141, 140, 155, 147, 132, 146, 151, 137, 146, 136, 145, 141, 149, 151, 138, 158, 164, 141, 146, 145, 142, 150, 155, 160, 156, 161, 147, 164, 150, 152, 155, 167, 145, 146, 151, 154, 161, 145, 155, 150, 151, 162, 172, 169, 170, 151, 152, 173, 160, 176 ],
zmin: 25, zmax: 280, colorbar: {y: 0, yanchor: "bottom", title: {text: "US states", side: "right"}}}
];
var layout = {map: {style: "dark", center: {lon: -110, lat: 50}, zoom: 0.8}, width: 600, height: 400, margin: {t: 0, b: 0}};
Plotly.newPlot('myDiv', data, layout);
---
name: Streets Tile
suite: tile-county-choropleth
markdown\_content: |
The following example sets `geojson object` of type `feature` and geometries of type 'Polygon'. For more information see [geojson attribute](https://plotly.com/javascript/reference/choroplethmap/#choroplethmap-geojson) in the reference page.
As you see, the scattermap trace is above the Choropleth map trace. To set the Choropleth map trace above all the other traces you should set [below attribute](https://plotly.com/javascript/reference/choroplethmap/#choroplethmap-below).
---
var data = [
{type: "scattermap", lon: [-86], lat: [34], marker: {size: 20, color: 'purple'}},
{
type: "choroplethmap",locations: ["AL"], z: [10], coloraxis: "coloraxis", geojson: {type: "Feature", id: "AL", geometry: {type: "Polygon", coordinates: [[
[-86, 35], [-85, 34], [-85, 32], [-85, 32], [-85, 32], [-85, 32], [-85, 31],
[-86, 31], [-87, 31], [-87, 31], [-88, 30], [-88, 30], [-88, 30], [-88, 30],
[-88, 34], [-88, 35]]]
}}}];
var layout = {width: 600, height: 400, map: {style: 'streets',
center: {lon: -86, lat: 33}, zoom: 5}, marker: {line: {color: "blue"}},
coloraxis: {showscale: false, colorscale: "Viridis"}};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a tile-based choropleth map in JavaScript. A Choropleth map shades geographic regions by value.
display\_as: maps
name: Choropleth Tile Map
page\_type: example\_index
permalink: javascript/tile-county-choropleth/
redirect\_from: javascript/mapbox-county-choropleth/
thumbnail: thumbnail/mapbox-choropleth.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","tile-county-choropleth" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Tile
suite: tile-county-choropleth
markdown\_content: |
This tutorial uses [Maplibre GL JS](https://maplibre.org/maplibre-gl-js/docs/) to make a map of US states using [vector tiles](https://plotly.com/javascript/map-layers/).
---
var data = [{
type: "choroplethmap", locations: ["NY", "MA", "VT"], z: [-50, -10, -20],
geojson: "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
}];
var layout = {map: {center: {lon: -74, lat: 43}, zoom: 3.5},
width: 600, height:400};
Plotly.newPlot('myDiv', data, layout);
---
name: Basic Tile using Mapbox
suite: tile-county-choropleth
markdown\_content: |
**> Mapbox traces are deprecated and may be removed in a future version of Plotly.js.**
Earlier examples use traces that render with [Maplibre GL JS](https://maplibre.org/maplibre-gl-js/docs/).
These traces were introduced in Plotly.js 2.35.0 and replace Mapbox-based tile maps,
which are now deprecated. Here's one of the earlier examples using the Mapbox-based `choroplethmapbox` trace
---
var data = [{
type: "choroplethmapbox", locations: ["NY", "MA", "VT"], z: [-50, -10, -20],
geojson: "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"
}];
var layout = {mapbox: {center: {lon: -74, lat: 43}, zoom: 3.5},
width: 600, height:400};
var config = {mapboxAccessToken: "your access token"};
Plotly.newPlot('myDiv', data, layout, config);
---
name: USA Bubble Map
suite: bubble-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2014\_us\_cities.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var cityName = unpack(rows, 'name'),
cityPop = unpack(rows, 'pop'),
cityLat = unpack(rows, 'lat'),
cityLon = unpack(rows, 'lon'),
color = [,"rgb(255,65,54)","rgb(133,20,75)","rgb(255,133,27)","lightgrey"],
citySize = [],
hoverText = [],
scale = 50000;
for ( var i = 0 ; i < cityPop.length; i++) {
var currentSize = cityPop[i] / scale;
var currentText = cityName[i] + " pop: " + cityPop[i];
citySize.push(currentSize);
hoverText.push(currentText);
}
var data = [{
type: 'scattergeo',
locationmode: 'USA-states',
lat: cityLat,
lon: cityLon,
hoverinfo: 'text',
text: hoverText,
marker: {
size: citySize,
line: {
color: 'black',
width: 2
},
}
}];
var layout = {
title: {text: '2014 US City Populations'},
showlegend: false,
geo: {
scope: 'usa',
projection: {
type: 'albers usa'
},
showland: true,
landcolor: 'rgb(217, 217, 217)',
subunitwidth: 1,
countrywidth: 1,
subunitcolor: 'rgb(255,255,255)',
countrycolor: 'rgb(255,255,255)'
},
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: Europe Bubble Map
suite: bubble-maps
---
var data = [{
type: 'scattergeo',
mode: 'markers',
locations: ['FRA', 'DEU', 'RUS', 'ESP'],
marker: {
size: [20, 30, 15, 10],
color: [10, 20, 40, 50],
cmin: 0,
cmax: 50,
colorscale: 'Greens',
colorbar: {
title: {text: 'Some rate'},
ticksuffix: '%',
showticksuffix: 'last'
},
line: {
color: 'black'
}
},
name: 'europe data'
}];
var layout = {
'geo': {
'scope': 'europe',
'resolution': 50
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based bubble map in JavaScript. A bubble map overlays
a bubble chart on a map.
display\_as: maps
name: Bubble Maps
page\_type: example\_index
permalink: javascript/bubble-maps/
redirect\_from: javascript-graphing-library/bubble-maps/
thumbnail: thumbnail/bubble-map.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","bubble-maps" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Example (Mapbox)
suite: scatter-tile-maps
order: 10
markdown\_content: |
**> Mapbox traces are deprecated and may be removed in a future version of Plotly.js.**
Earlier examples use traces that render with [Maplibre GL JS](https://maplibre.org/maplibre-gl-js/docs/).
These traces were introduced in Plotly.js 2.35.0 and replace Mapbox-based tile maps,
which are now deprecated. Here's one of the earlier examples using the Mapbox-based `choroplethmapbox` trace
---
var data = [{
type:'scattermapbox',
lat:['45.5017'],
lon:['-73.5673'],
mode:'markers',
marker: {
size:14
},
text:['Montreal']
}]
var layout = {
autosize: true,
hovermode:'closest',
mapbox: {
bearing:0,
center: {
lat:45,
lon:-73
},
pitch:0,
zoom:5
},
}
Plotly.setPlotConfig({
mapboxAccessToken: "your access token"
})
Plotly.newPlot('myDiv', data, layout)
---
name: Adding Colorscale to Maps
suite: scatter-tile-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2015\_06\_30\_precipitation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
scl = [[0, 'rgb(150,0,90)'],[0.125, 'rgb(0, 0, 200)'],[0.25,'rgb(0, 25, 255)'],[0.375,'rgb(0, 152, 255)'],[0.5,'rgb(44, 255, 150)'],[0.625,'rgb(151, 255, 0)'],[0.75,'rgb(255, 234, 0)'],[0.875,'rgb(255, 111, 0)'],[1,'rgb(255, 0, 0)']];
var data = [{
type: 'scattermap',
mode: 'markers',
text: unpack(rows, 'Globvalue'),
lon: unpack(rows, 'Lon'),
lat: unpack(rows, 'Lat'),
marker: {
color: unpack(rows, 'Globvalue'),
colorscale: scl,
cmin: 0,
cmax: 1.4,
reversescale: true,
opacity: 0.5,
size: 3,
colorbar:{
thickness: 10,
title: {side:
'right'
},
outlinecolor: 'rgba(68,68,68,0)',
ticks: 'outside',
ticklen: 3,
shoticksuffix: 'last',
ticksuffix: 'inches',
dtick: 0.1
}
},
name: 'NA Precipitation'
}];
layout = {
dragmode: 'zoom',
map: {
center: {
lat: 38.03697222,
lon: -90.70916722
},
domain: {
x: [0, 1],
y: [0, 1]
},
style: 'light',
zoom: 3
},
margin: {
r: 0,
t: 0,
b: 0,
l: 0,
pad: 0
},
showlegend: false
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Multiple Markers
suite: scatter-tile-maps
---
d3.csv('https://raw.githubusercontent.com/bcdunbar/datasets/master/meteorites\_subset.csv', function(err, rows){
var classArray = unpack(rows, 'class');
var classes = [...new Set(classArray)];
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = classes.map(function(classes) {
var rowsFiltered = rows.filter(function(row) {
return (row.class === classes);
});
return {
type: 'scattermap',
name: classes,
lat: unpack(rowsFiltered, 'reclat'),
lon: unpack(rowsFiltered, 'reclong')
};
});
var layout = {
title: {text: 'Meteorite Landing Locations'},
font: {
color: 'white'
},
dragmode: 'zoom',
map: {
center: {
lat: 38.03697222,
lon: -90.70916722
},
domain: {
x: [0, 1],
y: [0, 1]
},
style: 'dark',
zoom: 1
},
margin: {
r: 20,
t: 40,
b: 20,
l: 20,
pad: 0
},
paper\_bgcolor: '#191A1A',
plot\_bgcolor: '#191A1A',
showlegend: true,
annotations: [{
x: 0,
y: 0,
xref: 'paper',
yref: 'paper',
text: 'Source: [NASA](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh)',
showarrow: false
}]
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Adding Lines to Maps
suite: scatter-tile-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/c34aaa0b1b3cddad335173cb7bc0181897201ee6/2011\_february\_aa\_flight\_paths.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });}
function getMaxOfArray(numArray) {
return Math.max.apply(null, numArray);
}
var data = [];
var count = unpack(rows, 'cnt');
var startLongitude = unpack(rows, 'start\_lon');
var endLongitude = unpack(rows, 'end\_lon');
var startLat = unpack(rows, 'start\_lat');
var endLat = unpack(rows, 'end\_lat');
for ( var i = 0 ; i < count.length; i++ ) {
var opacityValue = count[i]/getMaxOfArray(count);
var result = {
type: 'scattermap',
lon: [ startLongitude[i] , endLongitude[i] ],
lat: [ startLat[i] , endLat[i] ],
mode: 'lines',
line: {
width: 1,
color: 'red'
},
opacity: opacityValue
};
data.push(result);
};
layout = {
dragmode: 'zoom',
map: {
center: {
lat: 38.03697222,
lon: -90.70916722
},
domain: {
x: [0, 1],
y: [0, 1]
},
style: 'dark',
zoom: 2
},
margin: {
r: 0,
t: 0,
b: 0,
l: 0,
pad: 0
},
paper\_bgcolor: '#191A1A',
plot\_bgcolor: '#191A1A',
showlegend: false
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: Set Marker Symbols
suite: scatter-tile-maps
markdown\_content: |
This example uses [symbol attribute](https://plotly.com/javascript/reference/scattermap/#scattermap-marker-symbol) to set the marker symbol.
---
var data = [
{
type: "scattermap",
mode: "markers+text+lines",
lon: [-75, -80, -50],
lat: [45, 20, -20],
marker: { size: 20, symbol: ["bus", "harbor", "airport"] },
text: ["Bus", "Harbor", "Airport"],
textposition: "bottom right"
}
];
var layout = {
map: { style: "outdoors", zoom: 0.7 },
showlegend: false, height: 500, width: 700
};
Plotly.newPlot("myDiv", data, layout);
---
name: Basic Example
suite: scatter-tile-maps
---
var data = [{
type:'scattermap',
lat:['45.5017'],
lon:['-73.5673'],
mode:'markers',
marker: {
size:14
},
text:['Montreal']
}]
var layout = {
autosize: true,
hovermode:'closest',
map: {
bearing:0,
center: {
lat:45,
lon:-73
},
pitch:0,
zoom:5
},
}
Plotly.newPlot('myDiv', data, layout)
---
description: How to make scatter plots on tile maps in Plotly.JS
display\_as: maps
name: Scatter Plots on Tile Maps
permalink: javascript/scatter-tile-maps/
redirect\_from: javascript/scattermapbox/
thumbnail: thumbnail/scatter-mapbox.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","scatter-tile-maps" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
description: How to migrate from Mapbox traces to Maplibre traces.
display\_as: maps
name: Migrate to Maplibre
page\_type: example\_index
permalink: javascript/maplibre-migration/
thumbnail: thumbnail/area.jpg
---

With the release of Plotly.js v2.35.0, we are introducing a new set of trace types for maps with tile underlays:

* Choroplethmap
* Scattermap
* Densitymap

These traces replace the existing Mapbox traces, `Choroplethmapbox`, `Scattermapbox`,
`Densitymapbox`, but use [MapLibre](https://maplibre.org) as the map renderer rather than
Mapbox.

When switching to the new traces, keep an eye out for improved rendering performance, WebGL2 support, and over time,
improved features in the Plotly map traces inherited from the MapLibre renderer, including projection support, globe
views, terrain support, and support for modern mapping standards.

You can learn more about the motivations for this change in our [announcement
post](https://plotly.com/blog/plotly-is-switching-to-maplibre/).

As a result of removing Mapbox as the rendering engine, we're also removing the Mapbox branding from these trace
names.
This means that migrating from Mapbox traces to MapLibre traces will require some code changes in your projects.

1. Change trace names from `*mapbox` to `*map`. For any existing trace name ending in
   `*mapbox`,
   ensure you've removed the "box" suffix.
2. If in use, update `layout.mapbox` argument in your layout configuration to `layout.map`.
   The nested properties are identical in the new map traces, so no other changes should be required.
3. If in use, update `mapbox_style` to `map_style`.
4. Verify your `map_style` settings. With `mapbox` traces, we bundle `basic`,
   `streets`,
   `outdoors`, `light`, `dark`, `satellite`, and
   `satellite-streets` styles,
   using Mapbox styling. These style names are still available, but they now reference slightly different styles
   provided by other tools.

Note that Mapbox API keys are no longer required for Plotly-provided styles, but using external styles in your Plotly
maps remains supported with the existing API.
---
name: Light Tile
suite: tile-density-heatmaps
---
var data = [
{type: "densitymap", lon: [10, 20, 30], lat: [15, 25, 35], z: [1, 3, 2],
radius: 50, colorbar: {y: 1, yanchor: 'top', len: 0.45}},
{type: 'densitymap', lon: [-10, -20, -30], lat: [15, 25, 35],
radius: [50, 100, 10], colorbar: {y: 0, yanchor: 'bottom', len: 0.45}
}];
var layout = {map: {style: 'light', center: {lat: 20}}, width: 600, height: 400};
Plotly.newPlot('myDiv', data, layout);
---
name: Outdoors Tile
suite: tile-density-heatmaps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv',
function(err, rows){function unpack(rows, key) {return rows.map(function(row){ return row[key];
})};
var data = [{
lon: unpack(rows, 'Longitude'), lat: unpack(rows, 'Latitude'), radius:10,
z: unpack(rows, 'Magnitude'), type: "densitymap", coloraxis: 'coloraxis',
hoverinfo: 'skip'}];
var layout = {
map: {center: {lon: 60, lat: 30}, style: "outdoors", zoom: 2},
coloraxis: {colorscale: "Viridis"}, title: {text: "Earthquake Magnitude"},
width: 600, height: 400, margin: {t: 30, b: 0}};
Plotly.newPlot('myDiv', data, layout);
})
---
description: How to make a tile-based density heatmap in JavaScript. A density heatmap
uses a variable binding expression to display population density.
display\_as: maps
name: Tile Density Heatmap
page\_type: example\_index
permalink: javascript/tile-density-heatmaps/
redirect\_from: javascript/mapbox-density-heatmaps/
thumbnail: thumbnail/mapbox-density.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","tile-density-heatmaps" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Light Tile (Mapbox) - Requires Token
suite: tile-density-heatmaps
markdown\_content: |
\*\*Mapbox traces are deprecated and may be removed in a future version of Plotly.js.\*\*
Earlier examples use traces that render with [Maplibre GL JS](https://maplibre.org/maplibre-gl-js/docs/).
These traces were introduced in Plotly.js 2.35.0 and replace Mapbox-based tile maps,
which are now deprecated. Here's one of the earlier examples written using the Mapbox-based `densitymapbox` trace.
---
var data = [
{type: "densitymapbox", lon: [10, 20, 30], lat: [15, 25, 35], z: [1, 3, 2],
radius: 50, colorbar: {y: 1, yanchor: 'top', len: 0.45}},
{type: 'densitymapbox', lon: [-10, -20, -30], lat: [15, 25, 35],
radius: [50, 100, 10], colorbar: {y: 0, yanchor: 'bottom', len: 0.45}
}];
var layout = {mapbox: {style: 'light', center: {lat: 20}}, width: 600, height: 400};
var config = {mapboxAccessToken: "your access token"};
Plotly.newPlot('myDiv', data, layout, config);
---
name: Stamen Terrain Tile
suite: tile-density-heatmaps
markdown\_content: |
---
var data = [{type: 'densitymapbox', lon: [10, 20, 30], lat: [15, 25, 35], z: [1, 3, 2]}];
var layout = {width: 600, height: 400, mapbox: {style: 'https://tiles.stadiamaps.com/styles/stamen\_watercolor.json?api\_key=YOUR-API-KEY'}};
Plotly.newPlot('myDiv', data, layout);
---
name: Using "layout.map.layers" to Specify a Base Map
suite: map-layers
markdown\_content: |
If you have access to your own private tile servers, or wish to use a tile server not included in the list above, the recommended approach is to set layout.map.style to "white-bg" and to use layout.map.layers with below to specify a custom base map.
If you omit the below attribute when using this approach, your data will likely be hidden by fully-opaque raster tiles!
---
---
name: Dark tiles
suite: map-layers
---
var url = "https://maplibre.org/maplibre-gl-js/docs/assets/significant-earthquakes-2015.geojson";
d3.json(url, (err, raw) => {
var lon = raw.features.map(f => f.geometry.coordinates[0]);
var lat = raw.features.map(f => f.geometry.coordinates[1]);
var z = raw.features.map(f => f.properties.mag);
var data = [
{ type: "scattermap", lon: lon, lat: lat, z: z, hoverinfo: "y" }
];
var layout = {
map: { style: "dark", zoom: 2, center: { lon: -150, lat: 60 } },
margin: { t: 0, b: 0 }
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: Base Tiles from the USGS
suite: map-layers
markdown\_content: |
Here is an example of a map which uses a public USGS imagery map, specified in layout.map.layers, and which is rendered below the data layer.
---
d3.csv(
"https://raw.githubusercontent.com/plotly/datasets/master/2015\_06\_30\_precipitation.csv",
function(err, rows) {
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var data = [
{
type: "scattermap",
text: unpack(rows, "Globvalue"),
lon: unpack(rows, "Lon"),
lat: unpack(rows, "Lat"),
marker: { color: "fuchsia", size: 4 }
}
];
var layout = {
dragmode: "zoom",
map: {
style: "white-bg",
layers: [
{
sourcetype: "raster",
source: ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"],
below: "traces"
}
],
center: { lat: 38, lon: -90 },
zoom: 3
},
margin: { r: 0, t: 0, b: 0, l: 0 }
};
Plotly.newPlot("myDiv", data, layout);
}
);
---
name: Base Tiles from the USGS, radar overlay from Environment Canada
suite: map-layers
markdown\_content: |
Here is the same example, with in addition, a WMS layer from Environment Canada which displays near-real-time radar imagery in partly-transparent raster tiles, rendered above the go.Scattermap trace, as is the default.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2015\_06\_30\_precipitation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'scattermap', text: unpack(rows, 'Globvalue'),
lon: unpack(rows, 'Lon'), lat: unpack(rows, 'Lat'),
marker: {color: 'fuchsia', size: 4}
}];
var layout = {
dragmode: 'zoom',
map: {
style: 'white-bg',
layers: [
{
"below": 'traces',
"sourcetype": "raster",
"source": [
"https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
]
},
{
sourcetype: "raster",
source: ["https://geo.weather.gc.ca/geomet/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR\_1KM\_RDBR&TILED=true&FORMAT=image/png"]}],
below: 'traces',
center: {lat: 38, lon: -90}, zoom: 4},
margin: {r: 0, t: 0, b: 0, l: 0},
showlegend: false};
Plotly.newPlot('myDiv', data, layout);
});
---
name: How Layers work in Tile-based Maps
suite: map-layers
markdown\_content: |
If your figure contains one or more traces of type `Scattermap`, `Choroplethmap` or `Densitymap`, the `layout` object in your figure contains configuration information for the map itself. The map is composed of various layers, of three different types.

1. `layout.map.style` defines the lowest layers, also known as your "base map"
2. The various traces in `data` are by default rendered above the base map (although this can be controlled via the `below` attribute).
3. `layout.map.layers` is an array that defines more layers that are by default rendered above the traces in `data` (although this can also be controlled via the `below` attribute).

---
---
name: OpenStreetMap tiles
suite: map-layers
markdown\_content: |
Here is a simple map rendered with "open-street-map" tiles.
---
d3.csv(
"https://raw.githubusercontent.com/plotly/datasets/master/2015\_06\_30\_precipitation.csv",
function(err, rows) {
function unpack(rows, key) {
return rows.map(function(row) {
return row[key];
});
}
var data = [
{
type: "scattermap",
text: unpack(rows, "Globvalue"),
lon: unpack(rows, "Lon"),
lat: unpack(rows, "Lat"),
marker: { color: "fuchsia", size: 4 }
}
];
var layout = {
dragmode: "zoom",
map: { style: "open-street-map", center: { lat: 38, lon: -90 }, zoom: 3 },
margin: { r: 0, t: 0, b: 0, l: 0 }
};
Plotly.newPlot("myDiv", data, layout);
}
);
---
name: Mapbox Maps and Access Tokens
suite: map-layers
order: 10
markdown\_content: |
**> Mapbox traces are deprecated and may be removed in a future version of Plotly.js.**
The word "mapbox" in the trace names and `layout.mapbox` refers to the Mapbox GL JS open-source library.
If your basemap in `layout.mapbox.style` uses data from the Mapbox \*service\*,
then you will need to register for a free account at https://mapbox.com/ and obtain a Mapbox Access token.
If your basemap uses data from the [Stadia Maps service](https://www.stadiamaps.com) (see below for details), you'll need to register for a Stadia Maps account and token.
To use a token, provide it as `mapboxAccessToken` in the `setPlotConfig` function, or as a variable that would be passed as an argument of `newPlot`.
If your `layout.mapbox.style` does not use data from the Mapbox service, you do \*not\* need to register for a Mapbox account.

###### Base Maps in `layout.mapbox.style`

The accepted values for `layout.mapbox.style` are one of the following tiles.

1. `"white-bg"` yields an empty white canvas which results in no external HTTP requests
2. `"open-street-map"`, `"carto-positron"`, or `"carto-darkmatter"` yield maps composed of \*raster\* tiles from various public tile servers which do not require signups or access tokens
3. `"stamen-terrain"`, `"stamen-toner"` or `"stamen-watercolor"` yield maps composed of \*raster\* tiles from the [Stadia Maps service](https://stadiamaps.com/) and require a Stadia Maps account and token.
4. `"basic"`, `"streets"`, `"outdoors"`, `"light"`, `"dark"`, `"satellite"`, or `"satellite-streets"` yield maps composed of \*vector\* tiles from the Mapbox service, and \*do\* require a Mapbox Access Token or an on-premise Mapbox installation.
5. A Mapbox service style URL, which requires a Mapbox Access Token or an on-premise Mapbox installation.
6. A Mapbox Style object as defined at https://docs.mapbox.com/mapbox-gl-js/style-spec/

---
---
description: How to make a tile-based maps in JavaScript with various base layers.
display\_as: maps
name: Tile Map Layers
page\_type: example\_index
permalink: javascript/tile-map-layers/
redirect\_from: javascript/mapbox-layers/
thumbnail: thumbnail/mapbox-layers.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","map-layers" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: US Airports Map
suite: scatter-plots-on-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2011\_february\_us\_airport\_traffic.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var scl = [[0,'rgb(5, 10, 172)'],[0.35,'rgb(40, 60, 190)'],[0.5,'rgb(70, 100, 245)'], [0.6,'rgb(90, 120, 245)'],[0.7,'rgb(106, 137, 247)'],[1,'rgb(220, 220, 220)']];
var data = [{
type:'scattergeo',
locationmode: 'USA-states',
lon: unpack(rows, 'long'),
lat: unpack(rows, 'lat'),
hoverinfor: unpack(rows, 'airport'),
text: unpack(rows, 'airport'),
mode: 'markers',
marker: {
size: 8,
opacity: 0.8,
reversescale: true,
autocolorscale: false,
symbol: 'square',
line: {
width: 1,
color: 'rgb(102,102,102)'
},
colorscale: scl,
cmin: 0,
color: unpack(rows, 'cnt'),
colorbar: {
title: {text: 'Incoming Flights February 2011'}
}
}
}];
var layout = {
title: {text: 'Most Trafficked US airports'},
colorbar: true,
geo: {
scope: 'usa',
projection: {
type: 'albers usa'
},
showland: true,
landcolor: 'rgb(250,250,250)',
subunitcolor: 'rgb(217,217,217)',
countrycolor: 'rgb(217,217,217)',
countrywidth: 0.5,
subunitwidth: 0.5
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: Canadian Cities Map
suite: scatter-plots-on-maps
---
var data = [{
type: 'scattergeo',
mode: 'markers+text',
text: [
'Montreal', 'Toronto', 'Vancouver', 'Calgary', 'Edmonton',
'Ottawa', 'Halifax', 'Victoria', 'Winnepeg', 'Regina'
],
lon: [
-73.57, -79.24, -123.06, -114.1, -113.28,
-75.43, -63.57, -123.21, -97.13, -104.6
],
lat: [
45.5, 43.4, 49.13, 51.1, 53.34, 45.24,
44.64, 48.25, 49.89, 50.45
],
marker: {
size: 7,
color: [
'#bebada', '#fdb462', '#fb8072', '#d9d9d9', '#bc80bd',
'#b3de69', '#8dd3c7', '#80b1d3', '#fccde5', '#ffffb3'
],
line: {
width: 1
}
},
name: 'Canadian cities',
textposition: [
'top right', 'top left', 'top center', 'bottom right', 'top right',
'top left', 'bottom right', 'bottom left', 'top right', 'top right'
],
}];
var layout = {
title: {
text: 'Canadian cities',
font: {
family: 'Droid Serif, serif',
size: 16
}
},
geo: {
scope: 'north america',
resolution: 50,
lonaxis: {
'range': [-130, -55]
},
lataxis: {
'range': [40, 70]
},
showrivers: true,
rivercolor: '#fff',
showlakes: true,
lakecolor: '#fff',
showland: true,
landcolor: '#EAEAAE',
countrycolor: '#d3d3d3',
countrywidth: 1.5,
subunitcolor: '#d3d3d3'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: North America Precipitation Map
suite: scatter-plots-on-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2015\_06\_30\_precipitation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
scl = [[0, 'rgb(150,0,90)'],[0.125, 'rgb(0, 0, 200)'],[0.25,'rgb(0, 25, 255)'],[0.375,'rgb(0, 152, 255)'],[0.5,'rgb(44, 255, 150)'],[0.625,'rgb(151, 255, 0)'],[0.75,'rgb(255, 234, 0)'],[0.875,'rgb(255, 111, 0)'],[1,'rgb(255, 0, 0)']];
var data = [{
type: 'scattergeo',
mode: 'markers',
text: unpack(rows, 'Globvalue'),
lon: unpack(rows, 'Lon'),
lat: unpack(rows, 'Lat'),
marker: {
color: unpack(rows, 'Globvalue'),
colorscale: scl,
cmin: 0,
cmax: 1.4,
reversescale: true,
opacity: 0.2,
size: 2,
colorbar:{
thickness: 10,
title: {side:
'right'
},
outlinecolor: 'rgba(68,68,68,0)',
ticks: 'outside',
ticklen: 3,
shoticksuffix: 'last',
ticksuffix: 'inches',
dtick: 0.1
}
},
name: 'NA Precipitation'
}];
var layout = {
geo:{
scope: 'north america',
showland: true,
landcolor: 'rgb(212,212,212)',
subunitcolor: 'rgb(255,255,255)',
countrycolor: 'rgb(255,255,255)',
showlakes: true,
lakecolor: 'rgb(255,255,255)',
showsubunits: true,
showcountries: true,
resolution: 50,
projection: {
type: 'conic conformal',
rotation: {
long: -100
}
},
},
longaxis: {
showgrid: true,
gridwidth: 0.5,
range: [ -140.0, -55.0 ],
dtick: 5
},
lataxis: {
showgrid: true,
gridwidth: 0.5,
range: [ 20.0, 60.0 ],
dtick: 5
},
title: {text: 'North America Precipitation'},
width: 600,
height: 600
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make D3.js-based scatter plots on maps in JavaScript. Scatter
plots on maps highlight geographic areas and can be colored by value.
display\_as: maps
name: Scatter Plots on Maps
permalink: javascript/scatter-plots-on-maps/
redirect\_from: javascript-graphing-library/scatter-plots-on-maps/
thumbnail: thumbnail/scatter-plot-on-maps.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","scatter-plots-on-maps" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
permalink: javascript/maps/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make maps.
name: Maps
layout: langindex
display\_as: maps
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Maps

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","maps" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
name: Choropleth Map of Florida Counties Colored by Political Party
suite: choropleth-maps
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/florida-red-data.json', function(redjson) {
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/florida-blue-data.json', function(bluejson) {
Plotly.newPlot('myDiv', [{
type: 'scattermap',
lat: [46],
lon: [-74]
}], {
title: {text: "Florida Counties"},
height: 600,
width: 600,
map: {
center: {
lat: 28,
lon: -84
},
style: 'light',
zoom: 4.8,
layers: [
{
sourcetype: 'geojson',
source: redjson,
type: 'fill',
color: 'rgba(163,22,19,0.8)'
},
{
sourcetype: 'geojson',
source: bluejson,
type: 'fill',
color: 'rgba(40,0,113,0.8)'
},
]
}
});
});
});
---
name: USA Choropleth Map
suite: choropleth-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2011\_us\_ag\_exports.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'choropleth',
locationmode: 'USA-states',
locations: unpack(rows, 'code'),
z: unpack(rows, 'total exports'),
text: unpack(rows, 'state'),
zmin: 0,
zmax: 17000,
colorscale: [
[0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'],
[0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],
[0.8, 'rgb(117,107,177)'], [1, 'rgb(84,39,143)']
],
colorbar: {
title: {text: 'Millions USD'},
thickness: 0.2
},
marker: {
line:{
color: 'rgb(255,255,255)',
width: 2
}
}
}];
var layout = {
title: {text: '2011 US Agriculture Exports by State'},
geo:{
scope: 'usa',
showlakes: true,
lakecolor: 'rgb(255,255,255)'
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
description: How to make a D3.js-based choropleth map in JavaScript. A choropleth
map shades geographic regions by value.
display\_as: maps
name: Choropleth Maps
permalink: javascript/choropleth-maps/
redirect\_from: javascript-graphing-library/choropleth-maps/
thumbnail: thumbnail/choropleth.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","choropleth-maps" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Choropleth Map of 2014 US Population by State
suite: choropleth-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2014\_usa\_states.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'choropleth',
locationmode: 'USA-states',
locations: unpack(rows, 'Postal'),
z: unpack(rows, 'Population'),
text: unpack(rows, 'State'),
autocolorscale: true
}];
var layout = {
title: {text: '2014 US Popultaion by State'},
geo:{
scope: 'usa',
countrycolor: 'rgb(255, 255, 255)',
showland: true,
landcolor: 'rgb(217, 217, 217)',
showlakes: true,
lakecolor: 'rgb(255, 255, 255)',
subunitcolor: 'rgb(255, 255, 255)',
lonaxis: {},
lataxis: {}
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: World Choropleth Map (Robinson Projection)
suite: choropleth-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2010\_alcohol\_consumption\_by\_country.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'choropleth',
locationmode: 'country names',
locations: unpack(rows, 'location'),
z: unpack(rows, 'alcohol'),
text: unpack(rows, 'location'),
autocolorscale: true
}];
var layout = {
title: {text: 'Pure alcohol consumption
among adults (age 15+) in 2010'},
geo: {
projection: {
type: 'robinson'
}
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: Country GDP Choropleth Map
suite: choropleth-maps
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/2014\_world\_gdp\_with\_codes.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: 'choropleth',
locations: unpack(rows, 'CODE'),
z: unpack(rows, 'GDP (BILLIONS)'),
text: unpack(rows, 'COUNTRY'),
colorscale: [
[0,'rgb(5, 10, 172)'],[0.35,'rgb(40, 60, 190)'],
[0.5,'rgb(70, 100, 245)'], [0.6,'rgb(90, 120, 245)'],
[0.7,'rgb(106, 137, 247)'],[1,'rgb(220, 220, 220)']],
autocolorscale: false,
reversescale: true,
marker: {
line: {
color: 'rgb(180,180,180)',
width: 0.5
}
},
tick0: 0,
zmin: 0,
dtick: 1000,
colorbar: {
autotic: false,
tickprefix: '$',
title: {text: 'GDP
Billions US$'}
}
}];
var layout = {
title: {text: '2014 Global GDP
Source:  [CIA World Factbook](https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html)'},
geo:{
showframe: false,
showcoastlines: false,
projection:{
type: 'mercator'
}
}
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
description: How to make a graph with D3.js-based multiple axes in javascript.
display\_as: multiple\_axes
name: Multiple Axes
permalink: javascript/multiple-axes/
redirect\_from: javascript-graphing-library/multiple-axes/
thumbnail: thumbnail/multiple-axes.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","multiple-axes" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Two Y-Axes
suite: multiple-axes
---
var trace1 = {
x: [1, 2, 3],
y: [40, 50, 60],
name: 'yaxis data',
type: 'scatter'
};
var trace2 = {
x: [2, 3, 4],
y: [4, 5, 6],
name: 'yaxis2 data',
yaxis: 'y2',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
title: {text: 'Double Y Axis Example'},
yaxis: {
title: {
text: 'yaxis title'
}
},
yaxis2: {
title: {
text: 'yaxis2 title',
font: {color: 'rgb(148, 103, 189)'}
},
tickfont: {color: 'rgb(148, 103, 189)'},
overlaying: 'y',
side: 'right'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Multiple Y-Axes
suite: multiple-axes
---
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
name: 'yaxis1 data',
type: 'scatter'
};
var trace2 = {
x: [2, 3, 4],
y: [40, 50, 60],
name: 'yaxis2 data',
yaxis: 'y2',
type: 'scatter'
};
var trace3 = {
x: [4, 5, 6],
y: [40000, 50000, 60000],
name: 'yaxis3 data',
yaxis: 'y3',
type: 'scatter'
};
var trace4 = {
x: [5, 6, 7],
y: [400000, 500000, 600000],
name: 'yaxis4 data',
yaxis: 'y4',
type: 'scatter'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'multiple y-axes example',
font: {color: '#1f77b4'}
},
width: 800,
xaxis: {domain: [0.3, 0.7]},
yaxis: {
title: {
text: 'yaxis title',
font: {color: '#1f77b4'}
},
tickfont: {color: '#1f77b4'}
},
yaxis2: {
title: {
text: 'yaxis2 title',
font: {color: '#ff7f0e'}
},
tickfont: {color: '#ff7f0e'},
anchor: 'free',
overlaying: 'y',
side: 'left',
position: 0.15
},
yaxis3: {
title: {
text: 'yaxis4 title',
font: {color: '#d62728'}
},
tickfont: {color: '#d62728'},
anchor: 'x',
overlaying: 'y',
side: 'right'
},
yaxis4: {
title: {
text: 'yaxis5 title',
font: {color: '#9467bd'}
},
tickfont: {color: '#9467bd'},
anchor: 'free',
overlaying: 'y',
side: 'right',
position: 0.85
}
};
Plotly.newPlot('myDiv', data, layout);
---
permalink: javascript/subplot-charts/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make subplots, insets, and multiple axes charts.
name: Subplots
layout: langindex
display\_as: multiple\_axes
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Subplots

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","multiple\_axes" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
description: How to make an inset graph in D3.js-based javascript charts.
display\_as: multiple\_axes
name: Inset Plots
page\_type: example\_index
permalink: javascript/insets/
redirect\_from: javascript-graphing-library/insets/
thumbnail: thumbnail/insets.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","insets" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Simple Inset Graph
suite: insets
---
var trace1 = {
x: [1, 2, 3],
y: [4, 3, 2],
type: 'scatter'
};
var trace2 = {
x: [20, 30, 40],
y: [30, 40, 50],
xaxis: 'x2',
yaxis: 'y2',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
yaxis2: {
domain: [0.6, 0.95],
anchor: 'x2'
},
xaxis2: {
domain: [0.6, 0.95],
anchor: 'y2'
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make 3D Subplots in javascript.
display\_as: multiple\_axes
name: 3D Subplots
page\_type: example\_index
permalink: javascript/3d-subplots/
redirect\_from: javascript-graphing-library/3d-subplots/
thumbnail: thumbnail/3d-subplots.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-subplots" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Multiple 3D Subplots
suite: 3d-subplots
---
function getrandom(num , mul) {
var value = [ ];
for ( i=0; i <= num; i++ ) {
var rand = Math.random() \* mul;
value.push(rand);
}
return value;
}
var trace1 = {
opacity: 0.5,
color: 'rgba(255,127,80,0.7)',
type: 'mesh3d',
x: getrandom(50 , -75),
y: getrandom(50 , 75),
z: getrandom(50 , 75),
scene: "scene1"
};
var trace2 = {
opacity: 0.5,
color: 'pink',
type: 'mesh3d',
x: getrandom(50 , -75),
y: getrandom(50 , 75),
z: getrandom(50 , 75),
scene: "scene2"
};
var trace3 = {
opacity:0.4,
color:'rgb(033,255,100)',
type: 'mesh3d',
x: getrandom(50 , -75),
y: getrandom(50 , -75),
z: getrandom(50 , -75),
scene: "scene3",
};
var trace4 = {
opacity: 0.5,
color:'rgb(200,100,200)',
type: 'mesh3d',
x: getrandom(50 , -75),
y: getrandom(50 , 75),
z: getrandom(50 , 75),
scene: "scene4"
};
var trace5 = {
opacity: 0.5,
color:'rgb(00,150,200)',
type: 'mesh3d',
x: getrandom(50 , 100),
y: getrandom(50 , 100),
z: getrandom(50 , 100),
scene: "scene5",
}
var layout = {
scene1: {
domain: {
x: [0.0, 0.5],
y: [0.5, 1.0]
},},
scene2: {
domain: {
x: [0.5, 1],
y: [0.5, 1.0]
}},
scene3: {
domain: {
x: [0.0, 0.33],
y: [0, 0.5]
},},
scene4: {
domain: {
x: [0.33, 0.66],
y: [0, 0.5]
}},
scene5: {
domain: {
x: [0.66, 0.99],
y: [0, 0.5]
},},
height: 600,
margin: {
l: 0,
r: 0,
b: 0,
t: 0,
pad: 0
},
}
Plotly.newPlot('myDiv', [trace1,trace2,trace3,trace4,trace5], layout);
---
name: Table and Chart Subplot
suite: subplot\_table
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
// header values
var headerNames = d3.keys(rows[0]);
var headerValues = [headerNames[1],headerNames[2],
headerNames[3],headerNames[4]];
// cell values
var cellValues = [];
for (i = 0; i < headerValues.length; i++) {
cellValue = unpack(rows, headerValues[i]);
cellValues[i] = cellValue;
}
// clean date
for (i = 0; i < cellValues[0].length; i++) {
var dateValue = cellValues[0][i].split(' ')[0]
cellValues[0][i] = dateValue
}
// create table
var table = {
type: 'table',
columnwidth: [150,200,200,150],
columnorder: [0,1,2,3],
header: {
values: headerValues,
align: "center",
line: {width: 1, color: 'rgb(50, 50, 50)'},
fill: {color: ['rgb(235, 100, 230)']},
font: {family: "Arial", size: 11, color: "white"}
},
cells: {
values: cellValues,
align: ["center", "center"],
line: {color: "black", width: 1},
fill: {color: ['rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']},
font: {family: "Arial", size: 10, color: ["black"]}
},
xaxis: 'x',
yaxis: 'y',
domain: {x: [0,0.4], y: [0,1]}
}
// create 1st plot
var trace1 = {
x: unpack(rows, 'Date'),
y: unpack(rows, 'Hash-rate'),
xaxis: 'x1',
yaxis: 'y1',
mode: 'lines',
line: {width: 2, color: '#9748a1'},
name: 'hash-rate-TH/s'
}
// create 2nd plot
var trace2 = {
x: unpack(rows, 'Date'),
y: unpack(rows, 'Mining-revenue-USD'),
xaxis: 'x2',
yaxis: 'y2',
mode: 'lines',
line: {width: 2, color: '#b04553'},
name: 'Mining-revenue-USD'
}
// create 3rd plot
var trace3 = {
x: unpack(rows, 'Date'),
y: unpack(rows, 'Transaction-fees-BTC'),
xaxis: 'x3',
yaxis: 'y3',
mode: 'lines',
line: {width: 2, color: '#af7bbd'},
name: 'Transaction-fees-BTC'
}
var data = [table,trace1,trace2,trace3]
// define subplot axes
var axis = {
showline: true,
zeroline: false,
showgrid: true,
mirror:true,
ticklen: 4,
gridcolor: '#ffffff',
tickfont: {size: 10},
}
var axis1 = {domain: [0.5, 1], anchor: 'y1', showticklabels: false}
var axis2 = {domain: [0.5, 1], anchor: 'y2', showticklabels: false}
var axis3 = {domain: [0.5, 1], anchor: 'y3'}
var axis4 = {domain: [0.66, 0.98], anchor: 'x1', hoverformat: '.2f'}
var axis5 = {domain: [0.34, 0.64], anchor: 'x2', tickprefix: '$', hoverformat: '.2f'}
var axis6 = {domain: [0.0, 0.32], anchor: 'x3', tickprefix: '\u20BF', hoverformat: '.2f'}
// define layout
var layout = {
title: {text: "Bitcoin mining stats for 180 days"},
plot\_bgcolor: 'rgba(228, 222, 249, 0.65)',
showlegend: false,
xaxis1: Object.assign(axis1,axis),
xaxis2: Object.assign(axis2,axis),
xaxis3: Object.assign(axis3,axis),
yaxis1: Object.assign(axis4,axis),
yaxis2: Object.assign(axis5,axis),
yaxis3: Object.assign(axis6,axis)
}
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make a D3.js-based table subplots in javascript.
display\_as: multiple\_axes
name: Table Subplots
page\_type: example\_index
permalink: javascript/table-subplots/
thumbnail: thumbnail/table\_subplots.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","subplot\_table" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Subplots with Shared Axes
suite: subplots
---
var trace1 = {
x: [1, 2, 3],
y: [2, 3, 4],
type: 'scatter'
};
var trace2 = {
x: [20, 30, 40],
y: [5, 5, 5],
xaxis: 'x2',
yaxis: 'y',
type: 'scatter'
};
var trace3 = {
x: [2, 3, 4],
y: [600, 700, 800],
xaxis: 'x',
yaxis: 'y3',
type: 'scatter'
};
var trace4 = {
x: [4000, 5000, 6000],
y: [7000, 8000, 9000],
xaxis: 'x4',
yaxis: 'y4',
type: 'scatter'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
grid: {
rows: 2,
columns: 2,
subplots:[['xy','x2y'], ['xy3','x4y4']],
roworder:'bottom to top'
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make D3.js-based subplots in Plotly.js. Seven examples of stacked,
custom-sized, and gridded subplots.
display\_as: multiple\_axes
name: Subplots
page\_type: example\_index
permalink: javascript/subplots/
redirect\_from: javascript-graphing-library/subplots/
thumbnail: thumbnail/subplots.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","subplots" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Stacked Subplots with a Shared X-Axis
suite: subplots
---
var trace1 = {
x: [0, 1, 2],
y: [10, 11, 12],
type: 'scatter'
};
var trace2 = {
x: [2, 3, 4],
y: [100, 110, 120],
yaxis: 'y2',
type: 'scatter'
};
var trace3 = {
x: [3, 4, 5],
y: [1000, 1100, 1200],
yaxis: 'y3',
type: 'scatter'
};
var data = [trace1, trace2, trace3];
var layout = {
yaxis: {domain: [0, 0.33]},
legend: {traceorder: 'reversed'},
yaxis2: {domain: [0.33, 0.66]},
yaxis3: {domain: [0.66, 1]}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Simple Subplot
suite: subplots
---
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: 'scatter'
};
var trace2 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: 'x2',
yaxis: 'y2',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
grid: {rows: 1, columns: 2, pattern: 'independent'},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Multiple Subplots
suite: subplots
---
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: 'scatter'
};
var trace2 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: 'x2',
yaxis: 'y2',
type: 'scatter'
};
var trace3 = {
x: [300, 400, 500],
y: [600, 700, 800],
xaxis: 'x3',
yaxis: 'y3',
type: 'scatter'
};
var trace4 = {
x: [4000, 5000, 6000],
y: [7000, 8000, 9000],
xaxis: 'x4',
yaxis: 'y4',
type: 'scatter'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
grid: {rows: 2, columns: 2, pattern: 'independent'},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Multiple Custom Sized Subplots
suite: subplots
---
var trace1 = {
x: [1, 2],
y: [1, 2],
type: 'scatter',
name: '(1,1)'
};
var trace2 = {
x: [1, 2],
y: [1, 2],
type: 'scatter',
name: '(1,2)',
xaxis: 'x2',
yaxis: 'y2'
};
var trace3 = {
x: [1, 2],
y: [1, 2],
type: 'scatter',
name: '(1,2)',
xaxis: 'x3',
yaxis: 'y3'
};
var trace4 = {
x: [1, 2],
y: [1, 2],
type: 'scatter',
name: '(1,2)',
xaxis: 'x4',
yaxis: 'y4'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {text: 'Multiple Custom Sized Subplots'},
xaxis: {
domain: [0, 0.45],
anchor: 'y1'
},
yaxis: {
domain: [0.5, 1],
anchor: 'x1'
},
xaxis2: {
domain: [0.55, 1],
anchor: 'y2'
},
yaxis2: {
domain: [0.8, 1],
anchor: 'x2'
},
xaxis3: {
domain: [0.55, 1],
anchor: 'y3'
},
yaxis3: {
domain: [0.5, 0.75],
anchor: 'x3'
},
xaxis4: {
domain: [0, 1],
anchor: 'y4'
},
yaxis4: {
domain: [0, 0.45],
anchor: 'x4'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Custom Sized Subplot
suite: subplots
---
var trace1 = {
x: [1, 2, 3],
y: [4, 5, 6],
type: 'scatter'
};
var trace2 = {
x: [20, 30, 40],
y: [50, 60, 70],
xaxis: 'x2',
yaxis: 'y2',
type: 'scatter'
};
var data = [trace1, trace2];
var layout = {
xaxis: {domain: [0, 0.7]},
yaxis2: {anchor: 'x2'},
xaxis2: {domain: [0.8, 1]}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Stacked Subplots
suite: subplots
---
var trace1 = {
x: [0, 1, 2],
y: [10, 11, 12],
type: 'scatter'
};
var trace2 = {
x: [2, 3, 4],
y: [100, 110, 120],
xaxis: 'x2',
yaxis: 'y2',
type: 'scatter'
};
var trace3 = {
x: [3, 4, 5],
y: [1000, 1100, 1200],
xaxis: 'x3',
yaxis: 'y3',
type: 'scatter'
};
var data = [trace1, trace2, trace3];
var layout = {
grid: {
rows: 3,
columns: 1,
pattern: 'independent',
roworder: 'bottom to top'}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make Mixed Subplots in javascript.
display\_as: multiple\_axes
name: Mixed Subplots
page\_type: example\_index
permalink: javascript/mixed-subplots/
thumbnail: thumbnail/mixed\_subplot.JPG
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","mixed-subplots" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Mixed Subplots
suite: mixed-subplots
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/volcano\_db.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var trace1 = {
x: unpack(rows, 'Status'),
y: unpack(rows, 'Type'),
z: unpack(rows, 'Elev'),
marker: {
size: 2,
color: unpack(rows, 'Elev'),
colorscale: 'Reds',
line: {color: 'transparent'}
},
mode: 'markers',
type: 'scatter3d',
text: unpack(rows, 'Country'),
hoverinfo: 'x+y+z+text',
showlegend: false
};
var x = unpack(rows, 'Elev');
var trace2 = {
x: unpack(rows, 'Elev'),
type: 'histogram',
hoverinfo: 'x+y',
showlegend: false,
xaxis: 'x2',
yaxis: 'y2',
marker: {
color: 'red'
}};
var trace3 = {
geo: 'geo3',
type:'scattergeo',
locationmode: 'world',
lon: unpack(rows, 'Longitude'),
lat: unpack(rows, 'Latitude'),
hoverinfo: 'text',
text: unpack(rows, 'Elev'),
mode: 'markers',
showlegend: false,
marker: {
size: 4,
color: unpack(rows, 'Elev'),
colorscale: 'Reds',
opacity: 0.8,
symbol: 'circle',
line: {
width: 1
}
}
};
var data = [trace1, trace2, trace3];
var layout = {
paper\_bgcolor: 'black',
plot\_bgcolor: 'black',
title: {text: 'Volcano Database: Elevation'},
font: {color: 'white'},
colorbar: true,
annotations: [{
x: 0,
y: 0,
xref: 'paper',
yref: 'paper',
text: 'Source: NOAA',
showarrow: false
}],
geo3: {
domain: {
x: [0, 0.45],
y: [0.02, 0.98]
},
scope: 'world',
projection: {
type: 'orthographic'
},
showland: true,
showocean: true,
showlakes: true,
landcolor: 'rgb(250,250,250)',
lakecolor: 'rgb(127,205,255)',
oceancolor: 'rgb(6,66,115)',
subunitcolor: 'rgb(217,217,217)',
countrycolor: 'rgb(217,217,217)',
countrywidth: 0.5,
subunitwidth: 0.5,
bgcolor: 'black'
},
scene: {domain: {
x: [0.55, 1],
y: [0, 0.6]
},
xaxis: {
title: {
text: 'Status'
},
showticklabels: false,
showgrid: true,
gridcolor: 'white'
},
yaxis: {
title: {
text: 'Type'
},
showticklabels: false,
showgrid: true,
gridcolor: 'white'
},
zaxis: {
title: {
text: 'Elev'
},
showgrid: true,
gridcolor: 'white'
}
},
yaxis2: {
anchor: 'x2',
domain: [0.7, 1],
showgrid: false
},
xaxis2: {
tickangle: 45,
anchor: 'y2',
ticksuffix: 'm',
domain: [0.6, 1]},
};
Plotly.newPlot("myDiv", data, layout, {showLink: false});
});
---
name: Getting Started
permalink: javascript/getting-started/
description: Getting Started with plotly
redirect\_from: javascript-graphing-library/getting-started/
---

## NPM

You can [install Plotly.js from NPM](https://www.npmjs.com/package/plotly.js) via `npm install plotly.js-dist` or `yarn install plotly.js-dist`

## plotly.js CDN

You can also use the ultrafast plotly.js CDN link. This CDN is graciously provided by the incredible team at [Fastly](https://fastly.com).

```
<head>
               <script src="https://cdn.plot.ly/plotly-{{site.data.jsversion.version}}.min.js" charset="utf-8"></script>
</head>
```

## Download

Download the minified plotly.js source code and dependencies.

Include the downloaded scripts before the end of the </head> tag in your HTML document:

```
<head>
	<script src="plotly-{{site.data.jsversion.version}}.min.js" charset="utf-8"></script>
</head>

```

[Download plotly.js](https://cdn.plot.ly/plotly-%7B%7Bsite.data.jsversion.version%7D%7D.min.js)

## Start plotting!

In your HTML document, create an empty DIV to draw the graph in:

```
<div id="tester" style="width:600px;height:250px;"></div>
```

Now you can make interactive plotly.js charts using `Plotly.newPlot()`.

```
<script>
	TESTER = document.getElementById('tester');
	Plotly.newPlot( TESTER, [{
	x: [1, 2, 3, 4, 5],
	y: [1, 2, 4, 8, 16] }], {
	margin: { t: 0 } } );
</script>
```

Now you can pass Plotly.newPlot() either the ID of the DIV ("tester") or the DIV DOM element (`TESTER`).

## Hello World Example

[more examples](/javascript/)

Distribution powered by

[![Fastly](https://www.fastly.com/sites/default/files/fastly_logo.png)](https://www.fastly.com/open-source)
---
permalink: javascript/3d-charts/
description: Plotly.js makes interactive, publication-quality graphs online. Examples of how to make 3D graphs such as 3D scatter and surface charts.
name: 3D Charts
layout: langindex
display\_as: 3d\_charts
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js 3D Charts

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","3d\_charts" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
name: Basic 3D Cone
suite: 3dcone
---
var data = [{
type: "cone",
x: [1], y: [1], z: [1],
u: [1], v: [1], w: [0]
}]
var layout = {
"scene": {
"camera": {
"eye": {x: -0.76, y: 1.8, z: 0.92}
}
}
}
Plotly.newPlot('myDiv',data,layout)
---
name: Multiple 3D Cone
suite: 3dcone
---
var data = [{
type: "cone",
x: [1, 2, 3],
y: [1, 2, 3],
z: [1, 2, 3],
u: [1, 0, 0],
v: [0, 3, 0],
w: [0, 0, 2],
sizemode: "absolute",
sizeref: 2,
anchor: "tip",
colorbar: {
x: 0,
xanchor: "right",
side: "left"
}
}]
var layout = {
scene: {
domain: {x: [0, 1]},
camera: {
eye: {x: -1.57, y: 1.36, z: 0.58}
}
},
width: 800
}
Plotly.newPlot('myDiv', data, layout)
---
name: 3D Cone Lighting
suite: 3dcone
---
var data = [{
type: "cone",
name: "base",
x: [1, 1, 1],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false
},
{
type: "cone",
name: "opacity:0.3",
x: [2, 2, 2],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
opacity: 0.3
},
{
type: "cone",
name: "lighting.ambient:0.3",
x: [3, 3, 3],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
lighting: {ambient: 0.3}
},
{
type: "cone",
name: "lighting.diffuse:0.3",
x: [4, 4, 4],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
lighting: {diffuse: 0.3}
},
{
type: "cone",
name: "lighting.specular:2",
x: [5, 5, 5],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
lighting: {specular: 2}
},
{
type: "cone",
name: "lighting.roughness:1",
x: [6, 6, 6],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
lighting: {roughness: 1}
},
{
type: "cone",
name: "lighting.fresnel:2",
x: [7, 7, 7],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
lighting: {fresnel: 2}
},
{
type: "cone",
name: "lighting.position x:0,y:0,z:1e5",
x: [8, 8, 8],
y: [1, 2, 3],
z: [1, 1, 1],
u: [1, 2, 3],
v: [1, 1, 2],
w: [4, 4, 1],
hoverinfo: "u+v+w+name",
showscale: false,
lightposition: {x: 0, y: 0, z: 1e5}
}]
var layout = {
scene: {
aspectmode: "data",
camera: {
eye: {x: 0.05, y: -2.6, z: 2}
}
},
width: 500,
height: 500,
margin: {t: 0, b: 0, l: 0, r: 0}
}
Plotly.newPlot('myDiv',data,layout)
---
description: How to make 3D cone plots in javascript.
display\_as: 3d\_charts
name: 3D Cone Plots
permalink: javascript/cone-plot/
redirect\_from: javascript/3d-cone/
thumbnail: thumbnail/3dcone.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3dcone" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Trisurf Plot
suite: trisurf
---
function trisurf(Tri, X, Y, Z, C) {
var data = {
type: 'mesh3d',
x: X,
y: Y,
z: Z,
i: Tri.map(function(f) { return f[0] }),
j: Tri.map(function(f) { return f[1] }),
k: Tri.map(function(f) { return f[2] }),
facecolor: C,
flatshading: true,
}
Plotly.newPlot('myDiv', [data])
}
//Example usage
trisurf(
[
[0, 1, 2],
[0, 2, 3],
[0, 3, 1],
[1, 2, 3]
],
[0, 1, 0, 0],
[0, 0, 1, 0],
[0, 0, 0, 1],
[
'rgb(0, 0, 0)',
'rgb(255, 0, 0)',
'rgb(0, 255, 0)',
'rgb(0, 0, 255)'
])
---
description: How to make Trisurf in javascript.
display\_as: 3d\_charts
name: Tri-Surf Plots
permalink: javascript/trisurf/
thumbnail: thumbnail/trisurf.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","trisurf" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Extending the Cube Example for Boxes
suite: trisurf
---
// Note x, y, z define the vertices for a unit cube
var x = [0, 0, 1, 1, 0, 0, 1, 1];
var y = [0, 1, 1, 0, 0, 1, 1, 0];
var z = [0, 0, 0, 0, 1, 1, 1, 1];
var i = [7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7];
var j = [3, 4, 1, 2, 5, 6, 5, 5, 0, 1, 2, 2];
var k = [0, 7, 2, 3, 6, 7, 1, 2, 5, 5, 7, 6];
var range\_x = [-2, 2];
var range\_y = [-3, 3];
var range\_z = [-1, 1];
function rectangle(x, y, z, range\_x, range\_y, range\_z) {
if (range\_x.length !== 2 || range\_y.length !== 2 || range\_z.length !== 2) {
throw 'Ranges must contain 2 values';
}
// we will forego other checks for to limit the length of the example
x = x.map(function(e, i) {
return range\_x[e];
});
y = y.map(function(e, i) {
return range\_y[e];
});
z = z.map(function(e, i) {
return range\_z[e];
});
return {x: x, y: y, z: z};
}
result = rectangle(x, y, z, range\_x, range\_y, range\_z);
// x, y, z now represent the vertices for the rectangular box with
// the ranges specified above
x = result.x;
y = result.y;
z = result.z;
var facecolor = [
'rgb(50, 200, 200)',
'rgb(100, 200, 255)',
'rgb(150, 200, 115)',
'rgb(200, 200, 50)',
'rgb(230, 200, 10)',
'rgb(255, 140, 0)'
];
facecolor2 = new Array(facecolor.length \* 2);
facecolor.forEach(function(x, i) {
facecolor2[i \* 2 + 1] = facecolor2[i \* 2] = x;
});
var data = {
x: x,
y: y,
z: z,
i: i,
j: j,
k: k,
facecolor: facecolor2,
type: 'mesh3d'
};
Plotly.newPlot('myDiv', [data]);
---
name: Trisurf Cube
suite: trisurf
---
var x = [0, 0, 1, 1, 0, 0, 1, 1]
var y = [0, 1, 1, 0, 0, 1, 1, 0]
var z = [0, 0, 0, 0, 1, 1, 1, 1]
var i = [7, 0, 0, 0, 4, 4, 2, 6, 4, 0, 3, 7]
var j = [3, 4, 1, 2, 5, 6, 5, 5, 0, 1, 2, 2]
var k = [0, 7, 2, 3, 6, 7, 1, 2, 5, 5, 7, 6]
var facecolor = [
'rgb(50, 200, 200)',
'rgb(100, 200, 255)',
'rgb(150, 200, 115)',
'rgb(200, 200, 50)',
'rgb(230, 200, 10)',
'rgb(255, 140, 0)'
]
facecolor2 = new Array(facecolor.length \* 2);
facecolor.forEach(function(x, i) {
facecolor2[i \* 2 + 1] = facecolor2[i \* 2] = x;
});
var data = {
x: x,
y: y,
z: z,
i: i,
j: j,
k: k,
facecolor: facecolor2,
type: 'mesh3d'
}
Plotly.newPlot('myDiv', [data])
---
name: Multiple 3D Surface Plots
suite: 3d-surface
---
z1 = [
[8.83,8.89,8.81,8.87,8.9,8.87],
[8.89,8.94,8.85,8.94,8.96,8.92],
[8.84,8.9,8.82,8.92,8.93,8.91],
[8.79,8.85,8.79,8.9,8.94,8.92],
[8.79,8.88,8.81,8.9,8.95,8.92],
[8.8,8.82,8.78,8.91,8.94,8.92],
[8.75,8.78,8.77,8.91,8.95,8.92],
[8.8,8.8,8.77,8.91,8.95,8.94],
[8.74,8.81,8.76,8.93,8.98,8.99],
[8.89,8.99,8.92,9.1,9.13,9.11],
[8.97,8.97,8.91,9.09,9.11,9.11],
[9.04,9.08,9.05,9.25,9.28,9.27],
[9,9.01,9,9.2,9.23,9.2],
[8.99,8.99,8.98,9.18,9.2,9.19],
[8.93,8.97,8.97,9.18,9.2,9.18]
];
z2 = [];
for (var i=0;i<z1.length;i++ ) {
z2\_row = [];
for(var j=0;j<z1[i].length;j++) {
z2\_row.push(z1[i][j]+1);
}
z2.push(z2\_row);
}
z3 = []
for (var i=0;i<z1.length;i++ ) {
z3\_row = [];
for(var j=0;j<z1[i].length;j++) {
z3\_row.push(z1[i][j]-1);
}
z3.push(z3\_row);
}
var data\_z1 = {z: z1, type: 'surface'};
var data\_z2 = {z: z2, showscale: false, opacity:0.9, type: 'surface'};
var data\_z3 = {z: z3, showscale: false, opacity:0.9, type: 'surface'};
Plotly.newPlot('myDiv', [data\_z1, data\_z2, data\_z3]);
---
name: Topographical 3D Surface Plot
suite: 3d-surface
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/api\_docs/mt\_bruno\_elevation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data=[ ]
for(i=0;i<24;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface'
}];
var layout = {
title: {
text: 'Mt Bruno Elevation'
},
autosize: false,
width: 500,
height: 500,
margin: {
l: 65,
r: 50,
b: 65,
t: 90,
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make 3D surface plots in javascript.
display\_as: 3d\_charts
name: 3D Surface Plots
page\_type: example\_index
permalink: javascript/3d-surface-plots/
redirect\_from: javascript-graphing-library/3d-surface-plots/
thumbnail: thumbnail/3d-surface.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-surface" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Surface Plot With Contours
suite: 3d-surface
order: 0.5
markdown\_content: |
Display and customize contour data for each axis using the `contours` attribute ([reference](/javascript/reference/surface/#surface-contours)).
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/api\_docs/mt\_bruno\_elevation.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var z\_data=[ ]
for(i=0;i<24;i++)
{
z\_data.push(unpack(rows,i));
}
var data = [{
z: z\_data,
type: 'surface',
contours: {
z: {
show:true,
usecolormap: true,
highlightcolor:"#42f462",
project:{z: true}
}
}
}];
var layout = {
title: {
text: 'Mt Bruno Elevation With Projected Contours'
},
scene: {camera: {eye: {x: 1.87, y: 0.88, z: -0.64}}},
autosize: false,
width: 500,
height: 500,
margin: {
l: 65,
r: 50,
b: 65,
t: 90,
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: 3D Scatter Plot
suite: 3d-scatter
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/3d-scatter.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row)
{ return row[key]; });}
var trace1 = {
x:unpack(rows, 'x1'), y: unpack(rows, 'y1'), z: unpack(rows, 'z1'),
mode: 'markers',
marker: {
size: 12,
line: {
color: 'rgba(217, 217, 217, 0.14)',
width: 0.5},
opacity: 0.8},
type: 'scatter3d'
};
var trace2 = {
x:unpack(rows, 'x2'), y: unpack(rows, 'y2'), z: unpack(rows, 'z2'),
mode: 'markers',
marker: {
color: 'rgb(127, 127, 127)',
size: 12,
symbol: 'circle',
line: {
color: 'rgb(204, 204, 204)',
width: 1},
opacity: 0.8},
type: 'scatter3d'};
var data = [trace1, trace2];
var layout = {margin: {
l: 0,
r: 0,
b: 0,
t: 0
}};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make 3D scatter plots in javascript.
display\_as: 3d\_charts
name: 3D Scatter Plots
page\_type: example\_index
permalink: javascript/3d-scatter-plots/
redirect\_from: javascript-graphing-library/3d-scatter-plots/
thumbnail: thumbnail/3d-scatter.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-scatter" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: 3D Point Clustering
suite: 3d-cluster
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/alpha\_shape.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
x: unpack(rows, 'x'),
y: unpack(rows, 'y'),
z: unpack(rows, 'z'),
mode: 'markers',
type: 'scatter3d',
marker: {
color: 'rgb(23, 190, 207)',
size: 2
}
},{
alphahull: 7,
opacity: 0.1,
type: 'mesh3d',
x: unpack(rows, 'x'),
y: unpack(rows, 'y'),
z: unpack(rows, 'z')
}];
var layout = {
autosize: true,
height: 480,
scene: {
aspectratio: {
x: 1,
y: 1,
z: 1
},
camera: {
center: {
x: 0,
y: 0,
z: 0
},
eye: {
x: 1.25,
y: 1.25,
z: 1.25
},
up: {
x: 0,
y: 0,
z: 1
}
},
xaxis: {
type: 'linear',
zeroline: false
},
yaxis: {
type: 'linear',
zeroline: false
},
zaxis: {
type: 'linear',
zeroline: false
}
},
title: {
text: '3d point clustering'
},
width: 477
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make a 3D Cluster Graph in JavaScript.
display\_as: 3d\_charts
name: 3D Cluster Graph
permalink: javascript/3d-point-clustering/
redirect\_from: javascript-graphing-library/3d-point-clustering/
thumbnail: thumbnail/3d-clusters.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-cluster" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
description: How to make a D3.js-based ribbon plot in JavaScript.
display\_as: 3d\_charts
name: Ribbon Plots
page\_type: example\_index
permalink: javascript/ribbon-plots/
redirect\_from: javascript-graphing-library/ribbon-plots/
thumbnail: thumbnail/ribbon-plot.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","ribbon-plot" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Ribbon Plot
suite: ribbon-plot
---
d3.json('https://raw.githubusercontent.com/plotly/datasets/master/3d-ribbon.json', function(figure){
var trace1 = {
x:figure.data[0].x, y:figure.data[0].y, z:figure.data[0].z,
name: '',
colorscale: figure.data[0].colorscale,
type: 'surface',
showscale: false
}
var trace2 = {
x:figure.data[1].x, y:figure.data[1].y, z:figure.data[1].z,
name: '',
colorscale: figure.data[1].colorscale,
type: 'surface',
showscale: false
}
var trace3 = {
x:figure.data[2].x, y:figure.data[2].y, z:figure.data[2].z,
colorscale: figure.data[2].colorscale,
type: 'surface',
showscale: false
}
var trace4 = {
x:figure.data[3].x, y:figure.data[3].y, z:figure.data[3].z,
colorscale: figure.data[3].colorscale,
type: 'surface',
showscale: false
}
var trace5 = {
x:figure.data[4].x, y:figure.data[4].y, z:figure.data[4].z,
colorscale: figure.data[4].colorscale,
type: 'surface',
showscale: false
}
var trace6 = {
x:figure.data[5].x, y:figure.data[5].y, z:figure.data[5].z,
colorscale: figure.data[5].colorscale,
type: 'surface',
showscale: false
}
var trace7 = {
x:figure.data[6].x, y:figure.data[6].y, z:figure.data[6].z,
name: '',
colorscale: figure.data[6].colorscale,
type: 'surface',
showscale: false
}
var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7];
var layout = {
title: {
text: 'Ribbon Plot'
},
showlegend: false,
autosize: true,
width: 600,
height: 600,
scene: {
xaxis: {title: {text: 'Sample #'}},
yaxis: {title: {text: 'Wavelength'}},
zaxis: {title: {text: 'OD'}}
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
name: 3D Mesh Plot with Alphahull
suite: 3d-mesh
---
// Generating random data..
a=[]; b=[]; c=[];
for(i=0;i<50;i++)
{
var a\_ = Math.random();
a.push(a\_);
var b\_ = Math.random();
b.push(b\_);
var c\_ = Math.random();
c.push(c\_);
}
// Plotting the mesh
var data=[
{
alphahull:5,
opacity:0.8,
color:'rgb(200,100,300)',
type: 'mesh3d',
x: a,
y: b,
z: c,
}
];
Plotly.newPlot('myDiv', data);
---
name: 3D Mesh Cube
suite: 3d-mesh
---
var intensity = [0, 0.14285714285714285, 0.2857142857142857, 0.42857142857142855, 0.5714285714285714, 0.7142857142857143, 0.8571428571428571, 1];
var data = [{
type: "mesh3d",
x: [0, 0, 1, 1, 0, 0, 1, 1],
y: [0, 1, 1, 0, 0, 1, 1, 0],
z: [0, 0, 0, 0, 1, 1, 1, 1],
i: [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
j: [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
k: [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
intensity: intensity,
colorscale: [
[0, 'rgb(255, 0, 255)'],
[0.5, 'rgb(0, 255, 0)'],
[1, 'rgb(0, 0, 255)']
]
}
];
Plotly.newPlot('myDiv', data, {});
---
description: How to make 3D mesh plots in javascript.
display\_as: 3d\_charts
name: 3D Mesh Plots
page\_type: example\_index
permalink: javascript/3d-mesh/
thumbnail: thumbnail/3d-mesh.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-mesh" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Simple 3D Mesh Plot
suite: 3d-mesh
sitemap: true
---
// Generating random data..
a=[]; b=[]; c=[];
for(i=0;i<50;i++)
{
var a\_ = Math.random();
a.push(a\_);
var b\_ = Math.random();
b.push(b\_);
var c\_ = Math.random();
c.push(c\_);
}
// Plotting the mesh
var data=[
{
opacity:0.8,
color:'rgb(300,100,200)',
type: 'mesh3d',
x: a,
y: b,
z: c,
}
];
Plotly.newPlot('myDiv', data);
---
name: 3D Mesh Tetrahedron
suite: 3d-mesh
---
var data = [{
type: "mesh3d",
x: [0, 1, 2, 0],
y: [0, 0, 1, 2],
z: [0, 2, 0, 1],
i: [0, 0, 0, 1],
j: [1, 2, 3, 2],
k: [2, 3, 1, 3],
intensity: [0, 0.33, 0.66, 1],
colorscale: [
[0, 'rgb(255, 0, 0)'],
[0.5, 'rgb(0, 255, 0)'],
[1, 'rgb(0, 0, 255)']
]
}
];
Plotly.newPlot('myDiv', data, {});
---
name: 3D Line + Markers Plot
suite: 3d-line
---
var pointCount = 31;
var i, r;
var x = [];
var y = [];
var z = [];
var c = [];
for(i = 0; i < pointCount; i++)
{
r = 10 \* Math.cos(i / 10);
x.push(r \* Math.cos(i));
y.push(r \* Math.sin(i));
z.push(i);
c.push(i)
}
Plotly.newPlot('myDiv', [{
type: 'scatter3d',
mode: 'lines+markers',
x: x,
y: y,
z: z,
line: {
width: 6,
color: c,
colorscale: "Viridis"},
marker: {
size: 3.5,
color: c,
colorscale: "Greens",
cmin: -20,
cmax: 50
}},
]);
---
name: 3D Line Plot
suite: 3d-line
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/3d-line1.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row)
{ return row[key]; }); }
var x = unpack(rows , 'x');
var y = unpack(rows , 'y');
var z = unpack(rows , 'z');
var c = unpack(rows , 'color');
Plotly.newPlot('myDiv', [{
type: 'scatter3d',
mode: 'lines',
x: x,
y: y,
z: z,
opacity: 1,
line: {
width: 6,
color: c,
reversescale: false
}
}], {
height: 640
});
});
---
name: 3D Line Spiral Plot
suite: 3d-line
---
var pointCount = 3142;
var i, r;
var x = [];
var y = [];
var z = [];
var c = [];
for(i = 0; i < pointCount; i++)
{
r = i \* (pointCount - i);
x.push(r \* Math.cos(i / 30));
y.push(r \* Math.sin(i / 30));
z.push(i);
c.push(i)
}
Plotly.newPlot('myDiv', [{
type: 'scatter3d',
mode: 'lines',
x: x,
y: y,
z: z,
opacity: 0.7,
line: {
width: 10,
color: c,
colorscale: 'Viridis'}
}]);
---
name: 3D Random Walk Plot
suite: 3d-line
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/\_3d-line-plot.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row)
{ return row[key]; });
}
var trace1 = {
x: unpack(rows, 'x1'),
y: unpack(rows, 'y1'),
z: unpack(rows, 'z1'),
mode: 'lines',
marker: {
color: '#1f77b4',
size: 12,
symbol: 'circle',
line: {
color: 'rgb(0,0,0)',
width: 0
}},
line: {
color: '#1f77b4',
width: 1
},
type: 'scatter3d'
};
var trace2 = {
x: unpack(rows, 'x2'),
y: unpack(rows, 'y2'),
z: unpack(rows, 'z2'),
mode: 'lines',
marker: {
color: '#9467bd',
size: 12,
symbol: 'circle',
line: {
color: 'rgb(0,0,0)',
width: 0
}},
line: {
color: 'rgb(44, 160, 44)',
width: 1
},
type: 'scatter3d'
};
var trace3 = {
x: unpack(rows, 'x3'),
y: unpack(rows, 'y3'),
z: unpack(rows, 'z3'),
mode: 'lines',
marker: {
color: '#bcbd22',
size: 12,
symbol: 'circle',
line: {
color: 'rgb(0,0,0)',
width: 0
}},
line: {
color: '#bcbd22',
width: 1
},
type: 'scatter3d'
};
var data = [trace1, trace2, trace3];
var layout = {
title: {
text: '3D Line Plot'
},
autosize: false,
width: 500,
height: 500,
margin: {
l: 0,
r: 0,
b: 0,
t: 65
}
};
Plotly.newPlot('myDiv', data, layout);
});
---
description: How to make 3D line plots in javascript.
display\_as: 3d\_charts
name: 3D Line Plots
page\_type: example\_index
permalink: javascript/3d-line-plots/
redirect\_from: javascript-graphing-library/3d-line-plots/
thumbnail: thumbnail/3d-line.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","3d-line" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Isosurface Plot
suite: isosurface
---
var data = [
{
type: "isosurface",
x: [0,0,0,0,1,1,1,1],
y: [0,1,0,1,0,1,0,1],
z: [1,1,0,0,1,1,0,0],
value: [1,2,3,4,5,6,7,8],
isomin: 2,
isomax: 6,
colorscale: "Reds"
}
];
var layout = {
margin: {t:0, l:0, b:0},
scene: {
camera: {
eye: {
x: 1.88,
y: -2.12,
z: 0.96
}
}
}
};
Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});
---
name: Multiple Isosurfaces with Caps
suite: isosurface
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/clebsch-cubic.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {return parseFloat(row[key]); });
}
var data = [
{
type: "isosurface",
x: unpack(rows, 'x'),
y: unpack(rows, 'y'),
z: unpack(rows, 'z'),
value: unpack(rows, 'value'),
isomin: -10,
isomax: 10,
surface: {show: true, count: 4, fill: 1, pattern: 'odd'},
caps: {
x: {show: true},
y: {show: true},
z: {show: true}
},
}
];
var layout = {
margin: {t:0, l:0, b:0},
scene: {
camera: {
eye: {
x: 1.86,
y: 0.61,
z: 0.98
}
}
}
};
Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});
});
---
description: How to make 3D isosurface plots in javascript.
display\_as: 3d\_charts
name: 3D Isosurface Plots
order: 10
permalink: javascript/3d-isosurface-plots/
thumbnail: thumbnail/isosurface.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","isosurface" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Isosurface with Additional Slices
suite: isosurface
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/clebsch-cubic.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {return parseFloat(row[key]); });
}
var data = [
{
type: "isosurface",
x: unpack(rows, 'x'),
y: unpack(rows, 'y'),
z: unpack(rows, 'z'),
value: unpack(rows, 'value'),
isomin: -100,
isomax: 100,
surface: {show: true, count: 1, fill: 0.8},
slices: {z: {
show: true, locations: [-0.3, 0.5]
}},
caps: {
x: {show: false},
y: {show: false},
z: {show: false}
},
}
];
var layout = {
margin: {t:0, l:0, b:0},
scene: {
camera: {
eye: {
x: 1.86,
y: 0.61,
z: 0.98
}
}
}
};
Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});
});
---
name: Starting Position and Segments
suite: streamtube
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-wind.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return +row[key]; });
}
var data = [{
type: 'streamtube',
x: unpack(rows, 'x'),
y: unpack(rows, 'y'),
z: unpack(rows, 'z'),
u: unpack(rows, 'u'),
v: unpack(rows, 'v'),
w: unpack(rows, 'w'),
starts: {
x: Array(16).fill(80),
y: [20,30,40,50,20,30,40,50,20,30,40,50,20,30,40,50],
z: [0,0,0,0,5,5,5,5,10,10,10,10,15,15,15,15]
},
sizeref: 0.3,
colorscale: "Portland",
showscale: false,
maxdisplayed: 3000
}]
var layout = {
scene: {
aspectratio: {
x: 2,
y: 1,
z: 0.3
}
},
margin: {
t: 20,
b: 20,
l: 20,
r: 20
},
width: 600,
height: 400
}
Plotly.newPlot('myDiv', data, layout);
});
---
name: Introduction
suite: streamtube
markdown\_content: |
In streamtube plots, attributes inlcude `x`, `y`, and `z`, which set the coorindates of the vector field, and `u`, `v`, and `w`, which sets the x, y, and z components of the vector field. Additionally, you can use `starts` to determine the streamtube's starting position. Lastly, `maxdisplayed` determines the maximum segments displayed in a streamtube.
---
---
name: Basic Streamtube Plot
suite: streamtube
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/streamtube-basic.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [{
type: "streamtube",
x: unpack(rows, 'x'),
y: unpack(rows, 'y'),
z: unpack(rows, 'z'),
u: unpack(rows, 'u'),
v: unpack(rows, 'v'),
w: unpack(rows, 'w'),
sizeref: 0.5,
cmin: 0,
cmax: 3
}]
var layout = {
scene: {
camera: {
eye: {
x: -0.7243612458865182,
y: 1.9269804254717962,
z: 0.6704828299861716
}
}
}
}
Plotly.newPlot('myDiv', data, layout)
});
---
description: How to make 3D streamtube plots in javascript.
display\_as: 3d\_charts
name: 3D Streamtube Plots
permalink: javascript/streamtube-plot/
thumbnail: thumbnail/streamtube.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","streamtube" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
# Contribute to Plotly's [JavaScript Documentation](https://plotly.com/javascript/)

Plotly welcomes contributions to its [open-source JavaScript graphing libraries documentation](https://plotly.com/javascript) from its community of users.

Our JavaScript tutorials are written in HTML files in the `_posts/plotly_js` directory of this repository.

## Contribute Quickly to Plotly's JavaScript Graphing Library Documentation

To quickly make a contribution to Plotly's JavaScript graphing libraries documentation, simply submit a pull request with the change you would like to suggest. This can be done using the GitHub graphical user interface at https://github.com/plotly/graphing-library-docs.

The easiest way to do this is to follow the `Edit this page on GitHub` link at the top right of the page you are interested in contributing to:

![Screen Shot 2020-01-07 at 12 45 39 PM](https://user-images.githubusercontent.com/1557650/71916356-bfe53800-314b-11ea-92b6-eb763037f6d5.png)

**You don't have to worry about breaking the site when you submit a pull request!** This is because your change will not be merged to production immediately. A Plotly team member will first perform a code review on your pull request in order to ensure that it definitely increases the health of Plotly's graphing libraries codebase.

## Develop Locally

For contributions such as new example posts, we recommend setting up a local development environment so that you can test your changes as you work on them.

**See the `How To Get The Application Working Locally` section of the [Contributing Guide](https://github.com/plotly/graphing-library-docs/blob/master/Contributing.md)  to learn how to clone this repository to your local development environment and install its dependencies.**

Then follow these instructions to create or modify a new post. If the post is the first of its chart type, you need to create an index page for it first.

## Create An Index Page For A New Chart Type:

If you are documenting a new chart type, then you need to create an index page for it before creating the actual example page.

1. In `documentation/_posts/plotly_js`, create a folder titled with the chart type or topic you're adding to the documentation (i.e. `bar`).

2. `cd` into the folder you created and create an HTML index file for the chart type named: `yyyy-mm-dd-chart_type_plotly_js_index.html`. Copy the index file template below. Make sure to replace placeholder text!
```
---
name: Add-Chart-Type-or-Topic
permalink: javascript/add-chart-type-or-topic/
description: How to make a D3.js-based add-chart-type-or-topic in javascript. Add an additional sentence summarizing chart-type or topic.
layout: langindex
thumbnail: thumbnail/mixed.jpg
language: plotly_js
page_type: example_index
display_as: **SEE BELOW
---
  {% assign examples = site.posts | where:"language","plotly_js" | where:"suite","add-chart-type-or-topic"| sort: "order" %}
  {% include posts/auto_examples.html examples=examples %}
```
  - Make sure to update `_includes/posts/documentation_eg.html`, `_includes/layouts/side-bar.html`, and `_data/display_as_py_r_js.yml` and the CI python scripts with the new chart type!

  - Index pages for chart categories must have `order: 5`.

## Create A New Example Post:

1. In the folder containing the examples for the chart type you are writing documentation for, create a file named: `yyyy-mm-dd-example-title.html`.

2. Copy the example post template below and write JavaScript code to demonstrate the feature you are documenting.
  - If `plot_url` front-matter is not present, then the resulting chart will be displayed inline and a `Try It Codepen` button will be automatically generated.
  - If `plot_url` front-matter is present, then the URL given will be embedded in an `iframe` below the example.
```
---
description: How to make a D3.js-based bar chart in javascript. Seven examples of
grouped, stacked, overlaid, and colored bar charts.
display_as: basic
language: plotly_js
name: Bar Charts
page_type: example_index
permalink: javascript/bar-charts/
redirect_from: javascript-graphing-library/bar-charts/
thumbnail: thumbnail/bar.jpg **MORE INFO ON ADDING THUMBNAILS BELOW
markdown_content: |
  indented content in markdown format which will prefix an example ****SEE BELOW
---
var data = [
  {
    x: ['giraffes', 'orangutans', 'monkeys'],
    y: [20, 14, 23],
    type: 'bar'
  }The
];

Plotly.newPlot('myDiv', data);
```

- `display_as` sets where your tutorial is displayed. Make sure to update `_includes/posts/documentation_eg.html` with the new chart type!:
  - 'file_settings' = https://plotly.com/javascript/plotly-fundamentals
  - 'basic' = https://plotly.com/javascript/basic-charts
  - 'statistical' = https://plotly.com/javascript/statistical-charts
  - 'scientific' = https://plotly.com/javascript/scientific-charts
  - 'financial' = https://plotly.com/javascript/financial-charts
  - 'maps' = https://plotly.com/javascript/maps
  - '3d_charts' = https://plotly.com/javascript/3d-charts
  - See additional options [HERE](https://github.com/plotly/graphing-library-docs/blob/master/_includes/posts/documentation_eg.html#L1)

  - `order` defines the order in which the tutorials appear in each section on plot.ly/javascript.
    - <b>Note</b> The `order` of posts within a `display_as` must be a set of consecutive integers (i.e. [1, 2, 3, 4, 5, 6, ...]).
    - If a post has an `order` less than 5, it **MUST** also have the `page_type: example_index` front-matter so that it gets displayed on the index page.

 - `markdown_content` is rendered directly above the examples. In general, it is best to *avoid* paragraph-formatted explanation and let the simplicity of the example speak for itself, but that's not always possible. Take note that headings in this block *are* reflected in the sidebar.

  - Thumbnail images should named `your-tutorial-chart.jpg` and be *EXACTLY* 160px X 160px.
    - posts in the following `display_as` categories **MUST** have a thumbnail
      - 'file_settings' = https://plotly.com/javascript/plotly-fundamentals
      - 'basic' = https://plotly.com/javascript/basic-charts
      - 'statistical' = https://plotly.com/javascript/statistical-charts
      - 'scientific' = https://plotly.com/javascript/scientific-charts
      - 'financial' = https://plotly.com/javascript/financial-charts
      - 'maps' = https://plotly.com/javascript/maps
      - '3d_charts' = https://plotly.com/javascript/3d-charts
    - Thumbnail images should be clear and interesting. You do not need to capture the ENTIRE chart, but rather focus on the most interesting part of the chart.
    - Use images.plot.ly for adding new images. The password is in the Plotly 1Password Engineering Vault.
      - Log-in here: https://661924842005.signin.aws.amazon.com/console
      - From the <b>Amazon Web Services Console</b> select <b>S3 (Scalable Storage in the Cloud)</b> then select <b>plotly-tutorials</b> -> <b>plotly-documentation</b> -> <b>thumbnail</b>
      - Now from <b>All Buckets /plotly-tutorials/plotly-documentation/thumbnail</b> select the <b>Actions</b> dropdown and <b>upload</b> your .jpg file

## Modify An Existing Post:

1. Find the post you want to modify in `_posts/plotly_js`. Then, open the HTML file that contains that post and modify either the front-matter or the JavaScript.

# Best Practices:
  - `order` examples from basic to advanced
  - avoid the use of global JavaScript variables for `data` and `layout`.
  - make the chart display in a DOM element named `myDiv`
  - use the `.newPlot()` function
  - use "real" data to make the examples realistic and useful for users.
    - avoid using random or dummy data as much as humanly possible! Should only be a last resort.
  - upload data files to https://github.com/plotly/datasets as importing data rather than pasting a large chunk of data in the tutorial creates a cleaner example.
   - use `var config = {mapboxAccessToken: "your access token"};` if your chart requires Mapbox authentication. `"your access token` will replaced by Plotly's private token at build time. In development mode, you will need to create a `_data/mapboxtoken.yml` file and paste Plotly's non-URL restricted Mapbox key into it. This is available in 1Password.

## Make a Pull Request
  - Ready for your changes to be reviewed? Make a pull request!

    - Create a feature branch and use `git status` to list changed files.
    ```
    git checkout -b your_feature_branch
    git status
    ```
    - Add, commit, and push the files that you'd like to add to your PR:
    ```
    git add file-a
    git add file-b
    git commit -m 'message about your changes'
    git push origin your_feature_branch
    ```
    - Visit the [documentation repo](https://github.com/plotly/graphing-library-docs) and open a pull request!. You can then tag **@jdamiba** for a review.

## Style Edits

Please refer to our [Styles README](https://github.com/plotly/graphing-library-docs/blob/master/style_README.md)

Thanks for contributing to our documentation!!

---
permalink: https://dash.plotly.com/?/
description: Analytical Apps with Dash
name: Analytical Apps with Dash
thumbnail: thumbnail/dash_apps.png
page_type: example_index
language: plotly_js
display_as: file_settings
---

---
name: Is Plotly.js Free?
permalink: javascript/is-plotly-free/
redirect_from: javascript/open-source-announcement/
description: Plotly's open-source graphing libraries are free to use, work offline and don't require any account registration. Plotly also has a commercial offering called Dash Enterprise.
no_in_language: true
language: plotly_js
---

#### Is Plotly.js Free?

 &nbsp;  &nbsp; **Yes.** &nbsp; Plotly.js is free and open-source software, [licensed under the **MIT license**](https://github.com/plotly/plotly.js/blob/master/LICENSE). It costs nothing to [install and use](/javascript/getting-started). You can view the source, report issues or contribute using [our Github repository](https://github.com/plotly/plotly.js).


#### Can I use Plotly.js without signing up to any service?

&nbsp;  &nbsp; **Yes.** &nbsp; You can use Plotly.js to make, view, and distribute charts and maps without registering for any service,
obtaining any token, or creating any account. The one exception is that to view tile maps
which use tiles from the Mapbox service (which is optional, as [you can use other tile servers](/javascript/mapbox-layers)), you will need to have a Mapbox token.

#### Can I use Plotly.js offline, without being connected to the internet?

&nbsp;  &nbsp; **Yes.** &nbsp; You can use Plotly.js to make, view, and distribute  graphics totally offline. The one exception is that to view tile maps
which use tiles from a cloud-hosted service, such as Open Street Maps or Mapbox, you will need a connection to that service. You can view tile maps totally offline if  you run your own local tile server and [use its tiles](/javascript/mapbox-layers).

#### Is Dash free?

&nbsp;  &nbsp; **Yes.** &nbsp; Plotly's [Dash](https://plotly.com/dash) analytics application framework is also free and open-source software, licensed under the **MIT license**.

#### Does Plotly also make commercial software?

&nbsp;  &nbsp; **Yes.** &nbsp; Plotly has commercial offerings such as [Dash Enterprise](https://plotly.com/dash).

---
name: Adding Names to Line and Scatter Plot
suite: line-plots
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: 'markers',
name: 'Scatter'
};
var trace2 = {
x: [2, 3, 4, 5],
y: [16, 5, 11, 9],
mode: 'lines',
name: 'Lines'
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: 'lines+markers',
name: 'Scatter + Lines'
};
var data = [ trace1, trace2, trace3 ];
var layout = {
title: {text: 'Adding Names to Line and Scatter Plot'}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Connect Gaps Between Data
suite: line-plots
order: 12
---
var trace1 = {
x: [1, 2, 3, 4, 5, 6, 7, 8],
y: [10, 15, null, 17, 14, 12, 10, null, 15],
mode: 'lines+markers',
connectgaps: true
};
var trace2 = {
x: [1, 2, 3, 4, 5, 6, 7, 8],
y: [16, null, 13, 10, 8, null, 11, 12],
mode: 'lines',
connectgaps: true
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Connect the Gaps Between Data'
},
showlegend: false
};
Plotly.newPlot('myDiv', data, layout);
---
name: Styling Line Plot
suite: line-plots
---
trace1 = {
type: 'scatter',
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: 'lines',
name: 'Red',
line: {
color: 'rgb(219, 64, 82)',
width: 3
}
};
trace2 = {
type: 'scatter',
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: 'lines',
name: 'Blue',
line: {
color: 'rgb(55, 128, 191)',
width: 1
}
};
var layout = {
width: 500,
height: 500
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data, layout);
---
name: Line and Scatter Plot
suite: line-plots
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: 'markers'
};
var trace2 = {
x: [2, 3, 4, 5],
y: [16, 5, 11, 9],
mode: 'lines'
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: 'lines+markers'
};
var data = [ trace1, trace2, trace3 ];
var layout = {
title: {text: 'Line and Scatter Plot'}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Line Shape Options for Interpolation
suite: line-plots
---
var trace1 = {
x: [1, 2, 3, 4, 5],
y: [1, 3, 2, 3, 1],
mode: 'lines+markers',
name: 'linear',
line: {shape: 'linear'},
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3, 4, 5],
y: [6, 8, 7, 8, 6],
mode: 'lines+markers',
name: 'spline',
text: ['tweak line smoothness
with "smoothing" in line object', 'tweak line smoothness
with "smoothing" in line object', 'tweak line smoothness
with "smoothing" in line object', 'tweak line smoothness
with "smoothing" in line object', 'tweak line smoothness
with "smoothing" in line object', 'tweak line smoothness
with "smoothing" in line object'],
line: {shape: 'spline'},
type: 'scatter'
};
var trace3 = {
x: [1, 2, 3, 4, 5],
y: [11, 13, 12, 13, 11],
mode: 'lines+markers',
name: 'vhv',
line: {shape: 'vhv'},
type: 'scatter'
};
var trace4 = {
x: [1, 2, 3, 4, 5],
y: [16, 18, 17, 18, 16],
mode: 'lines+markers',
name: 'hvh',
line: {shape: 'hvh'},
type: 'scatter'
};
var trace5 = {
x: [1, 2, 3, 4, 5],
y: [21, 23, 22, 23, 21],
mode: 'lines+markers',
name: 'vh',
line: {shape: 'vh'},
type: 'scatter'
};
var trace6 = {
x: [1, 2, 3, 4, 5],
y: [26, 28, 27, 28, 26],
mode: 'lines+markers',
name: 'hv',
line: {shape: 'hv'},
type: 'scatter'
};
var data = [trace1, trace2, trace3, trace4, trace5, trace6];
var layout = {
legend: {
y: 0.5,
traceorder: 'reversed',
font: {size: 16},
yref: 'paper'
}};
Plotly.newPlot('myDiv', data, layout);
---
name: Graph and Axes Titles
suite: line-plots
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: 'markers',
name: 'Scatter'
};
var trace2 = {
x: [2, 3, 4, 5],
y: [16, 5, 11, 9],
mode: 'lines',
name: 'Lines'
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: 'lines+markers',
name: 'Scatter and Lines'
};
var data = [trace1, trace2, trace3];
var layout = {
title: {
text: 'Title of the Graph'
},
xaxis: {
title: {
text: 'x-axis title'
}
},
yaxis: {
title: {
text: 'y-axis title'
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make D3.js-based line charts in JavaScript.
display\_as: basic
name: Line Charts
page\_type: example\_index
permalink: javascript/line-charts/
redirect\_from: javascript-graphing-library/line-charts/
thumbnail: thumbnail/line-plots.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","line-plots" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Labelling Lines with Annotations
suite: line-plots
order: 13
---
var xData = [
[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013],
[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013]
];
var yData = [
[74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
[45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
[13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
[18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23]
];
var colors = ['rgba(67,67,67,1)', 'rgba(115,115,115,1)', 'rgba(49,130,189, 1)',
'rgba(189,189,189,1)'
];
var lineSize = [2, 2, 4, 2];
var labels = ['Television', 'Newspaper', 'Internet', 'Radio'];
var data = [];
for ( var i = 0 ; i < xData.length ; i++ ) {
var result = {
x: xData[i],
y: yData[i],
type: 'scatter',
mode: 'lines',
line: {
color: colors[i],
width: lineSize[i]
}
};
var result2 = {
x: [xData[i][0], xData[i][11]],
y: [yData[i][0], yData[i][11]],
type: 'scatter',
mode: 'markers',
marker: {
color: colors[i],
size: 12
}
};
data.push(result, result2);
}
var layout = {
showlegend: false,
height: 600,
width: 600,
xaxis: {
showline: true,
showgrid: false,
showticklabels: true,
linecolor: 'rgb(204,204,204)',
linewidth: 2,
tickmode: 'linear',
ticks: 'outside',
tickcolor: 'rgb(204,204,204)',
tickwidth: 2,
ticklen: 5,
tickfont: {
family: 'Arial',
size: 12,
color: 'rgb(82, 82, 82)'
}
},
yaxis: {
showgrid: false,
zeroline: false,
showline: false,
showticklabels: false
},
autosize: false,
margin: {
autoexpand: false,
l: 100,
r: 20,
t: 100
},
annotations: [
{
xref: 'paper',
yref: 'paper',
x: 0.0,
y: 1.05,
xanchor: 'left',
yanchor: 'bottom',
text: 'Main Source for News',
font:{
family: 'Arial',
size: 30,
color: 'rgb(37,37,37)'
},
showarrow: false
},
{
xref: 'paper',
yref: 'paper',
x: 0.5,
y: -0.1,
xanchor: 'center',
yanchor: 'top',
text: 'Source: Pew Research Center & Storytelling with data',
showarrow: false,
font: {
family: 'Arial',
size: 12,
color: 'rgb(150,150,150)'
}
}
]
};
for( var i = 0 ; i < xData.length ; i++ ) {
var result = {
xref: 'paper',
x: 0.05,
y: yData[i][0],
xanchor: 'right',
yanchor: 'middle',
text: labels[i] + ' ' + yData[i][0] +'%',
showarrow: false,
font: {
family: 'Arial',
size: 16,
color: 'black'
}
};
var result2 = {
xref: 'paper',
x: 0.95,
y: yData[i][11],
xanchor: 'left',
yanchor: 'middle',
text: yData[i][11] +'%',
font: {
family: 'Arial',
size: 16,
color: 'black'
},
showarrow: false
};
layout.annotations.push(result, result2);
}
Plotly.newPlot('myDiv', data, layout);
---
name: Colored and Styled Scatter Plot
suite: line-plots
---
var trace1 = {
x: [52698, 43117],
y: [53, 31],
mode: 'markers',
name: 'North America',
text: ['United States', 'Canada'],
marker: {
color: 'rgb(164, 194, 244)',
size: 12,
line: {
color: 'white',
width: 0.5
}
},
type: 'scatter'
};
var trace2 = {
x: [39317, 37236, 35650, 30066, 29570, 27159, 23557, 21046, 18007],
y: [33, 20, 13, 19, 27, 19, 49, 44, 38],
mode: 'markers',
name: 'Europe',
text: ['Germany', 'Britain', 'France', 'Spain', 'Italy', 'Czech Rep.', 'Greece', 'Poland'],
marker: {
color: 'rgb(255, 217, 102)',
size: 12
},
type: 'scatter'
};
var trace3 = {
x: [42952, 37037, 33106, 17478, 9813, 5253, 4692, 3899],
y: [23, 42, 54, 89, 14, 99, 93, 70],
mode: 'markers',
name: 'Asia/Pacific',
text: ['Australia', 'Japan', 'South Korea', 'Malaysia', 'China', 'Indonesia', 'Philippines', 'India'],
marker: {
color: 'rgb(234, 153, 153)',
size: 12
},
type: 'scatter'
};
var trace4 = {
x: [19097, 18601, 15595, 13546, 12026, 7434, 5419],
y: [43, 47, 56, 80, 86, 93, 80],
mode: 'markers',
name: 'Latin America',
text: ['Chile', 'Argentina', 'Mexico', 'Venezuela', 'Venezuela', 'El Salvador', 'Bolivia'],
marker: {
color: 'rgb(142, 124, 195)',
size: 12
},
type: 'scatter'
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'Quarter 1 Growth'
},
xaxis: {
title: {
text: 'GDP per Capita'
},
showgrid: false,
zeroline: false
},
yaxis: {
title: {
text: 'Percent'
},
showline: false
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Line Dash
suite: line-plots
order: 10
---
var trace1 = {
x: [1, 2, 3, 4, 5],
y: [1, 3, 2, 3, 1],
mode: 'lines',
name: 'Solid',
line: {
dash: 'solid',
width: 4
}
};
var trace2 = {
x: [1, 2, 3, 4, 5],
y: [6, 8, 7, 8, 6],
mode: 'lines',
name: 'dashdot',
line: {
dash: 'dashdot',
width: 4
}
};
var trace3 = {
x: [1, 2, 3, 4, 5],
y: [11, 13, 12, 13, 11],
mode: 'lines',
name: 'Solid',
line: {
dash: 'solid',
width: 4
}
};
var trace4 = {
x: [1, 2, 3, 4, 5],
y: [16, 18, 17, 18, 16],
mode: 'lines',
name: 'dot',
line: {
dash: 'dot',
width: 4
}
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'Line Dash'
},
xaxis: {
range: [0.75, 5.25],
autorange: false
},
yaxis: {
range: [0, 18.5],
autorange: false
},
legend: {
y: 0.5,
traceorder: 'reversed',
font: {
size: 16
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Line and Scatter Styling
suite: line-plots
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: 'markers',
marker: {
color: 'rgb(219, 64, 82)',
size: 12
}
};
var trace2 = {
x: [2, 3, 4, 5],
y: [16, 5, 11, 9],
mode: 'lines',
line: {
color: 'rgb(55, 128, 191)',
width: 3
}
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: 'lines+markers',
marker: {
color: 'rgb(128, 0, 128)',
size: 8
},
line: {
color: 'rgb(128, 0, 128)',
width: 1
}
};
var data = [trace1, trace2, trace3];
var layout = {
title: {
text: 'Line and Scatter Styling'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Basic Line Plot
suite: line-plots
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3, 4],
y: [16, 5, 11, 9],
type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
name: Colored and Styled Bar Chart
suite: bar
---
var trace1 = {
x: [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
y: [219, 146, 112, 127, 124, 180, 236, 207, 236, 263, 350, 430, 474, 526, 488, 537, 500, 439],
name: 'Rest of world',
marker: {color: 'rgb(55, 83, 109)'},
type: 'bar'
};
var trace2 = {
x: [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
y: [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270, 299, 340, 403, 549, 499],
name: 'China',
marker: {color: 'rgb(26, 118, 255)'},
type: 'bar'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'US Export of Plastic Scrap'
},
xaxis: {tickfont: {
size: 14,
color: 'rgb(107, 107, 107)'
}},
yaxis: {
title: {
text: 'USD (millions)',
font: {
size: 16,
color: 'rgb(107, 107, 107)'
}
},
tickfont: {
size: 14,
color: 'rgb(107, 107, 107)'
}
},
legend: {
x: 0,
y: 1.0,
bgcolor: 'rgba(255, 255, 255, 0)',
bordercolor: 'rgba(255, 255, 255, 0)'
},
barmode: 'group',
bargap: 0.15,
bargroupgap: 0.1
};
Plotly.newPlot('myDiv', data, layout);
---
name: Grouped Bar Chart with Direct Labels
suite: bar
order: 5.5
---
var xValue = ['Product A', 'Product B', 'Product C'];
var yValue = [20, 14, 23];
var yValue2 = [24, 16, 20];
var trace1 = {
x: xValue,
y: yValue,
type: 'bar',
text: yValue.map(String),
textposition: 'auto',
hoverinfo: 'none',
opacity: 0.5,
marker: {
color: 'rgb(158,202,225)',
line: {
color: 'rgb(8,48,107)',
width: 1.5
}
}
};
var trace2 = {
x: xValue,
y: yValue2,
type: 'bar',
text: yValue2.map(String),
textposition: 'auto',
hoverinfo: 'none',
marker: {
color: 'rgba(58,200,225,.5)',
line: {
color: 'rgb(8,48,107)',
width: 1.5
}
}
};
var data = [trace1,trace2];
var layout = {
title: {
text: 'January 2013 Sales Report'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Rounded Corners on Bars
suite: bar
markdown\_content: |
To create rounded corners on bars, set `barcornerradius` on the layout to a number of pixels, or a string with a percentage of the bar width, for example, 25%.
You can also configure traces individually with `marker.cornerradius` on the trace.
---
var trace1 = {
x: ['South Korea', 'China', 'Canada'],
y: [24, 10, 9],
name: 'Gold',
type: 'bar',
};
var trace2 = {
x: ['South Korea', 'China', 'Canada'],
y: [13, 15, 12],
name: 'Silver',
type: 'bar',
};
var trace3 = {
x: ['South Korea', 'China', 'Canada'],
y: [11, 8, 12],
name: 'Bronze',
type: 'bar',
};
var data = [trace1, trace2, trace3];
var layout = {
scattermode: 'group',
title: {
text: 'Grouped by Country'
},
xaxis: {
title: {
text: 'Country'
}
},
yaxis: {
title: {
text: 'Medals'
}
},
barcornerradius: 15,
};
Plotly.newPlot('myDiv', data, layout);
---
name: Customizing Individual Bar Widths
suite: bar
---
var trace0 = {
type: 'bar',
x: [1, 2, 3, 5.5, 10],
y: [10, 8, 6, 4, 2],
width: [0.8, 0.8, 0.8, 3.5, 4]
}
var data = [trace0]
Plotly.newPlot('myDiv', data);
---
name: Waterfall Bar Chart
suite: bar
order: 10
---
// Base
var xData = ['Product
Revenue', 'Services
Revenue',
'Total
Revenue', 'Fixed
Costs',
'Variable
Costs', 'Total
Costs', 'Total'
];
var yData = [400, 660, 660, 590, 400, 400, 340];
var textList = ['$430K', '$260K', '$690K', '$-120K', '$-200K', '$-320K', '$370K'];
//Base
var trace1 = {
x: xData,
y: [0, 430, 0, 570, 370, 370, 0],
marker: {
color: 'rgba(1,1,1,0.0)'
},
type: 'bar'
};
//Revenue
var trace2 = {
x: xData,
y: [430, 260, 690, 0, 0, 0, 0],
type: 'bar',
marker: {
color: 'rgba(55,128,191,0.7)',
line: {
color: 'rgba(55,128,191,1.0)',
width: 2
}
}
};
//Cost
var trace3 = {
x: xData,
y: [0, 0, 0, 120, 200, 320, 0],
type: 'bar',
marker: {
color: 'rgba(219, 64, 82, 0.7)',
line: {
color: 'rgba(219, 64, 82, 1.0)',
width: 2
}
}
};
//Profit
var trace4 = {
x: xData,
y: [0, 0, 0, 0, 0, 0, 370],
type: 'bar',
marker: {
color: 'rgba(50,171, 96, 0.7)',
line: {
color: 'rgba(50,171,96,1.0)',
width: 2
}
}
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'Annual Profit 2015'
},
barmode: 'stack',
paper\_bgcolor: 'rgba(245,246,249,1)',
plot\_bgcolor: 'rgba(245,246,249,1)',
width: 600,
height: 600,
showlegend: false,
annotations: []
};
for ( var i = 0 ; i < 7 ; i++ ) {
var result = {
x: xData[i],
y: yData[i],
text: textList[i],
font: {
family: 'Arial',
size: 14,
color: 'rgba(245,246,249,1)'
},
showarrow: false
};
layout.annotations.push(result);
};
Plotly.newPlot('myDiv', data, layout);
---
name: Bar Chart with Hover Text
suite: bar
---
var trace1 = {
x: ['Liam', 'Sophie', 'Jacob', 'Mia', 'William', 'Olivia'],
y: [8.0, 8.0, 12.0, 12.0, 13.0, 20.0],
type: 'bar',
text: ['4.17 below the mean', '4.17 below the mean', '0.17 below the mean', '0.17 below the mean', '0.83 above the mean', '7.83 above the mean'],
marker: {
color: 'rgb(142,124,195)'
}
};
var data = [trace1];
var layout = {
title: {
text: 'Number of Graphs Made this Week'
},
font:{
family: 'Raleway, sans-serif'
},
showlegend: false,
xaxis: {
tickangle: -45
},
yaxis: {
zeroline: false,
gridwidth: 2
},
bargap :0.05
};
Plotly.newPlot('myDiv', data, layout);
---
name: Bar Chart with Relative Barmode
suite: bar
order: 11
---
var trace1 = {
x: [1, 2, 3, 4],
y: [1, 4, 9, 16],
name: 'Trace1',
type: 'bar'
};
var trace2 = {
x: [1, 2, 3, 4],
y: [6, -8, -4.5, 8],
name: 'Trace2',
type: 'bar'
};
var trace3 = {
x: [1, 2, 3, 4],
y: [-15, -3, 4.5, -8],
name: 'Trace3',
type: 'bar'
}
var trace4 = {
x: [1, 2, 3, 4],
y: [-1, 3, -3, -4],
name: 'Trace4',
type: 'bar'
}
var data = [trace1, trace2, trace3, trace4];
var layout = {
xaxis: {
title: {
text: 'X axis'
}
},
yaxis: {
title: {
text: 'Y axis'
}
},
barmode: 'relative',
title: {
text: 'Relative Barmode'
}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based bar chart in javascript. Seven examples of
grouped, stacked, overlaid, and colored bar charts.
display\_as: basic
name: Bar Charts
page\_type: example\_index
permalink: javascript/bar-charts/
redirect\_from: javascript-graphing-library/bar-charts/
thumbnail: thumbnail/bar.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","bar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Customizing Individual Bar Base
suite: bar
order: 8.5
---
var data = [
{
type: 'bar',
x: ['2016','2017','2018'],
y: [500,600,700],
base: [-500,-600,-700],
hovertemplate: '%{base}',
marker: {
color: 'red'
},
name: 'expenses'
},
{
type: 'bar',
x: ['2016','2017','2018'],
y: [300,400,700],
base: 0,
marker: {
color: 'blue'
},
name: 'revenue'
}]
Plotly.newPlot('myDiv', data);
---
name: Customizing Individual Bar Colors
suite: bar
---
var trace1 = {
x: ['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E'],
y: [20, 14, 23, 25, 22],
marker:{
color: ['rgba(204,204,204,1)', 'rgba(222,45,38,0.8)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)', 'rgba(204,204,204,1)']
},
type: 'bar'
};
var data = [trace1];
var layout = {
title: {
text: 'Least Used Feature'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Bar Chart with Rotated Labels
suite: bar
---
var trace1 = {
x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
y: [20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
type: 'bar',
name: 'Primary Product',
marker: {
color: 'rgb(49,130,189)',
opacity: 0.7,
}
};
var trace2 = {
x: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
y: [19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
type: 'bar',
name: 'Secondary Product',
marker: {
color: 'rgb(204,204,204)',
opacity: 0.5
}
};
var data = [trace1, trace2];
var layout = {
title: {
text: '2013 Sales Report'
},
xaxis: {
tickangle: -45
},
barmode: 'group'
};
Plotly.newPlot('myDiv', data, layout);
---
name: Stacked Bar Chart
suite: bar
---
var trace1 = {
x: ['giraffes', 'orangutans', 'monkeys'],
y: [20, 14, 23],
name: 'SF Zoo',
type: 'bar'
};
var trace2 = {
x: ['giraffes', 'orangutans', 'monkeys'],
y: [12, 18, 29],
name: 'LA Zoo',
type: 'bar'
};
var data = [trace1, trace2];
var layout = {barmode: 'stack'};
Plotly.newPlot('myDiv', data, layout);
---
name: Basic Bar Chart
suite: bar
---
var data = [
{
x: ['giraffes', 'orangutans', 'monkeys'],
y: [20, 14, 23],
type: 'bar'
}
];
Plotly.newPlot('myDiv', data);
---
name: Grouped Bar Chart
suite: bar
---
var trace1 = {
x: ['giraffes', 'orangutans', 'monkeys'],
y: [20, 14, 23],
name: 'SF Zoo',
type: 'bar'
};
var trace2 = {
x: ['giraffes', 'orangutans', 'monkeys'],
y: [12, 18, 29],
name: 'LA Zoo',
type: 'bar'
};
var data = [trace1, trace2];
var layout = {barmode: 'group'};
Plotly.newPlot('myDiv', data, layout);
---
name: Bar Chart with Direct Labels
suite: bar
---
var xValue = ['Product A', 'Product B', 'Product C'];
var yValue = [20, 14, 23];
var trace1 = {
x: xValue,
y: yValue,
type: 'bar',
text: yValue.map(String),
textposition: 'auto',
hoverinfo: 'none',
marker: {
color: 'rgb(158,202,225)',
opacity: 0.6,
line: {
color: 'rgb(8,48,107)',
width: 1.5
}
}
};
var data = [trace1];
var layout = {
title: {
text: 'January 2013 Sales Report'
},
barmode: 'stack'
};
Plotly.newPlot('myDiv', data, layout);
---
name: WebGL with 1 Million points
suite: webgl-vs-svg
---
function gaussianRand() {
var rand = 0;
for (var i = 0; i < 6; i += 1) {
rand += Math.random();
}
return (rand / 6)-0.5;
}
var X = [],
Y = [],
n = 1000000,
i;
for (i = 0; i < n; i += 1) {
X.push(gaussianRand());
Y.push(gaussianRand());
}
var data = [{
type: "scattergl",
mode: "markers",
marker: {
color : 'rgb(152, 0, 0)',
line: {
width: 1,
color: 'rgb(0,0,0)'}
},
x: X,
y: Y
}]
Plotly.newPlot('myDiv', data)
---
name: WebGL with many traces
suite: webgl-vs-svg
---
function gaussianRand() {
var rand = 0;
for (var i = 0; i < 6; i += 1) {
rand += Math.random();
}
return (rand / 6)-0.5;
}
var start\_value = 0,
stop\_value = 1,
point\_num = 5000,
trace\_num = 10;
var curr\_value = start\_value;
var step = (stop\_value - start\_value) / (point\_num - 1);
var data = [];
for (var j = 0; j < trace\_num; j++) {
var X = [],
Y = [];
for (var i = 0; i < point\_num; i++) {
X.push(curr\_value + (step \* i));
Y.push((gaussianRand()\*8)+(j\*5));
}
data.push({
type: "scattergl",
mode: "line",
x: X,
y: Y
})
}
var layout = {showlegend: false}
Plotly.newPlot('myDiv', data = data, layout = layout)
---
description: Implement WebGL for increased speed, improved interactivity, and the
ability to plot even more data!
display\_as: basic
name: WebGL vs SVG
order: 14
permalink: javascript/webgl-vs-svg/
thumbnail: thumbnail/webgl.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","webgl-vs-svg"| sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}

### Multiple WebGL Contexts

Most browsers have a limit of between 8 and 16 WebGL contexts per page. A Plotly WebGL-based figure may use multiple WebGL contexts, but generally you'll be able to render between 4 and 8 figures on one page.
If you exceed the browser limit on WebGL contexts, some figures won't render and you'll see an error. In the console in Chrome, for example, you'll see the error: "Too many active WebGL contexts. Oldest context will be lost".
If you encounter WebGL context limits when using WebGL-based figures, you can use [Virtual WebGL](https://github.com/greggman/virtual-webgl), which virtualizes a single WebGL context into multiple contexts.
To use it, add the following script on your page:

```
<script src="https://unpkg.com/virtual-webgl@1.0.6/src/virtual-webgl.js"></script>
```
---
name: WebGL with 100,000 points
suite: webgl-vs-svg
---
function gaussianRand() {
var rand = 0;
for (var i = 0; i < 6; i += 1) {
rand += Math.random();
}
return (rand / 6)-0.5;
}
var X = [],
Y = [],
n = 100000,
i;
for (i = 0; i < n; i += 1) {
X.push(gaussianRand());
Y.push(gaussianRand());
}
var data = [{
type: "scattergl",
mode: "markers",
marker: {
line: {
width: 1,
color: '#404040'}
},
x: X,
y: Y
}]
Plotly.newPlot('myDiv', data)
---
description: How to make a D3.js-based filled area plot in javascript. An area chart
displays a solid color between the traces of a graph.
display\_as: basic
name: Filled Area Plots
permalink: javascript/filled-area-plots/
redirect\_from: javascript-graphing-library/filled-area-plots/
thumbnail: thumbnail/area1.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","area" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Normalized Stacked Area Chart
suite: area
order: 2.1
---
var plotDiv = document.getElementById('plot');
var traces = [
{x: [1,2,3], y: [2,1,4], stackgroup: 'one', groupnorm:'percent'},
{x: [1,2,3], y: [1,1,2], stackgroup: 'one'},
{x: [1,2,3], y: [3,0,2], stackgroup: 'one'}
];
Plotly.newPlot('myDiv', traces, {title: {text: 'Normalized stacked and filled line chart'}});
---
name: Filled-Area Animation
permalink: javascript/filled-area-animation/
description: How to make an animated filled-area plot with Plotly JS
thumbnail: thumbnail/apple\_stock\_animation.gif
page\_type: example\_index
display\_as: animations
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","filled-area-animations" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Select Hover Points
suite: area
---
var data = [
{
x: [0,0.5,1,1.5,2],
y: [0,1,2,1,0],
fill: 'toself',
fillcolor: '#ab63fa',
hoveron: 'points+fills',
line: {
color: '#ab63fa'
},
text: "Points + Fills",
hoverinfo: 'text'
},
{
x: [3,3.5,4,4.5,5],
y: [0,1,2,1,0],
fill: 'toself',
fillcolor: '#e763fa',
hoveron: 'points',
line: {
color: '#e763fa'
},
text: "Points only",
hoverinfo: 'text'
}]
var layout = {
title: {
text: 'Hover on *points* or *fill*'
},
xaxis: {
range: [0,5]
},
yaxis: {
range: [0,3]
}
}
Plotly.newPlot('myDiv', data, layout)
---
name: Stacked Area Chart
suite: area
---
var plotDiv = document.getElementById('plot');
var traces = [
{x: [1,2,3], y: [2,1,4], stackgroup: 'one'},
{x: [1,2,3], y: [1,1,2], stackgroup: 'one'},
{x: [1,2,3], y: [3,0,2], stackgroup: 'one'}
];
Plotly.newPlot('myDiv', traces, {title: {text: 'stacked and filled line chart'}});
---
name: Basic Overlaid Area Chart
suite: area
---
var trace1 = {
x: [1, 2, 3, 4],
y: [0, 2, 3, 5],
fill: 'tozeroy',
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3, 4],
y: [3, 5, 1, 7],
fill: 'tonexty',
type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
name: Overlaid Area Chart Without Boundary Lines
suite: area
---
var trace1 = {
x: [1, 2, 3, 4],
y: [0, 2, 3, 5],
fill: 'tozeroy',
type: 'scatter',
mode: 'none'
};
var trace2 = {
x: [1, 2, 3, 4],
y: [3, 5, 1, 7],
fill: 'tonexty',
type: 'scatter',
mode: 'none'
};
var layout = {
title: {
text: 'Overlaid Chart Without Boundary Lines'
}
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based sunburst chart in javascript. Visualize hierarchical
data spanning outward radially from root to leaves.
display\_as: basic
name: Sunburst Charts
permalink: javascript/sunburst-charts/
thumbnail: thumbnail/sunburst.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","sunburst" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
See [https://plotly/.com/javascript/reference/sunburst](https://plotly.com/javascript/reference/sunburst)/ for more information and chart attribute options!
---
name: Basic Sunburst Chart
suite: sunburst
---
var data = [{
type: "sunburst",
labels: ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
parents: ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
values: [10, 14, 12, 10, 2, 6, 6, 4, 4],
outsidetextfont: {size: 20, color: "#377eb8"},
leaf: {opacity: 0.4},
marker: {line: {width: 2}},
}];
var layout = {
margin: {l: 0, r: 0, b: 0, t: 0},
width: 500,
height: 500
};
Plotly.newPlot('myDiv', data, layout);
---
name: Sunburst with Repeated Labels
suite: sunburst
---
var data = [{
type: "sunburst",
ids: [
"North America", "Europe", "Australia", "North America - Football", "Soccer",
"North America - Rugby", "Europe - Football", "Rugby",
"Europe - American Football","Australia - Football", "Association",
"Australian Rules", "Autstralia - American Football", "Australia - Rugby",
"Rugby League", "Rugby Union"
],
labels: [
"North
America", "Europe", "Australia", "Football", "Soccer", "Rugby",
"Football", "Rugby", "American
Football", "Football", "Association",
"Australian
Rules", "American
Football", "Rugby", "Rugby
League",
"Rugby
Union"
],
parents: [
"", "", "", "North America", "North America", "North America", "Europe",
"Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
"Australia - Football", "Australia - Football", "Australia - Rugby",
"Australia - Rugby"
],
outsidetextfont: {size: 20, color: "#377eb8"},
// leaf: {opacity: 0.4},
marker: {line: {width: 2}},
}];
var layout = {
margin: {l: 0, r: 0, b: 0, t:0},
sunburstcolorway:["#636efa","#ef553b","#00cc96"],
};
Plotly.newPlot('myDiv', data, layout);
---
name: Large Number of Slices
suite: sunburst
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/coffee-flavors.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var data = [
{
type: "sunburst",
maxdepth: 3,
ids: unpack(rows, 'ids'),
labels: unpack(rows, 'labels'),
parents:unpack(rows, 'parents')
}
];
var layout = {
margin: {l: 0, r: 0, b: 0, t:0},
sunburstcolorway:[
"#636efa","#EF553B","#00cc96","#ab63fa","#19d3f3",
"#e763fa", "#FECB52","#FFA15A","#FF6692","#B6E880"
],
extendsunburstcolorway: true
};
Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true});
})
---
name: Control Text Orientation Inside Sunburst Chart Sectors
suite: sunburst
markdown\_content: |
The `insidetextorientation` attribute controls the orientation of the text inside chart sectors. When set to \*auto\*, text may be oriented in any direction in order to be as big as possible in the middle of a sector. The \*horizontal\* option orients text to be parallel with the bottom of the chart, and may make text smaller in order to achieve that goal. The \*radial\* option orients text along the radius of the sector. The \*tangential\* option orients text perpendicular to the radius of the sector.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/coffee-flavors.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) {return row[key]})
}
var data = [{
type: "sunburst",
maxdepth: 2,
ids: unpack(rows, 'ids'),
labels: unpack(rows, 'labels'),
parents: unpack(rows, 'parents'),
textposition: 'inside',
insidetextorientation: 'radial'
}]
var layout = {margin: {l: 0, r: 0, b: 0, t:0}}
Plotly.newPlot('myDiv', data, layout)
})
---
name: Branchvalues
suite: sunburst
order: 1.5
markdown\_content: |
With branchvalues "total", the value of the parent represents the width of its wedge. In the example below,
"Enoch" is 4 and "Awan" is 6 and so Enoch's width is 4/6ths of Awans. With branchvalues "remainder", the
parent's width is determined by its own value plus those of its children. So, Enoch's width is 4/10ths of
Awan's (4 / (6 + 4)).

Note that this means that the sum of the values of the children cannot exceed the
value of their parent when branchvalues "total". When branchvalues "relative" (the default), children will not take
up all of the space below their parent (unless the parent is the root and it has a value of 0).
---
var data = [
{
"type": "sunburst",
"labels": ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
"parents": ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
"values": [65, 14, 12, 10, 2, 6, 6, 4, 4],
"leaf": {"opacity": 0.4},
"marker": {"line": {"width": 2}},
"branchvalues": 'total'
}];
var layout = {
"margin": {"l": 0, "r": 0, "b": 0, "t": 0},
};
Plotly.newPlot('myDiv', data, layout, {showSendToCloud: true})
myPlot = document.getElementById("myDiv");
---
description: How to make D3.js-based line and scatter plots in JavaScript. Examples
of basic and colored line and scatter plots.
display\_as: basic
name: Scatter Plots
page\_type: example\_index
permalink: javascript/line-and-scatter/
redirect\_from: javascript-graphing-library/line-and-scatter/
thumbnail: thumbnail/line-and-scatter.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","line\_and\_scatter" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Grouped Scatter Plot with Custom Scatter Gap
suite: line\_and\_scatter
---
var trace1 = {
x: ['South Korea', 'China', 'Canada'],
y: [24, 10, 9],
name: 'Gold',
type: 'scatter',
mode: 'markers'
};
var trace2 = {
x: ['South Korea', 'China', 'Canada'],
y: [13, 15, 12],
name: 'Silver',
type: 'scatter',
mode: 'markers'
};
var trace3 = {
x: ['South Korea', 'China', 'Canada'],
y: [11, 8, 12],
name: 'Bronze',
type: 'scatter',
mode: 'markers'
};
var data = [trace1, trace2, trace3];
var layout = {
scattermode: 'group',
title: {
text: 'Grouped by Country'
},
xaxis: {
title: {
text: 'Country'
}
},
yaxis: {
title: {
text: 'Medals'
}
},
scattergap: 0.7
};
Plotly.newPlot('myDiv', data, layout);
---
name: Data Labels Hover
suite: line\_and\_scatter
---
var trace1 = {
x: [1, 2, 3, 4, 5],
y: [1, 6, 3, 6, 1],
mode: 'markers',
type: 'scatter',
name: 'Team A',
text: ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],
marker: { size: 12 }
};
var trace2 = {
x: [1.5, 2.5, 3.5, 4.5, 5.5],
y: [4, 1, 7, 1, 4],
mode: 'markers',
type: 'scatter',
name: 'Team B',
text: ['B-a', 'B-b', 'B-c', 'B-d', 'B-e'],
marker: { size: 12 }
};
var data = [ trace1, trace2 ];
var layout = {
xaxis: {
range: [ 0.75, 5.25 ]
},
yaxis: {
range: [0, 8]
},
title: {text: 'Data Labels Hover'}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Grouped Scatter Plot
suite: line\_and\_scatter
---
var trace1 = {
x: ['South Korea', 'China', 'Canada'],
y: [24, 10, 9],
name: 'Gold',
type: 'scatter',
mode: 'markers'
};
var trace2 = {
x: ['South Korea', 'China', 'Canada'],
y: [13, 15, 12],
name: 'Silver',
type: 'scatter',
mode: 'markers'
};
var trace3 = {
x: ['South Korea', 'China', 'Canada'],
y: [11, 8, 12],
name: 'Bronze',
type: 'scatter',
mode: 'markers'
};
var data = [trace1, trace2, trace3];
var layout = {
scattermode: 'group',
title: {
text: 'Grouped by Country'
},
xaxis: {
title: {
text: 'Country'
}
},
yaxis: {
title: {
text: 'Medals'
}
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Data Labels on The Plot
suite: line\_and\_scatter
---
var trace1 = {
x: [1, 2, 3, 4, 5],
y: [1, 6, 3, 6, 1],
mode: 'markers+text',
type: 'scatter',
name: 'Team A',
text: ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],
textposition: 'top center',
textfont: {
family: 'Raleway, sans-serif'
},
marker: { size: 12 }
};
var trace2 = {
x: [1.5, 2.5, 3.5, 4.5, 5.5],
y: [4, 1, 7, 1, 4],
mode: 'markers+text',
type: 'scatter',
name: 'Team B',
text: ['B-a', 'B-b', 'B-c', 'B-d', 'B-e'],
textfont : {
family:'Times New Roman'
},
textposition: 'bottom center',
marker: { size: 12 }
};
var data = [ trace1, trace2 ];
var layout = {
xaxis: {
range: [ 0.75, 5.25 ]
},
yaxis: {
range: [0, 8]
},
legend: {
y: 0.5,
yref: 'paper',
font: {
family: 'Arial, sans-serif',
size: 20,
color: 'grey',
}
},
title: {text: 'Data Labels on the Plot'}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Scatter Plot with a Color Dimension
suite: line\_and\_scatter
---
var trace1 = {
y: [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
mode: 'markers',
marker: {
size: 40,
color: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
}
};
var data = [trace1];
var layout = {
title: {
text: 'Scatter Plot with a Color Dimension'
}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Line and Scatter Plot
suite: line\_and\_scatter
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 15, 13, 17],
mode: 'markers',
type: 'scatter'
};
var trace2 = {
x: [2, 3, 4, 5],
y: [16, 5, 11, 9],
mode: 'lines',
type: 'scatter'
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 9, 15, 12],
mode: 'lines+markers',
type: 'scatter'
};
var data = [trace1, trace2, trace3];
Plotly.newPlot('myDiv', data);
---
name: Line Chart and a Bar Chart
suite: mixed
---
var trace1 = {
x: [0, 1, 2, 3, 4, 5],
y: [1.5, 1, 1.3, 0.7, 0.8, 0.9],
type: 'scatter'
};
var trace2 = {
x: [0, 1, 2, 3, 4, 5],
y: [1, 0.5, 0.7, -1.2, 0.3, 0.4],
type: 'bar'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
name: A Contour and Scatter Plot
of the Method of Steepest Descent
suite: mixed
---
var trace1 = {
z: [[1.5, 1.23469387755, 1.01020408163, 0.826530612245, 0.683673469388, 0.581632653061, 0.520408163265, 0.5, 0.520408163265, 0.581632653061, 0.683673469388, 0.826530612245, 1.01020408163, 1.23469387755, 1.5], [1.36734693878, 1.10204081633, 0.877551020408, 0.69387755102, 0.551020408163, 0.448979591837, 0.387755102041, 0.367346938776, 0.387755102041, 0.448979591837, 0.551020408163, 0.69387755102, 0.877551020408, 1.10204081633, 1.36734693878], [1.25510204082, 0.989795918367, 0.765306122449, 0.581632653061, 0.438775510204, 0.336734693878, 0.275510204082, 0.255102040816, 0.275510204082, 0.336734693878, 0.438775510204, 0.581632653061, 0.765306122449, 0.989795918367, 1.25510204082], [1.16326530612, 0.897959183673, 0.673469387755, 0.489795918367, 0.34693877551, 0.244897959184, 0.183673469388, 0.163265306122, 0.183673469388, 0.244897959184, 0.34693877551, 0.489795918367, 0.673469387755, 0.897959183673, 1.16326530612], [1.09183673469, 0.826530612245, 0.602040816327, 0.418367346939, 0.275510204082, 0.173469387755, 0.112244897959, 0.0918367346939, 0.112244897959, 0.173469387755, 0.275510204082, 0.418367346939, 0.602040816327, 0.826530612245, 1.09183673469], [1.04081632653, 0.775510204082, 0.551020408163, 0.367346938776, 0.224489795918, 0.122448979592, 0.0612244897959, 0.0408163265306, 0.0612244897959, 0.122448979592, 0.224489795918, 0.367346938776, 0.551020408163, 0.775510204082, 1.04081632653], [1.01020408163, 0.744897959184, 0.520408163265, 0.336734693878, 0.19387755102, 0.0918367346939, 0.030612244898, 0.0102040816327, 0.030612244898, 0.0918367346939, 0.19387755102, 0.336734693878, 0.520408163265, 0.744897959184, 1.01020408163], [1.0, 0.734693877551, 0.510204081633, 0.326530612245, 0.183673469388, 0.0816326530612, 0.0204081632653, 0.0, 0.0204081632653, 0.0816326530612, 0.183673469388, 0.326530612245, 0.510204081633, 0.734693877551, 1.0], [1.01020408163, 0.744897959184, 0.520408163265, 0.336734693878, 0.19387755102, 0.0918367346939, 0.030612244898, 0.0102040816327, 0.030612244898, 0.0918367346939, 0.19387755102, 0.336734693878, 0.520408163265, 0.744897959184, 1.01020408163], [1.04081632653, 0.775510204082, 0.551020408163, 0.367346938776, 0.224489795918, 0.122448979592, 0.0612244897959, 0.0408163265306, 0.0612244897959, 0.122448979592, 0.224489795918, 0.367346938776, 0.551020408163, 0.775510204082, 1.04081632653], [1.09183673469, 0.826530612245, 0.602040816327, 0.418367346939, 0.275510204082, 0.173469387755, 0.112244897959, 0.0918367346939, 0.112244897959, 0.173469387755, 0.275510204082, 0.418367346939, 0.602040816327, 0.826530612245, 1.09183673469], [1.16326530612, 0.897959183673, 0.673469387755, 0.489795918367, 0.34693877551, 0.244897959184, 0.183673469388, 0.163265306122, 0.183673469388, 0.244897959184, 0.34693877551, 0.489795918367, 0.673469387755, 0.897959183673, 1.16326530612], [1.25510204082, 0.989795918367, 0.765306122449, 0.581632653061, 0.438775510204, 0.336734693878, 0.275510204082, 0.255102040816, 0.275510204082, 0.336734693878, 0.438775510204, 0.581632653061, 0.765306122449, 0.989795918367, 1.25510204082], [1.36734693878, 1.10204081633, 0.877551020408, 0.69387755102, 0.551020408163, 0.448979591837, 0.387755102041, 0.367346938776, 0.387755102041, 0.448979591837, 0.551020408163, 0.69387755102, 0.877551020408, 1.10204081633, 1.36734693878], [1.5, 1.23469387755, 1.01020408163, 0.826530612245, 0.683673469388, 0.581632653061, 0.520408163265, 0.5, 0.520408163265, 0.581632653061, 0.683673469388, 0.826530612245, 1.01020408163, 1.23469387755, 1.5]],
x: [-1.0, -0.857142857143, -0.714285714286, -0.571428571429, -0.428571428571, -0.285714285714, -0.142857142857, 0.0, 0.142857142857, 0.285714285714, 0.428571428571, 0.571428571429, 0.714285714286, 0.857142857143, 1.0],
y: [-1.0, -0.857142857143, -0.714285714286, -0.571428571429, -0.428571428571, -0.285714285714, -0.142857142857, 0.0, 0.142857142857, 0.285714285714, 0.428571428571, 0.571428571429, 0.714285714286, 0.857142857143, 1.0],
ncontours: 30,
showscale: false,
type: 'contour'
};
var trace2 = {
x: [-0.8, -0.48, -0.288, -0.1728, -0.10368, -0.062208, -0.0373248, -0.02239488, -0.013436928, -0.0080621568, -0.00483729408, -0.002902376448, -0.0017414258688, -0.00104485552128, -0.000626913312768, -0.000376147987661],
y: [-0.9, -0.72, -0.576, -0.4608, -0.36864, -0.294912, -0.2359296, -0.18874368, -0.150994944, -0.1207959552, -0.09663676416, -0.077309411328, -0.0618475290624, -0.0494780232499, -0.0395824185999, -0.0316659348799],
mode: 'markers+lines',
name: 'steepest',
line: {color: 'black'},
type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('myDiv', data);
---
description: How to makes figures with D3.js-based mixed chart types in JavaScript.
Examples of a contour plot with a scatter plot and a bar chart with a line chart.
display\_as: basic
name: Multiple Chart Types
order: 13
permalink: javascript/graphing-multiple-chart-types/
redirect\_from: javascript-graphing-library/graphing-multiple-chart-types/
thumbnail: thumbnail/mixed2.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","mixed" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Donut Chart
suite: pie
---
var data = [{
values: [16, 15, 12, 6, 5, 4, 42],
labels: ['US', 'China', 'European Union', 'Russian Federation', 'Brazil', 'India', 'Rest of World' ],
domain: {column: 0},
name: 'GHG Emissions',
hoverinfo: 'label+percent+name',
hole: .4,
type: 'pie'
},{
values: [27, 11, 25, 8, 1, 3, 25],
labels: ['US', 'China', 'European Union', 'Russian Federation', 'Brazil', 'India', 'Rest of World' ],
text: 'CO2',
textposition: 'inside',
domain: {column: 1},
name: 'CO2 Emissions',
hoverinfo: 'label+percent+name',
hole: .4,
type: 'pie'
}];
var layout = {
title: {
text: 'Global Emissions 1990-2011'
},
annotations: [
{
font: {
size: 20
},
showarrow: false,
text: 'GHG',
x: 0.17,
y: 0.5
},
{
font: {
size: 20
},
showarrow: false,
text: 'CO2',
x: 0.82,
y: 0.5
}
],
height: 400,
width: 600,
showlegend: false,
grid: {rows: 1, columns: 2}
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to graph D3.js-based pie charts in javascript with D3.js. Examples
of pie charts, donut charts and pie chart subplots.
display\_as: basic
name: Pie Charts
page\_type: example\_index
permalink: javascript/pie-charts/
redirect\_from:
- javascript-graphing-library/pie-chart/
- javascript/pie-chart/
thumbnail: thumbnail/pie-chart.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","pie" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Pie Chart Subplots
suite: pie
markdown\_content: |
In order to create pie chart subplots, you need to use the [domain](https://plotly.com/javascript/reference/pie/#pie-domain) attribute. `domain` allows you to place each trace on a [grid](https://plotly.com/javascript/reference/layout/#layout-grid) of rows and columns defined in the layout or within a rectangle defined by `X` and `Y` arrays. The example below uses the `grid` method (with a 2 x 2 grid defined in the layout) for the first three traces and the X and Y method for the fourth trace.
---
var allLabels = ['1st', '2nd', '3rd', '4th', '5th'];
var allValues = [
[38, 27, 18, 10, 7],
[28, 26, 21, 15, 10],
[38, 19, 16, 14, 13],
[31, 24, 19, 18, 8]
];
var ultimateColors = [
['rgb(56, 75, 126)', 'rgb(18, 36, 37)', 'rgb(34, 53, 101)', 'rgb(36, 55, 57)', 'rgb(6, 4, 4)'],
['rgb(177, 127, 38)', 'rgb(205, 152, 36)', 'rgb(99, 79, 37)', 'rgb(129, 180, 179)', 'rgb(124, 103, 37)'],
['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)', 'rgb(175, 49, 35)', 'rgb(36, 73, 147)'],
['rgb(146, 123, 21)', 'rgb(177, 180, 34)', 'rgb(206, 206, 40)', 'rgb(175, 51, 21)', 'rgb(35, 36, 21)']
];
var data = [{
values: allValues[0],
labels: allLabels,
type: 'pie',
name: 'Starry Night',
marker: {
colors: ultimateColors[0]
},
domain: {
row: 0,
column: 0
},
hoverinfo: 'label+percent+name',
textinfo: 'none'
},{
values: allValues[1],
labels: allLabels,
type: 'pie',
name: 'Sunflowers',
marker: {
colors: ultimateColors[1]
},
domain: {
row: 1,
column: 0
},
hoverinfo: 'label+percent+name',
textinfo: 'none'
},{
values: allValues[2],
labels: allLabels,
type: 'pie',
name: 'Irises',
marker: {
colors: ultimateColors[2]
},
domain: {
row: 0,
column: 1
},
hoverinfo: 'label+percent+name',
textinfo: 'none'
},{
values: allValues[3],
labels: allLabels,
type: 'pie',
name: 'The Night Cafe',
marker: {
colors: ultimateColors[3]
},
domain: {
x: [0.52,1],
y: [0, 0.48]
},
hoverinfo: 'label+percent+name',
textinfo: 'none'
}];
var layout = {
height: 400,
width: 500,
grid: {rows: 2, columns: 2}
};
Plotly.newPlot('myDiv', data, layout);
---
name: Control Text Orientation Inside Pie Chart Sectors
suite: pie
markdown\_content: |
The `insidetextorientation` attribute controls the orientation of the text inside chart sectors. When set to \*auto\*, text may be oriented in any direction in order to be as big as possible in the middle of a sector. The \*horizontal\* option orients text to be parallel with the bottom of the chart, and may make text smaller in order to achieve that goal. The \*radial\* option orients text along the radius of the sector. The \*tangential\* option orients text perpendicular to the radius of the sector.
---
var data = [{
type: "pie",
values: [2, 3, 4, 4],
labels: ["Wages", "Operating expenses", "Cost of sales", "Insurance"],
textinfo: "label+percent",
insidetextorientation: "radial"
}]
var layout = [{
height: 700,
width: 700
}]
Plotly.newPlot('myDiv', data, layout)
---
name: Basic Pie Chart
suite: pie
---
var data = [{
values: [19, 26, 55],
labels: ['Residential', 'Non-Residential', 'Utility'],
type: 'pie'
}];
var layout = {
height: 400,
width: 500
};
Plotly.newPlot('myDiv', data, layout);
---
name: Automatically Adjust Margins
suite: pie
markdown\_content: |
The following example sets [automargin](https://plotly.com/javascript/setting-graph-size/#automatically-adjust-margins) attribute to true, which automatically increases the margin size.
---
var data = [{
type: "pie",
values: [2, 3, 4, 4],
labels: ["Wages", "Operating expenses", "Cost of sales", "Insurance"],
textinfo: "label+percent",
textposition: "outside",
automargin: true
}]
var layout = {
height: 400,
width: 400,
margin: {"t": 0, "b": 0, "l": 0, "r": 0},
showlegend: false
}
Plotly.newPlot('myDiv', data, layout)
---
name:
suite: treemap
markdown\_content: |
This example uses marker.colorscale to change the sector's color.
---
var values = ["11", "12", "13", "14", "15", "20", "30"]
var labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
var parents = ["", "A1", "A2", "A3", "A4", "", "B1"]
var data = [{
type: 'treemap',
values: values,
labels: labels,
parents: parents,
marker: {colorscale: 'Blues'}
}]
Plotly.newPlot('myDiv', data)
---
name:
suite: treemap
markdown\_content: |
This example uses `treemapcolorway` attribute, which should be set in layout.
---
var labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"];
var parents = ["", "A1", "A2", "A3", "A4", "", "B1"];
var data = [{
type: 'treemap',
labels: labels,
parents: parents
}]
var layout = {treemapcolorway: ["pink", "lightgray"]}
Plotly.newPlot('myDiv', data, layout)
---
name: Nested Layers in Treemap
suite: treemap
markdown\_content: |
The following example uses hierarchical data that includes layers and grouping. Treemap and [Sunburst](https://plotly.com/javascript/sunburst-charts/) charts reveal insights into the data, and the format of your hierarchical data. [maxdepth](https://plotly.com/javascript/reference/treemap/#treemap-maxdepth) attribute sets the number of rendered sectors from the given level.
---
d3.csv('https://raw.githubusercontent.com/plotly/datasets/master/coffee-flavors.csv', function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]});
}
var data = [{
type: "treemap",
ids: unpack(rows, 'ids'),
labels: unpack(rows, 'labels'),
parents: unpack(rows, 'parents')
}];
Plotly.newPlot('myDiv', data);
})
---
name: Basic Treemap
suite: treemap
markdown\_content: |
[Treemap charts](https://en.wikipedia.org/wiki/Treemapping) visualize hierarchical data using nested rectangles. Same as [Sunburst](https://plotly.com/javascript/sunburst-charts/) the hierarchy is defined by [labels](https://plotly.com/javascript/reference/treemap/#treemap-labels) and [parents](https://plotly.com/javascript/reference/treemap/#treemap-parents) attributes. Click on one sector to zoom in/out, which also displays a pathbar in the upper-left corner of your treemap. To zoom out you can use the path bar as well.
---
data = [{
type: "treemap",
labels: ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
parents: ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ]
}]
Plotly.newPlot('myDiv', data)
---
name: Set Color of Treemap Sectors
suite: treemap
markdown\_content: |
There are three different ways to change the color of the sectors in Treemap:
1) [marker.colors](https://plotly.com/javascript/reference/treemap/#treemap-marker-colors), 2) [colorway](https://plotly.com/javascript/reference/layout/#layout-colorway), 3) [colorscale](https://plotly.com/javascript/reference/treemap/#treemap-marker-colorscale). The following examples show how to use each of them.
---
var labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"];
var parents = ["", "A1", "A2", "A3", "A4", "", "B1"];
var data = [{
type: 'treemap',
labels: labels,
parents: parents,
marker: {colors: ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]}
}]
Plotly.newPlot('myDiv', data)
---
description: How to make a D3.js-based treemap chart in javascript to visualize hierarchical
data.
display\_as: basic
name: Treemaps
order: 11
permalink: javascript/treemaps/
thumbnail: thumbnail/treemap.png
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","treemap" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
See [https://plotly/.com/javascript/reference/treemap](https://plotly.com/javascript/reference/treemap)/ for more information and chart attribute options!
---
name: Set Different Attributes in Treemap
suite: treemap
markdown\_content: |
This example uses the following attributes:

1. [values](https://plotly.com/javascript/reference/treemap/#treemap-values): sets the values associated with each of the sectors.
2. [textinfo](https://plotly.com/javascript/reference/treemap/#treemap-textinfo): determines which trace information appear on the graph that can be 'text', 'value', 'current path', 'percent root', 'percent entry', and 'percent parent', or any combination of them.
3. [pathbar](https://plotly.com/javascript/reference/treemap/#treemap-pathbar): a main extra feature of treemap to display the current path of the visible portion of the hierarchical map. It may also be useful for zooming out of the graph.
4. [branchvalues](https://plotly.com/javascript/reference/treemap/#treemap-branchvalues): determines how the items in `values` are summed. When set to "total", items in `values` are taken to be value of all its descendants. In the example below Eva = 65, which is equal to 14 + 12 + 10 + 2 + 6 + 6 + 1 + 4.

When set to "remainder", items in `values` corresponding to the root and the branches sectors are taken to be the extra part not part of the sum of the values at their leaves.
---
var labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
var parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
var data = [{
type: "treemap",
labels: labels,
parents: parents,
values: [10, 14, 12, 10, 2, 6, 6, 1, 4],
textinfo: "label+value+percent parent+percent entry",
domain: {"x": [0, 0.48]},
outsidetextfont: {"size": 20, "color": "#377eb8"},
marker: {"line": {"width": 2}},
pathbar: {"visible": false}
},{
type: "treemap",
branchvalues: "total",
labels: labels,
parents: parents,
domain: {x: [0.52, 1]},
values: [65, 14, 12, 10, 2, 6, 6, 1, 4],
textinfo: "label+value+percent parent+percent entry",
outsidetextfont: {"size": 20, "color": "#377eb8"},
marker: {"line": {"width": 2}},
pathbar: {"visible": false}
}];
var layout = {
annotations: [{
showarrow: false,
text: "branchvalues: **remainder**",
x: 0.25,
xanchor: "center",
y: 1.1,
yanchor: "bottom"
}, {
showarrow: false,
text: "branchvalues: **total**",
x: 0.75,
xanchor: "center",
y: 1.1,
yanchor: "bottom"
}]}
Plotly.newPlot('myDiv', data, layout)
---
name: Bar Chart with Line Plot
suite: horizontal-bar
---
var xSavings = [1.3586, 2.2623000000000002, 4.9821999999999997, 6.5096999999999996,
7.4812000000000003, 7.5133000000000001, 15.2148, 17.520499999999998
];
var xNetworth = [93453.919999999998, 81666.570000000007, 69889.619999999995, 78381.529999999999, 141395.29999999999, 92969.020000000004, 66090.179999999993, 122379.3];
var ySavings = ['Japan', 'United Kingdom', 'Canada', 'Netherlands', 'United States', 'Belgium', 'Sweden', 'Switzerland'];
var yNetworth = ['Japan', 'United Kingdom', 'Canada', 'Netherlands', 'United States', 'Belgium', 'Sweden', 'Switzerland'];
var trace1 = {
x: xSavings,
y: ySavings,
xaxis: 'x1',
yaxis: 'y1',
type: 'bar',
marker: {
color: 'rgba(50,171,96,0.6)',
line: {
color: 'rgba(50,171,96,1.0)',
width: 1
}
},
name: 'Household savings, percentage of household disposable income',
orientation: 'h'
};
var trace2 = {
x: xNetworth,
y: yNetworth,
xaxis: 'x2',
yaxis: 'y1',
mode: 'lines+markers',
line: {
color: 'rgb(128,0,128)'
},
name: 'Household net worth, Million USD/capita'
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Household Savings & Net Worth for Eight OECD Countries'
},
xaxis1: {
range: [0, 20],
domain: [0, 0.5],
zeroline: false,
showline: false,
showticklabels: true,
showgrid: true
},
xaxis2: {
range: [25000, 150000],
domain: [0.5, 1],
zeroline: false,
showline: false,
showticklabels: true,
showgrid: true,
side: 'top',
dtick: 25000
},
legend: {
x: 0.029,
y: 1.238,
font: {
size: 10
}
},
margin: {
l: 100,
r: 20,
t: 200,
b: 70
},
width: 600,
height: 600,
paper\_bgcolor: 'rgb(248,248,255)',
plot\_bgcolor: 'rgb(248,248,255)',
annotations: [
{
xref: 'paper',
yref: 'paper',
x: -0.2,
y: -0.109,
text: 'OECD ' + '(2015), Household savings (indicator), ' + 'Household net worth (indicator). doi: ' + '10.1787/cfc6f499-en (Accessed on 05 June 2015)',
showarrow: false,
font:{
family: 'Arial',
size: 10,
color: 'rgb(150,150,150)'
}
}
]
};
for ( var i = 0 ; i < xSavings.length ; i++ ) {
var result = {
xref: 'x1',
yref: 'y1',
x: xSavings[i]+2.3,
y: ySavings[i],
text: xSavings[i] + '%',
font: {
family: 'Arial',
size: 12,
color: 'rgb(50, 171, 96)'
},
showarrow: false,
};
var result2 = {
xref: 'x2',
yref: 'y1',
x: xNetworth[i] - 20000,
y: yNetworth[i],
text: xNetworth[i] + ' M',
font: {
family: 'Arial',
size: 12,
color: 'rgb(128, 0, 128)'
},
showarrow: false
};
layout.annotations.push(result, result2);
}
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based hortizontal bar chart in JavaScript.
display\_as: basic
name: Horizontal Bar Charts
permalink: javascript/horizontal-bar-charts/
redirect\_from: javascript-graphing-library/horizontal-bar-charts/
thumbnail: thumbnail/horizontal-bar.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","horizontal-bar" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Basic Horizontal Bar Chart
suite: horizontal-bar
---
var data = [{
type: 'bar',
x: [20, 14, 23],
y: ['giraffes', 'orangutans', 'monkeys'],
orientation: 'h'
}];
Plotly.newPlot('myDiv', data);
---
name: Colored Bar Chart
suite: horizontal-bar
---
var trace1 = {
x: [20, 14, 23],
y: ['giraffes', 'orangutans', 'monkeys'],
name: 'SF Zoo',
orientation: 'h',
marker: {
color: 'rgba(55,128,191,0.6)',
width: 1
},
type: 'bar'
};
var trace2 = {
x: [12, 18, 29],
y: ['giraffes', 'orangutans', 'monkeys'],
name: 'LA Zoo',
orientation: 'h',
type: 'bar',
marker: {
color: 'rgba(255,153,51,0.6)',
width: 1
}
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Colored Bar Chart'
},
barmode: 'stack'
};
Plotly.newPlot('myDiv', data, layout);
---
name: Categorical Dot Plot
suite: dot
---
var country = ['Switzerland (2011)', 'Chile (2013)', 'Japan (2014)', 'United States (2012)', 'Slovenia (2014)', 'Canada (2011)', 'Poland (2010)', 'Estonia (2015)', 'Luxembourg (2013)', 'Portugal (2011)'];
var votingPop = [40, 45.7, 52, 53.6, 54.1, 54.2, 54.5, 54.7, 55.1, 56.6];
var regVoters = [49.1, 42, 52.7, 84.3, 51.7, 61.1, 55.3, 64.2, 91.1, 58.9];
var trace1 = {
type: 'scatter',
x: votingPop,
y: country,
mode: 'markers',
name: 'Percent of estimated voting age population',
marker: {
color: 'rgba(156, 165, 196, 0.95)',
line: {
color: 'rgba(156, 165, 196, 1.0)',
width: 1,
},
symbol: 'circle',
size: 16
}
};
var trace2 = {
x: regVoters,
y: country,
mode: 'markers',
name: 'Percent of estimated registered voters',
marker: {
color: 'rgba(204, 204, 204, 0.95)',
line: {
color: 'rgba(217, 217, 217, 1.0)',
width: 1,
},
symbol: 'circle',
size: 16
}
};
var data = [trace1, trace2];
var layout = {
title: {
text: 'Votes cast for ten lowest voting age population in OECD countries',
font: {
color: 'rgb(204, 204, 204)'
}
},
xaxis: {
showgrid: false,
showline: true,
linecolor: 'rgb(102, 102, 102)',
tickfont: {
font: {
color: 'rgb(102, 102, 102)'
}
},
tickmode: 'linear',
dtick: 10,
ticks: 'outside',
tickcolor: 'rgb(102, 102, 102)'
},
margin: {
l: 140,
r: 40,
b: 50,
t: 80
},
legend: {
font: {
size: 10,
},
yanchor: 'middle',
xanchor: 'right'
},
width: 600,
height: 600,
paper\_bgcolor: 'rgb(254, 247, 234)',
plot\_bgcolor: 'rgb(254, 247, 234)',
hovermode: 'closest'
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make D3.js-based dot plots in JavaScript. Example of a styled,
categorical dot plot.
display\_as: basic
name: Dot Plots
permalink: javascript/dot-plots/
thumbnail: thumbnail/dot-plot.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","dot" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
description: Plotly.js makes interactive, publication-quality graphs online. Examples
of how to make basic charts.
layout: langindex
name: Basic Charts
display\_as: basic
permalink: javascript/basic-charts/
thumbnail: thumbnail/mixed.jpg
---

# Plotly.js Basic Charts

{{page.description}}

{% include layouts/dashplug.html %}

{% assign languagelist = site.posts | where:"language","plotly\_js" | where:"display\_as","basic" | where: "layout","base" | sort: "order" %}
{% include posts/documentation\_eg.html %}
---
name: Marker Size on Bubble Charts
suite: bubble
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 11, 12, 13],
mode: 'markers',
marker: {
size: [40, 60, 80, 100]
}
};
var data = [trace1];
var layout = {
title: {
text: 'Marker Size'
},
showlegend: false,
height: 600,
width: 600
};
Plotly.newPlot('myDiv', data, layout);
---
name: Bubble Size Scaling on Charts
suite: bubble
---
// To scale the bubble size, use the attribute sizeref. We recommend using the following formula to calculate a sizeref value:
// sizeref = 2.0 \* Math.max(...size) / (desired\_maximum\_marker\_size\*\*2)
// Note that setting 'sizeref' to a value greater than 1, decreases the rendered marker sizes, while setting 'sizeref' to less than 1, increases the rendered marker sizes. See https://plotly.com/python/reference/scatter/#scatter-marker-sizeref for more information. Additionally, we recommend setting the sizemode attribute: https://plotly.com/python/reference/scatter/#scatter-marker-sizemode to area.
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 11, 12, 13],
text: ['A
size: 40', 'B
size: 60', 'C
size: 80', 'D
size: 100'],
mode: 'markers',
marker: {
size: [400, 600, 800, 1000],
sizemode: 'area'
}
};
var trace2 = {
x: [1, 2, 3, 4],
y: [14, 15, 16, 17],
text: ['Asize: 40sixeref: 0.2', 'Bsize: 60sixeref: 0.2', 'Csize: 80sixeref: 0.2', 'Dsize: 100sixeref: 0.2'],
mode: 'markers',
marker: {
size: [400, 600, 800, 1000],
//setting 'sizeref' to lower than 1 decreases the rendered size
sizeref: 2,
sizemode: 'area'
}
};
var trace3 = {
x: [1, 2, 3, 4],
y: [20, 21, 22, 23],
text: ['Asize: 40sixeref: 2', 'Bsize: 60sixeref: 2', 'Csize: 80sixeref: 2', 'Dsize: 100sixeref: 2'],
mode: 'markers',
marker: {
size: [400, 600, 800, 1000],
//setting 'sizeref' to less than 1, increases the rendered marker sizes
sizeref: 0.2,
sizemode: 'area'
}
};
// sizeref using above formula
var desired\_maximum\_marker\_size = 40;
var size = [400, 600, 800, 1000];
var trace4 = {
x: [1, 2, 3, 4],
y: [26, 27, 28, 29],
text: ['Asize: 40sixeref: 1.25', 'Bsize: 60sixeref: 1.25', 'Csize: 80sixeref: 1.25', 'Dsize: 100sixeref: 1.25'],
mode: 'markers',
marker: {
size: size,
//set 'sizeref' to an 'ideal' size given by the formula sizeref = 2. \* max(array\_of\_size\_values) / (desired\_maximum\_marker\_size \*\* 2)
sizeref: 2.0 \* Math.max(...size) / (desired\_maximum\_marker\_size\*\*2),
sizemode: 'area'
}
};
var data = [trace1, trace2, trace3, trace4];
var layout = {
title: {
text: 'Size Scaling in Bubble Charts'
},
showlegend: false,
height: 600,
width: 600
};
Plotly.newPlot('myDiv', data, layout);
---
description: How to make a D3.js-based bubble chart in javascript. Examples of scatter
charts whose markers have variable color, size, and symbols.
display\_as: basic
name: Bubble Charts
page\_type: example\_index
permalink: javascript/bubble-charts/
redirect\_from: javascript-graphing-library/bubble-charts/
thumbnail: thumbnail/bubble.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","bubble" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Marker Size, Color, and Symbol as an Array
suite: bubble
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 11, 12, 13],
mode: 'markers',
marker: {
color: ['hsl(0,100,40)', 'hsl(33,100,40)', 'hsl(66,100,40)', 'hsl(99,100,40)'],
size: [12, 22, 32, 42],
opacity: [0.6, 0.7, 0.8, 0.9]
},
type: 'scatter'
};
var trace2 = {
x: [1, 2, 3, 4],
y: [11, 12, 13, 14],
mode: 'markers',
marker: {
color: 'rgb(31, 119, 180)',
size: 18,
symbol: ['circle', 'square', 'diamond', 'cross']
},
type: 'scatter'
};
var trace3 = {
x: [1, 2, 3, 4],
y: [12, 13, 14, 15],
mode: 'markers',
marker: {
size: 18,
line: {
color: ['rgb(120,120,120)', 'rgb(120,120,120)', 'red', 'rgb(120,120,120)'],
width: [2, 2, 6, 2]
}
},
type: 'scatter'
};
var data = [trace1, trace2, trace3];
var layout = {showlegend: false};
Plotly.newPlot('myDiv', data, layout);
---
name: Marker Size and Color on Bubble Charts
suite: bubble
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 11, 12, 13],
mode: 'markers',
marker: {
color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
opacity: [1, 0.8, 0.6, 0.4],
size: [40, 60, 80, 100]
}
};
var data = [trace1];
var layout = {
title: {
text: 'Marker Size and Color'
},
showlegend: false,
height: 600,
width: 600
};
Plotly.newPlot('myDiv', data, layout);
---
name: Hover Text on Bubble Charts
suite: bubble
---
var trace1 = {
x: [1, 2, 3, 4],
y: [10, 11, 12, 13],
text: ['A
size: 40', 'B
size: 60', 'C
size: 80', 'D
size: 100'],
mode: 'markers',
marker: {
color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
size: [40, 60, 80, 100]
}
};
var data = [trace1];
var layout = {
title: {
text: 'Bubble Chart Hover Text'
},
showlegend: false,
height: 600,
width: 600
};
Plotly.newPlot('myDiv', data, layout);
---
name: Changing Size of Rows and Columns
suite: tables
---
var values = [
['Salaries', 'Office', 'Merchandise', 'Legal', '**TOTAL
EXPENSES**'],
["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
"Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
"Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
"Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
"Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]
var data = [{
type: 'table',
columnorder: [1,2],
columnwidth: [80,400],
header: {
values: [["**EXPENSES**
as of July 2017"], ["**DESCRIPTION**"]],
align: ["left", "center"],
height: 40,
line: {width: 1, color: '#506784'},
fill: {color: '#119DFF'},
font: {family: "Arial", size: 12, color: "white"}
},
cells: {
values: values,
align: ["left", "center"],
height: 30,
line: {color: "#506784", width: 1},
fill: {color: ['#25FEFD', 'white']},
font: {family: "Arial", size: 11, color: ["#506784"]}
}
}]
Plotly.newPlot('myDiv', data);
---
name: Table Subplots
suite: tables
markdown\_content: |
Please see [Table Subplots](https://plotly.com/javascript/table-subplots) documentation.
---
---
name: Styled Table
suite: tables
---
var values = [
['Salaries', 'Office', 'Merchandise', 'Legal', '**TOTAL**'],
[1200000, 20000, 80000, 2000, 12120000],
[1300000, 20000, 70000, 2000, 130902000],
[1300000, 20000, 120000, 2000, 131222000],
[1400000, 20000, 90000, 2000, 14102000]]
var data = [{
type: 'table',
header: {
values: [["**EXPENSES**"], ["**Q1**"],
["**Q2**"], ["**Q3**"], ["**Q4**"]],
align: ["left", "center"],
line: {width: 1, color: '#506784'},
fill: {color: '#119DFF'},
font: {family: "Arial", size: 12, color: "white"}
},
cells: {
values: values,
align: ["left", "center"],
line: {color: "#506784", width: 1},
fill: {color: ['#25FEFD', 'white']},
font: {family: "Arial", size: 11, color: ["#506784"]}
}
}]
Plotly.newPlot('myDiv', data);
---
description: How to make a D3.js-based tables in javascript.
display\_as: basic
name: Tables
order: 12
permalink: javascript/table/
thumbnail: thumbnail/table.gif
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","tables" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Alternating Row Colors
suite: tables
---
var values = [
['Salaries', 'Office', 'Merchandise', 'Legal', '**TOTAL**'],
[1200000, 20000, 80000, 2000, 12120000],
[1300000, 20000, 70000, 2000, 130902000],
[1300000, 20000, 120000, 2000, 131222000],
[1400000, 20000, 90000, 2000, 14102000]]
var headerColor = "grey";
var rowEvenColor = "lightgrey";
var rowOddColor = "white";
var data = [{
type: 'table',
header: {
values: [["**EXPENSES**"], ["**Q1**"],
["**Q2**"], ["**Q3**"], ["**Q4**"]],
align: "center",
line: {width: 1, color: 'black'},
fill: {color: headerColor},
font: {family: "Arial", size: 12, color: "white"}
},
cells: {
values: values,
align: "center",
line: {color: "black", width: 1},
fill: {color: [[rowOddColor,rowEvenColor,rowOddColor,
rowEvenColor,rowOddColor]]},
font: {family: "Arial", size: 11, color: ["black"]}
}
}]
Plotly.newPlot('myDiv', data);
---
name: Table From a CSV
suite: tables
---
d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/Mining-BTC-180.csv", function(err, rows){
function unpack(rows, key) {
return rows.map(function(row) { return row[key]; });
}
var headerNames = d3.keys(rows[0]);
var headerValues = [];
var cellValues = [];
for (i = 0; i < headerNames.length; i++) {
headerValue = [headerNames[i]];
headerValues[i] = headerValue;
cellValue = unpack(rows, headerNames[i]);
cellValues[i] = cellValue;
}
// clean date
for (i = 0; i < cellValues[1].length; i++) {
var dateValue = cellValues[1][i].split(' ')[0]
cellValues[1][i] = dateValue
}
var data = [{
type: 'table',
columnwidth: [150,600,1000,900,600,500,1000,1000,1000],
columnorder: [0,1,2,3,4,5,6,7,8,9],
header: {
values: headerValues,
align: "center",
line: {width: 1, color: 'rgb(50, 50, 50)'},
fill: {color: ['rgb(235, 100, 230)']},
font: {family: "Arial", size: 8, color: "white"}
},
cells: {
values: cellValues,
align: ["center", "center"],
line: {color: "black", width: 1},
fill: {color: ['rgba(228, 222, 249, 0.65)','rgb(235, 193, 238)', 'rgba(228, 222, 249, 0.65)']},
font: {family: "Arial", size: 9, color: ["black"]}
}
}]
var layout = {
title: {
text: "Bitcoin mining stats for 180 days"
}
}
Plotly.newPlot('myDiv', data, layout);
});
---
name: Basic Table
suite: tables
---
var values = [
['Salaries', 'Office', 'Merchandise', 'Legal', '**TOTAL**'],
[1200000, 20000, 80000, 2000, 12120000],
[1300000, 20000, 70000, 2000, 130902000],
[1300000, 20000, 120000, 2000, 131222000],
[1400000, 20000, 90000, 2000, 14102000]]
var data = [{
type: 'table',
header: {
values: [["**EXPENSES**"], ["**Q1**"],
["**Q2**"], ["**Q3**"], ["**Q4**"]],
align: "center",
line: {width: 1, color: 'black'},
fill: {color: "grey"},
font: {family: "Arial", size: 12, color: "white"}
},
cells: {
values: values,
align: "center",
line: {color: "black", width: 1},
font: {family: "Arial", size: 11, color: ["black"]}
}
}]
Plotly.newPlot('myDiv', data);
---
description: How to make D3.js-based sankey diagrams in Plotly.js.
display\_as: basic
name: Sankey Diagrams
order: 10
permalink: javascript/sankey-diagram/
thumbnail: thumbnail/sankey.jpg
---
{% assign examples = site.posts | where:"language","plotly\_js" | where:"suite","sankey" | sort: "order" %}
{% include posts/auto\_examples.html examples=examples %}
---
name: Style Sankey Diagram
suite: sankey
description:
---
d3.json('https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey\_energy\_dark.json', function(fig){
var data = {
type: "sankey",
domain: {
x: [0,1],
y: [0,1]
},
orientation: "h",
valueformat: ".0f",
valuesuffix: "TWh",
node: {
pad: 15,
thickness: 15,
line: {
color: "black",
width: 0.5
},
label: fig.data[0].node.label,
color: fig.data[0].node.color
},
link: {
source: fig.data[0].link.source,
target: fig.data[0].link.target,
value: fig.data[0].link.value,
label: fig.data[0].link.label
}
}
var data = [data]
var layout = {
title: {
text: "Energy forecast for 2050
Source: Department of Energy & Climate Change, Tom Counsell via [Mike Bostock](https://bost.ocks.org/mike/sankey/)"
},
width: 1118,
height: 772,
font: {
size: 10,
color: 'white'
},
plot\_bgcolor: 'black',
paper\_bgcolor: 'black'
}
Plotly.newPlot('myDiv', data, layout)
});
---
name: Add Links
suite: sankey
description:
---
d3.json('https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey\_energy.json', function(fig){
var data = {
type: "sankey",
domain: {
x: [0,1],
y: [0,1]
},
orientation: "h",
valueformat: ".0f",
valuesuffix: "TWh",
node: {
pad: 15,
thickness: 15,
line: {
color: "black",
width: 0.5
},
label: fig.data[0].node.label,
color: fig.data[0].node.color
},
link: {
source: fig.data[0].link.source,
target: fig.data[0].link.target,
value: fig.data[0].link.value,
label: fig.data[0].link.label
}
}
var data = [data]
var layout = {
title: {
text: "Energy forecast for 2050
Source: Department of Energy & Climate Change, Tom Counsell via [Mike Bostock](https://bost.ocks.org/mike/sankey/)"
},
width: 1118,
height: 772,
font: {
size: 10
}
}
Plotly.newPlot('myDiv', data, layout)
});
---
name: Define Node Position
suite: sankey
description:
markdown\_content: |
The following example sets [node.x](https://plotly.com/javascript/reference/sankey/#sankey-node-x) and `node.y` to place nodes in the specified locations, except in the `snap arrangement` (default behaviour when `node.x` and `node.y` are not defined) to avoid overlapping of the nodes, therefore, an automatic snapping of elements will be set to define the padding between nodes via [nodepad](https://plotly.com/javascript/reference/sankey/#sankey-node-pad). The other possible arrangements are: 1) perpendicular 2) freeform 3) fixed
---
var data = [{
type: "sankey",
arrangement: "snap",
node:{
label: ["A", "B", "C", "D", "E", "F"],
x: [0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
y: [0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
pad:10}, // 10 Pixels
link: {
source: [0, 0, 1, 2, 5, 4, 3, 5],
target: [5, 3, 4, 3, 0, 2, 2, 3],
value: [1, 2, 1, 1, 1, 1, 1, 2]}
}]
var layout = {
title: {
text: "Sankey with manually positioned node"
}
}
Plotly.newPlot('myDiv', data, layout)
---
name: Add Nodes
suite: sankey
description:
---
d3.json('https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey\_energy.json', function(fig){
var data = {
type: "sankey",
domain: {
x: [0,1],
y: [0,1]
},
orientation: "h",
valueformat: ".0f",
valuesuffix: "TWh",
node: {
pad: 15,
thickness: 15,
line: {
color: "black",
width: 0.5
},
label: fig.data[0].node.label,
color: fig.data[0].node.color
}
}
var data = [data]
var layout = {
title: {
text: "Energy forecast for 2050
Source: Department of Energy & Climate Change, Tom Counsell via [Mike Bostock](https://bost.ocks.org/mike/sankey/)"
},
width: 1118,
height: 772,
font: {
size: 10
}
}
Plotly.newPlot('myDiv', data, layout)
});
---
name: Basic Sankey Diagram
suite: sankey
description:
---
var data = {
type: "sankey",
orientation: "h",
node: {
pad: 15,
thickness: 30,
line: {
color: "black",
width: 0.5
},
label: ["A1", "A2", "B1", "B2", "C1", "C2"],
color: ["blue", "blue", "blue", "blue", "blue", "blue"]
},
link: {
source: [0,1,0,2,3,3],
target: [2,3,3,4,4,5],
value: [8,4,2,8,4,2]
}
}
var data = [data]
var layout = {
title: {
text: "Basic Sankey"
},
font: {
size: 10
}
}
Plotly.react('myDiv', data, layout)
---
name: Node Alignment
suite: sankey
markdown\_content : |
You can set the alignment of nodes using `node.align`. In this example, we align nodes to the "right". `node.align` can also be set to "left", "center", or "justify". The default is "justify" if ``node.align` is not set, and is similar to aligning to the "left", except that nodes without outgoing links are moved to the right of the figure.
---
var data = {
type: "sankey",
orientation: "h",
node: {
label: ["0", "1", "2", "3", "4", "5"],
align: "right",
},
link: {
source: [0, 1, 4, 2, 1],
target: [1, 4, 5, 4, 3],
value: [4, 2, 3, 1, 2],
},
};
var data = [data];
var layout = {
title: {
text: "Align Nodes (Right)"
},
font: {
size: 10,
},
};
Plotly.newPlot('myDiv', data, layout);
---
name: Create Sankey Canvas
suite: sankey
description:
---
var data = {
type: "sankey",
domain: {
x: [0,1],
y: [0,1]
},
orientation: "h",
valueformat: ".0f",
valuesuffix: "TWh"
}
var data = [data]
var layout = {
title: {
text: "Energy forecast for 2050
Source: Department of Energy & Climate Change, Tom Counsell via [Mike Bostock](https://bost.ocks.org/mike/sankey/)"
},
width: 1118,
height: 772,
font: {
size: 10
}
}
---
permalink: /javascript/reference/scatter/
layout: langindex
page\_type: reference
name: scatter Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scatter` Traces

{% include posts/reference-trace.html trace\_name="scatter" trace\_data=site.data.plotschema.traces.scatter %}
---
permalink: /javascript/reference/contour/
layout: langindex
page\_type: reference
name: contour Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `contour` Traces

{% include posts/reference-trace.html trace\_name="contour" trace\_data=site.data.plotschema.traces.contour %}
---
permalink: /javascript/reference/layout/shapes/
layout: langindex
page\_type: reference
name: layout.shapes
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.shapes`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="shapes" %}
---
permalink: /javascript/reference/scatterpolar/
layout: langindex
page\_type: reference
name: scatterpolar Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scatterpolar` Traces

{% include posts/reference-trace.html trace\_name="scatterpolar" trace\_data=site.data.plotschema.traces.scatterpolar %}
---
permalink: /javascript/reference/barpolar/
layout: langindex
page\_type: reference
name: barpolar Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `barpolar` Traces

{% include posts/reference-trace.html trace\_name="barpolar" trace\_data=site.data.plotschema.traces.barpolar %}
---
permalink: /javascript/reference/box/
layout: langindex
page\_type: reference
name: box Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `box` Traces

{% include posts/reference-trace.html trace\_name="box" trace\_data=site.data.plotschema.traces.box %}
---
permalink: /javascript/reference/table/
layout: langindex
page\_type: reference
name: table Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `table` Traces

{% include posts/reference-trace.html trace\_name="table" trace\_data=site.data.plotschema.traces.table %}
---
permalink: /javascript/reference/densitymap/
layout: langindex
page\_type: reference
name: densitymap Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `densitymap` Traces

{% include posts/reference-trace.html trace\_name="densitymap" trace\_data=site.data.plotschema.traces.densitymap %}
---
permalink: /javascript/reference/cone/
layout: langindex
page\_type: reference
name: cone Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `cone` Traces

{% include posts/reference-trace.html trace\_name="cone" trace\_data=site.data.plotschema.traces.cone %}
---
permalink: /javascript/reference/carpet/
layout: langindex
page\_type: reference
name: carpet Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `carpet` Traces

{% include posts/reference-trace.html trace\_name="carpet" trace\_data=site.data.plotschema.traces.carpet %}
---
permalink: /javascript/reference/scatter3d/
layout: langindex
page\_type: reference
name: scatter3d Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scatter3d` Traces

{% include posts/reference-trace.html trace\_name="scatter3d" trace\_data=site.data.plotschema.traces.scatter3d %}
---
permalink: /javascript/reference/layout/sliders/
layout: langindex
page\_type: reference
name: layout.sliders
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.sliders`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="sliders" %}
---
permalink: /javascript/reference/choroplethmap/
layout: langindex
page\_type: reference
name: choroplethmap Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `choroplethmap` Traces

{% include posts/reference-trace.html trace\_name="choroplethmap" trace\_data=site.data.plotschema.traces.choroplethmap %}
---
permalink: /javascript/reference/contourcarpet/
layout: langindex
page\_type: reference
name: contourcarpet Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `contourcarpet` Traces

{% include posts/reference-trace.html trace\_name="contourcarpet" trace\_data=site.data.plotschema.traces.contourcarpet %}
---
permalink: /javascript/reference/isosurface/
layout: langindex
page\_type: reference
name: isosurface Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `isosurface` Traces

{% include posts/reference-trace.html trace\_name="isosurface" trace\_data=site.data.plotschema.traces.isosurface %}
---
permalink: /javascript/reference/pie/
layout: langindex
page\_type: reference
name: pie Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `pie` Traces

{% include posts/reference-trace.html trace\_name="pie" trace\_data=site.data.plotschema.traces.pie %}
---
permalink: /javascript/reference/layout/annotations/
layout: langindex
page\_type: reference
name: layout.annotations
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.annotations`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="annotations" %}
---
permalink: /javascript/reference/histogram2dcontour/
layout: langindex
page\_type: reference
name: histogram2dcontour Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `histogram2dcontour` Traces

{% include posts/reference-trace.html trace\_name="histogram2dcontour" trace\_data=site.data.plotschema.traces.histogram2dcontour %}
---
permalink: /javascript/reference/scatterternary/
layout: langindex
page\_type: reference
name: scatterternary Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scatterternary` Traces

{% include posts/reference-trace.html trace\_name="scatterternary" trace\_data=site.data.plotschema.traces.scatterternary %}
---
permalink: /javascript/reference/layout/ternary/
layout: langindex
page\_type: reference
name: layout.ternary
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.ternary`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="ternary" %}
---
permalink: /javascript/reference/layout/xaxis/
layout: langindex
page\_type: reference
name: layout.xaxis
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.xaxis`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="xaxis" %}
---
permalink: /javascript/reference/layout/mapbox/
layout: langindex
page\_type: reference
name: layout.mapbox
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.mapbox`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="mapbox" %}
---
permalink: /javascript/reference/scattermap/
layout: langindex
page\_type: reference
name: scattermap Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scattermap` Traces

{% include posts/reference-trace.html trace\_name="scattermap" trace\_data=site.data.plotschema.traces.scattermap %}
---
permalink: /javascript/reference/densitymapbox/
layout: langindex
page\_type: reference
name: densitymapbox Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `densitymapbox` Traces

{% include posts/reference-trace.html trace\_name="densitymapbox" trace\_data=site.data.plotschema.traces.densitymapbox %}
---
permalink: /javascript/reference/scattergl/
layout: langindex
page\_type: reference
name: scattergl Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scattergl` Traces

{% include posts/reference-trace.html trace\_name="scattergl" trace\_data=site.data.plotschema.traces.scattergl %}
---
permalink: /javascript/reference/splom/
layout: langindex
page\_type: reference
name: splom Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `splom` Traces

{% include posts/reference-trace.html trace\_name="splom" trace\_data=site.data.plotschema.traces.splom %}
---
permalink: /javascript/reference/funnel/
layout: langindex
page\_type: reference
name: funnel Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `funnel` Traces

{% include posts/reference-trace.html trace\_name="funnel" trace\_data=site.data.plotschema.traces.funnel %}
---
permalink: /javascript/reference/parcoords/
layout: langindex
page\_type: reference
name: parcoords Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `parcoords` Traces

{% include posts/reference-trace.html trace\_name="parcoords" trace\_data=site.data.plotschema.traces.parcoords %}
---
permalink: /javascript/reference/pointcloud/
layout: langindex
page\_type: reference
name: pointcloud Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `pointcloud` Traces

{% include posts/reference-trace.html trace\_name="pointcloud" trace\_data=site.data.plotschema.traces.pointcloud %}
---
permalink: /javascript/reference/sunburst/
layout: langindex
page\_type: reference
name: sunburst Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `sunburst` Traces

{% include posts/reference-trace.html trace\_name="sunburst" trace\_data=site.data.plotschema.traces.sunburst %}
---
permalink: /javascript/reference/treemap/
layout: langindex
page\_type: reference
name: treemap Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `treemap` Traces

{% include posts/reference-trace.html trace\_name="treemap" trace\_data=site.data.plotschema.traces.treemap %}
---
permalink: /javascript/reference/bar/
layout: langindex
page\_type: reference
name: bar Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `bar` Traces

{% include posts/reference-trace.html trace\_name="bar" trace\_data=site.data.plotschema.traces.bar %}
---
permalink: /javascript/reference/layout/selections/
layout: langindex
page\_type: reference
name: layout.selections
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.selections`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="selections" %}
---
permalink: /javascript/reference/surface/
layout: langindex
page\_type: reference
name: surface Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `surface` Traces

{% include posts/reference-trace.html trace\_name="surface" trace\_data=site.data.plotschema.traces.surface %}
---
permalink: /javascript/reference/funnelarea/
layout: langindex
page\_type: reference
name: funnelarea Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `funnelarea` Traces

{% include posts/reference-trace.html trace\_name="funnelarea" trace\_data=site.data.plotschema.traces.funnelarea %}
---
permalink: /javascript/reference/layout/smith/
layout: langindex
page\_type: reference
name: layout.smith
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.smith`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="smith" %}
---
permalink: /javascript/reference/histogram/
layout: langindex
page\_type: reference
name: histogram Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `histogram` Traces

{% include posts/reference-trace.html trace\_name="histogram" trace\_data=site.data.plotschema.traces.histogram %}
---
permalink: /javascript/reference/ohlc/
layout: langindex
page\_type: reference
name: ohlc Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `ohlc` Traces

{% include posts/reference-trace.html trace\_name="ohlc" trace\_data=site.data.plotschema.traces.ohlc %}
---
permalink: /javascript/reference/volume/
layout: langindex
page\_type: reference
name: volume Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `volume` Traces

{% include posts/reference-trace.html trace\_name="volume" trace\_data=site.data.plotschema.traces.volume %}
---
permalink: /javascript/reference/histogram2d/
layout: langindex
page\_type: reference
name: histogram2d Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `histogram2d` Traces

{% include posts/reference-trace.html trace\_name="histogram2d" trace\_data=site.data.plotschema.traces.histogram2d %}
---
permalink: /javascript/reference/indicator/
layout: langindex
page\_type: reference
name: indicator Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `indicator` Traces

{% include posts/reference-trace.html trace\_name="indicator" trace\_data=site.data.plotschema.traces.indicator %}
---
permalink: /javascript/reference/violin/
layout: langindex
page\_type: reference
name: violin Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `violin` Traces

{% include posts/reference-trace.html trace\_name="violin" trace\_data=site.data.plotschema.traces.violin %}
---
permalink: /javascript/reference/layout/scene/
layout: langindex
page\_type: reference
name: layout.scene
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.scene`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="scene" %}
---
permalink: /javascript/reference/candlestick/
layout: langindex
page\_type: reference
name: candlestick Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `candlestick` Traces

{% include posts/reference-trace.html trace\_name="candlestick" trace\_data=site.data.plotschema.traces.candlestick %}
---
permalink: /javascript/reference/scattercarpet/
layout: langindex
page\_type: reference
name: scattercarpet Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scattercarpet` Traces

{% include posts/reference-trace.html trace\_name="scattercarpet" trace\_data=site.data.plotschema.traces.scattercarpet %}
---
permalink: /javascript/reference/layout/images/
layout: langindex
page\_type: reference
name: layout.images
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.images`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="images" %}
---
permalink: /javascript/reference/heatmap/
layout: langindex
page\_type: reference
name: heatmap Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `heatmap` Traces

{% include posts/reference-trace.html trace\_name="heatmap" trace\_data=site.data.plotschema.traces.heatmap %}
---
permalink: /javascript/reference/layout/updatemenus/
layout: langindex
page\_type: reference
name: layout.updatemenus
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.updatemenus`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="updatemenus" %}
---
permalink: /javascript/reference/icicle/
layout: langindex
page\_type: reference
name: icicle Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `icicle` Traces

{% include posts/reference-trace.html trace\_name="icicle" trace\_data=site.data.plotschema.traces.icicle %}
---
permalink: /javascript/reference/image/
layout: langindex
page\_type: reference
name: image Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `image` Traces

{% include posts/reference-trace.html trace\_name="image" trace\_data=site.data.plotschema.traces.image %}
---
permalink: /javascript/reference/sankey/
layout: langindex
page\_type: reference
name: sankey Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `sankey` Traces

{% include posts/reference-trace.html trace\_name="sankey" trace\_data=site.data.plotschema.traces.sankey %}
---
permalink: /javascript/reference/scattergeo/
layout: langindex
page\_type: reference
name: scattergeo Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scattergeo` Traces

{% include posts/reference-trace.html trace\_name="scattergeo" trace\_data=site.data.plotschema.traces.scattergeo %}
---
permalink: /javascript/reference/streamtube/
layout: langindex
page\_type: reference
name: streamtube Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `streamtube` Traces

{% include posts/reference-trace.html trace\_name="streamtube" trace\_data=site.data.plotschema.traces.streamtube %}
---
permalink: /javascript/reference/mesh3d/
layout: langindex
page\_type: reference
name: mesh3d Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `mesh3d` Traces

{% include posts/reference-trace.html trace\_name="mesh3d" trace\_data=site.data.plotschema.traces.mesh3d %}
---
permalink: /javascript/reference/layout/
layout: langindex
page\_type: reference
name: layout
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="global" %}
{%- for trace in site.data.plotschema.traces -%}
{% if trace[1].layoutAttributes %}
{% assign attribute=trace[1].layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" %}
{% endif %}
{%- endfor -%}
---
permalink: /javascript/reference/layout/geo/
layout: langindex
page\_type: reference
name: layout.geo
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.geo`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="geo" %}
---
permalink: /javascript/reference/heatmapgl/
layout: langindex
page\_type: reference
name: heatmapgl Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `heatmapgl` Traces

{% include posts/reference-trace.html trace\_name="heatmapgl" trace\_data=site.data.plotschema.traces.heatmapgl %}
---
permalink: /javascript/reference/parcats/
layout: langindex
page\_type: reference
name: parcats Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `parcats` Traces

{% include posts/reference-trace.html trace\_name="parcats" trace\_data=site.data.plotschema.traces.parcats %}
---
permalink: /javascript/reference/layout/coloraxis/
layout: langindex
page\_type: reference
name: layout.coloraxis
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.coloraxis`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="coloraxis" %}
---
permalink: /javascript/reference/scatterpolargl/
layout: langindex
page\_type: reference
name: scatterpolargl Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scatterpolargl` Traces

{% include posts/reference-trace.html trace\_name="scatterpolargl" trace\_data=site.data.plotschema.traces.scatterpolargl %}
---
permalink: /javascript/reference/scattermapbox/
layout: langindex
page\_type: reference
name: scattermapbox Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scattermapbox` Traces

{% include posts/reference-trace.html trace\_name="scattermapbox" trace\_data=site.data.plotschema.traces.scattermapbox %}
---
permalink: /javascript/reference/layout/yaxis/
layout: langindex
page\_type: reference
name: layout.yaxis
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.yaxis`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="yaxis" %}
---
permalink: /javascript/reference/choropleth/
layout: langindex
page\_type: reference
name: choropleth Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `choropleth` Traces

{% include posts/reference-trace.html trace\_name="choropleth" trace\_data=site.data.plotschema.traces.choropleth %}
---
permalink: /javascript/reference/scattersmith/
layout: langindex
page\_type: reference
name: scattersmith Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `scattersmith` Traces

{% include posts/reference-trace.html trace\_name="scattersmith" trace\_data=site.data.plotschema.traces.scattersmith %}
---
permalink: /javascript/reference/layout/polar/
layout: langindex
page\_type: reference
name: layout.polar
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `layout.polar`

{% assign attribute=site.data.plotschema.layout.layoutAttributes %}
{% include posts/reference-block.html parentlink="layout" block="layout" parentpath="layout" mustmatch="polar" %}
---
permalink: /javascript/reference/waterfall/
layout: langindex
page\_type: reference
name: waterfall Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `waterfall` Traces

{% include posts/reference-trace.html trace\_name="waterfall" trace\_data=site.data.plotschema.traces.waterfall %}
---
permalink: /javascript/reference/choroplethmapbox/
layout: langindex
page\_type: reference
name: choroplethmapbox Traces
description: Figure attribute reference for Plotly's JavaScript open-source graphing library.
---

## JavaScript Figure Reference: `choroplethmapbox` Traces

{% include posts/reference-trace.html trace\_name="choroplethmapbox" trace\_data=site.data.plotschema.traces.choroplethmapbox %}
