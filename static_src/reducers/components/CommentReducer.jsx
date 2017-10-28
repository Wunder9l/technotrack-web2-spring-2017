import {
    ERROR_COMMENT_LOADING,
    SUCCESSFUL_COMMENT_LOADING,
    START_COMMENT_LOADING
} from '../../actions/components/Comment';

const initialStore = {
    commentList: [],
    isLoading: false,
};


const reducer = (store = initialStore, action) => {
    console.log(action);
    return store;
    switch (action.type) {
        case START_COMMENT_LOADING:{
            return
        }
    }
};

export default reducer;