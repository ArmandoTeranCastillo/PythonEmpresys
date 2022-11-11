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
}
</script>

<style lang="css" scoped>
</style>