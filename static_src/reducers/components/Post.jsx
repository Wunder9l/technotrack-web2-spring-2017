import update from 'react-addons-update';
import {
    ERROR_POST_LOADING,
    SUCCESSFUL_POST_LOADING,
    START_POST_LOADING,
} from '../../actions/components/Post';

const initialState = {
    posts: {
        isLoading: false,
        post_object: [],
    },
};


const reducer = (store = initialState, action) => {
    // return store;
    switch (action.type) {
        case START_POST_LOADING: {
            return update(store, {isLoading: {$set: true}});
        }
        case SUCCESSFUL_POST_LOADING: {
            console.log('SUCCESSFUL_POST_LOADING', action);
            return update(store, {isLoading: {$set: false}, posts: {$merge: [action.payload]}});
        }
        case ERROR_POST_LOADING: {
            console.log('ERROR', action);
            return update(store, {isLoading: {$set: false}});
        }
        default:
            return store;
    }
};

export default reducer;