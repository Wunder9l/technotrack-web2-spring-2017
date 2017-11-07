import {Map, List, fromJS} from 'immutable';
import {
    ERROR_COMMENT_LOADING,
    SUCCESSFUL_COMMENT_LOADING,
    START_COMMENT_LOADING,
    ADD_COMMENT,
} from '../../actions/components/CommentAction';

const initialState = Map({
    commentList: List(),
    isLoading: false,
});


const reducer = (store = initialState, action) => {
    // console.log(action, store);
    switch (action.type) {
        case START_COMMENT_LOADING: {
            console.log(store);
            // debugger;
            return store.set('isLoading', true);
        }
        case SUCCESSFUL_COMMENT_LOADING: {
            return store.merge(Map({isLoading: false, commentList: List(action.payload)}));
        }
        case ERROR_COMMENT_LOADING: {
            console.log('ERROR', action);
            return store.set('isLoading', true);
        }
        case ADD_COMMENT: {
            return store.update('commentList', list => list.insert(0, action.payload));
        }
        default:
            return store;
    }
};

export default reducer;