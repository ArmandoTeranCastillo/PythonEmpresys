<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de Graficos</h2>
            <div class="col-md-12">
                <b-table striped hover :items="graph" :fields="fields">
                </b-table>
            </div>
        </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
//Inicializar los campos de la tabla
    data(){
        return{
            fields: [
                {key: 'title', label:'Censo Poblacional'},
                {key: 'x_axis_title', label: 'Porcentaje'},
                {key: 'y_axis_title', label: 'Edades'}
            ],
            graph: []
        }
    },
    //Crear lista de funciones
    methods: {
        getGraph(){
            //Llamar al servidor Django para obtener las graficas
            const path = 'http://localhost:8000/api/v1.0/graphs/'
            axios.get(path).then((response) => {
                this.graph = response.data
            })
            .catch((error) => {
              console.log(error)  
            })
        },
        created(){
            this.getGraph()
        }

    }
}
</script>

<style lang="css" scoped>
</style>