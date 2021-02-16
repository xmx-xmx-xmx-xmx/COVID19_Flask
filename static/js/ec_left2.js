var ec_left2 = echarts.init(document.getElementById('left2',"dark")); // dark是一种主题 官网可以换主题

var ec_left2_option = {
    title: {
        text: '新增趋势展示',
        left: 'left',
        color: '#fff',
        textStyle:
        {color: "#ffffff"}
    },
    tooltip: {
        trigger: 'axis', // 指示器
        axisPointer: {
			type: 'line',
			lineStyle: {
				color: '#7171C6'
			}
		},
    },
    legend: {
        data: ['新增确诊', '新增疑似'],
        left: 'center',
        textStyle:
        {color: "#ffffff"}
    },
    // 图形位置
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        top: 50,
        containLabel: true
    },
    toolbox: {
        itemSize: 15,
        showTitle: true,
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        axisLabel:{color: 'white',},
        //x轴坐标点开始与结束点位置都不在最边缘
		// boundaryGap : true,
		data: []//['01.20', '01.21', '01.22']
    },
    yAxis: [{
        type: 'value',
		axisLabel: {
			show: true,
			color: 'white',
			fontSize: 12,
			formatter: function(value) {
				if (value >= 1000) {
					value = value / 1000 + 'k';
				}
				return value;
			}
		},
		//y轴线设置显示
		axisLine: {
			show: true
		},
		//与x轴平行的线样式
		splitLine: {
			show: true,
			lineStyle: {
				color: '#17273B',
				width: 1,
				type: 'solid',
			}
		}
    }],
    series: [
        {
            name: '新增确诊',
            type: 'line',
            smooth: true,
            data: []
        },
        {
            name: '新增疑似',
            type: 'line',
            smooth: true,
            data: []
        }
    ]
};

ec_left2.setOption(ec_left2_option)