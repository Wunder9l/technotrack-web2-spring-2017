import {combineReducers} from 'redux-immutable';
import comments from './components/CommentReducer';

const test = (store, action) => {
    console.log('test:', store, typeof (store));
    return store;
}

export default combineReducers(
    {
        comments,
    });
