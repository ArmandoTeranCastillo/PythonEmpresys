<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import axios from 'axios';
import moment from 'moment';
export default {
  name: 'App',
  components: {

  },
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
      data.forEach(d => {
        const {
          data,
          years,
          entity,
        } = d;
        this.Census.push([data, years, entity,]);
      })
      console.log(this.Census)
    })





  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
