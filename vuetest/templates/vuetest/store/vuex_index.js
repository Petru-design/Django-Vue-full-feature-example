const coachesModule = {% include './modules/coaches/index.js' %}


const store = Vuex.createStore({
    modules: {
        coaches: coachesModule
    },

    state() {
        return {       
            
        }
    },
    mutations: {

    },
    getters: {

    },

    actions: {

    }
});