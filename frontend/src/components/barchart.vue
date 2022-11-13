<template>
  <h3>Censo Poblacional</h3>
  <canvas id="myChart" width="400" height="400"></canvas>
  
</template>


<script>
import Chart from 'chart.js/auto';
import axios from 'axios';
export default {
  name: 'barchart',
  props:{msg:String},

  data(){
    return{
      GraphLabels: [],
      X_Labels: [],
      Y_Labels: [],
      Years: [],
      Entities: [],
      Census: [],
    }
  },

  created(){
    let urlGraph = 'http://127.0.0.1:8000/api/graph/'
    let urlX_axis_labels = 'http://127.0.0.1:8000/api/x_axis_labels/'
    let urlY_axis_labels = 'http://127.0.0.1:8000/api/y_axis_labels/'
    let urlYear = 'http://127.0.0.1:8000/api/year/'
    let urlEntity = 'http://127.0.0.1:8000/api/entity/'
    let urlCensus = 'http://127.0.0.1:8000/api/census/'
    
    function isMan(){

    }


    function axiosGraph(){
      const promise = axios.get(urlGraph)
      const dataPromise = promise.then((response) => response.data);
      return dataPromise
    }
    axiosGraph().then(data => {
      data.forEach(d => {
        const {
          title,
          x_axis_title,
          y_axis_title,
        } = d
        this.GraphLabels.push(title, x_axis_title, y_axis_title)
      })
      console.log(this.GraphLabels)
    })


    function axiosX_axis_labels(){
      const promise = axios.get(urlX_axis_labels)
      const dataPromise = promise.then((response) => response.data);
      return dataPromise
    }
    axiosX_axis_labels().then(data => {
      data.forEach(d => {
        const {
          label,
        } = d;
        this.X_Labels.push(label);
      })
      console.log(this.X_Labels)
    })


    function axiosY_axis_labels(){
      const promise = axios.get(urlY_axis_labels)
      const dataPromise = promise.then((response) => response.data);
      return dataPromise
    }
    axiosY_axis_labels().then(data => {
      data.forEach(d => {
        const {
          label,
        } = d;
        this.Y_Labels.push(label);
      })
      console.log(this.Y_Labels)
    })

  
    function axiosYears(){
      const promise = axios.get(urlYear)
      const dataPromise = promise.then((response) => response.data);
      return dataPromise
    }
    axiosYears().then(data => {
      data.forEach(d => {
        const {
          year,
        } = d;
        this.Years.push(year);
      })
      console.log(this.Years)
    })


    function axiosEntity(){
      const promise = axios.get(urlEntity)
      const dataPromise = promise.then((response) => response.data);
      return dataPromise
    }
    axiosEntity().then(data => {
      data.forEach(d => {
        const {
          Entity,
        } = d;
        this.Entities.push(Entity);
      })
      console.log(this.Entities)
    })

    function axiosCensus(){
      const promise = axios.get(urlCensus)
      const dataPromise = promise.then((response) => response.data);
      return dataPromise
    }
    axiosCensus().then(data => {
      this.Census = data
      console.log(this.Census)
     /* data.forEach(d => {
        const {
          data,
          years,
          entity,
        } = d;
        this.Census.push([data, years, entity,]);
      })
      console.log(this.Census)*/

    })

  },

  mounted(){
    const ctx = document.getElementById('myChart').getContext('2d');
    const myChart = new Chart(ctx, {
    
    
    type: 'bar',
    data: {
        labels: this.Y_Labels,
        datasets: [{
            label: 'Hombres',
            data: [2.0, 2.1, 2.3, 2.4, 2.1, 2.0, 1.9, 1.8, 1.7, 1.6],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
            ],
            borderWidth: 1,  
          },
          {
            label: 'Mujeres',
            data: [2.0, 2.2, 2.3, 2.3, 2.2, 2.0, 1.9, 1.8, 1.7, 1.6],
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
            y: {
                beginAtZero: true
            }
        }
    }
});


myChart;
  },
  methods: {
  }

}

</script>