var endpoint = "/api";
            $.ajax({
                method:"GET",
                url:endpoint,
                success: function(data){
                    drawLineGraph(data, 'myChartline');
                    drawBarGraph(data, 'myChartBar');
                },
                error: function(error_data){
                    console.log(error_data)
                }
            })

            function drawLineGraph(data,id){
                var labels = data.yearSummary.labels;
                var chartLabel = data.yearSummary.chartLabel;
                var chartdata = data.yearSummary.paperCount;

                var ctx = document.getElementById(id).getContext('2d');
                var chart = new Chart(ctx,{
                    type:'line',
                    data: {
                        labels: labels,
                        datasets: [{
                            label: chartLabel,
                            borderColor: 'rgb(75, 192, 192)',
                            data: chartdata,
                            tension: 0.1
                        }]
                    },
                    options: {
                        scales: {
                            xAxes: [{
                                display: true
                            }],
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true,
                                    userCallback: function(label, index, labels) {
                                    // when the floored value is the same as the value we have a whole number
                                        if (Math.floor(label) === label) {
                                            return label;
                                        }
                                    },
                                }
                            }]
                        }
                    }
                });
            }

            function drawBarGraph(data, id) {
                var labels = data.authorSummary.labels;
                var chartLabel = data.authorSummary.chartLabel;
                var chartdata = data.authorSummary.paperCount;

                var ctx = document.getElementById(id).getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                    labels: labels,
                    datasets: [{
                        label: chartLabel,
                        data: chartdata,
                        backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                        ],
                        borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }]
                    },
                    options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true,
                                userCallback: function(label, index, labels) {
                                        // when the floored value is the same as the value we have a whole number
                                    if (Math.floor(label) === label) {
                                                return label;
                                    }
                                },
                            }
                        }]
                    }
                    }
                });
                }