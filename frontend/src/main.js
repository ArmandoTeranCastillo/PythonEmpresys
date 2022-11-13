import { createApp } from 'vue';
import App from './App.vue';
import barchart from './components/barchart.vue';



const app = createApp(App);
app.component('barchart', barchart);
createApp(App).mount('#app');
