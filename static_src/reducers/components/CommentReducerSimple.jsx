import update from 'react-addons-update';
import {
    ERROR_COMMENT_LOADING,
    SUCCESSFUL_COMMENT_LOADING,
    START_COMMENT_LOADING,
    ADD_COMMENT,
} from '../../actions/components/Comment';

const initialState = {
    comments: {
        commentList: [],
        isLoading: false,
    },
};
// const initialState = Map({
//     comments: {
//         commentList: [],
//         isLoading: false,
//     },
// });

const reducer = (store = initialState, action) => {
    console.log(action, store);
    // return store;
    switch (action.type) {
        case START_COMMENT_LOADING: {
            return update(store, {isLoading: {$set: true}});
        }
        case SUCCESSFUL_COMMENT_LOADING: {
            return update(store, {isLoading: {$set: false}, commentList: {$set: action.payload}});
        }
        case ERROR_COMMENT_LOADING: {
            console.log('ERROR', action);
            return update(store, {isLoading: {$set: false}});
        }
        case ADD_COMMENT: {
            return update(store, {commentList: {$push: [action.payload]}});
        }
        default:
            return store;
    }
};

export default reducer;