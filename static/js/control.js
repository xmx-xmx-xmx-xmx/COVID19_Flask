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