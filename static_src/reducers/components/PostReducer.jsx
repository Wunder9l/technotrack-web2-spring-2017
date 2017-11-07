import {Map, List} from 'immutable';
import {
    ERROR_POST_LOADING,
    SUCCESSFUL_POST_LOADING,
    START_POST_LOADING,
} from '../../actions/components/PostAction';

const initialState = Map({
    isLoading: false,
    postList: Map(),
});


const reducer = (store = initialState, action) => {
    // return store;
    switch (action.type) {
        case START_POST_LOADING: {
            return store.set('isLoading', true);
        }
        case SUCCESSFUL_POST_LOADING: {
            console.log('SUCCESSFUL_POST_LOADING', action);
            const newPost = {};
            newPost[action.payload.id] = action.payload;
            return store.mergeDeep(Map({postList: Map(newPost), isLoading: false}));
            // const merging = Map({postList: Map(newPost), isLoading: false})
            // const one = Map({a: Map({x: 10, y: 10}), b: Map({x: 20, y: 50})})
            // const two = Map({a: Map({x: 2}), b: Map({y: 5}), c: Map({z: 3})})
            // one.mergeDeep(two)
            // debugger;
            // return store; //.merge(Map({isLoading: false, postList: Map(action.payload)}));
        }
        case ERROR_POST_LOADING: {
            console.log('ERROR', action);
            return store.set('isLoading', false);
        }
        default:
            return store;
    }
};

export default reducer;