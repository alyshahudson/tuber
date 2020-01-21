// import { get } from '../../mixins/rest';

export default {
  namespaced: true,
  state: {
    shifts: [],
  },
  actions: {
    getShifts({ commit }) {
      get('/api/shifts/list')
        .then((response) => {
          commit('importShifts', response.data);
        });
    },
  },
  mutations: {
    importShifts(data) {
      state.shifts = data.shifts;
    },
  },
};
