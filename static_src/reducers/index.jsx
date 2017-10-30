import {combineReducers} from 'redux-immutable';
import comments from './components/CommentReducer';

export default combineReducers(
    {
        comments,
    });
