// 百度热搜接口不可用，此js文件弃用
var ec_right2 = echarts.init(document.getElementById('right2'));

var kws = [{
	name: 'Sam S Club',
	value: 10000,
	textStyle: {
		color: 'black'
	},
	emphasis: {
		textStyle: {
			color: 'red'
		}
	}
},
{
	name: 'Macys',
	value: 6181
},
{
	name: 'Amy Schumer',
	value: 4386
},
{
	name: 'Jurassic World',
	value: 4055
},
{
	name: 'Charter Communications',
	value: 2467
},
{
	name: 'Chick Fil A',
	value: 2244
},
{
	name: 'Planet Fitness',
	value: 1898
},
{
	name: 'Pitch Perfect',
	value: 1484
},
{
	name: 'Express',
	value: 1112
},
{
	name: 'Home',
	value: 965
},
{
	name: 'Johnny Depp',
	value: 847
},
{
	name: 'Lena Dunham',
	value: 582
},
{
	name: 'Lewis Hamilton',
	value: 555
},
{
	name: 'KXAN',
	value: 550
},
{
	name: 'Mary Ellen Mark',
	value: 462
},
{
	name: 'Farrah Abraham',
	value: 366
},
{
	name: 'Rita Ora',
	value: 360
},
{
	name: 'Serena Williams',
	value: 282
},
{
	name: 'NCAA baseball tournament',
	value: 273
},
{
	name: 'Point Break',
	value: 265
}];
var option_right2 = {
	title: {
		text: "今日疫情热搜",
		textStyle: {
			color: 'white'
		},
		left: 'left'
	},
	tooltip: {
		show: false
	},
	series: [{
		type: 'wordCloud',
		gridSize: 1,
		sizeRange: [12, 55], //文字范围
		//文本旋转范围，文本将通过rotationStep45在[-90,90]范围内随机旋转
		rotationRange: [-45, 0, 45, 90],
		// rotationStep: 45,
		// textRotation: [0, 45, 90, -45],
		// //形状
		// shape: 'circle',
		textStyle: {
			normal: {
				color: function() { //文字颜色的随机色
					// return 'rgb(' + [
					// 	Math.round(Math.random() * 250),
					// 	Math.round(Math.random() * 250),
					// 	Math.round(Math.random() * 250)
					// ].join(',') + ')';
					return 'rgb(' +
						Math.round(Math.random() * 255) +
						',' + Math.round(Math.random() * 255) +
						',' + Math.round(Math.random() * 255) + ')'
				}
			}
		},
		right: null,
		bottom: null,
		data: kws
	}]
};
//使用制定的配置项和数据显示图表

// var option_right2 = {
// 	tooltip: {},
// 	series: [ {
// 		type: 'wordCloud',
// 		gridSize: 2,
// 		sizeRange: [12, 50],
// 		rotationRange: [-90, 90],
// 		shape: 'pentagon',
// 		width: 600,
// 		height: 400,
// 		drawOutOfBound: true,
// 		textStyle: {
// 			color: function () {
// 				return 'rgb(' + [
// 					Math.round(Math.random() * 160),
// 					Math.round(Math.random() * 160),
// 					Math.round(Math.random() * 160)
// 				].join(',') + ')';
// 			}
// 		},
// 		emphasis: {
// 			textStyle: {
// 				shadowBlur: 10,
// 				shadowColor: '#333'
// 			}
// 		},
// 		data: [
// 			{
// 				name: 'Sam S Club',
// 				value: 10000,
// 				textStyle: {
// 					color: 'black'
// 				},
// 				emphasis: {
// 					textStyle: {
// 						color: 'red'
// 					}
// 				}
// 			},
// 			{
// 				name: 'Macys',
// 				value: 6181
// 			},
// 			{
// 				name: 'Amy Schumer',
// 				value: 4386
// 			},
// 			{
// 				name: 'Jurassic World',
// 				value: 4055
// 			},
// 			{
// 				name: 'Charter Communications',
// 				value: 2467
// 			},
// 			{
// 				name: 'Chick Fil A',
// 				value: 2244
// 			},
// 			{
// 				name: 'Planet Fitness',
// 				value: 1898
// 			},
// 			{
// 				name: 'Pitch Perfect',
// 				value: 1484
// 			},
// 			{
// 				name: 'Express',
// 				value: 1112
// 			},
// 			{
// 				name: 'Home',
// 				value: 965
// 			},
// 			{
// 				name: 'Johnny Depp',
// 				value: 847
// 			},
// 			{
// 				name: 'Lena Dunham',
// 				value: 582
// 			},
// 			{
// 				name: 'Lewis Hamilton',
// 				value: 555
// 			},
// 			{
// 				name: 'KXAN',
// 				value: 550
// 			},
// 			{
// 				name: 'Mary Ellen Mark',
// 				value: 462
// 			},
// 			{
// 				name: 'Farrah Abraham',
// 				value: 366
// 			},
// 			{
// 				name: 'Rita Ora',
// 				value: 360
// 			},
// 			{
// 				name: 'Serena Williams',
// 				value: 282
// 			},
// 			{
// 				name: 'NCAA baseball tournament',
// 				value: 273
// 			},
// 			{
// 				name: 'Point Break',
// 				value: 265
// 			}
// 		]
// 	} ]
// };

ec_right2.setOption(ec_right2_option);

// window.onresize = chart.resize;