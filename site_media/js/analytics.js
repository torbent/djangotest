$(function(){

    // this is the example code from http://g.raphaeljs.com/
    var r = Raphael("chart");
    var lines = r.linechart(10, 10, 300, 200, [[1, 2, 3, 4, 5, 6, 7],[3.5, 4.5, 5.5, 6.5, 7, 8]], [[12, 32, 23, 15, 17, 27, 22], [10, 20, 30, 25, 15, 28]], { nostroke: false, axis: "0 0 1 1", smooth: true });

})