function createPieGraph( data ) {
    nv.addGraph(function() {
      width = $(".pie_graph_container").width();
      height =$(".pie_graph_container").height();

      var chart = nv.models.pieChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .showLabels(true)
          .width(width).height(height);

      d3.select("#pie_graph")
        .attr("width", "400px")
        .attr("height", "400px")
        .attr('viewBox','0 0 '+width+' '+height)
        .attr('preserveAspectRatio','xMinYMin')
        .datum(data)
        .transition().duration(350)
        .call(chart);

      return chart;
    });
}

function createChartGraph( data )
{
    nv.addGraph(function () {
        width = $(".chart_graph_container").width();
        height = 0.5 * width;

        var chart = nv.models.lineChart()
            .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
            .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
            .duration(350)  //how fast do you want the lines to transition?
            .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
            .showYAxis(true)        //Show the y-axis
            .showXAxis(true)
            .width(width).height(height);

        chart.xAxis     //Chart x-axis settings
            .axisLabel('Time (ms)')
            .tickFormat(d3.format(',r'));

        chart.yAxis     //Chart y-axis settings
            .axisLabel('Voltage (v)')
            .tickFormat(d3.format('.02f'));


        d3.select('#chart_graph')    //Select the <svg> element you want to render the chart in.
            .datum(data)
            .attr('viewBox','0 0 '+width+' '+height)
            .call(chart)

        //Update the chart when window resizes.
        nv.utils.windowResize(function () {
            chart.update()
        });
        return chart;
    });
}