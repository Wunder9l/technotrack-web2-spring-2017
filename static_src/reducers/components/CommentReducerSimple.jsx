import {update} from 'react-addons-update';
import {
    ERROR_COMMENT_LOADING,
    SUCCESSFUL_COMMENT_LOADING,
    START_COMMENT_LOADING,
} from '../../actions/components/Comment';

const initialState = {
    comments: {
        commentList: [],
        isLoading: false,
    },
};


const reducer = (store = initialState, action) => {
    console.log(action, store);
    // return store;
    switch (action.type) {
        case START_COMMENT_LOADING: {
            return fromJS(store).set('isLoading', true);
        }
        case SUCCESSFUL_COMMENT_LOADING: {
            return store.merge(Map({isLoading: false, commentList: action.payload}));
        }
        case ERROR_COMMENT_LOADING: {
            console.log('ERROR', action);
            return store.set('isLoading', true);
        }
        default:
            return store;
    }
};

export default reducer;