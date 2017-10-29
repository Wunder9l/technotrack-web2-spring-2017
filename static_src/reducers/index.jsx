// import {combineReducers} from 'redux-immutable';
import {combineReducers} from 'redux';
// import comments from './components/CommentReducer';
import comments from './components/CommentReducerSimple';

export default combineReducers(
    {
        comments,
    });
