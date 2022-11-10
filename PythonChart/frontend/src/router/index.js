import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import listgraph from '@/components/graph/listgraph'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    //JSON para las graficas
     {
      path: '/graph',
      name: 'listgraph',
      component: listgraph
     } 
  ],
  //Trabajar con los componentes a traves de URLs
  mode: 'history'
})
