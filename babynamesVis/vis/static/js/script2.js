var svg = d3.select("svg"),
margin = {top: 20, right: 20, bottom: 30, left: 50},
width = +svg.attr("width") - margin.left - margin.right,
height = +svg.attr("height") - margin.top - margin.bottom,
g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var parseTime = d3.timeParse("%Y");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.n); });

var searchRequest = null;

$(document).ready(function() {
    var minlength = 2;
    $('#your_name').keyup(function() {
        value = $(this).val();

        if (value.length >= minlength ) {
            if (searchRequest != null) {
                searchRequest.abort();
            }        
            searchRequest = $.ajax({
                url: 'api/v3/' + value + '/?format=json',
                type: "GET",
                dataType : "json",
                })
                .done(function( json ) {
                    //console.log( json );
                    var post_data = json;
                    drawChart(post_data);
            })
        }    
    });
});

function drawChart(data){
    for(var i = 0; i < data.length; i++) {
        data[i]['year'] = parseTime(data[i]['year']);
    }

    d3.selectAll("g > *").remove();

    nv.addGraph(function() {
        var chart = nv.models.lineChart()
          .useInteractiveGuideline(true);
      
        chart.xAxis
          .axisLabel('Year')
          //.tickFormat(d3.format(',r'));
      
        chart.yAxis
          .axisLabel('Number')
          //.tickFormat(d3.format('.02f'));
      
        g.datum(data)
          .transition().duration(500)
          .call(chart);
      
        nv.utils.windowResize(chart.update);
      
        return chart;
      });
}

