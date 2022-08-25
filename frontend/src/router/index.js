import Vue from 'vue'
import VueRouter from 'vue-router'
import DefaultView from '../views/DefaultView';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: DefaultView
  },
  {
    path: '/map/:id',
    name: 'map',
    component: () => import(/* webpackChunkName: "map" */ '../views/MapView')
  },
  {
    path: '/404',
    component: () => import(/* webpackChunkName: "map" */ '../views/NotFound')
  },
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  routes
})

export default router
