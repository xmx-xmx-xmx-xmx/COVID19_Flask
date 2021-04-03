function gettime(){
    $.ajax({
url: "/time",
    timeout: 10000, // 超时时间设置为10秒；
success: function(data) {
    $("#time").html(data) // 后台定义方法get时间
},
error: function(xhr, type, errorThrown) {

}
});
}

function get_center1_data(){
    $.ajax({
url: "/center1",
success: function(data) {
    $("#num h1").eq(0).text(data.confirm)
     // 后台定义方法get数据 eq 选第几个
    $("#num h1").eq(1).text(data.suspect)
    $("#num h1").eq(2).text(data.heal)
    $("#num h1").eq(3).text(data.dead)
},
error: function(xhr, type, errorThrown) {

}
});
}

function get_center2_data(){
    $.ajax({
        url:"/center2",
        success:function(data){
            ec_center_option.series[0].data=data.data
             //0!!!
            ec_center.setOption(ec_center_option)
        },
        error:function(xhr,type,errorThrown){}
    });
}


function get_left1_data(){
    $.ajax({
        url:"/left1",
        success:function(data){
            ec_left1_option.xAxis.data=data.day
            ec_left1_option.series[0].data=data.confirm
            ec_left1_option.series[1].data=data.suspect
            ec_left1_option.series[2].data=data.heal
            ec_left1_option.series[3].data=data.dead
            ec_left1.setOption(ec_left1_option)
        },
        error:function(xhr,type,errorThrown){}
    })
}


function get_left2_data(){
    $.ajax({
        url:"/left2",
        success:function(data){
            ec_left2_option.xAxis.data=data.ds
            ec_left2_option.series[0].data=data.confirm_add
            ec_left2_option.series[1].data=data.suspect_add
            ec_left2.setOption(ec_left2_option)
        },
        error:function(xhr,type,errorThrown){}
    })
}


function get_right1_data(){
    $.ajax({
        url:"/right1",
        success:function(data){
            ec_right1_option.xAxis.data=data.city
            ec_right1_option.series[0].data=data.confirm
            ec_right1.setOption(ec_right1_option)
        },
        error:function(xhr,type,errorThrown){}
    })
}

gettime()
get_center1_data()
get_center2_data()
get_left1_data()
get_left2_data()
get_right1_data()
setInterval(gettime, 1000) // 时间刷新，一秒钟执行一次这个函数
setInterval(get_center1_data, 100000) // 这些不需要过于频繁刷新，一小时执行一次这个函数
setInterval(get_center2_data, 100000)
setInterval(get_left1_data, 100000)
setInterval(get_left2_data, 100000)
setInterval(get_right1_data, 100000)