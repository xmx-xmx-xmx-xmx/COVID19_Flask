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
gettime()
setInterval(gettime, 1000) // 一秒钟执行一次这个函数

function get_center1_data(){
    $.ajax({
url: "/center1",
success: function(data) {
    $("#num h1").eq(0).text(data.confirm)
     // 后台定义方法get时间 eq 选第几个
    $("#num h1").eq(1).text(data.suspect)
    $("#num h1").eq(2).text(data.heal)
    $("#num h1").eq(3).text(data.dead)
},
error: function(xhr, type, errorThrown) {

}
});
}
get_center1_data()
setInterval(get_center1_data, 1000) // 一秒钟执行一次这个函数

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
get_center2_data()
setInterval(get_center2_data, 1000)

function get_left1_data(){
    $.ajax({
        url:"/left1",
        success:function(data){
            ec_left1_option.xAxis[0].data=data.day
            ec_left1_option.xAxis[1].data=data.confirm
            ec_left1_option.xAxis[2].data=data.suspect
            ec_left1_option.xAxis[3].data=data.heal
            ec_left1_option.xAxis[4].data=data.dead
            ec_left1.setOption(ec_left1_option)
        },
        error:function(xhr,type,errorThrown){}
    })
}
get_left1_data()
setInterval(get_left1_data, 1000)

function get_left2_data(){

}
get_left2_data()
setInterval(get_left2_data, 1000)