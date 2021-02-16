var ec_right1 = echarts.init(document.getElementById('right1',"dark")); // dark是一种主题 官网可以换主题

var ec_right1_option = {
    title: {
        text: '非湖北城市确诊TOP5',
        left: 'left',
        color: '#fff',
        textStyle:
        {color: "#ffffff"}
    },
    xAxis: {
        type: 'category',
        data: [],
        axisLabel:{color: 'white',}
    },
    yAxis: {
        type: 'value',
        axisLabel:{color: 'white',}
    },
    tooltip: {
		trigger: 'axis',
		axisPointer: {
			type: 'shadow'},
	},
    toolbox: {
        itemSize: 15,
        showTitle: true,
        feature: {
            saveAsImage: {}
        }
    },
    series: [{
        data: [],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(180, 180, 180, 0.2)'
        },
        itemStyle:{
            color:'#5C7BD9'
        },
    }]    
};

ec_right1.setOption(ec_right1_option)