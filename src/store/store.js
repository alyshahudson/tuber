import Vue from 'vue';
import Vuex from 'vuex';


// Modules
import events from './modules/events';
import user from './modules/user';
import snackbar from './modules/snackbar';
import shifts from './modules/shifts';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  modules: {
    events,
    user,
    snackbar,
    shifts,
  },
});
