// 绘制中国地图
var ec_center = echarts.init(document.getElementById('center2',"dark"));

var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}] // 外面：数组 / list 里面：json / 字典 测试数据

var ec_center_option = {
    title: {
        text: '',
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    //左侧小导航图标
    visualMap: {
        show: true,
        x: 'left',
        y: 'top',
        textStyle: {
            fontSize: 10,
            color: '#ffffff'
        },
        splitList: 
            [{ start: 1,end: 9 },
            {start: 10, end: 99 }, 
			{ start: 100, end: 999 },
            {  start: 1000, end: 9999 },
            { start: 10000 }],
        color: ['#8A3310', '#C64918', '#E55B25', '#F2AD92', '#F9DCD1']
    },
    //配置属性
    series: [{
        name: '累计确诊人数',
        type: 'map',
        mapType: 'china',
        roam: false, //拖动和缩放
        zoom: 0.8,
        itemStyle: {
            normal: {
                borderWidth: .4, //区域边框宽度
                borderColor: '#009fe8', //区域边框颜色
                areaColor: "#ffefd5", //区域颜色
            },
            emphasis: { //鼠标滑过地图高亮的相关设置
                borderWidth: .4,
                borderColor: '#4b0082',
                areaColor: "#fff",
            }
        },
        label: {
            normal: {
                show: true, //省份名称
                fontSize: 10,
            },
            emphasis: {
                show: true,
                fontSize: 10,
            }
        },
        data:[] //mydata //数据
    }]
};
ec_center.setOption(ec_center_option)